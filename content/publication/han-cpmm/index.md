---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Automated Attack Synthesis for Constant Product Market Makers
subtitle: ''
summary: ''
authors:
- Sujin Han
- Jinseo Kim
- Sung-Ju Lee
- Insu Yun
tags: []
categories: []
date: '2025-06-01'
lastmod: 2025-07-13T20:50:00+09:00
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
publishDate: '2025-07-13T11:50:00.869040Z'
publication_types:
- '0'
abstract: "Decentralized Finance (DeFi) enables many novel applications that were\
  \ impossible in traditional finances. However, it also introduces new types of vulnerabilities.\
  \ An example of such vulnerabilities is a composability bug between token contracts\
  \ and Decentralized Exchange (DEX) that follows the Constant Product Market Maker\
  \ (CPMM) model. This type of bug, which we refer to as CPMM composability bug, originates\
  \ from issues in token contracts that make them incompatible with CPMMs, thereby\
  \ endangering other tokens within the CPMM ecosystem. Since 2022, 23 exploits of\
  \ such kind have resulted in a total loss of 2.2M USD. BlockSec, a smart contract\
  \ auditing company, reported that 138 exploits of such kind occurred just in February\
  \ 2023.\n\nIn this paper, we propose CPMMX , a tool that automatically detects CPMM\
  \ composability bugs across\nentire blockchains. To achieve such scalability, we\
  \ first formalized CPMM composability bugs and found that these bugs can be induced\
  \ by breaking two safety invariants. Based on this finding, we designed CPMMX equipped\
  \ with a two-step approach, called shallow-then-deep search. In more detail, it\
  \ first uses shallow search to find transactions that break the invariants. Then,\
  \ it uses deep search to refine these transactions, making them profitable for the\
  \ attacker. We evaluated CPMMX against five baselines on two public datasets and\
  \ one synthetic dataset. In our evaluation, CPMMX detected 2.5x to 1.5x more vulnerabilities\
  \ compared to baseline methods. It also analyzed contracts significantly faster,\
  \ achieving higher F1 scores than the baselines. Additionally, we applied CPMMX\
  \ to all contracts on the latest blocks of the Ethereum and Binance networks and\
  \ discovered 26 new exploits that can result in 15.7K USD profit in total."
publication: '*Proceedings of the ACM SIGSOFT International Symposium on Software
  Testing and Analysis (ISSTA) 2025*'
url_slides: pubs/2025/han:cpmm-slides.pdf
url_paper: pubs/2025/han:cpmm.pdf
---
