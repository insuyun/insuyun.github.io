---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'From the Vulnerability to the Victory: A Chrome Renderer 1-Day Exploit’s Journey
  to v8CTF Glory'
subtitle: ''
summary: ''
authors:
- Haein Lee
- Insu Yun
tags: []
categories: []
date: '2024-05-01'
lastmod: 2024-07-31T22:41:44+09:00
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
publishDate: '2024-07-31T13:41:44.821846Z'
publication_types:
- '0'
abstract: "In today’s digital era, where the internet has become as essential as the\
  \ air we breathe, the browsers serve as our windows to the vast expanse of the digital\
  \ world. On top of web surfing, browsers extend their capabilities from being integrated\
  \ into embedded systems to supporting desktop apps. Browsers are fascinating targets\
  \ because they are widely used for user interaction, hence browser exploits are\
  \ frequently utilized in exploit chains. Inspired by the big success of kernelCTF,\
  \ Google launched v8CTF to gather exploit techniques in the V8 JavaScript engine\
  \ by rewarding 0day/1day exploits, thereby encouraging security engineers.\n\nIn\
  \ this talk, we will discuss our exploit, which was the second valid submission\
  \ in the history of v8CTF. To achieve this, we utilized a 1-day vulnerability identified\
  \ as CVE-2023-6702. Unlike other vulnerabilities, this one is quite unique. It causes\
  \ a type confusion between a 4-byte hash value and a V8 heap object. This vulnerability,\
  \ which may have been infeasible to exploit in the past, has become exploitable\
  \ due to the recent introduction of pointer compression in V8. To exploit this vulnerability,\
  \ we applied a variety of techniques and successfully achieved a remote code execution\
  \ with nearly a 100% success rate."
publication: '*TyphoonCon 2024*'
url_slides: pubs/2024/lee:v8-ctf-slides.pdf
url_code: https://github.com/kaist-hacking/CVE-2023-6702
---
