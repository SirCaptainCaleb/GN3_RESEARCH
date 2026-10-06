# Article VI — three-cover repartitions and recurrence

## Composition status

- Composition version: 1
- Stale: False
- Composed through revision: 1083
- Sections existing when composed: 10
- Sections now: 10

## Composition

---

## Section — Introduction

<!-- section_id: three_cover_repartitions_and_recurrence_introduction -->

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\).

Let \(\mathcal R(H)\) be the graph whose vertices are spanning three-covers of \(H\). Two vertices of \(\mathcal R(H)\) are adjacent when one is obtained from the other by a pairwise repartition. For
\[
C=P_1\mid P_2\mid P_3
\]
define
\[
\Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2.
\]

For every \(x\in V(H)\), minimality gives a deletion cover
\[
H-x=P\mid Q.
\]
Its singleton lift
\[
P\mid Q\mid\{x\}
\]
is a vertex of \(\mathcal R(H)\).

---

## Section — The central three- or five-vertex path

<!-- section_id: three_cover_repartitions_and_recurrence_the_central_three_or_five_vertex_path -->

Write
\[
P=(p_0,\ldots ,p_m),\qquad
Q=(q_0,\ldots ,q_s).
\]
Neither
\[
(p_{m-1},p_m,x)
\quad\text{nor}\quad
(x,q_0,q_1)
\]
is tight, since either would absorb \(x\) into one path of the deletion cover. Hence
\[
(x,p_m,p_{m-1}),
\qquad
(q_1,q_0,x)
\]
are tight.

**Lemma 1.** The singleton lift and a three-cover having a central path of order three or five lie in the same component of \(\mathcal R(H)\). More precisely:
- if \((p_m,x,q_0)\) is tight, two pairwise repartitions give
\[
(p_0,\ldots ,p_{m-1})
\mid(p_m,x,q_0)
\mid(q_1,\ldots ,q_s);
\]
- if \((p_m,x,q_0)\) is non-tight, two pairwise repartitions give
\[
(p_0,\ldots ,p_{m-2})
\mid(q_1,q_0,x,p_m,p_{m-1})
\mid(q_2,\ldots ,q_s).
\]

**Proof.** In the first case, repartition
\[
Q\mid\{x\}
\]
as
\[
(x,q_0)\mid(q_1,\ldots ,q_s),
\]
then repartition \(P\mid(x,q_0)\) as the two paths displayed above.

In the second case, boundary reversal gives \((q_0,x,p_m)\) tight. First repartition
\[
Q\mid\{x\}
\]
as
\[
(q_1,q_0,x)\mid(q_2,\ldots ,q_s).
\]
Then
\[
(q_1,q_0,x,p_m,p_{m-1})
\]
is tight because its three consecutive triples are
\[
(q_1,q_0,x),\quad(q_0,x,p_m),\quad(x,p_m,p_{m-1}).
\]
Repartitioning \(P\) with the three-vertex path gives the stated five-vertex central path. \(\square\)

Thus every deleted label has a canonical bounded representative in the same component of \(\mathcal R(H)\).

---

## Section — Minimum potential inside a component

<!-- section_id: three_cover_repartitions_and_recurrence_minimum_potential_inside_a_component -->

Fix a component \(\mathcal C\) of \(\mathcal R(H)\) containing a singleton lift, and choose \(C=P_1\mid P_2\mid P_3\in\mathcal C\) minimizing \(\Phi\).

**Lemma 2.** For \(i\ne j\), every two-cover \(R\mid S\) of
\[
H[V(P_i)\cup V(P_j)]
\]
satisfies
\[
\bigl||R|-|S|\bigr|
\ge
\bigl||P_i|-|P_j|\bigr|.
\]

**Proof.** The replacement \(P_i\mid P_j\mapsto R\mid S\) is an edge of \(\mathcal R(H)\). With fixed sum \(a+b\),
\[
a^2+b^2=\frac{(a+b)^2+(a-b)^2}{2},
\]
so a smaller size difference would decrease \(\Phi\), contrary to the choice of \(C\). \(\square\)

Thus every displayed pair is a minimum-imbalance two-cover of its union.

Among triples of positive integers with fixed sum, the minimum of the sum of squares occurs exactly when the largest and smallest entries differ by at most one. Therefore the absolute minimum size multisets are
\[
\{r,r,r\},\qquad
\{r+1,r,r\},\qquad
\{r+1,r+1,r\}.
\]
Strict decrease of \(\Phi\) must eventually stop, and it can stop at one of these profiles.

