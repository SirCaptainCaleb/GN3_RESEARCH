# Main Line 3 — Terminal-pair cycles and rotations

---

## Research Line — Introduction

<!-- research_line_id: terminal_pair_cycles_and_rotations_introduction -->

Let \(H\) be a finite \(P_\ell^{(3)}\)-free linear \(3\)-graph with \(m\) edges and \(n\) vertices. Let \(s\) be the number of special edges.

For every nonspecial edge \(e=\{x,u,v\}\), where \(x\) is the unique entrance, call \(uv\) its **terminal pair**. Linearity implies that distinct nonspecial edges have distinct terminal pairs. Hence the terminal pairs form a simple graph \(T\).

The purpose of this argument is to control the cycle rank
\[
\beta(T)=|E(T)|-|V(T)|+\kappa(T),
\]
where \(\kappa(T)\) is the number of nonempty connected components of \(T\).

---

## Research Line — The special-edge inequality

<!-- research_line_id: terminal_pair_cycles_and_rotations_the_special_edge_inequality -->

Form the snake digraph of \(H\): for every edge \(e\) and every vertex \(v\in e\) with
\[
\phi(e,v)=\phi(e),
\]
include the incidence \((e,v)\). A special edge contributes three such incidences; a nonspecial edge contributes exactly two.

### Lemma 1

For every vertex \(v\),
\[
d^-_{\mathrm{snake}}(v)\le 2\phi(v)-1. \tag{1}
\]

#### Proof
Put \(p=\phi(v)\) and choose a \(p\)-edge path
\[
P=(g_1,\ldots,g_p)
\]
with last vertex \(v\). Consider an edge \(f\ni v\) for which \(v\) is terminal at \(f\). If \(f\ne g_p\), then \(f\) must contain a vertex of
\[
V(P)\setminus g_p.
\]
Otherwise \(P\) can be continued through \(f\), contradicting the maximality of \(p\). Distinct such edges use distinct vertices of \(V(P)\setminus g_p\), since two edges already share \(v\) and cannot share another vertex. There are \(2p-2\) such vertices, and \(g_p\) itself contributes one further edge. ∎

### Corollary 2

\[
2m+s\le \sum_v(2\phi(v)-1)\le (2\ell-3)n. \tag{2}
\]

#### Proof
Summing (1), every special edge contributes \(3\) and every nonspecial edge contributes \(2\). Since there are \(s\) special edges,
\[
\sum_v d^-_{\mathrm{snake}}(v)=3s+2(m-s)=2m+s.
\]
The second inequality follows from \(\phi(v)\le\ell-1\). ∎

Thus any lower bound on \(s\) immediately improves the general coefficient.

---

## Research Line — Cycle rank as a sufficient parameter

<!-- research_line_id: terminal_pair_cycles_and_rotations_cycle_rank_as_a_sufficient_parameter -->

### Proposition 3

Suppose
\[
\beta(T)\le Cs+Dn \tag{3}
\]
for constants \(C,D\ge0\). Then
\[
m\le
\frac{(C+1)(2\ell-3)+D+1}{2C+3}\,n. \tag{4}
\]

#### Proof
Let \(b=m-s\) be the number of nonspecial edges. Since \(T\) is simple and \(|E(T)|=b\),
\[
b=|V(T)|-\kappa(T)+\beta(T)\le n+\beta(T).
\]
Using (3),
\[
b\le Cs+(D+1)n.
\]
Hence
\[
m=b+s\le (C+1)s+(D+1)n,
\]
so
\[
s\ge \frac{m-(D+1)n}{C+1}.
\]
Substitute this in (2) and rearrange. ∎

In particular, \(\beta(T)=O(n)\) gives the two-thirds leading coefficient. The central question is therefore whether the independent cycles of \(T\) force enough new path structure to bound \(\beta(T)\).

---

## Research Line — A maximum-total-rank spanning forest

<!-- research_line_id: terminal_pair_cycles_and_rotations_a_maximum_total_rank_spanning_forest -->

Give each graph edge \(uv\in E(T)\) the edge rank of its parent hyperedge. In each component of \(T\), choose a spanning tree of maximum total weight; let \(F\) be the resulting spanning forest.

### Lemma 4

Let \(e\in E(T)\setminus E(F)\), and let \(C_e\) be its fundamental cycle in \(F+e\). Then \(e\) has minimum weight on \(C_e\).

#### Proof
If a tree edge \(f\in C_e\) had smaller weight than \(e\), then replacing \(f\) by \(e\) would produce a spanning tree of larger total weight. ∎

The graph \(T\) has exactly \(\beta(T)\) nonforest edges. Hence Lemma 4 selects one rank-minimal edge on a fundamental cycle for every independent cycle.

These selected graph edges carry additional information in the hypergraph.

### Lemma 5

Let \(e\) and \(f\) be two nonspecial hyperedges whose terminal pairs are adjacent in \(T\) at a common terminal \(v\). If
\[
\phi(f)\ge\phi(e),
\]
then every maximum path with last edge \(f\) and last vertex \(v\) contains a second vertex of \(e\).

#### Proof
Let \(P\) be such a path. If \(P\cap e=\{v\}\), then appending \(e\) after \(P\) gives a path of length \(\phi(f)+1\) with last edge \(e\). Hence
\[
\phi(e)\ge\phi(f)+1,
\]
contrary to the hypothesis. ∎

