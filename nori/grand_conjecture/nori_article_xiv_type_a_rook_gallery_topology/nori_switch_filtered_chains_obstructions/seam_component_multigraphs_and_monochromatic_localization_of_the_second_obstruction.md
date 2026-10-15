# Seam-component multigraphs and monochromatic localization of the second obstruction

# Seam-component multigraph and the second tower obstruction

Let K=K0 union K1 be finite simplicial complexes, I=K0 intersect K1, and suppose an involution R exchanges the two pieces. Construct a bipartite multigraph Lambda with one vertex per connected component of K0 or K1, and **one edge for each connected component S of I**, joining the two color components containing S. Keep parallel edges. The involution exchanges the color parts and sends edge S to edge RS.

**Theorem 1 (equivariant graph and Mayer–Vietoris).** There is an equivariant piecewise-linear map nu:|K|→|Lambda| inducing bijection on connected components and surjection on first homology over F2. The following homology sequence has zero cokernel and each displayed kernel is the preceding image:
\[
H_1(I)\to H_1(K0)\oplus H_1(K1)\to H_1(K)
\xrightarrow{\nu_*}H_1(Lambda)\to0.
\tag{1}
\]

*Proof.* On the barycentric subdivision, send each simplex exclusively in K0 or K1 to the corresponding color-component vertex; send each simplex of I to the midpoint of the graph edge associated with its connected seam component. Nested simplices in I belong to the same component, and a chain exiting I enters only one color piece, so affine interpolation within a single graph edge is continuous. The rule commutes with R. Each graph walk lifts through its seam components and the adjacent connected color pieces, proving surjectivity on π1 and H1. Finally, the Mayer–Vietoris sequence has consecutive terms H1(I), H1(K0)⊕H1(K1), H1(K), H0(I), H0(K0)⊕H0(K1). The kernel of its last map is the graph cycle space H1(Lambda); the connecting map counts seam crossings and agrees with nu_*. This proves (1). □

**Theorem 2 (fixed seam threshold).** Assume R acts freely on K and let alpha be the double-cover class on K/R. If Lambda has no R-invariant edge, then alpha squared vanishes. An R-invariant edge of Lambda is equivalent to an R-invariant connected component S of I.

*Proof.* R swaps the bipartite vertex parts, so no graph vertex is fixed. If no edge is preserved as a set, Lambda is a free involution graph. Equivariance of nu makes alpha the pullback of the covering class on Lambda/R; its square vanishes because this quotient is a graph. The final equivalence follows from the definition of edges. □

**Theorem 3 (monochromatic location of the second obstruction).** Suppose C⊆K is connected and R-invariant, and contains an R-invariant connected seam component S⊆I. Choose p∈S and a mod-two path-chain gamma⊆S from p to Rp. The one-cycle zeta=gamma+Rgamma represents the canonical second-stage Tate obstruction theta(C), and
\[
\boxed{[zeta]\in\operatorname{im}\bigl(
H_1(K0\cap C)\oplus H_1(K1\cap C)\to H_1(C)\bigr).}
\tag{2}
\]

*Proof.* The preceding Smith-transfer theorem makes any symmetrized path from p to Rp a representative of theta(C). The map nu is constant on the connected seam component S, so it sends zeta to zero already on chains. By (1), its first-homology class belongs to the stated image. □

**Corollary.** If the image of monochromatic first homology in H1(C) vanishes under Theorem 3 (for instance, if both color pieces in C have zero first homology), then theta(C)=0, a tower through degree two exists, and alpha_C squared is nonzero.

For NORI1, this sharpens the separation of tasks: the first tower step is a parity walk in an incidence graph, while, after locating a reversal-invariant seam component, the second obstruction comes from the internal directed-turn homology of monochromatic pieces. It does not assert the required seam component exists in every coloring.
