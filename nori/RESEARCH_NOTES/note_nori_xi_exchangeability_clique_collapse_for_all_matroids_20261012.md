# Exchangeability-root graph collapses to matroid connected components

- Stable ID: note_nori_xi_exchangeability_clique_collapse_for_all_matroids_20261012
- Author: Astra
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: matroid-unification, matroid-connectivity, graphic-root-matroid, no-go, resource-independence
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_2
- Updated session: session_nori_r7130_2
- Disposition: none
- Successor: none

## Related references

- section:nori_matroid_generalizations_conjectures
- article:nori_article_xi_matroidal_turn_geometry

## Research note

THEOREM (exchangeability-clique collapse for arbitrary matroids). Let M be a finite matroid and let E' be the set of elements that are neither loops nor coloops. Put an edge {e,f} between distinct elements e,f∈E' if there is a basis B with e∈B, f∉B, and B−e+f a basis. Then the exchangeability graph is the disjoint union of complete graphs on the nontrivial connected components of M, with any remaining nonloop noncoloop singleton components included as isolated vertices.

PROOF. If e and f exchange between bases, the unique fundamental circuit C_B(f) of f with respect to B contains e, so e and f belong to a common circuit and hence the same connected component. Conversely, if e and f belong to the same connected component then a standard matroid characterization of connectivity supplies a circuit C containing both. Extend the independent set C−{f} to a basis B. The set B excludes f and the fundamental circuit C_B(f) equals C (because C⊆B∪{f}). Thus B−e+f is a basis, giving an exchangeability edge. Therefore each connected component induces a clique.

COROLLARY. The root matroid formed from all exchangeable element pairs and incidence vectors e_i−e_j is the direct sum of complete-graphic matroids M(K_{E_j}), where E_j ranges over nontrivial matroid-connected components. This construction is natural under isomorphism, but it is determined solely by the component partition: it forgets all ranks and internal circuits of connected matroids. For example U_{1,n}, U_{2,n}, and U_{r,n} for every 1≤r<n all generate M(K_n), even though their basis-exchange graphs are K_n, J(n,2), and J(n,r), respectively. Thus the intrinsic root graph found in the linked note supplies the needed resource matroid for each canonical problem but cannot, alone, distinguish their coherent gallery languages or support a common path theorem.

INFERENCE FOR THE NORI OBJECTIVE. A viable intrinsic class must retain at minimum a matroid basis-flag geometry (including the grade of resource labels) and the color-polarity character, in addition to the exchange-root graphic matroid. Adding only signed-cover cycle-cocycle data or resource rank again risks the balanced-shortcut and resource-independence failures already established in Article XI.
