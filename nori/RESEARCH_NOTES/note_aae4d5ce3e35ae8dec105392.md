# Prescribed cyclic color words with flat square-exchange neighborhoods

- Stable ID: note_aae4d5ce3e35ae8dec105392
- Author: session_nori_r7948_2
- Primary home: section:nori_type_a_rook_gallery_topology
- Labels: twisted-switch, coxeter-exchange, local-obstruction, geodesic
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7948_2
- Updated session: session_nori_r7948_2
- Disposition: none
- Successor: none

## Related references

- article:nori_article_xiv_type_a_rook_gallery_topology
- note:note_4faa19538adf3c3d215f274d

## Research note

Let \(n\ge4\). A complete cube geodesic \(g=(x;d_1,\dots,d_n)\) has a color word \(w(g)\in\{0,1\}^n\). The **root slide** \(T\) moves the first direction to the end while advancing the root along that edge; under an antipodally odd coloring its color word becomes \((w_2,\dots,w_n,1-w_1)\). Define the twisted cyclic switch count \(\sigma=\sum_{j<n}[w_j\ne w_{j+1}]+[w_n=w_1]\) and \(h=(\sigma-1)/2\).

**Theorem (prescribed full-word flatness around a cyclic gallery).** For every \(w\in\{0,1\}^n\) there exists an antipodally odd binary edge coloring \(c\) of \(Q_n\) and a complete geodesic \(g=(0;1,\dots,n)\) with word \(w\) such that, for every \(0\le t<2n\), every geodesic obtained from \(T^tg\) by a single adjacent dimension exchange has *the same full color word* as \(T^tg\). In particular every flag of this cyclic gallery has a neighborhood of constant \(h\). Taking \(w=0^{n-2}10\) yields a positive flat local minimum \(h=1\); an alternating \(w\) yields \(h=\lfloor(n-1)/2\rfloor\).

*Proof.* Form the \(2n\)-cycle with vertices
\[
v_0=0,\quad v_k=e_1+\cdots+e_k\ (1\le k\le n),\quad
v_{n+k}=\bar v_k\ (0\le k\le n),
\]
where additions are in \(\mathbb F_2^n\). Let \(E_k=\{v_{k-1},v_k\}\), cyclically indexed modulo \(2n\). We have \(E_{k+n}=\bar E_k\). For each \(1\le k\le n\), let \(F_k,G_k\) be the two edges, in traversal order, on the alternative route across the square through the consecutive cycle edges \(E_k,E_{k+1}\). The three sets of edges \(E_1,\dots,E_n\), \(F_1,\dots,F_n\), and \(G_1,\dots,G_n\) occupy \(3n\) distinct antipodal edge orbits.

Indeed, identify each direction-\(i\) undirected cube edge with its \(n-1\) fixed bits, whose complement represents its antipodal edge. The three edges in direction \(i\) are \(E_i,F_{i-1},G_i\), indices cyclic modulo \(n\). For \(2\le i<n\), the fixed-bit strings are:
\[
\begin{array}{c|c}
E_i&1\ (j<i),\ 0\ (j>i)\\
F_{i-1}&1\ (j<i-1),\ 0\ (j\ge i-1,\ j\ne i)\\
G_i&1\ (j<i\ \text{or}\ j=i+1),\ 0\ \text{otherwise}.
\end{array}
\]
These are distinct, and agree at every fixed position outside \(\{i-1,i+1\}\); such a position exists since \(n\ge4\), so none are complementary. For \(i=1\), the three strings, respectively, have all bits zero; bits \(2,\dots,n-1\) equal to one with bit \(n=0\); and bit \(2=1\) with every other fixed bit zero. They are distinct and share bit \(n=0\). For \(i=n\), the strings have all fixed bits one; all except \(n-1\) equal to one; and all except \(1\) equal to one. They are distinct and share bit \(2=1\). Thus no two edges in the same direction represent the same antipodal orbit, while different directions have disjoint orbits.

