# Monochromatic-geodesic closure is exactly an antipodal fixed point of the uncolored reachability nerve

# Exact fixed-point reformulation of monochromatic-geodesic reachability

Let Q_n have an antipodally odd binary UNDIRECTED edge coloring c(bar e)=1-c(e). For each cube vertex x define the COLOR-FREE region
\[
R(x)=\{z:\text{there is a monochromatic shortest path joining x and z, of either color}\},
\]
including x. Because cube edges are undirected, z∈R(x) iff x∈R(z). Antipodal oddness gives R(bar x)=bar(R(x)).

Define the **reachability nerve** \(K_R\) to be the abstract simplicial complex with vertex set Q_n and
\[
\sigma\in K_R\quad\Longleftrightarrow\quad\bigcap_{x\in\sigma}R(x)\ne\varnothing.
\]
Equivalently, by symmetric reachability,
\[
K_R=\bigcup_{z\in Q_n}\Delta(R(z)),
\]
the union of the full simplices spanned by the reachable-region vertex sets. Global complement \(\tau(x)=\bar x\) induces a simplicial involution of K_R.

**Theorem (exact fixed-point equivalence).** The following are equivalent:
1. A monochromatic full antipodal geodesic exists somewhere in Q_n.
2. There are antipodal roots x,bar x with R(x)∩R(bar x) nonempty.
3. The reachability nerve K_R contains an antipodal edge {x,bar x}.
4. The geometric realization |K_R| has a fixed point under its antipodal simplicial involution τ.

**Proof.** (1) iff (2) is the exact common-target reachability extraction theorem: a shared reachable target produces a full antipodal geodesic with at most one color change; odd edge coloring rotates a one-change antipodal geodesic to a monochromatic one. Conditions (2) and (3) are identical by the definition of a simplex in the nerve. An antipodal edge has τ-fixed midpoint, so (3) implies (4). Conversely let p∈|K_R| be fixed. Its unique minimal supporting simplex σ must be τ-invariant because τp=p. Since τ has no fixed vertex of Q_n, each vertex of σ is accompanied by its distinct antipode; σ therefore contains an antipodal edge. Hence (4) implies (3). QED.

**Corollary (Euler characteristic forcing).** If \(\chi(K_R)\) is odd, monochromatic antipodal-geodesic closure holds. In particular, if K_R is nonempty and acyclic over F_2, closure holds.

Proof. In the absence of an antipodal edge, τ acts without any invariant nonempty simplex: an invariant simplex would contain an antipodal pair. Thus τ partitions all k-simplices into disjoint pairs for every k, so each f_k is even and \chi is even. Contraposition proves the claim. Acyclicity gives \chi=1. QED.

**Crucial limitation.** Neither odd Euler characteristic nor nonzero antipodal Lefschetz number is a universal property of K_R, even for valid antipodally odd edge colorings: the explicit affine Q4 coloring in the next item gives \chi(K_R)=2 and antipodal Lefschetz number L(τ)=0 while all eight antipodal root pairs have a common reachable target. Thus this theorem supplies an exact topological restatement and a sufficient cohomological forcing criterion, not a completed proof of the edge conjecture. Any universal argument must exploit finer reachability incidence, another equivariant complex, or a relative/topological index that remains nontrivial beyond ordinary \chi or Lefschetz number.

**Relation to existing geometry.** K_R already contains every simplex \Delta({z}∪N_{Q_n}(z)), since every cube neighbor of z reaches z by a one-edge monochromatic geodesic. Extra simplices record genuinely longer monochromatic-geodesic reachability. Characterizing their imposed topology may permit a Hartman/KKM/Tucker contradiction. This approach precisely matches the user's intended unlabeled-color R(x) formulation.
