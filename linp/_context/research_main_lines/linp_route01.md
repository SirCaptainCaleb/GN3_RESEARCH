# Route 1 — Snake accounting and the 43/48 equality problem

## Statement

The fixed-entrance recurrence and exact snake identity yield the 43/48 bound and reduce near equality to explicit path-intersection and global multiplicity structure.

## Body

# Snake accounting and the \(43/48\) equality problem

Let \(H\) be a finite linear \(3\)-graph. For an edge \(e\) and a vertex \(v\in e\), let \(\phi(e,v)\) be the maximum length of a linear path with last edge \(e\) and last vertex \(v\). Put
\[
\phi(e)=\max_{v\in e}\phi(e,v),
\qquad
\phi(v)=\max_{e\ni v}\phi(e,v).
\]
An edge \(e\) is **special** if \(\phi(e,v)=\phi(e)\) for every \(v\in e\). If \(e\) is nonspecial, then all longest paths with last edge \(e\) have the same entrance label; this vertex is the **unique entrance** of \(e\), and the other two vertices are terminal at \(e\). A nonspecial edge \(e\) with unique entrance \(x\) is **ascending** if
\[
\phi(x)=\phi(e)-1.
\]

For a vertex \(v\), let \(T(v)\) be the set of ascending edges at which \(v\) is terminal, and put \(t(v)=|T(v)|\). Write
\[
S=\sum_{v\in V(H)}\phi(v)
\]
and let \(n_+\) be the number of nonisolated vertices.

## 1. The fixed-entrance bound

### Lemma 1
Let \(h\) be an ascending edge of edge rank \(q\ge4\), and let \(v\) be terminal at \(h\). Then
\[
\bigl|\{f\ni v:\phi(f)\le q\}\bigr|
\le
\left\lfloor\frac{11q-5}{8}\right\rfloor . \tag{1}
\]

#### Proof
Choose a \(q\)-edge path
\[
P=(g_1,\ldots,g_q)
\]
with last edge \(g_q=h\) and last vertex \(v\). Let
\[
x=g_{q-1}\cap h.
\]
Since \(h\) is ascending, \(\phi(x)=q-1\). Put
\[
W=V(P)\setminus h.
\]
For every edge \(f\ne h\) containing \(v\) with \(\phi(f)\le q\), define
\[
C_f=(f\setminus\{v\})\cap W.
\]
If \(C_f=\varnothing\), then a final segment of \(P\) followed by \(f\) gives a path longer than \(\phi(f)\). Thus \(C_f\ne\varnothing\). Linearity implies that the sets \(C_f\) are pairwise disjoint, and each has size one or two.

Write
\[
z_i=g_i\cap g_{i+1}\qquad(1\le i\le q-1),
\]
write \(g_1=\{a_1,b_1,z_1\}\), and for \(2\le i\le q-1\) let \(b_i\) be the private vertex of \(g_i\). The vertices
\[
a_1,\quad b_1,\quad b_{q-2},\quad z_{q-2}
\]
cannot occur as singleton sets \(C_f\): in each case replacing an initial or final segment of \(P\) by \(f\) gives a \(q\)-edge path with last vertex \(x\), contradicting \(\phi(x)=q-1\).

After these exclusions, the possible singleton positions occur in
\[
B_1=\{z_1\},
\qquad
B_i=\{b_i,z_i\}\quad(2\le i\le q-3),
\]
together with \(b_{q-1}\). A singleton in the forward position of \(B_i\) excludes specified singleton positions two steps later, because otherwise the two corresponding edges splice with \(P\) to produce a \(q\)-edge path ending at \(x\). Recording whether \(B_{i-1}\) and \(B_i\) contain a singleton gives the four-state recurrence
\[
00\to00:0,\quad 00\to01:2,\quad
01\to10:0,\quad 01\to11:1,
\]
\[
10\to00:0,\quad 10\to01:1,\quad
11\to10:0.
\]
After four steps every finite state value increases by \(3\). Hence the number \(s\) of singleton sets satisfies
\[
s\le
\left\lceil\frac{3q-8}{4}\right\rceil . \tag{2}
\]

