# Nonoptimal strict local minima for adjacent-swap geodesic exchange in dimensions n>=9

- Stable ID: note_nori_xi_strict_geodesic_exchange_trap
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: counterexample, matroid-exchange, cube
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_3
- Updated session: session_nori_r6430_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For every n>=9 there is an antipodally odd coloring of Q_n and a geodesic C of cyclic color-turn weight three such that all n single adjacent-direction swaps of C have weight five, while another geodesic is monochromatic. Construct at the root-zero geodesic using directions 1,...,n and prescribe turn disagreements at cyclic indices 0,3,6 only. Odd parity ensures consistent color assignment. Each swap changes three consecutive turn comparisons, at most one initially changed. Its two replacement edge-state colors can therefore be assigned to raise the three-term cost by two. The n swaps introduce 2n distinct antipodal edge orbits, also distinct from the original n, so these assignments are independent for n>=9. A random geodesic meets the 3n prescribed edge orbits in expectation 3n/2^(n-2)<1, so choose one disjoint and color all its edges zero, with antipodal mates one. This completes the coloring with a monochromatic geodesic and a strict nonoptimal swap-local minimum. Checked directly in Q9: prescribed base edge colors 0,1,1,1,0,0,0,1,1; all nine cyclic adjacent swaps have weight5. Thus a purely monotone single-swap descent theorem is false; additionally each length-(n+1) one-stationary cycle has a unique n-cycle parent, so alternating only elementary two-port curvature pivots cannot change geodesic parents.
