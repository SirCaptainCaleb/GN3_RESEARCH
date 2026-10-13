# Polarized Hamming turn geometry and a single quantitative NORI1 equivalence

# Polarized Hamming turn geometry and the displacement conjecture

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