---

## Section — Moving away from a three-vertex side

<!-- section_id: three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side -->

Suppose a state in \(\mathcal C\) has the form
\[
X\mid P\mid Q,
\qquad |X|=3,
\qquad
P=(p_1,\ldots ,p_m).
\]

If \(X\cup\{p_1\}\) is Hamiltonian, repartition \(X\mid P\) as
\[
(X\cup\{p_1\})\mid(p_2,\ldots ,p_m).
\]
The two affected orders change from \((3,m)\) to \((4,m-1)\), and
\[
16+(m-1)^2-(9+m^2)=8-2m.
\]
Hence the move strictly decreases \(\Phi\) for \(m\ge5\). The same holds at the other endpoint.

Assume neither endpoint extends \(X\). Boundary reversal then supplies reversed triples at both ends of \(P\). Comparing the six- and seven-vertex sets formed from \(X\), the two endpoints of \(P\), and one further path vertex gives one of two possibilities: a Hamiltonian four-set whose complement has a two-cover, or a Hamiltonian five-set containing both displayed endpoints of a long inherited interval. In either case the new three-cover lies in \(\mathcal C\), because it is obtained by repartitioning \(X\mid P\).

Consequently:

**Lemma 3.** From a three-vertex side adjacent to a path of order at least five, one obtains inside the same component of \(\mathcal R(H)\) either
1. a strict decrease of \(\Phi\);
2. a Hamiltonian four-vertex component with two-coverable complement; or
3. a Hamiltonian five-vertex component tied to displayed endpoints of a complementary path.

Repeated application either decreases \(\Phi\) or reaches a bounded Hamiltonian component carrying endpoint information.

---

## Section — Four- and five-vertex components

<!-- section_id: three_cover_repartitions_and_recurrence_four_and_five_vertex_components -->

Let
\[
W\mid P\mid Q
\]
be a state in \(\mathcal C\), where \(W\) is Hamiltonian and \(|W|=4\). If \(P=(p_1,\ldots ,p_m)\) with \(m\ge6\), then Hamiltonicity of \(W\cup\{p_1\}\) or \(W\cup\{p_m\}\) gives a repartition with orders \((5,m-1)\), changing the two square terms by
\[
10-2m<0.
\]

If both endpoint five-sets are non-Hamiltonian, comparison of their Hamiltonian four-vertex deletions gives two Hamiltonian four-sets
\[
\{p_1,p_m,a,b\},
\qquad
\{p_1,p_m,a,c\}
\]
sharing the three-set \(\{p_1,p_m,a\}\). Their complements have path-cover number two.

For a Hamiltonian five-vertex component \(Y\) beside a long path \(P\), the analogous endpoint test gives either a strict decrease of \(\Phi\), an equal-\(\Phi\) exchange of one vertex of \(Y\) with one endpoint of \(P\), or a tight triple through a vertex of \(Y\) reversing an edge of \(P\).

Thus a componentwise minimum of \(\Phi\) does not terminate at an arbitrary small support. It contains explicit overlap, endpoint exchange, or reversal data.

### Bounded four-support closure

The rooted small-support descent now completely classifies the bounded case in which a minimum-\(\Phi\) state contains a component of order four. Unless an order-three component or a \(4|6\) endpoint order disagreement is already present, every component order lies in \(\{4,5,6\}\). The six possible profiles containing a four then behave as follows.

- \(4|4|4\): every displayed \(4|4\) pair lies on an eight-set with at least seven complementary Hamiltonian \(4+4\) decompositions. Applying this to all three component pairs gives at least eighteen distinct nontrivial neutral neighbors at every state.
- \(4|4|5\) and \(4|5|5\): every \(4|5\) pair has a nontrivial neutral repartition, so these profiles have forced neutral cycles.
- \(4|4|6\), \(4|5|6\), and \(4|6|6\): every relevant \(4|6\) pair either exhibits an endpoint-six-set order disagreement or admits the neutral migration \(4|6\to6|4\). If no disagreement occurs, each state has at least two distinct neutral neighbors.

Thus none of the six bounded four-support size profiles remains as an unstructured terminal case. At a minimum of \(\Phi\), the entire order-four regime has already been converted into explicit neutral recurrence or an order disturbance.

---

## Section — Equal-potential recurrence

<!-- section_id: three_cover_repartitions_and_recurrence_equal_potential_recurrence -->

Equal-\(\Phi\) moves occur at the equitable size profiles and in the one-vertex transfer case. They must therefore be treated directly.

