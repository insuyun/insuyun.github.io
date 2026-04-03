---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Windows plays Jenga: Uncovering Design Weaknesses in Windows File System Security'
subtitle: ''
summary: ''
authors:
- Dong-uk Kim
- Junyoung Park
- Sanghak Oh
- Hyoungshick Kim
- Insu Yun
tags: []
categories: []
date: '2025-10-01'
lastmod: 2026-04-03T15:58:16+09:00
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
publishDate: '2026-04-03T06:58:16.089444Z'
publication_types:
- '0'
abstract: "File systems are essential components of modern operating systems, with\
  \ Windows being one of the most dominant platforms. Recently, a series of attacks\
  \ have exploited the Windows file system to trigger serious security threats such\
  \ as privilege escalation. Over the past several years, dozens of such attacks have\
  \ been reported and even exploited in the wild. However, Microsoft has consistently\
  \ addressed these issues with targeted patches rather than fundamental redesigns\
  \ — resembling a precarious game of Jenga where security measures are stacked upon\
  \ an unstable foundation. In this paper, we present a five-step comprehensive analysis\
  \ of the Windows file system's design weaknesses. First, we analyze how Windows\
  \ differs from another operating system, Linux. Second, we investigated how these\
  \ discrepancies lead to security vulnerabilities in real-world applications and\
  \ identified 13 high-impact vulnerabilities, including 11 previously unknown ones.\
  \ Third, we show that current compatibility layers in modern programming languages\
  \ fail to handle these discrepancies properly. Specifically, we examined compatibility\
  \ layers in six programming languages and found 27 non-compliant and 9 inconsistencies,\
  \ rendering these layers unreliable. Fourth, through a user study involving 21 experienced\
  \ developers, we found that most were unfamiliar with OS-level file system discrepancies\
  \ and rarely implemented appropriate mitigations. Finally, we analyze existing countermeasures\
  \ and discuss their limitations. Our findings reveal critical yet largely obscured\
  \ security risks resulting from design flaws in the Windows file system. Furthermore,\
  \ we suggest that Microsoft rethink its strategy and address these fundamental weaknesses.\n"
publication: '*Proceedings of the 32nd ACM Conference on Computer and Communications
  Security (CCS)*'
url_slides: pubs/2025/kim:jenga-slides.pdf
url_paper: pubs/2025/kim:jenga.pdf
author_notes:
- Equal contribution
- Equal contribution
---
