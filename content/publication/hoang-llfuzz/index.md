---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'LLFuzz: An Over-the-Air Dynamic Testing Framework for Cellular Baseband Lower
  Layers'
subtitle: ''
summary: ''
authors:
- Tuan Dinh Hoang
- Taekkyung Oh
- CheolJun Park
- Insu Yun
- Yongdae Kim
tags: []
categories: []
date: '2025-08-01'
lastmod: 2025-10-01T16:37:52+09:00
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
publishDate: '2025-10-01T07:37:52.077508Z'
publication_types:
- '0'
abstract: "Memory corruptions in cellular basebands are critical because they can\
  \ be\nremotely exploited over-the-air, resulting in severe consequences such as\n\
  remote code execution, denial of service, and information leakage. While\nprevious\
  \ research has made significant contributions to detecting memory\ncorruptions in\
  \ basebands, particularly in layer 3 protocols (e.g., NAS and\nRRC), the lower layers\
  \ have received comparatively less attention, with only a\nfew works exploring them\
  \ in a limited and non-systematic manner.\n\nIn this paper, we present Lower-Layer\
  \ Fuzzer (LLFUZZ), a novel over-the-air\ndynamic testing framework that discovers\
  \ memory corruptions in baseband lower\nlayers. LLFUZZ systematically targets lower\
  \ layers, which are the PDCP, RLC,\nMAC, and PHY layers of the cellular stack. Testing\
  \ these layers presents unique\nchallenges due to their multiple channels and packet\
  \ structures that can be\ndynamically configurable. To address these complexities,\
  \ LLFUZZ implements a\nchannel-driven, configuration-aware fuzzing approach to systematically\
  \ explore\nmultiple channels. During the testing process, LLFUZZ actively modifies\n\
  layer-specific configurations through signaling messages to trigger and test\ndiverse\
  \ packet structures, particularly those rarely used in commercial\nnetworks. Moreover,\
  \ LLFUZZ leverages 3GPP specifications to generate test cases\ntailored to the packet\
  \ structures of the lower layers. This ensures that the\ntest cases are syntactically\
  \ valid and capable of reaching the target layers\nwithout being prematurely discarded.\
  \ In our evaluation of 15 commercial\nbasebands from five major vendors, LLFUZZ\
  \ uncovered nine previously unknown\nmemory corruptions: two in PDCP, two in RLC,\
  \ and five in MAC layers. These\nfindings demonstrate LLFUZZ’s effectiveness in\
  \ finding critical memory\ncorruptions in baseband lower layers\n\n"
publication: '*Proceedings of the 34th USENIX Security Symposium (Security)*'
url_slides: pubs/2025/hoang:llfuzz-slides.pdf
url_paper: pubs/2025/hoang:llfuzz.pdf
---