Consider first the size multiset
\[
\{r+1,r+1,r\}.
\]
An equal-\(\Phi\) repartition transfers one endpoint from a large path to the small path. If no order disagreement or smaller Hamiltonian support appears, the transfers cycle through two labels \(x,y\) and three core paths \(A,B,C\):
\[
x:A\to B,\quad y:C\to A,\quad
x:B\to C,\quad y:A\to B,\quad
x:C\to A,\quad y:B\to C.
\]
Hence both \(x\) and \(y\) extend the same end of each of \(A,B,C\).

Let \(T\) be a two-cover of
\[
H-\{x,y\}=A\cup B\cup C.
\]
Decompose its paths into maximal blocks lying in \(A,B,C\). If \(t\) is the number of edges of \(T\) joining distinct cores and \(b_A,b_B,b_C\) are the block counts, then
\[
t=b_A+b_B+b_C-2.
\]
If \(t=1\), the three cores occur as whole blocks and the same-end extensions by \(x,y\) give a two-cover of \(H\). Thus \(t\ge2\). If \(t=2\), either an edge of one displayed core has endpoints in different paths of \(T\), or one path of \(T\) leaves and later returns to the same core. If \(t\ge3\), there are already three specified edges joining distinct cores.

Therefore a neutral cycle cannot return with only the size data changed: it leaves a concrete order or support discrepancy.

The profiles \(\{r,r,r\}\) and \(\{r+1,r,r\}\) admit the same endpoint comparison. A neutral transfer with opposite endpoint realizations gives a displayed end-edge reversal by greedy endpoint transport. If all endpoint realizations use the same side, Hall's theorem on the two transferred labels and the two paths of a double deletion gives either a two-cover, two reverse triples through one end edge, or two deletion covers differing by one transferred label.

We obtain:

**Lemma 4.** At a minimum of \(\Phi\) in \(\mathcal C\), equal-potential motion produces at least one of:
1. an order disagreement;
2. an edge of a comparison cover joining distinct displayed supports;
3. an inherited path edge whose endpoints lie in different paths of a comparison cover;
4. two separated blocks from one displayed support on one comparison path;
5. a tight triple reversing a displayed edge;
6. two Hamiltonian five-sets with a common four-set;
7. a one-vertex transfer whose endpoint realizations all use the same side.

These are the local recurrence residues.

---

## Section — Several deleted labels in one component

<!-- section_id: three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component -->

There is a second argument that does not follow one trajectory.

Two deletion covers are compatible when, after deleting both omitted labels, they induce the same support partition and the same relative order on every common support.

**Lemma 5.** If deletion covers \(F_x\) of \(H-x\) and \(F_y\) of \(H-y\) are compatible, their singleton lifts lie on one edge of \(\mathcal R(H)\).

**Proof.** On \(H-\{x,y\}\), compatibility gives two common ordered supports, say \(A,B\). In \(F_x\), the restored vertex \(y\) is inserted into one of them; in \(F_y\), the restored vertex \(x\) must be inserted into the same support, since insertion into the other support would produce two disjoint Hamiltonian supports covering \(H\). Suppose the common support is \(A\). Then the two singleton lifts have the form
\[
(A+y)\mid B\mid\{x\},
\qquad
(A+x)\mid B\mid\{y\}.
\]
Replacing
\[
(A+y)\mid\{x\}
\]
by
\[
(A+x)\mid\{y\}
\]
is a pairwise repartition. \(\square\)

Hence every connected component of the compatibility graph of chosen deletion covers maps into one connected component of \(\mathcal R(H)\).

By Lemma 1, this component then contains, for every deleted label in the compatibility component, its singleton lift and its central three- or five-vertex representative. Thus a large compatibility component produces many differently rooted bounded states in one component of \(\mathcal R(H)\).

If the compatibility graph has no large connected component, choosing labels from different components produces a large family of pairwise incompatible deletion covers. This is the complementary structural case and belongs to the deletion-cover argument rather than the recurrence argument.

### Support-graph shadow of neutral recurrence

### Compatibility cycles project to the support graph

Fix one selected deletion cover (F_d) for each label (d), and let (J) be the selected support graph. Let (K) be the graph on labels in which (ab) is an edge when (F_a,F_b) are compatible.

**Lemma 6 (line-graph shadow).** If (abin E(K)), then the selected support edges (e_a,e_bin E(J)) share a support vertex. Consequently
[
Ksubseteq L(J),
]
after identifying each label (d) with its selected support edge (e_d).

**Proof.** Compatibility of (F_a,F_b) gives two common ordered supports (P,Q) on
[
H-{a,b}.
]
By the insertion-slot lemma, the restored vertices (a,b) are inserted into the same common support, say (P). Hence
[
F_a=(P+b)mid Q,
qquad
F_b=(P+a)mid Q.
]
Thus the selected support edges
[
e_a=(P+b)Q,
qquad
e_b=(P+a)Q
]
are both incident with the exact support (Q). (square)

This makes closed neutral recurrence globally rigid.

**Corollary 7 (recurrence-cycle routing).** Let
[
d_0d_1cdots d_{m-1}d_0
]
be a simple cycle in the compatibility graph (K).

1. If (J) is a forest, then all selected edges
   [
   e_{d_0},ldots,e_{d_{m-1}}
   ]
   are incident with one common support (Q). Hence the deletion covers on the cycle are pairwise support-compatible.

   If (mge4), then either (H) has a two-cover or two of these covers have an order disagreement on their common domain. In the latter case the path-order disagreement machinery yields a tight triple reversing an edge of a displayed path.

   Thus a forest recurrence cycle not already returning to a reversal or two-cover has length exactly three.

2. If (J) is the spanning odd cycle from the support-graph dichotomy, then any simple cycle in (Ksubseteq L(J)) is the whole line graph (L(J)), which is again that same odd cycle. Hence a closed neutral recurrence in this case is not a new residue: it is exactly the global odd-cycle support geometry of Article I.

**Proof.** Suppose first that (J) is a forest. The line graph of a forest is a block graph: every simple cycle lies inside the clique formed by the edges incident with one vertex of the forest. Lemma 6 therefore gives one support (Q) incident with every selected edge on the recurrence cycle.

Write
[
X=V(H)-Q.
]
Since (e_{d_i}) is incident with (Q) and omits exactly (d_i), its other endpoint is necessarily
[
X-{d_i}.
]
Thus
[
F_{d_i}=(X-{d_i})mid Q
]
for every (i), so the family is pairwise support-compatible.

If (mge4) and the covers are pairwise compatible, compatibility gluing gives a two-cover of (H). Otherwise some pair is support-compatible but not compatible, so their common-support orders disagree. The reversal-from-order-disagreement theorem then gives a displayed-edge reversal.

Now suppose (J) is the spanning odd cycle. Its line graph is another cycle of the same odd length, and a proper subgraph of a cycle contains no simple cycle. Therefore any simple cycle of (Ksubseteq L(J)) must use every edge of (L(J)). (square)

Hence indefinite neutral omission-swap recurrence has only two genuine global destinations:

- a three-cover compatibility triangle around one support vertex in the forest case;
- the spanning odd-cycle support geometry.

Every longer forest recurrence already yields a two-cover or a fresh reversal. Neutral omission swaps therefore do not create an unrestricted new state space.

### Forest recurrence collapses to endpoint backtracking

### In the no-reversal forest residue, neutral recurrence cannot cycle

Retain the selected deletion covers, support graph (J), and compatibility graph (K) from Lemma 6.

**Corollary 8 (forest recurrence collapses to endpoint backtracking).** Suppose the global reversal/order-disagreement alternatives from Article I have been excluded, so that in the forest branch the selected support graph (J) is a disjoint union of support paths. Then:

1. (Ksubseteq L(J)) is also a disjoint union of paths. In particular (K) has no cycle.
2. Hence a neutral omission-swap trajectory which changes omitted labels and never immediately reverses its previous swap cannot recur indefinitely. Since the label set is finite, such a trajectory must terminate at a non-neutral outcome.
3. The only purely neutral forest recurrence is immediate backtracking along one compatibility edge (ab).
4. For such a compatible pair (F_a,F_b), outside the reversal and bounded-support alternatives, the two omitted labels are inserted into the same endpoint gap of their common ordered support.

**Proof.** Under the no-reversal/order-disagreement hypothesis, Article I reduces every forest component of (J) to a path. The line graph of a disjoint union of paths is again a disjoint union of paths. Lemma 6 gives
[
Ksubseteq L(J),
]
so (K) is acyclic and has maximum degree at most two. This proves (1).

A neutral omission swap from label (a) to label (b) moves along the compatibility edge (ab). A trajectory with no immediate backtracking therefore traces a simple path in (K). It cannot be infinite because (K) is finite, proving (2). Thus an indefinitely repeatable neutral move in the forest branch must alternate across one edge, proving (3).

Finally let (F_a,F_b) be that compatible pair. By the insertion-slot lemma their insertion gaps in the common support are equal or adjacent. Adjacent gaps force a reversing tight triple, excluded here. Hence the gaps are equal.

If the common gap is internal, say the common order contains the edge (uv), then both
[
(u,a,v)
qquad	ext{and}qquad
(u,b,v)
]
are tight. The compatible-extension lemma makes
[
{u,v,a,b}
]
a Hamiltonian four-set. In a minimum counterexample its complement has path-cover number two, which is the bounded-support alternative. Excluding that as well, the equal common gap must be one of the two endpoint gaps. (square)

Thus the forest neutral omission-swap residue has been reduced from arbitrary recurrence to a single rigid local form:

> two selected deletion covers exchange their omitted labels at the same endpoint of one common support, and the only neutral motion is the reverse swap back.

Any continuation that avoids immediate backtracking must leave the neutral regime and produce a reversal/order disagreement, split disturbance, strict descent, two-cover, or support-component escape.

### Quiet support paths have alternating endpoint exchanges

Let a support-path component of the selected support graph have support vertices
[
S_0,S_1,ldots,S_k
]
and edge labels (d_i) on (S_{i-1}S_i), (1le ile k).
Assume throughout this component that order disagreement, external reversal, and bounded Hamiltonian support have all been excluded.

For (1le ile k-1), the adjacent selected covers (F_{d_i}) and (F_{d_{i+1}}) share the exact support (S_i). They are therefore compatible, and the insertion-slot lemma says that the exchanged labels (d_i,d_{i+1}) occupy equal or adjacent slots in the common order on the other support. Adjacent slots give a reversal; an equal internal slot gives a Hamiltonian four-support by [[endpoint_transport_and_small_support_gluing_compatible_one_vertex_extensions]]. Hence only an equal endpoint slot remains. Write
[
\varepsilon_iin{L,R}
]
for that endpoint.

**Lemma 9 (endpoint alternation).** For every (1le ile k-3),
[
\varepsilon_{i+2}
e\varepsilon_i.
]
Consequently, for every (2le jle k-2), the two displayed endpoints of the common Hamilton order on (S_j) are exactly
[
d_{j-1}qquad	ext{and}qquad d_{j+2}.
]

**Proof.** The comparison of (F_{d_i}) and (F_{d_{i+1}}) expresses the support (S_{i+1}) as a common ordered core with the label (d_i) inserted at endpoint (\varepsilon_i). Likewise the comparison of (F_{d_{i+2}}) and (F_{d_{i+3}}) expresses the same support (S_{i+1}) as a common ordered core with (d_{i+3}) inserted at endpoint (\varepsilon_{i+2}).

The two selected covers incident with (S_{i+1}), namely (F_{d_{i+1}}) and (F_{d_{i+2}}), have no order disagreement. Hence they use the same Hamilton order on (S_{i+1}). The distinct vertices (d_i,d_{i+3}) are both endpoints of this one order. They cannot occupy the same endpoint, so
[
\varepsilon_{i+2}
e\varepsilon_i.
]

Now fix (2le jle k-2). The comparison indexed by (j-1) puts (d_{j-1}) at one endpoint of (S_j), while the comparison indexed by (j+1) puts (d_{j+2}) at the other endpoint by the first assertion. (square)

Thus the no-progress forest residue is not merely a collection of path components: every sufficiently internal support has its Hamilton-order endpoints determined by edge labels two steps away in the support path. The endpoint choices alternate deterministically along each parity subsequence.

This converts the remaining forest problem into a wiring problem between the ends of distinct support-path components.



### A quiet support-path component has at most two edges

**Corollary 10.** Under the no-progress hypotheses of Lemma 9, no support-path component of the selected support forest has three or more edges.

**Proof.** Suppose a component begins
[
S_0-S_1-S_2-S_3
]
with edge labels
[
d_1,d_2,d_3
]
in order. The cover
[
F_{d_1}=S_0mid S_1
]
is a leaf deletion cover.

The comparison of the adjacent selected covers (F_{d_2}) and (F_{d_3}) has (S_2) as its common support and (S_1,S_3) as its two varying supports. Since reversal, order disagreement, and bounded support are excluded, their exchanged labels use an equal endpoint slot. Hence (d_3) is a displayed endpoint of the Hamilton order on (S_1).

