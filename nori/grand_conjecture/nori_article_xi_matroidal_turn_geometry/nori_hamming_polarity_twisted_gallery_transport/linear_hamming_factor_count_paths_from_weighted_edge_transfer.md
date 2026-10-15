# Linear Hamming factor-count paths from weighted edge transfer

Let \(G=H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), with canonical spectral edge-resource matroid
\[
N_{\rm sp}(G)\cong\bigoplus_{j=1}^kM(K_q).
\]
Let \((b,c)\) be an arbitrary triangular-turn system:
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E(G)\}},\qquad b(u,v,w)=c(uv)+c(vw)\quad(uw\notin E(G)),\tag{1}
\]
with binary arithmetic. A path is **accepted** when all turns have label zero and the traversed edge resources are independent in \(N_{\rm sp}(G)\).

**Theorem (uniform linear factor bound).** Every system (1) admits an accepted monochromatic path with
\[
\boxed{\ell\ge\left\lceil\frac{k}{2}\right\rceil.}\tag{2}
\]
In combination with the cycle-dominating resource-matroid terminal theorem, this gives
\[
\boxed{\ell\ge\max\left\{\left\lceil\frac{k}{2}\right\rceil,\left\lceil\frac12\sqrt{k(q-1)}\right\rceil\right\}.}\tag{3}
\]
No antipodal condition, representability assumption beyond the canonical spectral resource, or restriction on triangle-turn orientations is required.

*Proof.* Fix one edge color \(s\). Process factors in the order \(1,\ldots,k\). Define \(L_j(x)\) as the maximum length of a color-\(s\) path ending at \(x\) that uses at most one edge from each factor \(1,\ldots,j\), with factor indices strictly increasing. Put \(L_0(x)=0\). A transition between different factors is nontriangular and has turn label \(s+s=0\); no turn inside a factor occurs. Consequently every such path is accepted. The use of each factor at most once guarantees independence in the direct-sum graphic resource matroid.

For a \(j\)-coordinate fiber, let \(F\) be the subgraph of \(K_q\) consisting of its color-\(s\) edges, and let \(w\) be the weights \(L_{j-1}\) at its \(q\) vertices. The new terminal weights are
\[
T_F(w)(v)=\max\bigl\{w(v),\max_{u:\,uv\in E(F)}(w(u)+1)\bigr\}.\tag{4}
\]
Put \(\delta_v=T_F(w)(v)-w(v)\ge0\). For each edge \(uv\in E(F)\), the inequalities \(T_F(w)(u)\ge w(v)+1\) and \(T_F(w)(v)\ge w(u)+1\) imply
\[
\delta_u+\delta_v\ge2.
\]
Summing over edges, and using \(\deg_F(v)\le q-1\), yields
\[
2|E(F)|\le\sum_v\deg_F(v)\delta_v\le(q-1)\sum_v\delta_v.
\]
Thus
\[
\sum_vT_F(w)(v)\ge\sum_vw(v)+\frac{2|E(F)|}{q-1}.\tag{5}
\]
Sum (5) over all \(j\)-coordinate fibers and then \(j=1,\ldots,k\):
\[
\sum_{x\in V(G)}L_k(x)\ge\frac{2|E_s|}{q-1}.\tag{6}
\]
Since the regular graph \(G\) has \(q^k\) vertices and \(k(q-1)q^k/2\) edges, one color class contains at least \(k(q-1)q^k/4\) edges. For that color, (6) shows some terminal \(x\) satisfies
\[
L_k(x)\ge\frac{2|E_s|}{(q-1)q^k}\ge\frac{k}{2}.
\]
Integrality proves (2); combining with the previously established root-resource square-root bound proves (3). \(\square\)

**Strengthening for nonhomogeneous Hamming products.** The same argument applies to
\[
G=\square_{j=1}^kK_{q_j},\qquad q_j\ge2,
\]
with root resources \(\bigoplus_jM(K_{q_j})\), because each \(j\)-fiber contributes \(2|E_s^{(j)}|/(q_j-1)\). Summing over the two color classes, the total normalized contribution is
\[
\frac1{|V(G)|}\sum_{j=1}^k\frac{2|E(G)^{(j)}|}{q_j-1}
=\sum_{j=1}^k1=k.
\]
Hence some color has a path of length at least \(\lceil k/2\rceil\), for any factor sizes, under the same intrinsic nontriangular potential condition.

**Relation to the central conjecture.** The theorem explains why the factor-count scale \(k\) is available independently of the spectral degree \(k(q-1)\): each Cartesian factor supplies one unit of aggregate weighted terminal growth across both colors. It proves half the proposed spanning factor-count guarantee uniformly, while the ternary turn-conservation theorem improves the coefficient to \(5/6\) for \(q=3\) and isolates its remaining loss to transitive monochromatic coordinate triangles.
