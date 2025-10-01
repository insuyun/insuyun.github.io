Memory corruptions in cellular basebands are critical because they can be
remotely exploited over-the-air, resulting in severe consequences such as
remote code execution, denial of service, and information leakage. While
previous research has made significant contributions to detecting memory
corruptions in basebands, particularly in layer 3 protocols (e.g., NAS and
RRC), the lower layers have received comparatively less attention, with only a
few works exploring them in a limited and non-systematic manner.

In this paper, we present Lower-Layer Fuzzer (LLFUZZ), a novel over-the-air
dynamic testing framework that discovers memory corruptions in baseband lower
layers. LLFUZZ systematically targets lower layers, which are the PDCP, RLC,
MAC, and PHY layers of the cellular stack. Testing these layers presents unique
challenges due to their multiple channels and packet structures that can be
dynamically configurable. To address these complexities, LLFUZZ implements a
channel-driven, configuration-aware fuzzing approach to systematically explore
multiple channels. During the testing process, LLFUZZ actively modifies
layer-specific configurations through signaling messages to trigger and test
diverse packet structures, particularly those rarely used in commercial
networks. Moreover, LLFUZZ leverages 3GPP specifications to generate test cases
tailored to the packet structures of the lower layers. This ensures that the
test cases are syntactically valid and capable of reaching the target layers
without being prematurely discarded. In our evaluation of 15 commercial
basebands from five major vendors, LLFUZZ uncovered nine previously unknown
memory corruptions: two in PDCP, two in RLC, and five in MAC layers. These
findings demonstrate LLFUZZ’s effectiveness in finding critical memory
corruptions in baseband lower layers

