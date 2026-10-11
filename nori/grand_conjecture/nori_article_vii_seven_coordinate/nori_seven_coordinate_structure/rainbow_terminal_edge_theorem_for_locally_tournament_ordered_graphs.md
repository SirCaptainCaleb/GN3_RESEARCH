# Rainbow terminal-edge theorem for locally tournament-ordered graphs

# Rainbow terminal-edge theorem for locally ordered graphs

Let \(G=(V,E)\) be a finite simple graph, \(|E|>0\). Label its edges by \(\lambda:E\to\Lambda\), with distinct labels on incident edges. At each \(v\in V\), fix a tournament \(T_v\) on the edges incident with \(v\). A path \(P=(v_1,\ldots,v_\ell)\) is **admissible** if its vertices are distinct, its edge labels are distinct, and
\[
v_{i-1}v_i\longrightarrow v_iv_{i+1}\quad\text{in }T_{v_i}
\quad (2\le i\le\ell-1).
\tag{1}
\]
Paths of two vertices are admissible. Let \(L\) be the maximum order of an admissible path and \(\bar d=2|E|/|V|\).

**Theorem.**
\[
\boxed{\bar d/2\le (L-1)(2L-3),\qquad
L\ge (5+\sqrt{1+4\bar d})/4.}
\tag{2}
\]
If the labels of all graph edges are distinct, then
\[
\boxed{\bar d/2\le (L-1)^2.} \tag{3}
\]

**Proof.** For every undirected edge \(e=\{u,v\}\), let \(r(e)\) be the greatest order of an admissible path ending in \(u,v\) or \(v,u\). Direct \(e\) toward the final vertex of a maximizing path, breaking ties arbitrarily. Some vertex \(v\) has indegree at least \(\bar d/2\). For \(r=2,\ldots,L\), let
\[
U_r=\{u:u\to v,\ r(\{u,v\})=r\},\qquad q=|U_r|.
\]
The tournament \(T_v\) on \(\{uv:u\in U_r\}\) contains an edge \(uv\) beating at least \((q-1)/2\) other incident edges \(vw\). Choose an admissible \(r\)-vertex path
\[
P=(a_1,\ldots,a_{r-2},u,v)
\]
ending with \(uv\). Whenever \(uv\to vw\) in \(T_v\), adding \(w\) satisfies the required comparison at \(v\). If \(w\) were new to \(P\) and \(\lambda(vw)\) unused on \(P\), the extension would be admissible of order \(r+1\), contradicting \(r(\{v,w\})=r\).

Among the beaten edges, at most \(r-2\) have \(w\in\{a_1,\ldots,a_{r-2}\}\). At most another \(r-2\) have \(\lambda(vw)\) previously used: \(\lambda(vw)\ne\lambda(uv)\) by properness, and each of the remaining \(r-2\) labels appears on at most one edge incident with \(v\). Therefore
\[
(q-1)/2\le2r-4,\qquad |U_r|\le4r-7.
\]
Consequently
\[
\bar d/2\le\deg^-(v)=\sum_{r=2}^L|U_r|
\le\sum_{r=2}^L(4r-7)=(L-1)(2L-3).
\]
Solving the quadratic gives the second inequality in (2).

With globally distinct edge labels, every edge \(vw\) differs from every edge of \(P\), so only repeated vertices can block extensions. Thus \((q-1)/2\le r-2\), implying \(|U_r|\le2r-3\) and
\[
\bar d/2\le\sum_{r=2}^L(2r-3)=(L-1)^2.
\]
This proves (3). \(\square\)

**Corollary (all ordinary boundary tournaments).** For any \(n\)-vertex function \(b(a,v,w)\in\{0,1\}\) on distinct ordered triples with \(b(w,v,a)=1-b(a,v,w)\), take \(G=K_n\), label each edge separately, and direct
\[
av\to vw\quad\text{in }T_v\quad\Longleftrightarrow\quad b(a,v,w)=1.
\]
These comparisons define tournaments at every vertex. An admissible graph path is precisely a vertex-simple positive tight path for \(b\). Since \(\bar d=n-1\), (3) gives
\[
L\ge1+\sqrt{(n-1)/2}.
\tag{4}
\]
This recovers the Devine–Milans boundary-tournament terminal-pair lower bound without an edge-orderability assumption.

**Corollary (all cube-edge colorings).** For any binary coloring \(c\) of the undirected edges of \(Q_n\), put \(G=Q_n\) and label each edge by its coordinate direction. At each vertex, order the incident edges first by their binary colors and break equal-color ties arbitrarily, taking \(T_v\) to be the resulting transitive tournament. Every admissible path is a cube geodesic because its directions are distinct. Its edge-color word is weakly increasing, hence has at most one change. With \(\bar d=n\), (2) yields an admissible geodesic of at least
\[
(5+\sqrt{1+4n})/4-1
\tag{5}
\]
edges. The conclusion holds in particular for unrestricted antipodally odd edge colorings.

The two corollaries use the same graph-theoretic comparison, admissibility predicate, and extremal proof. The cube bound concerns a partial geodesic, so its extension to a full antipodal geodesic needs additional global edge-consistency and antipodal linkage. The complete-graph bound is the established square-root boundary result; its proper-edge-label extension is the new common structural theorem.