Let \(d\) be the number of sets \(C_f\) of size two and let \(u\) be the number of unused vertices of \(W\). Since \(|W|=2q-2\),
\[
s+2d+u=2q-2.
\]
Therefore
\[
\bigl|\{f\ni v:\phi(f)\le q\}\bigr|
=
1+s+d
\le
q+\left\lfloor\frac{s}{2}\right\rfloor
\le
\left\lfloor\frac{11q-5}{8}\right\rfloor .
\]
For \(q=2,3\) the corresponding bounds are \(1,2\). ∎

Define
\[
\gamma(1)=0,\quad \gamma(2)=1,\quad \gamma(3)=2,
\qquad
\gamma(q)=\left\lfloor\frac{11q-5}{8}\right\rfloor\quad(q\ge4).
\]

### Corollary 2
For every nonisolated vertex \(v\),
\[
t(v)\le \gamma(\phi(v)). \tag{3}
\]

#### Proof
Choose \(h\in T(v)\) of maximum edge rank \(q\). Every member of \(T(v)\) has edge rank at most \(q\), and \(q\le\phi(v)\). Apply Lemma 1 and monotonicity of \(\gamma\). ∎

## 2. Path-relative terminal bounds

For a maximum \(p\)-edge path \(P\) ending at \(v\), and an incident edge \(f\ne g_p\), let
\[
\mu_P(f)=|(f\setminus\{v\})\cap(V(P)\setminus g_p)|.
\]
Assign \(\mu_P(g_p)=1\).

The following path-local estimate will be used in the exact count.

### Lemma 3
Let \(P\) be a \(p\)-edge path ending at \(v\), and let \(F_Q\) be a family of ascending edges \(e=\{x,u,v\}\) at which \(v\) is terminal and
\[
\phi(e)\le Q,\qquad
\left\lceil\frac{p+2}{2}\right\rceil\le Q\le p.
\]
If every member of \(F_Q\) has \(\mu_P(e)=1\), then
\[
|F_Q|\le 4Q-2p-3. \tag{4}
\]

The proof is a path-splice count. For \(e=\{x,u,v\}\), both \(x\) and \(u\) must occur in the final \(Q-1\) edges of any maximum \(p\)-edge path ending at \(v\), unless the edge has a second intersection with the path. Under \(\mu_P(e)=1\), the unique intersection therefore lies in the overlap of the two terminal intervals obtained from the entrance side and the opposite-terminal side. This overlap contains \(4Q-2p-3\) admissible vertices. Distinct members of \(F_Q\) use distinct admissible vertices by linearity, proving (4).

## 3. An exact global identity

Define
\[
\beta(1)=0,\quad
\beta(2)=1,\quad
\beta(3)=2,\quad
\beta(4)=2,\quad
\beta(5)=3,\quad
\beta(6)=5,
\]
and
\[
\beta(p)=\left\lfloor\frac{11p-16}{8}\right\rfloor
\qquad(p\ge7). \tag{5}
\]

For each nonisolated \(v\), put \(p_v=\phi(v)\), choose a maximum \(p_v\)-edge path \(P_v\) ending at \(v\), and let \(D_v\) be the number of incident edges with \(\mu_{P_v}(e)=2\). If \(T(v)\ne\varnothing\), let
\[
q(v)=\max\{\phi(e):e\in T(v)\}.
\]

### Lemma 4
For every nonisolated \(v\),
\[
t(v)-D_v\le \beta(p_v). \tag{6}
\]

#### Proof
If \(T(v)=\varnothing\), the assertion is immediate.

Suppose first that \(q(v)=p_v\). Choose \(P_v\) with last edge an ascending edge of rank \(p_v\). Lemma 1, with the double intersections removed, gives
\[
t(v)-D_v
\le
1+\left\lceil\frac{3p_v-8}{4}\right\rceil
=
\left\lceil\frac{3p_v-4}{4}\right\rceil . \tag{7}
\]

