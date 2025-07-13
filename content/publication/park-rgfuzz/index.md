---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'RGFuzz: Rule-Guided Fuzzer for WebAssembly Runtimes'
subtitle: ''
summary: ''
authors:
- Junyoung Park
- Yunho Kim
- Insu Yun
tags: []
categories: []
date: '2025-05-01'
lastmod: 2025-07-13T20:50:01+09:00
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
publishDate: '2025-07-13T11:50:01.066067Z'
publication_types:
- '0'
abstract: "WebAssembly runtimes embed compilers to compile WebAssembly code into machine\
  \ code for execution. These compilers use various compiler rules to define how to\
  \ optimize and lower the WebAssembly code. However, existing testing tools struggle\
  \ to explore these rules effectively due to their complexity. Moreover, they cannot\
  \ generate test cases diversely due to their limitations, which can result in undetected\
  \ bugs.\n\nThis paper presents RGFuzz, a differential fuzzer for WebAssembly runtimes,\
  \ addressing the existing limitations through two novel techniques. First, RGFuzz\
  \ uses rule-guided fuzzing, which extracts compiler rules from the WebAssembly runtime,\
  \ wasmtime, and uses them to guide test case generation, thereby effectively exploring\
  \ complex rules. Second, RGFuzz uses reverse stack-based generation to generate\
  \ test cases diversely. These techniques enable RGFuzz to find bugs effectively\
  \ in WebAssembly runtimes. We implemented RGFuzz and evaluated it on six engines:\
  \ wasmtime, Wasmer, WasmEdge, V8, SpiderMonkey, and JavaScriptCore. As a result,\
  \ RGFuzz found 20 new bugs in these engines, including one bug with a CVE ID issued.\
  \ Our evaluation demonstrates that RGFuzz outperforms existing fuzzers by utilizing\
  \ the extracted rules and diversely generating test cases."
publication: '*Proceedings of the 46th IEEE Symposium on Security and Privacy (Oakland)*'
url_slides: pubs/2025/park:rgfuzz-slides.pdf
url_paper: pubs/2025/park:rgfuzz.pdf
url_code: https://github.com/kaist-hacking/RGFuzz
---
