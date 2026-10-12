#!/usr/bin/env python3
"""Render a Seedance prompt to an .mp4 on Token360 (https://www.token360.ai).

Standard library only (Python 3.8+). Reads the API key from the
TOKEN360_API_KEY environment variable; the key is never printed or written.

    export TOKEN360_API_KEY="sk-..."
    python3 scripts/token360_video.py \
        --prompt "Static camera. A ceramic mug on a wooden table, steam rising, morning light." \
        --resolution 480p --duration 4 --out mug.mp4

Flow: POST /v1/videos -> poll GET /v1/videos/{id} -> download the result URL.
Common options map 1:1 to Token360 request fields (model, prompt, duration,
resolution, aspect_ratio, generate_audio, frame_images, input_references).
Docs: https://www.token360.ai/en-US/docs  Models: https://www.token360.ai/en-US/explore
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

DEFAULT_BASE = "https://api.token360.ai/v1"
DONE = {"completed", "succeeded", "success"}
FAILED = {"failed", "error", "cancelled", "canceled", "expired"}


def api(method, url, key, body=None, timeout=120):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json",
        "User-Agent": "seedance-prompt-skill/token360_video.py",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.headers.get("X-Request-ID"), json.loads(resp.read() or b"{}")
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            payload = json.loads(raw)
        except ValueError:
            payload = {"raw": raw[:500].decode("utf-8", "replace")}
        return e.code, e.headers.get("X-Request-ID"), payload


def result_url(job):
    for src in (job, job.get("content") or {}, job.get("data") or {}):
        if isinstance(src, dict):
            for k in ("video_url", "url"):
                if src.get(k):
                    return src[k]
    return None


def main():
    p = argparse.ArgumentParser(description="Render a Seedance prompt on Token360 and save the .mp4.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--prompt", help="prompt text")
    g.add_argument("--prompt-file", help="read the prompt from a UTF-8 text file")
    p.add_argument("--model", default=os.environ.get("TOKEN360_VIDEO_MODEL", "seedance-2.5"),
                   help="seedance-2.5 (default), seedance-2.0, seedance-2.0-fast, seedance-2.0-mini, ...")
    p.add_argument("--duration", type=int, default=5, help="seconds (Seedance 2.5: 4-30; 2.0: 4-15)")
    p.add_argument("--resolution", default="720p", help="480p | 720p | 1080p (model-dependent)")
    p.add_argument("--aspect-ratio", default="16:9", help="16:9 | 9:16 | 1:1 | 4:3 | 3:4 | 21:9 | adaptive")
    p.add_argument("--no-audio", action="store_true", help="disable generated audio (default: audio on)")
    p.add_argument("--first-frame", metavar="URL", help="public image URL used as the first frame")
    p.add_argument("--ref-image", metavar="URL", action="append", default=[],
                   help="public image URL sent as an input reference (repeatable)")
    p.add_argument("--extra", metavar="JSON", help='extra request fields, e.g. \'{"seed": 7}\'')
    p.add_argument("--out", default="seedance.mp4", help="output file (default: seedance.mp4)")
    p.add_argument("--poll", type=int, default=10, help="poll interval in seconds")
    p.add_argument("--timeout", type=int, default=1800, help="give up after N seconds")
    a = p.parse_args()

    key = os.environ.get("TOKEN360_API_KEY")
    if not key:
        sys.exit("Set TOKEN360_API_KEY first (get a key: https://www.token360.ai/en-US/sign-up"
                 "?utm_source=github&utm_medium=fork&utm_campaign=seedance-prompt-skill)")
    base = os.environ.get("TOKEN360_BASE_URL", DEFAULT_BASE).rstrip("/")

    prompt = a.prompt if a.prompt is not None else open(a.prompt_file, encoding="utf-8").read().strip()
    body = {"model": a.model, "prompt": prompt, "duration": a.duration, "resolution": a.resolution,
            "aspect_ratio": a.aspect_ratio, "generate_audio": not a.no_audio, "watermark": False}
    if a.first_frame:
        body["frame_images"] = [{"type": "image_url", "frame_type": "first_frame",
                                 "image_url": {"url": a.first_frame}}]
    if a.ref_image:
        body["input_references"] = [{"type": "image_url", "image_url": {"url": u}} for u in a.ref_image]
    if a.extra:
        body.update(json.loads(a.extra))

    status, req_id, job = api("POST", base + "/videos", key, body)
    if status >= 300:
        sys.exit("submit failed: HTTP %s request_id=%s %s" % (status, req_id, json.dumps(job)[:600]))
    vid = job.get("id")
    print("submitted %s model=%s request_id=%s" % (vid, a.model, req_id), file=sys.stderr)

    start = time.time()
    while True:
        status, _, job = api("GET", "%s/videos/%s" % (base, vid), key)
        state = str(job.get("status", "")).lower()
        if status >= 300:
            sys.exit("poll failed: HTTP %s %s" % (status, json.dumps(job)[:600]))
        if state in DONE:
            break
        if state in FAILED:
            sys.exit("generation failed: %s" % json.dumps(job.get("error") or job)[:800])
        if time.time() - start > a.timeout:
            sys.exit("timed out after %ss (last status: %s); job id %s" % (a.timeout, state, vid))
        print("  %s ... %ds" % (state or "pending", time.time() - start), file=sys.stderr)
        time.sleep(a.poll)

    url = result_url(job)
    if not url:
        sys.exit("completed but no video URL in response: %s" % json.dumps(job)[:600])
    with urllib.request.urlopen(url, timeout=600) as r, open(a.out, "wb") as f:
        f.write(r.read())
    usage = job.get("usage") or {}
    print(json.dumps({"ok": True, "file": a.out, "id": vid, "request_id": req_id, "model": a.model,
                      "duration": job.get("duration"), "resolution": job.get("resolution"),
                      "usage": usage}))


if __name__ == "__main__":
    main()