Now suppose \(q(v)<p_v\). Corollary 2 gives
\[
t(v)\le \gamma(q(v))\le \gamma(p_v-1). \tag{8}
\]
After the \(D_v\) double intersections are removed, every remaining member of \(T(v)\) has one off-\(v\) intersection with \(P_v\). Lemma 3 gives
\[
t(v)-D_v
\le
\max(0,4q(v)-2p_v-3)
\le
\max(0,2p_v-7). \tag{9}
\]
Thus
\[
t(v)-D_v
\le
\min\{\gamma(p_v-1),\max(0,2p_v-7)\}. \tag{10}
\]
Comparing (7) and (10) with (5), directly for \(p_v\le7\) and by the floor formula for \(p_v\ge8\), gives (6). ∎

Define the local nonnegative quantity
\[
\eta_v=\beta(p_v)-t(v)+D_v. \tag{11}
\]
Let
\[
D=\sum_vD_v,\qquad \eta=\sum_v\eta_v.
\]
Let \(C\) be the number of incidences \((v,e)\) for which \(\mu_{P_v}(e)=0\), and let
\[
R=\sum_v\left(2p_v-1-\sum_{e\ni v}\mu_{P_v}(e)\right). \tag{12}
\]
Linearity gives \(R\ge0\).

Let \(A\) be the number of ascending edges.

### Theorem 5
\[
6|E(H)|
=
\sum_v\bigl(4p_v-2+\beta(p_v)\bigr)
-D-\eta-2(A-C)-2R. \tag{13}
\]

#### Proof
For a fixed \(v\), the path \(P_v\) has \(2p_v-2\) vertices outside its last edge. Distinct incident edges can use each such vertex at most once, so (12) is nonnegative.

Summing the multiplicities \(\mu_{P_v}(e)\) over all incidences, an ordinary incidence contributes \(1\), a zero-intersection incidence contributes \(0\), and a double-intersection incidence contributes \(2\). Hence
\[
3m-C+D=2S-n_+-R. \tag{14}
\]

A zero-intersection incidence can occur only at the unique entrance of an ascending edge; otherwise the incident edge could be appended to the chosen maximum path. Therefore
\[
C\le A. \tag{15}
\]
Every ascending edge has two terminal vertices, so
\[
\sum_v t(v)=2A. \tag{16}
\]
By (11),
\[
\sum_v\beta(p_v)=2A-D+\eta. \tag{17}
\]
Substituting (17) into twice (14) gives (13). ∎

### Corollary 6
If \(H\) is \(P_\ell^{(3)}\)-free and \(\ell\ge8\), then
\[
|E(H)|
\le
\frac{43\ell-75-\rho_\ell}{48}\,n
\le
\frac{43\ell-75}{48}\,n, \tag{18}
\]
where \(0\le\rho_\ell\le7\) is determined by
\[
\left\lfloor\frac{11\ell-27}{8}\right\rfloor
=
\frac{11\ell-27-\rho_\ell}{8}.
\]

#### Proof
If \(H\) is \(P_\ell^{(3)}\)-free, then \(p_v\le\ell-1\). The function
\[
4p-2+\beta(p)
\]
is increasing. Discard the four nonnegative terms subtracted in (13) and substitute \(p_v\le\ell-1\). ∎

## 4. What near equality forces

Assume now that
\[
|E(H)|=\left(\frac{43}{48}-o(1)\right)S,
\qquad
\frac{S}{n_+}\to\infty. \tag{19}
\]
Since
\[
\sum_v(4p_v-2+\beta(p_v))
\le
\frac{43}{8}S+O(n_+),
\]
Theorem 5 implies
\[
D=o(S),\qquad
\eta=o(S),\qquad
A-C=o(S),\qquad
R=o(S). \tag{20}
\]

If \(q(v)=p_v=p\ge8\), then (7) gives
\[
\eta_v
\ge
\beta(p)-\left\lceil\frac{3p-4}{4}\right\rceil
\ge
\frac{5p-24}{8}. \tag{21}
\]
Thus the vertices satisfying \(q(v)=p_v\) have total vertex rank \(o(S)\).

