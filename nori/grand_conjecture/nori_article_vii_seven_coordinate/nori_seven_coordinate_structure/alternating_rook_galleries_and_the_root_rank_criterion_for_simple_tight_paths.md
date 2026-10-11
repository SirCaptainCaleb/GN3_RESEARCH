# Alternating rook galleries and the root-rank criterion for simple tight paths

# Alternating rook galleries and the root-rank criterion for simple tight paths

Let \(V\) be a finite set with \(|V|=n\ge3\), and let \(b:V^{\underline 3}\to\{0,1\}\) satisfy \(b(c,v,a)=1-b(a,v,c)\). Put
\[
\Omega_V=\{(a,c):a,c\in V,\ a\ne c\},\qquad
\rho(a,c)=e_a-e_c\in\mathbb R^V,\qquad J(a,c)=(c,a).
\]
The **rook graph** on \(\Omega_V\) joins two different ordered pairs if their first or second coordinates agree. Orient its edges by
\[
(a,v)\longrightarrow(c,v),\qquad
(v,a)\longrightarrow(v,c)
\quad\Longleftrightarrow\quad b(a,v,c)=0.\tag{1}
\]
The reversal law makes (1) an orientation of each row and column clique; \(J\) is an automorphism of this oriented graph. An **alternating rook gallery** is a rook walk whose steps alternate between columns (equal second coordinate) and rows (equal first coordinate).

**Theorem.** For \(3\le L\le n\), color-zero vertex-simple tight paths \((v_1,\ldots,v_L)\), with \(b(v_i,v_{i+1},v_{i+2})=0\) for all \(i\), correspond bijectively to directed alternating rook galleries \(q_1,\ldots,q_{L-1}\) beginning with a column step and satisfying linear independence of the roots \(\rho(q_1),\ldots,\rho(q_{L-1})\). The map is
\[
q_i=\begin{cases}(v_i,v_{i+1}),&i\text{ odd},\\
(v_{i+1},v_i),&i\text{ even}.
\end{cases}\tag{2}
\]
A directed alternating rook gallery beginning with a row step can be converted to one beginning with a column step by applying \(J\) to all its terms, preserving directedness and root rank.

More generally, for every alternating rook gallery \(q_1,\ldots,q_m\) and its induced vertex walk \(v_1,\ldots,v_{m+1}\),
\[
\operatorname{rank}_{\mathbb R}\{\rho(q_1),\ldots,\rho(q_m)\}
=|\{v_1,\ldots,v_{m+1}\}|-1.\tag{3}
\]
Thus the induced walk is vertex-simple if and only if its root vectors are linearly independent. Its rank deficit is
\[
m-\operatorname{rank}\{\rho(q_i)\}=(m+1)-|\{v_1,\ldots,v_{m+1}\}|.\tag{4}
\]

**Proof.** For odd \(i\), the pairs \(q_i=(v_i,v_{i+1})\) and \(q_{i+1}=(v_{i+2},v_{i+1})\) share the second coordinate; (1) directs the connecting rook edge forward precisely when \(b(v_i,v_{i+1},v_{i+2})=0\). For even \(i\), the pairs \(q_i=(v_{i+1},v_i)\) and \(q_{i+1}=(v_{i+1},v_{i+2})\) share the first coordinate, with the same condition. Conversely, the first pair of a column-first gallery determines \(v_1,v_2\), and each next rook edge determines its new coordinate \(v_{i+2}\). Its orientation enforces the color-zero triple condition. Hence (2) gives the correspondence for vertex walks with no immediate backtracking.

For each \(i\),
\[
\rho(q_i)=(-1)^{i-1}(e_{v_i}-e_{v_{i+1}}).\tag{5}
\]
The undirected multigraph with edges \(v_iv_{i+1}\) is connected on its encountered vertices. Its oriented incidence vectors span the codimension-one subspace of real vectors supported on those vertices and having coordinate sum zero. To see this, a vector orthogonal to every incidence vector must be constant on endpoints of each edge, hence constant on the connected graph. The span therefore has dimension one fewer than its vertex set. The signs in (5) preserve this rank, proving (3) and (4). The induced walk has no repeated vertex precisely when it uses \(m+1\) vertices, equivalent by (3) to rank \(m\). Finally \(J\) exchanges columns with rows, preserves orientation (1), and negates every root, so it preserves directedness and linear independence. \(\square\)

**Corollary.** An arbitrary boundary 3-tournament has a monochromatic vertex-simple tight path on \(L\) vertices if and only if its rook orientation has a directed alternating gallery with \(L-1\) linearly independent roots in the type-\(A_{n-1}\) root system. A color-one tight path reverses to a color-zero path by the reversal law. In particular, the distinct-original-vertex constraint is a graphic-matroid independence condition on an alternating rook gallery.
