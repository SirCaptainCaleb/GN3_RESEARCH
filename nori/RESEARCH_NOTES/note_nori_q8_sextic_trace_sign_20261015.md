# Opposite sixth-order noise-trace signs in balanced Q8

- Stable ID: note_nori_q8_sextic_trace_sign_20261015
- Author: Independent NORI1 researcher
- Primary home: subsection:odd_girth_and_frustration_of_switch_component_quotients
- Labels: obstruction, noise_trace, matrix, balanced
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_9
- Updated session: session_nori_r9962_9
- Disposition: none
- Successor: none

## Related references

- subsection:odd_girth_and_frustration_of_switch_component_quotients
- subsection:global_petrie_switch_moment_and_local_turn_counting

## Research note

Let n=8, with vertex bits x_0,...,x_7 and pair indices j mod 4. For either H={1} or H={1,2,3}, define
c_{2j}(x)= XOR_{h in H} x_{2(j+h mod 4)},   c_{2j+1}(x)=1-c_{2j}(x).
Each rule ignores its own bit, reverses under full bit complement (because |H| is odd), and each direction pair has one edge of each color at every vertex. Both colorings therefore satisfy antipodal oddness and vertex balance.

With A the cube adjacency, P the antipodal permutation, R the color-zero adjacency and F_H(t)=tr(P((A+t(2R-A))/2)^8), direct integer calculation gives
F_{ {1} }(t)=40320-53760t^2+19712t^4-1536t^6,
F_{ {1,2,3} }(t)=40320-32256t^2+3072t^6.
The sixth-degree coefficients have opposite signs.

Certificate independent of floating point: for each root x let d_x(S,k) count paths traversing precisely directions S with k edges of color one. Start with d_x(empty,0)=1. For each i outside S increment d_x(S union {i}, k+c_i(x XOR 1_S)) by d_x(S,k). Summing d_x([8],k) over all 256 roots gives g_k, k=0,...,8:
H={1}: (4736,113664,828928,2466816,3493632,2466816,828928,113664,4736);
H={1,2,3}: (11136,181248,1012224,2399232,3114240,2399232,1012224,181248,11136).
Both rows sum to 256*8!=10321920. The identity
F_H(t)=2^(-8) sum_{k=0}^8 g_k(1+t)^(8-k)(1-t)^k
gives the displayed polynomials. A separate direct enumeration of all 256*8! rooted orders confirms the same coefficients.

Consequently a fixed-sign assertion for the sixth-order noise-trace coefficient is false, even for perfectly balanced legal cube colorings obeying the full Boolean realization equations. Both examples have zero-colored full antipodal geodesics, with oriented counts 4736 and 11136; the claim concerns the sign of a higher mixed moment, not NORI1 itself.
