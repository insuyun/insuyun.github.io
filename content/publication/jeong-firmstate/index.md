---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'FirmState: Bringing Cellular Protocol States to Shannon Baseband Emulation'
subtitle: ''
summary: ''
authors:
- Suhwan Jeong
- Beomseok Oh
- Kwangmin Kim
- Insu Yun
- Yongdae Kim
- CheolJun Park
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
publishDate: '2025-07-13T11:50:00.767555Z'
publication_types:
- '0'
abstract: "Cellular baseband processors represent critical security components in\
  \ modern\nmobile devices, yet they remain challenging to analyze due to their complexity\n\
  and restricted access. While the FirmWire enables full-system baseband\nemulation,\
  \ it lacks protocol state awareness, limiting its coverage and\nfidelity. While\
  \ implementing such support demands substantial engineering\neffort, accurately\
  \ modeling protocol states remains essential for comprehensive\nbaseband security\
  \ analysis. In this paper, we present FirmState, a state-aware\nmethodology that\
  \ augments baseband emulation, specifically targeting Samsung\nShannon baseband.\
  \ FirmState semiautomatically recovers and applies state\ninformation extracted\
  \ from physical devices during actual network\ncommunication, enabling more complete\
  \ code coverage and authentic behavior\nreproduction without extensive reverse engineering.\
  \ Our evaluation demonstrates\na significant improvement in code coverage, achieving\
  \ 7.5% for RRC–2.7× higher\nthan previous work. Additionally, our system newly supports\
  \ NAS over FirmWire,\nwith code coverage ranging from 4.5% to 9.2%, depending on\
  \ the protocol state.\nUsing our approach, we discovered and analyzed two 1-day\
  \ vulnerabilities in\nSamsung’s baseband implementation, demonstrating FirmState’s\
  \ effectiveness for\nbaseband security. We make FirmState opensource to support\
  \ further research in\nbaseband security.\n"
publication: '*Proceedings of the 18th ACM Conference on Security and Privacy in Wireless
  and Mobile Networks (WiSec)*'
url_slides: pubs/2025/jeong:firmstate-slides.pdf
url_paper: pubs/2025/jeong:firmstate.pdf
---
