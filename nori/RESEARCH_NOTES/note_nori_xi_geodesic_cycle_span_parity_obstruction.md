# Geodesic-circuit parity cannot characterize admissible turn cochains

- Stable ID: note_nori_xi_geodesic_cycle_span_parity_obstruction
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xi_matroidal_turn_geometry
- Labels: obstruction, proved, matroidal, finite-computation
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_3
- Updated session: session_nori_r6430_3
- Disposition: none
- Successor: none

## Related references

- subsection:folded_cube_cycle_space_presentation_and_antipodal_girth
- subsection:monotone_triangle_contractions_and_directional_excess_in_antipodal_turn_cycles

## Research note

**Universal parity obstruction.** Let \(H_n=L(Q_n)/\langle\tau\rangle\), \(n\ge3\), and let \(\alpha:Z_1(H_n;\mathbb F_2)\to\mathbb F_2\) denote antipodal monodromy, represented by a cochain \(a\). Let \(\mathcal R_n\) denote the length-\(n\) monodromy-one graphic circuits, namely the cyclic turn cycles of full antipodal geodesics. Define \(h_n(t)=1+(n\bmod2)a(t)\) over \(\mathbb F_2\). For every \(C\in\mathcal R_n\),
\[
\langle h_n,C\rangle=|C|+(n\bmod2)\alpha(C)=n+(n\bmod2)=0\pmod2.
\]
But for any star triangle \(T\), \(\alpha(T)=0\) and \(\langle h_n,T\rangle=3=1\pmod2\). Therefore \(h_n\) is not a cut, and the binary span of \(\mathcal R_n\) is a proper subspace of \(Z_1(H_n;\mathbb F_2)\) for every \(n\ge3\). The cochain \(d^*=a+h_n\) has the prescribed odd turn sum on every antipodal geodesic cycle, yet violates star-triangle parity. Thus testing parity only on geodesic witnesses cannot characterize the admissible switching class.

**Computational rank audit.** Exhaustively enumerate cyclic antipodal geodesics by choosing their first coordinate direction as 0 (by cyclic rotation), iterating all cube roots and all permutations of the remaining coordinates, encoding each cyclic turn cycle as a binary incidence vector in \(E(H_n)\), deduplicating vectors, then performing Gaussian elimination over \(\mathbb F_2\). The results are:

| n | Number of circuits | Their span rank | Full cycle rank | Deficiency |
|---|---:|---:|---:|---:|
| 3 | 4 | 4 | 7 | 3 |
| 4 | 24 | 23 | 33 | 10 |
| 5 | 192 | 116 | 121 | 5 |
| 6 | 1920 | 379 | 385 | 6 |
| 7 | 23040 | 1114 | 1121 | 7 |
| 8 | 322560 | 3065 | 3073 | 8 |

The deficiency \(n\) for \(5\le n\le8\) is an observed finite pattern; its extension remains unproved. These computational values provide supplementary evidence; the universal theorem above has a symbolic proof.

**Methodological implication.** The parity annihilator of geodesic cycles strictly contains the cut space in all dimensions. Quantitative turn weights and locally generated cycle constraints must remain coupled in matroidal arguments.
