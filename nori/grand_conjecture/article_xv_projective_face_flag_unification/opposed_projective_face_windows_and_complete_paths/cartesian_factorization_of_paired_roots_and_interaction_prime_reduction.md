# Cartesian factorization of paired roots and interaction-prime reduction

### Product factorization of paired roots and the prime closure target

Let \(f\) be an arbitrary binary coloring of the undirected edges of \(Q_d\), without antipodal hypotheses. For a root \(z\in Q_d\), let \(z\in A(f)\) mean that a full dimension-simple geodesic from \(z\) to \(\bar z\) has color word \(0^p1^{d-p}\) for some \(0\le p\le d\). Both monochromatic words are admitted, corresponding to empty initial or final blocks. Define the **paired-root set**
\[
P(f)=A(f)\cap\bar A(f)
=\{z:z\in A(f)\text{ and }\bar z\in A(f)\}.
\tag{1}
\]
By the universal bridge equivalence in the gauge-criticality Subsection, NORI1 in dimension \(d+1\) is equivalent to \(P(f)\ne\varnothing\) for every \(d\)-cube edge coloring \(f\).

**Theorem 1 (Cartesian factorization).** Let \(f\) and \(g\) be arbitrary edge colorings of \(Q_a\) and \(Q_b\). Define \(f\boxtimes g\) on \(Q_{a+b}=Q_a\times Q_b\) by coloring edges moving in the first block according to \(f\) and edges moving in the second block according to \(g\), independently of the opposite block. Then
\[
\boxed{A(f\boxtimes g)=A(f)\times A(g),\qquad
P(f\boxtimes g)=P(f)\times P(g).}
\tag{2}
\]

*Proof.* Restrict any full geodesic \(P\) in \(Q_a\times Q_b\) to the steps moving in the first factor. Its subsequence is a full dimension-simple geodesic from the first root to its antipode, and its colors are precisely the corresponding \(f\)-edge colors. The same applies to the second factor. Every subsequence of a word \(0^*1^*\) is itself of this form, proving \(A(f\boxtimes g)\subseteq A(f)\times A(g)\). Conversely, take paths in the factors whose words are respectively \(0^{p}1^{a-p}\) and \(0^{q}1^{b-q}\). Traverse the zero prefixes in both factors, followed by their one suffixes in both factors. The result is a full dimension-simple product geodesic with color word \(0^{p+q}1^{a+b-p-q}\), proving equality. Antipodal complementation acts componentwise on roots, so intersecting with the antipodal images gives the second identity. QED.

**Theorem 2 (exponentially sparse favorable and paired roots).** Let \(h\) color the two edges incident with \(00\in Q_2\) by 1 and the two edges incident with \(11\in Q_2\) by 0. Then
\[
A(h)=\{01,10,11\},\qquad P(h)=\{01,10\}.
\tag{3}
\]
For the \(k\)-fold Cartesian product \(h^{\boxtimes k}\) on \(Q_{2k}\),
\[
\boxed{
|A(h^{\boxtimes k})|=3^k,\quad
|P(h^{\boxtimes k})|=2^k,\quad
\frac{|A|}{2^{2k}}=(3/4)^k,\quad
\frac{|P|}{2^{2k}}=(1/2)^k.
}\tag{4}
\]
In particular there is no positive dimension-independent lower bound on the *density* of favorable roots or of paired roots, even within colorings satisfying the paired-root conclusion. Moreover the number of antipodal pairs contained in \(P(h^{\boxtimes k})\) equals \(2^{k-1}\), which is even for every \(k\ge2\).

*Proof.* From root \(00\), both possible two-step full geodesics have word \(10\), so \(00\notin A(h)\). From \(11\), both have word \(01\), so \(11\in A(h)\). From \(01\) or \(10\), one order gives word \(00\) and the other gives word \(11\), so both roots belong to \(A(h)\). The paired roots are \(01,10\), giving (3). Apply Theorem 1 repeatedly to obtain (4) and divide by the \(4^k\) total roots. The antipodal involution on \(P\) has no fixed root, giving \(2^{k-1}\) orbits. QED.

**Theorem 3 (canonical interaction-prime decomposition).** For any undirected edge coloring \(f\) of \(Q_d\), write \(f_i(x)\) for the color of the direction-\(i\) edge at \(x\), so \(f_i(x)=f_i(x\oplus e_i)\). For distinct dimensions \(i,j\), put
\[
\partial_j f_i(x)=f_i(x)+f_i(x\oplus e_j)\pmod2.
\]
Form the **interaction graph** \(\Gamma(f)\) on the \(d\) dimensions, joining \(i\) and \(j\) if either \(\partial_jf_i\) or \(\partial_if_j\) is nonzero somewhere. If \(C_1,\ldots,C_t\) are its connected components, there are uniquely determined factor colorings \(f^{(s)}\) such that
\[
\boxed{f=\boxtimes_{s=1}^t f^{(s)},\qquad
A(f)=\prod_{s=1}^t A(f^{(s)}),\qquad
P(f)=\prod_{s=1}^t P(f^{(s)}).}
\tag{5}
\]
Consequently the paired-root conjecture for all cube colorings is equivalent to its restriction to colorings whose interaction graph is connected. Any counterexample of least dimension must have connected interaction graph.

*Proof.* If \(i\in C_s\) and \(j\notin C_s\), then \(\partial_j f_i\equiv0\). Hence \(f_i\) is invariant under changing any bit outside \(C_s\); therefore it depends only on the bits within \(C_s\). This defines the factor coloring \(f^{(s)}\), and proves the product representation. Conversely, any product decomposition yields no interaction edges between different factors. Thus the component partition is the unique finest product decomposition, and (5) follows from Theorem 1. If a product has no paired root, one factor has no paired root; a minimum-dimension counterexample cannot have more than one factor. QED.

**Closure program and its limits.** The bridge theorem reduces NORI1 to paired-root existence, while Theorem 3 further reduces it to **interaction-connected** edge colorings. Theorems 1-2 rigorously rule out two tempting shortcuts: pigeonholing from a fixed positive favorable-root density and an odd-parity count of antipodal paired-root orbits. A prospective closure proof should instead detect an invariant of the *antipodal arrangement* of feasible roots that is preserved under Cartesian products and is forced for interaction-connected colorings. The interaction graph records all cross-dimension dependence (square derivatives), offering a natural induction parameter tied to dimension-simplicity rather than the total number of local switches. The result by itself does not prove the paired-root conjecture for connected interaction graphs.

## Interaction-connected sparse-root colorings

The previous product construction has disconnected interaction graph. A one-dimensional coupling shows that even restricting to interaction-prime colorings cannot support a uniform positive density lower bound for favorable roots.

**Theorem 4 (connected interactions with exponentially sparse roots).** For every \(k\ge1\), there is an edge coloring \(F_k\) of \(Q_{2k+1}\) for which:
1. its interaction graph \(\Gamma(F_k)\) is connected (indeed, contains a spanning star);
2. \(P(F_k)\ne\varnothing\);
3. its favorable-root and paired-root densities obey
\[
\boxed{
\frac{|A(F_k)|}{2^{2k+1}}\le(3/4)^k,\qquad
\frac{|P(F_k)|}{2^{2k+1}}\le(1/2)^k.
}
\tag{6}
\]
Thus both densities tend to zero even for interaction-connected colorings that satisfy the paired-root conclusion.

*Proof.* Take the \(2k\)-dimensional product coloring \(f_k=h^{\boxtimes k}\) of Theorem 2. Extend it to \(Q_{2k+1}=Q_{2k}\times Q_1\) by retaining all its old-dimension edge colors unchanged in both layers, and assigning to the new-direction edge above \(x\in Q_{2k}\) the color
\[
F_k(x,\mathrm{new})=\sum_{i=1}^{2k}x_i\pmod2.
\tag{7}
\]
This is well-defined on the unoriented new edge, because it is independent of the new bit. Its derivative in each old dimension equals one. Therefore the interaction graph contains every edge joining the new dimension to an old dimension and is connected.

Take any full \(0^*1^*\) geodesic in the enlarged cube and delete its unique step in the new dimension. All remaining old steps form a full geodesic in \(Q_{2k}\), with the same color subsequence, hence remain \(0^*1^*\). Therefore
\[
A(F_k)\subseteq A(f_k)\times\{0,1\}
\]
and, after antipodal intersection,
\[
P(F_k)\subseteq P(f_k)\times\{0,1\}.
\]
Using \(|A(f_k)|=3^k\), \(|P(f_k)|=2^k\) gives the two density bounds.

To show a paired root exists, take any \(x\in P(f_k)=\{01,10\}^k\). Every such \(x\) has Hamming weight \(k\), and its antipode in \(Q_{2k}\) has the same Hamming weight \(k\). Thus the new-direction edge color at \(x\) and \(\bar x\) is the common bit \(k\bmod2\). If this bit is zero, insert the new-direction step **before** a \(0^*1^*\) old path from each of \(x,\bar x\); if it is one, insert the step **after** each old path. The resulting geodesics in \(Q_{2k+1}\) still have word \(0^*1^*\), from both antipodal roots \((x,t)\) and \((\bar x,1-t)\). Hence \(P(F_k)\ne\varnothing\). QED.

**Corollary 5 (absence of a rootwise orientation covering).** Let \(A_1(f)\) denote roots supporting a \(1^*0^*\) geodesic. Reversal of full paths gives \(A_1(f)=\bar A(f)\). For the product coloring \(f_k=h^{\boxtimes k}\),
\[
\boxed{|A(f_k)\cup A_1(f_k)|=2\cdot3^k-2^k.}
\tag{8}
\]
The fraction of roots supporting *either* one-switch orientation tends to zero. The same upper bound (after dividing by the corresponding total vertex count) holds for the connected extension \(F_k\), because restriction to old directions preserves both monotone color-word types.

*Proof.* By Theorem 2, \(|A(f_k)|=3^k\) and \(|A(f_k)\cap\bar A(f_k)|=2^k\). Inclusion–exclusion gives (8). Restriction of any full \(1^*0^*\) path to the old dimensions gives a path of that type in \(f_k\), and similarly for \(0^*1^*\). QED.

**Implication for closure.** Even a prime-interaction hypothesis cannot force a fixed positive density of favorable roots or a rootwise choice of one of the two monotone orientations. Cartesian factorization remains useful as an induction simplification, but the missing theorem has to use the precise antipodal *placement* and mutual compatibility of the favorable roots rather than their abundance or mere interaction-connectedness.

## Seam insertion and the directed dependency cycle core

**Lemma 6 (unrestricted seam insertion).** Let \(f\) be an arbitrary binary edge coloring of \(Q_d\). Color both horizontal layers of \(Q_{d+1}=Q_d\times Q_1\) identically by \(f\), and color the vertical edge over \(x\) arbitrarily by \(h(x)\). For \(F\) so obtained,
\[
\boxed{A(F)=A(f)\times\{0,1\},\qquad P(F)=P(f)\times\{0,1\}.}
\tag{9}
\]

*Proof.* Restrict a full \(0^*1^*\) geodesic under \(F\) to the old directions. Its subsequence remains a full antipodal geodesic in \(Q_d\), with unchanged colors, hence has the same monotone word pattern. Conversely, let a favorable full path under \(f\) have word \(0^p1^{d-p}\), allowing \(p=0,d\). Starting at \((z,t)\), traverse its first \(p\) edges in layer \(t\), traverse the new vertical edge at the switch vertex \(v\), then traverse its final \(d-p\) old-direction edges in layer \(1-t\). If \(h(v)=0\), the extra edge extends the zero prefix; if \(h(v)=1\), it starts or extends the one suffix. Either way the full path is favorable, regardless of \(h\) and \(t\). Its endpoint is \((\bar z,1-t)\). This proves the first equality, and intersection with the componentwise antipodal images yields the second. QED.

**Theorem 7 (directed dependency sink elimination).** For an arbitrary edge coloring \(f\) of \(Q_d\), define a digraph \(\vec\Gamma(f)\) on dimensions by placing an arc \(i\to j\) if \(i\ne j\) and
\[
\partial_i f_j(x):=f_j(x)+f_j(x\oplus e_i)
\]
is nonzero at some cube vertex. If \(i\) has outdegree zero, the coloring on every other direction is independent of the \(i\)-th bit. Deleting that dimension gives a smaller coloring \(g\), with
\[
\boxed{A(f)=A(g)\times\{0,1\},\qquad P(f)=P(g)\times\{0,1\}.}
\tag{10}
\]
Repeated sink deletion gives an induced core with no outdegree-zero vertices, preserving paired-root existence.

*Proof.* An absent arc \(i\to j\) states precisely that the \(j\)-edge colors are invariant under the \(i\)-bit flip. The \(i\)-edge colors themselves are arbitrary functions of the other bits. Thus Lemma 6 applies. Removing a dimension does not change interactions between remaining dimensions; repeating gives the core. QED.

**Corollary 8 (full-root theorem for acyclic dependencies).** If \(\vec\Gamma(f)\) is acyclic, every vertex of \(Q_d\) supports a complete \(0^*1^*\) geodesic, and
\[
\boxed{A(f)=P(f)=V(Q_d).}
\tag{11}
\]

*Proof.* Remove sink dimensions successively in an acyclic digraph, reaching the zero-dimensional cube, whose empty path is favorable. Each inverse seam insertion duplicates its entire favorable-root set by Lemma 6. Hence every root is favorable and paired. QED.

**Corollary 9 (cycle core is necessary for minimal failure).** If the paired-root conjecture is false, any counterexample of minimum dimension has a directed dependency graph with minimum outdegree at least one, so it contains a directed cycle. By the earlier product theorem, its underlying undirected interaction graph may also be assumed connected.

*Proof.* A sink would reduce the failure to fewer dimensions without changing paired-root existence, contradicting minimal dimension. A finite digraph of minimum outdegree one has a directed cycle. Disconnected undirected interaction graphs split as Cartesian products, and failure in a product implies failure in a factor. QED.

**Corollary 10 (connected sparse-root gadget revisited).** The interaction-connected coloring \(F_k\) in Theorem 4 has identical old edges across its added dimension. Thus the earlier root-count upper estimates are equalities:
\[
\boxed{|A(F_k)|=2\cdot3^k,\qquad |P(F_k)|=2^{k+1}.}
\tag{12}
\]
Its added direction has outdegree zero in \(\vec\Gamma(F_k)\), illustrating that undirected interaction-connectedness is weaker than directed sink irreducibility.

**Closure program.** This is a proof-preserving reduction for *every* arbitrary lower-cube coloring: strip all sink dimensions without changing the paired-root question. It rules out all directed-acyclic colorings and isolates a cyclic dependency core as the first remaining case. The seam insertion operation preserves dimension-simplicity and works regardless of the added edge's color. Root density cannot replace this reduction, since root densities in the preceding product and connected gadget examples tend to zero. The cyclic-core paired-root conjecture remains open.### The full two-layer arm interface and inductive closure target

Let \(F\) be any binary edge coloring of \(Q_{d+1}=Q_d\times\{0,1\}\), described by horizontal-layer colorings \(f_0,f_1\) and vertical-edge colors \(h(y)\). Fix a root \((z,t)\). For a subset \(U\subseteq[d]\), put \(y=z\oplus\mathbf1_U\). A directed *zero arm* uses only color-zero edges; a *one arm* only color-one edges; a *monotone arm* has color word \(0^*1^*\). Each arm follows dimensions from its prescribed subset without repetition; empty arms are allowed.

**Theorem 11 (two-layer interface equivalence).** The root \((z,t)\) admits a full dimension-simple \(0^*1^*\) geodesic if and only if there exists \(U\subseteq[d]\) such that one of the following holds:

(i) \(h(y)=0\), there is a zero arm from \(z\) to \(y\) in layer \(t\) using all and only \(U\), and there is a monotone arm from \(y\) to \(\bar z\) in layer \(1-t\) using all and only \(U^c\).

(ii) \(h(y)=1\), there is a monotone arm from \(z\) to \(y\) in layer \(t\) using all and only \(U\), and there is a one arm from \(y\) to \(\bar z\) in layer \(1-t\) using all and only \(U^c\).

The root is paired if and only if the criterion holds both at \((z,t)\) and its antipode \((\bar z,1-t)\), with independently chosen seam subsets.

*Proof.* Any full geodesic uses the new vertical dimension precisely once. Before it, the old steps use a subset \(U\) and end at \(y=z\oplus\mathbf1_U\); after it, the remaining steps use \(U^c\) and end at \(\bar z\). If the vertical bit is zero, any earlier color one would break the nondecreasing word, so the initial arm must be all zero while the final arm can be monotone. If it is one, any later zero would break the word, so the final arm must be all one while the initial arm can be monotone. Conversely each indicated pair of arms concatenated across the vertical edge forms a full dimension-simple monotone-color geodesic. QED.

**Proposition 12 (order-compatible seam suffices).** Suppose a full dimension order \(\pi\) starting at \(z\) has words \(0^{p_0}1^{d-p_0}\) in layer \(f_0\) and \(0^{p_1}1^{d-p_1}\) in layer \(f_1\), where \(p_0\ge p_1\). Then for **every** vertical coloring \(h\), the extended cube has a full favorable geodesic from \((z,0)\). The new step can be inserted at any rank \(r\) with \(p_1\le r\le p_0\).

*Proof.* Traverse the first \(r\) old directions in layer zero, the vertical edge at the resulting vertex, then the remaining old directions in layer one. The first block is entirely zero since \(r\le p_0\); the last block is entirely one since \(r\ge p_1\). The inserted edge may have either color without creating a decrease. Every dimension occurs once. QED.

**Induction blueprint.** The universal bridge equivalence reduces NORI1 in dimension \(d+1\) to paired-root existence for arbitrary horizontal layer colorings and vertical bits. To induct from dimension \(d\), it would suffice to prove that the two layerwise monotone-arm systems always have complementary seam certificates simultaneously at some antipodal roots, as characterized by Theorem 11. The newly proved seam-insertion lemma settles the whole two-layer problem when \(f_0=f_1\), regardless of vertical colors; the order-interlacing proposition supplies a further sufficient certificate for one orientation. The missing assertion is a coupling of directed arm reachability under distinct layers, while preserving the partition of dimensions before and after the crossing. This assertion is not proved here.

## Closing paired roots on functional cyclic cores with arbitrary nonlinear tails

The directed sink reduction and the existing affine one-dependency theorem combine to settle a substantial family that retains cyclic dependencies and allows unrestricted nonlinear color functions on all removable dimensions.

**Theorem 13 (paired roots for disjoint directed-cycle cores).** Let \(f\) be any binary coloring of the undirected edges of \(Q_d\). Repeatedly remove dimensions of outdegree zero in its directed dependency graph \(\vec\Gamma(f)\), as in Theorem 7, and let \(C\) be the retained dimension set. Assume the induced directed dependency graph on \(C\) is a disjoint union of directed cycles of lengths at least two. Then
\[
\boxed{P(f)\ne\varnothing.}
\tag{13}
\]
Indeed, on the core, if the cycles have lengths \(\ell_1,\ldots,\ell_r\), then at least
\[
\boxed{\prod_{j=1}^r(2^{\ell_j}-2)}
\tag{14}
\]
different roots admit a **monochromatic zero** full geodesic both from themselves and from their antipodes. On the original \(Q_d\), each of these paired core roots lifts to \(2^{d-|C|}\) paired roots supporting \(0^*1^*\) complete geodesics. The case \(C=\varnothing\) is covered by the full-root acyclic theorem.

*Proof.* Theorem 7 shows that deletion of each sink direction preserves the favorable-root and paired-root sets, after projection to the remaining dimensions. Thus it suffices to analyze the restricted core coloring \(g\) on \(Q_C\).

For every \(i\in C\), the core dependency digraph has precisely one incoming arc, from its predecessor \(p(i)\ne i\) on a directed cycle. Therefore the color of a direction-\(i\) edge is independent of all old dimensions except \(p(i)\), and independent of bit \(i\) by undirected-edge consistency. Since the derivative in predecessor direction is nonzero, the color is necessarily
\[
g_i(x)=a_i+x_{p(i)}\pmod2
\tag{15}
\]
for some constant bit \(a_i\).

Choose a root \(z\in Q_C\), and define \(b_i=a_i+z_{p(i)}\). For an order of the dimension labels, the color seen when dimension \(i\) is traversed is \(b_i+\mathbf1_{\{p(i)\text{ occurs earlier than }i\}}\). Thus an all-zero geodesic from \(z\) exists precisely when the precedence constraints
\[
\mathbf1_{\{p(i)\text{ before }i\}}=b_i
\tag{16}
\]
admit a linear ordering. On a directed dependency cycle, these constraints are inconsistent only when they orient every relation cyclically in one of the two directions, equivalently when all bits \(b_i\) on that cycle are equal. If the bits are not all equal, the resulting orientation of that cycle is acyclic and admits a topological ordering. Different dependency cycles are disjoint, so such orderings can be concatenated. Consequently an all-zero geodesic from \(z\) exists whenever the \(b\)-sequence is nonconstant on each cycle.

At the antipodal root \(\bar z\), the values become \(b_i+1\). Complementing all bits preserves nonconstancy, so the same acyclicity argument supplies an all-zero geodesic from \(\bar z\), possibly under a different dimension order. Thus every such \(z\) is a paired root.