The remaining high-rank vertices have \(q(v)<p_v\). Fix one, write
\[
p=p_v,\qquad q=q(v),
\]
choose \(e_0\in T(v)\) of edge rank \(q\), choose a maximum \(q\)-edge path \(Q\) ending in \(e_0\) at \(v\), and retain the chosen maximum \(p\)-edge path \(P=P_v\).

### Lemma 7
There is a family \(F_v\subseteq T(v)\) of edges that meet \(Q\) in both vertices outside \(v\) and meet \(P\) in exactly one vertex outside \(v\), with
\[
|F_v|
\ge
\beta(p)-\eta_v
-\left\lceil\frac{3q-4}{4}\right\rceil. \tag{22}
\]
In particular,
\[
|F_v|\ge \frac58p-\eta_v-O(1). \tag{23}
\]

#### Proof
Applied to the \(q\)-edge path \(Q\), the singleton part of Lemma 1 shows that at most
\[
\left\lceil\frac{3q-4}{4}\right\rceil
\]
members of \(T(v)\) fail to have both off-\(v\) vertices on \(Q\). Hence at least
\[
t(v)-\left\lceil\frac{3q-4}{4}\right\rceil
\]
have both.

Among these, at most \(D_v\) have two off-\(v\) vertices on \(P\). Removing them leaves at least
\[
t(v)-D_v-\left\lceil\frac{3q-4}{4}\right\rceil
=
\beta(p)-\eta_v-\left\lceil\frac{3q-4}{4}\right\rceil,
\]
which proves (22). Since \(q\le p-1\), (5) gives (23). ∎

## 5. The interior-pair count

Write
\[
P=(g_1,\ldots,g_p).
\]
For \(1\le i\le p-3\), put
\[
z_i=g_i\cap g_{i+1}
\]
and let \(b_i\) be the private vertex of \(g_i\). Define the interior pair
\[
B_i=\{b_i,z_i\}. \tag{24}
\]

Apart from \(O(1)\) boundary positions, the unique off-\(v\) intersection of every member of \(F_v\) with \(P\) lies in one of the pairs \(B_i\). Let \(s_v\) be the number of members represented in the interior pairs. Then
\[
s_v\ge \frac58p-\eta_v-O(1). \tag{25}
\]