Combining Lemmas 4 and 5, every nonforest edge \(e\) has two forced second intersections: one associated with each neighboring edge of its fundamental cycle.

This is the structural content of cycle rank. A cycle is not merely an extra graph edge; it prescribes two additional intersections with maximum hypergraph paths.

---

## Research Line — Rotating a longest path

<!-- research_line_id: terminal_pair_cycles_and_rotations_rotating_a_longest_path -->

The forced second intersections of Lemma 5 can change the last vertex of a longest path.

### Lemma 6

Let
\[
P=(g_1,\ldots,g_L)
\]
be a linear path with last vertex \(z\in g_L\). Let \(f\notin E(P)\) contain \(z\), and suppose that
\[
(f\setminus\{z\})\cap V(P)=\{w\}.
\]
Let \(j\) be the first index for which \(w\in g_j\). If \(j\le L-2\), then
\[
g_1,\ldots,g_j,f,g_L,g_{L-1},\ldots,g_{j+2}
\]
is an \(L\)-edge linear path.

#### Proof
The new sequence uses the initial segment \(g_1,\ldots,g_j\), crosses to \(f\), then traverses the old final segment in reverse. Consecutive edges meet at the prescribed vertices. Since \(f\) has no other vertex on \(P\), it has no nonconsecutive intersection with the old path. The original path is linear, so reversing the final segment creates no new intersection. ∎

Thus every single additional intersection at a suitable position creates another longest path with a different last vertex. Iterating such rotations is the natural mechanism for turning the \(\beta(T)\) fundamental-cycle intersections into many reachable last vertices.

---

## Research Line — Entrance support is an unavoidable parameter

<!-- research_line_id: terminal_pair_cycles_and_rotations_entrance_support_is_an_unavoidable_parameter -->

Cycle rank alone cannot describe all linear dependencies. Let \(h\) be the number of distinct unique entrances of nonspecial edges, and let \(N_{\mathrm{ns}}\) be the real vertex-edge incidence matrix restricted to nonspecial edges.

### Proposition 7

\[
\operatorname{nullity}(N_{\mathrm{ns}})\le \beta(T)+h. \tag{5}
\]
For the full incidence matrix \(N\),
\[
\operatorname{nullity}(N)\le \beta(T)+h+s. \tag{6}
\]

#### Proof
For a nonspecial edge \(e\) with unique entrance \(x_e\) and terminal pair \(u_ev_e\), write its incidence column as
\[
\mathbf 1_{u_e}+\mathbf 1_{v_e}+\mathbf 1_{x_e}.
\]
Let \(B\) be the ordinary \(0/1\) vertex-edge incidence matrix of \(T\), with zero rows added for vertices outside \(V(T)\), and let \(R\) be the matrix whose \(e\)-column is \(\mathbf 1_{x_e}\). Then
\[
N_{\mathrm{ns}}=B+R.
\]
Since \(R\) is supported on \(h\) rows,
\[
\operatorname{rank}(R)\le h.
\]
The inequality
\[
\operatorname{rank}(B+R)\ge\operatorname{rank}(B)-\operatorname{rank}(R)
\]
gives
\[
\operatorname{nullity}(N_{\mathrm{ns}})
\le |E(T)|-\operatorname{rank}(B)+h.
\]

For a graph with \(v\) vertices, \(b\) edges, and \(c_{\mathrm{bip}}\) bipartite components, the real \(0/1\) incidence matrix has rank \(v-c_{\mathrm{bip}}\). Hence
\[
b-\operatorname{rank}(B)
=
b-v+c_{\mathrm{bip}}
\le
b-v+\kappa(T)
=
\beta(T).
\]
This proves (5). Adding \(s\) special columns can increase nullity by at most \(s\), proving (6). ∎

Thus the natural global quantity is \(\beta(T)+h\), not \(\beta(T)\) alone.

---

## Research Line — A false strengthening

<!-- research_line_id: terminal_pair_cycles_and_rotations_a_false_strengthening -->

It is not true that
\[
\beta(T)\le s.
\]
There are linear \(3\)-graphs with \(s=0\) whose terminal-pair graph is a disjoint union of copies of \(K_{3,3}\). Each copy has cycle rank \(4\). The same examples yield nontrivial dependencies among nonspecial incidence columns.

This obstruction shows that a nonforest terminal-pair edge cannot be assigned directly to a special edge. Repeated use of the same unique entrances or the same maximum paths must be included in any valid count.

---

## Research Line — The remaining theorem

<!-- research_line_id: terminal_pair_cycles_and_rotations_the_remaining_theorem -->

The previous lemmas reduce the argument to a quantitative rotation statement.

### Open problem

Let \(F\) be a maximum-total-rank spanning forest of the terminal-pair graph. For each of the \(\beta(T)\) nonforest edges, take the two second intersections supplied by Lemma 5. Prove that these data imply
\[
\beta(T)+h\le Cs+Dn \tag{7}
\]
for absolute constants \(C,D\), or prove an equivalent inequality that gives the same conclusion through Proposition 3.

A proof may proceed by separating two cases.

If the forced second intersections occur on many distinct maximum paths or at many distinct positions, Lemma 6 should yield many distinct last vertices.

If many of them reuse the same path, unique entrance, or path position, that multiplicity must force either larger edge rank, additional unique entrances, or a special edge.

What is not presently proved is the global multiplicity bound required to sum these local alternatives over all fundamental cycles.
