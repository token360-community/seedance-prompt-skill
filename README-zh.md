![Seedance Prompt Skill · Token360 版](assets/token360-header.webp)

# Seedance 2.0 视频提示词撰写技能 · Token360 版

[English](README.md)

> [!NOTE]
> **本仓库 fork 自 [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)，原作者 [Dex（dexhunter）](https://github.com/dexhunter)，MIT 许可。原项目的全部功劳归原作者所有。**
>
> 技能文件、提示词模式与模板均出自原作者及[全体贡献者](https://github.com/dexhunter/seedance2-skill/graphs/contributors)。Token360 版只增加了可选的「在 Token360 上渲染」步骤：一个视频生成脚本、快速上手、Seedance 2.5 说明、新的头图与缩略图，以及用 Token360 生成的示例视频。本仓库与原作者无隶属或背书关系。原 [LICENSE](LICENSE) 与版权声明（Copyright (c) 2026 Dex）保持不变，全部改动见 [NOTICE](NOTICE)。欢迎给[原项目](https://github.com/dexhunter/seedance2-skill)点 ⭐，与 Token360 无关的改进请直接提交到上游。
>
> **与字节跳动无关。** Seedance、即梦、Dreamina 是字节跳动的产品与商标。本技能内容整理自字节跳动公开的 Seedance 2.0 使用手册与实测案例（见[资料来源](#资料来源)）；本 fork 与字节跳动无隶属、赞助或背书关系。

## ⚡ Token360 快速上手

先用技能写好提示词，再通过 Token360 的 OpenAI 兼容 API 用 Seedance 2.5 渲染。需要 Python 3.8+，只用标准库。

1. 注册并创建 API Key：[token360.ai 注册](https://www.token360.ai/en-US/sign-up?utm_source=github&utm_medium=fork&utm_campaign=seedance-prompt-skill)
2. 渲染一段视频：

```bash
export TOKEN360_API_KEY="sk-..."                         # 你的 Key（不要提交到仓库）
export TOKEN360_BASE_URL="https://api.token360.ai/v1"    # 默认值，写出来便于理解
python3 scripts/token360_video.py --model seedance-2.5 \
  --prompt "Static camera. A sage-green ceramic mug on a wooden table, steam curling up in soft morning light, dust motes drifting. Calm ambient music." \
  --resolution 480p --duration 4 --out mug.mp4
# → {"ok": true, "file": "mug.mp4", ...}   （通常 2–5 分钟；实测这段 4 秒 480p 视频花费 $0.54）
```

脚本调用 `POST /v1/videos`，轮询 `GET /v1/videos/{id}` 并下载结果。可用 `--resolution 720p|1080p`、`--duration 4-30`、`--aspect-ratio 9:16`、`--no-audio`、`--first-frame <图片 URL>`、`--ref-image <图片 URL>`，或 `--model seedance-2.0 | seedance-2.0-fast | seedance-2.0-mini`。详见 `python3 scripts/token360_video.py -h`、[全部视频模型与价格](https://www.token360.ai/en-US/explore?utm_source=github&utm_medium=fork&utm_campaign=seedance-prompt-skill)和[文档](https://www.token360.ai/en-US/docs?utm_source=github&utm_medium=fork&utm_campaign=seedance-prompt-skill)。若任务因 `content_policy_violation`（"generated audio may violate copyright restrictions"）失败，重试一次或加 `--no-audio` 即可；我们测试中同一 prompt 重试即通过，失败任务未计费。技能本身与平台无关：写出的提示词照样可以用在即梦 / Dreamina 或其他 Seedance 服务商。

## 🎬 Made with Token360

用本技能的提示词模式编写、在 **Token360 上用 Seedance 2.5** 渲染的 4 段 5 秒视频（产品广告、对白、科普、一镜到底）。点击预览打开带声音的 mp4；prompt 与费用见 [examples/token360-samples](examples/token360-samples/README.md)。

| 产品广告（§9） | 对白配音（§7） |
|---|---|
| <a href="examples/token360-samples/product-ad.mp4"><img src="examples/token360-samples/product-ad.gif" width="380" alt="产品广告"></a> | <a href="examples/token360-samples/dialogue-comedy.mp4"><img src="examples/token360-samples/dialogue-comedy.gif" width="380" alt="对白"></a> |
| **科普教育（§10）** | **一镜到底（§8）** |
| <a href="examples/token360-samples/science-edu.mp4"><img src="examples/token360-samples/science-edu.gif" width="380" alt="科普"></a> | <a href="examples/token360-samples/one-take.mp4"><img src="examples/token360-samples/one-take.gif" width="380" alt="一镜到底"></a> |

<img src="assets/thumbnail-token360.jpg" width="380" alt="Seedance 2.0 视频提示词撰写技能缩略图"><br>
<sub>仓库缩略图：在 Token360 上用 <code>gpt-image-2</code> 按仓库自带的<a href="assets/thumbnail-prompt.txt">缩略图提示词</a>重新生成（文字为后期叠加，非模型渲染）。</sub>

为[即梦 Seedance 2.0](https://jimeng.jianying.com/) 多模态 AI 视频生成模型打造的 [Agent Skills](https://agentskills.io) 提示词撰写技能。支持 Claude Code、Cursor、Cline 等兼容的 AI 代理。

涵盖输入约束、@ 引用语法、运镜语言、提示词结构模式，以及广告、短剧、MV、科普教育等场景的现成模版。

## 安装

### 方式 A：手动复制（推荐）

克隆或下载本仓库，然后将技能文件复制到 Claude skills 目录：

```bash
mkdir -p ~/.claude/skills

# 中文版
cp zh/SKILL.md ~/.claude/skills/seedance-prompt-zh.md

# 英文版
cp SKILL.md ~/.claude/skills/seedance-prompt-en.md
```

### 方式 B：通过 skills CLI

```bash
npx skills add token360-community/seedance-prompt-skill
```

然后让你的 AI 代理帮你撰写 Seedance 2.0 视频提示词即可。

## 技能文件

| 文件 | 语言 | 说明 |
|---|---|---|
| [SKILL.md](SKILL.md) | English | Prompt writing guide for Seedance 2.0 |
| [zh/SKILL.md](zh/SKILL.md) | 中文 | Seedance 2.0 提示词撰写指南 |
| [scripts/token360_video.py](scripts/token360_video.py) | — | Token360 版新增：可选脚本，在 Token360 上用 Seedance 渲染提示词 |

## 资料来源

基于字节跳动官方文档整理：

- [即梦 Seedance 2.0 使用手册](https://bytedance.larkoffice.com/wiki/A5RHwWhoBiOnjukIIw6cu5ybnXQ) — 参数说明、交互方式、多模态能力与示例提示词
- [小云雀 Seedance 2.0 实测案例](https://bytedance.larkoffice.com/wiki/LJXzwehluiFdzKkb1recZdfonZg) — 剧情制作、电商广告、舞蹈模仿、科普教学、AI MV 等场景

## 与上游的差异（Token360 版）

- 新增 `scripts/token360_video.py`、Token360 快速上手、`.env.example` 与 `examples/token360-samples/` 示例视频
- 在 `SKILL.md` 与 `zh/SKILL.md` 末尾新增可选的「在 Token360 上渲染」小节与 Seedance 2.5 说明；原指南内容未改动
- 更换头图：移除原 `assets/seedance2-thumbnail.png`；`assets/thumbnail-token360.jpg` 由 Token360 按仓库自带的 `assets/thumbnail-prompt.txt` 重新生成（文字相关指令改为「不渲染文字」，见 `assets/thumbnail-prompt-token360.txt`，标题为后期叠加）
- 完整清单见 [NOTICE](NOTICE)

## 许可证

[MIT](LICENSE)。保留原版权声明；Token360 版改动见 [NOTICE](NOTICE)。
