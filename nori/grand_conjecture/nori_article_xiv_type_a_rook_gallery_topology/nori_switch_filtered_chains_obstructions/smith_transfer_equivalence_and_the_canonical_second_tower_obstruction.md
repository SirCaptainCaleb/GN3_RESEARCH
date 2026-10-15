# Smith transfer equivalence and the canonical second tower obstruction

# Smith transfer equivalence and the canonical second tower obstruction

Let X be a finite simplicial complex carrying a free simplicial involution R, let Q=X/R, and take all chains and cohomology over F₂. Write N=1+R, let π:C_*(X)→C_*(Q) be the orbit projection, and let t:C_*(Q)→C_*(X) send an orbit simplex to the sum of its two lifts. Then

0 → C_*(Q) --t→ C_*(X) --π→ C_*(Q) → 0

is a short sequence of chain complexes, with tπ=N. Its homology connecting operator D:H_j(Q)→H_{j−1}(Q) is the Smith transfer connecting map.

**Lemma (Smith connecting map).** D(h)=α cap h, where α=w₁(X→Q)∈H¹(Q;F₂).

*Proof.* Choose one lift of each quotient simplex and represent the double cover by its sheet-transition one-cocycle α. The boundary of the lifted chain differs from the lift of the boundary by the transfer of the transition-weighted faces. On cycles these transitions give the simplicial cap product with α; changing lift choices changes this representative only by a boundary. Equivalently, the covering chain extension above is the local-system extension classified by α. Therefore D=α cap −. □

**Theorem 1 (full converse to the antipodal chain-tower criterion).** For every integer q≥1, the following are equivalent:

(i) α^q≠0 in H^q(Q;F₂).

(ii) There exist chains z_j∈C_j(X), 0≤j≤q, such that
εz₀=1 and ∂z_j=Nz_{j−1} for 1≤j≤q.

*Proof.* Suppose a tower exists. Set h_j=πz_j for all j. Because πN=0, each h_j for j≥1 is a cycle; h₀ is a zero-cycle. The connecting operator sends [h_j] to [h_{j−1}] since ∂z_j=t h_{j−1}. Hence D^q[h_q]=[h₀]. Its augmentation is εz₀=1. By the lemma, this means ⟨α^q,[h_q]⟩=1, proving (i).

Conversely if α^q≠0, choose a quotient q-cycle h_q with ⟨α^q,[h_q]⟩=1; this is possible over the field F₂. Lift h_q to an arbitrary chain z_q upstairs. Since ∂h_q=0, the boundary ∂z_q is in ker π=im t, so ∂z_q=t h_{q−1} for a unique quotient chain h_{q−1}. Injectivity of t implies ∂h_{q−1}=0. Lift h_{q−1} to z_{q−1}; then ∂z_q=tπz_{q−1}=Nz_{q−1}. Iterate to obtain z_{q−2},...,z₀ with every required norm-boundary equation. At degree zero, εz₀ equals the augmentation of D^q[h_q], which is ⟨α^q,[h_q]⟩=1. This proves (ii). □

In particular the maximal height of such a tower equals the largest nonzero power of the reversal-covering class. This completes the converse missing from the earlier one-chain-per-degree construction in Article XIV. It also shows that producing a tower is a topological index problem, not merely a weaker proxy for one.

**Theorem 2 (a canonical obstruction at degree two).** Let C be an R-invariant connected component of X. Choose a vertex p∈C and a mod-two one-chain γ with ∂γ=p+Rp. Put ζ=γ+Rγ. Then [ζ]∈H₁(C;F₂)^R, and its class
θ(C)=[ζ] mod N H₁(C;F₂)
in the quotient H₁(C;F₂)^R / N H₁(C;F₂)
is independent of both p and γ. Moreover
θ(C)=0 if and only if C admits a tower of height two, equivalently if and only if α_C²≠0.

*Proof.* If γ is changed with p fixed, its difference is a one-cycle η, and ζ changes by Nη. If the root changes from p to p', choose a path-chain η from p to p', replace γ by γ+η+Rη, and observe that ζ stays unchanged because N²=0. Thus θ is canonical.

If θ=0, choose a cycle η with [ζ]=N[η]. Replacing γ with γ+η makes the symmetrized cycle a boundary, say ∂z₂=N(γ+η). With z₀=p and z₁=γ+η this is a height-two tower. Conversely any height-two tower with odd zero-chain in C can be normalized to z₀=p by connecting its zero-chain to p and adding N of the connecting one-chain to z₁. Then its second equation implies θ(C)=0. The last equivalence follows from Theorem 1. □

**NORI interpretation.** For a hypothetical counterexample, apply the theorem to the free reversal action on the two-color directed endpoint complex K. The earlier half-dimensional bound gives α_K^q=0, where q=floor((n−1)/2). By Theorem 1 no height-q tower exists. For n≥5, the first stage is the odd-walk condition on the red-component incidence graph; if an invariant connected component exists, its *second* obstruction is the choice-independent class θ(C), rather than the homology class of any one arbitrarily chosen symmetrized path. At greater degrees, the Smith transfer sequence gives the analogous test through iterated cap products with α.

The result does not prove that the needed tower exists, and it does not close NORI1. Its value is a two-way algebraic characterization and a canonical obstruction that can be computed without making arbitrary root/path choices.
