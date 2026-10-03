# Main Line 4 — Incidence rank and induced paths in the intersection graph

---

## Research Line — Introduction

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_introduction -->

Let \(H\) be a finite linear \(3\)-graph with \(n\) vertices and \(m\) edges. Let \(N\) be its real \(n\times m\) vertex-edge incidence matrix. Let \(F\) be the intersection graph of \(H\): the vertices of \(F\) are the edges of \(H\), and two vertices of \(F\) are adjacent precisely when the corresponding hyperedges intersect.

The target inequality in this approach is
\[
\ell\,\operatorname{rank}_{\mathbb R}N\ge 3m. \tag{1}
\]
Since \(\operatorname{rank}N\le n\), (1) immediately implies
\[
m\le \frac{\ell}{3}n. \tag{2}
\]

---

## Research Line — Linear paths and induced graph paths

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_linear_paths_and_induced_graph_paths -->

### Lemma 1

A sequence of distinct hyperedges
\[
e_1,\ldots,e_t
\]
forms a linear hypergraph path if and only if the corresponding vertices form an induced path in \(F\).

#### Proof
If the hyperedges form a linear path, consecutive edges intersect and nonconsecutive edges are disjoint, so their intersection graph is exactly a graph path.

Conversely, assume \(e_1,\ldots,e_t\) form an induced path in \(F\). Proceed by induction on \(t\). By induction, \(e_1,\ldots,e_{t-1}\) can be ordered as a linear hypergraph path. Let
\[
v=e_{t-1}\cap e_t.
\]
Inducedness implies that \(e_t\) is disjoint from every \(e_i\) with \(i\le t-2\). Linearity implies that
\[
e_t\cap e_{t-1}=\{v\}.
\]
Thus \(e_t\setminus\{v\}\) consists of two new vertices, and appending them after \(v\) extends the hypergraph path. ∎

Hence
\[
H\text{ is }P_\ell^{(3)}\text{-free}
\iff
F\text{ is induced-}P_\ell\text{-free}. \tag{3}
\]

---

## Research Line — Realizability of the intersection graph

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_realizability_of_the_intersection_graph -->

The graph \(F\) is not arbitrary.

For each vertex \(x\in V(H)\), let
\[
C_x=\{e\in E(H):x\in e\}.
\]
This is a clique of \(F\).

### Lemma 2

The indexed clique family \(\{C_x:x\in V(H)\}\) has the following properties.

1. Every vertex of \(F\) belongs to exactly three cliques.
2. Every edge of \(F\) belongs to exactly one clique.

Conversely, any graph equipped with an indexed family of cliques satisfying these two properties is the intersection graph of a linear \(3\)-graph.

#### Proof
A hyperedge has exactly three vertices, so its corresponding vertex of \(F\) belongs to exactly the three cliques indexed by those vertices. If two hyperedges intersect, linearity gives a unique common vertex, so the corresponding graph edge lies in exactly one \(C_x\).

Conversely, suppose a graph \(F\) has cliques \(C_x\) satisfying the two conditions. For a graph vertex \(q\), define
\[
E_q=\{x:q\in C_x\}.
\]
The first condition gives \(|E_q|=3\). If \(q,q'\) are adjacent, the graph edge \(qq'\) lies in a unique \(C_x\), so
\[
E_q\cap E_{q'}=\{x\}.
\]
If \(q,q'\) are nonadjacent, they lie together in no \(C_x\), so \(E_q\cap E_{q'}=\varnothing\). Thus the triples \(E_q\) form a linear \(3\)-graph whose intersection graph is \(F\). ∎

Any proof of (1) may therefore use the three-clique realization furnished by Lemma 2. A theorem for arbitrary induced-path-free graphs is unnecessarily general.

---

## Research Line — The spectral identity

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_the_spectral_identity -->

### Lemma 3

\[
N^{T}N=3I_m+A(F). \tag{4}
\]
Consequently
\[
\operatorname{rank}N
=
m-\operatorname{mult}_F(-3), \tag{5}
\]
where \(\operatorname{mult}_F(-3)\) is the multiplicity of the adjacency eigenvalue \(-3\).

#### Proof
The \((e,f)\)-entry of \(N^TN\) is \(|e\cap f|\). It is \(3\) when \(e=f\), \(1\) when \(e\ne f\) and the two hyperedges intersect, and \(0\) otherwise. This proves (4).

Over \(\mathbb R\),
\[
\ker(N^TN)=\ker N.
\]
Thus \(N\) and \(N^TN\) have the same rank. Since \(3I+A(F)\) is symmetric, its nullity equals the multiplicity of \(-3\) as an eigenvalue of \(A(F)\), proving (5). ∎

Therefore the one-third problem is equivalently a bound on the \(-3\) eigenspace inside the realizable class of Lemma 2.

---

## Research Line — A weighted rank inequality

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_a_weighted_rank_inequality -->

### Theorem 4

Assign weights \(0\le w_e\le1\) to the edges of \(H\). Put
\[
W=\sum_e w_e,
\qquad
d_w(v)=\sum_{e\ni v}w_e.
\]
If
\[
d_w(v)\le D
\qquad\text{for every }v,
\]
then
\[
\operatorname{rank}N\ge \frac{3W}{D+2}. \tag{6}
\]

#### Proof
Let
\[
R=\operatorname{diag}(w_e)
\]
and
\[
Q=R^{1/2}N^TNR^{1/2}.
\]
Then \(Q\) is positive semidefinite and
\[
\operatorname{rank}Q\le\operatorname{rank}N.
\]
Since every hyperedge has size three,
\[
\operatorname{tr}Q=3W.
\]