Prescribe \(c(E_k)=w_k\) for \(1\le k\le n\), and use oddness to prescribe \(c(E_{k+n})=1-w_k\). For each \(1\le k\le n\) prescribe \(c(F_k)=c(E_k)\) and \(c(G_k)=c(E_{k+1})\), with \(E_{n+1}\) carrying color \(1-w_1\). The orbit-disjointness just proved makes all these prescriptions compatible. By antipodality the same route-color identities hold for the squares \(k+n\). Color all remaining antipodal edge pairs arbitrarily and oppositely.

The path \(T^tg\) follows \(n\) consecutive edges of the \(2n\)-cycle. An adjacent dimension exchange replaces one consecutive two-edge segment \((E_k,E_{k+1})\) by its alternative square route \((F_k,G_k)\), preserving the vertex after these two steps and every subsequent edge. Both ordered pairs have identical color bits, so the entire word remains unchanged. For the displayed words the stated values of \(h\) follow by direct comparison. \(\square\)

**Scope.** This defeats every proof rule claiming a strictly improving *single* adjacent dimension exchange from each positive-\(h\) cyclic root-slide class, even when the complete ordered color word is used. It also strengthens the even-dimensional parity-coloring plateau example already recorded in the unification research notes: the present construction works in every \(n\ge4\), prescribes every cyclic word, and freezes the entire word rather than only its twisted variation. It leaves open global equivariant cancellation, nonlocal exchange sequences, and root-changing type-B chamber moves.

**Corollary (independence of cyclic exchange data).** In the construction, write \(u_k=c(F_k)\), \(v_k=c(G_k)\) for \(1\le k\le n\). The restriction map from antipodally odd colorings of \(Q_n\) to
\[
(c(E_1),\ldots,c(E_n),u_1,v_1,\ldots,u_n,v_n)\in\mathbb F_2^{3n}
\]
is surjective. Each fiber has size \(2^{n2^{n-2}-3n}\). Consequently, conditional on an arbitrary prescribed cyclic geodesic word \(w\), all alternative two-edge route words at its \(n\) antipodal square pairs can be prescribed independently. The \(n\) square curvatures \(\kappa_k=c(E_k)+c(E_{k+1})+u_k+v_k\), with \(c(E_{n+1})=1-w_1\), can likewise be prescribed independently.

*Proof.* An \(n\)-cube has \(n2^{n-1}\) edges, partitioned into \(n2^{n-2}\) antipodal pairs. By the orbit-disjointness proved above, the displayed \(3n\) observations select one edge from each of \(3n\) distinct antipodal pairs, and hence are independent binary choices on the affine space of antipodally odd colorings. All remaining antipodal pairs may be colored freely, giving the fiber count. Given \(w\), independently choosing \(u_k,v_k\) realizes any prescribed square curvature by solving its displayed linear equation. \(\square\)

Thus a prescribed complete root-slide orbit imposes no compatibility equations among the color words of its one-exchange neighbors, apart from antipodal pairing.

**Proposition (global integrability of the twisted quadratic defect).** On the graph of complete geodesics modulo cyclic root slides, assign to each adjacent-exchange edge \(gg'\) the coefficient \(q(gg')\in\mathbb F_2\) of \(u^2\) in
\[
(1+u)^{\sigma(g)}+(1+u)^{\sigma(g')}.
\]
Then
\[
\boxed{q(gg')=h(g)+h(g')\pmod2.}
\]
In particular \(q=d(h\bmod2)\) is an ordinary graph coboundary, so its sum over every closed exchange walk is zero, including walks that traverse distinct root-slide representatives. Hence this scalar quadratic defect, by itself, has trivial class in \(H^1\) of the cyclic gallery quotient. This holds for every antipodally odd coloring in every dimension \(n\ge3\).

*Proof.* Write \(\sigma=2h+1\). Lucas's theorem, or the elementary binomial identity, gives \([u^2](1+u)^{2h+1}=\binom{2h+1}{2}\equiv h\pmod2\). Add the two coefficients. Since \(h(Tg)=h(g)\), the zero-cochain \(h\bmod2\) is defined on root-slide classes and has \(q\) as its coboundary. \(\square\)

The proposition extends the interior fixed-endpoint integrability theorem already in Article XIV to all adjacent exchanges and the cyclic-root quotient. A nontrivial projective obstruction would have to arise from the geometry of the carrier-valued chain assignments or from the failure of the filtered fillings, rather than from this scalar one-cochain.