At most two members of \(F_v\) can use one \(B_i\), by linearity. Let \(D'_v\) be the number of \(B_i\) using both positions.

A member meeting \(P\) in \(B_i\) gives a length-preserving rotation of \(P\) whose last edge is \(g_{i+2}\). Hence
\[
\phi(g_{i+2})\ge p. \tag{26}
\]
Let \(I_v\) be the number of occupied \(B_i\) for which every vertex of \(g_{i+2}\) has vertex rank at least \(p\).

### Lemma 8
\[
D'_v+I_v
\ge
s_v-\left\lceil\frac{p-3}{2}\right\rceil. \tag{27}
\]
Consequently
\[
D'_v+I_v
\ge
\frac18p-\eta_v-O(1). \tag{28}
\]

#### Proof
Let \(C_v\) be the number of occupied interior pairs. Since each occupied pair contains one or two intersections,
\[
s_v=C_v+D'_v. \tag{29}
\]

Consider an occupied \(B_i\) that is not counted by \(I_v\). By (26), \(\phi(g_{i+2})\ge p\). Since some vertex of \(g_{i+2}\) has rank below \(p\), the edge \(g_{i+2}\) must have edge rank exactly \(p\), must be nonspecial ascending, and its unique entrance is its forward joint
\[
g_{i+2}\cap g_{i+3},
\]
which has vertex rank \(p-1\).

Two consecutive output edges cannot both have this form. Indeed, if \(g_j\) has unique entrance
\[
z_j=g_j\cap g_{j+1}
\]
with \(\phi(z_j)=p-1\), and \(g_{j+1}\) has the analogous form, then \(z_j\) is a terminal vertex of the rank-\(p\) edge \(g_{j+1}\), forcing \(\phi(z_j)\ge p\), a contradiction.

Thus the occupied interior pairs that are neither doubly occupied nor counted by \(I_v\) form an independent set in the path of \(p-3\) interior indices. There are at most
\[
\left\lceil\frac{p-3}{2}\right\rceil
\]
of them. Using (29) gives (27), and (25) gives (28). ∎

If \(B_i\) is doubly occupied, the edge \(g_i\) and the two members of \(F_v\) using \(b_i,z_i\) form a \(3\)-edge linear cycle. Distinct doubly occupied interior pairs yield edge-disjoint such cycles apart from the common vertex \(v\) in their two nonpath edges. Distinct indices counted by \(I_v\) yield distinct path edges \(g_{i+2}\) contained in the rank superlevel
\[
V_{\ge p}=\{w:\phi(w)\ge p\}. \tag{30}
\]

Thus every low-\(\eta_v\) high-rank vertex produces linearly many local cycles or linearly many distinct edges in its rank superlevel.

## 6. Refinement of the selected ascending edges

The exact identity also controls the intersections at the unique entrance and at the two terminals.

By (20), \(A-C=o(S)\). Hence, after deleting \(o(S)\) ascending edges, if
\[
e=\{x,u,v\}
\]
has unique entrance \(x\), the chosen maximum path ending at \(x\) contains neither \(u\) nor \(v\). Likewise \(D=o(S)\), and every maximum path chosen at a terminal of an ascending edge must contain at least one of the other two vertices; after deleting \(o(S)\) terminal incidences, it contains exactly one.

It remains to remove terminal incidences \((e,w)\) for which
\[
\phi(e)=\phi(w). \tag{31}
\]
Such an incidence makes \(w\) terminal at an ascending edge whose edge rank equals \(\phi(w)\). Hence
\[
q(w)=\phi(w).
\]
By (21), vertices with this equality have total vertex rank \(o(S)\). Corollary 2 gives
\[
t(w)\le \gamma(\phi(w))=O(\phi(w)),
\]
so the total number of incidences satisfying (31) is also \(o(S)\).

Consequently one may choose families \(G_v\subseteq T(v)\) such that
\[
\sum_v\left(\frac{\phi(v)}8-|G_v|\right)_+=o(S), \tag{32}
\]
and every edge \(e=\{x,u,v\}\in G_v\) satisfies

\[
V(P_x)\cap\{u,v\}=\varnothing, \tag{33}
\]
for the chosen maximum path \(P_x\) ending at its unique entrance, and
\[
|(e\setminus\{w\})\cap V(P_w)|=1 \tag{34}
\]
for each terminal \(w\in\{u,v\}\), together with
\[
\phi(e)<\min\{\phi(u),\phi(v)\}. \tag{35}
\]

The point of (32)–(35) is that they retain the \(1/8\)-scale family while removing the exceptional entrance and terminal incidences measured by the four terms of (13).

## 7. Fundamental cycles of the terminal-pair graph

Form a graph \(J\) whose edges are the terminal pairs \(uv\) of the edges
\[
e=\{x,u,v\}
\]
appearing in the families \(G_v\). Give \(uv\) weight \(\phi(e)\). In each component choose a spanning tree of maximum total weight.

### Lemma 9
After deleting \(o(S)\) further incidences, one obtains families \(H_v\subseteq G_v\) satisfying
\[
\sum_v\left(\frac{\phi(v)}8-|H_v|\right)_+=o(S), \tag{36}
\]
such that every \(e\in H_v\) is a nonforest edge, has minimum edge rank on its fundamental cycle, and has the following property: if \(f\) is either neighboring edge on that cycle and \(w\) is their common terminal, then every maximum path with last edge \(f\) and last vertex \(w\) contains a second vertex of \(e\).

#### Proof
A spanning forest contains fewer than \(n_+\) graph edges. Deleting the associated terminal incidences costs \(O(n_+)=o(S)\), proving (36).

Let \(e\) be a remaining nonforest edge. If a tree edge \(f\) on its fundamental cycle had smaller weight, replacing \(f\) by \(e\) would increase the total tree weight. Thus \(e\) has minimum edge rank on the cycle.

Let \(f\) be a cycle-neighbor of \(e\), sharing terminal \(w\). Since
\[
\phi(f)\ge\phi(e),
\]
a maximum path ending in \(f\) at \(w\) cannot meet \(e\) only at \(w\); otherwise appending \(e\) gives a path with last edge \(e\) longer than \(\phi(e)\). ∎

Since an ascending edge can belong to at most the two families indexed by its terminal vertices, (36) contains
\[
\left(\frac1{16}-o(1)\right)S \tag{37}
\]
distinct hyperedges.

## 8. A three-way local alternative

Fix \(v\), put \(p=\phi(v)\), and let \(F\subseteq H_v\) contain \(k\) edges that meet the chosen maximum \(p\)-edge path \(P\) in exactly one off-\(v\) vertex.

Separate \(F\) into \(U\) and \(X\), where an edge belongs to \(U\) if that intersection is its opposite terminal and belongs to \(X\) if that intersection is its unique entrance.

For \(e\in X\), let \(a(e)\) be the first edge of \(P\) containing its unique entrance and put
\[
\sigma(e)=\phi(x_e)-a(e).
\]
The path-splice recurrence for ordered entrance intersections gives, for every integer \(s\ge0\),
\[
k
\le
|U|+
|\{e\in X:\sigma(e)>s\}|+
4s+O(\log p). \tag{38}
\]

Take \(s=\lfloor k/16\rfloor\). If \(|U|\ge k/2\), at least half of the family meets \(P\) at its opposite terminal. Otherwise
\[
|\{e\in X:\sigma(e)>s\}|
\ge
k/4-O(\log p). \tag{39}
\]
Linearity places these edges in at least
\[
k/8-O(\log p)
\]
distinct interior pairs. By Lemma 8, at least half of those pairs either are doubly occupied and therefore determine a \(3\)-edge linear cycle, or have a distinct output edge contained in \(V_{\ge p}\).

We have proved:

### Theorem 10
Outside a set of vertices of total vertex rank \(o(S)\), every high-rank vertex \(v\) has a family \(H_v\) satisfying Lemma 9 and at least one of the following:

1. at least
   \[
   (1/16-o(1))\phi(v)
   \]
   members meet the chosen maximum path at their opposite terminal;
2. at least
   \[
   (1/128-o(1))\phi(v)
   \]
   distinct \(3\)-edge linear cycles arise from doubly occupied interior pairs;
3. at least
   \[
   (1/128-o(1))\phi(v)
   \]
   distinct path edges lie entirely in
   \[
   V_{\ge\phi(v)}.
   \]

Partitioning the vertices according to one alternative shows that one of the three alternatives has total vertex-indexed multiplicity \(\Omega(S)\).

## 9. The remaining implication

The proof of a strict improvement over \(43/48\) now reduces to a global multiplicity statement.

### Open problem
For one of the three families in Theorem 10, prove that \(\Omega(S)\) vertex-indexed occurrences cannot be supported by \(o(S)\) distinct global objects with unbounded multiplicity.

A sufficient statement is the following. Assign every selected edge to one of its terminal vertices, and let \(d(w)\) be the number assigned to \(w\). Prove
\[
d(w)\le g(\phi(w))
\qquad\text{with}\qquad
g(p)=o(p). \tag{40}
\]
Then
\[
|E'|\le\sum_wg(\phi(w))=o(S),
\]
because for every \(\varepsilon>0\),
\[
\sum_wg(\phi(w))
\le
\varepsilon S+O_\varepsilon(n_+)
=
\varepsilon S+o(S).
\]
This contradicts (37).

The remaining difficulty is therefore global reuse of the maximum paths, terminal vertices, fundamental-cycle edges, local \(3\)-cycles, and rank-superlevel edges produced above.

## 10. Obstructions to simpler continuations

The cumulative fixed-entrance bound does not force a positive proportion of a terminal family to have edge rank uniformly below its maximum; it is an upper bound on the low-rank portion.

Even families satisfying (33)–(35) can violate simple four-edge spacing inequalities. Hence edge ranks alone do not encode enough of the path intersections.

Finally, the vertex-indexed families \(H_v\) are not globally disjoint. Any summation that treats their members, their maximum paths, or their output edges as distinct without a multiplicity bound loses exactly the information needed for the final step.