By linearity,
\[
Q_{ee}=3w_e,
\]
and for \(e\ne f\),
\[
Q_{ef}=
\begin{cases}
\sqrt{w_ew_f},&e\cap f\ne\varnothing,\\
0,&e\cap f=\varnothing.
\end{cases}
\]
Hence
\[
\operatorname{tr}(Q^2)
=
9\sum_e w_e^2
+
2\sum_{e<f,\ e\cap f\ne\varnothing}w_ew_f. \tag{7}
\]

On the other hand,
\[
\sum_v d_w(v)^2
=
3\sum_e w_e^2
+
2\sum_{e<f,\ e\cap f\ne\varnothing}w_ew_f, \tag{8}
\]
because every intersecting pair has a unique common vertex. Combining (7) and (8),
\[
\operatorname{tr}(Q^2)
=
6\sum_e w_e^2+\sum_v d_w(v)^2.
\]
Since \(0\le w_e\le1\),
\[
\sum_e w_e^2\le W.
\]
Also,
\[
\sum_v d_w(v)^2
\le
D\sum_v d_w(v)
=
3DW.
\]
Therefore
\[
\operatorname{tr}(Q^2)\le 3(D+2)W.
\]
For a positive semidefinite matrix,
\[
\operatorname{rank}Q
\ge
\frac{(\operatorname{tr}Q)^2}{\operatorname{tr}(Q^2)}.
\]
Substituting the preceding estimates gives
\[
\operatorname{rank}N
\ge
\operatorname{rank}Q
\ge
\frac{9W^2}{3(D+2)W}
=
\frac{3W}{D+2}.
\]
∎

### Corollary 5

If \(\Delta(H)\le \ell-2\), then
\[
\ell\,\operatorname{rank}N\ge 3m. \tag{9}
\]

#### Proof
Put
\[
t=\frac{2}{\ell-\Delta(H)}
\]
and assign the constant weight \(w_e=t\) to every edge. Since \(\Delta(H)\le\ell-2\), we have \(0<t\le1\). Then
\[
W=tm,
\qquad
D=t\Delta(H),
\]
and
\[
D+2=t\Delta(H)+2=t\ell.
\]
Theorem 4 gives
\[
\operatorname{rank}N
\ge
\frac{3tm}{t\ell}
=
\frac{3m}{\ell}.
\]
∎

Thus every counterexample to (1) must satisfy
\[
\Delta(H)\ge \ell-1. \tag{10}
\]

The low-degree range is completely settled.

---

## Research Line — Nullity and terminal-pair complexity

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_nullity_and_terminal_pair_complexity -->

The rank problem also receives information from the terminal-pair graph of nonspecial edges.

Let \(T\) be that graph, let \(h\) be the number of distinct unique entrances of nonspecial edges, and let \(s\) be the number of special edges.

### Proposition 6

\[
\operatorname{nullity}(N)\le \beta(T)+h+s. \tag{11}
\]

#### Proof
For the nonspecial columns, write
\[
N_{\mathrm{ns}}=B+R
\]
as follows: \(B\) is the ordinary \(0/1\) incidence matrix of \(T\), and the column of \(R\) corresponding to a nonspecial edge is the standard basis vector indexed by its unique entrance. Since \(R\) is supported on \(h\) rows,
\[
\operatorname{rank}R\le h.
\]
Hence
\[
\operatorname{rank}N_{\mathrm{ns}}
\ge
\operatorname{rank}B-h.
\]
The real \(0/1\) incidence matrix of a graph has nullity at most its cycle rank, so
\[
\operatorname{nullity}(N_{\mathrm{ns}})\le \beta(T)+h.
\]
Adding the \(s\) special columns can increase nullity by at most \(s\). ∎

Thus a bound on \(\beta(T)+h\) would also yield a rank theorem.

---

## Research Line — What a counterexample must look like

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_what_a_counterexample_must_look_like -->

Several simple classes cannot contain a counterexample to (1).

The low-degree class is excluded by Corollary 5.

If the intersection graph \(F\) is chordal, then the clique-tree structure and the three-clique realization imply
\[
m\le \frac32 n.
\]
More generally, excess above \(3n/2\) forces linearly many edge-disjoint linear cycles in \(H\). Hence a dense counterexample must have substantial cycle structure.

A bounded matching number is not enough to imply (1); there are induced-path-free realizable examples showing that this parameter alone only yields a weaker asymptotic coefficient. Therefore a successful rank proof must use the full incidence realization, not merely coarse graph sparsity.

There are also linear \(3\)-graphs with no special edges and positive incidence nullity. In particular,
\[
\operatorname{nullity}(N)\le s
\]
is false, and nonspecial incidence columns need not be independent.

---

## Research Line — The remaining theorem

<!-- research_line_id: incidence_rank_and_induced_paths_in_the_intersection_graph_the_remaining_theorem -->

All preceding statements reduce the one-third upper bound to the high-degree realizable case.

### Open problem

Let \(F\) be induced-\(P_\ell\)-free and equipped with an indexed clique family such that every vertex of \(F\) belongs to exactly three cliques and every edge of \(F\) belongs to exactly one. Let \(N\) be the corresponding incidence matrix. Prove
\[
\operatorname{rank}N\ge \frac{3m}{\ell}. \tag{12}
\]

Equivalently, prove (12) for every \(P_\ell^{(3)}\)-free linear \(3\)-graph satisfying \(\Delta(H)\ge\ell-1\).

Two weaker statements would also advance the argument:

1. find weights with \(W\) a fixed positive proportion of \(m\) and \(D\) sufficiently smaller than \(\ell\), so that Theorem 4 improves the current coefficient;
2. prove a bound on \(\beta(T)+h\) strong enough that Proposition 6 forces the desired rank.

The unresolved step is therefore confined to the high-degree part of the three-clique realizability class.
