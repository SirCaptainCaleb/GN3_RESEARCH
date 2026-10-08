# Article I — deletion-cover compatibility and global obstruction structure

---

## Section — Introduction

<!-- section_id: deletion_covers_and_the_support_graph_introduction -->

Let \(H\) be a finite boundary \(3\)-tournament. A tight path is a sequence
\[
(v_1,\ldots ,v_m)
\]
of distinct vertices such that \((v_i,v_{i+1},v_{i+2})\) is a tight triple for every \(1\le i\le m-2\). A path cover is a collection of vertex-disjoint tight paths whose supports partition \(V(H)\), and \(\operatorname{pc}(H)\) denotes the minimum number of paths in a cover.

Assume throughout that \(H\) is a counterexample of minimum order to
\[
\operatorname{pc}(H)\le 2.
\]
Then \(\operatorname{pc}(H)=3\). For every \(x\in V(H)\), minimality gives a two-cover of \(H-x\). Neither path can be empty, and \(H-x\) cannot be Hamiltonian, since a Hamilton path of \(H-x\) together with the one-vertex path \(x\) would be a two-cover of \(H\). Thus every deletion cover at \(x\) consists of two nonempty paths.

For each \(x\in V(H)\), choose a deletion cover
\[
F_x=P_x\mid Q_x
\]
that minimizes \(|P_x|^2+|Q_x|^2\) among all two-covers of \(H-x\). Equivalently, choose a deletion cover whose two component orders have minimum possible imbalance.

---

## Section — Defect span

<!-- section_id: deletion_covers_and_the_support_graph_defect_span -->

For an ordering \(\pi=(v_1,\ldots ,v_n)\), an index \(i\), \(2\le i\le n-1\), is a defect center if
\[
(v_{i-1},v_i,v_{i+1})
\]
is non-tight. The defect span of \(\pi\) is \(0\) when there is no defect center and otherwise is
\[
\max D-\min D+1,
\]
where \(D\) is the set of defect centers.

**Lemma 1.** \(H\) has a two-cover if and only if it has a spanning ordering of defect span at most \(2\).

**Proof.** If \(P=(v_1,\ldots ,v_j)\) and \(Q=(v_{j+1},\ldots ,v_n)\) form a two-cover, then all defect centers of the concatenated ordering lie among \(j,j+1\). Conversely, if all defect centers lie among two consecutive indices \(j,j+1\), then
\[
(v_1,\ldots ,v_j)\quad\text{and}\quad (v_{j+1},\ldots ,v_n)
\]
are tight paths and form a two-cover. \(\square\)

Let \(H-x=P\mid Q\), where
\[
P=(p_1,\ldots ,p_r),\qquad Q=(q_1,\ldots ,q_s).
\]
The ordering
\[
(p_1,\ldots ,p_r,x,q_1,\ldots ,q_s)
\]
has possible defect centers only at the three positions adjacent to the join. The two outer join triples are necessarily non-tight: if \((p_{r-1},p_r,x)\) were tight, then \((P,x)\mid Q\) would be a two-cover of \(H\), and the other side is symmetric. Hence every deletion cover gives a spanning ordering of defect span \(3\).

If the middle triple \((p_r,x,q_1)\) is also non-tight, boundary reversal gives
\[
(x,p_r,p_{r-1}),\qquad (q_1,x,p_r),\qquad (q_2,q_1,x)
\]
tight whenever the displayed vertices exist. Thus
\[
(q_2,q_1,x,p_r,p_{r-1})
\]
is a tight path. The problem is therefore to reduce a spanning ordering of defect span \(3\) to one of defect span at most \(2\).

---

## Section — Compatibility of deletion covers

<!-- section_id: deletion_covers_and_the_support_graph_compatibility_of_deletion_covers -->

Two path covers of the same vertex set are support-compatible if they induce the same partition into path supports. They are compatible if they are support-compatible and every two vertices lying in one common support occur in the same relative order in the two path orders. When two deletion covers omit different vertices, these definitions are applied after restricting both covers to their common vertex set.

**Lemma 2 (compatibility gluing).** Let \(D\subseteq V(H)\), \(|D|\ge4\), and for every \(d\in D\) let \(F_d\) be a cover of \(H-d\) by at most two tight paths. If the covers are pairwise compatible on their common domains, then \(H\) has a two-cover.

**Proof.** For distinct \(u,v\), choose \(d\in D-\{u,v\}\). The relation saying that \(u,v\) lie in the same path of \(F_d\), together with their relative order when they do, is independent of \(d\) by compatibility. Any three vertices survive in some \(F_d\), so the same-path relation is transitive. It therefore partitions \(V(H)\) into at most two classes; otherwise three representatives from distinct classes survive in one cover.