The two adjacent partition identities
[
mathbf 1_{S_1}+mathbf 1_{S_2}
=
mathbf 1_V-mathbf 1_{{d_2}},
]
[
mathbf 1_{S_2}+mathbf 1_{S_3}
=
mathbf 1_V-mathbf 1_{{d_3}}
]
give
[
S_3=(S_1-{d_3})cup{d_2}.
]
Likewise (S_2) has the same cardinality as (S_0), so it is not a strict subset of (S_0). The set (S_3) contains the nonempty set (S_1-{d_3}), which is disjoint from (S_0), and hence (S_3) is not a subset of (S_0).

Therefore the selected cover
[
F_{d_3}=S_2mid S_3
]
cannot be non-mixing relative to the leaf cover (S_0mid S_1): Lemma 1 of [[leaf_comparisons_in_deletion_support_forests]] says that any non-mixing endpoint cover must have one path support strictly contained in the leaf support (S_0).

Thus (F_{d_3}) contains a direct mixed edge between (S_0) and (S_1-{d_3}). Apply
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]]
to the displayed endpoint (d_3) of (S_1).

All non-neutral outcomes are already successful disturbances. Suppose the neutral omission-swap outcome occurs. In the proof of the cited theorem, the surviving block
[
B=S_1-{d_3}
]
lies in one component of (F_{d_3}). Setwise that component must be (S_3), and
[
S_3=Bcup{d_2}
]
contains exactly one vertex outside (B).

If (d_2) follows (B) in the displayed order of (S_3), the restoration construction has empty prefix and produces a two-cover. If (d_2) precedes (B), the terminal case of that construction has no further exterior prefix: either its junction triple fails, giving an endpoint reversal, or it is tight and again produces a two-cover. Hence the neutral omission-swap alternative is impossible.

Thus a three-edge support-path component already forces a successful non-neutral outcome, contradiction. (square)

Consequently, after excluding two-covers, bounded support, reversal/order disagreement, split disturbance, and strict descent, every component of the selected support forest has one or two edges.

The remaining forest residue is therefore finite-width at the **support-graph level**, independent of (|V(H)|): all global complexity is now in how these one-edge and two-edge components are wired to one another by their ground labels.



### Component-minimal selection restricts cross-component neutral swaps

Assume minimum-imbalance deletion covers have been chosen, and among all such choices choose the family so that its selected support forest (J) has the minimum possible number of connected components. Work in the no-progress forest residue, so every component of (J) has one or two edges by Corollary 10.

**Lemma 11 (neutral transfer between support components).** Suppose an endpoint comparison reaches the neutral omission-swap outcome and, after the balancing step of
[[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]],
produces an equally balanced deletion cover (G_w) of (H-w) compatible with the selected cover (F_y).

Let (C_w,C_y) be the components of (J) containing the selected support edges (e_w,e_y). Then, unless a successful disturbance already occurs, exactly one of the following holds.

1. (C_w=C_y), and this common component has two edges. Thus the neutral move is internal to one two-edge support-path component.
2. (C_w
e C_y), (C_w) has two edges, and (C_y) has one edge. Replacing (F_w) by (G_w) changes the component types
   [
   2+1longrightarrow1+2:
   ]
   the source component loses one selected edge and the target component gains the compatible replacement edge.

In particular, a genuinely cross-component neutral move can only transfer the two-edge status from one support component to a one-edge component.

**Proof.** Compatibility of (G_w) with (F_y) implies that the support edge (g_w) of (G_w) shares a support vertex with (e_y). Since the balancing theorem is in its equality case, (G_w) is itself a minimum-imbalance deletion cover and may replace the selected cover (F_w).

Suppose first that (C_w
e C_y). If (C_w) had one edge, deleting (e_w) would remove that entire support component, while inserting (g_w) attaches the replacement edge to (C_y). The number of connected components of the selected support graph would decrease, contradicting the component-minimal choice. Hence (C_w) has two edges.

Now suppose (C_y) also had two edges. Remove (e_w) and insert (g_w). The source component remains nonempty, with one selected edge. At the target, the new edge (g_w) is incident with (e_y). If its other support already lies in another existing component, the reselection merges components and again lowers the component count. Otherwise the target component acquires a third edge.

But a three-edge target component cannot survive in the no-progress residue: if it branches, the degree-three support obstruction in [[deletion_covers_and_the_support_graph_compatibility_of_deletion_covers]] gives an order disagreement or reversal; if it is a path, Corollary 10 gives a successful disturbance. Thus (C_y) cannot have two edges. It has one edge, proving outcome 2.

