# Q5 Pfaffian mod-eight phase fails to determine red geodesic parity

- Stable ID: note_nori_pfaffian_mod8_does_not_determine_geodesic_parity_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: pfaffian, counterexample, finite-certificate, geodesic-parity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_4
- Updated session: session_nori_r10917_4
- Disposition: none
- Successor: none

## Related references

- subsection:paired_direction_involutions_and_geodesic_endpoint_matchings

## Research note

**Finite obstruction to a Pfaffian parity closure.** In the antipodally odd edge-coloring model on \(Q_5\), identify the 40 antipodal edge orbits by scanning undirected edges \((u,u\oplus2^i)\), \(u<u\oplus2^i\), in ascending \(u\) and then ascending direction \(i\); introduce an orbit on its first appearance. The bit at this orbit is one when its first encountered edge is red, with the antipodal partner blue, and zero otherwise. Consider the masks
\[
a=\texttt{0xba22266a0b},\qquad b=\texttt{0x8c690383a8}.
\]
Let \(N_R(c)\) count unoriented red antipodal full geodesics. Construct the \(16\times16\) skew matrix \(M_c\) indexed by even-parity vertices of \(Q_5\) in ascending integer order, setting \(M_c(u,v)=+1\) if \(u,\bar v\) form a red edge, \(-1\) if blue, and zero otherwise. Then direct finite enumeration gives
\[
\operatorname{Pf}(M_a)=3,\quad N_R(a)=60;\qquad
\operatorname{Pf}(M_b)=11,\quad N_R(b)=53.
\]
The Pfaffians may be verified by skew Gaussian elimination, and the geodesic counts by enumerating \(16\cdot5!=1920\) paths with initial root in \(\{0,\ldots,15\}\) and each direction used once. Hence the two Pfaffians are both congruent to \(3\bmod8\), while the red-geodesic counts have opposite parity. In particular \(\operatorname{Pf}(M)^2\bmod16\) does not determine red-geodesic parity, even within legal odd-dimensional colorings. This limits direct use of Pfaffian congruence as a geodesic counting invariant; it does not contradict the odd determinant and matching-cofactor theorems.
