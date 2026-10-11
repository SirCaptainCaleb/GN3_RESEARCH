# Exact one-change words, width-one guards, and rooted state

## Statement

Exact one-change word and based-state transition

## Body

For a based antipodal geodesic γ=(X0,...,Xn), let ai=c(Xi,X(i+1),X(i+2),X(i+3)), 0≤i≤n−3. Then γ is good exactly when ∑(ai⊕a(i+1))≤1, equivalently its word is 0^p1^q or 1^p0^q. For exact partial-state search, retain the actual current cube vertex, used coordinate directions, preceding three vertices (or equivalent based history), the last color and whether the single permitted change has occurred. Extending along an unused direction evaluates the actual resulting window. This is a combinatorial identity rather than proof of existence, and needs no translation invariance. Adapted from NOR cochain_viewpoint_on_color_changes and one_change_nor_is_reachability_in_a_two_layer_flag_prism.

Width-one guard: the word 010 satisfies the first-zero/last-one inequality q <= p+1 but has two changes. The weaker width-one condition is equivalent to forbidding the contiguous subwords 001, 011 and 0101 (see archived original two_cover_words_avoid_three_local_patterns for proof). Actual NORI state search must retain the physical root and ordered window memory. This entry consolidates nori_one_change_vs_width_one_relaxation and two_cover_words_avoid_three_local_patterns; archived originals preserve full proofs.

Proof of forbidden-pattern equivalence. If the width-one inequality fails, there are positions i<j with a_i=0, a_j=1 and j-i>=2. Choose such a pair of minimum distance d. If d=2, the three-letter block is 001 or 011. If d>=3, minimality forces a_(i+1)=1 and a_(j-1)=0, since otherwise there is a shorter nonadjacent zero-to-one pair. If d>=4, a_(i+2)=1 makes (i,i+2) a shorter nonadjacent pair, while a_(i+2)=0 makes (i+2,j) one; contradiction. Therefore d=3 and the block is 0101. Conversely each of 001, 011 and 0101 contains a zero followed at distance >=2 by a one. This proves the equivalence.


## Metadata

- ID: nori_one_change_local_derivative
- Kind: toolkit
- Version: 4
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted
