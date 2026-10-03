# Main Line 5 — Induction on the complement of a longest path

---

## Research Line — Introduction

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_introduction -->

Fix \(\ell\ge2\). This approach seeks to prove
\[
3|E(H)|\le \ell |V(H)| \tag{1}
\]
for every \(P_\ell^{(3)}\)-free linear \(3\)-graph \(H\), by induction on \(|V(H)|\).

Let
\[
P=(e_1,\ldots,e_k)
\]
be a longest linear path in \(H\). Put
\[
X=V(P),\qquad Y=V(H)\setminus X.
\]
Since \(P\) is a \(k\)-edge linear \(3\)-uniform path,
\[
|X|=2k+1. \tag{2}
\]
Let
\[
m_Y=|E(H[Y])|
\]
and let \(e_X\) be the number of edges of \(H\) that meet \(X\). Thus
\[
|E(H)|=m_Y+e_X. \tag{3}
\]

---

## Research Line — Inductive reduction

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_inductive_reduction -->

### Lemma 1

Assume the inductive inequality
\[
3m_Y\le \ell |Y|.
\]
Define
\[
D_Y=\ell |Y|-3m_Y.
\]
Then (1) is equivalent to
\[
3e_X\le \binom{|X|}{2}+(\ell-k)|X|+D_Y. \tag{4}
\]

#### Proof
Using (3),
\[
3|E(H)|
=
3m_Y+3e_X.
\]
Hence (1) is equivalent to
\[
3e_X
\le
\ell |X|+\ell |Y|-3m_Y
=
\ell |X|+D_Y. \tag{5}
\]
By (2),
\[
\binom{|X|}{2}
=
\frac{(2k+1)(2k)}2
=
k(2k+1)
=
k|X|.
\]
Therefore
\[
\ell |X|
=
\binom{|X|}{2}+(\ell-k)|X|,
\]
and (5) becomes (4). ∎

When \(k=\ell-1\), the longest possible value in a \(P_\ell^{(3)}\)-free graph, (4) reduces to
\[
3e_X\le \binom{|X|}{2}+|X|+D_Y. \tag{6}
\]

Equation (4) is the entire inductive problem. The first term depends only on unordered pairs of vertices of \(X\); the second records the difference between the forbidden length and the actual longest-path length; the third is the amount by which \(H[Y]\) falls below the inductive extremal bound.

---

## Research Line — Why unordered pairs of \(X\) are the natural local resource

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_why_unordered_pairs_of_x_are_the_natural_local_resource -->

Linearity implies that an unordered pair of vertices belongs to at most one hyperedge. Thus every edge meeting \(X\) that contains two vertices of \(X\) determines a unique pair in
\[
\binom{X}{2}. \tag{7}
\]

The difficulty is caused by edges that meet \(X\) in only one vertex. Longest-path maximality must control these edges indirectly. If such an edge could be inserted into or appended to \(P\) without creating an additional intersection, then \(P\) would not be longest. Therefore every one-vertex intersection with \(X\) is accompanied by an obstruction elsewhere on \(P\), or by a restriction on the structure of \(H[Y]\).

The desired proof of (4) is a uniform way of converting those restrictions into the three terms on its right-hand side.

---

## Research Line — Deletion and the change in extremal deficit

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_deletion_and_the_change_in_extremal_deficit -->

The third term \(D_Y\) cannot be treated as a harmless remainder. It records genuine missing edges outside the longest path.

For a real number \(d\), define the \(d\)-deficit of a hypergraph \(G\) by
\[
r_d(G)=d|V(G)|-|E(G)|.
\]

### Lemma 2

Let \(S\subseteq V(H)\), and let \(N_H(S)\) be the set of hyperedges meeting \(S\). Then
\[
r_d(H-S)
=
r_d(H)+|N_H(S)|-d|S|. \tag{8}
\]

#### Proof
Since
\[
|E(H-S)|=|E(H)|-|N_H(S)|,
\]
we have
\[
\begin{aligned}
r_d(H-S)
&=d(|V(H)|-|S|)-(|E(H)|-|N_H(S)|)\\
&=r_d(H)+|N_H(S)|-d|S|.
\end{aligned}
\]
∎

The identity is elementary, but it prevents a common error: deleting a vertex or a small set while preserving density does not by itself contradict minimality.

### Lemma 3

Let \(H\) be vertex-minimal among linear \(3\)-graphs satisfying all of the following:

1. \(|E(H)|/|V(H)|\ge d\);
2. \(\delta(H)\ge d+1\);
3. \(H\) contains a fixed nonspecial edge together with a fixed maximum path \(P\) that witnesses its nonspeciality.

Assume in addition that
\[
|E(H)|=d|V(H)|.
\]
Let \(w\notin V(P)\) satisfy
\[
d_H(w)\le d.
\]
Then there is a vertex \(u\ne w\) such that
\[
d_H(u)=d+1,\qquad d_{H-w}(u)=d,
\]
and exactly one hyperedge contains the pair \(\{u,w\}\).

#### Proof
Since \(w\notin V(P)\), deleting \(w\) preserves the fixed path and therefore preserves the specified nonspecial witness. Lemma 2 gives
\[
r_d(H-w)
=
r_d(H)+d_H(w)-d
\le0,
\]
so \(H-w\) still has density at least \(d\).

If \(\delta(H-w)\ge d+1\), then \(H-w\) would satisfy all three defining properties of \(H\), contradicting vertex-minimality. Hence some vertex \(u\) satisfies
\[
d_{H-w}(u)\le d.
\]
Since \(\delta(H)\ge d+1\),
\[
d_H(u)\ge d+1.
\]
Linearity implies that deleting \(w\) removes at most one edge through \(u\), because two distinct hyperedges containing both \(u\) and \(w\) would share two vertices. Therefore
\[
d_H(u)-1\le d_{H-w}(u)\le d.
\]
It follows that
\[
d_H(u)=d+1,\qquad d_{H-w}(u)=d,
\]
and exactly one hyperedge contains \(\{u,w\}\). ∎

Thus deletion of a low-degree vertex outside the witness path produces a specific edge joining it to a degree-\((d+1)\) vertex; it does not by itself contradict minimality.

---

## Research Line — A path-forest consequence of threshold deletion

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_a_path_forest_consequence_of_threshold_deletion -->

The following elementary statement is useful whenever a threshold set \(D\) has already been shown to contain every edge not lying on a fixed maximum path.

### Lemma 4

Suppose \(D\subseteq V(H)\) has the property that every edge of \(H-D\) belongs to the edge set of a linear path \(P\). Then \(H-D\) is a disjoint union of linear paths and isolated vertices. In particular,
\[
\Delta(H-D)\le2
\]
and
\[
|E(H-D)|\le \frac{|V(H)\setminus D|}{2}. \tag{9}
\]

#### Proof
A subset of the edge set of a linear path has no intersections except between consecutive selected path edges. Its nonempty connected components are therefore linear paths.

If the nonempty components have \(t_1,\ldots,t_c\) edges, they use
\[
\sum_{i=1}^c(2t_i+1)=2|E(H-D)|+c
\]
vertices. Hence
\[
2|E(H-D)|+c\le |V(H)\setminus D|,
\]
which implies (9). ∎

If every vertex outside \(D\) has degree at least \(q+1\), Lemma 4 immediately implies that every such vertex lies in at least \(q-1\) edges meeting \(D\).

---

## Research Line — Vertices of degree above the minimum threshold

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_vertices_of_degree_above_the_minimum_threshold -->

A dense equality case has many vertices whose degree is strictly above the minimum degree.

### Lemma 5

Suppose
\[
|E(H)|=dn
\qquad\text{and}\qquad
\delta(H)\ge d+1.
\]
Let
\[
R=\{v:d_H(v)\ge d+2\}.
\]
Then
\[
|R|\ge 4d-1. \tag{10}
\]
Consequently, every \(q\)-edge path omits at least
\[
4d-2q-2 \tag{11}
\]
vertices of \(R\).

#### Proof
The total degree excess above \(d+1\) is
\[
\sum_v(d_H(v)-(d+1))
=
3dn-(d+1)n
=
(2d-1)n. \tag{12}
\]
Vertices outside \(R\) contribute nothing to (12). By linearity,
\[
d_H(v)\le \frac{n-1}{2}
\]
for every vertex \(v\), because the \(2d_H(v)\) vertices paired with \(v\) in incident hyperedges are all distinct. Hence each vertex of \(R\) contributes at most
\[
\frac{n-1}{2}-(d+1)
=
\frac{n-2d-3}{2}
\]
to (12). Therefore
\[
(2d-1)n
\le
|R|\frac{n-2d-3}{2},
\]
so
\[
|R|
\ge
\frac{2(2d-1)n}{n-2d-3}
>
4d-2.
\]
Since \(|R|\) is integral, (10) follows.

A \(q\)-edge linear \(3\)-uniform path has \(2q+1\) vertices, so it contains at most \(2q+1\) vertices of \(R\). Subtracting from (10) gives (11). ∎

Thus even when \(P\) is nearly spanning relative to the forbidden length, a dense equality case contains many high-degree vertices outside \(P\).

---

## Research Line — The remaining inequality

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_the_remaining_inequality -->

The induction closes if the following statement is proved.

### Open problem

For every longest \(k\)-edge path \(P\) in a \(P_\ell^{(3)}\)-free linear \(3\)-graph \(H\), with
\[
X=V(P),\qquad Y=V(H)\setminus X,
\]
prove
\[
3e_X\le \binom{|X|}{2}+(\ell-k)|X|+D_Y, \tag{13}
\]
where
\[
D_Y=\ell |Y|-3|E(H[Y])|.
\]

The first term in (13) is exhausted by distinct pairs of vertices of \(X\). The second term is smaller when the longest path is close to length \(\ell\), so the case \(k=\ell-1\) is the most restrictive. The third term must account for the edge families that cannot be represented by distinct pairs of \(X\).

A sufficient statement would be the following: whenever the edges meeting \(X\) require \(r\) more units than can be represented by the first two terms of (13), prove
\[
D_Y\ge r. \tag{14}
\]
Lemmas 2–5 describe mechanisms by which missing edges in \(H[Y]\) can arise, but they do not yet prove (14).

---

## Research Line — Obstruction to the naive deletion argument

<!-- research_line_id: induction_on_the_complement_of_a_longest_path_obstruction_to_the_naive_deletion_argument -->

A deletion preserving density does not imply that a vertex-minimal counterexample has been contradicted. Lemma 3 gives the precise conclusion: the deleted vertex is joined by a unique hyperedge to a vertex whose degree falls from \(d+1\) to \(d\).

Accordingly, a proof of (13) must follow the structure created when a deletion is restored. Merely showing that a set can be deleted without lowering the density does not establish the required deficit \(D_Y\).
