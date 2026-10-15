## Hamming Gallery Polarities and Twisted Transport

### Permutation galleries, unimodular transport, and endpoint degrees

Let \(H(k,q)=K_q^{\square k}\) with \(k\ge1,q\ge2\), and \(N_{\rm sp}\) its canonical spectral-resource matroid on graph edges. Fix a root \(x\), let \(d=k(q-1)\), and put
\[
D_x=\{(i,b): i\in[k],\ b\in[q]\setminus\{x_i\}\},
\qquad |D_x|=d.
\]
Orient a root edge by the direction of traversal. Its spectral difference vector is \(e_b-e_a\) in coordinate summand \(i\) when that coordinate changes from \(a\) to \(b\).

**Theorem 1 (full-rank gallery permutation correspondence).** Every \(N_{\rm sp}\)-independent path of length \(d\) beginning at \(x\) is obtained uniquely from a permutation \(\pi=(t_1,\ldots,t_d)\) of \(D_x\): for \(t_j=(i,b)\), replace the current \(i\)-th coordinate value by \(b\). Every such permutation yields a resource-independent path.

**Proof.** Resource independence means the transitions in each coordinate form a forest in the graphic matroid \(M(K_q)\). Since the coordinate transitions form a trail, they cannot revisit a coordinate symbol. Rank saturation forces \(q-1\) transitions in each coordinate, so the successive visited symbols are a permutation of the \(q-1\) symbols other than \(x_i\). Interleaving the \(k\) coordinate sequences gives a permutation of \(D_x\). Conversely a permutation of \(D_x\) gives a simple coordinate path in each complete-graph factor, hence a forest, and the resource vectors for different factors occupy direct-sum subspaces. The entire set of \(d\) edge vectors is therefore independent. \(\square\)

**Corollary 2 (diametral endpoints and uniform fibers).** Every full-rank path from \(x\) finishes at some \(y\) differing from \(x\) in all \(k\) coordinates. Every such \(y\) occurs, and the number of full-rank paths with prescribed directed endpoints \(x,y\) is
\[
\boxed{\frac{d!}{(q-1)^k}}.
\tag{1}
\]
In particular there are \(d!\) full-rank paths from \(x\), distributed uniformly among the \((q-1)^k\) diametral endpoints.

**Proof.** In each coordinate the prescribed terminal symbol is the last visited among \(q-1\) tokens. Choose the orders of the \(q-2\) remaining tokens in \((q-2)!\) ways, and interleave the \(k\) ordered coordinate sequences in \(d!/((q-1)!)^k\) ways. Their product is (1). \(\square\)

In the cube endpoint \(H(n,2)=Q_n\), this is the familiar \(n!\) antipodal geodesics between fixed endpoints. At \(H(1,n)=K_n\) the count becomes \((n-2)!\) Hamilton paths between prescribed distinct vertices.

**Theorem 3 (unimodular triangular change of basis).** Let \(w_{i,b}=e_b-e_{x_i}\), for \((i,b)\in D_x\), be the root-star basis of the spectral resource space. For \(\pi=(t_1,\ldots,t_d)\), write \(u_j\) for the vector of its \(j\)-th oriented path edge, and \(p(j)<j\) for the previous occurrence of the coordinate of \(t_j\), if one exists. Then
\[
u_j=w_{t_j}-w_{t_{p(j)}} ,
\]
where the second term is zero if \(p(j)\) does not exist. The matrix with columns \(u_j\) in the ordered basis \((w_{t_1},\ldots,w_{t_d})\) is unitriangular. Consequently, relative to any fixed ordering of the root-star basis,
\[
\boxed{\det(u_1,\ldots,u_d)=\operatorname{sgn}(\pi).}
\tag{2}
\]
Adjacent token swaps reverse this determinant, thereby connecting resource-basis orientation to the permutohedral exchange graph.

**Proof.** The changed coordinate goes from the value visited at its previous occurrence (or \(x_i\) for its first occurrence) to the newly named symbol. Subtracting their root-star vectors gives the identity above. The new token contributes diagonal coefficient one and any previous token contributes a coefficient in an earlier row. Hence the matrix is unitriangular, and the remaining determinant sign is the sign of the ordering permutation. \(\square\)

**Proposition 4 (signed endpoint enumeration).** Fix \(x\) and a diametral endpoint \(y\). The signed sum \(\sum_{\pi:x\to y}\operatorname{sgn}(\pi)\) is zero for \(q\ge4\), and also for \(q=2,k\ge2\). For \(q=3\), its absolute value is \(k!\), with the sign depending on the reference token order.

**Proof.** When \(q\ge4\), each factor has at least two nonterminal tokens. Interchange two chosen nonterminal tokens from one factor in the permutation word. The endpoint stays fixed, and the determinant changes sign; this is a sign-reversing fixed-point-free involution. For \(q=2,k\ge2\), each factor has one token, and every permutation has the same endpoint. Transpose the positions of two fixed tokens to pair signs.

For \(q=3\), the prescribed endpoint leaves a pair of ordered tokens in each coordinate. Every endpoint gallery is a shuffle of these \(k\) ordered pairs. Partition the \(2k\) word positions into adjacent slots \((1,2),(3,4),\ldots,(2k-1,2k)\). For a shuffle in which one slot contains tokens from different coordinates, choose the first such slot and swap its two tokens. This is a fixed-point-free sign-reversing involution, preserving each coordinate's internal token order. The surviving shuffles have every slot occupied by the two tokens of the same coordinate in their prescribed order. There are \(k!\) such shuffles. Permuting two complete slots makes four elementary transpositions, so all survivors have the same sign. The signed sum thus has absolute value \(k!\). \(\square\)

**Interpretation.** The cube and rank-two uniform endpoints have a common permutation-gallery and unimodular resource orientation algebra. The untwisted signed degree cancels at both endpoints for growing rank; the ternary Hamming interpolation retains a nonzero integer signed endpoint enumerator. This alone does not force any color-coherent gallery. Any determinant-degree attempt for arbitrary cube antipodal coloring must incorporate the coloring, root transport, or a signed-cover twist.

### Polarized Hamming turn geometry and the displacement conjecture

Let \(M=\bigoplus_{i=1}^{k}U_{r_i,E_i}\), with \(m_i:=|E_i|\ge2\) and \(1\le r_i<m_i\). The summand ground sets are the intrinsic connected components of \(M\). Define
\[
M^\flat=\bigoplus_iU_{1,E_i},\quad
G=\Gamma(M^\flat)=\square_iK_{E_i},\quad
N=\bigoplus_i M(K_{E_i}),\quad
d=\operatorname{rk}(N)=\sum_i(m_i-1).
\tag{1}
\]
An edge changing symbol \(a\) to \(b\) in factor \(i\) carries resource \((i,\{a,b\})\), represented by \(e_b-e_a\) in the \(i\)-th summand. The potential \(\Phi(x)=\bigoplus_i e_{x_i}\) is injective; its edge differences realize \(N\). Consequently every star of \(G\) is an \(N\)-basis, and every graph cycle is \(N\)-dependent.

A **factorwise polarity** \(\tau\) is either the identity, or a product of fixed-point-free involutions \(\tau_i:E_i\to E_i\) on all factors, with \(k\ge2\) in the latter case. Put \(\chi_\tau=0\) in the identity case and \(1\) otherwise. Equivalently, \(\chi_\tau\) is the canonical faithful character of \(\langle\tau\rangle\) into \(\mathbb F_2\), including the trivial group. Let \(c:E(G)\to\mathbb F_2\) color undirected edges and satisfy
\[
c(\tau e)=c(e)+\chi_\tau.
\tag{2}
\]
For each nonbacktracking turn \((u,v,w)\), prescribe a bit \(b(u,v,w)\) according to the **triangle-curvature rule**
\[
\boxed{
\begin{cases}
b(u,v,w)+b(w,v,u)=1,&uw\in E(G),\\
b(u,v,w)=c(uv)+c(vw),&uw\notin E(G).
\end{cases}}
\tag{3}
\]
The triangular case is an unrestricted tournament comparison; the other case tests edge-color agreement. For products of cliques, a turn is triangular precisely when its two steps change one factor. Both clauses are invariant under isomorphisms of the matroid with its chosen polarity.

Call a path \(P=(v_0,\ldots,v_\ell)\) an **accepted gallery** when its edge resources are \(N\)-independent, its graph edges have a common \(c\)-color, and every interior turn has bit \(b=0\). Matroid independence entails vertex simplicity because a closed subwalk yields an \(N\)-dependent cycle. The witness predicate is uniform across all members of this class.

**Theorem 1 (common rank-growth bound).** Every preceding geometry has an accepted gallery with
\[
\ell\ge\left\lceil\tfrac12\sqrt d\right\rceil .
\tag{4}
\]

*Proof.* One \(c\)-color class spans at least half the edges of the \(d\)-regular graph \(G\). Its spanning subgraph \(H\) has average degree at least \(d/2\). At every vertex of \(H\), put a tournament on the incident edges: for a pair forming a triangular turn, favor the bit-zero direction, which is unique by (3); for a nontriangular turn, both bit values are zero because both edges have the same color, so choose either direction. Restrict \(N\) to the edges of \(H\). Vertex stars remain independent, and all cycles of \(H\) remain dependent. The cycle-dominating resource-matroid terminal theorem of Article XI provides an \(N\)-independent path respecting these tournaments and containing at least \(\sqrt{\bar d(H)/2}\ge\sqrt d/2\) edges. Its turns have bit zero and its edges share one color. Taking the ceiling proves the claim. \(\square\)

The **polar displacement** is the intrinsic quantity
\[
\rho(G,\tau):=\min_x d_G(x,\tau x)=k\chi_\tau.
\tag{5}
\]

**Conjecture U (polarized Hamming displacement).** Every preceding geometry admits an accepted gallery with
\[
\boxed{\ell\ge \max\left\{
\left\lceil\tfrac12\sqrt{\operatorname{rk}N}\right\rceil,\,
\rho(G,\tau)\right\}.}
\tag{6}
\]
This is one quantitative conjecture over a continuous family of root-exchange geometries. It uses the same resource-independence, color-consistency, and turn-admissibility witness in every instance.

**Theorem 2 (NORI1 equivalence).** Conjecture U over the entire polarized Hamming class holds if and only if NORI1 holds for every admissible dimension.

*Proof that U implies NORI1.* For \(M=\bigoplus_{i=1}^nU_{1,2}\), \(G=Q_n\), \(N\) is the coordinate-partition resource matroid of rank \(n\), and \(\tau\) toggles all \(n\) factors. An arbitrary antipodally odd coloring of undirected cube edges satisfies (2), while all nonbacktracking turns are nontriangular and (3) becomes \(b(u,v,w)=c(uv)+c(vw)\). Thus accepted galleries are monochromatic coordinate-distinct geodesics. Equation (6) forces \(n\) edges. Independence then forces each coordinate to appear once, so the endpoints are antipodal.

*Proof that NORI1 implies U.* For identity polarity, Theorem 1 proves (6). Suppose \(\tau=\prod_i\tau_i\) is nontrivial. Choose any \(a_i\in E_i\) and consider the induced cube
\[
Q(a)=\prod_i\{a_i,\tau_i(a_i)\}\subseteq G.
\tag{7}
\]
It is invariant under \(\tau\), and \(\tau\) acts on it as cube complementation. By (2), the restriction of \(c\) is antipodally odd. NORI1 supplies a monochromatic geodesic of \(k\) edges within this cube. Each step changes a different factor, so its \(N\)-resources lie in different direct summands and are independent. Every turn changes two factors; hence its outside endpoints are nonadjacent in \(G\) and its bit is zero by (3). It is an accepted gallery of length \(k=\rho(G,\tau)\). Theorem 1 separately gives a gallery of length at least \(\lceil\sqrt d/2\rceil\). Taking the longer witness establishes (6). \(\square\)

**Corollary 3 (both original models).** The cube model \(M=\bigoplus U_{1,2}\), with its canonical nontrivial polarity, yields a full monochromatic antipodal geodesic by U. For the boundary model \(M=U_{2,n}\), the root is \(G=K_n\), \(N=M(K_n)\), \(d=n-1\), and \(\tau=\mathrm{id}\). Choose \(c\equiv0\). All turns are triangular, so any reversal-odd boundary coloring \(b(a,v,w)\) satisfies (3). Accepted galleries are vertex-simple bit-zero tight paths. Theorem 1 gives at least \(1+\lceil\sqrt{n-1}/2\rceil\) original vertices, and the unpartitioned terminal bound in Article XI improves this to \(1+\sqrt{(n-1)/2}\). Reversing the original vertex word gives the opposite color.

**Corollary 4 (even-alphabet antipodal extension).** Assuming NORI1, for any \(k\ge2\), any even \(m_i\ge2\), any factorwise fixed-point-free \(\tau\), and any edge coloring of \(\square_iK_{m_i}\) with \(c(\tau e)=1-c(e)\), there is a monochromatic path of \(k\) edges from some \(x\) to \(\tau x\), using every factor once. No triangle-turn comparison restricts this witness. This follows from the invariant cube (7).

**Proposition 5 (polarity is invisible locally).** In a nontrivially polarized product, fix \(x\) and \(R\) with \(2R<k\). Any arbitrary coloring of the edges induced by the radius-\(R\) ball about \(x\) extends to a global coloring satisfying (2).

*Proof.* If an edge \(e\) and \(\tau e\) both lay within that ball, some vertex \(y\) and its image \(\tau y\) would both be within distance \(R\) of \(x\). This contradicts \(k=d_G(y,\tau y)\le2R\). The edge action is free, since \(\tau\) changes every factor and \(k\ge2\), so each edge orbit has size two. Choose the prescribed bit on the unique orbit representative lying in the ball, put its complement on the translated edge, and fill all other orbits arbitrarily. \(\square\)

