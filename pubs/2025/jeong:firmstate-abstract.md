Cellular baseband processors represent critical security components in modern
mobile devices, yet they remain challenging to analyze due to their complexity
and restricted access. While the FirmWire enables full-system baseband
emulation, it lacks protocol state awareness, limiting its coverage and
fidelity. While implementing such support demands substantial engineering
effort, accurately modeling protocol states remains essential for comprehensive
baseband security analysis. In this paper, we present FirmState, a state-aware
methodology that augments baseband emulation, specifically targeting Samsung
Shannon baseband. FirmState semiautomatically recovers and applies state
information extracted from physical devices during actual network
communication, enabling more complete code coverage and authentic behavior
reproduction without extensive reverse engineering. Our evaluation demonstrates
a significant improvement in code coverage, achieving 7.5% for RRC–2.7× higher
than previous work. Additionally, our system newly supports NAS over FirmWire,
with code coverage ranging from 4.5% to 9.2%, depending on the protocol state.
Using our approach, we discovered and analyzed two 1-day vulnerabilities in
Samsung’s baseband implementation, demonstrating FirmState’s effectiveness for
baseband security. We make FirmState opensource to support further research in
baseband security.
