# Main Line 2 — Ascending edges in a dense subgraph

# Ascending edges in a dense subgraph

Let \(H\) be a finite linear \(3\)-graph. We use the notation \(\phi(e,v)\), \(\phi(e)\), and \(\phi(v)\) from the preceding rehearsal. A nonspecial edge \(e\) with unique entrance \(x\) is ascending when
\[
\phi(x)=\phi(e)-1.
\]
Let \(A\) denote the number of ascending edges.

This line of argument seeks the asymptotic bound
\[
|E(H)|\le \left(\frac{2}{3}\ell+o(\ell)\right)|V(H)|
\]
for \(P_\ell^{(3)}\)-free linear \(3\)-graphs. The essential point is that the only incidences that exceed the ordinary vertex-rank bound are the unique-entrance incidences of ascending edges.

## 1. Ascending edges are the incidence defect

### Lemma 1
For every incident pair \(v\in e\),
\[
\phi(e)\le \phi(v)+1.
\]
Equality holds if and only if \(e\) is ascending and \(v\) is its unique entrance.

#### Proof
If \(e\) is special, then \(v\) is terminal at \(e\), so \(\phi(v)\ge\phi(e)\).

Suppose \(e\) is nonspecial with unique entrance \(x\) and edge rank \(q\). Each terminal vertex is the last vertex of a \(q\)-edge path ending in \(e\), and therefore has vertex rank at least \(q\). Deleting \(e\) from a longest path ending in \(e\) shows \(\phi(x)\ge q-1\). Thus \(q\le\phi(v)+1\) at every incidence. Equality can occur only at the unique entrance, and there it is exactly the defining equality for an ascending edge. ∎

### Lemma 2
If \(H\) has \(m\) edges and \(n\) vertices, then
\[
3m-A\le \sum_{v}(2\phi(v)-1). \tag{1}
\]
Consequently, if \(H\) is \(P_\ell^{(3)}\)-free,
\[
3m-A\le (2\ell-3)n. \tag{2}
\]

#### Proof
Fix \(v\) and put \(p=\phi(v)\). Choose a maximum \(p\)-edge path \(P\) with last vertex \(v\). Every incident edge \(e\) with \(\phi(e)\le p\), except possibly the last edge of \(P\), must contain a vertex of \(V(P)\) outside the last edge; otherwise it can be appended to a suitable final segment of \(P\), producing a path longer than \(\phi(e)\). Distinct incident edges give distinct such vertices by linearity. There are \(2p-2\) vertices outside the last edge, so at most \(2p-1\) incident edges have edge rank at most \(p\).

By Lemma 1, the only remaining incident edges are ascending edges whose unique entrance is \(v\). Summing the bound \(2\phi(v)-1\) over all vertices therefore counts every edge three times except that each ascending edge loses exactly its unique-entrance incidence. This proves (1). If \(H\) is \(P_\ell^{(3)}\)-free, then \(\phi(v)\le\ell-1\), which gives (2). ∎

Thus the two-thirds bound follows once \(A=o(\ell n)\).

## 2. Rank superlevels

For \(t\ge1\), put
\[
V_t=\{v:\phi(v)\ge t\}.
\]

### Lemma 3
Let \(e\) have edge rank \(q\).

1. If \(q>t\), then every vertex of \(e\) lies in \(V_t\).
2. If \(q=t\), then \(e\) meets \(V(H)\setminus V_t\) if and only if \(e\) is ascending. In that case its unique entrance lies outside \(V_t\), and both terminal vertices lie in \(V_t\).

#### Proof
If \(e\) is special, every vertex is terminal at \(e\), hence has vertex rank at least \(q\).

If \(e\) is nonspecial with unique entrance \(x\), then the two terminal vertices have rank at least \(q\), while \(\phi(x)\ge q-1\). Therefore \(q>t\) implies all three ranks are at least \(t\). When \(q=t\), the unique entrance lies outside \(V_t\) exactly when \(\phi(x)=t-1\), which is exactly the ascending condition. ∎

Accordingly, ascending edges are precisely the boundary edges of the rank superlevels at their own edge rank.

## 3. Properly colored terminal-pair graphs

Fix \(t\ge1\). Form a graph \(R_t\) as follows. For every nonspecial edge
\[
e=\{x,u,v\}
\]
whose unique entrance satisfies \(\phi(x)<t\) and whose two terminal vertices satisfy
\[
\phi(u),\phi(v)\ge t,
\]
put the graph edge \(uv\) in \(R_t\) and color it by \(x\).

### Lemma 4
The coloring of \(R_t\) is proper, and \(R_t\) contains no rainbow path with \(t\) edges.

