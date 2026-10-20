# Strict bad-root local maximum of complete arm-pair polynomial in Q6

- Stable ID: note_nori_strict_lex_arm_polynomial_local_trap_20261019_r11913
- Author: unspecified; session provenance retained
- Primary home: subsection:creative_routes_to_unrestricted_forcing_and_a_carry_forward_map
- Labels: NORI1, balanced, method-obstruction, verified
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_2
- Updated session: session_nori_r11913_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_q6_rooted_bichromatic_arm_plateau_20261019_r11913

## Research note

Define F_e(x): direction supports of color-e geodesics rooted at x. Define Phi_x(t)=sum t^(|S|+|T|) over S in F_0(x), T in F_1(x) with S disjoint T. LEGAL Q6 CONSTRUCTION: remove bit i from x to obtain integer r_i(x); set edge color c_i(x) to bit r_i(x) of 32-bit mask T_i. In direction order the hexadecimal masks are 2aab2aab, aaaaaaaa, 9b371326, 7700ff11, 77117711, c044ddfc. Direct enumeration of all vertices verifies undirected-edge consistency, antipodal color reversal, and three edges of each color at every vertex. Root 3 has the red full direction order (2,3,4,0,1,5), endpoint 60. Phi coefficients in ascending degree 0,...,6 are: root 0: (1,6,20,38,39,20,0); root 1: (1,6,19,35,38,19,0); root 2: (1,6,19,35,38,19,0); root 4: (1,6,20,37,38,16,0); root 8: (1,6,19,35,39,20,0); root 16: (1,6,18,34,38,17,0); root 32: (1,6,19,37,41,18,0). To verify, recursively add direction i to support S when i is unused and c_i(x xor S)=e, then count disjoint pairs of supports by total size. Thus all six neighbors have Phi lexicographically STRICTLY LOWER than root 0, but no full red path starts at root 0: a strict non-successful local maximum. For Cartesian products of legal colorings, F_e factors and Phi_(c boxplus d)=Phi_c Phi_d. Multiplication by a polynomial with positive leading term preserves strict lex ordering. Hence the k-fold product on Q_(6k) gives a strict non-successful local maximum with maximum disjoint support 5k although successful roots reach 6k. This refutes universal strict one-bit lex ascent of the COMPLETE arm-pair polynomial, not NORI1.