Finally suppose (C_w=C_y). The component cannot have one edge because distinct labels (w,y) have distinct selected support edges. Hence it has exactly two edges, proving outcome 1. (square)

Thus the remaining forest recurrence has a component-level token description. Two-edge components are the only possible sources of cross-component neutral motion, and one-edge components are the only possible targets. A cross-component neutral step merely moves the unique extra selected edge from one support component to another; it cannot create or destroy that token without producing progress.



### Correction: equal endpoint-slot backtracking remains unresolved

The previous claimed closure of the same-endpoint backtracking pair used the assertion that exactly one of \((a,b,p_1)\) and \((b,a,p_1)\) is tight. These are not boundary flips. The boundary flip of \((a,b,p_1)\) is \((p_1,b,a)\), and no cyclic or other reordering has prescribed status. Therefore that lemma and the resulting claim that all forest neutral recurrence is closed are withdrawn.

The preceding reductions remain valid: in the no-progress forest branch, a neutral trajectory either terminates, transfers the two-edge component token as in Lemma 11, or backtracks across one compatibility edge. Outside reversal and bounded-support outcomes, such a backtracking pair inserts its two omitted labels into the same endpoint gap of one common ordered support. This same-endpoint pair is the genuine unresolved forest-neutral residue.

Any closure of it must use additional attachment information from the second common support, leaf mixing, or a proved extension theorem; boundary antisymmetry alone does not concatenate the two same-side extenders.


### Correct closure of same-endpoint backtracking via the second support

**Lemma 12 (same-endpoint backtracking forces bounded support).** Let \(F_a,F_b\) be compatible deletion covers. Suppose the omitted labels \(a,b\) are inserted into the same endpoint gap of a common ordered support
\[
P=(p_1,\ldots,p_m),
\]
while the other common support is
\[
Q=(q_1,\ldots,q_t).
\]
Then either \(H\) has a two-cover, or \(H\) contains a Hamiltonian support \(K\) of order four or five with
\[
\operatorname{pc}(H-K)=2.
\]

**Proof.** Reverse \(P\) if necessary so
\[
F_a=(b,p_1,\ldots,p_m)\mid Q,
\qquad
F_b=(a,p_1,\ldots,p_m)\mid Q.
\]

If \(t=1\), the path on \(\{a,q_1\}\), together with \((b,p_1,\ldots,p_m)\), two-covers \(H\). Hence assume \(t\ge2\).

Neither \(a\) nor \(b\) can attach to either displayed end of \(Q\). For example, a Hamilton path obtained by attaching \(a\) to \(Q\), together with \((b,p_1,\ldots,p_m)\), would two-cover \(H\); the other three endpoint attachments are symmetric.

Therefore, for each \(z\in\{a,b\}\),
\[
(z,q_1,q_2)
\]
is non-tight and
\[
(q_{t-1},q_t,z)
\]
is non-tight. Boundary antisymmetry gives
\[
(q_2,q_1,z),
\qquad
(z,q_t,q_{t-1})
\]
tight.

If \(t=2\), using different labels at the two ends gives
\[
(b,q_2,q_1,a)
\]
as a Hamiltonian four-path. Thus assume \(t\ge3\).

Fix \(z\in\{a,b\}\). Exactly one of
\[
(q_1,z,q_t),
\qquad
(q_t,z,q_1)
\]
is tight.

If
\[
(q_1,z,q_t)
\]
is tight for either \(z\), then
\[
(q_2,q_1,z,q_t,q_{t-1})
\]
is a Hamiltonian five-path.

Otherwise both labels satisfy
\[
(q_t,a,q_1),
\qquad
(q_t,b,q_1)
\]
tight. Hence \(a\) and \(b\) are two parallel middle vertices between the fixed endpoints \(q_t,q_1\). The parallel-middle lemma in localextend01 gives a Hamiltonian four-support on
\[
\{q_t,q_1,a,b\}.
\]

Thus in every case either \(H\) already has a two-cover or there is a Hamiltonian support \(K\) of order four or five. Such \(K\) is proper in a minimum counterexample. Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K)\le2,
\]
and the complement cannot be Hamiltonian, since a Hamilton path on \(H-K\) together with one on \(K\) would two-cover \(H\). Therefore
\[
\operatorname{pc}(H-K)=2.
\]
\(\square\)

The closure uses the two endpoint failures on the fixed second support \(Q\). It does not use the false inference that two different exterior vertices reversing one common edge force a Hamiltonian four-set.


