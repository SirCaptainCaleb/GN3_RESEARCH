# Independent audit: external gauge does not close the maximal A2 braid — preserved pre-item development

## Development

## Independent audit of the terminal edge-surgery closure

The claimed closure in [[rank_two_coherence_closes_by_the_external_gauge]] fails at its first load-bearing implication.

For the fixed-path witness labeling actually defined in the earlier development, a bad chamber first selects the earliest represented unsigned edge of the witness path. If exactly one orientation of that selected edge is represented by a forbidden-pattern occurrence, the label uses that **intrinsic witness orientation**. The external antipodal gauge is invoked only when both orientations of the same selected edge occur, and for the self-reverse-complement centered alternating tie-break. Therefore, on the full set of chambers carrying a fixed unsigned witness edge (e_r), one does **not** have a universal identity
[
ell(pi)=g(pi)e_r.
]

Consequently a Coxeter edge with labels (+e_rleftrightarrow -e_r) need not swap the two fixed gauge vertices. The ensuing claim that a commuting square or braid hexagon has at most two terminal sign-flip edges is therefore unsupported. In particular, the external-gauge argument does not eliminate the surviving (A_2) obstruction identified in [[rank_two_normalization_squares_close_and_only_the_inside_boundary_braid_remains]]; it merely suppresses it by replacing intrinsic witness orientation with a stronger labeling rule that Article VII did not define.

The remaining audit checks separate cleanly.

1. **Ten-position normalization.** The pointwise normalization is legitimate for each terminal determining interval of size at most ten. Internal generators preserve the support, exterior generators commute, and a single endpoint crossing changes the ten-set by one vertex. This remains useful without the gauge shortcut.
2. **Boundary-crossing braid compatibility.** The statement that the *two gauge-swap supports* can be chosen equal or one-vertex apart is irrelevant once terminal sign flips are not confined to gauge-swap edges. The maximal boundary braid can involve the three supports (T+{a,b}, T+{a,c}, T+{b,c}), and these must be reconciled cyclically.
3. **Compatible one-vertex (5|5) lemma.** [[compatible_two_covers_under_a_one_vertex_terminal_support_exchange]] has an independent counting proof and does supply two ten-support covers sharing a Hamiltonian side, including the support-saturating two-support case. But pairwise compatibility does not close the three-support odd cycle of the maximal braid.
4. **Equivariance.** Reversal can make any already coherent surgery/carrier assignment equivariant by choosing representatives of reversal orbits and reversing the choices. This is conditional on existence of the coherent local assignment and does not repair the missing braid compatibility.
5. **Rank-two-to-global extension.** The Coxeter presentation reduces compatibility of adjacent-swap data to commuting squares and braid hexagons; an acyclic-carrier extension is therefore available once every such rank-two residue has a compatible contractible next-depth carrier. The unresolved maximal (A_2) residue prevents invoking this step.
6. **Index iteration.** The stated arithmetic is consistent: with (m=n-2), witness-edge dimension (d=m-2), (gamma(Y_1)=m+1), and a loss of at most one per depth, one obtains (gamma(Y_{d+1})ge3), hence a nonempty witness-free level. A witness-free chamber avoids (001,011,0101) and gives a two-cover by the exact forbidden-pattern theorem. There is no separate endpoint/indexing defect visible here; the missing premise is the map (S_r	o Y_{r+1}) at the maximal braid.

**Smallest repair obligation.** Close the maximal order-eleven boundary (A_2) braid left by [[rank_two_normalization_squares_close_and_only_the_inside_boundary_braid_remains]]. A sufficient finite statement is the common-core braid lemma: for the eight-vertex core (T) and moving vertices (a,b,c), find a Hamiltonian five-set (Bsubset T) such that, for (C=Tsetminus B), all of (C+{a,b}, C+{a,c}, C+{b,c}) are Hamiltonian. Alternatively, exhibit a more flexible contractible next-depth carrier joining the three normalized surgeries.

Thus the grand conjecture is **not audited closed**. The correct frontier is the single maximal order-eleven (A_2) braid.