On a cycle of length \(\ell\), the map \(z\mapsto(b_i)_{i\text{ in cycle}}\) is a bijection because \(p\) permutes that cycle. Precisely two of its \(2^\ell\) assignments are constant. The number of roots satisfying all cycle conditions is therefore at least the product (14). Reinsert each deleted dimension using Lemma 6: favorable-root and paired-root sets duplicate across its two possible starting bits without requiring any restriction on that dimension's own edge-color function. This establishes (13) and the asserted lifted count. QED.

**Corollary 14 (in-degree-one cyclic core).** The conclusion holds whenever the sink-deletion core has **indegree at most one at every vertex**. Since every retained vertex has outdegree at least one and the total indegree equals the total outdegree, this forces indegree and outdegree one everywhere, and hence a union of directed cycles.

**Closure implication.** In any least-dimensional counterexample to paired-root existence, the dependency digraph has no sink and cannot be a disjoint union of directed cycles. In particular it must have a vertex of indegree at least two, or an equivalent branching feature. The proof extends the established affine one-predecessor construction to arbitrary nonlinear colorings outside the directed cyclic core, relying on the seam-insertion identity rather than on color density. This is not a proof for general branching cores.

## Fiberwise seam insertion removes globally cyclic dependency blocks

Let \(Q_{a+b}=Q_A\times Q_B\) be a Cartesian splitting of the dimensions. Let \(F\) be an arbitrary binary edge coloring such that every edge moving in \(A\) has a color depending only on its \(A\)-vertex, not on the \(B\)-bits; these \(A\)-edges induce a coloring \(f\) of \(Q_A\). For each \(x\in Q_A\), let \(g_x\) denote the induced coloring of the \(B\)-dimensional fiber \(\{x\}\times Q_B\). The \(g_x\) may differ arbitrarily with \(x\).

**Theorem 15 (all-root fiber gluing).** If
\[
\boxed{A(g_x)=V(Q_B)\qquad\text{for every }x\in Q_A,}
\tag{17}
\]
then
\[
\boxed{A(F)=A(f)\times V(Q_B),\qquad
P(F)=P(f)\times V(Q_B).}
\tag{18}
\]
Consequently an arbitrary collection of \(B\)-directions can be removed without changing paired-root nonemptiness whenever the outer edge colors are independent of them and each fixed outer-vertex fiber has all roots favorable.

*Proof.* Take any full \(0^*1^*\) geodesic of \(F\) and erase all steps in dimensions \(B\). Since the remaining \(A\)-edge colors are independent of \(B\), their sequence is unchanged and retains the form \(0^*1^*\). This gives \(A(F)\subseteq A(f)\times V(Q_B)\).

Conversely, fix \(z\in A(f)\) and any \(t\in Q_B\). Choose a full \(A\)-geodesic from \(z\) to \(\bar z\) whose word is \(0^p1^{a-p}\), and let \(v\) be its vertex after the first \(p\) edges. By (17) the fiber coloring \(g_v\) admits a full \(B\)-geodesic from \(t\) to \(\bar t\) with word \(0^q1^{b-q}\). Insert this full fiber path at \(v\), between the zero prefix and one suffix of the \(A\)-path. The resulting word is \(0^{p+q}1^{a+b-p-q}\); all dimensions in \(A\cup B\) are used once, and the endpoint is \((\bar z,\bar t)\). Thus the reverse inclusion holds. Intersecting with antipodal images gives the formula for \(P\). QED.

**Corollary 16 (fiberwise acyclic criterion).** The conclusion holds whenever, for every \(x\in Q_A\), the directed dependency graph **within the fiber** \(g_x\) is acyclic. The dependency graph of the full coloring \(F\) may nonetheless contain directed cycles and vertices with several incoming dependencies.

*Proof.* Corollary 8 gives \(A(g_x)=V(Q_B)\) for every fiber. Apply Theorem 15. QED.

**Example 17 (a sink-free branching dependency graph eliminated by fibers).** Split three dimensions as \(A=\{a\}\) and \(B=\{u,v\}\). Color every \(a\)-edge zero, independent of \(u,v\). For the other directions set
\[
\begin{array}{c|cc}
a&F_u(a,u,v)&F_v(a,u,v)\\ \hline
0&0&u\\
1&v&0
\end{array}
\tag{19}
\]
where each expression is independent of the bit in its own direction and hence defines an undirected edge coloring.

When \(a=0\), the fiber dependency graph has one arc \(u\to v\); when \(a=1\), it has one arc \(v\to u\). Both are acyclic, so all four roots of each \(Q_2\) fiber are favorable. However the dependency digraph of the full \(Q_3\) coloring contains \(u\to v\), \(v\to u\), \(a\to u\) and \(a\to v\). It has no sink, possesses a directed two-cycle, and has branching at \(a\). The preceding single-direction sink reduction therefore cannot remove any dimension. Nevertheless Theorem 15 applies to the entire block \(B\), with the base \(a\)-edge constantly zero, and proves
\[
\boxed{A(F)=P(F)=V(Q_3).}
\]
This illustrates that fiberwise gluing handles some cyclic dependency cores with branching, not merely acyclic global dependency digraphs.

**Closing direction.** Theorem 15 reframes the remaining induction obstacle: when an external block affects its internal colorings, gluing succeeds if the fibers are root-universally favorable. To extend it beyond acyclic fibers, one needs a weaker two-fiber antipodal-intersection principle that permits fibers having only some favorable roots. This is precisely where the paired-root theorem is stronger than all-root feasibility; the product examples show that all-root feasibility cannot be demanded in full generality.

## Sink strongly connected cycle elimination: closure reduces to internal branching

The preceding sink-dimension reduction and disjoint-cycle theorem leave a gap for interactions **between** different directed cycles. The following fiberwise overlap principle removes that gap without assuming any independence of the cycle edge colors from the outside bits.

For an arbitrary binary edge coloring f of \(Q_d\), write \(A(f)\) for the starting roots supporting a full \(0^*1^*\) geodesic and \(P(f)=A(f)\cap\overline{A(f)}\) for its paired roots.

**Lemma 18 (paired-root gluing across a fiber block).** Suppose \(Q_{a+b}=Q_A\times Q_B\) carries a coloring F whose A-direction edge colors depend only on the A-vertex, inducing f on \(Q_A\). For each \(x\in Q_A\), let \(g_x\) be the B-fiber coloring above x. Assume
\[
\boxed{A(g_x)\cap\overline{A(g_y)}\ne\varnothing
\quad\text{for all }x,y\in Q_A.}
\tag{20}
\]
Then
\[
\boxed{P(F)\ne\varnothing\iff P(f)\ne\varnothing.}
\tag{21}
\]
More quantitatively, if the intersections in (20) all have cardinality at least L, then \(|P(F)|\ge L|P(f)|\).

*Proof.* Any full favorable path in F projects, after deleting B-direction steps, to a full favorable path in f. Thus a paired root of F projects to a paired root of f.

Conversely choose \(z\in P(f)\). Take full favorable A-paths from \(z\) and from \(\bar z\), and denote the A-vertices at their respective color switch seams by x and y; seam vertices exist even for monochromatic paths by allowing an empty prefix or suffix. Choose \(t\in A(g_x)\cap\overline{A(g_y)}\). Insert a full favorable B-path from t at the first seam and a full favorable B-path from \(\bar t\) at the second seam. Since each fiber path has a \(0^*1^*\) color word, its insertion between the zero prefix and one suffix of the A-path preserves monotonicity and uses every B-direction once. Hence \((z,t)\) and \((\bar z,\bar t)\) are both favorable in F, proving pairedness. Distinct t give distinct paired roots. Since z ranges over all P(f), this proves the quantitative statement as well. \(\square\)

**Lemma 19 (all-root except one for a directed dependency cycle).** Let g color the undirected edges of \(Q_m\), \(m\ge2\), and suppose its directed dependency graph is a subgraph of a fixed directed cycle of length m. Then
\[
\boxed{|Q_m\setminus A(g)|\le1.}
\tag{22}
\]
For \(m=1\), every root is favorable.

*Proof.* If one dependency arc of the cycle is missing, the directed dependency graph is acyclic, and the established acyclic-dependency theorem gives \(A(g)=Q_m\). Otherwise each direction i has one predecessor \(p(i)\), with \(\partial_{p(i)}g_i\ne0\) and no other dependencies. Thus
\[
g_i(u)=a_i+u_{p(i)}
\]
for constant bits a_i. At root z put \(b_i=a_i+z_{p(i)}\). During a dimension order \(\pi\), the edge in direction i has color \(b_i+[p(i)\text{ occurs before }i]\).

If the bits b_i are not all equal, orient each relation between p(i) and i to make the edge color zero. The resulting orientation of the underlying directed cycle cannot itself be a directed cycle, as that would require all b_i equal. It therefore admits a total order, yielding an all-zero full geodesic.

If all b_i equal zero, order dimensions along the reverse cyclic dependency, so that every predecessor occurs *after* its direction except for the last direction. The resulting geodesic color word is \(0^{m-1}1\), which is favorable.

If all b_i equal one, the first direction of every order has color one (its predecessor has not appeared), while the final direction has color zero (its predecessor has appeared), so no order is favorable. Since the predecessor map p permutes the dimension set, there is only one root with all b_i=1. This proves (22). \(\square\)

**Theorem 20 (SCC cycle elimination and root-count lower bound).** Let f be any binary edge coloring of \(Q_d\), with directed dependency graph \(\vec\Gamma(f)\). Suppose **every strongly connected component** is either a singleton or a directed simple cycle (of length at least two). Let the nontrivial components have sizes \(m_1,\ldots,m_s\), and let there be r singleton components. Then
\[
\boxed{
|P(f)|\ge2^r\prod_{j=1}^s(2^{m_j}-2)>0.}
\tag{23}
\]
In particular every coloring with a directed pseudoforest condensation of cyclic components satisfies the paired-root theorem and hence the corresponding NORI1 bridge conclusion. Edges between distinct components may be arbitrarily numerous and their color dependence nonlinear.

*Proof.* The condensation of any finite directed graph is acyclic and has a sink component B. No directed dependency arrow leads from B to its complement A, so all A-direction edge colors are independent of B-bits. For every fixed outer vertex x, the dependency graph of the B-fiber g_x is a subgraph of the component's induced dependency graph. If B is a singleton then \(A(g_x)=Q_B\). If B is a directed cycle of size m, Lemma 19 shows that each fiber favorable-root set omits at most one root. Thus for every x,y, the intersection \(A(g_x)\cap\overline{A(g_y)}\) has size at least \(2^m-2\), positive for m>=2. Apply Lemma 18 to remove B, preserving paired-root nonemptiness and multiplying the lower bound for the number of paired roots by two for a singleton or \(2^m-2\) for a cyclic component. Repeat along the condensation DAG. At the empty cube there is one paired root (the empty path), proving (23). \(\square\)

**Corollary 21 (structural minimum-counterexample obstruction).** If the paired-root theorem—and hence NORI1—fails, an edge coloring of least dimension with no paired root has a **strongly connected dependency component with branching inside the component**: it is neither a singleton nor a directed simple cycle. This is strictly stronger than ruling out globally acyclic graphs, disconnected interactions, sinks, or an entire digraph that is a disjoint union of cycles. Arbitrarily complicated nonlinear branching *between* cyclic strongly connected components cannot produce a counterexample.

**Research significance.** A proof of paired-root existence for a single strongly connected branching dependency core, stable under arbitrary exterior fiber parameters, is now the well-delimited missing step. The obstruction is not a large family of geodesics but the interaction pattern of the directional Boolean derivatives within one component. The full theorem remains open for such components.

## A nonlinear single-branch dependency core has strictly more than half its roots favorable

The SCC reduction above settles directed simple cycles, but a first strongly connected branching pattern also admits a structural solution. Fix \(m\ge3\). Let the dimensions of a fiber be \(0,1,\ldots,m-1\), and suppose every non-hub direction i, \(1\le i<m\), has edge color
\[
\boxed{g_i(u)=a_i+u_{i-1},}
\tag{24}
\]
whereas the hub-direction color \(g_0(u)=h(u_1,\ldots,u_{m-1})\) is an **arbitrary Boolean function**. In particular the hub may depend nonlinearly on all other dimensions and receive arbitrarily many incoming dependency arcs. No assumption is made about the functional form of h. The non-hub predecessor derivatives in (24) are active for every input, not merely somewhere.

**Theorem 22 (single-branch favorable-root majority).** Every coloring of the displayed form satisfies
\[
\boxed{|A(g)|>2^{m-1}.}
\tag{25}
\]
More precisely, unless h is constant, one has
\[
\boxed{|A(g)|\ \ge 2^{m-1}+|\{u\in\{0,1\}^{m-1}:h(u)=0\}|.}
\tag{26}
\]
When h is constant, all roots are favorable.

*Proof.* For each starting root \(z\), prescribe that every direction i>=1 traverse a color-zero edge. This imposes the precedence relation
\[
[i-1\prec i]=a_i+z_{i-1}\quad(i=1,\ldots,m-1).
\tag{27}
\]
These comparisons orient the edges of the path \(0-1-\cdots-(m-1)\), so they always admit a total order.

If \(a_1+z_0=0\), the constraint at the first path edge orients \(1\prec0\). The hub vertex 0 is then a sink in this oriented path and can be placed **last** in a topological ordering. The non-hub edges have color zero, and the last hub edge has either color, giving a favorable word \(0^{m-1}0\) or \(0^{m-1}1\).

If \(a_1+z_0=1\), the constraint orients \(0\prec1\). The hub is a source in the oriented path and can be placed **first**. Its edge color is \(h(z_1,\ldots,z_{m-1})\), independent of z0. Whenever this bit is zero, all m edges in this order have color zero.

For each assignment of the other m−1 starting bits, one of the two choices of z0 belongs to the first case; the second choice is also favorable whenever h equals zero. This proves (26). If h is nonconstant it has at least one zero, giving (25). If h is constant, the hub has no incoming dependency arcs, and the dependency graph is the directed path \(0\to1\to\cdots\to m-1\), which is acyclic. The existing acyclic-dependency theorem then gives \(A(g)=Q_m\). \(\square\)

**Corollary 23 (nonlinear one-branch SCC elimination).** In the sink-component paired-root gluing lemma, the sink component B can also be removed if, for each fixed outside assignment x, its fiber coloring can be relabeled into the displayed nonlinear single-branch form (24), with arbitrary offsets \(a_i(x)\) and hub function \(h_x\). Indeed,
\[
\boxed{|A(g_x)\cap\overline{A(g_y)}|\ge2
\quad\text{for every outside pair }x,y.}
\tag{28}
\]
Therefore paired-root existence for the full cube is equivalent to paired-root existence for the outside coloring, and the number of paired roots in the full cube is at least twice that of the outside cube.

*Proof.* Each fiber favorable-root set has cardinality at least \(2^{m-1}+1\) by Theorem 22, so any two sets, one of them antipodally complemented, intersect in at least two roots. Apply Lemma 18. \(\square\)

**Scope.** This settles a strongly connected dependency component with arbitrarily many additional incoming arcs into **one** hub, allowing any nonlinear Boolean hub color and arbitrary dependence of fiber offsets on outside bits. It does not cover components where the non-hub predecessor derivatives can vanish on some outside fibers, nor components with independent branching at two or more targets. Under these assumptions, the first unresolved local core must exhibit one of those latter features, rather than merely a nonlinear hub with many dependencies.


## Arbitrary small terminal fibers: a sharp majority gluing theorem

This extends the prior paired-root fiber-overlap lemma to all fiber colorings on up to three dimensions, without an acyclicity, affine, or single-branch assumption.

For any binary coloring \(g\) of \(Q_b\), write \(A(g)\) for the roots supporting a full dimension-simple geodesic of color word \(0^*1^*\), with empty blocks permitted, and \(P(g)=A(g)\cap\overline{A(g)}\).

**Lemma 24 (sharp favorable-root majority in ranks two and three).** Every coloring of \(Q_2\) satisfies \(|A(g)|\ge3\). Every coloring of \(Q_3\) satisfies \(|A(g)|\ge6\). Both bounds are attained.

*Proof.* An unfavorable \(Q_2\) root has both incident edge bits one and both opposite edge bits zero, making the other three roots favorable.

For \(Q_3\), cube automorphisms reduce any two distinct roots with the same vertex parity to vertices \(0\) and \(3\) in binary integer notation. Label edge colors
\[
a=g(01),\ b=g(13),\ c=g(37),\ d=g(15),\
e=g(57),\ f=g(04),\ h=g(45).
\]
Here \(uv\) refers to the unoriented edge joining vertices \(u,v\). Three full color words from root \(0\) are \(abc,ade,fhe\), and three from root \(3\) are \(baf,bdh,ceh\). If both roots were unfavorable, each word would contain a descent \(10\).

If \(a=0\), the words \(abc,ade\) force \(b=d=1,c=e=0\), while \(bdh\) forces \(h=0\). Then \(ceh=000\), contradiction. If \(a=1\), the word \(baf\) forces \(f=0\), then \(fhe\) forces \(h=1,e=0\), \(ceh\) forces \(c=1\), and \(abc\) forces \(b=0\); but \(bdh=0d1\) is favorable. Therefore no two roots in the same vertex-parity class can be unfavorable. Each class has four vertices, so at most two roots are unfavorable. Taking the Cartesian product of the sharp \(Q_2\) coloring with a constant-colored one-dimensional factor gives six favorable \(Q_3\) roots, attaining the bound. \(\square\)

**Theorem 25 (majority-overlap gluing for arbitrary fibers).** Split \(Q_{a+b}=Q_A\times Q_B\). Suppose every \(A\)-edge color is independent of the \(B\)-bits, inducing a coloring \(f\) of \(Q_A\). Above each \(x\in Q_A\), permit an arbitrary \(B\)-fiber coloring \(g_x\). If \(|A(g_x)|\ge\mu>2^{b-1}\) for every \(x\), then
\[
\boxed{|P(F)|\ge (2\mu-2^b)|P(f)|.}
\tag{29}
\]
For arbitrary fibers of dimension \(b=1,2,3\), this specializes respectively to
\[
\boxed{|P(F)|\ge 2|P(f)|,\qquad
|P(F)|\ge 2|P(f)|,\qquad
|P(F)|\ge 4|P(f)|.}
\tag{30}
\]