#### Proof
If two graph edges incident with \(u\) had the same color \(x\), the corresponding hyperedges would both contain \(u\) and \(x\), contrary to linearity.

Suppose
\[
v_0v_1\cdots v_t
\]
were a rainbow \(t\)-edge path in \(R_t\), with edge \(v_{i-1}v_i\) colored \(x_i\). The associated hyperedges are
\[
e_i=\{x_i,v_{i-1},v_i\}.
\]
The colors \(x_i\) are distinct and have vertex rank below \(t\), whereas every \(v_i\) has vertex rank at least \(t\). Hence no color equals a path vertex. Properness and linearity then imply that
\[
e_1,\ldots,e_t
\]
form a linear \(t\)-edge path. The vertex \(x_t\) is private in the last hyperedge, so the path can be oriented with last vertex \(x_t\). This gives \(\phi(x_t)\ge t\), a contradiction. ∎

There is a useful summation consequence.

### Corollary 5
For a nonspecial edge \(e\), let \(a(e)\) be the vertex rank of its unique entrance and let
\[
p(e)=\min\{\phi(u),\phi(v)\}
\]
for its two terminal vertices. Then the edges with \(a(e)<p(e)\) satisfy
\[
\sum_e\left(\frac1{a(e)}-\frac1{p(e)}\right)=O(n\log\ell) \tag{3}
\]
in every \(P_\ell^{(3)}\)-free linear \(3\)-graph.

#### Proof
An edge with entrance rank \(a\) and minimum terminal rank \(p>a\) occurs in \(R_t\) precisely for
\[
a<t\le p.
\]
Therefore
\[
\frac1a-\frac1p
=
\sum_{t=a+1}^{p}\frac1{t(t-1)}.
\]
Summing over the edges and reversing the order of summation gives
\[
\sum_e\left(\frac1{a(e)}-\frac1{p(e)}\right)
=
\sum_{t\ge2}\frac{|E(R_t)|}{t(t-1)}.
\]
A rainbow-path extremal bound for properly colored graphs with no rainbow \(t\)-edge path gives \(|E(R_t)|=O(tn)\). Since \(t\le\ell-1\), the right-hand side is \(O(n\log\ell)\). ∎

Thus edges with a substantial entrance-to-terminal rank gap have bounded total harmonic mass. The unresolved contribution must concentrate near equal ranks.

## 4. A sufficient common-terminal bound

For a vertex \(v\), let
\[
c(v)=|\{e:e\text{ is ascending and }v\text{ is terminal at }e\}|.
\]

### Proposition 6
Suppose \(g\) is nondecreasing and
\[
c(v)\le g(\phi(v))
\]
for every vertex. Then every \(P_\ell^{(3)}\)-free linear \(3\)-graph satisfies
\[
m\le
\left(
\frac{2\ell-3}{3}
+
\frac{g(\ell-1)}6
\right)n. \tag{4}
\]
In particular, \(g(p)=o(p)\) implies the two-thirds leading coefficient.

#### Proof
Every ascending edge has exactly two terminal vertices, so
\[
2A=\sum_v c(v)\le ng(\ell-1).
\]
Substitute this in (2). ∎

Hence full specialness is stronger than necessary: a sublinear common-terminal bound already suffices.

## 5. Longest-path decomposition of the remaining ascending edges

Choose for every vertex \(v\) a maximum path
\[
P_v=(g_1,\ldots,g_p),\qquad p=\phi(v),
\]
with last vertex \(v\). Assign each ascending edge
\[
e=\{x,u,v\}
\]
to a terminal of smaller vertex rank, breaking ties arbitrarily. Thus, if \(e\) is assigned to \(v\),
\[
\phi(u)\ge\phi(v)=p. \tag{5}
\]

Except when \(e\) is the last edge of \(P_v\), every maximum \(p\)-edge path ending at \(v\) contains \(x\) or \(u\). Indeed, otherwise \(e\) can be appended after \(P_v\), contradicting maximality. Thus every assigned edge falls into one of the following three classes:
\[
\begin{array}{ll}
D:& x,u\in V(P_v),\\[2mm]
X:& x\in V(P_v),\ u\notin V(P_v),\\[2mm]
U:& u\in V(P_v),\ x\notin V(P_v).
\end{array}
\tag{6}
\]

The class \(D\) is controlled by double intersections with the chosen paths. The other two classes have more useful structure.

### Lemma 7
Fix \(\varepsilon>0\). Among the edges in class \(X\) assigned to a fixed vertex \(v\), only \(O_\varepsilon(1)\) can satisfy
\[
\phi(e)\le (1-\varepsilon)\phi(v). \tag{7}
\]

