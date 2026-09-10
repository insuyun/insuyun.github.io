---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Prism: A Multi-Team Orchestration of LLM Agents for Automatic Program Repair
  (to appear)'
subtitle: ''
summary: ''
authors:
- Yunjae Choi
- Min Woo Baek
- Insu Yun
tags: []
categories: []
date: '2026-10-01'
lastmod: 2026-09-10T18:07:18+09:00
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
publishDate: '2026-09-10T09:07:18.298653Z'
publication_types:
- '0'
abstract: 'Automatic Program Repair (APR) has emerged as a critical technology for
  autonomously addressing software vulnerabilities. While recent advances in Large
  Language Models (LLMs) have enabled sophisticated agentic APR systems, existing
  approaches still struggle to generate patches for vulnerabilities whose root causes
  are difficult to identify. This happens because prior methods (1) merely determine
  patch locations based on given crash reports or (2) employ poorly engineered context,
  which distracts the model and hinders effective reasoning. To address these challenges,
  we present Prism, a multi-team LLM-based APR system. Prism employs a multi-team
  architecture with three specialized teams coordinated through hierarchical context
  management: the Analysis Team systematically explores codebases and synthesizes
  repair strategies, the Patch Team translates strategies into concrete patches with
  pre-execution validation, and the Evaluation Team executes patches and generates
  feedback. To systematically explore codebases, Prism supports progressive code retrieval
  that combines top-down structural exploration with bottom-up, query-driven search.
  We evaluated Prism on 92 real-world vulnerabilities from DARPA’s AI Cyber Challenge
  (AIxCC). Prism successfully fixed 77 bugs (83.7%), outperforming baselines by 27
  to 70 percentage points. Among those, we further analyzed 21 hard-to-localize vulnerabilities
  where fix locations do not appear in stack traces. In these cases, Prism fixed 13
  of 21 bugs (62%), which is 24 to 62 percentage points higher than other baselines.
  These results demonstrate the effectiveness of Prism’s design, which leverages a
  multi-team architecture with strategy-based patch generation and progressive code
  retrieval.'
publication: '*Proceedings of the 2026 International Symposium on Research in Attacks,
  Intrusions and Defenses (RAID)*'
---
