---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'CTFusion: A CTF-based Benchmark for LLM Agent Evaluation'
subtitle: ''
summary: ''
authors:
- Dongjun Lee
- Ga-eun Bae
- Insu Yun
tags: []
categories: []
date: '2026-07-01'
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
publishDate: '2026-09-10T09:07:18.424023Z'
publication_types:
- '0'
abstract: "Recent advances in Large Language Models (LLMs) have enabled agentic systems\
  \ for complex, multi-step tasks; cybersecurity is emerging as a prominent application.\
  \ To evaluate such agents, researchers widely adopt Capture The Flag (CTF) benchmarks.\
  \ However, current CTF benchmarks reuse existing challenges, which exposes them\
  \ to data contamination and potential cheating. Notably, we confirmed these issues\
  \ in practice by integrating web search tools into an existing agent. To address\
  \ these limitations, we present CTFusion, a streaming evaluation framework built\
  \ on Live CTFs. To achieve this, CTFusion preserves per-agent independence under\
  \ a single team account and reduces competition impact by forwarding only the first\
  \ correct flag per challenge. Moreover, we implement CTFusion as a Model Context\
  \ Protocol (MCP) server on the widely used CTFd platform, which offers broad applicability\
  \ to diverse CTF events and agent types. Through experiments with three LLMs, two\
  \ agents, and five Live CTFs, we demonstrate that existing CTF benchmarks can be\
  \ unreliable in assessing LLM-based agents, while CTFusion can serve as a robust\
  \ solution for evaluating cybersecurity agents. We release CTFusion as open source\
  \ to foster future research in this area.\n"
publication: '*Proceedings of the Second Workshop on Agents in the Wild: Safety, Security,
  and Beyond (ICML AIWILD)*'
url_paper: pubs/2026/lee:ctfusion.pdf
---