---

## Section — Two distinct remaining lemmas

<!-- section_id: three_cover_repartitions_and_recurrence_two_distinct_remaining_lemmas -->

The one-trajectory and many-root arguments require different conclusions.

**Remaining Lemma A.** Let \(\mathcal C\) contain a singleton lift and let \(C\in\mathcal C\) minimize \(\Phi\). If \(C\) has one of the recurrence residues in Lemma 4, then either \(H\) has a two-cover, or \(\mathcal C\) contains a three-cover of smaller \(\Phi\), or there is an equal-\(\Phi\) move that strictly decreases a well-founded secondary integer.

A proof rules out recurrence in one component.

**Remaining Lemma B.** There is a constant \(k\) such that if one component of \(\mathcal R(H)\) contains central bounded representatives associated with \(k\) distinct deleted labels, then either \(H\) has a two-cover, that component contains a three-cover of smaller \(\Phi\), or two of the rooted representatives combine to give a spanning ordering of defect span at most \(2\).

A proof rules out congestion of many deletion roots without requiring a secondary invariant on every equal-\(\Phi\) move.

These statements are genuinely different. Lemma A orients one trajectory. Lemma B uses several rooted neighborhoods simultaneously.

---

## Section — Appendix. Why finiteness is insufficient

<!-- section_id: three_cover_repartitions_and_recurrence_appendix_why_finiteness_is_insufficient -->

A finite sequence of equal-\(\Phi\) pairwise repartitions may return to its initial three-cover. Finiteness alone therefore does not make neutral motion terminate. A valid recurrence argument needs either a secondary quantity that decreases on every selected neutral move or a contradiction obtained from the oriented data accumulated around a cycle.

Boundary reversal also remains local:
\[
(a,b,c)\text{ non-tight}
\quad\Longleftrightarrow\quad
(c,b,a)\text{ tight}.
\]
It does not justify reversing a path or cyclically rotating a triple. Every recurrence argument above therefore keeps the displayed path orders through each pairwise repartition.

---

## Section — Canonical references

<!-- section_id: three_cover_repartitions_and_recurrence_canonical_references -->

- [[fivefence01]] — Five-set fence: bare complement witnesses are not closure

## Contained Sections

- 1. [Introduction](../SECTIONS/three_cover_repartitions_and_recurrence_introduction.md) (`three_cover_repartitions_and_recurrence_introduction`; composition v1; stale=False)
- 2. [The central three- or five-vertex path](../SECTIONS/three_cover_repartitions_and_recurrence_the_central_three_or_five_vertex_path.md) (`three_cover_repartitions_and_recurrence_the_central_three_or_five_vertex_path`; composition v1; stale=False)
- 3. [Minimum potential inside a component](../SECTIONS/three_cover_repartitions_and_recurrence_minimum_potential_inside_a_component.md) (`three_cover_repartitions_and_recurrence_minimum_potential_inside_a_component`; composition v1; stale=False)
- 4. [Moving away from a three-vertex side](../SECTIONS/three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side.md) (`three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side`; composition v1; stale=False)
- 5. [Four- and five-vertex components](../SECTIONS/three_cover_repartitions_and_recurrence_four_and_five_vertex_components.md) (`three_cover_repartitions_and_recurrence_four_and_five_vertex_components`; composition v1; stale=False)
- 6. [Equal-potential recurrence](../SECTIONS/three_cover_repartitions_and_recurrence_equal_potential_recurrence.md) (`three_cover_repartitions_and_recurrence_equal_potential_recurrence`; composition v1; stale=False)
- 7. [Several deleted labels in one component](../SECTIONS/three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component.md) (`three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component`; composition v1; stale=False)
- 8. [Two distinct remaining lemmas](../SECTIONS/three_cover_repartitions_and_recurrence_two_distinct_remaining_lemmas.md) (`three_cover_repartitions_and_recurrence_two_distinct_remaining_lemmas`; composition v1; stale=False)
- 9. [Appendix. Why finiteness is insufficient](../SECTIONS/three_cover_repartitions_and_recurrence_appendix_why_finiteness_is_insufficient.md) (`three_cover_repartitions_and_recurrence_appendix_why_finiteness_is_insufficient`; composition v1; stale=False)
- 10. [Canonical references](../SECTIONS/three_cover_repartitions_and_recurrence_canonical_references.md) (`three_cover_repartitions_and_recurrence_canonical_references`; composition v1; stale=False)