#### Proof
For an edge in class \(X\), the intersection of \(e\) with \(P_v\) is exactly \(\{x,v\}\). Order such intersections along \(P_v\). If two unique entrances occur far enough apart, the two corresponding edges can replace an interval of \(P_v\), producing a path that ends at one entrance and is too long for its vertex rank. Quantitatively, if the later edge has edge-rank deficit
\[
D=\phi(v)-\phi(e),
\]
then successive admissible entrance positions must be separated by at least \(D+1\), up to an absolute boundary term. Hence only
\[
O\!\left(\frac{\phi(v)}{D+1}+1\right)
\]
such edges can occur. Under (7), \(D\ge\varepsilon\phi(v)\), which gives \(O_\varepsilon(1)\). ∎

Thus a leading-order class \(X\) family must have edge rank \((1-o(1))\phi(v)\).

The class \(U\) creates many alternative last vertices by rotation.

### Lemma 8
Let \(U(v)\) be the class \(U\) edges assigned to \(v\). There is a set \(W(v)\) of vertices with
\[
\phi(w)\ge\phi(v)\qquad (w\in W(v))
\]
such that
\[
|U(v)|\le 2|W(v)|+1. \tag{8}
\]

#### Proof
Let \(e=\{x,u,v\}\in U(v)\), and let \(j(e)\) be the first index for which \(u\in g_{j(e)}\). Since \(x\notin V(P_v)\), the edge \(e\) can replace the suffix immediately after \(g_{j(e)}\), producing a \(\phi(v)\)-edge path with new last vertex
\[
w(e)=g_{j(e)+1}\cap g_{j(e)+2}.
\]
Hence \(\phi(w(e))\ge\phi(v)\).

Different indices \(j\) give different vertices \(w(e)\). By linearity, distinct edges assigned to \(v\) have distinct opposite terminals \(u\). Along a linear path, at most two vertices have their first occurrence in a given \(g_j\) for \(j\ge2\), and at most three do so in \(g_1\). Therefore at most two edges of \(U(v)\) give the same \(j\), apart from one boundary excess. This yields (8). ∎

Lemmas 7 and 8 reduce the unresolved ascending mass to two phenomena:

1. many edges of edge rank \(p-o(p)\) whose unique entrance lies on a maximum \(p\)-edge path;
2. many alternative last vertices of rank at least \(p\), produced from edges whose opposite terminal lies on that path.

## 6. Directed rank growth

There is a complementary global representation. For every ascending edge
\[
e=\{x,u,v\}
\]
with unique entrance \(x\), draw the arcs
\[
x\to u,\qquad x\to v.
\]

### Lemma 9
Along every directed arc \(x\to y\),
\[
\phi(y)\ge\phi(x)+1.
\]
Consequently a directed path of length \(r\) forces a vertex of rank at least \(r\), and therefore forces a linear hypergraph path of length at least \(r\).

#### Proof
If \(e\) has edge rank \(q\), then \(\phi(x)=q-1\), while each terminal vertex has rank at least \(q\). Iteration proves the first assertion. The second follows from the definition of vertex rank. ∎

Thus repeated movement through ascending edges cannot continue indefinitely without increasing rank.

## 7. The remaining problem

The preceding lemmas leave one theorem to prove.

### Open problem
Show that, in a \(P_\ell^{(3)}\)-free linear \(3\)-graph, the near-top-rank families isolated by Lemmas 7 and 8 cannot occur with total size \(\Theta(\ell n)\).

Any of the following would suffice:

1. \(c(v)=o(\phi(v))\) uniformly, by Proposition 6;
2. a bounded-multiplicity theorem for the vertices \(W(v)\) in Lemma 8;
3. a rank-growth theorem showing that repeated near-top edges produce directed paths whose length contradicts \(\phi\le\ell-1\);
4. a proof that a \(>(2\ell/3)\)-core contains no nonspecial edge.

The last statement is the strongest of these sufficient conditions. The first three are weaker and already give the same leading coefficient.

## 8. Obstructions to simpler arguments

Several natural strengthenings are false.

The terminal-pair graph of all ascending edges need not be rainbow-\(P_4\)-free, even when all terminal vertices on the graph path have the same vertex rank. It need not be a forest or a pseudoforest. Hence the rank parameter cannot be discarded.

A common terminal may support several ascending edges, so a constant common-terminal bound is false in this generality.

Finally, the rank-superlevel decomposition does not give a free positive error term at every threshold. The contribution of an induced superlevel must be counted with its full boundary term. Consequently independent estimates at separate thresholds cannot simply be added.