Theorem 1 is a uniform local rank-growth mechanism common to both examples. Theorem 2 shows that promoting this mechanism to full polar displacement is equivalent to the unresolved NORI1 assertion. The freedom in triangular turns and the forced color-potential rule on commuting-factor turns arise from the same graph's intrinsic local geometry. The current implication from NORI1 to U uses an invariant cube slice, leaving open a direct rank-saturation proof that interacts with all factors without restricting to that slice.

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

### Linear resource-independent path growth from square-flat turns

Let \(H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), and let \(N_{\rm sp}\) be its canonical spectral resource matroid of rank \(d=k(q-1)\). Let \(b(u,v,w)\in\mathbb F_2\) be defined on all nonbacktracking ordered turns, satisfying the mixed triangle/square axioms:

(i) if \(uw\in E(H)\), then \(b(u,v,w)+b(w,v,u)=1\);

(ii) there is one global edge coloring \(c:E(H)\to\mathbb F_2\) such that \(b(u,v,w)=c(uv)+c(vw)\) whenever \(uw\notin E(H)\).

A zero-turn path has \(b=0\) at every internal turn, and it is resource-independent when its edge vectors are independent in \(N_{\rm sp}\). The involution hypothesis at the cubical endpoint, when applicable, can be imposed additionally; it is unnecessary here.

**Theorem 1 (factor-count linear guarantee).** Every such mixed triangle/square turn system contains a zero-turn \(N_{\rm sp}\)-independent path with at least
\[
\boxed{\ell\ge \lceil k/2\rceil}
\tag{1}
\]
edges. The bound is uniform in \(q\) and valid for arbitrary triangular reversal-odd comparisons.

**Proof.** Choose any two symbols in each \(K_q\) factor and let \(C\subseteq H(k,q)\) be the induced copy of the hypercube \(Q_k\) on their \(2^k\) product vertices. Every two successive edges of a geodesic in \(C\) change distinct Cartesian factors. Therefore the two outer vertices of every such turn differ in two factors and are nonadjacent in the full Hamming graph. By (ii) its turn label is the sum of the colors of the two edges.

The restriction of \(c\) to \(C\) gives a binary edge coloring of \(Q_k\). Of its two monochromatic subgraphs, at least one has average degree at least \(k/2\), because \(Q_k\) is \(k\)-regular and the edge sets partition its edges. By the Leader–Long long-geodesic theorem (Imre Leader and Eoin Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33), any subgraph of a hypercube of average degree \(a\) contains a graph geodesic of at least \(a\) edges. Hence the denser color subgraph of \(C\) contains a monochromatic geodesic with at least \(\lceil k/2\rceil\) edges.

Such a geodesic changes each cube coordinate at most once. Its consecutive edge colors coincide; by (ii), all its turn labels are zero. The spectral resource vectors of its edges lie in distinct coordinate summands and are linearly independent. Thus it is an accepted zero-turn \(N_{\rm sp}\)-independent path of the required length. \(\square\)

In conjunction with the general mixed-turn terminal bound previously proved in Article XI, of order \(\sqrt{k(q-1)}\), this yields complementary, simultaneous guarantees of linear growth in factor count and square-root growth in resource rank:
\[
\ell_{\max}\ge \max\!\left\{\lceil k/2\rceil,\ \tfrac12\sqrt{k(q-1)}\right\}.
\tag{2}
\]
Formula (2) is a lower-bound combination; the stronger proposed unified conjecture asks for \(\ell\ge k\) in addition to the square-root term. The remaining gap is therefore a factor at most two in the factor-count branch.

**Lemma 2 (matroidal minimum-degree growth).** Let \(G\) be a finite simple graph with a matroid \(N\) on \(E(G)\) such that each vertex star is independent in \(N\) and every graph cycle is dependent in \(N\). If a subgraph \(F\subseteq G\) has minimum degree \(\delta\), then from every vertex of \(F\) there is an \(N\)-independent simple path with at least \(\delta\) edges.

**Proof.** Start at any vertex. If the current path has \(r<\delta\) edges, its edge set \(X\) is independent of rank \(r\). At the terminal vertex \(v\), the incident \(F\)-edges are independent in \(N\), so at most \(r\) of them can belong to \(\operatorname{cl}_N(X)\). Thus some incident edge \(e=vw\) is outside the closure, and \(X+e\) remains independent. If \(w\) were an earlier vertex of the path, \(X+e\) would contain a graph cycle and therefore be dependent, a contradiction. Hence the path can be extended. Continue until it has at least \(\delta\) edges. \(\square\)

**Corollary 3 (self-contained density bound).** Under the hypotheses of Lemma 2, every subgraph \(F\subseteq G\) of average degree \(a\) contains an \(N\)-independent simple path of length at least \(a/2\). Moreover, for every two-color edge coloring of a \(d\)-regular graph \(G\) under these hypotheses, some monochromatic \(N\)-independent path has length at least \(d/4\).

**Proof.** Iteratively delete vertices of current degree below \(a/2\). Such deletions strictly increase the average degree of the remaining nonempty graph, so a nonempty subgraph with minimum degree at least \(a/2\) remains. Apply Lemma 2. For a two-coloring, one color subgraph has average degree at least \(d/2\); apply the first assertion to it. \(\square\)

This corollary supplies a self-contained weaker version of (1), namely \(\ell\ge k/4\) on any induced \(Q_k\), without invoking the sharper Leader–Long theorem.

**Scope and asymmetry.** The rank-\(k\) root cube witness in Theorem 1 uses only cross-factor square-flat turns. Consequently it survives completely arbitrary and non-edge-orderable triangular comparisons. At the boundary endpoint \(k=1\), however, it supplies just one edge and does not replace the square-root boundary-tournament theorem. The mixed turn system combines the flat edge-potential geometry responsible for linear-in-\(k\) growth with freely oriented triangular comparisons responsible for the separate \(\sqrt{d}\) tournament bound.

### Edge-free coordinatewise polarities and the maximal Hamming reduction

Let \(G=\square_{i=1}^kK_{E_i}\), with \(|E_i|\ge2\). Let \(\tau=\prod_i\tau_i\) be any coordinatewise involution of \(G\), allowing fixed symbols in the individual factors. Define
\[
J(\tau)=\{i:\operatorname{Fix}(\tau_i)=\varnothing\},
\qquad h(\tau)=|J(\tau)|.
\tag{1}
\]
A nontrivial binary edge polarity is an undirected-edge coloring \(c\) satisfying \(c(\tau e)=1-c(e)\).

**Theorem 1 (edge-freeness and displacement).** For a nonidentity coordinatewise involution \(\tau\), the following are equivalent:

(i) \(\tau\) fixes no undirected edge of \(G\);

(ii) \(h(\tau)\ge2\);

(iii) there exists a binary edge polarity \(c\) with \(c(\tau e)=1-c(e)\).

Furthermore, for every coordinatewise involution, including the identity,
\[
\boxed{\min_{x\in V(G)} d_G(x,\tau x)=h(\tau).}
\tag{2}
\]

*Proof.* Every factor indexed by \(J(\tau)\) changes its symbol at every vertex, while every factor outside \(J(\tau)\) has at least one fixed symbol. A shortest Hamming path from \(x\) to \(\tau x\) changes precisely the factors on which \(x_i\ne\tau_i x_i\). Choosing fixed symbols in the other factors gives (2).

Assume \(h(\tau)\ge2\). An edge \(e\) changes one coordinate \(j\), leaving every other coordinate constant. At least one factor in \(J(\tau)\setminus\{j\}\) changes its constant symbol under \(\tau\); thus \(\tau e\ne e\), proving (i).

Conversely, assume \(h(\tau)\le1\) and \(\tau\) is nonidentity. Choose a component \(j\) in which \(\tau_j\) exchanges two distinct symbols \(a,b\); if \(h(\tau)=1\), take the sole fixed-point-free component for \(j\). For every \(i\ne j\), choose a fixed symbol of \(\tau_i\), possible by the definition of \(h\). Then the edge whose changing coordinate \(j\) joins \(a\) to \(b\), with all other coordinates fixed, is stabilized setwise by \(\tau\). Hence (i) implies (ii). An edge-stabilizing involution cannot support an odd binary edge polarity since it would require \(c(e)=1-c(e)\). If all edge orbits have size two, assign one arbitrary bit per orbit and its complement to the other edge, producing such a coloring. This proves the equivalence. \(\square\)

**Theorem 2 (NORI1 gives full intrinsic displacement).** Suppose \(\tau\) is nonidentity and \(h(\tau)\ge2\). Let \(c\) be any edge polarity of \(G\) and \(b\) any turn system obeying the triangle-curvature rule
\[
b(u,v,w)+b(w,v,u)=1\quad(uw\in E(G)),
\qquad b(u,v,w)=c(uv)+c(vw)\quad(uw\notin E(G)).
\tag{3}
\]
Assuming NORI1, there is a monochromatic accepted gallery \(P\) from \(x\) to \(\tau x\) of length \(h(\tau)\). Its edge labels are independent in the canonical resource matroid
\(N=\bigoplus_i M(K_{E_i})\).

*Proof.* For every \(i\in J(\tau)\) choose a symbol \(a_i\), and in every component outside \(J(\tau)\) choose a fixed symbol \(f_i=\tau_i(f_i)\). The induced subgraph
\[
Q=\prod_{i\in J(\tau)}\{a_i,\tau_i(a_i)\}
 \times\prod_{i\notin J(\tau)}\{f_i\}
\tag{4}
\]
is an \(h(\tau)\)-cube invariant under \(\tau\), whose restricted involution is its antipode. The restriction of \(c\) to \(Q\) is therefore antipodally odd. NORI1 supplies a monochromatic geodesic \(P\) joining antipodal vertices of \(Q\). The gallery changes every active component once, using pairwise different direct summands of \(N\), so its resource labels are independent. Consecutive steps change different factors, making the endpoints of their turn nonadjacent in the ambient Hamming graph. The second rule in (3) makes the bit of every interior turn zero. Since \(Q\) is induced, \(P\) is a path of \(G\) and its endpoints are \(x,\tau x\). Its length is \(h(\tau)\), which equals the minimum displacement by Theorem 1. \(\square\)

