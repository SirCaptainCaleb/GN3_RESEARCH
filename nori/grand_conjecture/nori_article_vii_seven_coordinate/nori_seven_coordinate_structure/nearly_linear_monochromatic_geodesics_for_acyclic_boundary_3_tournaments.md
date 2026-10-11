# Nearly-linear monochromatic geodesics for acyclic boundary 3-tournaments

# Nearly-linear monochromatic geodesics for acyclic boundary 3-tournaments

## Scope and principal transfer theorem

Let \(V\) be an \(n\)-element coordinate set, \(n\ge3\). A **boundary 3-tournament** is a function \(b(a,b,c)\in\{0,1\}\) on ordered triples of distinct coordinates obeying \(b(c,b,a)=1-b(a,b,c)\). The corresponding direction-only coloring of genuine physical ordered 3-faces is
\[
 c(F,(a,b,c)):=b(a,b,c).
 \tag{1}
\]
This satisfies both \(c(F,\operatorname{rev}\pi)=1-c(F,\pi)\) and \(c(\bar F,\pi)=c(F,\pi)\), hence the combined NORI antipodal-reversal oddness condition.

Associate to \(b\) an orientation \(\vec L\) of the line graph \(L(K_V)\), whose vertices are unordered edges of \(K_V\), by orienting
\[
 \{a,b\}\longrightarrow\{b,c\}
 \quad\Longleftrightarrow\quad b(a,b,c)=1.
 \tag{2}
\]
The reversal identity makes (2) well defined.

**Theorem (acyclic transfer, using the edge-ordered-graph altitude theorem).** If \(\vec L\) is acyclic, the coloring (1) has a monochromatic geodesic traversing at least
\[
 \frac{n}{2^{C\sqrt{(\log n)(\log\log n)}}}
 \tag{3}
\]
distinct coordinate directions, for some absolute constant \(C>0\) and all sufficiently large \(n\). In particular its longest monochromatic geodesic has length \(n^{1-o(1)}\).

The count in (3) is of **edges of the original simple path in \(K_V\)**, equivalently of coordinate moves in the cube. It is not a count of vertices of \(L(K_V)\) without an incidence-consistent lift. The resulting cube geodesic may be partial; (3) makes no spanning assertion.

**Proof.** Since the finite orientation \(\vec L\) is acyclic, take a topological order \(\prec\) of its vertices. These vertices are precisely the unordered edges of \(K_V\), so \(\prec\) is one strict ordering of the edges of \(K_V\). Every comparison (2) is respected:
\[
 b(a,b,c)=1\quad\Longleftrightarrow\quad \{a,b\}\prec\{b,c\}. \tag{4}
\]
For the converse direction in (4), note that the two line-graph vertices are adjacent and their edge is oriented exactly one way; topological order must respect that orientation.

Apply the theorem of M. Bucić, M. Kwan, A. Pokrovskiy, B. Sudakov, T. Tran and A. Z. Wagner (*Nearly-linear monotone paths in edge-ordered graphs*, Israel J. Math. 238 (2020), 663–685, Theorem 1.1; DOI 10.1007/s11856-020-2035-7) to the edge-ordered complete graph \((K_V,\prec)\). This gives a **vertex-simple** original-graph path
\[
 v_0,v_1,\ldots,v_\ell,\quad
 \{v_0,v_1\}\prec\{v_1,v_2\}\prec\cdots
 \prec\{v_{\ell-1},v_\ell\},
 \tag{5}
\]
with \(\ell\) at least the quantity in (3).

Choose any cube starting vertex \(x\) and traverse distinct coordinate directions \(v_0,v_1,\ldots,v_\ell\) in this order. Because no coordinate is repeated, this is a genuine geodesic of length \(\ell+1\) if we traverse every \(v_i\), or \(\ell\) if we traverse \(v_0,\ldots,v_{\ell-1}\). In either case, all its consecutive ordered 3-face windows have color 1 by (4)–(5), using the direction-only rule (1). Choosing all \(\ell+1\) vertices of the original graph path as distinct coordinate moves yields a cube geodesic of length \(\ell+1\), with exactly \(\ell-1\) windows, each colored 1. Thus (3) follows (indeed with one extra coordinate move). The start \(x\) is arbitrary because the coloring ignores fixed exterior bits. \(\square\)

**Length convention.** The edge-ordered increasing path has \(\ell\) edges and \(\ell+1\) distinct original vertices. These \(\ell+1\) distinct vertices become \(\ell+1\) cube coordinate directions. Thus there is no hidden loss through repeated original vertices, and there is no appeal to an arbitrary directed path of \(L(K_V)\).

