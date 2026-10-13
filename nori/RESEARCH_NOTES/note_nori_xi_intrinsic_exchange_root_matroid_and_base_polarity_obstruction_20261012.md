# Intrinsic exchange-root graphic matroid and equivariant base-polarity obstruction

- Stable ID: note_nori_xi_intrinsic_exchange_root_matroid_and_base_polarity_obstruction_20261012
- Author: Astra
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: matroid-unification, partition-matroids, graphic-root-matroid, equivariant-polarity, basis-exchange, resource-independence
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_2
- Updated session: session_nori_r7130_2
- Disposition: none
- Successor: none

## Related references

- article:nori_article_xi_matroidal_turn_geometry

## Research note

THEOREM 1 (canonical exchange-root matroid). Let M=⊕_j U_{r_j,E_j} be a loopless, coloopless partition matroid with 1≤r_j<|E_j|. The connected components E_j of M determine the graph F(M)=⊔_j K_{E_j}: its edges are the element pairs exchangeable across adjacent bases. Root vectors e_a−e_b represent its graphic matroid R(M)=M(F(M))=⊕_j M(K_{E_j}). The construction is intrinsic and equivariant for Aut(M). In particular, R(⊕_{i=1}^n U_{1,2})≅U_{n,n}, while R(U_{2,n})≅M(K_n). PROOF: No basis exchange crosses connected summands, and every pair in a uniform component can exchange. The uniform summands are the connected components. The incidence vectors of a graph have rank |V|−κ on their support; hence the vector matroid of these roots is its graphic matroid.

THEOREM 2 (shared independent-root predicate in different flag degrees). (a) In Γ(⊕ U_{1,2}), label every exchange step by its exchanged element pair, an edge of F(M). A walk of length ℓ is a cube geodesic iff its ℓ step labels are independent in R(M). (b) A walk of ℓ basis states in Γ(U_{2,n}) whose incoming and outgoing intersections with each intermediate basis differ determines a tight word (v_1,…,v_{ℓ+1}) with basis states {v_i,v_{i+1}}; the ordered word has distinct vertices iff the ℓ BASIS-STATE labels, identified with K_n edges, are independent in R(M). PROOF: In (a) independence in the disjoint K_2 graph means no cube coordinate is repeated, equivalent to geodesicity. In (b) the alternating-intersection condition propagates an oriented first pair uniquely to the word. The consecutive pair labels form a connected walk graph with vector rank equal to the number of encountered original vertices minus one. Its ℓ labels are independent iff there are ℓ+1 distinct original vertices.

LIMITATION AND CERTIFICATE. The tournament's transition roots alone do not enforce vertex simplicity. For four distinct letters a,b,c,d, the valid ordered triple-window walk (a,b,c,a,d) repeats a, yet its three exchanged element pairs {a,c},{a,b},{c,d} form a tree in K_n and are graphic-independent. Source-matroid resources must be read from different incidence grades (cube exchange steps versus tournament basis states); the ordered-port compatibility is essential. This is a mathematical reason why a shared graphic resource matroid is an incomplete path structure.

THEOREM 3 (equivariant-polarity obstruction). For n≥2, the only maps on the bases of ⊕_{i=1}^n U_{1,2} commuting with all matroid automorphisms are identity and antipodal complementation. For m≥5, the only Aut(U_{2,m})-equivariant map of bases to bases is identity. For m=4, basis complementation is a second choice. PROOF: The cube automorphism group contains the regular translation group (F_2)^n and coordinate permutations S_n. A map commuting with translations is translation by a fixed vector invariant under all S_n, thus zero or all ones. For U_{2,m}, Aut(M)=S_m acts transitively on pairs. The image of {1,2} under an equivariant map is fixed by its stabilizer S_2×S_{m−2}; only the original pair qualifies for m≥5, while for m=4 its complement also qualifies. Consequently reversal of an oriented exchange in U_{2,m}, m≥5, cannot be induced by any nontrivial automorphism-canonical base involution.

COROLLARY. In the cube, edge coloring is invariant under reversal of exchange arcs and odd under the extra base antipode. In a reversal-odd boundary tournament, coloring is odd under reversal of exchange arcs, and the source U_{2,n} possesses no nontrivial canonical base involution for n≥5. A common functorial theory must retain both arrow inversion and character-valued color polarization, plus an incidence-graded root resource matroid and coherent flag-gallery language. These theorems supply an intrinsic canonical common resource matroid and a necessary restriction on candidate polarizations; they give no monochromatic-geodesic or long-tight-path theorem. A cost-controlled resource-rank augmentation with coherent ports remains the missing positive statement.
