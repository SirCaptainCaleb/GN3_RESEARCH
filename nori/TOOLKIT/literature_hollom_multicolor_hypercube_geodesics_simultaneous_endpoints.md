# Hollom-type hypercube geodesic averaging: multicolor extension and simultaneous endpoints

**Summary:** Every fixed finite family of arbitrary edge colorings of Q_m has a common antipodal geodesic with O(sqrt(m)) switches per coloring (constant depends on number of colorings).

## Statement

For an arbitrary q-coloring of the edges of Q_m, the mean over antipodal roots of the minimum geodesic color-switch count is at most B_m(q) = [m sqrt(q-1)/(2 sqrt(m-1))] sum_{k=1}^{m-1} [k(m-k)]^{-1/2} = (pi sqrt(q-1)/2+o(1)) sqrt(m). In particular, two arbitrary binary edge colorings admit a common spanning antipodal geodesic with at most floor(B_m(4)) switches in each coloring; their low-switch terminal sets intersect. This is the multicolor extension of a binary hypercube averaging method attributed in the source manuscript to Lawrence Hollom.

## Body

Let \(\chi:E(Q_m)\to[q]\) be an arbitrary coloring of the undirected edges of the \(m\)-cube, where \(m\ge2\) and \(q\ge2\). For a geodesic \(P\), write \(\sigma_\chi(P)\) for its number of changes of edge color, and for \(u\in Q_m\) set
\[
D_\chi(u)=\min\{\sigma_\chi(P):P\text{ is a geodesic from }u\text{ to }\bar u\}.
\]

**Theorem (multicolor antipodal-geodesic averaging).** For every such coloring,
\[
\boxed{\frac{1}{2^m}\sum_{u\in Q_m}D_\chi(u)
\le B_m(q):=
\frac{m\sqrt{q-1}}{2\sqrt{m-1}}
\sum_{k=1}^{m-1}\frac{1}{\sqrt{k(m-k)}}.}\tag{1}
\]
Consequently some spanning antipodal geodesic changes color at most \(\lfloor B_m(q)\rfloor\) times, and
\[
B_m(q)=\left(\frac{\pi\sqrt{q-1}}{2}+o(1)\right)\sqrt m
\quad(m\to\infty,\ q\text{ fixed}).\tag{2}
\]
The bound requires no relationship among the colors of antipodal edges.

**Proof.** For \(u,v\in Q_m\) and \(a\in[q]\), let \(F_a(u,v)\) be the minimum of
\[
\sigma_\chi(P)+[\text{the last edge of }P\text{ has color different from }a]\tag{3}
\]
over geodesics \(P\) from \(u\) to \(v\), with \(F_a(u,u)=0\). Thus a change to the prescribed terminal color \(a\) is allowed at \(v\). For every \(u,v,a,b\),
\[
|F_a(u,v)-F_b(u,v)|\le1.\tag{4}
\]
Indeed, the two costs in (3) differ by at most one for each fixed path. At \(v=\bar u\), \(\min_aF_a(u,v)=D_\chi(u)\).

Fix \(u,v\) at Hamming distance \(k\), \(1\le k\le m-1\). Write \(I^u(v)\) and \(J^u(v)\) for the neighbors of \(v\) at distance \(k-1\) and \(k+1\), respectively, from \(u\); their cardinalities are \(k\) and \(m-k\). Let \(I_a\) and \(J_a\) count the edges of color \(a\) among these inward and outward neighbors. Define
\[
\begin{aligned}
f(u,v)&=\sum_{a=1}^q\frac{J_a}{m-k}F_a(u,v),\\
h(u,v)&=\sum_{a=1}^q\frac{I_a}{k}F_a(u,v),\\
g(u,v)&=\frac1k\sum_{w\in I^u(v)}F_{\chi(wv)}(u,w).
\end{aligned}\tag{5}
\]
Appending an edge \(wv\) of color \(a\) to a path realizing \(F_a(u,w)\) shows \(F_a(u,v)\le F_a(u,w)\). Hence \(h(u,v)\le g(u,v)\).

The probability vectors \(p_a=J_a/(m-k)\) and \(r_a=I_a/k\) sum to one. By (4), their averages of the numbers \(F_a(u,v)\) differ by at most their total-variation distance:
\[
f(u,v)-h(u,v)\le \frac12\sum_{a=1}^q|p_a-r_a|=:T(u,v).\tag{6}
\]
Thus \(f(u,v)\le g(u,v)+T(u,v)\).

For \(0\le k\le m-1\), let \(\Phi_k=\mathbb E[f(U,V)\mid d(U,V)=k]\), where \(U,V\) are uniform cube vertices; set \(\Phi_0=0\). If \((U,V)\) is uniform among distance-\(k\) ordered pairs and \(W\) is a uniform inward neighbor of \(V\), then \((U,W)\) is uniform among distance-\((k-1)\) ordered pairs and, conditioned on \(U,W\), the neighbor \(V\) is uniform among outward neighbors of \(W\). It follows from (5) that
\[
\mathbb E[g(U,V)\mid d(U,V)=k]=\Phi_{k-1},\tag{7}
\]
so \(\Phi_k\le\Phi_{k-1}+\mathbb E_kT(U,V)\).