## What directed cycles can obstruct

**Corollary.** Any sequence of direction-only boundary 3-tournaments \(b_n\) whose longest monochromatic cube geodesic has \(o(n^{1-o(1)})\) length (in particular \(O(\sqrt n)\)) must have a **directed cycle in its line-graph comparison orientation** for all sufficiently large \(n\).

More quantitatively, if a direction-only boundary tournament on \(n\) directions has no monochromatic geodesic of length at least the explicit lower bound (3), then its line-graph orientation contains a directed cycle.

This is the contrapositive of the theorem. It gives a precise requirement for a prospective short-path boundary obstruction: the local comparisons cannot all arise from one global edge ordering.

The converse is false: presence of a directed cycle says nothing by itself about the largest monochromatic simple path. It only obstructs an exact edge-order realization. The orientation and realizability correspondence are proved independently in the sibling manuscript *Scope of the distinguished-coordinate counterexamples and edge-order realizability*.

## Exact limitation: exterior dependence

The theorem applies to the **direction-only** coloring (1), and in particular to every edge-ordered complete graph. For a general physical coloring \(c(F,(a,b,c))\), even assuming
\[
 c(F,(c,b,a))=1-c(F,(a,b,c)),\qquad
 c(\bar F,(a,b,c))=c(F,(a,b,c)),
 \tag{6}
\]
the comparison assigned to adjacent edges \(\{a,b\}\) and \(\{b,c\}\) can depend on the exterior coordinate bits of the physical face \(F\). Different windows along a cube path generally belong to different exterior fibers. Even if each fiber separately admits an acyclic comparison orientation, its topological order may depend on the fiber and therefore need not supply a common monotone original-graph path.

A sufficient **global-flatness hypothesis** for the proof is that one total edge order \(\prec\) of \(K_V\) realizes every comparison uniformly:
\[
 c(F,(a,b,c))=\mathbf1_{\{\{a,b\}\prec\{b,c\}\}}\quad
 \text{for every physical face }F.
 \tag{7}
\]
This is stronger than separate fiberwise acyclicity. Identifying a weaker coherent-transport hypothesis under which (3) persists is an explicit structural problem with a clear mathematical payoff.

## Relation to NORI-k switch amplification

The unbounded-switch multilevel coloring of ordered physical 3-faces uses the reversal-even rule \(h(a,b,c)=h(c,b,a)\), so it violates the extra boundary symmetry (6). The present theorem gives a strong lower bound on **long monochromatic paths** for an acyclic subclass of the reversal-odd boundary-compatible colorings; it makes no assertion for boundary tournaments with directed cycles, and no assertion for arbitrary exterior-dependent colorings satisfying (6).

In particular, the old NORI3 obstruction does not imply an edge-ordered increasing-path obstruction. The near-linear bound (3) is an application of the published Bucić–Kwan–Pokrovskiy–Sudakov–Tran–Wagner theorem, **not** a new lower bound for altitude. The contribution here is the exact incidence- and face-consistent transfer and its explicit boundary on possible counterexamples.

## References

M. Bucić, M. Kwan, A. Pokrovskiy, B. Sudakov, T. Tran, A. Z. Wagner, *Nearly-linear monotone paths in edge-ordered graphs*, Israel Journal of Mathematics **238** (2020), 663–685. DOI: 10.1007/s11856-020-2035-7. arXiv:1809.01468.

See also the companion NORI research manuscript *Scope of the distinguished-coordinate counterexamples and edge-order realizability* for the exact correspondence between boundary 3-tournaments and orientations of \(L(K_n)\).

## Directed-pair rank rigidity and quantitative boundary defects

The following rigidity result closes a natural attempt to enlarge the edge-ordered boundary-tournament class by assigning asymmetric scores to *ordered* pairs.

**Theorem (directed-pair score symmetrization).** Let \(V\) be a finite set, and let \(\lambda(a,b)\) take values in an arbitrary totally ordered set for all distinct \(a,b\in V\). Define
\[
h(a,b,c)=\mathbf 1\{\lambda(a,b)<\lambda(b,c)\},\qquad a,b,c\ \text{distinct}.
\tag{8}
\]
If \(h(c,b,a)=1-h(a,b,c)\) for every ordered triple, then there exists one total order \(\prec\) of the undirected edges of \(K_V\) for which
\[
h(a,b,c)=1\quad\Longleftrightarrow\quad\{a,b\}\prec\{b,c\}.
\tag{9}
\]
Conversely, every boundary tournament induced by a global edge order admits the representation (8).

