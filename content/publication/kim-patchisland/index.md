---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'PatchIsland: Orchestration of LLM Agents for Continuous Vulnerability Repair
  (to appear)'
subtitle: ''
summary: ''
authors:
- Wonyoung Kim
- Seunggi Min
- Minjae Gwon
- Haein Lee
- Dowoo Baik
- Hyeon Heo
- Minjae Lee
- Min Woo Baek
- Yonghwi Jin
- Younggi Park
- Yunjae Choi
- Taesoo Kim
- Sangdon Park
- Insu Yun
tags: []
categories: []
date: '2026-12-01'
lastmod: 2026-09-16T20:15:09+09:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2026-09-16T11:15:09.568629Z'
publication_types:
- '0'
abstract: "Continuous fuzzing platforms such as OSS-Fuzz uncover large numbers of\
  \ vulnerabilities, yet the subsequent repair process remains largely manual. Unfortunately,\
  \ existing Automated Vulnerability Repair (AVR) techniques---including recent LLM-based\
  \ systems---are not directly applicable to continuous fuzzing. This is because these\
  \ systems are designed and evaluated on a static, single-run benchmark setting,\
  \ making them ill-suited for the diverse, noisy, and failure-prone environments\
  \ in continuous fuzzing.\n\nTo address these issues, we introduce PatchIsland, a\
  \ system for Continuous Vulnerability Repair (CVR) that tightly integrates with\
  \ continuous fuzzing pipelines. Our key idea for PatchIsland is to employ an ensemble\
  \ of diverse LLM agents. By leveraging multiple LLM agents, PatchIsland can cover\
  \ a wider range of settings (e.g., different projects, bug types, and programming\
  \ languages) and also improve operational robustness. In addition, PatchIsland utilizes\
  \ a two-phase deduplication to mitigate duplicate crashes and patches, which can\
  \ be problematic in continuous fuzzing. \n\nWe evaluate PatchIsland in both internal\
  \ and external settings. In our internal evaluation, PatchIsland successfully repaired\
  \ 84 of 92 vulnerabilities, outperforming state-of-the-art CVR systems. We also\
  \ applied PatchIsland in the official AIxCC final. During this competition, PatchIsland\
  \ patched 31 of 43 vulnerabilities while operating fully autonomously for more than\
  \ a week. This result represents the largest number of patches and the second-highest\
  \ repair rate (72.1%) among participating systems. More surprisingly, PatchIsland\
  \ could produce a zero-day patch that exactly matched with the official one. This\
  \ shows that PatchIsland can be a practical solution for real-world CVR."
publication: '*Proceedings of the 42nd Annual Computer Security Applications Conference
  (ACSAC)*'
author_notes:
- Equal contribution
- Equal contribution
---
