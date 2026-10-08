# Root-coupled window incidence and the Freudenthal chart obstruction

# Root-coupled Freudenthal incidence geometry for NORI

Let \(V=[n]\), \(x\in\mathbb F_2^V\), \(p=(p_1,\dots,p_n)\) a permutation. Let
\[
W_i(x,p)=(F_i(x,p),(p_i,p_{i+1},p_{i+2})),\qquad 1\le i\le n-2,
\]
be its actual ordered three-face: its exterior coordinates equal \(x_j\oplus{\bf1}_{j\in\{p_1,\dots,p_{i-1}\}}\). Put \(w_i(x,p)=c(W_i(x,p))\), \(d_i=w_i\oplus w_{i+1}\) for \(1\le i\le n-3\).

**Lemma 1 (exact root-coupling / window fibers).** For every fixed \(p,i\), \(w_i(x,p)\) is constant on the eight roots \(x\oplus T\) with \(T\subseteq\{p_i,p_{i+1},p_{i+2}\}\). Conversely, two roots yield the same ordered window \(W_i\) precisely when they agree outside this three-set. In particular, \(d_i(x,p)\) is constant on each square
\[
x\oplus 2^{\{p_{i+1},p_{i+2}\}},
\]
and depends only on the \(n-2\) root bits outside these two common free coordinates.

*Proof.* The face exterior is determined by \(x\) outside its three free coordinates, while the free bits are discarded. Consecutive free triples intersect exactly in \(\{p_{i+1},p_{i+2}\}\), so both window colors, hence their difference, are invariant under toggling those two root bits. \(\square\)

**Lemma 2 (correct reversal equivariance).** The antipodal-reversal involution on full geodesics is
\[
J(x,p)=(x,\operatorname{rev}p).
\]
It preserves the root, and the odd ordered-face law yields
\[
w_i(x,\operatorname{rev}p)=1\oplus w_{n-1-i}(x,p),\quad 1\le i\le n-2,
\]
and
\[
d_i(x,\operatorname{rev}p)=d_{n-2-i}(x,p),\quad 1\le i\le n-3.
\]
Thus reversal is an involution *within* each rooted permutahedral chamber system. All cross-root information instead enters through Lemma 1's window fibers.

**Lemma 3 (no single Freudenthal triangulation contains every rooted maximal chain).** The Freudenthal triangulation rooted at \(x\) uses the total order \(A\le_x B\) iff \(A\oplus x\subseteq B\oplus x\). Already on a 2-dimensional coordinate square, the maximal chains rooted at the corner \(00\) use its diagonal \(00\)--\(11\), whereas maximal chains rooted at \(10\) use the crossing diagonal \(10\)--\(01\). An ordinary geometric triangulation cannot simultaneously contain both crossing diagonals as edges. Therefore a topological proof encompassing all rooted geodesics needs a *coupled family of Freudenthal charts* or a common subdivision/cell complex whose combinatorial data still remembers the individual root-dependent chains; interpreting all roots as chambers of one fixed Freudenthal triangulation is invalid.

**Root-coupled incidence proposal.** Introduce states \((x,p,i)\) with an ordered-face evaluation map \(e(x,p,i)=W_i(x,p)\). Its fibers are precisely the 3-cubes in Lemma 1 (for fixed \(p,i\)), and adjacent-seam evaluation descends to 2-cubes of roots. Reversal \(J\) acts within each \(x\)-fiber while the incidence identifications glue *across* roots. These two operations commute with the underlying ordered-face labels in the precise senses above. This provides a canonical finite combinatorial input for an equivariant carrier / chain-complex approach: one-switch reachability is a property of the full sequence \(w_i\), and a topological obstruction must detect reachability of a full root-plus-order chamber, rather than simply a balanced set of window labels.

**Topology frontier (open).** Construct an equivariant chain map or acyclic carrier over this coupled incidence system for a hypothetical all-bad coloring such that the induced map violates a nonzero mod-2 degree/index. A successful extraction theorem must force a **single chamber** with at most one nonzero \(d_i\), rather than merely a balanced convex combination of signs in multiple chambers. Fixed-root-only Tucker/Borsuk--Ulam arguments cannot suffice: the established rooted obstructions show arbitrary prescribed roots may have no good full order. A second key issue is that rooted charts have incompatible diagonals, as Lemma 3 demonstrates; any proposed simplicial proof must explicitly resolve those crossing chains.
