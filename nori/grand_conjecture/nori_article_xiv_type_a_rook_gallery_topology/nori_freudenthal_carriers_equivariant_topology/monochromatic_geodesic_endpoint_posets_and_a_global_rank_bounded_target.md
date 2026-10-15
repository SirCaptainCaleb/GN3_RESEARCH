# Monochromatic geodesic endpoint posets and a global rank-bounded target

# Monochromatic geodesic endpoint posets and a global rank-bounded target

The monochromatic prefix complexes depend on a chosen root. The following construction places the geodesic certificates from all roots in one finite poset. Its order retains the condition needed for dimension-simple concatenation, while intervals with fixed endpoints provide nested contractible carriers. Under a hypothetical failure of NORI1, this global complex admits an explicit equivariant map to \(S^{n-3}\).

Let \(c\) be any binary coloring of the undirected edges of \(Q_n\). Fix a color \(a\), and let \(\mathcal P_a(c)\) consist of the ordered pairs \((u,v)\) of distinct cube vertices for which a color-\(a\) geodesic from \(u\) to \(v\) exists. Write \(d\) for Hamming distance. Define
\[
(u,v)\preceq(u',v')
\tag{1}
\]
when color-\(a\) geodesics from \(u'\) to \(u\) and from \(v\) to \(v'\) exist, allowing empty paths, and
\[
d(u',v')=d(u',u)+d(u,v)+d(v,v').
\tag{2}
\]
Thus (2) requires the two extensions and the intervening path to use disjoint dimension sets.

**Theorem 1 (a poset with coherent path certificates).** Relation (1) is a partial order. Its rank function
\[
r(u,v)=d(u,v)
\]
strictly increases under strict comparison. Every chain in \(\mathcal P_a(c)\) is witnessed simultaneously by one color-\(a\) geodesic containing all its ordered endpoint pairs as nested subpaths. Endpoint reversal
\[
J(u,v)=(v,u)
\tag{3}
\]
is an order-preserving involution, free on the order complex.

*Proof.* Reflexivity follows by using empty extensions. If two pairs are comparable and have equal rank, (2) forces both extension lengths to vanish, so the pairs agree. This proves antisymmetry and strict rank increase.

To prove transitivity, suppose
\[
(u,v)\preceq(u',v')\preceq(u'',v'').
\]
Choose monochromatic witnesses for the four extensions and for \(u\to v\). Their concatenation is
\[
u''\to u'\to u\to v\to v'\to v''.
\]
The two distance equalities show that its length is \(d(u'',v'')\). Hence it is a cube geodesic: every dimension used in any constituent is used once in the entire path. In particular its initial portion \(u''\to u\) and terminal portion \(v\to v''\) are monochromatic geodesics, proving the required comparison. Repeating this argument proves the simultaneous witness assertion for an arbitrary chain.

Undirected path reversal preserves monochromaticity and reverses the distance decomposition, giving (3). The involution fixes no ordered pair. It also fixes no simplex setwise: the vertices of a chain have distinct ranks, and an invariant chain would have to fix its unique vertex at each represented rank. \(\square\)