**Corollary 3 (largest coordinatewise polarized class).** Let \(\mathcal H\) consist of all pairs \((M,\tau)\) where \(M=\bigoplus_iU_{r_i,E_i}\) is a partition matroid and \(\tau\) acts coordinatewise on its intrinsic rank-one reduction, subject to either \(\tau=\mathrm{id}\) or \(h(\tau)\ge2\). Equip these pairs with undirected colors and the turn rule (3), imposing \(c(\tau e)=c(e)+\chi_\tau\), where \(\chi_\tau=0\) for the identity and \(1\) otherwise. Every member has an accepted gallery of length at least \(\lceil\sqrt{\operatorname{rk}N}/2\rceil\), by the cycle-dominating resource-matroid terminal theorem. The single strengthened assertion
\[
\boxed{\ell\ge\max\left\{
\left\lceil\tfrac12\sqrt{\operatorname{rk}N}\right\rceil,\,
\min_x d_G(x,\tau x)\right\}
\tag{5}
\]
for an accepted gallery in every member of \(\mathcal H\) is equivalent to NORI1.

*Proof.* The uniform rank-growth theorem in the preceding Article XI Hamming Subsection applies unchanged to \(\mathcal H\); its proof does not require nontrivial polarity. In the nontrivial case Theorem 2 supplies an independent witness of length equal to the second term of (5). The longer of these two witnesses proves (5) assuming NORI1. Conversely take \(M=\bigoplus_{i=1}^n U_{1,2}\) with its antipodal involution. Then the second term of (5) is \(n\), and an accepted gallery of \(n\) edges is a monochromatic antipodal cube geodesic. Thus (5) entails NORI1. \(\square\)

Theorem 1 establishes why this class is maximal among coordinatewise involutions admitting an odd coloring on undirected edges: every excluded nonidentity involution stabilizes an edge and admits no such coloring. Theorem 2 extends the antipodal cube transfer to Hamming products with odd-sized factors, arbitrary mixed component ranks, and fixed symbols in some factors; only the \(h(\tau)\) forced-moving components enter the invariant cube. This extension retains the same graphic resource matroid and the same local turn law that yield unrestricted boundary-tournament square-root paths when \(\tau\) is the identity.

### Canonical central polarity of partition-matroid Hamming roots

Let \(M=\bigoplus_{i\in I}U_{r_i,E_i}\), with \(1\le r_i<|E_i|\). The connected-component decomposition is intrinsic to \(M\). Define the rank-one reduction and its root graph
\[
M^\flat=\bigoplus_{i\in I}U_{1,E_i},
\qquad G_M=\Gamma(M^\flat)=\square_{i\in I}K_{E_i}.
\tag{1}
\]
Put \(I_2=\{i:|E_i|=2\}\), \(s=|I_2|\). On every two-element ground set the exchange of its elements is a choice-free involution. Let
\[
\eta_M(x)_i=
\begin{cases}
E_i\setminus\{x_i\},&i\in I_2,\\
x_i,&i\notin I_2.
\end{cases}
\tag{2}
\]
Here \(x=(x_i)\) is a basis of \(M^\flat\), and in the first case the complement is understood as its unique member. The map \(\eta_M\) depends only on \(M\).

**Theorem 1 (center of the root-matroid automorphism group).** If \(s=0\), the center of \(\operatorname{Aut}(M^\flat)\) is trivial. If \(s\ge1\), it has order two and is generated by \(\eta_M\). Thus the unique possible nonidentity root automorphism commuting with all automorphisms of \(M^\flat\) is simultaneous exchange of every two-element component.

*Proof.* For every \(m\ge2\), let \(k_m\) denote the number of components of size \(m\). The action on the ground set identifies
\[
\operatorname{Aut}(M^\flat)
=\prod_{m\ge2}\left(S_m^{k_m}\rtimes S_{k_m}\right)
\tag{3}
\]
(the factor for \(k_m=0\) is omitted). A central element must normalize and centralize the independent symmetric groups acting within individual components. Conjugation carries the subgroup supported on a component \(i\) to the subgroup supported on its image; commuting with all such subgroups forces each component to be preserved individually. The restriction to a component of size \(m\) must then lie in \(Z(S_m)\), which is trivial for \(m\ge3\) and is \(S_2\) when \(m=2\). Finally, centrality with respect to permutations of equally sized components forces all two-element components to be flipped together or none to be flipped. Both choices commute with every automorphism. Thus the claimed center consists of \(\mathrm{id}\) and \(\eta_M\) when \(s\ge1\), and only \(\mathrm{id}\) otherwise. \(\square\)

**Theorem 2 (maximal canonical odd-coloring domain).** If \(s\ge1\), the canonical involution \(\eta_M\) has graph displacement
\[
d_{G_M}(x,\eta_M x)=s\qquad\text{for every }x.
\tag{4}
\]
It acts without fixed undirected graph edges if and only if \(s\ge2\). Consequently a binary edge coloring satisfying
\[
c(\eta_M e)=1-c(e)
\tag{5}
\]
exists if and only if \(s\ge2\).

*Proof.* Formula (2) changes the coordinate on each of the \(s\) two-element factors and fixes all others, giving (4). If \(s=1\), fix arbitrary coordinates in the other factors and take the edge that changes the unique two-element factor; it is preserved as an undirected edge by \(\eta_M\). If \(s\ge2\), every graph edge changes just one factor, while \(\eta_M\) flips at least one other factor; hence the edge moves to a different edge. The edge-orbit action then consists of two-element orbits, and assigning complementary colors to their two members gives (5). A fixed edge would require its color to equal its complement, which is impossible. \(\square\)

Define the **canonical polarized partition class**
\[
\mathcal C_{\rm can}=
\{M=\bigoplus_iU_{r_i,E_i}:s(M)=0\text{ or }s(M)\ge2\},
\tag{6}
\]
and put \(\tau_M=\eta_M\) for \(s\ge2\), and \(\tau_M=\mathrm{id}\) for \(s=0\). This polarization is canonically determined by the undecorated matroid \(M\); no symbols, matchings, preferred bases, or external involutions are chosen. The excluded case \(s=1\) is precisely the case when the only nonidentity central involution would stabilize an undirected edge. Equip the root graph with the canonical graphic resource matroid
\[
N_M=\bigoplus_i M(K_{E_i})
\tag{7}
\]
and the mixed turn law: on triangular turns, reversal exchanges bit zero and bit one, while on nontriangular turns the bit is the sum of the two incident graph-edge colors. A witness is a monochromatic path with independent \(N_M\)-resources and all turn bits zero.

**Corollary 3 (undecorated common class and quantitative conjecture).** Both \(M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2}\) for \(n\ge2\) and \(M_{\rm bd}=U_{2,n}\) for \(n\ge3\) lie in \(\mathcal C_{\rm can}\). In the former, \((G_M,\tau_M)=(Q_n,\text{complement})\); in the latter, \((G_M,\tau_M)=(K_n,\mathrm{id})\). The resource rank is
\(d=\sum_i(|E_i|-1)\).
On this class the single strengthened path assertion
\[
\boxed{\ell\ge\max\left\{
\left\lceil\tfrac12\sqrt d\right\rceil,\ s(M)
\right\}}
\tag{8}
\]
for a monochromatic resource-independent accepted gallery is equivalent to NORI1.

*Proof.* The universal \(\lceil\sqrt d/2\rceil\) lower bound follows from the cycle-dominating resource-matroid terminal theorem, as in the preceding polarized Hamming Subsection. In the cube model the canonical polarity is complement and \(s=d=n\), so (8) gives a full monochromatic antipodal geodesic. For the reverse implication, assume NORI1. When \(s=0\) the terminal theorem proves (8). When \(s\ge2\), fix one symbol in each factor of size at least three and retain both symbols of each two-element factor. The induced \(s\)-cube is invariant under \(\eta_M\), which acts as the antipode there. The restricted edge coloring is odd. NORI1 yields a monochromatic geodesic changing every two-element factor once; it has independent root-graphic resources and all its turns are nontriangular, so the turn bits vanish. This yields a gallery of length \(s\). Take the longer of this witness and the terminal-theorem witness to obtain (8). In the boundary model \(s=0,d=n-1\), the root is \(K_n\), and the triangular turn law realizes every ordinary reversal-odd boundary tournament, giving the common square-root bound. \(\square\)

**Interpretation.** Simultaneous binary-factor complementation is the unique nontrivial symmetry canonically available from the root-matroid automorphism group. Arbitrary pairings in factors of size at least four lead to legitimate *chosen* polarizations but cannot be obtained as automorphism-equivariant operations on those factors. The canonical class (6) therefore answers the intrinsic-polarization objection for the partition-matroid Hamming family. The rank-saturation term of (8) remains equivalent to NORI1; the shared resource-rank growth mechanism is proved independently.

### Affine cube-edge colorings: permutation syndromes and elimination of two-dimensional obstructions

Let \(Q_n\) have coordinates in \(\mathbb F_2^n\). Consider arbitrary affine binary colors on its undirected coordinate edges,
\[
c_i(x)=a_i+\sum_{j\ne i}B_{ij}x_j,
\qquad a\in\mathbb F_2^n,\quad B\in\mathbb F_2^{n\times n},\quad B_{ii}=0.
\tag{1}
\]
The formula is independent of the toggled bit \(x_i\), as required for an undirected edge color. The antipodal oddness condition \(c_i(x+\mathbf1)=c_i(x)+1\) is equivalent to
\[
B\mathbf1=\mathbf1.
\tag{2}
\]
The matrix \(B\) is the linear cross-coordinate influence operator of the edge coloring. Write \(V=\mathbb F_2^n/\operatorname{im}B\), and denote the quotient map by \(p:\mathbb F_2^n\to V\).

For a permutation \(\pi=(i_1,\dots,i_n)\), put
\[
v_\pi(i)=\sum_{j\text{ occurring before }i\text{ in }\pi} B_{ij}.
\tag{3}
\]
A geodesic beginning at \(x\) and flipping the coordinates in order \(\pi\) has color word, indexed by its step directions,
\[
c_{\pi}(x)=a+Bx+v_\pi.
\tag{4}
\]
It is monochromatic if and only if
\[
a+v_\pi\in\operatorname{im}B.
\tag{5}
\]
Indeed a constant color-one word can be converted to a color-zero word by replacing its root \(x\) by \(x+\mathbf1\), using (2). The obstruction to a given order is therefore the quotient syndrome \(p(a+v_\pi)\).

**Lemma 1 (cyclic rotation identity).** If \(\pi=(i,i_2,\ldots,i_n)\) and \(\operatorname{rot}\pi=(i_2,\ldots,i_n,i)\), then
\[
v_{\operatorname{rot}\pi}=v_\pi+e_i+Be_i,
\qquad
p(v_{\operatorname{rot}\pi})=p(v_\pi)+p(e_i).
\tag{6}
\]
For every permutation the \(n\) cyclic rotations consequently trace in \(V\) a closed walk whose successive increments are \(p(e_{i_1}),\ldots,p(e_{i_n})\).

*Proof.* Moving the first direction \(i\) to the end changes its own predecessor parity from zero to \(\sum_{j\ne i}B_{ij}=1\). For every other direction \(j\), the presence of \(i\) among its predecessors is removed, changing its parity by \(B_{ji}\). Thus the syndrome difference is \(e_i+Be_i\). The second equation follows by quotienting by \(\operatorname{im}B\), and the cyclic walk follows by iteration. The walk closes because \(\sum_i p(e_i)=p(\mathbf1)=0\) by (2). \(\square\)

**Theorem 2 (affine rank-codimension-two closure).** Suppose (1)--(2) hold and
\[
\boxed{\operatorname{rank}_{\mathbb F_2}B\ge n-2.}
\tag{7}
\]
Then there exist a starting vertex \(x\) and a coordinate permutation \(\pi\) such that the entire antipodal geodesic \(x\to x+\mathbf1\) following \(\pi\) is monochromatic. In particular every antipodally odd affine cube-edge coloring whose cross-influence matrix has nullity at most two satisfies NORI1.

More precisely, for every \(a\), the quotient-syndrome set
\[
\boxed{\{p(v_\pi):\pi\in S_n\}=V}
\tag{8}
\]
whenever \(\dim V\le2\). If \(\dim V=0\), every permutation admits a monochromatic geodesic; for each successful permutation, the number of roots of either prescribed constant color is \(2^{n-\operatorname{rank}B}\), and the roots for opposite colors are antipodal translates.

*Proof.* Let \(t=\dim V=n-\operatorname{rank}B\). The claim is immediate for \(t=0\), since then \(V=0\). If \(t=1\), the classes \(p(e_i)\) span \(V\), so some \(i\) has \(p(e_i)\ne0\). Take any permutation starting with \(i\). Lemma 1 shows that its syndrome and the syndrome of its cyclic rotation differ by the nonzero element of \(V\), and hence together attain all of \(V\).

Now let \(t=2\). Put \(w_i=p(e_i)\in V\cong\mathbb F_2^2\). Their sum vanishes by (2), and they span \(V\), since the \(e_i\) span \(\mathbb F_2^n\). Suppose there are distinct indices \(i,j,h\) with
\[
w_i=w_h=u\ne0,\qquad w_j=v\notin\{0,u\}.
\tag{9}
\]
Choose a permutation beginning \((i,j,h)\). Its first four cyclic-rotation syndromes, by (6), differ from the first by
\[
0,\quad u,\quad u+v,\quad v,
\]
which exhaust \(V\). Thus (8) follows in this case.

It remains to show that (9) can fail only in a special configuration and that this configuration also satisfies (8). Let \(N_u,N_v,N_{u+v}\) be the multiplicities of the three nonzero vectors of \(V\) among the \(w_i\). The identity \(\sum_iw_i=0\) forces
\[
N_u\equiv N_v\equiv N_{u+v}\pmod2.
\tag{10}
\]
Since the \(w_i\) span \(V\), if some nonzero value occurs at least twice and another linearly independent nonzero value occurs, (9) holds. If no such pair exists, (10) implies that the only nonzero \(w_i\) are three distinct values \(u,v,u+v\), each appearing once. Denote their indices by \(i,j,h\) respectively. All other \(w_\ell\) vanish.

Because \(p(Be_\ell)=0\) for every \(\ell\), this exceptional configuration gives
\[
B_{i\ell}u+B_{j\ell}v+B_{h\ell}(u+v)=0.
\]
Linear independence of \(u,v\) yields
\[
B_{i\ell}=B_{j\ell}=B_{h\ell}\qquad\text{for every }\ell.
\tag{11}
\]
The three rows \(i,j,h\) of \(B\) coincide. Their diagonal entries vanish, so their entries in the three columns \(i,j,h\) are all zero. By (2), their common row has odd sum; consequently some index \(z\notin\{i,j,h\}\) satisfies
\[
B_{iz}=B_{jz}=B_{hz}=1,\qquad w_z=0.
\tag{12}
\]

