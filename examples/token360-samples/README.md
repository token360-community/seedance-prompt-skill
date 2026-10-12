# Made with Token360 · sample clips

Four short clips rendered on **2026-10-11** with **Seedance 2.5 on [Token360](https://www.token360.ai/en-US/explore?utm_source=github&utm_medium=fork&utm_campaign=seedance-prompt-skill)**, each from a prompt written with the patterns in [SKILL.md](../../SKILL.md). Original generations; no upstream or third-party footage was used. Click a GIF for the mp4 (with sound).

本目录的 4 段视频均于 2026-10-11 用 Token360 上的 Seedance 2.5 生成，prompt 按 [SKILL.md](../../SKILL.md) 中的模式编写；均为原创生成，未使用任何上游或第三方素材。点击 GIF 可打开带声音的 mp4。

Run this low-cost smoke test from the repository root with `TOKEN360_API_KEY` set. To reproduce a sample, save its prompt below to `my-prompt.txt` and use the recorded 5 s / 720p settings with [`scripts/token360_video.py`](../../scripts/token360_video.py):

```bash
printf '%s\n' 'Static camera. A ceramic mug on a wooden table, steam rising in morning light.' > my-prompt.txt
python3 scripts/token360_video.py --prompt-file my-prompt.txt --duration 4 --resolution 480p --aspect-ratio 16:9 --out clip.mp4
```

### Product ad · `product-ad`

<a href="product-ad.mp4"><img src="product-ad.gif" width="400" alt="Product ad"></a>

- Pattern: SKILL.md §9 E-commerce / Product Showcase
- Request: `seedance-2.5`, 5 s, 720p, 16:9, `generate_audio: true`, `watermark: false`
- Billed: 108,900 output tokens × $13.8565/M = **$1.509**
- Files: [product-ad.mp4](product-ad.mp4) (re-encoded to 854x480 H.264 + AAC for the repo) · [product-ad.gif](product-ad.gif) (400 px, 8 fps, silent preview)

```text
Static camera. A deluxe double cheeseburger suspended and rotating slowly mid-air against a warm dark studio backdrop. Ingredients gently and precisely separate while maintaining shape and proportion: golden sesame bun top, fresh green lettuce, dewy red tomato slices, two thick juicy beef patties with melting golden cheddar, soft bun base. They hover apart, then slowly descend and perfectly reassemble into the complete burger. Cheese keeps melting and dripping slowly, dewdrops glisten on lettuce and tomato. Smooth motion, no extra effects. Cinematic food commercial, shallow depth of field. Sound: soft whoosh as layers separate, gentle sizzle, subtle upbeat background music.
```

### Dialogue / voice acting · `dialogue-comedy`

<a href="dialogue-comedy.mp4"><img src="dialogue-comedy.gif" width="400" alt="Dialogue / voice acting"></a>

- Pattern: SKILL.md §7 Dialogue and Voice Acting
- Request: `seedance-2.5`, 5 s, 720p, 16:9, `generate_audio: true`, `watermark: false`
- Billed: 108,900 output tokens × $13.8565/M = **$1.509**
- Files: [dialogue-comedy.mp4](dialogue-comedy.mp4) (re-encoded to 854x480 H.264 + AAC for the repo) · [dialogue-comedy.gif](dialogue-comedy.gif) (400 px, 8 fps, silent preview)

```text
Animated 3D cartoon comedy segment, "Cat & Dog Roast Show", two pet hosts sitting behind a small talk-show desk with warm stage lights. Cat host (licking paw, rolling eyes): "Who understands my suffering? This one next to me does nothing but wag his tail." Dog host (head tilted, tail wagging, grinning): "You're one to talk? You sleep eighteen hours a day!" Medium shot, gentle push in, exaggerated comedic expressions, playful studio audience laughter, light jazzy background music. Pixar-like stylized animation, no realistic humans.
```

### Science / education · `science-edu`

<a href="science-edu.mp4"><img src="science-edu.gif" width="400" alt="Science / education"></a>

- Pattern: SKILL.md §10 Science/Educational Content
- Request: `seedance-2.5`, 5 s, 720p, 16:9, `generate_audio: true`, `watermark: false`
- Billed: 108,900 output tokens × $13.8565/M = **$1.509**
- Files: [science-edu.mp4](science-edu.mp4) (re-encoded to 854x480 H.264 + AAC for the repo) · [science-edu.gif](science-edu.gif) (400 px, 8 fps, silent preview)

```text
Health educational clip, 4K medical CGI, semi-transparent visualization. 0-2s: transparent blue human upper body, camera slowly pushes into a clear artery, blood flows smoothly in clean blue tones. 2-4s: symbolic sugar and fat particles enter the bloodstream, camera follows the blood flow, yellowish lipid deposits begin forming on the vessel walls. 4-5s: the vessel lumen visibly narrows and flow slows, colors darken for contrast. Documentary tone, calm ambient synth music, soft heartbeat sound.
```

### One-take / long take · `one-take`

<a href="one-take.mp4"><img src="one-take.gif" width="400" alt="One-take / long take"></a>

- Pattern: SKILL.md §8 One-Take / Long Take
- Request: `seedance-2.5`, 5 s, 720p, 16:9, `generate_audio: true`, `watermark: false`
- Billed: 108,900 output tokens × $13.8565/M = **$1.509**
- Files: [one-take.mp4](one-take.mp4) (re-encoded to 854x480 H.264 + AAC for the repo) · [one-take.gif](one-take.gif) (400 px, 8 fps, silent preview)

```text
One-take tracking shot, no cuts: following a runner in a bright orange jacket from behind as she jogs along a rain-wet city street at dawn, up a flight of concrete stairs, through a short corridor and out onto a rooftop, the camera rising as she stops at the edge overlooking the city skyline in golden sunrise light. Smooth gimbal motion, cinematic quality, shallow depth of field, cool-warm contrast. Sound: footsteps, distant traffic, rising ambient music.
```

Total for the four clips: **$6.04** (4 × $1.509).