Each class inherits a total order. Take three consecutive vertices in one class. A deletion label can be chosen outside them, and in the corresponding \(F_d\) these three vertices occur consecutively in the inherited order. Their ordered triple is tight. Hence every class is a tight path. These one or two paths cover \(H\). \(\square\)

The next lemma gives the local form of a compatible pair.

**Lemma 3 (insertion slots).** Let \(F_a\) and \(F_b\) be compatible deletion covers. Then the omitted vertices \(a\) and \(b\) are inserted into the same common support. Their insertion slots in the common order are equal or adjacent. If the slots are adjacent, there is a tight triple reversing the two inserted labels across the unique common vertex between the slots.

**Proof.** On \(V(H)-\{a,b\}\), compatibility gives two ordered supports, say \(P,Q\). In \(F_a\), the vertex \(b\) is inserted into one of them; in \(F_b\), the vertex \(a\) is inserted into one of them. If they are inserted into different supports, augmenting both supports simultaneously gives a two-cover of \(H\), a contradiction. Thus both are inserted into the same support, say
\[
P=(p_1,\ldots ,p_m).
\]

If the two slots are separated by at least one entire slot, insert both vertices into \(P\) at their respective positions. No new consecutive triple contains both inserted vertices; each consecutive triple is inherited from \(P\), \(F_a\), or \(F_b\). This again gives a two-cover with \(Q\). Hence the slots are equal or adjacent.

In the adjacent case write the common order as \(L,z,R\), with
\[
F_b=(L,a,z,R)\mid Q,\qquad F_a=(L,z,b,R)\mid Q.
\]
Every consecutive triple of \((L,a,z,b,R)\) is known to be tight except possibly \((a,z,b)\). If this triple were tight, the displayed path together with \(Q\) would cover \(H\) by two paths. Hence \((a,z,b)\) is non-tight, so its boundary flip
\[
(b,z,a)
\]
is tight. \(\square\)

### Three compatible covers force a reversal

### A connected support path already closes the theorem

**Lemma 6 (connected support path closure).** Let one deletion cover (F_x) be selected for every vertex (xin V(H)), and let (J) be the resulting support graph. If (J) is a connected path, then (H) has a two-cover.

**Proof.** Put
[
n=|V(H)|.
]
There is exactly one selected edge (e_x) for each label (x), so (J) has exactly (n) edges. Since it is a connected path, write
[
S_0-S_1-cdots-S_n
]
for its support vertices, with the edge (S_{i-1}S_i) labeled (x_i).

For any vertex label (z
e x_i), exactly one of (S_{i-1},S_i) contains (z), because the two endpoint supports of (e_{x_i}) partition
[
V(H)-{x_i}.
]
For (z=x_i), neither endpoint contains (z).

Fix (j). The label (x_j) is absent from both
[
S_{j-1},S_j.
]
Moving left from (S_{j-1}), membership of (x_j) alternates across each preceding edge, since none of those edges is labeled (x_j). Therefore
[
x_jin S_0
quadLongleftrightarrowquad
j 	ext{is even}.
]
Likewise, moving right from (S_j),
[
x_jin S_n
quadLongleftrightarrowquad
n-j 	ext{is odd}.
]

If (n) is even, the second condition is equivalent to (j) odd. Hence
[
S_0={x_j:j 	ext{even}},
qquad
S_n={x_j:j 	ext{odd}}.
]
The two supports are disjoint and their union is (V(H)). Every support vertex of (J) is the support of a tight path in a selected deletion cover, so both (S_0) and (S_n) are Hamiltonian. They therefore form a two-cover of (H).

If (n) is odd, then
[
n-j 	ext{odd}
quadLongleftrightarrowquad
j 	ext{even},
]
so
[
S_n=S_0.
]
But the support vertices on a path are distinct. Equivalently, identifying the equal endpoints closes the displayed walk into a cycle, contradicting the assumption that (J) is a path in a forest.

Thus a connected support path cannot occur in a counterexample. (square)

**Corollary 7 (global no-reversal support residue).** In a counterexample, after excluding the reversal/order-disagreement outcome of Corollary 5, the selected support graph cannot be a connected forest. Hence the only remaining support-graph geometries are

1. a disconnected union of support paths; or
2. the unique spanning odd cycle from the support-graph dichotomy.

Thus the connected forest case is closed at arbitrary order. The remaining forest issue is precisely the already-identified **component escape** between distinct support-path components, not any internal tree or branching geometry.

### Compatible pairs have no quiet endpoint-slot residue

The insertion-slot lemma can be sharpened at an endpoint.

**Proposition (compatible-pair trichotomy).** Let \(F_a,F_b\) be deletion covers of \(H-a,H-b\) that are support-compatible. Then at least one of the following holds:

1. their common-support orders disagree, hence a displayed-edge reversal is forced by the order-disagreement machinery;
2. \(H\) has a two-cover;
3. \(H\) contains a Hamiltonian four-support with non-Hamiltonian path-cover-two complement;
4. the two insertion slots are adjacent, hence Lemma 3 gives a reversing tight triple.

In particular, a compatible pair has no purely neutral equal-endpoint-slot residue.

**Proof.** If the common-support orders disagree, outcome 1 holds. Otherwise \(F_a,F_b\) are compatible, so Lemma 3 puts the omitted labels \(a,b\) into the same common support in equal or adjacent insertion slots.

Adjacent slots give outcome 4.

Suppose the slots are equal and internal, between consecutive common vertices \(u,v\). Then both
\[
(u,a,v),\qquad (u,b,v)
\]
are tight. The compatible one-vertex extension lemma makes
\[
\{u,v,a,b\}
\]
Hamiltonian. In a minimum counterexample its complement has path-cover number two and is non-Hamiltonian, giving outcome 3.

It remains that the common slot is an endpoint gap. Write the common ordered support as
\[
P=(p_1,\ldots,p_m)
\]
and, after reversing if necessary,
\[
F_a=(b,p_1,\ldots,p_m)\mid Q,
\qquad
F_b=(a,p_1,\ldots,p_m)\mid Q.
\]
Exactly one of the two boundary orientations
\[
(a,b,p_1),\qquad (b,a,p_1)
\]
is tight. In the first case
\[
(a,b,p_1,\ldots,p_m)
\]
is a tight path; in the second
\[
(b,a,p_1,\ldots,p_m)
\]
is. Together with \(Q\), either order gives a spanning two-cover of \(H\). This is outcome 2. \(\square\)

Consequently, in the spanning odd-cycle support geometry, every adjacent pair of selected support edges immediately yields a reversal, a bounded Hamiltonian four-support, or a two-cover. Thus the odd-cycle geometry cannot support an additional quiet neutral omission-swap recurrence.


---

## Section — The support graph

<!-- section_id: deletion_covers_and_the_support_graph_the_support_graph -->

Let \(J\) be the graph whose vertices are the distinct supports occurring among the selected covers \(F_x\), with an edge \(e_x\) joining the two supports of \(F_x\). The edge is labeled by \(x\). The graph is simple: its two endpoint supports have union \(V(H)-\{x\}\), so they determine the label \(x\).

**Lemma 4 (support-graph dichotomy).** Either \(J\) is a forest, or \(V(H)\) has odd order \(2k+1\), every vertex of \(H\) occurs as an edge label, and \(J\) is one cycle of length \(2k+1\). In the cyclic case every support has order \(k\).

**Proof.** Fix \(z\in V(H)\). On every edge \(e_x\) with \(x\ne z\), exactly one endpoint support contains \(z\); on \(e_z\), if present, neither endpoint contains \(z\). Hence membership of \(z\) gives a bipartition of \(J-e_z\).

Suppose \(J\) contains a cycle \(C\) and \(e_z\in E(C)\). The path \(C-e_z\) joins two supports omitting \(z\), while membership of \(z\) alternates at each edge. Thus \(|C|-1\) is even, so \(C\) is odd.

If some \(y\in V(H)\) is not a label of \(C\), membership of \(y\) alternates around all edges of the odd cycle, which is impossible. Therefore the labels of \(C\) are all vertices of \(H\). Since edge labels are distinct, no selected edge lies outside \(C\). Every support vertex is incident with a selected edge, so \(J=C\). On each edge, the endpoint support sizes sum to \(n-1\). Alternating this equality around an odd cycle forces all support sizes to be \((n-1)/2\). \(\square\)

Two selected covers are support-compatible exactly when their edges of \(J\) share a support vertex.

**Lemma 5.** For distinct labels \(a,b\), the selected covers \(F_a,F_b\) are support-compatible if and only if \(e_a,e_b\) are adjacent in \(J\).

**Proof.** A shared endpoint of \(e_a,e_b\) is a common path support, so the restricted support partitions agree.

Conversely, write \(F_a=A\mid B\) with \(b\in A\), and assume that the restrictions of \(F_a,F_b\) to \(H-\{a,b\}\) have the same support partition. Since neither component of a deletion cover is a singleton, the two restricted classes are \(A-\{b\}\) and \(B\). In \(F_b\), the restored vertex \(a\) must join one of them. If it joins \(B\), then \(A\) and \(B\cup\{a\}\) are disjoint Hamiltonian supports covering \(H\), a contradiction. Hence it joins \(A-\{b\}\), and \(B\) is a support of both selected covers. \(\square\)

Thus the graph of support compatibility is the line graph \(L(J)\).

---

## Section — Support-compatible families

<!-- section_id: deletion_covers_and_the_support_graph_support_compatible_families -->

A large support-compatible family has only one varying support.

**Lemma 6 (localization).** Let \(D\subseteq V(H)\), \(|D|\ge3\), and suppose \(\{F_d:d\in D\}\) is pairwise support-compatible. Then there are disjoint sets \(X,Q\) with \(V(H)=X\cup Q\), \(D\subseteq X\), such that
\[
F_d=(X-\{d\})\mid Q
\]
for every \(d\in D\). The set \(Q\) is Hamiltonian, every \(X-\{d\}\) is Hamiltonian, and \(X\) is not Hamiltonian.

**Proof.** For two vertices \(u,v\), choose \(d\in D-\{u,v\}\) and declare \(u\sim v\) when they lie in the same path of \(F_d\). Support compatibility makes the definition independent of \(d\). Transitivity follows by viewing any three vertices in one deletion cover; when the three vertices themselves exhaust \(D\), any vertex outside \(D\) supplies the same comparison. Thus \(\sim\) has two equivalence classes, say \(X,Q\).

The deletion labels cannot occupy both classes. If \(a\in D\cap X\) and \(b\in D\cap Q\), then one selected cover Hamiltonizes \(X\) and another Hamiltonizes \(Q\), giving a two-cover of \(H\). Hence \(D\subseteq X\) after relabeling. The asserted support partitions follow. If \(X\) were Hamiltonian, its Hamilton path together with a Hamilton path on \(Q\) would be a two-cover of \(H\). \(\square\)

The following endpoint comparison will be used repeatedly.

**Lemma 7 (endpoint comparison).** Suppose \(H-x=P\mid Q\) is a deletion cover and \(y\) is an endpoint of the displayed path \(Q\). Let \(G_y\) be a deletion cover at \(y\) that is support-incompatible with \(P\mid Q\) on \(H-\{x,y\}\). Put \(B=Q-\{y\}\). Then \(G_y\) has at least two edges joining distinct classes of
\[
P\mid B\mid\{x\}.
\]
If it has exactly two such edges and none joins \(P\) to \(B\), then \(B\cup\{x\}\) is Hamiltonian.

**Proof.** If there were only one edge joining distinct classes, deleting it from the two paths of \(G_y\) would leave three path blocks. The support partition would be one of
\[
(P\cup B)\mid\{x\},\qquad (P\cup\{x\})\mid B,\qquad P\mid(B\cup\{x\}).
\]
The first gives a two-cover of \(H\) after adjoining the two-vertex path \((x,y)\); the second would make \(P\cup\{x\}\) Hamiltonian and hence give \((P\cup\{x\})\mid Q\); the third is support-compatible with \(P\mid Q\) after deleting \(x\). All are impossible.

Assume there are exactly two interclass edges and neither joins \(P\) to \(B\). Both are incident with \(x\). Cutting them produces four blocks, so precisely one of \(P,B\) is split into two blocks. If \(B\) is split, \(x\) cannot be adjacent in the contracted two-path forest to the unique \(P\)-block, since that would make \(P\cup\{x\}\) Hamiltonian. Hence \(x\) joins the two \(B\)-blocks, making \(B\cup\{x\}\) Hamiltonian. If \(P\) is split, \(x\) cannot join both \(P\)-blocks for the same reason, so it joins the unique \(B\)-block and one \(P\)-block; again \(B\cup\{x\}\) is a tight path. \(\square\)

Applying the lemma at both endpoints of \(Q\) requires one additional case. Put \(Q=(q_0,\ldots ,q_m)\). If neither endpoint deletion cover contains an edge joining a surviving vertex of \(P\) to a surviving vertex of \(Q\), then both endpoint replacements of \(Q\) by \(x\) are Hamiltonian. If either replacement Hamilton path changes the inherited order of the surviving vertices of \(Q\), there is an order disagreement. Otherwise the insertion position of \(x\) in \((Q-\{q_0\})\cup\{x\}\) is either before \(q_1\) or between \(q_1,q_2\), since any later position permits \(q_0\) to be prepended and would make \(Q\cup\{x\}\) Hamiltonian. Symmetrically, the insertion position in \((Q-\{q_m\})\cup\{x\}\) is either after \(q_{m-1}\) or between \(q_{m-2},q_{m-1}\).

An adjacent insertion forces a displayed reversal. If the left replacement begins \((q_1,x,q_2,\ldots)\), then \((q_0,q_1,x)\) must be non-tight, and hence \((x,q_1,q_0)\) is tight. If the right replacement ends \((\ldots,q_{m-2},x,q_{m-1})\), then \((x,q_{m-1},q_m)\) must be non-tight, and hence \((q_m,q_{m-1},x)\) is tight.

The only remaining order-preserving case has replacement orders
\[
(x,q_1,\ldots ,q_m),\qquad (q_0,\ldots ,q_{m-1},x).
\]
Together with \(Q\), these give three deletion covers sharing the fixed support \(P\). Their singleton lifts form a triangle of equal-potential pairwise repartitions, and the two endpoint-replacement paths have an order disagreement on the common support \(\{x,q_1,\ldots ,q_{m-1}\}\). Thus opposite extreme insertion is a concrete recurrence configuration, not a Hamiltonian insertion of \(x\) into all of \(Q\). See [[leaf_endpoint_singleton_triangle01]].

---

## Section — The forest case

<!-- section_id: deletion_covers_and_the_support_graph_the_forest_case -->

### The forest case

Assume \(J\) is a forest. Let \(e_x=PQ\) be a leaf edge, with \(P\) the leaf support and \(Q\) its neighbor. Thus
\[
V(H)=P\mathbin{\dot\cup}Q\mathbin{\dot\cup}\{x\}.
\]
The detailed leaf analysis is carried by [[leaf_comparisons_in_deletion_support_forests]]. Its strongest consequence is that the forest route has a substantially cleaner normal form than the original one-endpoint comparison suggests.

### Connected trees

Assume first that \(J\) is connected. For every leaf support \(P\) with neighbor \(Q\), all but at most one label \(y\in Q\) have a selected deletion cover \(F_y\) containing a consecutive pair with one endpoint in \(P\) and the other in \(Q-\{y\}\). Under the standing minimum-imbalance selection, the unique possible exceptional cover may be replaced by an equally balanced alternative. After at most one such reselection, either the selected support graph becomes disconnected, or it remains a connected tree with a leaf edge
\[
H-x=L\mid M
\]
such that every \(z\in M\) has a selected deletion cover \(F_z\) containing an edge joining \(L\) to \(M-\{z\}\).

In particular, fixing any Hamiltonian order
\[
M=(m_0,\ldots,m_s),
\]
both endpoint deletion covers \(F_{m_0}\) and \(F_{m_s}\) contain direct mixed edges between the two old supports. Thus the connected-tree branch does not need a preliminary endpoint merely to force interaction: direct mixing is simultaneously available at both ends.

**Proposition 8 (two-endpoint leaf normal form).** Under minimum-imbalance deletion-cover selection, if the selected support graph is a connected tree, then after changing at most one selected cover to an equally balanced alternative, either the support graph becomes disconnected or there is a leaf edge
\[
H-x=L\mid M,\qquad M=(m_0,\ldots,m_s),
\]
for which each endpoint deletion cover \(F_{m_i}\), \(i\in\{0,s\}\), contains an edge joining a surviving vertex of \(L\) to a surviving vertex of \(M\).

**Proof.** This is the paired-endpoint reduction proved in [[leaf_comparisons_in_deletion_support_forests]]. \(\square\)

Consequently the connected-tree case enters the direct-mixing hypothesis of the Remaining Lemma at either endpoint. If one continues the local endpoint analysis instead, the same cited Section shows independently at both ends that one obtains an order disagreement, a split inherited edge of \(M-\{m_i\}\), a leave-and-return path disturbance through \(L\), an end-edge reversal, strict quadratic-potential descent, or equal-potential recurrence between selected singleton lifts. The important global point is that these are now paired endpoint disturbances: neither endpoint is spent establishing the existence of a mixed edge.

### Disconnected forests

Let \(T\) be the tree component containing a leaf edge \(P Q\), and let \(D_T\) be its set of edge labels. For a Hamiltonian order on \(Q\) with endpoints \(a,b\), [[leaf_comparisons_in_deletion_support_forests]] gives the following dichotomy:

- if \(a,b\in D_T\), then at least one of \(F_a,F_b\) contains an edge joining \(P\) to the surviving part of \(Q\);
- otherwise at least one endpoint label has its selected edge in a different tree component of \(J\).

More strongly, among labels \(y\in Q\cap D_T\), at most one can fail to mix \(P\) with \(Q-\{y\}\); if \(Q\) contains any label outside \(D_T\), then no internal label is exceptional.

Hence the genuinely new residue of the disconnected-forest branch is not a split leaf support. It is component escape: an endpoint of the neighboring Hamilton path may index a selected deletion cover whose support edge lies in another tree component. Whenever both endpoint labels remain in the leaf component, the forest route again reaches the direct-mixing hypothesis of the Remaining Lemma.

Thus the forest case is reduced to two global interfaces:

1. direct mixed edges at one or, in the connected-tree normal form, both ends of a neighboring displayed path;
2. in a disconnected support forest, migration of an endpoint label to another support-tree component.

The earlier leaf-splitting alternative is absorbed by the leaf-comparison structure and need not be carried as a terminal forest residue.

### Component escape is not a terminal forest residue

The disconnected-forest alternative can now be treated at the same endpoint level as the connected-tree case.

**Corollary 9.** Let
[
H-x=Pmid Q,
qquad
Q=(q_0,ldots,q_m),
]
correspond to a leaf edge of an arbitrary selected support forest. Then, unless (H) already contains a bounded Hamiltonian support with two-coverable complement, an order disagreement, or an external reversal, at least one endpoint
[
yin{q_0,q_m}
]
has a selected deletion cover (F_y) containing an ordinary path edge joining (P) to (Q-{y}).

Consequently the endpoint disturbance theorem applies at some displayed endpoint of every leaf-neighbor path, regardless of whether the selected endpoint edge remains in the leaf's tree component.

**Proof.** If one endpoint cover already contains such a mixed edge, there is nothing to prove. Suppose neither endpoint cover mixes the two old supports. Lemma 13 of [[leaf_comparisons_in_deletion_support_forests]] then gives one of: a bounded Hamiltonian support, an order disagreement, or an adjacent-slot reversal. These are exactly the excluded successful disturbances. Hence the two endpoint covers cannot both be non-mixing in the unresolved branch. (square)

Combining this with
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]],
the forest route has only the following outputs at a leaf edge:
[
	ext{order disagreement},quad
	ext{split/leave-and-return},quad
	ext{external reversal},quad
	ext{strict }Phi	ext{-descent},quad
	ext{neutral omission swap},
]
or a two-cover/bounded-support conclusion.

Order disagreement and split/leave-and-return already collapse to the external-reversal interface in Article III. Thus the only genuinely quiet forest phenomenon is neutral omission-swap recurrence. The earlier “component escape” alternative is no longer independent.



### Neutral omission-swap recurrence is not a forest obstruction

The last quiet forest alternative also closes globally.

**Corollary 10 (forest recurrence closure).** In the forest branch, every leaf-endpoint comparison eventually yields one of
[
	ext{two-cover},quad
	ext{bounded Hamiltonian support},quad
	ext{order disagreement},quad
	ext{external reversal},quad
	ext{split/leave-and-return disturbance},quad
	ext{strict }Phi	ext{-descent}.
]
Neutral omission-swap recurrence is not an additional terminal alternative.

**Proof.** By Corollary 9, after bounded support, order disagreement, and external reversal are excluded, some displayed endpoint of every leaf-neighbor path enters the direct-mixing disturbance theorem
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]].
Its only quiet output is a neutral omission swap.

Continue such a neutral swap through the selected minimum-imbalance deletion covers as in
[[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]].
Corollary 12 of
[[three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component]]
shows that, in a selected support forest, no indefinitely neutral trajectory exists: every such continuation eventually leaves the neutral regime through a two-cover, bounded-support outcome, order disagreement, external reversal, split disturbance, or strict descent. (square)

Thus the selected-support forest is no longer an independent global obstruction. After the Article I support-graph reductions, every forest branch returns to the same successful disturbance interfaces already used by Articles III–VI.



---

## Section — The odd-cycle case

<!-- section_id: deletion_covers_and_the_support_graph_the_odd_cycle_case -->

Assume now that \(J\) is the cycle of Lemma 4. Write
\[
V(H)=\{d_0,\ldots ,d_{2k}\},
\]
and write the support vertices cyclically as \(S_0,\ldots ,S_{2k}\), where \(e_{d_i}=S_iS_{i+1}\). Membership alternation gives
\[
S_i=\{d_{i+1},d_{i+3},\ldots ,d_{i+2k-1}\},
\]
with indices modulo \(2k+1\).

If two consecutive selected covers have an order disagreement, Proposition 8 has its analogue immediately. Hence suppose consecutive selected covers are compatible. Their common support orders agree, so each \(S_i\) has a Hamilton order \(P_i\) used by both incident deletion covers.

### 6.1 Consecutive double deletions

For each \(i\), let \(T_i\) be any two-cover of
\[
H-\{d_i,d_{i+1}\},
\]
which exists by minimality. Put
\[
K_i=S_i-\{d_{i+1}\}=S_{i+2}-\{d_i\}.
\]

**Lemma 9.** For some \(i\), either \(T_i\) has an edge joining two distinct nonempty path pieces obtained by deleting an internal exchanged label from one of the incident selected covers, or the two inherited covers of the double deletion have an order disagreement.

**Proof.** Suppose neither event occurs for any \(i\). Then each exchanged label is an endpoint of the relevant support path, and deleting \(d_i,d_{i+1}\) leaves the same ordered supports \(K_i,S_{i+1}\). Let \(\varepsilon_i\in\{L,R\}\) denote the end of \(K_i\) at which \(d_{i+1}\) is restored to obtain \(P_i\), equivalently the end at which \(d_i\) is restored to obtain \(P_{i+2}\).

If \(\varepsilon_{i+2}=\varepsilon_i\), the two successive restorations at that end force the next removed label to equal the preceding one, contradicting the distinctness of the cycle labels. Hence
\[
\varepsilon_{i+2}\ne\varepsilon_i
\]
for every \(i\). Addition by \(2\) is one cycle modulo \(2k+1\). Following it around the odd number of indices reverses the end an odd number of times and returns to the starting index with the opposite value, a contradiction. \(\square\)

### 6.2 Rank transport

For consecutive compatible covers,
\[
S_i\cap S_{i+2}=S_i-\{d_{i+1}\}=S_{i+2}-\{d_i\}.
\]
Lemma 3 shows that \(P_i\) and \(P_{i+2}\) arise from a common order by inserting \(d_{i+1}\) and \(d_i\) in equal or adjacent slots. An adjacent-slot transition supplies a tight triple reversing the two inserted labels across the intervening common vertex.

**Lemma 10.** At least \(k-1\) of the \(2k+1\) step-two transitions use adjacent slots. Their number is congruent to \(k-1\pmod 2\), and every adjacent transposition of consecutive ranks \(1,\ldots ,k\) occurs at least once.

**Proof.** Follow the \(k\) positions of the support order while replacing \(d_{i+1}\) by \(d_i\) and advancing from \(S_i\) to \(S_{i+2}\). An equal-slot transition preserves the rank positions; an adjacent-slot transition applies one simple adjacent transposition. After one circuit, the deterministic replacement of labels induces a \(k\)-cycle on the rank positions. A factorization of a \(k\)-cycle into adjacent transpositions uses every simple generator and has at least \(k-1\) factors. Its parity is \(k-1\), giving the congruence. \(\square\)

Thus the odd cycle contains linearly many explicitly located reversals. Their existence is not the remaining difficulty.

### 6.3 Incidence identities

Let \(C\) be the ordinary cycle on ground vertices \(d_0,\ldots ,d_{2k}\), with edge \(\{d_{i-1},d_i\}\). The support identities are
\[
\mathbf 1_{S_i}+\mathbf 1_{S_{i+1}}=\mathbf 1_V-\mathbf 1_{\{d_i\}},
\qquad
\sum_i\mathbf 1_{S_i}=k\mathbf 1_V.
\]

Let \(T\) be the support of a tight path that is a vertex cover of \(C\), and write \(|T|=k+r\). Define
\[
I(T)=\{i:d_{i-1},d_i\in T\}.
\]

**Lemma 11.** One has
\[
|I(T)|=2r-1,\qquad
\mathbf 1_T+\sum_{i\in I(T)}\mathbf 1_{S_i}=r\mathbf 1_V.
\]

**Proof.** Put \(t_i=\mathbf 1_T(d_i)\) and \(a_i=t_{i-1}+t_i\). Since \(T\) covers every edge of \(C\), \(a_i\in\{1,2\}\), and \(a_i-1\) is the indicator of \(I(T)\). Then
\[
\sum_i a_i\mathbf 1_{S_i}
 =\sum_j t_j(\mathbf 1_{S_j}+\mathbf 1_{S_{j+1}})
 =|T|\mathbf 1_V-\mathbf 1_T.
\]
Subtracting \(\sum_i\mathbf 1_{S_i}=k\mathbf 1_V\) gives the second identity. Summing the \(a_i\) gives
\[
2|T|=(2k+1)+|I(T)|,
\]
which gives the first. \(\square\)

If \(r=1\), Lemma 11 says that \(T\) and one selected support \(S_i\) are disjoint and cover \(V(H)\). Therefore a Hamiltonian vertex cover of the ground cycle of order \(k+1\) gives a two-cover of \(H\).

### Odd cycle forces bounded support


### The spanning odd cycle immediately yields bounded support

**Lemma 12 (odd-cycle bounded-support reduction).** Assume the selected support graph is the spanning odd cycle
\[
S_0S_1\cdots S_{2k}S_0,
\]
with edge \(S_iS_{i+1}\) labeled \(d_i\). Then either \(H\) has a two-cover, or \(H\) contains a Hamiltonian four-support \(K\) with
\[
\operatorname{pc}(H-K)=2.
\]

**Proof.** Fix \(i\). The selected deletion cover at \(d_i\) is
\[
H-d_i=S_i\mid S_{i+1}.
\]
Choose displayed Hamilton orders
\[
P_i=(s_1,\ldots,s_k),
\qquad
P_{i+1}=(t_1,\ldots,t_k)
\]
on these two supports.

Neither \(S_i\cup\{d_i\}\) nor \(S_{i+1}\cup\{d_i\}\) is Hamiltonian. Indeed, a Hamilton path on the first set together with \(P_{i+1}\), or a Hamilton path on the second together with \(P_i\), would give a spanning two-cover of \(H\).

Hence \(d_i\) cannot be prepended to either displayed path. Therefore
\[
(d_i,s_1,s_2),
\qquad
(d_i,t_1,t_2)
\]
are non-tight. Boundary antisymmetry gives
\[
(s_2,s_1,d_i),
\qquad
(t_2,t_1,d_i)
\]
tight.

Thus the single exterior vertex \(d_i\) reverses the initial edges of the two vertex-disjoint tight paths \(P_i\) and \(P_{i+1}\). Exactly one of
\[
(s_1,d_i,t_1),
\qquad
(t_1,d_i,s_1)
\]
is tight. In the first case
\[
(s_2,s_1,d_i,t_1)
\]
is a Hamiltonian four-path; in the second
\[
(t_2,t_1,d_i,s_1)
\]
is a Hamiltonian four-path. Hence a Hamiltonian four-support \(K\) exists.

Since \(K\) is proper in a minimum counterexample, minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K)\le2.
\]
Its complement cannot be Hamiltonian, or a Hamilton path on \(H-K\) together with a Hamilton path on \(K\) would two-cover \(H\). Thus
\[
\operatorname{pc}(H-K)=2.
\]
\(\square\)

The crucial point is that the common-reverser argument uses **one deleted label and two disjoint displayed end edges**. Two different deleted labels reversing one common edge do not suffice.

Therefore the spanning odd cycle is not an independent terminal support-graph geometry. At arbitrary order it immediately returns to the bounded-support/maximal-support route. Combined with the forest analysis, the selected support graph has no quiet global residue outside the bounded-support and reversal/disturbance interfaces.


---

## Section — The remaining lemma

<!-- section_id: deletion_covers_and_the_support_graph_the_remaining_lemma -->

The preceding argument reduces the deletion-cover method to the following statement.

**Remaining Lemma.** Let \(H\) be a minimum counterexample and let \(H-x=P\mid Q\) be a deletion cover. Suppose that the selected deletion covers yield, relative to \(P\mid Q\) or to a consecutive double deletion,
- an order disagreement attached to the displayed supports;
- an edge in an endpoint deletion cover joining surviving vertices of \(P\) and \(Q\);
- an inherited displayed path edge whose endpoints lie in different paths of an endpoint deletion cover; or
- an edge joining distinct inherited path pieces in the odd-cycle configuration.

Then \(H\) has a spanning ordering of defect span at most \(2\).

By Lemma 1, this would contradict the choice of \(H\). In the odd-cycle case it would also suffice to prove that the rank transport of Lemma 10 forces a Hamiltonian vertex cover of the ground cycle of order \(k+1\), since Lemma 11 would then give a two-cover directly.

No further production of isolated reversals is required: Lemma 10 already supplies many. The unresolved point is to use their positions to remove one of the two independent defects in the spanning order arising from a deletion cover.

---

## Section — Appendix. Why two selected supports need not suffice in the forest case

<!-- section_id: deletion_covers_and_the_support_graph_appendix_why_two_selected_supports_need_not_suffice_in_the_forest_case -->

The forest alternative cannot in general be completed by choosing two supports already present in the selected family.

Let \(J\) be a connected selected-support tree, with support \(S_u\) at each vertex \(u\). For vertices \(u,v\), let \(P_{uv}\) be their tree path.

**Proposition A.1.** The union \(S_u\cup S_v\) equals \(V(H)\) if and only if \(P_{uv}\) has even length and every edge outside \(P_{uv}\) is pendant and attached to a vertex of \(P_{uv}\) at odd distance from \(u\).

**Proof.** For an edge label \(e\), membership in \(S_w\) is determined by the parity of the distance from \(w\) to the nearer endpoint of \(e\): the label belongs to \(S_w\) exactly at odd distance. If \(P_{uv}\) has odd length, its first edge label is omitted by both supports. Assume the path has even length. Every label on the path then belongs to exactly one of \(S_u,S_v\). For an edge off the path, the first edge of its branch belongs to both supports exactly when its attachment point is at odd distance from \(u\); a second edge on the same branch would then be omitted by both. This proves the criterion. \(\square\)

Consequently, if branching remains after suppressing degree-two vertices on one side of the tree bipartition and deleting leaves on that side, no two selected supports cover all vertices. Any two-cover must then use a Hamiltonian support not already present among the selected deletion-cover components. This obstruction concerns only selection from the existing support family; it does not obstruct the theorem itself.

---

## Section — Canonical references

<!-- section_id: deletion_covers_and_the_support_graph_canonical_references -->

- [[mincex01]] — Minimum-counterexample calculus