**Theorem 2 (nested contractible carriers for fixed endpoints).** For each \(p=(u,v)\in\mathcal P_a(c)\), the order complex of the principal ideal
\[
\mathcal P_{\le p}=\{q:q\preceq p\}
\tag{4}
\]
is a simplicial cone with apex \(p\). If \(p\preceq p'\), these carriers are nested. Every monochromatic geodesic with endpoints \(u,v\), together with all its oriented nonempty subpaths, is represented in the same carrier (4).

*Proof.* The ideal has maximum element \(p\), so adjoining \(p\) to any chain gives another chain. This proves the cone assertion. Ideal inclusion gives nesting. A subpath of a monochromatic geodesic satisfies (2), and the portions before and after it supply the required monochromatic extensions. \(\square\)

For example, when both routes across a square are monochromatic of the same color, their orders define one endpoint pair and lie in its common contractible carrier. Identifying these orders preserves a shortest-path witness with its dimension support. It requires no transitivity of unrestricted unrooted reachability: transitivity in Theorem 1 uses (2) at every composition. When one route changes color, that route supplies no monochromatic certificate to this carrier.

**Theorem 3 (global equivariant dimension bound).** Let \(n\ge3\), and suppose
\[
c(\bar e)=1-c(e).
\]
If \(c\) has no monochromatic full antipodal geodesic, then, for either color \(a\),
\[
\boxed{\dim\Delta\mathcal P_a(c)\le n-3.}
\tag{5}
\]
There is an explicit \(J\)-equivariant simplicial map
\[
\boxed{\Delta\mathcal P_a(c)\longrightarrow
\partial\operatorname{Crosspolytope}_{n-2}\cong S^{n-3}.}
\tag{6}
\]
The assertions include an empty order complex.

*Proof.* A monochromatic geodesic of length \(n-1\) leaves one dimension \(i\) unused. Its endpoints \(u,v\) differ in every other dimension. The two dimension-\(i\) edges incident with \(u,v\) are antipodal, so one has the path's color. Prepending or appending that edge gives a monochromatic full geodesic. Thus the hypothesis excludes every monochromatic geodesic of length \(n-1\), as well as length \(n\). Every pair in \(\mathcal P_a(c)\) has rank between \(1\) and \(n-2\). Strict rank increase bounds the number of vertices in a chain by \(n-2\), proving (5).

Fix an ordering of the cube dimensions. For a pair \(p=(u,v)\), let \(i(p)\) be the first dimension in which \(u,v\) differ, and define
\[
\lambda(p)=(-1)^{u_{i(p)}}e_{r(p)}
\in\{\pm e_1,\ldots,\pm e_{n-2}\}.
\tag{7}
\]
Swapping endpoints negates the label. In a chain all ranks differ, so its labels use distinct axes and span a face of the crosspolytope boundary. Formula (7) therefore defines the simplicial map (6). \(\square\)

The involution in (6) is reversal of ordered monochromatic endpoints. Geometric cube antipodality has the additional color-complementing action
\[
A:\mathcal P_a(c)\longrightarrow\mathcal P_{1-a}(c),
\qquad A(u,v)=(\bar u,\bar v).
\tag{8}
\]
It preserves the order and commutes with \(J\). A source-to-target construction must track both operations.

**Theorem 4 (root transport has one global endpoint certificate).** Let \(xy\) be a color-\(a\) edge in dimension \(i\). Suppose there are color-\(a\) geodesics from \(x\) with support \(S\), and from \(y\) with support \(T\), where
\[
i\notin S\cup T,\qquad S\cap T=\varnothing.
\tag{9}
\]
Then
\[
\boxed{(x\oplus\mathbf1_S,\ y\oplus\mathbf1_T)
\in\mathcal P_a(c)}
\tag{10}
\]
has rank \(|S|+|T|+1\). The certificate is unchanged when the joining edge is included in the first arm or in the second.

*Proof.* Reverse the first arm, traverse \(x\to y\), and traverse the second arm. Conditions (9) make the three dimension sets disjoint, so the result is a monochromatic geodesic between the endpoints in (10). Splitting it at \(x\) or at \(y\) changes only which arm contains dimension \(i\); its ordered endpoints and support remain fixed. \(\square\)

This realizes the support-preserving transport between neighboring prefix constructions within a single global poset. Longer transports remain governed by (2), which requires each concatenation to be a geodesic.

**Proposition 5 (the endpoint involution has nontrivial local topology).** If some vertex has three incident color-\(a\) edges in distinct dimensions, \(\Delta\mathcal P_a(c)\) contains a \(J\)-invariant circle on which \(J\) acts antipodally.

*Proof.* Let the center be \(x\) and the three neighbors be \(u_1,u_2,u_3\). Include the six oriented edge pairs \((u_i,x),(x,u_i)\) of rank one and the six pairs \((u_i,u_j)\), \(i\ne j\), of rank two. The latter are monochromatic geodesics through \(x\). Each rank-two pair is above its two directed edge pairs. The resulting incidence subcomplex is a twelve-cycle. Endpoint reversal sends each vertex to the vertex six steps away. Thus it is an antipodal circle. \(\square\)

**Remaining proof obligation.** Theorems 1–4 supply one global target, a dimension bound, and nested contractible carriers derived solely from the original monochromatic geodesics. They provide an alternative to separately choosing sphere models for root-dependent prefix complements. A proof of NORI1 still requires an equivariant augmentation-preserving chain assignment from the cube's antipodal carrier into this target, using the color-selective edge transports and compatible higher fillings. Such an assignment from \(S^{n-1}\) would contradict (6) by the chain-level Borsuk–Ulam obstruction. The assignment is unproved; the existence of a low-dimensional target alone supplies no contradiction.
