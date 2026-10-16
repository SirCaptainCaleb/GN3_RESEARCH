# Balanced six-cube without complementary direction pairs

- Stable ID: note_nori_balanced_nonpaired_q6_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:odd_girth_and_frustration_of_switch_component_quotients
- Labels: balanced-cube, negative-certificate, square-trade
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

In a vertex-balanced antipodally odd Q_{2m}, signs s_i=(-1)^{c_i} satisfy sum_i s_i=0 and s_i ignores bit i. For every odd Walsh set S, sum_{i outside S} Fourier(s_i,S)=0. Taking S=[2m] minus {i} shows the top odd coefficient of each s_i vanishes. On Q4, s_i therefore is a signed one-bit character, and balance forces complementary pairs of direction functions.

This pairing conclusion fails on Q6. Use bit indices 0,...,5. Begin with (c0,c1,c2,c3,c4,c5)=(x2,1-x2,x4,1-x4,x0,1-x0). Invert the four edge colors on the square in directions (0,3) with remaining bits (x1,x2,x4,x5)=(0,0,0,0), and invert all four antipodal edges. Then invert the square in directions (1,4) with remaining bits (x0,x2,x3,x5)=(0,0,1,0), again with its antipodal square. Each square initially has opposite colors on its two directions, so these paired alternating-square trades preserve vertex balance and antipodal oddness. After both trades every pair ij of direction functions agrees at a witness vertex x (integer encoding sum 2^k x_k). For ij=01,02,03,04,05,12,13,14,15,23,24,25,34,35,45, corresponding x=0,2,4,1,0,4,2,1,0,0,0,1,0,1,8. Therefore no c_i and c_j are pointwise complements. This refutes any unrestricted implication from balance to a paired-direction partition, though a separate counterexample-preserving paired-direction lift remains valid.