*Proof.* Fix \(z\in P(f)\). Choose a full \(0^*1^*\) geodesic in \(Q_A\) from \(z\) to \(\bar z\), and another from \(\bar z\) to \(z\); let their zero-to-one seam vertices be \(v,v'\). By inclusion--exclusion,
\[
|A(g_v)\cap\overline{A(g_{v'})}|
\ge |A(g_v)|+|A(g_{v'})|-2^b
\ge 2\mu-2^b.
\]
For each root \(t\) in that intersection, insert a favorable full \(B\)-fiber geodesic from \(t\) at the seam \(v\), and another from \(\bar t\) at seam \(v'\). The two resulting full geodesics in \(Q_{a+b}\) start at \((z,t)\) and its antipode \((\bar z,\bar t)\), both have word \(0^*1^*\), and use every dimension once. Different pairs \((z,t)\) give different paired roots, yielding (29). In dimension one both fiber roots are favorable; in dimensions two and three Lemma 24 gives \(\mu=3,6\), proving (30). \(\square\)

**Corollary 26 (no small terminal dependency component in a minimum obstruction).** Form the directed dependency graph whose vertices are cube directions, with an arc \(j\to i\) whenever changing input bit \(j\) can change a direction-\(i\) edge bit. If an arbitrary edge coloring of least possible dimension has no paired root, then every terminal strongly connected component of its dependency graph has at least four directions.

*Proof.* A terminal component \(B\) has no outgoing dependence on directions outside \(B\). Thus the outer edge colors are independent of \(B\)-bits, and Theorem 25 applies. If \(|B|\le3\) and the outer block is nonempty, least-dimensionality supplies a paired root in the smaller outer coloring, so Theorem 25 forces one in the full cube. If the outer block is empty, the strict favorable-root majority in \(Q_{|B|}\) itself forces an antipodal pair of favorable roots. Both contradict minimality. \(\square\)

**Structural significance.** In the full unrestricted paired-root conjecture equivalent to NORI1 one dimension higher, terminal nonlinear dependency blocks of size one, two, or three can always be eliminated by monotone fiber-path insertion and antipodal overlap. This supplements the previous cycle-component and special branching-fiber results: a least-dimensional obstruction must contain a terminal strongly connected component of size at least four. No global closure is asserted for those larger components.


## A full-component closure theorem for bounded and cyclic dependency blocks

The fiber gluing lemma is inductive over the **condensation DAG** of the directed dependency graph. The new nonlinear-hub theorem combines with the independently proved arbitrary-three-dimensional fiber majority to give the following all-dimensional closure result.

Call a strongly connected component B of the directed dependency graph **reducible** if at least one of the following holds:
(i) \(|B|\le3\), with no restriction on its internal edge-color functions;
(ii) its induced dependency digraph is a directed simple cycle, of any length;
(iii) after a cyclic relabeling \(B=\{0,\ldots,m-1\}\), all non-hub direction colors satisfy \(f_i(x)=x_{i-1}+a_i(x_{B^c})\) for \(1\le i<m\), with arbitrary Boolean outside-offset functions \(a_i\), while the hub edge color \(f_0\) is any Boolean function independent of bit 0 (possibly nonlinear in all other bits).

For each such B set
\[
L(B)=
\begin{cases}
2,&|B|=1\text{ or }2,\\
4,&|B|=3,\\
2^{|B|}-2,&B\text{ is a directed cycle of size }\ge4,\\
2,&B\text{ satisfies (iii) and is not already covered above}.
\end{cases}
\tag{31}
\]

**Theorem 27 (SCC-by-SCC paired-root closure).** If **every** strongly connected component of the directed dependency graph of an arbitrary binary cube-edge coloring f is reducible, then
\[
\boxed{|P(f)|\ge\prod_{B\in\operatorname{SCC}(\vec\Gamma(f))}L(B)>0.}
\tag{32}
\]
This holds regardless of how many nonlinear dependencies run *between* the components, and regardless of their directed-acyclic arrangement.

*Proof.* Choose a sink SCC B in the condensation DAG, and put A equal to the remaining dimensions. Because no arrow leaves B for A, the A-direction edge colors are independent of B-bits, inducing a smaller coloring on Q_A. For each outer assignment x, the induced B-fiber coloring g_x has: (i) at least 2,3,6 favorable roots respectively when \(|B|=1,2,3\), by Lemma 24; (ii) at most one unfavorable root if the global induced component is a simple directed cycle, because each fiber dependency graph is a subgraph of this cycle and Lemma 19 applies; or (iii) strictly more than half its roots favorable, by Theorem 22. Therefore for every x,y the intersection \(A(g_x)\cap\overline{A(g_y)}\) has at least L(B) roots. Lemma 18 gives \(|P(f)|\ge L(B)|P(f_A)|\).

Removing B from the global dependency graph leaves the induced graph on A, whose SCCs are the remaining original SCCs, since a sink has no outgoing arrows and cannot participate in another component. Apply induction until no dimensions remain. The empty cube has one paired root, proving (32). \(\square\)

**Corollary 28 (unrestricted small-SCC theorem).** In particular, **every** binary coloring of \(Q_d\) whose dependency SCCs all have size at most three has a paired root. Thus NORI1 holds for every upper-cube antipodally odd coloring whose bridge restriction is in this class, with no bound on d. The theorem is not a small-dimension test: d can be arbitrarily large and the quotient SCC network can have arbitrarily complicated interactions.

**Corollary 29 (irreducible local obstruction).** A paired-root counterexample, if one exists, must have a sink SCC of size at least four that is neither a directed simple cycle nor a uniformly active single-hub cycle with arbitrary hub nonlinearity. For a counterexample of minimum dimension, every sink component must have this property. The remaining problem is therefore internal branching or input-dependent loss of some non-hub predecessor interactions inside a sufficiently large terminal SCC, not interaction between already reducible components.

The proof is fully constructive given favorable-root witnesses for the smaller quotient problem and for the pertinent B-fiber roots: insert a B-geodesic at each of the two color-switch seams. It neither uses switch-count averaging nor requires tracking a global family of geodesics.

## Fan-cycle fiber majority without uniform predecessor derivatives

The single-branch theorem above assumed that each non-hub predecessor derivative remains one in every outside fiber. That assumption can be removed: *every* subgraph of a directed cycle with arbitrary additional arcs into one hub has strict favorable-root majority.

Call a directed graph on \(\{0,\ldots,m-1\}\), \(m\ge2\), a **fan-cycle dependency graph** if its arrows belong to
\[
\boxed{\{i-1\to i:1\le i<m\}\ \cup\
\{i\to0:1\le i<m\}.}
\tag{33}
\]
The set of arrows into hub 0 is unrestricted; its edge color may be any Boolean function of bits \(1,\ldots,m-1\). Each non-hub edge color is of the form
\[
g_i(u)=a_i+\lambda_i u_{i-1},\qquad
a_i,\lambda_i\in\mathbb F_2,\quad 1\le i<m,
\]
with \(\lambda_i\) possibly zero. The function \(g_0\) is arbitrary and independent of its own bit.

**Lemma 30 (all fan-cycle colorings have favorable-root majority).** Every binary cube-edge coloring g whose directed dependency graph is a subgraph of (33) satisfies
\[
\boxed{|A(g)|>2^{m-1}.}
\tag{34}
\]
In particular for any two such colorings g,h (which may have different predecessor activations and unrelated hub functions),
\[
\boxed{|A(g)\cap\overline{A(h)}|\ge2.}
\tag{35}
\]

*Proof.* Every directed cycle of the dependency digraph contains hub 0, since after deleting hub 0 all remaining arrows strictly increase their labels. Thus there is at most one nontrivial strongly connected component B. If no such component exists the entire graph is acyclic, and the acyclic-dependency theorem gives \(A(g)=Q_m\).

Otherwise B consists of a prefix \(\{0,\ldots,s\}\), \(1\le s<m\), or of the full vertex set: for 0 to reach a vertex i it must traverse the successive predecessor arrows \(0\to1\to\cdots\to i\), and for i to lie in B there must be a return path to 0. All predecessor arrows inside B are therefore present. The induced coloring on any B-fiber, after fixing the bits outside B, is in the *uniformly active nonlinear single-hub* form of Theorem 22, so its favorable-root set has size strictly greater than \(2^{|B|-1}\).

In the condensation DAG repeatedly remove terminal **singleton** components as long as B is not terminal. A singleton terminal component is a sink direction, whose deletion duplicates neither restrictions nor losses in favorable-root density: the earlier seam-insertion theorem states that its favorable-root set is the smaller set times both bit values. This process terminates with B as a terminal component, possibly together with singleton components pointing into B. The remaining outside graph is acyclic, since B is its only nontrivial SCC. Hence its coloring f has **all roots favorable**.

For each outside starting root z choose a full favorable f-geodesic and its zero-to-one seam vertex x. Every root t favorable in the B-fiber g_x can be inserted at this seam, producing a full favorable geodesic starting at (z,t). Thus the full favorable-root set has cardinality at least
\[
|A(f)|\min_x|A(g_x)|
>2^{|B^c|}2^{|B|-1}
=2^{m-1}.
\]
Reinserting each previously deleted terminal singleton doubles the root count and retains the strict majority. This proves (34). By inclusion-exclusion, both \(A(g)\) and \(\overline{A(h)}\) contain more than half the \(2^m\) roots, so their intersection contains at least two vertices, proving (35). \(\square\)

**Theorem 31 (fan-cycle SCC elimination).** In the SCC-by-SCC closure theorem, replace condition (iii) with the strictly broader condition:

> The induced dependency digraph on the SCC is isomorphic to a subgraph of a fan-cycle graph (33), and its edge color functions may depend arbitrarily and nonlinearly on the outside bits.

If **every** SCC of the full directed dependency graph is either of size at most three, a directed cycle, or a fan-cycle component as above, then the coloring has a paired root. For every fan-cycle component B, the paired-root count gains a factor of at least two upon removal.

*Proof.* Pick a terminal SCC B. Its outside-edge colors are independent of B. At every fixed outside assignment, the internal fiber dependency digraph is a subgraph of the same fan-cycle pattern; some predecessor arrows may disappear, but Lemma 30 still gives favorable-root majority. Consequently any two B-fiber favorable-root sets intersect after complementing one, in at least two roots. Apply the paired-root fiber-gluing lemma and induct on the SCC condensation DAG. Components covered by the other two hypotheses were already handled in Theorem 27. \(\square\)

**Closure significance.** An internal SCC with only a single extra nonlinear dependency target on a directed cyclic spine cannot obstruct NORI1, *even when the other cycle derivatives switch off in some outside fibers*. Any remaining minimal obstruction must have a terminal SCC whose internal influence graph is not of this fan-cycle type (and is not covered by the small-component or ordinary-cycle theorems). This is an all-dimensional structural reduction; it does not rely on switch-count averages or search through low-order cubes.

## Square-factorable fiber gluing with variable matchings

**Theorem.** Let F be any edge coloring of Q_{a+2r}, with dimension blocks A and B, where |B|=2r>=2. Assume A-edge colors do not depend on B-bits, inducing a coloring f of Q_A. For each outer vertex x, assume only that the B-fiber coloring g_x is a Cartesian product of arbitrary colored Q2 squares across a perfect matching M_x of B. The matchings M_x may vary arbitrarily with x.

For every paired root z of f, choose favorable full 0*1* paths from z and from its antipode, with seam vertices v_z,w_z. Then
|P(F)| >= sum_{z in P(f)} 2^{c(M_{v_z},M_{w_z})} >= 2|P(f)|,
where c(M,N) is the number of alternating-cycle components in the multigraph union of matchings M,N, including parallel pairs. In particular, paired-root existence always lifts through such an even-dimensional fiber block, regardless of the size of B.

*Proof.* The cross-orientation square-matching theorem in the separate Subsection "Cross-orientation root intersections for distinct square factorizations" proves that for any two square-factorable colorings g,g' with matchings M,N,
|A(g) intersect antipodal(A(g'))| >= 2^{c(M,N)}.
Each square factor forbids at most one of four root patterns for each monotone orientation; the combined forbidden-pattern constraints form disjoint alternating cycles, each admitting at least two assignments. Apply this to g_{v_z},g_{w_z}. Every root t in this intersection allows a favorable full B-geodesic from t at the first seam and from its antipode at the second seam. Inserting these B-geodesics into the two outer paths yields full dimension-simple 0*1* geodesics from (z,t) and its antipode. Counting distinct roots proves the inequality.

**Corollary.** A least-dimensional coloring without a paired root cannot contain a terminal dimension block of any even size whose fibers are all products of colored squares, even if their matchings depend on the outer vertex.

This result goes beyond majority-based gluing: for r>=3, a product of r sharp Q2 colorings has favorable-root density (3/4)^r below one half, yet cross-fiber intersection is forced by the cycle structure of two matchings. The outstanding closure problem is to extend the intersection principle to fibers with overlapping dependencies.

## Nonlinear star feedback: a sharp three-quarter favorable-root theorem

Let Q_{m+1}, m>=2, have hub bit t and leaf bits x in F_2^m. Assume each leaf-direction edge has color g_i(t,x)=a_i+t for a fixed bit a_i, while the hub-edge color is g_0(t,x)=h(x) for an **arbitrary Boolean function** h. Thus every hub-to-leaf influence is present but feedback to the hub is unrestricted.

**Theorem (sharp star majority).** Such a coloring satisfies
\[
\boxed{|A(g)|\ge3\cdot2^{m-1},\qquad |P(g)|\ge2^m.}
\tag{38}
\]
Furthermore **one entire hub-bit slice** consists of favorable roots, and the opposite slice contains at most 2^{m-1} unfavorable roots. The first bound is sharp for every m.

*Proof.* For a root (t,x), put J={i:a_i+t=0}, I={i:a_i+t=1}. Before the hub flip, J-leaf steps are zero and I-leaf steps are one; afterward their colors reverse. For any subset U of J:
- If h(x xor 1_U)=0, use the dimension order U,hub,I,J\U. Its color word is 0^*1^*.
- If h(x xor 1_I xor 1_U)=1, use U,I,hub,J\U, likewise with word 0^*1^*.

Thus a root can fail only if h is constantly one on C_0=x+F_2^J and constantly zero on C_1=x+1_I+F_2^J. If I is empty the two subcubes coincide, so no root in that hub slice fails. If I is nonempty the involution x↦x+1_I exchanges C_0,C_1, and at most half of that hub slice can fail.

Suppose at least one root with hub bit t fails. Its two J-subcubes C_0,C_1 have opposite constant h-values. Reversing the hub starting bit swaps I and J. Failure in that opposite hub slice would require h to be constant on an I-subcube, which varies the I-bits while keeping J-bits fixed. But every such I-subcube meets **both** C_0 and C_1, so h assumes both values on it. Hence every root in the other hub slice is favorable. This proves at most 2^{m-1} unfavorable roots overall and the A bound. Since P=A intersect antipodal(A), inclusion-exclusion gives |P|>=2|A|-2^{m+1}>=2^m.

For sharpness take all a_i=0 and h(x)=x_1. All roots with t=0 are favorable. For t=1, any root with x_1=1 is unfavorable: every leaf step before the hub has color one and after the hub color zero, while the hub color switches from one to zero when leaf 1 is traversed. If leaf 1 is before the hub, a zero-colored hub follows a one-colored leaf; if after the hub, a zero-colored leaf follows a one-colored hub. Thus 2^{m-1} roots fail, meeting the bound. QED.

**Corollary (star SCC cross-fiber gluing).** Suppose a terminal dependency SCC B has active hub-to-leaf derivatives throughout every fixed outside fiber, but arbitrary and possibly nonlinear leaf-to-hub feedback and outside-dependent offsets. Its fiber favorable sets each contain at least three quarters of Q_B. Any two such sets after complementing one intersect in at least 2^{|B|-1} roots. The paired-root fiber gluing theorem therefore gives
\[
\boxed{|P(F)|\ge2^{|B|-1}|P(f_A)|,}
\tag{39}
\]
and this terminal SCC cannot cause a paired-root failure.

The theorem is an all-dimensional closure result for a branching SCC with unrestricted nonlinear feedback at one hub. It does not yet cover multi-level branching or disappearing hub-to-leaf derivatives in some outside fibers.

## Partial-matchings remove fiber blocks in every dimension

**Lemma (path-cycle feasibility).** Take a union H of two partial matchings on a finite set of binary variables. On each edge forbid at most one of four assignments to its endpoints, allowing independent constraints on parallel edges. Then the system has at least 2^{c(H)} satisfying assignments, where isolated variables count as components.

*Proof.* Every component of H is a path, an even cycle (possibly a parallel-edge two-cycle), or a singleton. On a path, choose the initial bit in either of two ways and greedily choose subsequent bits; at most one next bit is forbidden, hence both initial choices extend. On a cycle, delete one constraint, and similarly build two assignments having different first bits. The removed constraint, incident to that first variable, can invalidate at most one, so a satisfying assignment exists. If a cycle had a unique satisfying assignment, each single-variable flip would have to violate an incident constraint. Each currently satisfied constraint can prohibit flipping at most one endpoint, since only one binary endpoint pair is forbidden. A cycle has as many constraints as variables; hence each constraint would protect one different vertex and its forbidden pair would differ from the solution pair in one bit. Complement every bit: each edge pair now differs from the original solution in two bits and therefore violates none of those constraints, contradicting uniqueness. Each component thus contributes at least two assignments, and components multiply. QED.

**Corollary (changing-partial-matching fiber gluing).** In the preceding variable-matching fiber theorem, one may allow a B-fiber of *any dimension*, decomposed as a Cartesian product of arbitrarily colored Q2 squares and independent Q1 edges. The factorization and partial matching M_x may vary with the outer vertex x. For every paired root z of the outer coloring, let v_z,w_z be seam vertices of two favorable outer paths. If c_z is the number of components of M_{v_z} union M_{w_z}, including isolated directions, then
|P(F)| >= sum_{z in P(f)} 2^{c_z} >= 2|P(f)|.

*Proof.* Every colored Q2 square excludes at most one of four favorable-root patterns; every colored Q1 factor excludes none. The intersection A(g_{v_z}) intersect antipodal(A(g_{w_z})) is the solution set of forbidden-pattern constraints on the union of the two partial matchings. By the lemma it has at least 2^{c_z} members. Insert full favorable fiber paths from a compatible root and its antipode into the respective two outer paths at their zero-to-one seams. Each resulting full path uses every direction once. Summing gives the inequality. QED.

This yields an all-dimensional terminal-block elimination rule for variable square and singleton decompositions. It applies even when fiber favorable-root densities are exponentially smaller than one half. The unresolved case requires overlapping dependencies not representable by such partial matchings.

## Star-root majority persists when hub-to-leaf dependencies disappear

The three-quarter favorable-root theorem is stable under arbitrary deletion of hub-to-leaf dependency arrows, a feature needed when passing to fibers of a larger coloring.

**Theorem (full star-pattern three-quarter bound).** Let a colored cube have hub bit t and m leaf bits \(x_1,\ldots,x_m\). Assume its direction-i leaf-edge bit is
\[
\boxed{g_i(t,x)=a_i+\lambda_i t,\quad i=1,\ldots,m,}
\]
where \(a_i,\lambda_i\in\mathbb F_2\) are arbitrary, and the hub-edge bit \(g_0(t,x)=h(x)\) is any Boolean function. Then, for every m>=1,
\[
\boxed{|A(g)|\ge\tfrac34 2^{m+1},\qquad
|P(g)|\ge\tfrac12 2^{m+1}.}
\tag{40}
\]
The three-quarter factor is sharp. In particular any two such colorings g,g' of the same dimension satisfy
\[
\boxed{|A(g)\cap\overline{A(g')}|\ge2^m.}
\tag{41}
\]

*Proof.* Partition the leaves into the active set T={i:lambda_i=1} and the inactive set I={i:lambda_i=0}. The inactive-direction edge colors are fixed constants a_i, independent of the hub and the active-leaf bits. Treat Q_I as an outer cube and Q_{\{0\}\cup T} as the inner fiber. The outer coloring has every starting root favorable: traverse its zero-colored dimensions first and its one-colored dimensions afterward.

For each fixed outside leaf assignment y, the inner fiber has all active hub-to-leaf arrows and an arbitrary hub function \(h_y\). If T is nonempty, the three-quarter theorem applies to this fiber (including the elementary one-leaf case, which is a colored Q2 with at least three favorable roots). If T is empty, the inner fiber is a single edge and both its roots are favorable. Hence every inner fiber has at least three quarters of its roots favorable.

For every outer starting root z, choose a favorable outer geodesic with seam vertex y. Insert any favorable full inner-fiber path beginning at a chosen inner root into that seam; this produces a full favorable path in the combined cube. Thus the favorable-root count is at least
\[
2^{|I|}\cdot\tfrac34 2^{|T|+1}
=\tfrac34 2^{m+1}.
\]
Antipodal inclusion-exclusion gives the P bound. Applying the same count to any two colorings and complementing one gives (41). Sharpness follows from the active-star instance with all offsets zero and hub function h(x)=x_1. \(\square\)

**Corollary (terminal star SCC closure without uniform activation).** A terminal dependency SCC can be removed by paired-root gluing whenever its internal dependency graph is a subgraph of a bidirected star (all arrows join the hub to leaves), even if individual hub-to-leaf derivatives vanish on some fixed outside fibers and all leaf-to-hub feedback is nonlinear. Every such fiber has at least three quarters favorable roots, so the paired-root lower bound gains a factor of at least \(2^{|B|-1}\) upon removal.

This eliminates the variable-activation caveat from the star SCC result. A minimal obstruction must contain a terminal SCC whose internal directed graph is neither a fan-cycle nor a bidirected-star subgraph nor one of the other reducible component types.

## Arbitrary rooted-tree feedback: three-quarter favorable-root theorem

Let T be a rooted tree on dimensions 0,...,m with parent map p(i), and color edges by
\[
f_0(x)=h(x_1,\ldots,x_m),\quad f_i(x)=a_i+\lambda_i x_{p(i)}\quad(i>0),
\]
where h is an arbitrary Boolean function and \(a_i,\lambda_i\in\mathbb F_2\).

**Lemma (monochromatic branch).** If all lambda_i=1, any branch B hanging off hub 0 can be traversed using only color \(a_c+t\), where c is its top direction and t is the current hub bit.

*Proof.* The top edge c has color k=a_c+t. For every other descendant i, obtaining color k requires [p(i) before i]=k+a_i+x_{p(i)}, using the initial B-bits x. These relations orient the edges of the tree B and therefore admit a total order. Such an order traverses every B direction in color k. QED.

**Theorem (active tree).** If every lambda_i=1 then
\[
\boxed{|A(f)|\ge\tfrac34 2^{m+1},\quad |P(f)|\ge\tfrac12 2^{m+1}.}
\]

*Proof.* Partition the nonhub dimensions into the disjoint child branches B_1,...,B_r. The full-branch toggles 1_Bj generate an r-dimensional subspace of F_2^m. Partition leaf-root assignments into cosets of that subspace. In each coset choose representative y and let s_j encode whether branch B_j is toggled. Define a macro-star coloring on Q_{r+1} by
\[
g_j(t,s)=a_{c_j}+t,\quad
g_0(t,s)=h(y+\sum_j s_j1_{B_j}),
\]
where c_j is the first direction of branch B_j. The established nonlinear-star theorem gives a favorable full 0*1* macro-geodesic from at least three quarters of the macro-roots. Expand each macro-leaf step into a monochromatic full traversal of B_j using the lemma. Each expansion has the color of the replaced step and flips every bit of that branch, so the new full word is still 0*1*. At the hub step the leaf bits agree with the macro assignment, hence its edge color is also preserved. Thus every favorable macro-root gives a favorable original root. Sum over the disjoint cosets to obtain the bound on A. Inclusion-exclusion for P=A intersect antipodal(A) gives the other bound. QED.

**Theorem (inactive interactions).** The same bounds hold for arbitrary lambda_i in F_2.

*Proof.* In the dependency digraph, nonhub arcs go outward along the parent tree and all other arcs enter hub 0. Therefore every directed cycle contains hub 0 and there is at most one nontrivial SCC B. If the whole digraph is acyclic, every root is favorable. Otherwise B consists of hub 0 and an outward-rooted subtree in which every internal parent arc is active, since each vertex of B must be reached from hub along its unique ancestral path. Outside B, every SCC is a singleton and the induced graph is acyclic.

Remove terminal singleton SCCs by the proven one-direction seam-insertion identity, which duplicates favorable roots. Once B becomes terminal, the remaining outside coloring has acyclic dependencies, so all outer roots are favorable. For each such root choose a favorable outer path and its zero-to-one seam. At that seam the B-fiber has active rooted-tree form; the preceding theorem guarantees favorable B-paths from at least three quarters of its roots. Insert each such B-path at the outer seam. At least three quarters of combined roots are favorable. Reinsert removed singleton directions, preserving this fraction. The antipodal paired-root bound follows by inclusion-exclusion. QED.

**Corollary (SCC elimination).** Any terminal dependency SCC whose internal arcs lie in an outward-rooted tree plus arbitrary feedback arrows to the root can be removed through paired-root fiber gluing. Fixed outside assignments may deactivate parent arrows, and root-edge color functions can vary arbitrarily. Every fiber is still at least three quarters favorable; hence any two fibers have at least half their roots in the intersection of one favorable set with the antipodal image of the other.

This proves the all-dimensional rooted-tree feedback majority conjecture; its three-quarter factor is sharp over the class, as witnessed by the nonlinear star. The remaining hard cores require more than one nonlinear feedback target or overlapping feedback circuits.

## Quantitative SCC root count and two-branch necessary condition

The rooted-tree feedback theorem extends across the condensation DAG of any directed dependency graph by the paired-root fiber gluing lemma.

**Theorem (exponentially many paired roots).** Let f be a binary cube-edge coloring of Q_d. Suppose every nontrivial SCC B of its directed dependency graph has an internal graph whose arcs lie in an outward rooted tree together with arbitrary arcs entering the root of that tree. Let k denote the number of SCCs of size at least two. Then
\[
\boxed{|P(f)|\ge 2^{d-k}>0.}
\tag{44}
\]
The bound is sharp, for example when f is a Cartesian product of k copies of the sharp two-dimensional coloring and d−2k independent one-dimensional factors. Arbitrary nonlinear dependencies **between** the SCCs do not affect the bound.

*Proof.* Remove sink SCCs one at a time. If B is a singleton, its fiber has both starting roots favorable, and paired-root seam gluing multiplies the count of paired outside roots by two. If |B|=s>=2, each fixed-outside B-fiber has at least three quarters of its roots favorable, by the rooted-tree theorem. For any two outside seam vertices, the corresponding fiber favorable sets intersect after antipodal complement in at least
\[
2\cdot\tfrac34\,2^s-2^s=2^{s-1}
\]
roots, so seam gluing multiplies the paired-root count by at least \(2^{s-1}\). The condensation is acyclic and the outer edge colors are independent of the terminal component's bits, so the argument iterates. Starting from the empty cube with one paired root, multiplication yields \(2^{\sum_B |B|-\#\{B:|B|\ge2\}}=2^{d-k}\). For sharpness, each independent sharp Q2 factor has two paired roots and each Q1 factor has two; their Cartesian product has \(2^{d-k}\) paired roots. \(\square\)

**Lemma (one internal branching target is reducible).** Let D be a finite strongly connected loopless digraph with at least two vertices. If at most one vertex has indegree greater than one, then D is a directed cycle or an outward rooted spanning tree together with additional arrows entering its root.

*Proof.* Every vertex of a nontrivial strongly connected digraph has indegree at least one. If each has indegree one, strong connectivity forces a single directed cycle. Otherwise let v be the sole vertex of indegree greater than one. Every other vertex u has a unique predecessor p(u). A directed path from v to u exists by strong connectivity; its final step must be p(u)->u. Thus the shortest-path distance from v strictly increases along every arrow p(u)->u, so these n−1 arrows form an outward arborescence rooted at v. All further arrows enter v, since no other vertex has a second incoming arrow. \(\square\)

**Corollary (irreducible minimal obstruction).** In a least-dimensional counterexample to paired-root existence, **every terminal SCC** must have at least four vertices and at least **two distinct vertices of internal indegree at least two**. Otherwise that component is a singleton, a small arbitrary SCC already handled by the three-dimensional majority theorem, or a rooted-tree feedback component removable by the theorem above. Hence any first obstruction must contain multiple independent branching targets inside one feedback-connected component.

These constraints are structural and dimension-uniform; they do not depend on mean switch counts or enumeration of small cubes.

## Multi-hub forest compression: root-wise lift preserving antipodal pairs

The macro-star proof generalizes to **any number of nonlinear feedback hubs**. Its value is that long tree branches can be collapsed without losing dimension-simple geodesic witnesses or paired-root witnesses.

Choose a subset H of k hub dimensions in a cube Q_{k+m}. Partition the remaining m dimensions into vertex-disjoint rooted branch trees \(B_1,\ldots,B_r\). The top direction \(c_j\) of B_j has a hub parent \(h(j)\in H\). Suppose for every nonhub direction i the edge color is
\[
\boxed{f_i(x)=a_i+x_{p(i)},}
\tag{45}
\]
where \(p(i)\) is either another direction in B_j or, for its top direction, the hub h(j). Each hub-direction edge color may be any Boolean function of all cube bits except its own.

Let \(L\subseteq\mathbb F_2^m\) be the span of the disjoint branch-toggle vectors \(\mathbf1_{B_1},\ldots,\mathbf1_{B_r}\). Partition nonhub starting assignments into cosets \(y+L\). For one coset, encode a root by hub bits \(t\in\mathbb F_2^k\) and branch bits \(s\in\mathbb F_2^r\), representing the original root \((t,y+\sum_j s_j\mathbf1_{B_j})\).

Define its **compressed coloring** \(g_y\) on \(Q_{k+r}\) as follows: a macro-leaf direction j has color
\[
\boxed{g_{y,j}(t,s)=a_{c_j}+t_{h(j)},}
\]
and a hub direction i has the color of the corresponding original hub edge evaluated at the represented original vertex.

**Theorem (multi-hub monotone lifting).** Every full \(0^*1^*\) macro-geodesic of \(g_y\) lifts to a full \(0^*1^*\) geodesic of f at the represented root. Moreover the antipodal map acts **within each coset** by \((t,s)\mapsto(\bar t,\bar s)\), and consequently
\[
\boxed{
|A(f)|\ge\sum_{y+L}|A(g_y)|,\qquad
|P(f)|\ge\sum_{y+L}|P(g_y)|.}
\tag{46}
\]
In particular if all macro-hub colorings in this class satisfy the paired-root assertion, then all their arbitrary rooted-tree expansions satisfy it as well.

*Proof.* Expand each macro-leaf traversal into the monochromatic full geodesic in its branch, using the tree-ordering lemma established above. The top edge has color \(a_{c_j}+t_{h(j)}\) and the target color at every deeper edge is imposed by orienting its parent-child relation, an acyclic tree. Thus all expanded branch edges have the macro-step color. Since the branch is traversed in full, its binary starting assignment changes by \(\mathbf1_{B_j}\), precisely the change of its macro-bit s_j. Hub edges occur at the represented original states and retain their macro colors. All dimensions are used once and replacing a macro color by a nonempty block of the same color preserves the monotone word.

The branches partition all nonhub dimensions, so full complementation of the represented root is
\[
(\bar t,\bar y+\sum_j s_j\mathbf1_{B_j})
=(\bar t,y+\sum_j(1-s_j)\mathbf1_{B_j}).
\]
It therefore corresponds to \((\bar t,\bar s)\) in the **same** coset. Each favorable macro-root and each paired macro-root lifts to an original root of the corresponding kind; roots from distinct cosets remain distinct. Summing gives (46). \(\square\)

**Closure use.** With one hub, the compressed coloring is the nonlinear star, yielding the three-quarter theorem. With two hubs, every arbitrary-depth forest attached to those hubs reduces to the **two-hub star** problem: two arbitrary nonlinear hub functions and macro-leaf colors each depending on one assigned hub. The latter is the first unproved structurally richer target; two-root interaction, rather than tree depth, carries the remaining difficulty. This theorem is a reduction, not a proof of the two-hub assertion.

## Two branching targets: compression to a two-hub star

**Lemma (unique-predecessor forest).** Let D be a finite strongly connected loopless digraph with at least two vertices. Let H be the vertices of indegree greater than one, and assume H is nonempty. Every cycle meets H, and the arrows entering vertices outside H form outward-rooted trees attached to H.

*Proof.* Every vertex outside H has a unique predecessor. A cycle contained entirely outside H already uses the sole incoming arrow of every vertex on it, so no path from H could enter it, contradicting strong connectivity. Thus the subgraph outside H is acyclic. Following predecessors backward from any other vertex must terminate at H, or else produce a cycle outside H. Those unique predecessors define a forest rooted at H. All additional arrows enter H. QED.

**Theorem (two-hub compression).** Suppose a binary cube-edge coloring f has a strongly connected directed dependency graph with two vertices of indegree greater than one. Every other dimension i has one incoming dependency from a predecessor p(i), so its edge color is
\[
\boxed{f_i(x)=a_i+x_{p(i)}.}
\]
All such dimensions form disjoint rooted tree branches attached to the two hub dimensions. Each hub edge color may be an arbitrary nonlinear Boolean function of every other bit. The previous multi-hub macro-forest theorem therefore constructs, for each coset of branch-toggle vectors, a two-hub star coloring g whose favorable and paired macro-root sets lift to corresponding root sets of f. Hence a universal paired-root theorem for two-hub stars would settle this full class of arbitrary-size, arbitrary-depth strongly connected dependency colorings.

*Proof.* Apply the unique-predecessor lemma to the two hubs. A Boolean edge color depending on only one other bit, with an active dependency, has the indicated affine form. Compress each branch to one macro-leaf, using monochromatic tree traversal, and apply the previously published macro-forest lifting theorem. The paired-root correspondence respects antipodal complementation within each coset. QED.

**Corollary (minimal graph excess).** Any least-dimensional paired-root counterexample has a terminal SCC with at least four vertices and at least two vertices of indegree greater than one. Therefore that SCC has at least s+2 arrows if it has s vertices. If it has s+2 arrows, it has two indegree-two branching targets and all other vertices have indegree one; hence the two-hub reduction above applies. The minimal directed graph excess is thus a two-hub problem, independent of the lengths of its intervening dependency paths.

**Next conjecture (unproved).** For every coloring of Q_{r+2} with two hub bits t_0,t_1, with leaf j edge color \(a_j+t_{\eta(j)}\), \(\eta(j)\in\{0,1\}\), and arbitrary nonlinear edge colors in the two hub directions, does
\[
\boxed{|A(g)|>2^{r+1}}
\]
always hold? This favorable-root strict-majority conjecture would permit paired-root gluing of every terminal SCC with two branching targets. A candidate stronger bound is \( |A(g)|\ge (9/16)2^{r+2}\), attained by a product of two sharp star gadgets, but it is not yet established.

## Rootwise orientation coverage for rooted-tree feedback

The rooted-tree majority theorem has a stronger pointwise companion. Write \(A_0(f)\) and \(A_1(f)\) for roots admitting full geodesics with words \(0^*1^*\) and \(1^*0^*\), respectively.

**Theorem (hub-first orientation at every prescribed root).** Suppose
\[
f_0(x)=h(x_1,\ldots,x_m),\qquad
f_i(x)=a_i+\lambda_i x_{p(i)}\quad(i>0),
\]
where the parent relations form a tree rooted at \(0\), the hub function \(h\) is arbitrary, and \(a_i,\lambda_i\in\mathbb F_2\). For every root \(z\), put \(q=h(z_1,\ldots,z_m)\). There is a full geodesic starting with direction \(0\) whose word is
\[
\boxed{q^*(1-q)^*.}
\]
In particular,
\[
\boxed{A_0(f)\cup A_1(f)=V(Q_{m+1}).}
\]

*Proof.* Traverse the hub edge first, obtaining color \(q\) and fixing the hub bit at \(1-z_0\). Delete the hub from the parent tree and remove each remaining parent link whose child has \(\lambda_i=0\). The resulting components are rooted trees. The top direction \(c\) of each component has a fixed edge color \(k_c\): it is \(a_c+\lambda_c(1-z_0)\) when its parent is the hub, and \(a_c\) when its parent link was removed.

Every other direction \(i\) in that component has \(\lambda_i=1\). To give its edge color \(k_c\), impose the precedence condition
\[
[p(i)\text{ occurs before }i]=k_c+a_i+z_{p(i)}.
\]
These conditions orient the component's tree edges. Every orientation of a tree is acyclic, so a total order satisfying them exists. Traversing the component in this order colors all its steps \(k_c\). Its edge colors are independent of bits in other components: removed parent links have coefficient zero.

Traverse all components of color \(q\), followed by all components of color \(1-q\). Together with the initial hub edge, this gives the required full dimension-simple word. \(\square\)

**Corollary (one branching target in a strongly connected dependency graph).** If a cube coloring has a strongly connected directed dependency graph with at most one vertex of indegree greater than one, every root admits at least one monotone orientation.

*Proof.* A one-direction coloring is constant and every root is paired. For a strongly connected graph with at least two vertices and no branching target, the graph is a directed cycle; designate any vertex as the hub. With one such vertex, the unique-predecessor lemma gives an outward rooted tree with all remaining arrows entering that hub. Each nonhub edge-color function depends on its sole predecessor and has the form \(a_i+x_{p(i)}\). Apply the theorem. \(\square\)

**Restoration consequence.** The endpoint restoration theorem in the gauge-criticality Subsection produces an affected zero face with two prescribed opposite roots admitting neither orientation. Such a face, and any isolated factor carrying its sole exceptional edge, cannot have rooted-tree feedback form. If the surviving defect factor is strongly connected, it must have at least two distinct internal branching targets. This applies the rooted-tree argument at the prescribed restoration corners, without transporting a paired root from elsewhere in the face.

The hub-first construction was additionally checked on 640 sampled rooted-tree instances in dimensions two through nine, allowing inactive parent links. The proof above establishes the statement in every dimension.


**Audit of the graph reductions.** The unique-predecessor forest lemma assumes a nonempty branching set \(H\). Without this hypothesis a directed cycle has \(H=\varnothing\) and remains cyclic after deleting \(H\), so the formerly unrestricted statement was false. The one-target graph classification assumes at least two vertices; singleton strongly connected graphs are handled separately. The two-hub compression and all nontrivial-component applications satisfy these hypotheses. The hub-first rooted-tree theorem and its critical-face consequence are unchanged.


## Four-type macro-branch reduction for arbitrary two-hub feedback

Let f be a coloring of the undirected edges of Q_(m+2) with hub bits t_0,t_1 and leaves indexed by j, such that each leaf-edge bit has form f_j(t,x)=a_j+t_(eta(j)), where eta(j) is 0 or 1 and a_j is 0 or 1. The hub edge-bit functions are arbitrary Boolean functions of all bits other than their own hub bit.

Group leaf directions by their pair (eta(j),a_j). There are at most four nonempty classes B_1,...,B_r. The disjoint indicator vectors 1_(B_i) generate a subspace L of F_2^m of rank r. For each coset y+L write a represented root as
\[
(t,s)\longmapsto(t,y+\sum_i s_i1_{B_i}).
\]
Define a compressed coloring g_y on Q_(r+2) by giving each macro leaf the color a_i+t_(eta(i)) and both hub directions the colors of f at the represented vertex. These are well-defined undirected edge colors.

**Theorem (four-type compression).** The two-hub favorable and paired-root counts satisfy
\[
\boxed{|A(f)|\ge\sum_{y+L}|A(g_y)|,\qquad
|P(f)|\ge\sum_{y+L}|P(g_y)|.}
\]
Every favorable or paired macro-root expands to the corresponding kind of original root, and in particular every two-hub star in arbitrary dimension reduces to structured stars on at most six directions.

*Proof.* Expand a macro leaf step into a consecutive traversal of all original dimensions in its type class. Those edges have the macro color because no controlling hub is flipped during expansion. The expanded step flips the entire class, retaining the represented macro state; hub steps inherit their original colors. Hence expanding a full dimension-simple nondecreasing-color word gives a full dimension-simple nondecreasing-color word. The classes partition the nonhub directions, so taking the antipode of a represented root acts inside the same coset by (t,s) -> (1-t,1-s). Thus paired macro-roots also lift. Cosets are disjoint and partition the original vertex set. QED.

If the conjectural sharp nine-sixteenths favorable-root lower bound holds for every reduced star with r<=4 and one leaf of each present type, then it holds for all two-hub stars in all dimensions. This is a *reduction*, not a proof of that numerical bound.

**Multi-hub version (parameterized kernel).** Suppose a strongly connected dependency digraph has k>=1 vertices of indegree at least two. Every other vertex has a unique predecessor and belongs to an outward-rooted tree attached to a branching hub: a cycle avoiding the hubs would have no incoming arrows and contradict strong connectivity. Each nonhub edge color is an affine function of its predecessor bit. First collapse each entire branch using its monochromatic tree-ordering traversal, then merge branches with the same hub parent and the same leading-edge offset. There are at most two macro leaves per hub, so one obtains a coloring with at most 3k directions on every coset of branch-toggle vectors. Favorable and paired macro-roots lift to favorable and paired roots of the original coloring. The hubs retain arbitrary nonlinear color functions. Thus the dependency-core complexity can be reduced to at most 3k directions, although k itself need not be bounded.

**Remaining target.** For k=2 this yields a bounded, structured six-direction theorem. Any proof of strict favorable-root majority in that class would establish the corresponding result for all two-hub stars, with arbitrary numbers of repeated leaf types and arbitrary nonlinear hub feedback. The reduction does not claim this majority theorem or NORI1.


## Nonlinear antipodal two-direction deletion and fixed-rank kernel improvement

Let c_k(x) be the color of the undirected direction-k cube edge incident at x, independent of bit x_k. Assume c_k(\bar x)=1+c_k(x) for every k.

**Theorem (nonlinear twin-pair restoration).** Suppose distinct i,j satisfy
\[
c_k(x+e_i+e_j)=c_k(x)\ (k\ne i,j),\quad
c_i(x+e_j)=c_i(x),\quad c_j(x+e_i)=c_j(x)
\]
for all vertices x. Restrict to the face x_i=x_j=0 to obtain c' on Q_(n-2). Then c' is antipodally odd, and any monochromatic full antipodal geodesic in c' lifts to one in c of the same color.

*Proof.* Write y for the other bits, u,v for the selected bits. The assumptions yield c_k(y,u,v)=g_k(y,u+v) for k outside {i,j}, c_i=h_i(y), and c_j=h_j(y), for arbitrary Boolean functions. Full antipodal oddness gives g_k(\bar y,p)=1+g_k(y,p) and h_i(\bar y)=1+h_i(y), h_j(\bar y)=1+h_j(y). Thus c'_k(y)=g_k(y,0) is odd.

Take a monochromatic complete c' path of color b from y to \bar y. Reverse its traversal if necessary, choosing its start s with h_i(s)=b (possible because h_i(\bar y)=1+h_i(y)). If h_j(s)=b, start at (s,0,0), traverse i and j consecutively to (s,1,1), then follow the smaller path. The selected edges and the smaller edges all have color b; along the smaller path u+v=0. The destination (\bar s,1,1) is the antipode.

If h_j(s)=1+b, start at (s,1,0), traverse i to (s,0,0), follow the smaller path to (\bar s,0,0), then traverse j to (\bar s,0,1). The first selected edge has color h_i(s)=b; the last has h_j(\bar s)=1+h_j(s)=b. The smaller path again runs with u+v=0. Both resulting full paths use every direction once. QED.

**Lemma (unread-direction deletion).** If c_k(x+e_i)=c_k(x) for all k different from i, then deleting i preserves oddness and every smaller monochromatic full geodesic lifts by inserting i at its beginning. Choose the path's starting endpoint so the color of the i-edge matches the monochromatic color; oddness gives opposite i-edge colors at the two possible endpoints.

**Corollary (affine column-twin elimination).** For an affine odd coloring c_i(x)=(Lx)_i+a_i with L_ii=0 and L1=1, equality of columns Le_i=Le_j alone suffices for pair deletion. The equal columns imply L_ij=L_ji=0 and invariance of all other direction colors under toggling i and j together. No equality of rows or offsets is required.

**Corollary (finite rank kernel).** Any such rank-r matrix, r>=2, can be reduced by zero-column and repeated-column-pair deletions to a row-odd zero-diagonal matrix of rank at most r with at most
\[
\boxed{2^r-2}
\]
remaining directions. Each deleted dimension or pair can be restored along any smaller monochromatic full path.

*Proof.* All deletions preserve odd row sums and zero diagonal. In the final matrix, columns are distinct and nonzero. If its rank is s<=r, choose a basis U of s independent odd rows and let t_i=Ue_i; these are distinct nonzero vectors in F2^s. Their XOR equals U1=1_s, which is nonzero. For s>=2 the XOR of all 2^s-1 nonzero vectors is zero. Therefore some nonzero vector is absent, and at most 2^s-2<=2^r-2 columns remain. The nonempty rank-one odd zero-diagonal case is impossible. QED.

This improves the earlier fixed-rank bound 2^(r-1)(2^(r-1)-1): rank three now needs at most six residual dimensions, and rank four at most fourteen. The first theorem also eliminates nonlinear symmetric dimension pairs from any least-dimensional hypothetical NORI1 obstruction.



## Bounded global Boolean influence rank forces nonlinear twin reduction

The nonlinear pair deletion theorem admits a dimension-free structural consequence based on the binary rank of the full Boolean-derivative profile matrix.

For an arbitrary antipodally odd cube-edge coloring c, define the global derivative matrix J(c) over F2. Its columns are indexed by cube directions i; its rows are indexed by pairs (k,x) with k a direction and x a cube vertex. Put
\[
J(c)_{(k,x),i}=c_k(x+e_i)+c_k(x)=\partial_i c_k(x).
\]
Its diagonal direction derivatives vanish because undirected edge colors do not depend on their own direction bit. Write \(r(c)=\operatorname{rank}_{F2}J(c)\).

**Lemma (derivative twins imply antipodal twins).** If column i of J(c) is zero, direction i is unread and can be deleted by the preceding one-direction theorem. If columns i,j agree, then i,j satisfy every hypothesis of the nonlinear antipodal pair-deletion theorem and can be deleted together.

*Proof.* A zero column says \(\partial_i c_k(x)=0\) for every k,x, so no other direction color reads bit i. If columns i,j agree, then for every k,x
\[
c_k(x+e_i)=c_k(x+e_j).
\]
Replace x by x+e_i to obtain \(c_k(x)=c_k(x+e_i+e_j)\), giving simultaneous-flip invariance for all other directions. For k=i, the self-derivative \(\partial_i c_i\) vanishes, so column equality forces \(\partial_j c_i=0\). Similarly \(\partial_i c_j=0\). These are the remaining pair-deletion conditions. \(\square\)

**Theorem (nonlinear rank kernel).** If \(r(c)=r\), repeated unread-direction and equal-derivative-column pair deletions produce an antipodally odd coloring of a cube with at most
\[
\boxed{2^r-1}
\]
directions, such that **every** monochromatic full geodesic of the residual coloring lifts to one in c.

*Proof.* Each deletion is justified by the preceding lemma and the nonlinear restoration theorem. Its induced coloring is the restriction of the remaining edge-color functions to a face. The new global derivative matrix is obtained by retaining some original direction columns and projecting their entries onto the smaller set of remaining rows and face vertices. Hence its rank never exceeds r. Continue until every remaining derivative column is nonzero and the columns are pairwise distinct. A binary vector space of dimension at most r has only 2^r-1 distinct nonzero vectors, proving the bound. Reversing the sequence of deletions lifts every residual monochromatic full geodesic to the original coloring. \(\square\)

**Corollary (minimum-obstruction derivative-rank bound).** A least-dimensional odd coloring of \(Q_n\) without any monochromatic full antipodal geodesic would necessarily satisfy
\[
\boxed{r(c)\ge\lceil\log_2(n+1)\rceil.}
\]
Indeed a minimal obstruction has neither an unread dimension nor equal derivative columns, so all n columns of J(c) are distinct nonzero vectors and n<=2^{r(c)}-1.

**Scope and closure route.** This works for arbitrary nonlinear Boolean edge-color functions, not merely affine readers. It proves an all-dimensional induction reduction for every class with a uniform bound on global derivative-column rank. The stronger affine kernel bound 2^r-2 uses the extra constant-matrix odd-row identity and need not hold for nonlinear derivatives. The remaining unrestricted obstruction requires derivative-column diversity large enough to prevent both unary deletion and paired symmetry restoration.



## Closure transfer from finite dimensions to bounded nonlinear derivative rank

The nonlinear derivative-column deletion theorem yields a useful quantified induction principle.

**Theorem (finite-dimension closure transfer).** Fix \(D\ge2\) and suppose the ordinary **edge-coloring NORI1** assertion is established for every antipodally odd coloring of \(Q_d\), for each \(2\le d\le D\). Then:
1. every antipodally odd coloring of arbitrary dimension whose global Boolean derivative-column rank is \(r\) with \(2^r-1\le D\) has a monochromatic full antipodal geodesic;
2. every affine antipodally odd coloring of arbitrary dimension whose reader matrix has rank \(r\ge2\) with \(2^r-2\le D\) has such a geodesic.

*Proof.* In the first case, apply nonlinear unread-direction and twin-pair deletions until the residual cube has at most \(2^r-1\le D\) directions. The reduced coloring remains antipodally odd, and its derivative rank has not increased. By the assumed finite-dimensional edge-coloring NORI1 theorem, it has a monochromatic full geodesic; restore all deleted directions to lift that path to the original cube. The affine case is identical using its sharper \(2^r-2\) column-kernel bound. Odd edge colorings cannot exist in dimension one, so there is no exceptional rank-one terminal coloring to consider. \(\square\)

**Important distinction.** A dimension-six closure result for **ordered three-face colorings with one permitted color change** is not the edge-coloring NORI1 assertion assumed here. The two statements must not be interchanged. The rank-three affine result already established in this project has its own finite transition-state verification; the improved six-dimension column kernel offers a smaller alternative verification target, but it does not itself constitute an unconditional proof for rank three without a valid edge-coloring result in those residual dimensions.



## Paired-root twin restoration for arbitrary cube-edge colorings

Let P(f)=A_0(f) intersection A_1(f), with A_0 and A_1 denoting full dimension-simple monotone edge-color geodesics of opposite orientations. Assume distinct directions i,j satisfy
\[
f_k(x+e_i+e_j)=f_k(x)\quad(k\ne i,j),\quad
f_i(x+e_j)=f_i(x),\quad f_j(x+e_i)=f_j(x).
\]
Let g_0,g_1 be the two reduced colorings obtained by setting the chosen two bits to parity zero or parity one respectively.

**Theorem (two-slice restoration without antipodal oddness).**
\[
\boxed{|P(f)|\ge2|P(g_0)|+2|P(g_1)|.}
\]
For every paired root z of g_p, both full roots with outside bits z and selected-bit parity p are paired.

*Proof.* The other direction colors depend on the selected two bits only through their parity, while the two selected edge colors depend on neither selected bit. Choose the two opposite monotone geodesics of g_p from z. Insert both selected directions consecutively at the respective monotone switch seams, sorting their two edge colors 0 before 1 in the nondecreasing path and 1 before 0 in the nonincreasing path. Because the selected colors do not change while either inserted edge is traversed, and the selected parity before and after the pair is p, every other edge retains its lower-cube color. Both enlarged paths start from either specified parity-p two-bit assignment and end at its antipode. Counting the disjoint lifts proves the bound. QED.

**Lemma (unread direction).** If direction i influences no other direction edge color, removing i yields g with |P(f)|>=2|P(g)|. Insert the removed dimension at the monotone switch seam of each reduced favorable path; its own edge bit fits either orientation. The starting bit i is arbitrary.

Define global derivative matrix J(f) by J_(k,x),i=f_k(x+e_i)+f_k(x). Equal columns imply the twin hypotheses, and zero columns identify unread dimensions. The derivative rank cannot increase after restriction to a face.

**Theorem (sharp half-cube root guarantee at derivative rank two).** Every undirected binary cube-edge coloring with rank J(f)<=2 satisfies
\[
\boxed{|P(f)|\ge2^{n-1}.}
\]
Proof by induction on n. Dimensions one, two and three have respectively at least 2,2 and 4 paired roots, the last from the sharp three-cube majority bound |A_0|,|A_1|>=6. For n>=4, there are more than three columns in a binary rank-two space, so some column is zero or some two coincide. Deleting a zero column and using induction doubles the lower bound. Deleting two equal columns and applying induction separately on both parity-slice colorings, followed by the displayed twin inequality, multiplies the two separate (n-2)-cube lower bounds by two and sums them, again giving 2^(n-1). The result is sharp: take reciprocal readers f_1=x_2, f_2=x_1 on Q_2 and constant edge colors in all other independent directions. The square has paired roots 01 and 10 only, so the product has 2^(n-1) paired roots and derivative rank two. QED.

These results apply directly to the arbitrary facet coloring in the universal odd-bridge equivalence. In particular NORI1 holds for any odd upper-cube coloring whose lower facet has derivative rank at most two, yielding at least 2^(n-1) lower-facet paired-root witnesses.



## Exterior derivative-rank degree theorem

Let f be an arbitrary binary undirected cube-edge coloring. Form its global derivative matrix J with entries J_(k,x),i = f_k(x+e_i)+f_k(x), and put r=rank J and C=ker J. For direction k let epsilon_k be one if column k is zero and zero otherwise.

**Theorem.** The algebraic normal form of f_k has degree at most r-1+epsilon_k. Furthermore, the binary vector space of Boolean functions satisfying the first-order derivative relations of C and the self-edge condition D_k f_k=0 has dimension 2^(r-1+epsilon_k).

*Proof.* The vector space of squarefree Boolean polynomials is the exterior algebra on the degree-one symbols x_1,...,x_n over F2. Differencing in one bit, D_i f(x)=f(x+e_i)+f(x), removes x_i from each monomial containing it, so it is contraction by the corresponding dual basis vector. Every vector a in C gives a linear derivative operator sum_i a_i D_i annihilating each f_k. Self-edge invariance adds D_k f_k=0. Thus all contractions associated to H_k=C+span(e_k) annihilate f_k. This space has dimension n-r+1 when derivative column k is nonzero and dimension n-r when it vanishes.

For any s-dimensional subspace H of the dual of an n-dimensional vector space E, the common kernel of contractions from H on the exterior algebra is the exterior algebra of H-perp. To see this choose bases adapted to H; the contractions remove s independent generators, so the surviving monomials involve only the other n-s generators. The common kernel has dimension 2^(n-s) and degree no greater than n-s. Substitute the two possible dimensions of H_k. QED.

**Corollary (affine and quadratic rigidity).** If no direction is unread, rank at most two forces every edge-color function to be affine; rank at most three forces every such function to be quadratic. At rank three with nonzero derivative column k, the space of allowed direction-k functions has dimension four, of which the affine functions comprise a dimension-three subspace. Thus each direction has at most one independent nonlinear quadratic mode modulo affine terms.

*Proof.* The full allowed function space has dimension 2^(3-1)=4. The affine functions b+sum_i a_i x_i have gradients a in C-perp of dimension three; the condition a_k=0 removes one independent gradient dimension because e_k lies outside C. Including b gives dimension three. QED.

**Corollary (minimal obstruction).** A least-dimensional hypothetical paired-root-free coloring has nonzero pairwise distinct derivative columns, by the unread/twin restoration theorem. If it has n directions and derivative rank r, necessarily
\[
\boxed{n\le2^r-1,\qquad \max_k\deg f_k\le r-1.}
\]
This constraint applies to arbitrary nonlinear edge-colorings.

**Limitation.** Linear relations among first-order Boolean differences do not imply invariance under simultaneous flips of three or more original cube bits. The exterior-contraction proof only uses the valid linear differential relations.



## Binary matroid exterior normal form for nonlinear edge colorings

Let T be an r-by-n binary matrix of rank r, with columns t_1,...,t_n in F2^r. Interpret squarefree polynomials in the n vertex bits x_i as the exterior vector space Lambda(E), where E is the degree-one span of x_i. Exterior products represent squarefree coefficient tensors, not ordinary multiplication of Boolean functions.

For each direction k set
\[
\boxed{W_k=\{\sum_i(a\cdot t_i)x_i:\ a\cdot t_k=0\}\subseteq E.}
\tag{MN1}
\]
For t_k nonzero this has dimension r-1; for t_k zero it has dimension r.

**Theorem (complete derivative-matroid representation).** If every direction-k edge-color polynomial f_k is chosen from the exterior algebra Lambda(W_k), then it is independent of its own bit x_k and the global Boolean derivative matrix J(f) has rank at most r with all dependencies from ker T. Conversely, every arbitrary undirected binary cube-edge coloring f of global derivative rank r has some rank-r matrix T for which every f_k belongs to Lambda(W_k).

*Proof.* The Boolean derivative D_i f=f(x+e_i)+f(x) removes x_i from every squarefree monomial containing it; as a linear map on the exterior space, this is contraction with the i-th dual basis vector. For u in ker T, the contraction D_u=sum_i u_i D_i annihilates every degree-one form in W_k because D_u(sum_i(a dot t_i)x_i)=a dot Tu=0, and hence annihilates all of Lambda(W_k). Contraction by e_k also annihilates W_k, because a dot t_k=0. Therefore the chosen f_k are legal edge-color functions whose global derivative columns obey all relations of ker T, so rank J<=r.

Conversely choose a basis for the column span of J(f), and let the t_i encode its columns. Then ker J=ker T. Every f_k is annihilated by contractions from ker T and by its self-edge contraction D_k. The common kernel of contractions from a subspace H is the exterior algebra on its annihilator H-perp, proved in the previous degree theorem. Here H=ker T+span(e_k) and its annihilator is W_k. QED.

**Corollary (simple binary matroid obstruction).** A least-dimensional paired-root counterexample has a derivative-column matroid with no zero or repeated columns, by unrestricted paired-root unread/twin restoration. Thus its matroid is simple, has at most 2^r-1 points at rank r, and each point t_k carries a local exterior polynomial from Lambda(W_k). This also explains the degree bound deg f_k<=r-1.

**Theorem (canonical Fano quadratic normal form).** Suppose r=3 and the n=7 derivative labels comprise all seven nonzero vectors of F2^3. Then every permitted direction-k color polynomial has the form
\[
\boxed{f_k(x)=b_k+\sum_i(a_k\cdot t_i)x_i+
\eta_k\sum_{i<j}\det(t_i,t_j,t_k)x_ix_j,\quad a_k\cdot t_k=0,}
\tag{MN2}
\]
with binary constants b_k,eta_k and any a_k in the two-dimensional annihilator of t_k. Conversely these choices define legitimate edge colorings of global derivative rank at most three.

*Proof.* W_k has dimension two, so Lambda(W_k) has graded dimensions 1,2,1. The linear part has the displayed form. Let a,b be a basis for the annihilator of t_k. Its unique nonzero degree-two exterior generator has coefficient
(a dot t_i)(b dot t_j)+(a dot t_j)(b dot t_i)
on x_i x_j. This equals the alternating three-dimensional determinant det(t_i,t_j,t_k); the exterior two-form formed by a,b is normalized uniquely over F2. The quadratic component therefore has the one-bit coefficient eta_k. The converse follows from the general theorem. QED.

**Fano geometry.** For each k, det(t_i,t_j,t_k) is zero precisely when the three corresponding Fano points are collinear. Among the other six points there are fifteen unordered pairs, three of which lie with k on a Fano line. Thus each canonical nonlinear quadratic mode contains twelve quadratic monomials. Every local direction-k function in this maximal rank-three derivative kernel has four binary parameters (one constant, two linear, one quadratic), yielding sixteen permitted local functions.

**Research target.** Every derivative-irreducible paired-root obstruction has a simple binary-matroid exterior model. The first full nonlinear model occurs at rank three with the Fano plane. The missing general theorem is a matroid-compatible selection of two opposite monotone full cube paths, not another small-cube enumeration.



## Projective binary submatroids force high-order nonlinear translation symmetries

Let f be an arbitrary undirected cube-edge coloring with global derivative-column matrix J(f) of rank r. Represent its columns by t_i in F2^r as in the binary-matroid exterior normal form, so that every linear relation among the t_i is a global relation among the derivative operators on every edge-color function.

**Theorem (projective-subspace translation invariance).** Suppose there is a direction subset S whose derivative-column labels consist of the \(2^s-1\) nonzero vectors of an s-dimensional linear subspace of F2^r, each occurring once, with \(s\ge3\). Then for every direction k and every cube vertex x,
\[
\boxed{f_k(x+\mathbf1_S)=f_k(x),}
\tag{PG1}
\]
where \(\mathbf1_S\) flips all the direction bits of S simultaneously. This holds for arbitrary nonlinear functions f_k and arbitrary coloring outside S; no antipodal or affine assumption is needed.

*Proof.* Let D_i denote the Boolean difference operator \(D_i f(x)=f(x+e_i)+f(x)\). It satisfies \(D_i^2=0\), and all D_i commute. Choose basis labels for the s-dimensional subspace and corresponding s independent derivative operators \(\mathcal D_1,\ldots,\mathcal D_s\) acting on the span of the color functions and their translates. Every derivative operator D_i with i in S acts on that space as
\[
D_i=\sum_{a=1}^s t_{ai}\mathcal D_a.
\]
This identity follows from the global derivative-column relations: they hold on all color functions at every cube vertex and are preserved under further translations or Boolean derivatives. The operators \(\mathcal D_a\) commute and square to zero.

Flipping bit i acts as \(I+D_i\). Thus flipping all bits in S acts on every color function by
\[
\prod_{i\in S}(I+D_i)
=
\prod_{v\in\mathbb F_2^s\setminus\{0\}}
\left(I+\sum_{a=1}^s v_a\mathcal D_a\right).
\tag{PG2}
\]
We prove that this product is the identity in the algebra
\(A_s=\mathbb F_2[X_1,\ldots,X_s]/(X_1^2,\ldots,X_s^2)\) for every s>=3.

In the ordinary polynomial ring define
\[
F_s(Z)=\prod_{v\in\mathbb F_2^s}(Z+\sum_av_aX_a).
\]
Induction on s shows \(F_s(Z)\) is a linearized additive polynomial in Z with monomial powers \(Z^{2^j}\): for s=1, \(F_1(Z)=Z^2+X_1Z\); and
\[
F_s(Z)=F_{s-1}(Z)F_{s-1}(Z+X_s)
=F_{s-1}(Z)^2+F_{s-1}(X_s)F_{s-1}(Z).
\]
Its leading term is \(Z^{2^s}\). By homogeneity, the coefficient of each other possible monomial \(Z^{2^j}\), \(j\le s-1\), has X-degree \(2^s-2^j\), at least \(2^{s-1}\). For s>=3 we have \(2^{s-1}>s\). Every positive-degree coefficient therefore vanishes in \(A_s\), where a nonzero squarefree monomial has degree at most s. Consequently \(F_s(1)=1\) in \(A_s\). The v=0 factor of \(F_s(1)\) is one, so this proves (PG2) is the identity after substituting X_a=\mathcal D_a, and hence (PG1). \(\square\)

**Corollary (maximal simple derivative matroids are antipodally even).** If the derivative columns of an n-direction coloring comprise every nonzero vector of F2^r once, with n=2^r-1 and r>=3, then
\[
\boxed{f_k(\bar x)=f_k(x)\quad\text{for every }k,x.}
\]
Thus every such coloring is antipodally even, despite no symmetry being assumed in its definition.

**Lemma (path reversal for an even coloring).** If all edge-color functions satisfy f_k(\bar x)=f_k(x), then for every root z and every full dimension order \(\pi\),
\[
w_f(z,\pi^R)=\operatorname{rev}(w_f(z,\pi)).
\]
Indeed the reverse traversal of a full geodesic starts at its antipode and reverses the sequence of undirected edge colors. Translating that reverse geodesic antipodally starts it at the original root and preserves edge colors under the evenness assumption. Consequently
\[
\boxed{A_0(f)=A_1(f)=P(f).}
\tag{PG3}
\]
For these colorings the unrestricted paired-root assertion reduces to the one-sided existence of any full nondecreasing color geodesic.

**Caution.** The conclusion (PG1) concerns a simultaneous toggle of the whole \(2^s-1\)-direction projective set. It does not assert that the corresponding first-order derivative columns vanish or repeat. The projective submatroid may be simple, with every involved derivative column nonzero and distinct. This is a new high-order symmetry beyond the previously established single-direction and twin-direction deletion rules.

**Closure target.** The projective translation theorem identifies large nonlinear symmetry subsets in any coloring whose derivative matroid contains a full binary projective geometry of dimension at least two. A restoration theorem accommodating a \(2^s-1\)-direction invariant block, or a one-sided nondecreasing-geodesic theorem for antipodally even edge colorings, would immediately dispose of the maximal simple derivative kernels in all ranks. Neither further assertion is established by the present symmetry theorem.



## Quadratic-moment compression of Boolean derivative rank

Let \(f=(f_1,\ldots,f_n)\) be an arbitrary binary coloring of the undirected edges of \(Q_n\), with \(f_i(x+e_i)=f_i(x)\). The global Boolean-derivative matrix \(J(f)\) has \(i\)-th column \((D_i f_k(x))_{k,x}\), where \(D_i f_k(x)=f_k(x+e_i)+f_k(x)\). Put \(r=\operatorname{rank}_{\mathbb F_2}J(f)\). After choosing a basis of its column span, denote the label of column \(i\) by \(t_i\in\mathbb F_2^r\). Define
\[
q=r+\binom r2,\quad
\nu(t)=\bigl((t_a)_{a=1}^r,(t_at_b)_{1\le a<b\le r}\bigr)\in\mathbb F_2^q,\quad
M=(\nu(t_1)\ \cdots\ \nu(t_n)).
\]

**Theorem (quadratic-moment period theorem).** Every \(u\in\ker M\) is a simultaneous translation period of all the edge-color functions:
\[
\boxed{f_k(x+u)=f_k(x)\quad(k\in[n],\ x\in Q_n).}\tag{QM1}
\]
Consequently their common period group has codimension at most \(q\), and there exist functions \(F_k:\operatorname{im}M\to\mathbb F_2\) satisfying
\[
\boxed{f_k(x)=F_k(Mx),\qquad F_k(y+\nu(t_k))=F_k(y).}\tag{QM2}
\]

*Proof.* Consider the commutative square-zero algebra \(B_r=\mathbb F_2[X_1,\ldots,X_r]/(X_1^2,\ldots,X_r^2)\). Every linear form in the \(X_a\) has square zero. Define
\[
\Phi_T(u)=\prod_{i:u_i=1}(1+t_i\cdot X)\in B_r.
\]
Since each factor is its own inverse, \(\Phi_T\) is a homomorphism from the additive group \(\mathbb F_2^n\) to the multiplicative group of units of \(B_r\). We first establish
\[
\boxed{\Phi_T(u)=1\iff Mu=0.}\tag{QM3}
\]
Indeed, the coefficient of \(X_a\) in \(\Phi_T(u)\) is \(S_a=\sum_i u_i t_{ai}\). For \(a<b\), the coefficient of \(X_aX_b\) is
\[
S_aS_b+\sum_i u_i t_{ai}t_{bi}.
\]
Thus \(\Phi_T(u)=1\) implies \(Mu=0\).

Conversely, combine all factors with a common label \(t\), cancelling each pair, and observe that label \(0\) contributes the identity. The resulting choice of labels is an indicator vector \(v\) on \(\mathbb F_2^r\setminus\{0\}\), extended by zero at \(0\). For \(r\ge3\), let \(\mathcal C\) be the binary vector space of evaluation vectors of squarefree polynomials in the label variables of degree at most \(r-3\), punctured at label zero. This puncturing is injective, since the indicator of the single point zero has degree \(r\). Hence
\[
\dim\mathcal C=\sum_{j=0}^{r-3}\binom rj=2^r-1-q.
\]
Every vector in \(\mathcal C\) has zero first and second moments: the product of its defining polynomial with any monomial of degree one or two has degree at most \(r-1\), so its sum on \(\mathbb F_2^r\) is zero; the test monomial vanishes at label zero. The \(q\) first- and second-moment test vectors are linearly independent on the nonzero labels, because a polynomial of degree at most two with zero constant term that vanishes there also vanishes at zero and therefore vanishes identically. Dimension comparison identifies \(\mathcal C\) with the full kernel of these moment tests.

We show that \(\Phi(v)=1\) for all \(v\in\mathcal C\). The support of a label monomial \(\prod_{a\in I}t_a\), with \(|I|\le r-3\), is an affine subspace of dimension \(r-|I|\ge3\), partitionable into affine three-flats. The monomial evaluation vectors span \(\mathcal C\); it suffices to establish the identity on an affine three-flat \(w+\langle a,b,c\rangle\). Put \(z=1+w\cdot X\), \(A=a\cdot X\), \(B=b\cdot X\), \(C=c\cdot X\). Their squares vanish, and direct multiplication in \(B_r\) gives
\[
\prod_{\epsilon,\eta\in\mathbb F_2}(z+\epsilon A+\eta B)=z^4+ABz^2.
\]
Replacing \(z\) by \(z+C\) leaves the right-hand side unchanged. Multiplying the two four-point products gives
\[
(z^4+ABz^2)^2=z^8=1,
\]
the product over the eight labels of the flat. Any factor for label zero is \(1\). Taking products over sums of evaluation vectors proves \(\Phi(v)=1\) for all \(v\in\mathcal C\), hence for every vanishing-moment selection. For \(r\le2\), the moment evaluations distinguish all nonzero labels and are linearly independent, so vanishing moments allow only zero labels and cancellations of repeated labels. This establishes (QM3) in all ranks.

Choose \(r\) directions \(b_1,\ldots,b_r\) whose derivative columns form the selected basis. On the vector space spanned by all translates of all \(f_k\), the difference operators satisfy \(D_i=\sum_a t_{ai}D_{b_a}\). The equality follows from \(J(f)\) on each \(f_k\) at each vertex and persists under translation because the difference operators commute with translations. All \(D_{b_a}\) commute and square to zero. Translation by \(u\) is \(\prod_{i:u_i=1}(I+D_i)\). Substituting \(X_a=D_{b_a}\) into (QM3) shows that this is the identity on every \(f_k\) whenever \(Mu=0\), proving (QM1). Thus every \(f_k\) factors through \(M\), and its self-edge invariance gives the second equality in (QM2). \(\square\)

**Corollary (period code of a complete simple derivative matroid).** If the labels are precisely the \(2^r-1\) nonzero vectors of \(\mathbb F_2^r\), each once, then \(\operatorname{rank}M=q\), so \(\ker M\) has dimension
\[
2^r-1-r-\binom r2.
\]
For \(r\ge3\), this kernel is the binary Reed--Muller evaluation code of degree at most \(r-3\), punctured at zero. The code is generated by indicators of affine three-flats (punctured at zero). Thus the projective \(2^s-1\)-direction translation periods, \(s\ge3\), are instances of a larger system of periods determined by the quadratic moments of the derivative-column labels.

**Scope.** The theorem compresses the vertex dependence of every rank-\(r\) coloring to a linear quotient of dimension at most \(r(r+1)/2\), independently of \(n\). In the quotient the original \(n\) directions become labeled moves \(\nu(t_i)\), which a full cube geodesic must still traverse once each. The resulting path-selection problem remains open.



### Optimality of the quadratic-moment period bound

**Theorem (sharpness for every derivative rank at least three).** For every \(r\ge3\) there exists an edge coloring on the \(2^r-1\) directions labeled by all nonzero \(t\in\mathbb F_2^r\) whose derivative matrix has rank \(r\) and whose common translation-period group is precisely \(\ker M\). Thus the bound \(r+\binom r2\) in the quadratic-moment period theorem cannot be decreased for this class by replacing \(\ker M\) with a larger universally guaranteed translation-period group.

*Proof.* Write the cube bits as \(x_t\), indexed by the nonzero \(t\in\mathbb F_2^r\), and put
\[
L_a(x)=\sum_{t\ne0}t_a x_t,\qquad Q_{ab}(x)=\sum_{t\ne0}t_at_bx_t\quad(a<b).
\]
For each unordered pair \(a<b\), choose the direction \(k_{ab}\) labeled by the binary vector having zeros in positions \(a,b\) and ones at every other position. These \(\binom r2\) labels are nonzero and distinct because \(r\ge3\). Color direction \(k_{ab}\) by
\[
f_{k_{ab}}(x)=L_a(x)L_b(x)+Q_{ab}(x)
=\sum_{s<t}(s_at_b+s_bt_a)x_sx_t,
\]
where the sum is over a fixed ordering of the nonzero binary labels. Color all remaining directions constantly zero. Because the label of \(k_{ab}\) has zero entries at \(a,b\), its color is independent of its own direction bit, so this defines an undirected-edge coloring.

Its first derivatives satisfy
\[
D_t f_{k_{ab}}(x)=t_aL_b(x)+t_bL_a(x).
\]
As \(x\) varies, \((L_1(x),\ldots,L_r(x))\) ranges over all of \(\mathbb F_2^r\). For each \(a<b\), the derivative rows from direction \(k_{ab}\) therefore span the two linear functionals \(t\mapsto t_a\) and \(t\mapsto t_b\). Taking all pairs shows that the derivative-column rank is \(r\), with column labels \(t\) in this basis.

For a translation vector \(u\), write \(U_a=L_a(u)\). Direct expansion yields
\[
f_{k_{ab}}(x+u)+f_{k_{ab}}(x)
=U_aL_b(x)+U_bL_a(x)+U_aU_b+Q_{ab}(u).
\]
If \(u\) preserves all the color functions, this expression vanishes for every \(x\) and every pair \(a<b\). Independence of the forms \(L_a,L_b\) forces \(U_a=U_b=0\) for each pair, hence \(L(u)=0\). The displayed expression then reduces to \(Q_{ab}(u)\), which must also vanish for every pair. Therefore \(Mu=0\). The converse is the quadratic-moment period theorem, proving that the period group is \(\ker M\). \(\square\)

In particular the codimension \(r(r+1)/2\) can be attained by a family of quadratic color functions, even though their global derivative rank is only \(r\). Any stronger all-rank compression must use information beyond universal translation periods.



### A simple twelve-point derivative matroid with no affine three-flat

**Proposition (flat-free quadratic-moment period).** Let
\[
T=\{t\in\mathbb F_2^5:t_1t_2+t_3t_4=1\}.
\]
Then \(T\) contains twelve distinct nonzero vectors and satisfies \(\sum_{t\in T}\nu(t)=0\) for the quadratic-moment lift \(\nu:\mathbb F_2^5\to\mathbb F_2^{15}\). Nevertheless \(T\) contains no affine three-flat and no complete seven-point projective plane. Consequently **every** cube-edge coloring whose twelve derivative columns have these distinct labels is antipodally even, although its derivative matroid contains neither of these saturated local configurations.

*Proof.* The quadratic Boolean polynomial \(q(t)=t_1t_2+t_3t_4\) is the indicator of \(T\). Its first four bits have six solutions, and the fifth bit is free; thus \(|T|=12\) and \(0\notin T\). For every squarefree monomial \(p(t)\) of degree one or two, the product \(p(t)q(t)\) has degree at most four in five variables, so its sum over \(\mathbb F_2^5\) is zero. These are precisely the first- and second-moment identities \(\sum_{t\in T}\nu(t)=0\).

The six solutions in the first four bits are
\[
\{(11,v):v\in\{00,01,10\}\}\ \cup\
\{(u,11):u\in\{00,01,10\}\}.
\]
No four distinct points of this six-point set sum to zero. Indeed, if three are taken from one group and one from the other, the fixed two-bit block has nonzero sum; if two are taken from each group, the sum of the two distinct variable blocks is nonzero. Thus the six-point set has no affine two-flat. Any affine three-flat in \(\mathbb F_2^5\) projects onto an affine subspace of dimension at least two in the first four bits, and hence cannot lie inside \(T\).

If the seven nonzero members of a three-dimensional linear subspace \(U\) lay in \(T\), the restriction \(q|_U\) would equal the indicator of the nonzero vectors of \(U\). In three independent binary variables that indicator has algebraic degree three, whereas \(q|_U\) has degree at most two. This contradiction excludes complete projective planes. Finally, the quadratic-moment period theorem applied to \(\sum_{t\in T}\nu(t)=0\) shows that flipping all twelve directions preserves every color function. \(\square\)

**Structural implication.** The period code \(\ker M\) can contain nonzero words even when the derivative-label configuration contains no affine three-flat or complete projective plane. Thus a proof based solely on detecting saturated projective subsets would overlook global nonlinear translation periods; structural induction must account for aggregate moment cancellations.



**Nonlinear realization.** Identify the twelve direction labels in \(T\) with integers in low-bit-first binary order, and put \(L_a(x)=\sum_{t\in T}t_ax_t\). For the five distinct labels \(k_1=12,k_2=13,k_3=3,k_4=7,k_5=11\), each having \((k_a)_a=0\), assign \(f_{k_a}=L_a\). The remaining colors are initially zero. The five derivative rows span the five label-component functions, and \(T\) spans \(\mathbb F_2^5\). Hence the resulting derivative matrix has rank five with nonzero pairwise distinct columns labeled by \(T\).

Now set, in the previously unused direction \(28=(0,0,1,1,1)\in T\),
\[
f_{28}(x)=L_1(x)L_2(x)+\sum_{t\in T}t_1t_2x_t.
\]
This rule is independent of bit \(x_{28}\), has a nonzero quadratic part, and satisfies \(D_t f_{28}=t_1L_2+t_2L_1\). All its derivative rows lie in the previous five-dimensional span. The full coloring therefore has derivative rank five, a non-affine color function, twelve distinct nonzero derivative labels, and the flat-free twelve-direction period.


### One-way periodic block restoration

Let \(S,T\) be a partition of the direction set of an arbitrary binary edge coloring \(f\), with both parts nonempty. Assume
\[
 f_i(s,t)=h_i(s)\quad(i\in S),\qquad
 f_j(s+\mathbf1_S,t)=f_j(s,t)\quad(j\in T).
 \tag{PB1}
\]
For each \(s\in Q_S\), let \(g_s\) be the edge coloring of \(Q_T\) obtained by fixing the \(S\)-bits to \(s\).

**Theorem (periodic-block restoration).** Under (PB1),
\[
\boxed{\bigcup_{s\in P(h)}\bigl(\{s\}\times P(g_s)\bigr)\subseteq P(f),
\qquad
|P(f)|\ge\sum_{s\in P(h)}|P(g_s)|.}
\tag{PB2}
\]
An analogous inclusion holds for each monotone orientation separately.

*Proof.* Fix \(s\in P(h)\) and \(t\in P(g_s)\). Choose nondecreasing full geodesics in \(h\) and \(g_s\) with initial roots \(s,t\), and words \(0^a1^b\), \(0^p1^q\). Follow the first \(p\) steps of the \(T\)-geodesic, then the whole \(S\)-geodesic, then the remaining \(q\) steps of the \(T\)-geodesic. The \(S\)-bits equal \(s\) before their complete traversal and \(\bar s=s+\mathbf1_S\) afterward. By the second part of (PB1), all \(T\)-edges have the colors they had in \(g_s\). By the first part of (PB1), all \(S\)-edges have their colors from \(h\), independently of the \(T\)-bits. Therefore the resulting full geodesic has word \(0^{p+a}1^{b+q}\).

Repeat from the same root \((s,t)\) with the nonincreasing geodesics in \(h\) and \(g_s\), inserting the full \(S\)-path at the \(1\)-to-\(0\) seam of the \(T\)-path. This gives word \(1^*0^*\). Both paths use every dimension once. Hence \((s,t)\in P(f)\), and distinct choices give distinct roots. The same construction restricted to either orientation proves the final assertion. \(\square\)

**Corollary (minimal-counterexample exclusion).** A least-dimensional paired-root-free coloring contains no proper nonempty block \(S\) satisfying (PB1). Otherwise \(h\) and each \(g_s\) have fewer dimensions and possess paired roots by minimality, contradicting (PB2).

**Corollary (projective source-block elimination).** Suppose a proper nonempty set \(S\) of directions has derivative-column labels comprising all nonzero vectors of a binary subspace of dimension \(r\ge3\), each once. If every \(S\)-direction color function is independent of the bits in \(T\), then \(S\) is removable in the paired-root minimal-counterexample induction.

*Proof.* The projective translation-period theorem guarantees that simultaneous flipping of the bits in \(S\) preserves every edge-color function, giving the second hypothesis of (PB1). The assumed external independence gives its first hypothesis. Apply the preceding corollary. \(\square\)

This mechanism permits nonlinear dependence of \(T\)-direction colors on \(S\)-bits. For instance,
\[
f_1=x_2,\quad f_2=x_3,\quad f_3=x_1,\quad
f_4=x_5+x_1+x_2,\quad f_5=x_4\pmod2
\]
has directed cycles on \(S=\{1,2,3\}\) and \(T=\{4,5\}\), together with arrows from \(S\) to \(T\), and no directed sink. Nevertheless (PB1) holds. Periodic-block restoration thus eliminates configurations which survive every individual sink-deletion step. The theorem applies at arbitrary block size and does not resolve unrestricted strongly connected influence cores.


### Quadratic-moment period supports must receive external influence

Retain the global derivative-column labels \(t_i\in\mathbb F_2^r\) and the quadratic-moment matrix \(M\) with columns
\[
\nu(t_i)=\bigl((t_{ia})_{a\in[r]},(t_{ia}t_{ib})_{a<b}\bigr).
\]
Let \(D(f)\) be the directed influence graph, with an arc \(j\to i\) when \(D_jf_i\) is nonzero somewhere.

**Corollary (period-support indecomposability of a minimal obstruction).** If \(f\) is a least-dimensional paired-root-free coloring, then for every nonzero \(u\in\ker M\) having proper support \(S=\{i:u_i=1\}\subsetneq[n]\), there is an influence arc
\[
\boxed{j\longrightarrow i\quad\text{with }j\notin S,\ i\in S.}
\tag{PM1}
\]
Equivalently, no proper nonempty source-closed direction set can equal the support of a word in the quadratic-moment period code \(\ker M\).

*Proof.* By the quadratic-moment period theorem, \(u\in\ker M\) implies \(f_k(x+u)=f_k(x)\) for every \(k\) and \(x\). If there were no arc from \(T=[n]\setminus S\) into \(S\), the color function of every \(S\)-direction edge would be independent of all \(T\)-bits. Flipping all bits of \(S\) is precisely translation by \(u\), and preserves every \(T\)-direction edge color. Thus (PB1) would hold and the periodic-block restoration theorem would contradict minimality. \(\square\)

This condition applies to nonlinear period words of arbitrary support, including the twelve-point flat-free example above: a complete projective subgeometry is unnecessary. It couples the binary-matroid moment kernel to the condensation structure of the directed influence graph. A future proof through this route would need either to produce a period word whose support is source-closed, or to show that the forced incoming arcs for every proper period support cannot coexist in a minimal obstruction.


## Strongly connected nonlinear influence with sparse favorable roots

**Theorem.** For every \(n=2m\ge6\), pair directions \(a_t=2t,b_t=2t+1\) and define an ordinary cube-edge coloring by
\[
f_{b_t}(x)=x_{a_t},\qquad
f_{a_t}(x)=x_{b_t}+\prod_{j\ne a_t}(1+x_j)
\quad\text{over }\mathbb F_2. \tag{SC1}
\]
Its full directed influence graph (arrow \(j\to i\) when \(f_i\) reads bit \(j\)) is strongly connected, yet
\[
\boxed{A_0(f)=\{x:(x_{a_t},x_{b_t})\ne(1,1)\ \forall t\},\quad
|A_0(f)|=3^m,\quad |P(f)|=2^m.} \tag{SC2}
\]
Consequently even one strongly connected influence component may have favorable-root density \((3/4)^m\) and paired-root density \((1/2)^m\), both tending to zero.

*Proof.* Compare (SC1) with the Cartesian product \(h_{a_t}(x)=x_{b_t},h_{b_t}(x)=x_{a_t}\) of reciprocal-reader squares. The sole alterations are that the \(m\) even-direction edges incident with \(0^n\) change from color zero to one.

Every root with pairs in \(\{00,01,10\}\) remains rising-favorable. For every \(00\) pair traverse \(b_t\) during the initial all-zero phase, and \(a_t\) later in the all-one phase. For every \(01\) pair traverse \(a_t,b_t\) successively, both color one. For every \(10\) pair traverse \(b_t,a_t\) successively, again both color one. Shuffle these within-pair steps to put all zero edges first. Every traversed even edge then sees \(x_{b_t}=1\), so its exceptional product term is zero. This constructs the required path.

Conversely suppose a rising full path begins at a root containing a pair \(11\). Within that pair the first step has color one, and the second would have color zero unless it is an altered even edge. Thus its odd step must precede its even step, and the even step must be the altered edge **entering** vertex \(0^n\). At most one \(11\) pair can be repaired in this way, because the geodesic visits \(0^n\) at most once.

At the moment of arrival at \(0^n\), consider any different pair. It cannot start at \(11\) by the preceding argument. Starting pattern \(10\) leaves its odd edge untraversed with color zero, forbidden after the previously traversed color-one edge. Starting \(00\) leaves both directions untraversed, and its first remaining edge is color zero unless it is the altered even edge immediately **leaving** \(0^n\). Starting \(01\) leaves its even edge untraversed, also of color zero unless it is the same immediately outgoing altered edge. Hence each of the other \(m-1\ge2\) pairs would require the single outgoing edge of \(0^n\), impossible. Thus no rising root contains \(11\), proving the first formula of (SC2).

The function \(f_{a_t}\) reads every other bit: for a bit other than \(b_t\), vary that bit with all other inputs zero; for \(b_t\), set a third bit to one to suppress the product and expose its linear dependence. Each \(f_{b_t}\) reads \(x_{a_t}\). Therefore every direction can reach an even direction, and the even directions reach every vertex through their odd partners: the directed influence graph is strongly connected.

Reversing a full path gives \(A_1(f)=\overline{A_0(f)}\). Hence paired roots require each two-bit block to be neither \(00\) nor \(11\), leaving precisely \(01,10\) and giving \(|P(f)|=2^m\). \(\square\)

**Implication.** This example does not refute NORI1: \(f\) is an ordinary facet coloring with many paired roots. It refutes a proposed dimension-independent density route even after imposing strong connectivity of the *directed* influence core. Strong-connectivity reductions must retain root-compatibility data rather than infer majority from irreducibility.


## Antipodally odd strongly connected cubes with sparse monochromatic starting roots

The preceding ordinary-facet construction extends to the original NORI1 class, where sparsity concerns starting vertices of monochromatic antipodal geodesics themselves.

**Theorem.** For each \(m\ge3\), put \(n=2m\), pair directions \(a_t=2t,b_t=2t+1\), and adjoin a bridge direction \(h=n\). Write vertices of \(Q_{n+1}\) as \((y,s)\in Q_n\times\mathbb F_2\). Define
\[
\begin{aligned}
c_{b_t}(y,s)&=y_{a_t},\\
c_{a_t}(y,0)&=y_{b_t}+\prod_{j\ne a_t}(1+y_j),\\
c_{a_t}(y,1)&=y_{b_t}+\prod_{j\ne a_t}y_j,\\
c_h(y,s)&=y_{a_0}.
\end{aligned} \tag{SO1}
\]
All operations in the color rules are over \(\mathbb F_2\). This is an antipodally odd coloring of undirected edges of \(Q_{2m+1}\), and its directed influence graph is strongly connected. The set \(M(c)\) of starting vertices of monochromatic dimension-simple antipodal geodesics is
\[
\boxed{M(c)=
\{(y,s): (y_{a_t},y_{b_t})\in\{01,10\}
\text{ for every }t,\quad s\in\{0,1\}\}.} \tag{SO2}
\]
In particular
\[
\boxed{|M(c)|=2^{m+1},\qquad
|M(c)|/2^{2m+1}=2^{-m}.} \tag{SO3}
\]

*Proof.* For any lower direction \(i\), formula (SO1) is independent of the bit \(y_i\); the bridge color is independent of \(s\). Antipodal complementation sends \(s\) to \(1-s\) and \(y\) to \(\bar y\). It flips all odd-direction colors, exchanges the lower product \(\prod_{j\ne a_t}(1+y_j)\) with the upper product \(\prod_{j\ne a_t}y_j\), and flips \(c_h=y_{a_0}\). Hence the coloring is antipodally odd.

Compare with the base coloring
\[
d_{a_t}(y,s)=y_{b_t},\quad
d_{b_t}(y,s)=y_{a_t},\quad d_h(y,s)=y_{a_0}.
\]
The only changes from \(d\) are the even-direction edges incident with \(y=0^n\) in the lower bridge facet, whose colors switch \(0\to1\), and the even-direction edges incident with \(y=1^n\) in the upper bridge facet, whose colors switch \(1\to0\). These are the two *exceptional stars*.

A monochromatic zero path cannot traverse a changed lower-star edge, which has color one. Suppose it uses a changed upper-star edge. Its lower-bit projection visits \(1^n\) in the upper facet. At most two edges of its full geodesic are incident with this vertex, so among the \(m\ge3\) direction pairs at least one pair uses no exceptional edge. In that unaffected pair both traversal colors must be zero under the reciprocal-reader base rules. The initial pair must therefore be \(01\) or \(10\), and its two-step trajectory passes through \(00\) rather than \(11\). Thus this pair cannot have both bits one at the upper corner, a contradiction.

Likewise a monochromatic one path cannot traverse a changed upper-star edge of color zero. If it used a changed lower-star edge, it would visit \(0^n\) in the lower facet. Some direction pair would be unaffected by the at most two incident edges. For the unaffected pair, both base traversal colors are one only if its initial bits are \(01\) or \(10\); its two-step trajectory then passes through \(11\), never \(00\). This contradicts visiting the lower corner. Hence **no monochromatic path uses any exceptional edge**.

Under the base reciprocal-reader rules, a two-direction block admits a monochromatic traversal iff its initial bits are \(01\) or \(10\). Since every full path traverses both directions of every block, the preceding paragraph proves the necessary part of (SO2).

Conversely let all starting blocks be \(01\) or \(10\), with either initial bridge bit \(s\). Construct a color-zero full path as follows. If \(y_{a_0}=0\), traverse the bridge first. If \(y_{a_0}=1\), traverse \(a_0\) first, then the bridge. The bridge is crossed when \(y_{a_0}=0\), hence with color zero. Complete every block with a color-zero reciprocal-reader order: for \(01\) traverse odd then even, and for \(10\) traverse even then odd, respecting the previously traversed \(a_0\) when applicable. Process other blocks one after another. Throughout, at least one block not currently being traversed has one bit equal to one, while no block ever has both bits one. Consequently the path visits neither \(0^n\) nor \(1^n\) during a traversal of a lower-direction edge, so it uses no exceptional edge and remains monochromatic zero. This proves sufficiency.

For strong connectivity, the lower facet already has the strongly connected directed influence graph of (SC1). These dependencies persist in (SO1). The bridge rule gives an arrow \(a_0\to h\); the different lower and upper even-direction color functions give arrows \(h\to a_t\) for every \(t\). Thus \(h\) belongs to the same strongly connected component as all lower directions. Finally the \(m\) independent choices \(01,10\) and the two bridge bits give (SO3). \(\square\)

**Consequence for closure methods.** In an antipodally odd NORI1 instance, even a single strongly connected directed influence component can admit monochromatic geodesics from an exponentially small proportion of vertices. The conjecture concerns existence, not root density. A universal local-to-global proof based on majority of starting roots cannot be rescued by requiring strong connectivity or antipodal oddness. This is an explicit positive NORI1 family, not a counterexample.


## Two-fold path packing and robust odd-coloring closure

Fix \(m\ge2\), \(n=2m+1\), with direction pairs \(a_t=2t,b_t=2t+1\), \(0\le t<m\), and an additional direction \(h=2m\). Define the antipodally odd edge coloring
\[
d_{a_t}(x)=x_{b_t},\quad d_{b_t}(x)=x_{a_t},
\quad d_h(x)=x_{a_0}. \tag{RP1}
\]
Select roots whose paired bits each equal \(01\) or \(10\), allowing either initial \(h\)-bit. There are \(2^{m+1}\) roots. At each such root \(x\), choose the following direction order \(P_x\). In block zero, traverse \(h,b_0,a_0\) if its starting bits are \(01\), or \(a_0,h,b_0\) if they are \(10\). Subsequently, for \(t=1,\ldots,m-1\), traverse \(b_t,a_t\) if block \(t\) starts \(01\), or \(a_t,b_t\) if it starts \(10\). Direct substitution in (RP1) shows that every \(P_x\) is an all-zero full antipodal geodesic.

**Theorem (at most two paths per antipodal edge pair).** Every antipodal pair of undirected cube edges occurs in at most two paths of the family \(\{P_x\}\).

*Proof.* Because \(d\) is antipodally odd and the selected paths are all-zero, only one member of an antipodal edge pair can occur in the family.

Fix an undirected edge in a lower direction belonging to block \(t\). At its traversal, all blocks before \(t\) have finished and all blocks after \(t\) remain untouched. The bit state of every other block therefore recovers that block's initial \(01/10\) pattern uniquely. If \(t>0\), the bridge has already been crossed, so its current bit recovers the initial bridge bit. If \(t=0\), its bridge-crossing status is determined by the initial pattern of block zero, so the initial bridge bit is again uniquely determined after choosing that pattern. The active block \(t\) has only two possible initial patterns, proving that the edge appears in at most two selected paths.

For a bridge edge, the nonzero-index blocks have not yet been traversed, and their initial patterns are read directly. At the bridge traversal, block zero is in state \(01\) if it began \(01\), or state \(00\) if it began \(10\), recovering its starting pattern. Only the starting bridge bit may vary, and there are two choices. Hence every edge lies on at most two selected paths. \(\square\)

**Corollary (exponential tolerance to arbitrary recoloring).** Suppose an odd edge coloring \(c\) differs from \(d\) on at most \(t\) antipodal edge pairs, with no restriction on the positions, directions or dependencies of those changes. Then at least
\[
\boxed{\max\{0,2^{m+1}-2t\}} \tag{RP2}
\]
of the selected rooted geodesics are still monochromatic zero in \(c\). In particular, every such \(c\) with \(t<2^m\) satisfies NORI1.

*Proof.* Each flipped antipodal edge pair spoils at most two selected paths. The union of spoiled paths has size at most \(2t\), so the remaining paths retain their original monochromatic words. \(\square\)

**Scope.** This gives a positive dimension-uniform class closed under exponentially many arbitrary nonlinear antipodal edge-pair recolorings, without assuming acyclic or bounded-feedback influence graphs. It is a certificate-packing theorem for a restricted but robust neighborhood of the reader-pair coloring, not an unrestricted NORI1 proof.


**Proposition (sharpness for the selected certificate family).** The minimum number of antipodal edge pairs meeting every selected canonical path \(P_x\) in (RP1) is precisely \(2^m\).

*Proof.* By the two-fold incidence theorem, fewer than \(2^m\) edge pairs can meet at most \(2t<2^{m+1}\) selected paths, so the transversal number is at least \(2^m\). Every selected path traverses one bridge edge. The bridge crossings have lower-bit patterns consisting of \(01\) or \(00\) in block zero and \(01\) or \(10\) in every other block, so there are \(2^m\) distinct bridge-edge antipodal pairs used by the family. Their union meets every selected path. Thus the lower bound is attained. \(\square\)

This sharpness refers to interception of the **fixed canonical path family**, not to the minimum number of edge-pair recolorings needed to eliminate *all* monochromatic paths of the original coloring. In general those are different transversal problems.


## Even-dimensional extension and a global distance bound for hypothetical obstructions

**Theorem (paired-reader error tolerance in every dimension).** Let \(n\ge2\) and \(m=\lfloor n/2\rfloor\). For even \(n=2m\), define the antipodally odd reciprocal-reader coloring
\[
d_{2t}(x)=x_{2t+1},\qquad d_{2t+1}(x)=x_{2t},
\quad 0\le t<m. \tag{RE1}
\]
For each of the \(2^m\) starting roots whose paired bits are all \(01\) or \(10\), choose the full path that visits the blocks in order, traversing their odd direction before their even direction if the block starts \(01\), and their even direction before their odd direction if it starts \(10\). Every selected path is all-zero.

Every antipodal edge pair occurs in at most two selected paths. Consequently changing the colors on any \(t\) antipodal edge pairs leaves at least \(\max\{0,2^m-2t\}\) selected monochromatic paths; in particular \(t<2^{m-1}\) preserves NORI1.

*Proof.* A lower-direction edge in block \(j\) occurs after every earlier block was fully toggled and before every later block was touched. Its incident bit values recover the initial patterns in all the other blocks. For its own block, either of the two initial patterns \(01,10\) is possible, and no third pattern is admitted. Thus the edge lies on at most two selected paths. Antipodal oddness ensures its antipodal mate, which is color one, lies on none. The preceding path-packing union bound proves the assertion. \(\square\)

The odd-dimensional case \(n=2m+1\) was proved above using one extra bridge reader, with \(2^{m+1}\) selected paths and robustness for \(t<2^m\).

**Corollary (uniform necessary Hamming separation).** In every dimension \(n\ge2\), let \(\mathscr D_n\) contain the relevant paired-reader baseline(s) above, together with all their images under cube automorphisms (bit translations and permutations of dimensions) and optional global exchange of edge colors. Define \(d_{\rm odd}(c,d)\) as the number of antipodal pairs of undirected edges on which two antipodally odd colorings differ. If a bad antipodally odd coloring \(c\) of \(Q_n\) exists, then
\[
\boxed{\min_{d\in\mathscr D_n}d_{\rm odd}(c,d)\ge
2^{\lceil n/2\rceil-1}.} \tag{RE2}
\]
Indeed every coloring closer than this to any one of these templates retains one of its explicit monochromatic path certificates. The cube automorphisms and global color exchange preserve the oddness condition, path existence and antipodal edge-pair distance.

**Limitation.** The inequality is a universal necessary property of any bad coloring in odd or even dimension, not a contradiction: the space of legal colorings is much larger than the union of these Hamming balls. It supplies a distance-from-tractable-templates parameter for future minimal-counterexample extremization. It does not support an assertion that a bad coloring must be close to some template.


**Low-dimensional endpoint.** The odd-dimensional canonical bridge construction and two-fold incidence proof also hold for \(m=1\), where there is one reciprocal reader pair and one bridge direction. Its four selected roots give four zero-colored paths, and each antipodal edge pair meets at most two of them. Thus the bound (RE2) includes \(n=3\); the even construction includes \(n=2\). These endpoint verifications require no additional dimension hypothesis.


## Optimal edge-disjoint monochromatic geodesic packings in even dimension

The earlier reciprocal-reader packing has edge-pair multiplicity two and yields radius roughly \(2^{n/2}\). A different construction gives the largest possible disjoint certificate family in **every even dimension**, improving the guaranteed legal-coloring perturbation radius to order \(2^n\). Its argument is a direct partition of cube edges, without any auxiliary geometry.

**Theorem (fixed-order antipodal geodesic decomposition).** Let \(n\ge2\) be even and fix a direction permutation \(\pi\). For every even-Hamming-parity root \(x\), let \(P_x^\pi\) be the rooted full cube geodesic traversing the directions in order \(\pi\). Then the \(2^{n-1}\) paths \(P_x^\pi\) partition \(E(Q_n)\). Antipodal complementation sends \(P_x^\pi\) onto \(P_{\bar x}^\pi\), and because \(n\) is even, both roots have even parity.

*Proof.* Fix an edge in direction \(i\), and let \(S_i\) be the set of directions preceding \(i\) in \(\pi\). The two potential roots from which the given edge is traversed at step \(i\) are the endpoints of that edge with the bits of \(S_i\) toggled. They differ in the single bit \(i\), so precisely one has even parity. Thus the paths partition the edges. Complementing all vertex bits transforms a \(\pi\)-ordered path rooted at \(x\) into a \(\pi\)-ordered path rooted at \(\bar x\). \(\square\)

**Theorem (optimal zero-path packing with antipodal oddness).** Let \(g\) be any Boolean labeling of the even-parity roots obeying \(g(\bar x)=1-g(x)\). For each undirected edge \(e\), let \(x(e)\) be its unique even-parity root in the preceding decomposition and put
\[
c_g(e)=g(x(e)). \tag{OP1}
\]
Then \(c_g(\bar e)=1-c_g(e)\), and precisely \(2^{n-2}\) of the paths \(P_x^\pi\) are monochromatic zero. These zero paths are edge-disjoint and use no two edges from the same antipodal edge pair. Hence changing colors on any \(t\) antipodal edge pairs preserves at least
\[
\boxed{\max\{0,2^{n-2}-t\}} \tag{OP2}
\]
of the chosen zero geodesics. The size \(2^{n-2}\) is the largest possible number of pairwise edge-disjoint zero full geodesics in any antipodally odd coloring of \(Q_n\).

*Proof.* Antipodality follows because \(x(\bar e)=\overline{x(e)}\). Each \(P_x^\pi\) has constant color \(g(x)\), and the involution on even roots exchanges the two labels, giving precisely \(2^{n-2}\) zero paths. Each antipodal edge pair has one zero and one one-colored edge, and the partition uses each zero edge once. A recoloring of one antipodal edge pair therefore spoils at most one selected zero path, proving (OP2). Finally any odd edge coloring has precisely \(n2^{n-2}\) zero edges, whereas each edge-disjoint monochromatic zero full geodesic consumes \(n\) of them. Thus at most \(2^{n-2}\) such paths exist. \(\square\)

**A simple explicit baseline.** With \(\pi=(0,\ldots,n-1)\), choose \(g(x)=x_0\) on even-parity roots. Formula (OP1) then becomes
\[
\boxed{c_0(x)=\sum_{j=1}^{n-1}x_j,\qquad
c_i(x)=1+x_0\ \ (1\le i<n),} \tag{OP3}
\]
where the first sum and all subsequent additions are modulo two. All even-parity starting roots with \(x_0=0\) follow the order \(\pi\) along a monochromatic zero path; the paths partition the zero-colored edges.

**Odd-dimensional extension.** For odd \(n\ge3\), let \(d=n-1\) be even and use the baseline (OP3) on both horizontal facets of \(Q_d\times Q_1\), independent of the added bridge bit \(s\). Color each bridge edge above \(y\) by \(y_0\). This full coloring is antipodally odd: the horizontal baseline is odd under complementing \(y\), and the bridge value \(y_0\) is odd as well. For each even-parity lower root \(y\) with \(y_0=0\), start at \((y,0)\), cross the bridge first (color zero), and then traverse all \(d\) horizontal directions in fixed order (all zero). These \(2^{n-3}\) monochromatic full paths are pairwise edge-disjoint and avoid antipodal pairs of each other's edges. Accordingly, arbitrary recoloring on \(t<2^{n-3}\) antipodal edge pairs preserves a monochromatic geodesic.

**Odd-dimensional parity obstruction to perfect edge packing.** Suppose \(n\) is odd and \(k\) monochromatic-zero antipodal geodesics are pairwise edge-disjoint. Their antipodal images are \(k\) edge-disjoint one-colored geodesics and are edge-disjoint from the zero paths. The union therefore consists of \(2k\) edge-disjoint full geodesics. At each cube vertex, every zero path with that vertex as endpoint has its antipodal image also ending there; endpoint-degree contributions occur in pairs, whereas every internal path visit contributes two. Thus the degree of this union at every vertex is even. Since \(\deg_{Q_n}(v)=n\) is odd, at least one edge incident with each vertex remains unused. Counting degrees yields
\[
2kn\le (n-1)2^{n-1},
\quad\text{so}\quad
\boxed{k\le \left\lfloor\frac{n-1}{n}2^{n-2}\right\rfloor.} \tag{OP4}
\]
In particular the even-dimensional perfect packing of \(2^{n-2}\) zero paths is impossible in odd dimension. No claim that the odd construction attains the best possible bound is made.

**Necessary distance from tractable templates.** Let \(\mathscr D_n\) contain these even-dimensional fixed-order partition colorings for all \(\pi,g\), and for odd dimension the corresponding bridge extensions and cube-symmetry copies. If a bad antipodally odd coloring \(c\) of \(Q_n\) exists, then its antipodal-edge-pair Hamming distance from every member \(d\in\mathscr D_n\) obeys
\[
\boxed{
d_{\rm odd}(c,d)\ge
\begin{cases}
2^{n-2},&n\text{ even},\\
2^{n-3},&n\text{ odd}.
\end{cases}} \tag{OP5}
\]
This strengthens the previously published reciprocal-reader radius for all sufficiently large dimensions. It is only a necessary exclusion region, not a proof that arbitrary colorings are close to any of these templates.


**Partition certificate identity.** In (OP1), every independent antipodal edge-pair variable has one zero-colored edge. The \(2^{n-2}\) selected zero geodesics partition these variables into disjoint sets \(B_x\), each of size \(n\). For any family \(F\) of flipped edge pairs, the number of selected surviving monochromatic-zero geodesics is
\[
2^{n-2}-|\{x:B_x\cap F\ne\varnothing\}|. \tag{OP6}
\]
Thus hitting every member of this selected family needs \(2^{n-2}\) flips. This does not imply that every monochromatic path of the perturbed coloring is destroyed.


### Complete nonlinear influence with exponentially sparse antipodal roots

**Theorem (component classification and sharp root support for an all-to-all nonlinear family).** For each integer \(k\ge3\), there is an antipodally odd coloring \(c\) of the undirected edges of \(Q_{2k}\) with the following properties.

1. Every direction function is nonlinear, and for each pair of distinct directions \(a,b\), its derivative \(\partial_b c_a\) is nonzero somewhere. Thus the directed influence graph is the complete loopless digraph.
2. Its red spanning subgraph has \(2^k-k+1\) connected components, with the component descriptions below.
3. The set \(S(c)\) of roots joined to their antipodes by a monochromatic path, with no path-length restriction, is precisely
\[
S(c)=\bigl\{x:\text{all dimension pairs are }01\text{ or }10\bigr\}
\cup
\bigl\{x:\text{one pair is }00,\text{ one distinct pair is }11,
\text{ and all others are }01\text{ or }10\bigr\}.
\]
Each root in this set admits a monochromatic **full antipodal geodesic of each color**. In particular,
\[
\boxed{|S(c)|=2^k+k(k-1)2^{k-2},\quad
\frac{|S(c)|}{2^{2k}}=\left(1+\frac{k(k-1)}4\right)2^{-k}.}
\]
There is therefore no positive uniform lower bound on the proportion of roots admitting any monochromatic antipodal path, even within legal colorings whose directed influence graph is complete and whose every direction rule is nonlinear.

*Construction and legality.* Partition the dimensions into \(k\) ordered pairs. Put
\[
z_j=x_{2j-1}\oplus x_{2j},
\qquad
F_j(x)=\prod_{\ell\ne j} z_\ell.
\]
Define
\[
c_{2j-1}(x)=x_{2j}\oplus F_j(x),\qquad
c_{2j}(x)=x_{2j-1}\oplus F_j(x).
\tag{SR1}
\]
Each function is independent of its own dimension bit. Every \(z_\ell\) is invariant under complementing all bits; the partner bit in each expression toggles under complementation. Hence the coloring is antipodally odd. If \(k\ge3\), the products \(F_j\) have Boolean degree \(k-1\ge2\), so every direction rule is nonlinear. The partner-bit derivative is one, and changing either bit in any other pair changes \(F_j\) whenever all the remaining \(z_\ell\) equal one. Thus every off-diagonal derivative is nonzero.

*Red component classification.* Regard each two-bit pair as one of four states \(A=00\), \(B=11\), \(U=01\), \(V=10\); call \(U,V\) odd. Since \(F_j=1\) precisely when all other pairs are odd, the red edges in pair \(j\), with all other pairs fixed, are precisely
\[
\begin{array}{c|c}
 F_j=0&A\leftrightarrow U,\quad A\leftrightarrow V\\
 F_j=1&B\leftrightarrow U,\quad B\leftrightarrow V.
\end{array}
\tag{SR2}
\]
There are three types of red components:

- \(C_-\): configurations containing no \(B\) and at least one \(A\). A final remaining \(A\) cannot change, since then \(F_j=1\); no \(B\) can be created while an \(A\) remains. Using one \(A\) as an anchor, any other pair can be changed among \(A,U,V\), and the anchor can be moved. Thus \(C_-\) is connected.
- \(C_+\): configurations with all pairs odd, together with configurations containing precisely one \(B\), with any number of \(A\)'s. From a state with a single \(B\), change every \(A\) to an odd pair using \(F_j=0\); then change the last \(B\) to odd using \(F_j=1\). Every all-odd configuration is connected to every other by the two-edge red move \(U\to B\to V\) (or its reverse), using one pair at a time. Every such configuration is therefore in one component, and transitions (SR2) preserve the displayed set.
- For every fixed \(J\subseteq[k]\) with \(|J|\ge2\), \(C_J\): the configurations whose set of \(B\)-pairs is precisely \(J\). Each \(B\) is frozen, as another \(B\) makes \(F_j=0\). Every remaining pair can move among \(A,U,V\) using \(F_j=0\), so \(C_J\) is a connected component.

These sets partition the entire cube, and (SR2) shows no red edge joins distinct listed sets. There are \(1+1+(2^k-k-1)=2^k-k+1\) components.

*Antipodal roots.* Vertex antipodality interchanges \(A\) and \(B\), and interchanges \(U\) and \(V\). No vertex of \(C_-\) has its antipode in \(C_-\). In \(C_J\), \(|J|\ge2\), the fixed \(B\)-indices of any vertex and of its antipode are disjoint, so its antipode belongs to another red component. For \(x\in C_+\), the antipode also belongs to \(C_+\) precisely when either all pairs are odd or there is one \(A\) and one \(B\). This proves the asserted root set for red connectivity. In every legal coloring, antipodal reflection followed by path reversal interchanges red and blue paths with the same antipodal endpoints, so the blue and red antipodal root sets coincide.

*Full-geodesic witnesses.* If all pairs are odd, in each pair take the red two-edge path through \(B\), interchanging \(U\) and \(V\); the other pairs stay odd. Concatenation traverses every dimension once and joins the root to its antipode. If \(i\) is the unique \(A\)-pair and \(j\ne i\) the unique \(B\)-pair, first change \(A_i\) to odd (\(F_i=0\) because of \(B_j\)), then change \(B_j\) to odd (\(F_j=1\)). Now all pairs are odd. Traverse each other odd pair through \(B\) as above, reversing it in two red steps. Next change the odd pair \(i\) to \(B_i\) (\(F_i=1\)), then the odd pair \(j\) to \(A_j\) (\(F_j=0\) because of \(B_i\)). Every dimension has been traversed once, every step was red, and each pair has become its antipode. Antipodal reflection and reversal supply a blue full geodesic from the same root.

There are \(2^k\) all-odd roots, and \(k(k-1)2^{k-2}\) roots having one \(A\), one \(B\) and otherwise odd pairs, giving the count.

*Interpretation.* This family is maximally interacting and nonlinear. Its favorable-root density is exponentially small even for antipodal paths allowed to repeat dimensions. Consequently root-density or local-influence expansion arguments require assumptions stronger than directed strong connectivity and nonlinearity. The theorem supplies an all-dimensional obstruction to such proposed closure mechanisms; it does not refute unrestricted NORI1.


**Corollary (perfectly balanced, nonlinear, connected colorings with exponentially sparse antipodal roots).** Let \(c^{(k)}\) be the \(2k\)-dimensional family defined by (SR1), for \(k\ge3\). Form the complementary paired lift \(B(c^{(k)})\) on \(Q_{4k}\) with edge rules
\[
B_i(x,y)=c^{(k)}_i(x),\qquad
B_{2k+i}(x,y)=1\oplus c^{(k)}_i(x)\quad(1\le i\le2k).
\]
Then this coloring is legal and has precisely \(2k\) incident edges of each color at every vertex. All \(4k\) direction functions are nonlinear, and its undirected direction-interaction graph is connected. Its root set supporting a monochromatic antipodal path of either color, with arbitrary permitted path length, is
\[
\boxed{S(B(c^{(k)}))=S(c^{(k)})\times Q_{2k}.}
\]
Every favorable root supports a monochromatic full antipodal geodesic of both colors. Its favorable-root density is
\[
\boxed{\left(1+\frac{k(k-1)}4\right)2^{-k}
=\exp(-\Omega(4k)).}
\]

*Proof.* Each paired original/dummy direction gives one edge of each color at each vertex, and antipodal oddness follows from that of \(c^{(k)}\). Every rule is a copy or complement of a nonlinear rule. All original directions interact pairwise by the preceding theorem; each dummy direction depends nontrivially on every original direction other than its matched one, so the undirected interaction graph is connected. An antipodal monochromatic path in the lift projects to one in \(c^{(k)}\). Conversely, for any monochromatic antipodal path in \(c^{(k)}\), each dummy direction can be traversed once at the beginning or end, choosing the endpoint with the requested color, as its paired dummy rule has complementary values at the antipodal endpoints of the original path. This proves the displayed root-set identity. For roots with a full original geodesic, the same insertion produces a full geodesic in the doubled cube. Divide the favorable-root count in the preceding theorem by the number of original roots; doubling multiplies both numerator and denominator by \(2^{2k}\). \(\square\)

This supplies exponential sparsity even under vertex balance, pairwise complementary directions, nonlinear rules in every direction, and undirected interaction connectedness simultaneously. The directed feedback core need not contain the dummy directions, which are sinks; thus the conclusion makes no assertion of strong connectivity for the directed influence graph.


### Orbit-disjoint geodesic packing and edge-critical boundary reduction

An antipodal edge orbit is a pair \(\{e,\bar e\}\) of undirected edges. A legal edge-pair flip reverses both colors in one orbit. Call a successful legal coloring *edge-critical* if some such single flip produces a coloring with no monochromatic full antipodal geodesic. Two full geodesics are *orbit-disjoint* when no edge of one is equal or antipodal to an edge of the other. Paths of a common color that are orbit-disjoint form independently persistent certificates under edge-pair flips.

**Theorem (orbit-disjoint product block paths).** Suppose \(c^{(1)},\ldots,c^{(r)}\), \(r\ge2\), are legal successful colorings of cubes \(Q_{n_j}\), \(n_j\ge2\). Their independent Cartesian product has \(r\) pairwise orbit-disjoint monochromatic full antipodal geodesics, all starting at one root and all ending at its antipode.

*Proof.* Antipodal translation allows the choice of one red full geodesic \(P_j\) from \(a_j\) to \(\bar a_j\) in each factor. Concatenate these blocks in the \(r\) cyclic orders of the factors. The resulting red geodesics share root \(a=(a_1,\ldots,a_r)\). In any fixed factor \(j\), the set of other factor blocks already completed when block \(j\) is traversed is distinct among the cyclic orders; hence each edge of \(P_j\) is traversed at a different tuple of spectator endpoints. Two such product edges could be antipodal only if their factor-\(j\) edges were antipodal, but both have the same factor edge of \(P_j\), which is different from its antipodal edge since \(n_j\ge2\). Different factor directions cannot share an edge orbit. Therefore the \(r\) geodesics are pairwise orbit-disjoint. \(\square\)

**Theorem (spectator parity-code packing).** Suppose a legal successful coloring \(c\) of \(Q_m\), \(m\ge2\), is extended by \(k\ge1\) spectator directions whose rules are odd under antipodal reflection of the original bits, and are independent of all spectator bits. The extension contains \(2^{k-1}\) pairwise orbit-disjoint monochromatic full antipodal geodesics of one color.

*Proof.* Take a red original geodesic \(P\) from \(x\) to \(\bar x\), and denote the \(k\) spectator rules by \(g_j(x)\). For every starting spectator vector \(y\) of even Hamming parity, traverse each direction \(j\) with \(g_j(x)=0\) before \(P\), followed by \(P\), followed by each remaining spectator direction at \(\bar x\). These are red full antipodal geodesics. Different even-parity vectors differ in at least two spectator bits. Their original-direction edges belong to distinct antipodal edge orbits because they use the same original edge in different spectator layers and an original edge is different from its antipodal mate. For each fixed spectator direction \(j\), the paths differ in a spectator bit other than \(j\), so those edges also belong to different edge orbits. \(\square\)

**Corollary (necessary structure of first-failure colorings).** If unrestricted NORI1 fails in dimension \(n\ge4\), then there exists a successful edge-critical coloring \(c\) in that dimension. Every such edge-critical coloring has connected undirected direction-interaction graph and has at most one direction of outdegree zero in its directed influence graph.

*Proof.* The space of legal colorings is a Boolean cube whose variables are antipodal edge orbits. Connect any known successful coloring to a counterexample by a sequence of single-orbit flips. The first step leaving the successful set has a successful edge-critical predecessor. If that predecessor had disconnected undirected interaction graph, it would factor into at least two independent legal colorings, each successful because any monochromatic full product geodesic projects to full monochromatic geodesics in the factors. The product theorem would supply two orbit-disjoint geodesics, at least one surviving any single-orbit flip. Similarly, if it had two sink directions, deleting them simultaneously expresses it as a two-spectator extension of a legal lower-dimensional coloring. Projecting a successful full geodesic shows that the retained base is successful; the spectator packing theorem with \(k=2\) again supplies two orbit-disjoint geodesics. Both conclusions contradict edge-criticality. \(\square\)

In particular, a proposed dimension-uniform theorem saying that every successful legal coloring with connected interaction graph and at most one sink can avoid each prescribed antipodal edge orbit would imply unrestricted NORI1 by the first-failure argument. The necessary structure above is unconditional; it applies to a hypothetical failure with arbitrarily many nonlinear direction rules.


## Quantitative facet gates and path-count extremization

Let \(a\) be an arbitrary binary edge coloring of \(Q_m\), \(m\ge1\). Write \(h_a(z)\) for the number of full geodesics rooted at \(z\) whose color word is \(0^p1^{m-p}\) for some \(0\le p\le m\), counting path orders separately. For an odd Boolean function \(g\), satisfying \(g(\bar z)=1-g(z)\), construct the legal coloring of \(Q_{m+1}\)
\[
C_i(x,0)=a_i(x),\qquad C_i(x,1)=1-a_i(\bar x)\ (i<m),\qquad C_m(x,t)=g(x).
\tag{FG1}
\]
Let \(N_R(C_g)\) count its rooted red full antipodal geodesics.

**Theorem (optimal gate).**
\[
\boxed{N_R(C_g)=2\sum_{z:g(z)=0}h_a(z).}\tag{FG2}
\]
Consequently, over all odd gates,
\[
\boxed{\min_gN_R(C_g)=2\sum_{\{z,\bar z\}}\min(h_a(z),h_a(\bar z)),}\tag{FG3}
\]
\[
\boxed{\max_gN_R(C_g)=2\sum_{\{z,\bar z\}}\max(h_a(z),h_a(\bar z)),}\tag{FG4}
\]
and \(N_R(C_g)+N_R(C_{1-g})=2\sum_z h_a(z)\). Both extrema are attained by selecting, independently in each antipodal pair, the endpoint with the smaller or larger path count as the red vertex of the new-direction edge.

*Proof.* A red full geodesic starting in the lower facet crosses the new direction at \((z,0)\to(z,1)\), so \(g(z)=0\). Before crossing, its base projection is a red path from some \(x\) to \(z\) using dimensions \(S\); afterward, its upper-facet portion is red from \(z\) to \(\bar x\) using \([m]\setminus S\). Complementing and reversing the upper portion gives a blue path under \(a\) from \(x\) to \(\bar z\). Reversing the red prefix and following the resulting blue path produces a full \(0^*1^*\) geodesic from \(z\) to \(\bar z\). Conversely, cutting such a geodesic at the switch recovers both portions. A red full geodesic starting in the upper facet gives a second copy through the same \(z\). This proves (FG2). The condition \(g(\bar z)=1-g(z)\) permits one eligible vertex per antipodal pair, independently of all other pairs. Minimizing or maximizing the indicated contributions proves (FG3)--(FG4) and the complementary-gate identity. \(\square\)

**Subset-count algorithm.** For \(S\subseteq[m]\), let \(R_x(S)\), respectively \(B_x(S)\), count the red, respectively blue, geodesics from \(x\) to \(x\oplus\mathbf1_S\) that use all dimensions of \(S\). They satisfy the recurrence
\[
R_x(S)=\sum_{i\in S}[a_i(x\oplus\mathbf1_{S\setminus\{i\}})=0]R_x(S\setminus\{i\}),
\quad R_x(\varnothing)=1,
\]
with blue recurrence obtained by replacing color zero by one. Then
\[
\boxed{h_a(z)=\sum_{S\subseteq[m]}R_{z\oplus\mathbf1_S}(S)
 B_{z\oplus\mathbf1_S}([m]\setminus S).}\tag{FG5}
\]
Computing both recurrences for all base roots uses \(O(m4^m)\) arithmetic operations. The optimal gate is then obtained from the \(2^{m-1}\) antipodal pairs, without enumerating the \(2^{2^{m-1}}\) admissible gates.

**Sharp insertion bounds.** When \(a\) is itself antipodally odd, both horizontal facets in (FG1) equal \(a\). Each red full base geodesic permits insertion of the new red step at between one and \(m\) of its \(m+1\) vertices: its antipodal endpoints have opposite gate colors. Accounting for the two initial facet choices yields
\[
\boxed{2N_R(a)\le N_R(C_g)\le2mN_R(a).}\tag{FG6}
\]
Both bounds occur in every \(m\ge2\) with the same legal base coloring
\[
a_0(x)=x_1,\qquad a_i(x)=x_0\quad(1\le i<m).
\]
A red full base geodesic traverses dimension zero first from \(x_0=1,x_1=0\), or last from \(x_0=0,x_1=1\), and traverses the other dimensions in any order. Thus \(N_R(a)=2^{m-1}(m-1)!\). Every internal vertex on these red paths has \(x_0=0\). The odd gate \(g(x)=1-x_0\), red only at \(x_0=1\), admits one insertion per path and attains the lower bound. The odd gate \(g(x)=x_0\), red only at \(x_0=0\), admits \(m\) insertions per path and attains the upper bound. \(\square\)

The known qualitative facet bridge states that every odd gate has positive \(N_R(C_g)\) if and only if some antipodal pair satisfies \(h_a(z)h_a(\bar z)>0\). Equations (FG2)--(FG6) refine this bridge by determining the minimum and maximum counts and the corresponding optimal gates.


**Corollary (factorized gate-count distribution).** Under the hypotheses and notation of (FG1)--(FG4), the full counting polynomial over admissible odd gate functions factors as
\[
\boxed{\sum_{\substack{g:Q_m\to\mathbb F_2\\g(\bar z)=1-g(z)}}t^{N_R(C_g)/2}
=\prod_{\{z,\bar z\}}\bigl(t^{h_a(z)}+t^{h_a(\bar z)}\bigr).}\tag{FG7}
\]
Consequently, for a uniformly random odd gate,
\[
\boxed{\mathbb E_gN_R(C_g)=\sum_z h_a(z),\qquad
\operatorname{Var}_gN_R(C_g)
=\sum_{\{z,\bar z\}}\bigl(h_a(z)-h_a(\bar z)\bigr)^2.}\tag{FG8}
\]
The number of odd gates producing zero red full geodesics equals
\[
\boxed{\prod_{\{z,\bar z\}}\left([h_a(z)=0]+[h_a(\bar z)=0]\right).}\tag{FG9}
\]
In particular that product is positive precisely when the paired-root set \(P(a)\) is empty.

*Proof.* The contribution of each antipodal pair to \(N_R(C_g)/2\) in (FG2) is one of the two integers \(h_a(z),h_a(\bar z)\), chosen independently of the contributions from every other pair. Multiplying the two-term generating factors gives (FG7). Each choice has probability one-half, so linearity of expectation and independence give (FG8); the variance of twice a fair choice between \(u\) and \(v\) equals \((u-v)^2\). The constant term of (FG7) counts gates for which every chosen contribution vanishes, giving (FG9). \(\square\)

Equivalently, with one independent sign \(\varepsilon_{\{z,\bar z\}}\in\{-1,1\}\) for each antipodal pair, \(N_R(C_g)\) is the Rademacher sum \(\sum_z h_a(z)+\sum_{\{z,\bar z\}}\varepsilon_{\{z,\bar z\}}(h_a(z)-h_a(\bar z))\). This is an identity of the complete distribution over all legal extensions of a fixed lower-facet coloring.


## Middle-level favorable-root geometry and antipodal index

## Middle-level roots and topology of antipodal favorable sets

Let \(a_i(x)=\bigoplus_{j\ne i}x_j\) define an undirected-edge coloring of \(Q_m\). Each rule ignores its own direction bit and depends on every other direction; the undirected interaction graph is complete. Let \(A(a)\) be the set of starting vertices of full antipodal geodesics with nondecreasing color word \(0^K1^{m-K}\), and \(P(a)=A(a)\cap\overline{A(a)}\).

**Theorem 1 (middle-level root characterization).** For \(m=2h+1\),
\[
A(a)=P(a)=\{x:|x|=h\text{ or }h+1\}.
\tag{ML1}
\]
For \(m=2h\),
\[
A(a)=\begin{cases}
\{x:|x|=h\text{ or }h+1\}&h\text{ even},\\
\{x:|x|=h-1\text{ or }h\}&h\text{ odd},
\end{cases}
\qquad P(a)=\{x:|x|=h\}.
\tag{ML2}
\]
Every admitted root has a witness whose direction order is obtained by arranging its starting vertex bits into a specified alternating pattern.

*Proof.* Let \(p=|x|\bmod2\), and let \(\pi\) be a full direction order. Immediately before step \(k\), the total parity has changed by \(k-1\bmod2\), while the \(\pi_k\)-th starting bit is unchanged. Thus its edge color is \(w_k=p\oplus(k-1\bmod2)\oplus x_{\pi_k}\). The required profile \(w_k=[k>K]\) forces
\[
x_{\pi_k}=p\oplus(k-1\bmod2)\oplus[k>K].
\tag{ML3}
\]
The word \(((k-1\bmod2)\oplus[k>K])_{k=1}^m\) contains \(h+1\) ones for even \(K\), or \(h\) for odd \(K\), when \(m=2h+1\); when \(m=2h\) the respective counts are \(h\) and \(h-1\). For even \(p\) the forced starting word has this weight, while for odd \(p\) its weight is the complement. Requiring \(|x|\equiv p\pmod2\) gives the displayed layers. Conversely, for every weight in the displayed list, choose a permitted cut \(K\) and rearrange the starting bits to satisfy (ML3). In odd dimension, antipodal translation leaves every \(a_i\) unchanged; hence \(A(a)=\overline{A(a)}\). In even dimension, intersecting the two adjacent levels with their antipodal images leaves the central level. \(\square\)

Given any vertex subset \(V\subseteq Q_m\), let \(\mathcal K(V)\) be the cubical complex consisting of all faces of \(Q_m\) whose vertices belong to \(V\).

**Theorem 2 (complete interaction with cohomological index one).** For every odd \(m=2h+1\ge3\), \(\mathcal K(P(a))\) is the connected middle-level graph between the weights \(h\) and \(h+1\). Its vertex number, edge number, and integral first Betti number are
\[
|V|=2\binom{2h+1}{h},\qquad |E|=(h+1)\binom{2h+1}{h},\qquad
b_1=(h-1)\binom{2h+1}{h}+1.
\tag{ML4}
\]
Antipodal complementation acts freely on the realization. Its double-cover characteristic class \(\omega\in H^1(\mathcal K(P(a))/\tau;\mathbb F_2)\) satisfies
\[
\omega\ne0,\qquad \omega^2=0.
\tag{ML5}
\]
In particular the cohomological index stays one, although the cube dimension grows without bound and the direction-interaction graph is complete.

*Proof.* No two-dimensional cube face lies in just two consecutive Hamming-weight levels, so the induced cubical complex is one-dimensional. Each weight-\(h\) vertex has \(h+1\) neighbors of weight \(h+1\), giving the edge count. Two weight-\(h\) subsets differing by one exchange connect through their union; the Johnson exchange graph is connected, hence so is the middle-level graph. Its first Betti number is \(|E|-|V|+1\). For \(m\ge3\), antipodality neither fixes a vertex nor exchanges the endpoints of any graph edge, so its action on the realization is free. The covering is nontrivial because the covering graph is connected. Its quotient is again a graph and has vanishing second cohomology. Therefore its nonzero covering class squares to zero. \(\square\)

**Theorem 3 (arbitrarily high-dimensional torus root complexes).** Let \(b_r\) on \(Q_{3r}\) be the Cartesian product of \(r\) copies of the three-dimensional coloring from Theorem 1. Then
\[
\mathcal K(P(b_r))\cong(S^1)^r,\qquad
H_j(\mathcal K(P(b_r));\mathbb Z)\cong\mathbb Z^{\binom rj}\quad(0\le j\le r).
\tag{ML6}
\]
Antipodality acts as a half-turn in each circle factor; its quotient is a torus, and its associated double-cover class has cohomological index one.

*Proof.* The three-dimensional favorable and paired-root set is \(Q_3\setminus\{000,111\}\), whose induced graph is a six-cycle. The existing Cartesian favorable-root and paired-root factorization shows that the product coloring's paired-root set is the Cartesian product of these six-vertex sets. Faces supported on a vertex Cartesian product are products of supported factor faces, giving the cubical product of \(r\) circles. The homology is obtained by the Kunneth formula. Complementing the three bits moves each six-cycle vertex to the opposite vertex, inducing simultaneous half-turns on the torus. Its quotient is a torus, modeled as \(\mathbb R^r/(\mathbb Z^r+\mathbb Z(\frac12,\ldots,\frac12))\). Its nontrivial degree-one covering class squares to zero in the cohomology ring of a torus. \(\square\)

The theorems provide a constructive family of geodesic witnesses through (ML3). They also show that complete direction interaction and the paired-root property do not force favorable-root complexes to be contractible or to have cohomological index growing with ambient dimension. The results do not prove unrestricted paired-root existence.
