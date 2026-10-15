# Unused-coordinate sections localize reversal index to monochromatic supports

# Reversal-index localization by unused-dimension signs

Let K be any reversal-stable simplicial subcomplex of a directed geodesic endpoint-poset complex of Q_n. A vertex p=(u,v) uses S(p)={i:u_i≠v_i}; comparable vertices have nested supports and agree on bits of dimensions unused by both. Write R(u,v)=(bar v,bar u), and assume R is free on K.

**Theorem.** For every T⊆[n] the vertex rule s_T(p)_i=0 when i∈S(p), and s_T(p)_i=(-1)^{u_i} otherwise, i∈T, extends affinely over K to an odd continuous map s_T:|K|→R^T. Its zero set is the induced subcomplex K_T on vertices whose supports contain T.

*Proof.* Along a chain, the i-th entry takes only the values 0 and one fixed sign; an affine combination vanishes if and only if every vertex of positive weight uses i. Intersecting these conditions for i∈T identifies the zero locus. R complements the common endpoint bit in unused dimensions, so s_T(Rx)=-s_T(x). □

Let α∈H¹(K/R;F₂) classify the double cover. Put j=|T|. The map s_T descends to a section of j copies of the cover line bundle L. Its top Stiefel–Whitney class equals α^j; this class vanishes off K_T/R because the section there is nowhere zero. Therefore α^j is in the image of H^j(K/R,(K\K_T)/R;F₂)→H^j(K/R;F₂), and α^j≠0 implies K_T≠∅.

**One-component saturation.** If α^j≠0 for j≥1, one R-invariant connected component C⊆K has the property that, for **every** j-subset T⊆[n], some vertex p∈C satisfies T⊆S(p). Indeed α^j restricts nontrivially to one quotient component; its preimage must be connected (a swapped pair of components gives a trivial double cover). Apply the preceding zero-set criterion separately for each T on that same component.

**NORI consequence.** In a hypothetical coloring with no monochromatic full antipodal geodesic, put K=K₀∪K₁ and I=K₀∩K₁. Seam transgression gives α_K^{j+1}=δ(α_I^j). Thus a nonzero (j+1)-st covering power of K requires a single R-invariant connected component of the bi-monochromatic seam I containing a pair using all directions of T, for every j-subset T. In particular α_K²≠0 requires a single connected R-invariant bi-monochromatic family collectively covering every cube direction.

If the largest support occurring in C has size r≥j, the number of distinct supports in C is at least ceil(binomial(n,j)/binomial(r,j)), by counting the j-subsets covered by each support.

These are necessary conditions on any surviving reversal-index class; they do not establish that such classes exist or settle NORI1.
