# Several deleted labels in one component

## Composition

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

## Support-graph shadow of neutral recurrence

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

## Forest recurrence collapses to endpoint backtracking

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


## Metadata

- ID: three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component
- Kind: section
- Version: 13
- Math version: 10
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False
- Subsections existing when composed: 3
- Subsections now: 3

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component_subsection_a.md) (`three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component_subsection_a`; development v2; composition v1; stale=False)
- [Subsection 2 — Support-graph shadow of neutral recurrence](../SUBSECTIONS/three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component_subsection_b.md) (`three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component_subsection_b`; development v3; composition v1; stale=False)
- [Subsection 3 — Forest recurrence collapses to endpoint backtracking](../SUBSECTIONS/three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component_subsection_c.md) (`three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component_subsection_c`; development v10; composition vNone; stale=False)
