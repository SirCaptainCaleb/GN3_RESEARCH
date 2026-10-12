# Highly connected graph covers violate P4 despite large local quadratic rank

- Stable ID: note_nori_xi_high_connectivity_cover_p4_failure
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: counterexample, high-connectivity, matroid-generalization
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

For odd ell>=5 and m>=3, let G=C_ell square K_m and tilde G=C_(2ell) square K_m, with deck shift tau(i,u)=(i+ell,u). The base graph has degree m+1 and vertex connectivity m+1 by Spacapan's Cartesian-product theorem (Applied Mathematics Letters 21 (2008), 682-685). Color each ring edge from index i to i+1 by i mod2; color each clique edge at index i by i mod2. Deck shift flips every color because ell is odd. The minimum distance from a cover vertex to its deck mate is ell, and every path attaining it traverses only ring edges. All shortest odd-monodromy turn cycles therefore have ell turns, all with color disagreement one. In the pointed binary lift their minimum port cocircuits have size ell+1 and intersection ell+1 with the admissible port cycle; P4 fails. Every base star has m incident edges of one color and one of the other. The local quadratic polar rank is 2 floor((m-1)/2), summing across ell*m disjoint stars to R=ell*m*2 floor((m-1)/2). Thus arbitrarily strong local quadratic mixing and arbitrary graph connectivity do not imply the short-port intersection property. The example is not a cube counterexample; it shows that cubical resource geometry cannot be discarded.