**Proof.** Because \(V\) is finite, replace each \(\lambda\)-value by its rank among the \(m\) distinct values attained by \(\lambda\). This preserves all strict and weak comparisons. Write \(\rho(a,b)\in\{1,\ldots,m\}\) for the resulting rank and put
\[
s(\{a,b\})=\rho(a,b)+\rho(b,a).
\tag{10}
\]
If \(h(a,b,c)=1\), then \(\rho(a,b)<\rho(b,c)\). The reversal identity gives \(h(c,b,a)=0\), so \(\rho(c,b)\ge\rho(b,a)\). Adding yields
\[
s(\{a,b\})<s(\{b,c\}).
\]
If \(h(a,b,c)=0\), apply the previous argument to the reversed triple, for which \(h(c,b,a)=1\), to obtain the reverse *strict* score inequality. Consequently every pair of incident edges has distinct \(s\)-scores and the strict inequalities induced by \(h\) coincide with their comparisons under \(s\). Sort undirected edges by \(s\), breaking possible ties only between disjoint edges. This produces the total edge order (9). Conversely, assign to both directed copies \((a,b)\) and \((b,a)\) the rank of \(\{a,b\}\) in any prescribed total edge order. Formula (8) reproduces its adjacent-edge comparisons. \(\square\)

**Corollary (nearly-linear positive tight paths).** Every reversal-odd boundary tournament represented by directed-pair strict comparisons (8) admits a positive vertex-simple tight path on \(n/2^{O(\sqrt{\log n\log\log n})}\) vertices, by the preceding acyclic-transfer theorem and the Bucić–Kwan–Pokrovskiy–Sudakov–Tran–Wagner monotone-path theorem. The original graph vertices are distinct; their labels provide distinct cube directions in the corresponding direction-only physical coloring.

The rigidity admits a quantitative form *without assuming reversal oddness*. For each unordered triple \(\{a,b,c\}\), say it is **defective** if at least one of its three possible middle vertices violates \(h(c,b,a)=1-h(a,b,c)\), with \(h\) still defined by (8). Let \(B\) be the number of defective unordered triples.

**Theorem (rank-height/defect tradeoff).** If the directed score \(\lambda\) takes \(m\) distinct values, then
\[
\boxed{B\ \ge\ \frac n6\left(\frac{(n-1)^2}{2m-1}-(n-1)\right)_+.}
\tag{11}
\]
In particular, if there are no defective triples then
\[
\boxed{m\ge \lceil n/2\rceil;}
\tag{12}
\]
if \(m=O(\log n)\) along a family with \(n\to\infty\), then \(B=\Omega(n^3/\log n)\).

**Proof.** Normalize all distinct \(\lambda\)-values to consecutive ranks \(1,\ldots,m\) as in the preceding theorem and use the same symmetric integer scores (10), which range from \(2\) to \(2m\). If two incident edges \(\{a,b\},\{b,c\}\) have equal symmetric score, reversal oddness at middle vertex \(b\) is impossible: otherwise the first theorem's strict-inequality argument, which uses only reversal oddness at that triple, would force one of the two unequal strict orders. Fix \(b\), and let \(d_t(b)\) count its \(n-1\) incident edges with score \(t\in\{2,\ldots,2m\}\). Every colliding pair of edges produces a reversal violation with middle \(b\). By Cauchy–Schwarz,
\[
\begin{aligned}
\sum_{t=2}^{2m}\binom{d_t(b)}2
&=\frac12\left(\sum_t d_t(b)^2-(n-1)\right)\\
&\ge\frac12\left(\frac{(n-1)^2}{2m-1}-(n-1)\right).
\end{aligned}
\]
Summing over \(b\) counts at most three violating middle-vertex choices for each defective unordered triple. Dividing by three and taking the nonnegative part gives (11). If \(B=0\), every star has \(n-1\) pairwise distinct symmetric integer scores in a set of size \(2m-1\), implying (12). The asymptotic defect bound follows by substituting \(m=O(\log n)\) into (11). \(\square\)

**Scope and consequence.** The proof holds for arbitrary asymmetric ordered-pair scores, arbitrary discrete ranking/tie patterns, and (by rank normalization) every totally ordered score set, including lexicographically ordered tuples. It is an exact no-go for transferring an \(O(\log n)\)-height *directed-pair strict-comparison* construction to an ordinary boundary 3-tournament. It does **not** imply global edge-orderability for arbitrary boundary 3-tournaments, because their line-graph comparison orientations can contain directed cycles. It makes no assertion about unrestricted exterior-dependent physical 3-face colorings or unrestricted NORI1. A full ordinary boundary theorem must exploit mechanisms beyond strict comparisons of directed-pair potentials.
