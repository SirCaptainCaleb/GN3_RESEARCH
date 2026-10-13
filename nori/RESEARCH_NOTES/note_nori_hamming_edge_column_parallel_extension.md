# Resource-label matroid versus edge-column parallel extension

- Stable ID: note_nori_hamming_edge_column_parallel_extension
- Author: unspecified; session provenance retained
- Primary home: subsection:polarized_hamming_turn_geometry_and_a_single_quantitative_nori1_equivalence
- Labels: ground-set, resource-matroid, proof-clarification
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_3
- Updated session: session_nori_r7130_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

In the Hamming root graph \(G=\square_i K_{E_i}\), the resource matroid \(N=\oplus_i M(K_{E_i})\) has ground set of distinct factorwise symbol-pair labels \((i,\{a,b\})\). Different edges of \(G\) may share one label, so the terminal extension theorem's matroid on \(E(G)\) is the canonical **parallel extension** \(\widehat N\): each graph edge receives its vector \(\pm(e_b-e_a)\) in the corresponding factor. Each vertex star contains distinct resource labels forming an \(N\)-basis and hence an independent set of \(\widehat N\). Every graph cycle is \(\widehat N\)-dependent because its oriented edge differences telescope. An edge sequence is independent in \(\widehat N\) if and only if its multiset of resource labels has no repetition and is independent in \(N\). All rank-growth and vertex-simplicity claims in the polarized Hamming Subsection use \(\widehat N\) on graph edges and \(N\) on resource labels. This makes the matroid ground sets explicit without changing any bound or hypothesis.