We bound the last expectation. Condition on \(V=v\); the \(k\) inward directions toward uniform \(U\) form a uniform \(k\)-subset of the \(m\) directions incident with \(v\). Suppose \(s_a\) of those \(m\) incident edges have color \(a\), put \(\theta_a=s_a/m\), and let \(X_a=I_a\). The random variable \(X_a\) is hypergeometric with
\[
\mathbb EX_a=k\theta_a,\qquad
\operatorname{Var}(X_a)=\frac{k(m-k)}{m-1}\theta_a(1-\theta_a).\tag{8}
\]
Since \(J_a=s_a-X_a\),
\[
\frac{J_a}{m-k}-\frac{I_a}{k}
=\frac{m(k\theta_a-X_a)}{k(m-k)}.\tag{9}
\]
Jensen's inequality, (8), and Cauchy--Schwarz therefore give
\[
\begin{aligned}
\mathbb E[T(U,V)\mid V=v]
&\le\frac{m}{2\sqrt{(m-1)k(m-k)}}
\sum_{a=1}^q\sqrt{\theta_a(1-\theta_a)}\\
&\le\frac{m\sqrt{q-1}}{2\sqrt{(m-1)k(m-k)}}.
\end{aligned}\tag{10}
\]
For the second inequality use \(\sum_a\theta_a=1\) and \(\sum_a(1-\theta_a)=q-1\). The bound is uniform in \(v\). Summing the recurrence in (7) over \(k=1,\ldots,m-1\) proves \(\Phi_{m-1}\le B_m(q)\).

Finally take \(V=\bar U\), with \(U\) uniform. Every neighbor of \(V\) is inward. From the extension argument and (3),
\[
D_\chi(U)=\min_aF_a(U,\bar U)
\le\frac1m\sum_{w\sim\bar U}F_{\chi(w\bar U)}(U,w)
=g(U,\bar U).\tag{11}
\]
The same incidence counting as (7) gives \(\mathbb E[g(U,\bar U)]=\Phi_{m-1}\). Hence the root average of \(D_\chi\) is at most \(B_m(q)\). Since \(D_\chi(u)\) is integral, some root has \(D_\chi(u)\le\lfloor B_m(q)\rfloor\). The sum in (1) is a Riemann sum converging to \(\int_0^1[t(1-t)]^{-1/2}\,dt=\pi\), giving (2). \(\square\)

**Corollary (unrestricted simultaneous common path).** Let \(d,e:E(Q_m)\to\{0,1\}\) be two arbitrary binary edge colorings, with no relationship between their values. There is one spanning antipodal geodesic \(P\) such that
\[
\boxed{\sigma_d(P)\le\lfloor B_m(4)\rfloor,\qquad
\sigma_e(P)\le\lfloor B_m(4)\rfloor.}\tag{12}
\]
Thus, writing \(E_s(d)\) for the set of terminal vertices of spanning \(d\)-geodesics with at most \(s\) switches,
\[
\boxed{E_{\lfloor B_m(4)\rfloor}(d)\cap
E_{\lfloor B_m(4)\rfloor}(e)\ne\varnothing.}\tag{13}
\]
The common-path assertion extends to any fixed number \(t\) of arbitrary binary colorings by replacing \(4\) with \(2^t\).

*Proof.* Color each edge by the ordered pair \(\chi(f)=(d(f),e(f))\in\{0,1\}^2\). Every switch of either constituent coloring is a switch of \(\chi\), so (12) follows from the theorem with \(q=4\). Reverse the same \(P\) in the two copies of \(Q_m\) to obtain corresponding terminals. For \(t\) colorings take the joint label in \(\{0,1\}^t\). \(\square\)

**Application to parallel codimension-two faces.** Let \(n=m+2\), and let \(c\) be any antipodally odd edge coloring of \(Q_n\). Fix adjacent parallel codimension-two faces \(F,F^a\) with the same \(m\) free directions. Under coordinate identification their restrictions are two arbitrary edge colorings \(d,e\) of \(Q_m\). Applying (12) produces long geodesics in \(F,F^a\) with corresponding terminal vertices and at most \(\lfloor B_m(4)\rfloor\) switches each. Article VIII's parallel-face extension bound gives
\[
\mu(c)\le 2\left\lceil\frac{\lfloor B_m(4)\rfloor}{2}\right\rceil.\tag{14}
\]
The binary version of (1) and its asymptotic leading constant are due to Lawrence Hollom, *Hypercube geodesics with few colour changes* (2026), arXiv:2605.20184. The argument above proves the multicolor extension and its simultaneous-geodesic application.

The unresolved Article X endpoint target is (13) with the constant \(s=2\) for every pair \(d,e\). The estimate (12) supplies simultaneous endpoint alignment at scale \(O(\sqrt m)\), independently of any inherited antipodal condition in the faces; (14) does not improve the known single-color \(O(\sqrt n)\) bound.

## Metadata

- ID: literature_hollom_multicolor_hypercube_geodesics_simultaneous_endpoints
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