Choose \(\pi=(i,z,j,h,\ldots)\). Its first cyclic-rotation syndromes attain the three values
\[
p(v_\pi)+\{0,u,u+v\};
\]
the missing fourth value is \(p(v_\pi)+v\). Swap the adjacent symbols \(z,j\), obtaining \(\pi'=(i,j,z,h,\ldots)\). An adjacent transposition of directions \(j,z\) changes \(v_\pi\) by
\(B_{jz}e_j+B_{zj}e_z\). By (12),
\[
p(v_{\pi'})=p(v_\pi)+w_j=p(v_\pi)+v,
\]
the missing value. Thus the two permutations together with the displayed cyclic rotations exhaust \(V\). This proves (8) for \(t=2\).

Finally, (8) permits choosing \(\pi\) so that \(p(v_\pi)=p(a)\), making (5) hold. The system \(Bx=a+v_\pi\) then has \(2^{n-\operatorname{rank}B}\) roots. Adding \(\mathbf1\) to any solution changes all its edge colors from zero to one by (2), proving the last assertion. \(\square\)

**Corollary 3 (necessary structure of affine counterexamples).** An affine antipodally odd counterexample to NORI1, if one exists, must have
\[
\boxed{\dim\ker B^{\mathsf T}\ge3.}
\tag{13}
\]
Furthermore for any \(B\) satisfying (2), the quotient syndrome of a cyclically rotated permutation changes by a coordinate class \(p(e_i)\). Thus the possible affine obstruction is a simultaneous multi-syndrome obstruction on the permutation exchange geometry; no obstruction of dimension one or two survives arbitrary cyclic rotations and adjacent transpositions.

The theorem is dimension-independent, and imposes no symmetry on \(B\). Its proof uses the same resource-permutation language as the dual-basis galleries of Article XI. It establishes full rank saturation for a broad affine NORI1 class, while leaving nonlinear colorings and affine influence matrices of nullity at least three open.

#### 4. Uniform random affine closure probability

Consider the uniform ensemble of affine antipodally odd cube-edge colorings (1): choose each intercept \(a_i\) independently and uniformly, and independently choose each row \(B_{i,*}\) uniformly among binary vectors with \(B_{ii}=0\) and odd Hamming weight. Every admissible affine coloring occurs with equal probability.

**Theorem 4 (random influence rank).** For \(n\ge3\), if \(T=n-\operatorname{rank}B=\dim\ker B^{\mathsf T}\), then
\[
\boxed{\mathbb E(2^T-1)=1-2^{1-n}.}
\tag{14}
\]
Consequently,
\[
\boxed{\Pr(T\ge3)\le\frac{1-2^{1-n}}7<\frac17,}
\tag{15}
\]
and, by Theorem 2, the probability that an affine antipodally odd cube-edge coloring admits a full monochromatic antipodal geodesic is at least
\[
\boxed{1-\frac{1-2^{1-n}}7>\frac67.}
\tag{16}
\]
The conclusion is uniform in the dimension and in the arbitrary intercept vector.

*Proof.* Expand \(2^T-1=\sum_{y\ne0}\mathbf1_{\{y^{\mathsf T}B=0\}}\). Since \(B\mathbf1=\mathbf1\), any left-kernel vector \(y\) has even Hamming weight, so an odd-weight \(y\) contributes zero probability. For an even-weight nonzero \(y\), choose two distinct positions \(i,j\) in its support. A uniform row \(B_{i,*}\) is supported on the odd-parity affine hyperplane with coordinate \(i\) fixed to zero; its translation space is
\[
W_i=\{z:z_i=0,\ z\cdot\mathbf1=0\}.
\]
For \(n\ge3\), the sum \(W_i+W_j\) is the full even-parity hyperplane \(W=\{z:z\cdot\mathbf1=0\}\). Indeed \(W_i^\perp=\langle\mathbf1,e_i\rangle\) and \(W_j^\perp=\langle\mathbf1,e_j\rangle\), whose intersection is \(\langle\mathbf1\rangle\); taking orthogonal complements proves the claim. The sum of the two independent uniform rows is consequently uniform on an even-parity affine coset, which here equals \(W\). Adding the other independently chosen rows in the even support of \(y\) preserves uniformity on \(W\), since their total parity is even. Thus
\[
\Pr(y^{\mathsf T}B=0)=|W|^{-1}=2^{-(n-1)}
\]
for every even-weight nonzero \(y\). There are \(2^{n-1}-1\) such vectors. Summing proves (14). On the event \(T\ge3\), the number \(2^T-1\) is at least seven, so Markov's inequality gives (15). Theorem 2 guarantees the desired geodesic on the complementary event \(T\le2\), proving (16). \(\square\)

The estimate concerns an ensemble of arbitrary affine cross-coordinate influence operators, including nonsymmetric ones. It is independent of the chosen coordinate order and complements the permutation-syndrome closure theorem, which applies deterministically whenever \(T\le2\).

### Affine root-syndrome gallery transport and corank-one closure

Let \(n\ge2\), \(M\in\mathbb F_2^{n\times n}\) have zero diagonal and \(M\mathbf1=\mathbf1\), and color the undirected coordinate-\(i\) edges of \(Q_n\) by
\[
c_i(x)=a_i+\sum_jM_{ij}x_j.
\tag{1}
\]
The row-oddness condition \(M\mathbf1=\mathbf1\) is the antipodal-odd coloring law. For a coordinate permutation \(\pi\in S_n\), put
\[
t_i(\pi)=\sum_{\pi^{-1}(j)<\pi^{-1}(i)}M_{ij}.
\tag{2}
\]
Let \(R=\operatorname{im}M\), \(q=n-\operatorname{rk}M\), and \(\Phi(\pi)=t(\pi)+R\in\mathbb F_2^n/R\).

**Theorem 1 (root criterion).** A monochromatic full geodesic with coordinate order \(\pi\) exists if and only if \(\Phi(\pi)=a+R\). For each qualifying \(\pi\), there are \(2^{q+1}\) directed monochromatic geodesics with that order, counted over both colors and all roots. Swapping two consecutive directions \(i,j\) changes the quotient syndrome by
\[
\boxed{\Phi(\pi')-\Phi(\pi)=\Delta_{ij}+R,\qquad
\Delta_{ij}=M_{ij}e_i+M_{ji}e_j.}
\tag{3}
\]

**Proof.** The edge traversed in direction \(i\) from root \(x\), after visiting the earlier directions, has color \(a_i+(Mx)_i+t_i(\pi)\). Hence the full word is constant \(s\) if and only if \(Mx=a+t(\pi)+s\mathbf1\). Since \(\mathbf1=M\mathbf1\in R\), existence is independent of \(s\) and is equivalent to the quotient criterion. Each solvable equation has \(2^q\) solutions \(x\) for either \(s\). Adjacent exchange modifies only the two preceding-direction sums for \(i,j\), giving (3). \(\square\)

**Theorem 2 (universal quotient span and balanced characters).** For every matrix satisfying (1),
\[
\boxed{R+\operatorname{span}\{\Delta_{ij}:i<j\}=\mathbb F_2^n.}
\tag{4}
\]
Consequently the affine span of \(\Phi(S_n)\) is the entire quotient. Moreover, every nonzero linear character of \(\mathbb F_2^n/R\) takes each of its values on at least \((n-1)!\) permutations.

**Proof.** A vector \(z\) annihilating both \(R\) and all the \(\Delta_{ij}\) obeys \(M^Tz=0\) and \(z_iM_{ij}+z_jM_{ji}=0\) for all \(i\ne j\). Fixing \(i\) and summing the latter relations over \(j\ne i\) gives
\[
0=z_i\sum_jM_{ij}+\sum_jM_{ji}z_j=z_i+(M^Tz)_i=z_i.
\]
Thus \(z=0\), proving (4). Every \(\Delta_{ij}\) appears as a difference of \(\Phi\)-values on two permutations in which \(i,j\) are adjacent, giving the affine-span assertion.

For nonzero \(z\in\ker M^T\), (4) ensures some \(i,j\) satisfy \(z\cdot\Delta_{ij}=1\). There are \((n-1)!\) permutations containing \(i,j\) consecutively in that order and the same number containing \(j,i\) consecutively. Swapping the two entries pairs them and flips the value of \(z\cdot\Phi\). Thus each character value occurs at least \((n-1)!\) times. \(\square\)

**Corollary 3 (unrestricted nonsymmetric affine closure in corank at most one).** If \(\operatorname{rk}M\ge n-1\), then for every choice of \(a\), the coloring (1) admits a monochromatic full antipodal geodesic. There are \(2n!\) directed such geodesics when \(\operatorname{rk}M=n\), and at least \(4(n-1)!\) when \(\operatorname{rk}M=n-1\).

**Proof.** If \(q=0\), the quotient is trivial and every order qualifies. If \(q=1\), Theorem 2 forces both elements of the quotient to be attained and guarantees at least \((n-1)!\) permutations in either class. Apply Theorem 1. \(\square\)

**Proposed affine quotient-surjectivity conjecture.** Every zero-diagonal row-odd binary matrix satisfies
\[
\Phi(S_n)=\mathbb F_2^n/\operatorname{im}M.
\tag{5}
\]
Its proof would settle all antipodally odd *affine* cube-edge colorings. Full affine span from Theorem 2 is a necessary step but does not alone imply (5) when \(q\ge2\). The general nonlinear NORI1 conjecture remains separate.

**Falsification check.** Direct exhaustive enumeration of all row-odd zero-diagonal matrices at dimensions \(3,4,5\) found no counterexample to (5): respectively \(8,256,32768\) matrices. The largest observed coranks were respectively \(1,2,3\). No computation is used in the proofs.

**Relationship to prior work.** The manuscript's forest-coupling theorem gives rooted switch bounds for sparse symmetric \(M\). The results here apply to arbitrary nonsymmetric matrices of corank at most one and establish an unrestricted-dimensional gallery-exchange span statement for every affine antipodally odd interaction matrix.

#### Theorem 4 (corank-two affine NORI1 closure)

Under the assumptions of Theorem 1, if
\[
\boxed{\operatorname{rk}_{\mathbb F_2}M\ge n-2,}
\tag{11}
\]
then **every** choice of \(a\) yields a monochromatic full antipodal geodesic. When \(\operatorname{rk}M=n-2\), there are at least \(16\) directed monochromatic full geodesics. Thus affine root-syndrome surjectivity (5) holds for quotient dimensions \(q=0,1,2\), with no symmetry condition on \(M\).

**Lemma 4.1 (cyclic gallery transport).** Let \(\pi=(i_1,\ldots,i_n)\) and let \(\rho\pi=(i_2,\ldots,i_n,i_1)\). In \(Q=\mathbb F_2^n/\operatorname{im}M\), write \(g_i=e_i+\operatorname{im}M\). Then
\[
\boxed{\Phi(\rho\pi)=\Phi(\pi)+g_{i_1}.}
\tag{12}
\]
Successive cyclic rotations visit the cosets
\[
\Phi(\pi),\quad\Phi(\pi)+g_{i_1},\quad
\Phi(\pi)+g_{i_1}+g_{i_2},\quad\ldots.
\tag{13}
\]

**Proof.** Moving \(i_1\) from first to last reverses its order relative to every other direction. Its own coordinate of \(t\) changes by \(\sum_{j\ne i_1}M_{i_1j}=1\), while coordinate \(j\ne i_1\) changes by \(M_{j i_1}\). Thus
\[
t(\rho\pi)+t(\pi)=e_{i_1}+Me_{i_1},
\]
whose quotient class is \(g_{i_1}\). Iteration proves (13). \(\square\)

**Proof of Theorem 4.** The cases \(q=0,1\) are Corollary 3, so suppose \(q=2\). The \(n\) vectors \(g_i\in Q=\mathbb F_2^2\) span \(Q\) and satisfy \(\sum_i g_i=\mathbf1+\operatorname{im}M=0\).

First suppose some nonzero class \(u\in Q\) occurs as \(g_i=g_{i'}=u\) at two distinct coordinates, and some other coordinate has class \(v\notin\{0,u\}\). Take a permutation beginning with \(i,j,i'\), where \(g_j=v\). By (13), four successive cyclic rotations have syndrome classes
\[
z,\quad z+u,\quad z+u+v,\quad z+v.
\]
They are the four elements of \(Q\). Therefore \(\Phi(S_n)=Q\).

Otherwise, because the \(g_i\) span \(Q\) and sum to zero, the only nonzero \(g_i\)'s consist of **three distinct nonzero classes appearing once each**. Denote the corresponding coordinates by \(a,b,c\), and let \(S=\{a,b,c\}\). Every \(e_u\) with \(u\notin S\) lies in \(R=\operatorname{im}M\), and \(e_a+e_b+e_c\in R\). These \(n-2\) vectors are independent, so
\[
R=\operatorname{span}\{e_u:u\notin S\}
+\operatorname{span}\{e_a+e_b+e_c\}.
\tag{14}
\]
Every column \(Me_j\) lies in \(R\); restriction of such a column to the coordinates \(a,b,c\) therefore has either \(000\) or \(111\). Consequently rows \(a,b,c\) of \(M\) are identical; denote their common row by \(w\). The zero diagonal gives \(w_a=w_b=w_c=0\). Since the row sum is odd, some \(u\notin S\) satisfies \(w_u=1\).

Choose permutations beginning with the four-letter blocks
\[
(a,b,c,u),\qquad (a,u,b,c),\qquad
(b,u,a,c),\qquad (c,u,a,b),
\]
and place all other coordinates afterward, in any common order. For their syndrome vectors \(t(\pi)\), the entries at \(a,b,c\) are respectively
\[
000,\qquad 011,\qquad 101,\qquad 110.
\]
Indeed, within \(S\) the common row \(w\) vanishes, all other outside coordinates come after the block, and the sole preceding \(w\)-active coordinate inside the block is \(u\). By (14), the four triples represent the four quotient classes. Hence \(\Phi(S_n)=Q\) also in this case.

For any \(a+R\), therefore, a qualifying permutation exists. Reversing a qualifying permutation gives another: because \(M\mathbf1=\mathbf1\), formula (2) gives \(t(\operatorname{rev}\pi)=t(\pi)+\mathbf1\), and \(\mathbf1\in R\). The two permutations are distinct for \(n\ge3\). Each supplies \(2^{q+1}=8\) directed full monochromatic geodesics by Theorem 1, giving the lower bound \(16\). \(\square\)

**Scope.** This handles affine antipodally odd cube-edge colorings whenever the binary interaction matrix has corank at most two. It strengthens the corank-one case without assuming symmetry or a sparse interaction graph. The first unresolved affine quotient dimension is \(q=3\).

#### Theorem 5 (fixed-support rank-defect control)

The following holds even for a zero-diagonal affine matrix \(M\) without the row-oddness condition. Write \(q=n-\operatorname{rk}M\). There is a set \(I\subseteq[n]\) of cardinality \(q\), depending only on \(M\), with this property: **for every prescribed permutation \(\pi\)** there is a root \(x\) for which all edges of its full geodesic in directions outside \(I\) have color zero. Its color-one counterpart on those directions exists whenever \(M\mathbf1=\mathbf1\). In particular, some full antipodal geodesic has at most \(q\) color changes:
\[
\boxed{\mu(c)\le n-\operatorname{rk}M.}
\tag{15}
\]

**Proof.** Choose \(I\) such that the coordinate cosets \(\{e_i+R:i\in I\}\) form a basis of \(\mathbb F_2^n/R\), with \(R=\operatorname{im}M\). Then every coset has one representative supported on \(I\). For any \(\pi\), choose that representative \(w\) for the coset \(a+t(\pi)+R\). Solve \(Mx=a+t(\pi)+w\). Formula (4) of Theorem 1 says the associated edge-color vector is \(w\), vanishing outside \(I\). If \(M\mathbf1=\mathbf1\), replace \(x\) by \(x+\mathbf1\) to complement the colors. Finally choose \(\pi\) to traverse every direction outside \(I\) first and the \(q\) directions in \(I\) last. Its word is \(0^{n-q}w_I\), which changes color at most \(q\) times. \(\square\)

For \(q=1\) and antipodal oddness, the ordinary odd-change rotation of the full path converts the resulting at-most-one-switch path into a monochromatic full path. Theorem 4 strengthens this conclusion to the larger class \(q=2\).

#### Theorem 6 (binary cut transport and a Gray-code saturation criterion)

For any subset \(S\subseteq[n]\), let \(\mathbf1_S\) be its indicator vector. Moving a consecutive initial block whose coordinate set is \(S\) to the end of the permutation, preserving the internal order of both blocks, changes its syndrome by
\[
\boxed{\Phi(\text{block rotated }\pi)-\Phi(\pi)=\mathbf1_S+R.}
\tag{16}
\]
Indeed the cross-block swaps contribute
\[
\sum_{i\in S,j\notin S}\Delta_{ij}
=\mathbf1_S+M\mathbf1_S
\]
because each full transposition star obeys
\(\sum_{j\ne i}\Delta_{ij}=e_i+Me_i\) and the internal pairs cancel twice. Reduction modulo \(R\) proves (16).

More generally, suppose the projected coordinate vectors \(g_i=e_i+R\) contain a quotient basis \(h_1,\ldots,h_q\) with at least \(2^{q-j}\) distinct coordinate representatives of \(h_j\) for every \(j=1,\ldots,q\). Then \(\Phi:S_n\to\mathbb F_2^n/R\) is surjective, and every affine antipodally odd coloring with this matrix \(M\) has a monochromatic full geodesic.

**Proof.** The standard reflected binary Gray sequence on \(\mathbb F_2^q\) visits all \(2^q\) vectors, starting at zero, using \(2^{q-j}\) steps in basis direction \(h_j\). Choose distinct coordinates representing those steps and place them first in a coordinate permutation, ordered as in this Gray sequence; place the remaining coordinates afterward. By Lemma 4.1, consecutive cyclic rotations traverse its successive quotient prefix sums. They visit all \(2^q\) quotient syndromes, proving surjectivity and then the existence assertion by Theorem 1. \(\square\)

The cut identity (16) is the affine root-transport analogue of the cycle–cocycle relation: the sum of local pair exchanges across a coordinate cut equals its indicator modulo the root-change image. The Gray-code condition is a sufficient structural criterion, while Theorem 4 proves the entire corank-two family without a repetition hypothesis.

#### Theorem 7 (all rank-two antipodally odd affine interactions admit monochromatic full paths)

Suppose \(M_{ii}=0\), \(M\mathbf1=\mathbf1\), and
\[
\boxed{\operatorname{rk}_{\mathbb F_2}M=2.}
\tag{17}
\]
Then for every constant vector \(a\), the affine coloring \(c_i(x)=a_i+(Mx)_i\) admits a monochromatic antipodal geodesic. Moreover, there exist two fixed coordinate directions \(u,t\), depending only on \(M\), such that for every \(a\) a monochromatic full geodesic begins at one of the four roots \(0,e_u,e_t,e_u+e_t\).

**Proof.** Because all rows of \(M\) have odd parity, and the two-dimensional row space contains only two odd-parity vectors, there are precisely two distinct row types \(v,w\). Let \(A\) be the nonempty set of row indices of type \(v\) and \(B\) those of type \(w\), partitioning \([n]\). The zero diagonal forces \(v_i=0\) for \(i\in A\) and \(w_j=0\) for \(j\in B\). Therefore
\[
U=\operatorname{supp}v\subseteq B,\qquad
T=\operatorname{supp}w\subseteq A,
\]
and both \(|U|\) and \(|T|\) are odd. For any \(u\in U\) and \(t\in T\), the columns of \(M\) satisfy
\[
Me_u=\mathbf1_A,\qquad Me_t=\mathbf1_B.
\tag{18}
\]
Hence the root-change image is \(R=\operatorname{span}\{\mathbf1_A,\mathbf1_B\}\).

Choose bits \(\alpha,\beta\), and define target labels \(h_i=a_i+\alpha\) on \(A\) and \(h_j=a_j+\beta\) on \(B\). Because \(|T|\) is odd, one can choose \(\alpha\) so that
\[
|T_0|:=|\{i\in T:h_i=0\}|\quad\text{is even};
\]
because \(|U|\) is odd, choose \(\beta\) so that
\[
|U_0|:=|\{j\in U:h_j=0\}|\quad\text{is odd}.
\]
Write \(T_1=T\setminus T_0\), \(U_1=U\setminus U_0\). Construct a coordinate permutation whose active-coordinate blocks occur in the order
\[
\boxed{T_0,\quad U_0,\quad T_1,\quad U_1.}
\tag{19}
\]
Every \(i\in T_0\) encounters zero earlier members of \(U\), so \(t_i(\pi)=0=h_i\). Every \(j\in U_0\) encounters \(|T_0|\) earlier members of \(T\), an even number, so \(t_j(\pi)=0=h_j\). Every \(i\in T_1\) encounters \(|U_0|\) earlier members of \(U\), an odd number, so \(t_i(\pi)=1=h_i\). Every \(j\in U_1\) encounters all \(|T|\) earlier members of \(T\), also odd, so \(t_j(\pi)=1=h_j\).

For \(i\in A\setminus T\), the same formula \(t_i(\pi)=|\{u\in U:u\text{ precedes }i\}|\pmod2\) applies. Insert such an inactive coordinate at the very beginning if \(h_i=0\), and at the very end if \(h_i=1\). For \(j\in B\setminus U\), insert it at the beginning if \(h_j=0\) and at the end if \(h_j=1\). Their insertion does not change any active parity, since inactive \(A\)-vertices are absent from \(T\) and inactive \(B\)-vertices are absent from \(U\). All target equalities \(t_i(\pi)=h_i\) are therefore realized.

Thus
\[
a+t(\pi)=\alpha\mathbf1_A+\beta\mathbf1_B
=M(\alpha e_u+\beta e_t).
\]
Choose root \(x=\alpha e_u+\beta e_t\). The edge-color formula (4) yields
\[
a+Mx+t(\pi)=0,
\]
so the full path from \(x\) in direction order \(\pi\) is monochromatic. The possible roots form the stated four-element set. \(\square\)

**Corollary (affine gap reduced to intermediate ranks).** A zero-diagonal row-odd binary matrix has rank at least two: if it had rank one, all nonzero odd rows would coincide, and the zero diagonal would force their common row to vanish. Combining Theorems 4 and 7, every antipodally odd affine cube-edge coloring is solved when
\[
\operatorname{rk}M=2\quad\text{or}\quad \operatorname{rk}M\ge n-2.
\]
The first potentially unresolved interaction ranks are \(3\le\operatorname{rk}M\le n-3\), beginning at dimension \(n=6\). In particular all affine antipodally odd cube-edge colorings in dimensions \(n\le5\) are covered by theorems in this subsection.

**Structural interpretation.** A rank-two odd interaction matrix forces a bipartite two-row-type dependence system. The four-block permutation (19) is an explicit resource-basis gallery that solves the root syndrome. It complements the high-rank quotient approach and applies in arbitrarily large dimensions with corank \(n-2\).

### Triangle–square rigidity of canonical Hamming resource matroids

Let \(G=\square_{i=1}^k K_{E_i}\) be a finite Cartesian product of nontrivial complete graphs, with \(|E_i|=m_i\ge2\). Write \(A_i\subseteq E(G)\) for the graph edges changing coordinate \(i\), and \(d=\sum_i(m_i-1)\). A **Cartesian square** is a four-cycle obtained by changing two different coordinates, and a **fiber triangle** is a three-cycle obtained by changing one coordinate. A matroid \(N\) on the graph-edge ground set \(E(G)\) is said to have **local resource compatibility** if:

(S) every graph vertex star \(\delta_G(x)\) is independent in \(N\);

(T) every fiber triangle is dependent in \(N\);

(P) the two opposite graph edges of each Cartesian square are parallel elements of \(N\).

These axioms refer only to the graph's intrinsic local geometry and the circuit/independence structure of \(N\). No representation, spectral projection, orientation, or edge coloring is assumed.

For the product \(G\), define \(R(G)\) to be the matroid on \(E(G)\) obtained by giving each edge \(e\in A_i\), joining symbols \(a,b\in E_i\), the graphic resource label \((i,\{a,b\})\). On the set of distinct labels the matroid is
\[
R_0(G)=\bigoplus_{i=1}^k M(K_{E_i});
\tag{1}
\]
the matroid \(R(G)\) is its parallel extension in which different graph edges with a common label are parallel.

**Theorem 1 (local resource rigidity).** A matroid \(N\) on \(E(G)\) satisfies (S), (T), and (P) if and only if
\[
\boxed{N=R(G).}
\tag{2}
\]
In particular, the three local matroid axioms determine the complete independence system, and
\[
\boxed{\operatorname{rk}N=\sum_{i=1}^k(m_i-1)=\deg G.}
\tag{3}
\]
Every graph cycle is then \(N\)-dependent, and every resource-independent graph walk has distinct vertices.

*Proof.* Fix a vertex \(o=(o_1,\ldots,o_k)\) of \(G\). For each factor \(i\), let \(B_i\) be the \(m_i-1\) edges incident with \(o\) that change coordinate \(i\), and put \(B=\bigcup_i B_i=\delta_G(o)\). By (S), \(B\) is independent.

First consider an arbitrary edge of type \(i\), changing the two symbols \(a,b\in E_i\), in a fiber whose other coordinates need not agree with those of \(o\). Change those other coordinates one at a time until the fiber coincides with the fiber of \(o\). At every change the edge is opposite a corresponding edge in a Cartesian square. By (P), its resource element is parallel to the corresponding element in the next fiber. Hence it is parallel to the edge \(e^i_{ab}\) of type \(i\) in the reference fiber through \(o\).

If \(a=o_i\) or \(b=o_i\), the element \(e^i_{ab}\) belongs to \(B_i\). Otherwise the edges \(e^i_{o_i a}, e^i_{o_i b},e^i_{ab}\) form a fiber triangle. By (T) its three elements are dependent, and by (S) each pair is independent since any pair shares a graph vertex. Thus the triangle is a three-element circuit, giving
\[
e^i_{ab}\in\operatorname{cl}_N
\{e^i_{o_i a},e^i_{o_i b}\}
\subseteq\operatorname{cl}_N(B_i).
\tag{4}
\]
Together with opposite-edge parallel transport this proves
\[
A_i\subseteq\operatorname{cl}_N(B_i)
\qquad\text{for every }i.
\tag{5}
\]
The \(B_i\)'s are disjoint subsets of the independent set \(B\), so \(r_N(A_i)=|B_i|=m_i-1\), while \(B\) spans all of \(E(G)\). Therefore
\[
r_N(E(G))=|B|=\sum_i r_N(A_i).
\tag{6}
\]
Rank additivity across the partition \(E(G)=\bigsqcup_i A_i\) implies
\[
N=\bigoplus_i N|A_i.
\tag{7}
\]

It remains to determine the single-factor restriction. By (P), all copies of a given edge \(\{a,b\}\) in distinct fibers are parallel, and every such parallel class contains the reference-fiber edge \(e^i_{ab}\). Consider the induced restriction \(N_i\) to the reference-fiber edges of \(K_{E_i}\). Every vertex star in \(K_{E_i}\) is independent by (S), and every triangle is a three-element circuit by (S) and (T).

We claim that \(N_i=M(K_{E_i})\). Every graph spanning tree \(T\) of \(K_{E_i}\) can be turned into the star at \(o_i\) through successive **triangle pivots** that preserve matroid span. Root \(T\) at \(o_i\). Whenever a vertex \(v\) has depth at least two, let \(u\) be its parent and \(p\) the parent of \(u\). Replace the tree edge \(uv\) by the complete-graph edge \(pv\). The result is another spanning tree with smaller total depth, and the triangle \(pu,uv,pv\) is a three-element circuit. Because \(pu\) remains in the tree, the outgoing and incoming edges lie in each other's closure together with \(pu\), so the two spanning-tree edge sets have the same closure and rank. Repeating the operation eventually yields the star at \(o_i\), which is independent of rank \(m_i-1\). Thus **every spanning tree has rank \(m_i-1\) and is independent**, and every graph forest, being extendible to a spanning tree, is independent in \(N_i\).

Conversely, take any graph cycle \(C\) of \(K_{E_i}\), with vertex set \(S\), and choose \(z\in S\). Its star edges \(\{zv:v\in S\setminus\{z\}\}\) form an independent family of \(|S|-1\) elements. Every edge \(uv\) of the cycle not incident with \(z\) belongs to the closure of \(zu,zv\) by the triangular circuit; edges incident with \(z\) already belong to the star. Hence the \(|S|\) edges of \(C\) have rank at most \(|S|-1\), so \(C\) is dependent. Consequently the independent sets of \(N_i\) are precisely the graph forests, proving \(N_i=M(K_{E_i})\).

Equations (7) and the parallel-class description now give \(N=R(G)\). Conversely, in \(R(G)\) every graph vertex star uses distinct edges of the factor-graphic root stars, and their union is independent in the direct sum; any triangle in a factor is a graphic cycle; and opposite Cartesian-square edges share the same factor and unordered pair of symbols, hence are parallel. Thus \(R(G)\) satisfies (S), (T), and (P), proving (2).

Finally every closed graph walk projects in every coordinate to a closed walk of the corresponding complete graph. If the original walk is nonempty, some coordinate projection is nontrivial; its multiset of graphic resource labels contains a repeated edge or a cycle, and so is dependent. The original edge set is dependent in \(R(G)\). In particular a resource-independent walk cannot repeat a vertex. \(\square\)

**Corollary 2 (intrinsic matroidal unification).** For
\[
M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2},
\qquad M_{\rm bd}=U_{2,n},
\tag{8}
\]
the connected-component rank-one reduction \(M^\flat\) and its basis graph \(G=\Gamma(M^\flat)\) recover the two canonical root graphs \(Q_n\) and \(K_n\). Theorem 1 uniquely determines their resource matroids from vertex-star independence, triangle dependence, and Cartesian-square parallelism:
\[
R(Q_n)=\text{coordinate-direction partition matroid on cube edges},
\quad
R(K_n)=M(K_n).
\tag{9}
\]
Thus both resource-independence notions have a common choice-free characterization using ordinary matroid circuits and the local graph structure. The turn bits and global involution are additional data that remain necessary for the colored path assertion.

**Proposition 3 (logical sharpness of the three axioms).** Each hypothesis (S), (T), and (P) is needed for uniqueness.

- Without (S), take \(G=K_3\), and put the rank-one uniform matroid \(U_{1,3}\) on its graph edges. Its triangle is dependent, and (P) is vacuous, while the canonical resource is \(M(K_3)=U_{2,3}\).
- Without (T), take \(G=K_3\) and the free rank-three matroid on its graph edges. Every star is independent and (P) is vacuous, but the canonical triangle circuit disappears.
- Without (P), take \(G=Q_2=C_4\) and \(N=U_{2,4}\) on its four graph edges. Every two-edge star is independent, and (T) is vacuous; the four-cycle is dependent, but opposite edges are independent rather than parallel. The canonical resource instead is \(U_{1,2}\oplus U_{1,2}\).

These examples also show that star independence and graph-cycle dependence alone do not determine the cube resource matroid: the commuting-square condition (P) carries essential information.

**Interpretation.** The rank-one reduction of the source matroid supplies the common Hamming root geometry. Theorem 1 recovers the full resource matroid solely from its local triangle/square behavior, with no spectral or vector choice. Independent-star terminal arguments therefore have a canonical combinatorial foundation in both source models. The missing step toward the full NORI1 statement is a global antipodal rank-saturation argument for arbitrary edge colorings; Theorem 1 isolates its resource geometry from the unconstrained coloring problem.

### Commuting-turn cohomology and intrinsic antipodal holonomy

Let \(G=\square_{i=1}^k K_{E_i}\), where \(k\ge2\) and \(|E_i|\ge2\). The **commuting-turn graph** \(T(G)\) is the following ordinary undirected graph:
- its vertices are the graph edges \(e\in E(G)\);
- \(e,f\) are adjacent in \(T(G)\) if they are distinct incident edges of \(G\) which change *different* Cartesian coordinates.

Equivalently, their ordered two-edge turn \((u,v,w)\) has nonadjacent outside endpoints \(u,w\). A binary value on each edge of \(T(G)\) is thus an assignment to the underlying *unoriented* commuting turns of \(G\).

**Lemma 1 (connectivity).** If \(k\ge2\), the graph \(T(G)\) is connected.

*Proof.* The line graph \(L(G)\) is connected since \(G\) is connected. Every adjacency \(ef\) in \(L(G)\) between edges of different Cartesian factors is also an edge of \(T(G)\). If \(e,f\) are incident at \(v\) and change the same factor \(i\), choose any edge \(g\) incident at \(v\) changing a different factor \(j\ne i\). Then \(e,g,f\) is a two-edge walk in \(T(G)\). Thus every line-graph adjacency can be replaced by a \(T(G)\)-walk of length at most two, proving connectivity. \(\square\)

**Theorem 2 (choice-free reconstruction of edge colors from commuting turns).** Let \(B:E(T(G))\to\mathbb F_2\). The following are equivalent:

(i) for every cycle \(C\) of \(T(G)\), \(\sum_{t\in C}B(t)=0\);

(ii) there exists \(c:E(G)\to\mathbb F_2\) such that
\[
B(\{e,f\})=c(e)+c(f)
\quad\text{for every }\{e,f\}\in E(T(G)).
\tag{1}
\]

When these conditions hold, \(c\) is unique up to simultaneous complementation on all edges of \(G\). In particular, for any graph edges \(e,f\), the quantity
\[
\delta_B(e,f)=\sum_{t\in P}B(t)
\tag{2}
\]
is independent of the choice of \(T(G)\)-path \(P:e\leadsto f\), and satisfies \(\delta_B(e,f)=c(e)+c(f)\).

*Proof.* Under (ii), the sum around every cycle telescopes to zero. Conversely, fix \(e_0\in E(G)=V(T(G))\), set \(c(e_0)=0\), and for any \(e\) define \(c(e)\) to be the sum of \(B\) along a \(T(G)\)-path from \(e_0\) to \(e\). Condition (i) makes this path independent, and adding the values at adjacent vertices gives (1). If \(c'\) also satisfies (1), then \(c+c'\) is constant along every edge of the connected graph \(T(G)\), so it is globally constant. Equation (2) follows from the same telescoping argument. \(\square\)

Let \(\tau\) be any involutive automorphism of \(G\) preserving the Cartesian factor directions, such as the canonical central polarity determined by the two-element components of a partition matroid. It acts on \(T(G)\). Say \(B\) is \(\tau\)-invariant if \(B(\tau t)=B(t)\).

**Theorem 3 (intrinsic oddness as a path integral).** Suppose \(B\) satisfies Theorem 2 and is \(\tau\)-invariant. Then there exists one bit \(\omega_\tau(B)\in\mathbb F_2\), independent of the graph edge \(e\), such that
\[
\boxed{\omega_\tau(B)=\delta_B(e,\tau e)
=c(e)+c(\tau e).}
\tag{3}
\]
It is independent of the choice of the reconstructed edge coloring \(c\). In particular,
\[
\boxed{\omega_\tau(B)=1
\quad\Longleftrightarrow\quad
c(\tau e)=1-c(e)\ \text{for all }e\in E(G).}
\tag{4}
\]

*Proof.* Let \(h(e)=c(e)+c(\tau e)\). For adjacent \(e,f\) in \(T(G)\),
\[
h(e)+h(f)
=B(\{e,f\})+B(\{\tau e,\tau f\})=0
\]
by invariance. Connectivity of \(T(G)\) makes \(h\) constant. By Theorem 2 this constant equals the path integral \(\delta_B(e,\tau e)\). Replacing \(c\) by \(c+1\) leaves \(h\) unchanged. The equivalence (4) follows. \(\square\)

For a nontrivial canonical polarity \(\eta\) involving at least two two-element factors, \(\eta\) acts freely on \(E(G)\). The class \(\omega_\eta(B)=1\) is therefore possible: assign arbitrary complementary colors on the two-member orbits of \(\eta\), and construct \(B\) using (1). Formula (3) recovers the familiar nontrivial deck parity entirely from commuting-turn data, without introducing a separate chosen edge coloring.

#### A graph-and-matroid intrinsic turn system

For \(k\ge2\), equip every ordered nonbacktracking turn \((u,v,w)\) with a bit \(b(u,v,w)\) subject to:

(C1) if \(u,w\) are nonadjacent, then \(b(u,v,w)=b(w,v,u)\); these common values form \(B:E(T(G))\to\mathbb F_2\) satisfying the cycle condition of Theorem 2;

(C2) if \(u,w\) are adjacent, then \(b(u,v,w)+b(w,v,u)=1\), with no other restrictions on these triangular comparisons;

(C3) when the canonical polarity \(\eta\) is nontrivial, \(B\) is \(\eta\)-invariant and \(\omega_\eta(B)=1\).

Define an **accepted resource gallery** to be a path \(P=(v_0,\ldots,v_\ell)\) whose graph edges are independent in the uniquely determined triangle–square resource matroid \(R(G)\) of the preceding Article XI Subsection and for which, at every internal vertex, both
\[
b(v_{j-1},v_j,v_{j+1})=0,\qquad
\delta_B(v_{j-1}v_j,v_jv_{j+1})=0.
\tag{5}
\]
The second constraint is intrinsic by Theorem 2. On nontriangular turns, the two constraints coincide.

For the one-factor case \(G=K_m\), the commuting-turn graph has no edges. Use instead the intrinsic triangular rule \(b(a,v,c)+b(c,v,a)=1\) and define an accepted gallery using the first constraint of (5) alone. This is the boundary-tournament specialization and involves no edge-color potential.

**Corollary 4 (faithful decoding of the canonical examples).**

(a) For \(M=\bigoplus_{i=1}^nU_{1,2}\), \(n\ge2\), its rank-one root is \(G=Q_n\) and its canonical polarity is cube complementation. Every nonbacktracking turn is commuting, so the turn bit is \(\delta_B(e,f)\). A turn system satisfying (C1)--(C3) is equivalent, up to simultaneous exchange of the color names, to an arbitrary antipodally odd binary coloring of undirected cube edges. The accepted resource galleries are its monochromatic coordinate-distinct geodesics. In particular, a gallery of length \(n\) is a monochromatic antipodal geodesic.

(b) For \(M=U_{2,n}\), \(n\ge3\), the root is \(G=K_n\), and the canonical polarity is the identity. Every nonbacktracking turn is triangular. The turn rule is precisely an arbitrary reversal-odd boundary 3-tournament on distinct ordered triples, and the accepted resource galleries are its monochromatic vertex-simple tight paths.

*Proof.* Part (a) follows from Theorems 2--3 and the triangle–square rigidity characterization \(R(Q_n)\) as the coordinate-direction partition matroid. Part (b) follows from the absence of commuting turns in a complete graph and \(R(K_n)=M(K_n)\), whose independent paths are precisely the vertex-simple paths in the original complete graph. \(\square\)

**Corollary 5 (a turn-only unified conjecture).** Let \(\mathcal C_{\rm can}\) be the intrinsic partition-matroid class whose number \(s\) of two-element connected components satisfies \(s=0\) or \(s\ge2\). Let \(G=\Gamma(M^\flat)\), \(k\) be its Cartesian-factor count, and \(d=\operatorname{rk}R(G)\). Use the turn-only systems (C1)--(C3) for \(k\ge2\) and the unrestricted triangular turn system for \(k=1\). The single quantitative conjecture
\[
\boxed{
L\ge\max\left\{
\left\lceil\frac{k}{2}\right\rceil,
\left\lceil\frac{\sqrt d}{2}\right\rceil,
s
\right\}
}
\tag{6}
\]
for an accepted resource gallery is equivalent to NORI1.

*Proof.* The factor-count bound \(\lceil k/2\rceil\) is already established for arbitrary edge colors on Hamming products by the monochromatic factorwise transfer theorem in Article XI. The resource-rank bound \(\lceil\sqrt d/2\rceil\) is established by the cycle-dominating resource-matroid terminal theorem. Both apply to the reconstructed \(c\) by Theorem 2, and for \(k=1\) the rank theorem applies directly to the unrestricted local tournament. If \(s\ge2\), the canonical polarity acts by simultaneous complementation of all binary factors and fixes the remaining factors. Under NORI1, restrict the reconstructed odd coloring to a cube obtained by retaining those binary factors and fixing the others. A monochromatic \(s\)-edge antipodal geodesic on that slice is resource-independent and accepted, giving the third bound. Conversely the pure cube case has \(k=s=d=n\), so (6) forces a monochromatic antipodal geodesic and hence NORI1. \(\square\)

The reconstructed color bit is a gauge choice: changing it globally affects none of the turn data, holonomy, or accepted galleries. Thus both the resource matroid and the antipodal color law can be specified using intrinsic circuit geometry and a binary turn cocycle. The nontrivial remaining mathematical task is the full-rank path-existence theorem for such unrestricted polarized turn systems.

#### Dimension of the intrinsic odd-holonomy space

**Theorem 6 (two cosets of invariant commuting-turn cuts).** Let \(\tau\) be a fixed-point-free involution on the vertices of the connected graph \(T(G)\), induced by a factor-preserving graph involution of \(G\). Put \(2m=|V(T(G))|=|E(G)|\), and let \(\mathcal B^\tau\) be the vector space of \(\tau\)-invariant edge functions \(B:E(T(G))\to\mathbb F_2\) whose sum around every graph cycle vanishes. Then
\[
\boxed{\dim_{\mathbb F_2}\mathcal B^\tau=m.}
\tag{7}
\]
The map \(B\mapsto\omega_\tau(B)\) is a surjective linear functional on this space. Its two fibers have
\[
\boxed{|\{B\in\mathcal B^\tau:\omega_\tau(B)=\epsilon\}|
=2^{m-1}\quad(\epsilon\in\mathbb F_2).}
\tag{8}
\]
In particular, antipodally odd edge colorings modulo simultaneous exchange of the two colors correspond bijectively to the nonzero-holonomy fiber.

*Proof.* By Theorem 2, the cycle-zero cochains on \(T(G)\) are precisely the image of the graph coboundary map \(d:C^0(T(G);\mathbb F_2)\to C^1(T(G);\mathbb F_2)\), whose kernel consists of the two constant vertex functions. By Theorem 3, \(dc\) is \(\tau\)-invariant precisely when \(c+\tau c=\alpha\mathbf1\) for some \(\alpha\in\mathbb F_2\), and then \(\omega_\tau(dc)=\alpha\). On each of the \(m\) two-element vertex orbits of \(\tau\), choose the value of \(c\) at one representative freely; the other value is forced to be \(c+\alpha\). Thus all such potentials \(c\), allowing either \(\alpha\), form an \((m+1)\)-dimensional vector space. Quotienting by the one-dimensional constant kernel of \(d\) gives dimension \(m\), proving (7). Both values of \(\alpha\) occur (choose representative values all zero, and then choose either value of \(\alpha\)), so \(\omega_\tau\) is surjective, with kernel of dimension \(m-1\). This proves (8). \(\square\)

For the canonical cube \(Q_n\), \(n\ge2\), the commuting-turn graph has \(|E(Q_n)|=n2^{n-1}\) vertices and its antipodal involution pairs them freely, so \(m=n2^{n-2}\). Thus the entire unrestricted space of antipodally odd edge colorings, modulo exchanging the colors, is a single nonzero-holonomy coset of cardinality \(2^{n2^{n-2}-1}\). No regularity restriction is imposed on the colorings.

### Universal twisted-gallery switch enumeration and degree mixing

Let \(n\ge2\) and let \(c:E(Q_n)\to\mathbb F_2\) be any undirected edge coloring satisfying \(c(\bar e)=1-c(e)\). For the \(T=2^n n!\) rooted directed full geodesics \((x,\pi)\), let \(S_j\) count those with \(j\) changes in their length-\(n\) edge-color word. There is no affine or other regularity assumption.

**Theorem 1 (switch spectrum under rooted rotations).** For \(2r+1\le n\),
\[
\boxed{(2r+1)S_{2r+1}=(n-2r-1)S_{2r}.}\tag{1}
\]
In particular
\[
\boxed{S_1=(n-1)S_0.}\tag{2}
\]
More strongly, there are integers \(A_{2r+1}\ge0\) such that
\[
\boxed{S_{2r}=2(2r+1)A_{2r+1},\quad
S_{2r+1}=2(n-2r-1)A_{2r+1}.}\tag{3}
\]

**Proof.** If a path \(P=(x;i_1,\dots,i_n)\) has color word \(w=(w_1,\dots,w_n)\), its rooted cyclic rotation
\[
R(P)=(x^{i_1};i_2,\dots,i_n,i_1)
\]
has color word
\[
\boxed{w(R(P))=(w_2,\dots,w_n,1-w_1).}\tag{4}
\]
The last new edge is antipodal to the original first edge. The action \(R\) has orbit size \(2n\): before \(n\) steps the coordinate permutation has not returned, and after \(n\) steps the root becomes its antipode. The associated length-\(2n\) circular word is \(w_1,\dots,w_n,1-w_1,\dots,1-w_n\). Define its half-circle change count
\[
k(P)=\sum_{i=1}^{n-1}[w_i\ne w_{i+1}]+[w_n\ne1-w_1].
\]
It is odd, because its transitions change the initial bit to its complement. It is invariant under \(R\). In an orbit with \(k=2r+1\), every rooted linear word omits one of the \(n\) comparisons of a twisted half-circle. If the omitted comparison is a change, the linear word has \(k-1=2r\) changes; otherwise it has \(k=2r+1\). Over all \(2n\) rotations, \(2k\) omit a change and \(2(n-k)\) omit an equality. Thus each orbit contributes \(2(2r+1)\) paths of type \(2r\) and \(2(n-2r-1)\) paths of type \(2r+1\). Summation gives (1)--(3). \(\square\)

**Theorem 2 (local color mixing determines the first cyclic moment).** Put \(a(v)=\deg_{c=0}(v)\), the number of zero-color edges incident with vertex \(v\). For uniformly random rooted full geodesic \(P\),
\[
\boxed{\mathbb E k(P)=\frac{2}{2^n(n-1)}
\sum_{v\in Q_n}a(v)(n-a(v)).}\tag{5}
\]

**Proof.** Each of the \(n-1\) internal transitions of the full geodesic is an ordered pair of distinct directions at a uniformly random cube vertex. The closing comparison is between the final edge and the antipodal image of the initial edge at the terminal vertex; its vertex and ordered direction pair have the same uniform law. At a vertex \(v\), the proportion of mixed-color ordered edge pairs is
\[
\frac{2a(v)(n-a(v))}{n(n-1)}.
\]
Summing the \(n\) cyclic comparisons and averaging proves (5). \(\square\)

**Corollary 3 (quantitative existence criterion).** For every antipodally odd coloring,
\[
\boxed{S_0\ge2^{n-1}(n-1)!\,
\max\left\{0,\ 3-\frac{2}{2^n(n-1)}
\sum_v a(v)(n-a(v))\right\}.}\tag{6}
\]
In particular, if the mean of \(a(v)(n-a(v))\) over cube vertices is less than \(3(n-1)/2\), a monochromatic antipodal geodesic exists.

**Proof.** Let \(p\) be the fraction of rotation orbits with \(k=1\). All other odd switch counts are at least three, hence \(\mathbb E k\ge p+3(1-p)\) and \(p\ge(3-\mathbb E k)/2\). Each orbit has \(2n\) rooted paths; a \(k=1\) orbit has two monochromatic paths, and no other orbit has any. Thus \(S_0=(T/n)p=2^n(n-1)!p\). Substitute (5). \(\square\)

**Corollary 4 (sharp low-dimensional witness multiplicities).** Every antipodally odd coloring has
\[
\boxed{S_0(Q_3)\ge8,\qquad S_0(Q_4)\ge16.}\tag{7}
\]
Both bounds are attained. In \(Q_4\), equality holds if and only if each vertex has two edges of each color.

**Proof.** For \(n=3\), integer \(a\) satisfies \(a(3-a)\le2\), so \(\mathbb E k\le2\); (6) gives \(S_0\ge8\). The coloring
\[
c_1=x_2,\quad c_2=x_1,\quad c_3=1+x_1
\]
is antipodally odd, and both colors occur at every vertex, making \(\mathbb E k=2\). Since the twisted count \(k\in\{1,3\}\), the proof of (6) gives \(S_0=8\).

For \(n=4\), \(a(4-a)\le4\) gives \(\mathbb E k\le8/3\), and (6) yields \(S_0\ge16\). The coloring
\[
c_1=x_2,\quad c_2=x_1,\quad c_3=1+x_2,\quad c_4=1+x_1
\]
is antipodally odd and has two colors of each type in every vertex star. Its cyclic counts likewise belong to \(\{1,3\}\), so it attains \(S_0=16\). Conversely, equality \(S_0=16\) forces the mean in (5) to be \(8/3\); hence every vertex maximizes \(a(4-a)\), meaning \(a(v)=2\) for all \(v\). \(\square\)

**Corollary 5 (rigidity of a putative \(Q_5\) counterexample).** If an antipodally odd coloring of \(Q_5\) had no monochromatic antipodal geodesic, then every vertex would have two or three edges of color zero, and **every** rooted full geodesic would have cyclic switch number \(k=3\). Its ordinary switch word would always have two or three changes, with \(3S_3=2S_2\).

**Proof.** Since \(a(5-a)\le6\), (5) gives \(\mathbb E k\le3\). If \(S_0=0\), Theorem 1 excludes any \(k=1\) rotation orbit, so \(k\ge3\) everywhere. Equality of the upper and lower means forces \(a(v)\in\{2,3\}\) at every vertex and \(k=3\) throughout. Equation (1) for \(r=1\) completes the statement. \(\square\)

**Scope.** These theorems hold for *every* legal antipodally odd cube-edge coloring, unlike affine-subclass results. The odd-switch rotation is established elsewhere in Article XI; Theorem 1 upgrades it to full integer-valued switch-spectrum relations, and Theorem 2 connects those counts to a simple vertex-degree observable. The sharp multiplicity bound settles dimensions 3 and 4 by a new count and yields explicit sufficient conditions in all dimensions. For large \(n\), the first-moment threshold is not sufficient near balanced vertex stars: one would need further moments or square-turn correlations to force \(k=1\). No unrestricted NORI1 proof follows from the displayed bounds alone.

#### Theorem 6 (rank-one antipodal completion and facet enumeration)

Let \(M_{n-1}(c)\) denote the number of **directed** monochromatic geodesics of length \(n-1\) in \(Q_n\), counted with their initial vertices and their ordered sets of \(n-1\) distinct coordinate directions. Then
\[
\boxed{M_{n-1}(c)=2S_0(c),\qquad
S_1(c)=\frac{n-1}{2}M_{n-1}(c).}
\tag{10}
\]
Moreover, writing \(F_{j,0}=\{x\in Q_n:x_j=0\}\), and letting \(B(F_{j,0})\) count all monochromatic directed full geodesics within the \((n-1)\)-dimensional face \(F_{j,0}\) under the inherited coloring, one has
\[
\boxed{S_0(c)=\sum_{j=1}^n B(F_{j,0}).}
\tag{11}
\]

**Proof.** Let \(P\) be a monochromatic geodesic of length \(n-1\), from \(x\) to \(y\), missing direction \(j\). Then \(y=\bar x^{j}\). The \(j\)-edge at the start, \(xx^{j}\), and the \(j\)-edge at the end, \(yy^{j}\), are antipodal images of each other. By the oddness condition, their colors are opposite. Precisely one of them agrees with the common color of \(P\), allowing one and only one monochromatic full-geodesic extension by adding direction \(j\) at the appropriate end. Conversely, deleting the first or the last edge of any monochromatic full geodesic produces two different directed \((n-1)\)-edge monochromatic geodesics, each of which is uniquely extended back to the original full geodesic. This is a two-to-one correspondence, proving the first identity in (10). The second identity follows from (2).

Every \((n-1)\)-edge cube geodesic lies in precisely one coordinate facet, determined by its omitted direction \(j\) and the fixed \(j\)-bit of its vertices. The cube antipode maps the facet \(F_{j,0}\) bijectively to its opposite facet \(F_{j,1}\), reversing all edge colors; hence their monochromatic spanning-geodesic counts coincide. Therefore
\[
M_{n-1}(c)=\sum_{j=1}^n \bigl(B(F_{j,0})+B(F_{j,1})\bigr)
=2\sum_{j=1}^n B(F_{j,0}).
\]
Combine with \(M_{n-1}(c)=2S_0(c)\) to obtain (11). \(\square\)

This count identity makes precise the distinction between **partial witness growth** and **rank saturation**. An \((n-1)\)-resource monochromatic path extends automatically, thanks to the antipodal pair of final resource ports. However, a path of only \(\sqrt n\), \(n/2\), or \(n-2\) independent resources need not have such an antipodal pair at its endpoints. An unrestricted proof via the common matroid terminal theorem must therefore either grow witnesses up to rank \(n-1\) or find an analogue of the complementary-endport completion mechanism at larger resource defect. The reversal-odd boundary tournament does not automatically possess this two-end extension rule, so the possible unification must encode different seam arities without discarding the resource constraints.

#### Theorem 7 (second-moment certificate for arbitrary antipodally odd colorings)

Let \(n\ge3\), let \(K\) be the largest odd integer at most \(n\), and regard \(k(P)\in\{1,3,\ldots,K\}\) as a random variable over uniformly chosen rooted full geodesics. Put \(m_1=\mathbb E k\), \(m_2=\mathbb E k^2\). Then
\[
\boxed{
S_0\ge
2^{n-1}(n-1)!\,
\max\left\{0,\frac{m_2-(K+3)m_1+3K}{K-1}\right\}.}
\tag{12}
\]
This is a second-moment certificate independent of any affine or regularity condition.

**Proof.** The polynomial \(g(k)=(k-3)(K-k)\) vanishes at \(k=3,K\), is nonnegative at every admissible odd \(k\ge3\), and has \(g(1)=-2(K-1)\). If \(p\) is the fraction of rotation orbits with \(k=1\), it follows that
\[
\mathbb E g(k)\ge -2(K-1)p.
\]
But \(-\mathbb E g(k)=m_2-(K+3)m_1+3K\). As proved in Corollary 3, \(S_0=2^n(n-1)!p\). The inequality follows. \(\square\)

**Corollary 8 (a variance characterization of the balanced \(Q_5\) case).** Suppose \(n=5\) and every vertex star has zero-color degree two or three. Then \(m_1=3\), and
\[
\boxed{S_0(c)=96\,\operatorname{Var}(k).}
\tag{13}
\]
Consequently in this balanced-star regime, a monochromatic antipodal geodesic exists if and only if the cyclic switch number is not constant over the rooted full geodesics.

**Proof.** By (5), balanced stars give \(m_1=3\). The cyclic switch count can be \(1,3,5\). Its probabilities at 1 and 5 are equal because their contributions to \(m_1-3\) are opposite. If that common probability is \(p\), then \(\operatorname{Var}(k)=4p+4p=8p\), while \(S_0=2^5\cdot4!p=768p\). Therefore \(S_0=96\operatorname{Var}(k)\). \(\square\)

This suggests a possible unrestricted strategy beyond average-degree bounds: estimate cyclic-switch variance (or suitable higher positive polynomial moments) from square-turn correlations and rooted gallery exchanges. The first moment depends only on the vertex color degrees; the second moment detects correlations across turns and may remain informative when all vertex stars are perfectly balanced. Formula (13) is a sharp manifestation in dimension five. It is not, by itself, a proof that such variance must be positive in every balanced coloring.

### Cyclic switch calculus for cube galleries and arbitrary boundary tournaments

#### A binary local system and its cut identity

Let \(m\ge3\), \(h\in\{1,\ldots,m\}\), and \(w_i\in\mathbb F_2\), indexed by integers, satisfy
\[
w_{i+m}=w_i+\eta,\qquad\eta\in\mathbb F_2.
\]
Put \(d_i=w_i+w_{i+1}\pmod2\), and let \(D=\sum_{i=0}^{m-1}d_i\) be an integer sum. Then \(d\) is \(m\)-periodic and
\[
D\equiv\eta\pmod2.
\]
A retained switch-window with seam width \(h\) has cost
\[
J_s=D-\sum_{j=s}^{s+h-1}d_j.
\]
**Lemma 1 (cyclic cut transfer).** The cut costs obey
\[
\boxed{\sum_{s=0}^{m-1}J_s=(m-h)D,\qquad
\sum_{s=0}^{m-1}z^{J_s}
=\sum_{s=0}^{m-1}z^{D-\sum_{j=s}^{s+h-1}d_j}.}
\]
In particular, a cut with cost at most one exists if and only if one block of \(h\) consecutive comparisons contains at least \(D-1\) changes.

*Proof.* The switch sequence is periodic because the twist cancels when taking adjacent differences. Its cyclic XOR telescopes to \(\eta\), proving parity. Each comparison belongs to \(h\) deleted blocks and \(m-h\) retained blocks, proving the sum formula. The generating-function identity is termwise. \(\square\)

#### Cubical odd-monodromy specialization

Let \(c:E(Q_n)\to\mathbb F_2\) be arbitrary except for \(c(\bar e)=1-c(e)\). Moving the first step of a rooted full geodesic to its end, while shifting the root over that edge, transforms its color word by
\[
(w_0,\ldots,w_{n-1})\mapsto(w_1,\ldots,w_{n-1},1-w_0).
\]
Therefore \(m=n,\eta=1,h=1\). A rooted rotation orbit has \(2n\) members and contains two lifts of each cyclic cut. If its odd cyclic switch count is \(D\), the orbit has \(2D\) paths with \(D-1\) ordinary switches and \(2(n-D)\) paths with \(D\) switches. The universal switch-spectrum identity from the preceding subsection follows. The presence of a monochromatic full geodesic is equivalent to existence of a rooted cyclic gallery with \(D=1\).

#### Boundary even-monodromy specialization

Let \(V\) be an \(n\)-vertex set, \(n\ge4\), and let \(b(a,v,c)\) be an arbitrary reversal-odd boundary coloring:
\[
b(c,v,a)=1-b(a,v,c).
\]
Take any oriented Hamiltonian cycle \(C=(v_0,\ldots,v_{n-1})\), modulo rotations but not reversal, and define, with subscripts modulo \(n\),
\[
t_i=b(v_{i-1},v_i,v_{i+1}),\qquad
d_i=t_i+t_{i+1}\pmod2,\qquad D(C)=\sum_i d_i.
\]
The word \(t\) is \(n\)-periodic, so \(D(C)\) is even. Open the cycle into the Hamiltonian path
\(P_s=(v_s,v_{s+1},\ldots,v_{s+n-1})\).
The path's turn colors are \(t_{s+1},\ldots,t_{s+n-2}\); their switch count is
\[
\boxed{\sigma(P_s)=D(C)-(d_{s-2}+d_{s-1}+d_s).}
\tag{1}
\]
Thus the seam width is \(h=3\), rather than the cubical \(h=1\).

**Theorem 2 (boundary Hamiltonian cycle-window theorem).** Each oriented Hamiltonian cycle supplies \(n\) distinct Hamiltonian paths, and
\[
\boxed{\sum_{s=0}^{n-1}\sigma(P_s)=(n-3)D(C).}
\tag{2}
\]
The number of cyclic cuts with at most one switch equals the number of cyclic length-three blocks of \(d(C)\) containing at least \(D(C)-1\) ones. Hence:

- For \(D(C)=0\), all \(n\) cuts give monochromatic Hamiltonian paths.
- For \(D(C)=2\), at least four cuts give Hamiltonian paths with at most one switch.
- For \(D(C)=4\), some cut works if and only if three consecutive entries of \(d(C)\) are one.
- For \(D(C)\ge6\), no cyclic cut works.

The spanning one-switch Hamiltonian boundary conjecture is consequently equivalent to the existence of a Hamiltonian cycle with \(D(C)\le2\), or one with \(D(C)=4\) and three consecutive changes.

*Proof.* Each permutation of the \(n\) original vertices opens a unique oriented Hamiltonian cycle, obtained by appending its closing edge. Formula (1) omits three consecutive circular comparisons and retains the \(n-3\) internal comparisons. Apply Lemma 1 to obtain (2) and the cut condition. Since \(D\) is even, the four listed cases exhaust the possibilities. For \(D=2\), each of the two changed comparisons belongs to three deleted three-blocks; their combined set contains at least four different blocks. At \(D=4\), deleting at least three changed comparisons requires an all-one three-block; at \(D\ge6\), three deletions cannot leave fewer than three changes. \(\square\)

**Corollary 3 (unconditional spanning one-switch path on five vertices).** Every binary coloring of ordered triples on \(n\le5\) distinct vertices, even without reversal oddness, has a Hamiltonian vertex ordering whose consecutive triple-color word has at most one switch.

*Proof.* For \(n\le4\) there are at most two successive triple colors. At \(n=5\), any cyclic binary five-term turn word has \(D\in\{0,2,4\}\). The first two cases are covered by Theorem 2. In the last case, the cyclic comparison word has four ones and one zero, and therefore three consecutive ones. Theorem 2 applies. \(\square\)

**Theorem 4 (boundary quartet-discrepancy moment).** Let
\[
\beta(b)=\frac1{n(n-1)(n-2)(n-3)}
\sum_{\substack{a,u,v,d\in V\\\mathrm{distinct}}}
\mathbf1_{\{b(a,u,v)\ne b(u,v,d)\}}.
\]
For uniform oriented Hamiltonian cycle \(C\) and uniform Hamiltonian path \(P\),
\[
\boxed{\mathbb E D(C)=n\beta(b),\qquad
\mathbb E\sigma(P)=(n-3)\beta(b).}
\tag{3}
\]
In particular, if \(\beta(b)<4/n\), there is a Hamiltonian path with at most one switch.

*Proof.* Four consecutive vertices in a uniformly random oriented Hamiltonian cycle form a uniformly random ordered quadruple of distinct vertices. Thus each cyclic turn comparison changes color with probability \(\beta(b)\), giving the first equality. Averaging (2) over cycles, whose cuts partition the permutations, gives the second. If the mean cyclic count is below four, some cycle has even count zero or two; apply Theorem 2. \(\square\)

#### Mathematical distinction

Both models encode the turn defects of full-resource galleries as cyclic \(\mathbb F_2\)-differences. An existence witness is a cut whose deleted seam contains nearly all defects. This is a shared statement valid for all legal colorings; no affinity, local transitivity, or special edge order is involved.

The cube has odd monodromy and a one-comparison seam; the boundary has even monodromy and a three-comparison seam. For the former, existence is governed solely by the smallest cyclic change count \(D=1\). For the latter, the relative positions of up to four cyclic changes also matter. Consequently a proof of the boundary conjecture must control clustering or reductions of cyclic turn defects, not just their total. The results give a common analytic mechanism but do not assert that a general unifying existence theorem has been proved.

#### 5. Quantized local exchange curvature

**Lemma 5 (adjacent-exchange Lipschitz bounds).** On the graph of full-resource galleries related by transposing adjacent steps, the cyclic switch count \(D\) changes as follows:

(a) For arbitrary antipodally odd cubical edge colors, transposing two consecutive directions changes \(D\) by an even integer of absolute value at most two.

(b) For arbitrary boundary triple colors, transposing two consecutive vertices in a cyclic Hamiltonian ordering changes \(D\) by an even integer of absolute value at most four.

Both statements hold without assuming the target conjectures.

**Proof.** The cyclic switch count of a binary color word is the number of unequal adjacent colors, including the twisted closing comparison in (a) and the periodic closing comparison in (b). In both cases its parity is preserved under gallery transpositions: odd in (a), even in (b).

In (a), exchanging two consecutive coordinate steps replaces two edges of a single coordinate square; all the other path edges stay unchanged. Thus only two neighboring entries of the length-\(n\) edge-color word can change, affecting at most three consecutive cyclic comparisons. The integer difference of switch counts is even, so its magnitude is at most two.

In (b), swapping two consecutive vertices in the Hamiltonian cycle changes only the four consecutive triple colors whose centers are the swapped vertices or their two immediate neighbors. All other turn colors are unchanged. Therefore at most five cyclic comparisons are affected. The integer difference is even, hence of magnitude at most four. \(\square\)

**Variational consequence.** A gallery minimizing the cyclic switch count is automatically stable under every adjacent exchange. In the cube its local energy increments belong to \(\{0,2\}\), and for boundary Hamiltonian cycles they belong to \(\{0,2,4\}\). To prove the target from such a minimum, one must show that an odd local minimum with \(D\ge3\) (cube), respectively a boundary local minimum outside the \(D\le2\)/clustered-\(D=4\) extraction classes, is impossible or can be escaped by a coordinated sequence of zero-cost exchanges. The support bounds make this a finite-neighborhood curvature problem, not a solution in themselves.


#### Switch signatures as the prescribed covering class

**Theorem 6 (odd vertex labels versus switch cohomology).** Let \(H\) be a finite graph with a fixed-point-free involution \(R\) on vertices and edges, let \(G=H/R\), and let \(\alpha=w_1(H\to G)\in H^1(G;\mathbb F_2)\). An edge signature \(s:E(G)\to\mathbb F_2\) arises from an odd vertex coloring \(c(Rv)=1+c(v)\) by
\[
s([uv])=c(u)+c(v)
\]
if and only if
\[
\boxed{[s]=\alpha.}\tag{6}
\]
For connected \(G\), the coloring is unique up to simultaneous complementation; in general it has one binary choice on each quotient component.

*Proof.* Select one lift \(\widetilde v\) of each quotient vertex. Put \(\eta(vw)=0\) if the lift of \(vw\) from \(\widetilde v\) reaches \(\widetilde w\), and \(\eta(vw)=1\) if it reaches \(R\widetilde w\). This cochain represents \(\alpha\). Writing \(b(v)=c(\widetilde v)\), oddness gives \(s(vw)=\eta(vw)+b(v)+b(w)\), so \([s]=\alpha\). Conversely, if \(s+\eta=\delta b\), assign \(c(\widetilde v)=b(v)\) and \(c(R\widetilde v)=1+b(v)\). These assignments induce \(s\) on every edge orbit. Any two potential choices differ by a locally constant function on \(G\). \(\square\)

**Corollary 7 (legal perturbations are graph cuts).** Two legal signatures on \(G\) differ by a coboundary \(\delta f\), i.e. by toggling all signature edges crossing a vertex cut. Changing just one switch while leaving all others unchanged is legal precisely when the selected edge of \(G\) is a bridge.

*Proof.* Theorem 6 says both signatures lie in the same affine coset \(\alpha+B^1(G;\mathbb F_2)\). A one-edge indicator is a graph coboundary if and only if that edge lies on no graph cycle. \(\square\)

**Theorem 8 (common switch-only encoding for both unrestricted gallery problems).** There are native graphs \(H_\square,H_\partial\) on which the two original reversal-odd bit colorings become odd vertex colorings, and the switches become representatives of the corresponding covering class.

For NORI1, take \(H_\square=L(Q_n)\), whose vertices are cube edges and whose adjacencies are incident pairs of distinct cube edges. Antipodal inversion acts freely. The quotient \(G_\square=L(Q_n)/A\cong L(Q_n/A)\) has vertices representing antipodal pairs of cube edges and edges representing projective turns. The NORI1 conclusion is equivalent to: every edge signature on \(G_\square\) in the class \(\alpha_\square\) admits a dimension-simple projective Petrie loop with precisely **one** active turn.

For ordinary reversal-odd boundary 3-tournaments, take \(H_\partial\) whose vertices are ordered triples \((a,b,c)\) of distinct symbols, with an undirected edge joining \((a,b,c)\) to \((b,c,d)\) for every ordered quadruple of distinct symbols. The involution \(R(a,b,c)=(c,b,a)\) preserves adjacency and reverses transition orientations. The quotient \(G_\partial=H_\partial/R\) has one edge for each reversal-orbit of four-symbol transitions. Every unrestricted odd triple coloring becomes an odd vertex coloring of \(H_\partial\). The boundary conclusion is equivalent to: every signature representing \(\alpha_\partial\) admits a vertex-simple Hamilton triple-overlap path with **at most one** active transition.

Neither \(G_\square\) nor \(G_\partial\) has bridges. In \(G_\square\), each turn belongs to a triangle formed by three edges incident at one projective cube vertex, since \(n\ge3\). In \(G_\partial\), every transition belongs to the four-cycle obtained by rotating its four distinct symbols:
\[
(a,b,c)\to(b,c,d)\to(c,d,a)\to(d,a,b)\to(a,b,c).
\]
Its quotient remains a cycle. Thus no single-switch deletion is legal in either unrestricted class.

*Proof.* Apply Theorem 6 to the graphs and involutions defined above. Cube edge bits become vertex bits of the line graph and their changes occur on turn edges. The closed projective Petrie path represents a nontrivial lift and has an odd number of changes; one change is equivalent, by cyclic root sliding, to a monochromatic antipodal half-geodesic. Consecutive ordered triples of a Hamilton vertex order trace a path in \(H_\partial\), and its changes are the transition signature. The graph-cycle assertions prove the bridge claim. \(\square\)

**Research consequence.** This is one common structural encoding of the two full unrestricted coloring classes; it does **not** yet prove one substantive shared path-existence theorem. Their distinguished complete path families differ. It does correct the natural switch-criticality induction: legal perturbations are whole graph cuts, not deletion of arbitrary isolated turns. The signed-graph class \(\alpha+B^1\), together with the prescribed dimension-simple or vertex-simple path family, is the proper object for cut-critical investigations.
