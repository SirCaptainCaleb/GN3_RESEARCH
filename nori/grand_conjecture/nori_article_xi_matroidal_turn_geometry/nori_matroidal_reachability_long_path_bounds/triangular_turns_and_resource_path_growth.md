# Triangular turns and resource-path growth

Let \(G=(V,E)\) be a finite connected simple graph and let \(N\) be a matroid on \(E\) such that
\[
\text{each vertex star }E(v)\text{ is independent in }N,
\qquad
\text{every graph cycle is dependent in }N.\tag{1}
\]
Let \(c:E\to\mathbb F_2\) be an arbitrary edge coloring. Give each nonbacktracking oriented two-edge walk \((u,v,w)\), with \(u\ne w\), a bit \(b(u,v,w)\). Assume
\[
b(u,v,w)=c(uv)+c(vw)\pmod2\qquad\text{if }uw\notin E,\tag{2}
\]
and
\[
b(u,v,w)+b(w,v,u)=1\pmod2\qquad\text{if }uw\in E.\tag{3}
\]
Thus a turn with nonadjacent outside vertices tests agreement of its incident edge colors, whereas a turn belonging to a triangle has an arbitrarily oriented comparison. The two conditions are equivalent to a reversal law
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E\}},
\]
together with the potential condition (2) on nontriangular turns.

Call a vertex-simple path \(P=(v_0,\ldots,v_\ell)\) **accepted** if \(\{v_{i-1}v_i:1\le i\le\ell\}\) is independent in \(N\) and \(b(v_{i-1},v_i,v_{i+1})=0\) for every internal turn.

**Theorem (two-color triangular-turn terminal bound).** Under (1)--(3), there exists an accepted path of at least
\[
\boxed{\ell\ge\frac12\sqrt{\bar d(G)},\qquad \bar d(G)=\frac{2|E|}{|V|}}\tag{4}
\]
edges. Its edge set can be chosen monochromatic under \(c\).

*Proof.* Partition \(E=E_0\sqcup E_1\) by the edge coloring \(c\). At least one color class, say \(E_s\), has at least \(|E|/2\) edges. Hence the spanning monochromatic subgraph \(G_s=(V,E_s)\) has average degree at least \(\bar d(G)/2\). Some nontrivial connected component \(H\) of \(G_s\) has average degree at least \(\bar d(G)/2\).

For every vertex \(v\in V(H)\), define a tournament on the incident edges of \(H\). Given two incident edges \(uv\), \(vw\), if \(u,w\) are adjacent in \(G\), orient their tournament comparison from \(uv\) to \(vw\) when \(b(u,v,w)=0\), and in the opposite direction otherwise. Condition (3) ensures that one orientation is accepted. If \(u,w\) are nonadjacent in \(G\), both edges have color \(s\), so (2) gives
\[
b(u,v,w)=c(uv)+c(vw)=0,
\]
and the reversed turn also has value zero. Either orientation may be chosen in the tournament. Thus **every forward comparison of these vertex-star tournaments is an accepted turn**.

The restriction \(N|E(H)\) has independent vertex stars and dependent graph cycles, by (1). Apply the cycle-dominating resource-matroid terminal-path theorem to \(H\) with the constructed local tournaments. It gives a path with \(N\)-independent edge set, all its turns accepted, and at least
\[
\sqrt{\bar d(H)/2}\ge\sqrt{\bar d(G)/4}
\]
edges. Since the path lies in \(H\subseteq G_s\), all its edges also have color \(s\). \(\square\)

**Corollary (common spectral-root bound).** Let \(G=H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), and let \(N=N_{\rm sp}(G)\) be its canonical second-adjacency-eigenspace edge-difference matroid. Then (1) holds, \(\bar d(G)=k(q-1)\), and every turn system (2)--(3) admits an accepted \(N\)-independent path of at least
\[
\boxed{\frac12\sqrt{k(q-1)}}\tag{5}
\]
edges.

*Proof.* The second-eigenspace difference vectors are supported within individual Cartesian factors, representing a direct sum of \(k\) copies of \(M(K_q)\). The vectors in every vertex star form a basis of \(N\). Graph cycles are dependent because their oriented edge differences telescope to zero. The graph is \(k(q-1)\)-regular. Apply (4). \(\square\)

**Canonical specializations.** For \(G=Q_n=H(n,2)\), every nonbacktracking turn has nonadjacent outside vertices, so the turn condition (2) reduces to \(b(u,v,w)=c(uv)+c(vw)\). An accepted resource-independent path is a monochromatic coordinate-distinct cube geodesic. Consequently **every** binary coloring of the edges of \(Q_n\), without any antipodal condition, admits such a geodesic of at least \(\frac12\sqrt n\) edges.

For \(G=K_n=H(1,n)\), every turn has adjacent outside vertices; (3) is the reversal-odd boundary 3-tournament rule, and condition (2) is vacuous. Here the auxiliary edge coloring \(c\) may be chosen constant. Applying the terminal-path theorem directly to the full \(K_n\) recovers the stronger boundary estimate
\[
\ell\ge\sqrt{(n-1)/2}.\tag{6}
\]
The spectral resource matroid is \(M(K_n)\), so independence is equivalent to vertex simplicity along a path.

These instances share a single accepted-turn predicate, a single star-independent cycle-dominating resource matroid hypothesis, and a common terminal-set counting proof. To force the full \(n\)-edge cubical geodesic, an additional global condition must strengthen the square-root estimate (5).
