# Rooted small-support descent from deletion-cover lifts

**Summary:** Deletion-cover singleton lifts can be converted into bounded Hamiltonian supports carrying the deleted label; long neighboring paths force further descent or a small classified endpoint-core obstruction.

## Statement

Starting from a deletion cover H-x=P|Q in a minimum counterexample, track pairwise repartitions that keep x inside a bounded Hamiltonian support. The initial singleton lift strictly descends to a rooted three-path; interaction with long neighboring paths then produces rooted four- or five-supports, nonincreasing transport, or sharply positioned endpoint-core obstructions.

## Body

## Rooted descent through bounded supports


Let (H) be a minimum counterexample and let
[
H-x=Pmid Q
]
be a deletion cover. The singleton lift (Pmid Qmid{x}) lies in the three-cover repartition graph. Write
[
Phi(R_1mid R_2mid R_3)=|R_1|^2+|R_2|^2+|R_3|^2.
]

### 1. Descent from the singleton lift

By [[toolkit_lift_strictly_descends_to_a_rooted_three_vertex_component]], one pairwise repartition strictly decreases (Phi) and places the deleted label (x) in a Hamiltonian three-support (T). Thus every deletion-cover component contains a state in which the distinguished label lies in a bounded nontrivial support.

Let (Tmid C) be two displayed components with (|T|=3) and (C=(c_1,ldots,c_m)). If (mge6), [[three_vertex_component_long_neighbor_rotation01]] gives a strict decrease. At (m=5), direct Hamiltonian enlargement to order four is still strict, while failure of both endpoint enlargements forces the neutral rotation
[
3mid5longrightarrow5mid3.
]

### 2. Quadratic-minimal states with a three-support

Suppose a spanning three-cover is (Phi)-minimal in its repartition component and has a component of order three. By [[toolkit_a_phi_minimum_containing_a_three_path_has_order_at_most_thirteen]], its size multiset is one of
[
{3,3,5},qquad {3,4,4},qquad {3,4,5},qquad {3,5,5}.
]

For a (3mid4) pair, [[toolkit_34_pair_gives_a_neutral_endpoint_swap_or_a_controlled_52_detour]] gives either the neutral swap (3mid4	o4mid3) or a controlled (5mid2) detour. For a (3mid5) pair, [[toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set]] produces a complementary non-Hamiltonian matching-block four-set. Its local order is sharpened by [[toolkit_gives_an_interior_end_edge_reversal_or_a_central_sandwich]] to an interior end-edge reversal or a central sandwich. Two neutral (3mid5) rotations perform the two-for-two support exchange of [[toolkit_35_rotations_perform_a_controlled_two_for_two_support_exchange]].

The four size profiles have the following global consequences.

- In profile (3mid3mid5), [[toolkit_minimal_335_state_forces_a_cross_side_hamiltonian_five_support]] gives a Hamiltonian five-support meeting both three-sides and the interior triple of the five-side.
- In profile (3mid4mid4), [[toolkit_a_neutral_swap_an_order_disagreement_or_a_common_terminal_pair]] gives a neutral swap, an order disagreement, or a common terminal pair for two controlled Hamiltonian five-paths.
- In profile (3mid4mid5), [[toolkit_phi_minimal_345_state_has_a_nontrivial_neutral_reconfiguration]] gives a nontrivial equal-(Phi) reconfiguration.
- In profile (3mid5mid5), [[minimal_355_profile_has_a_neutral_cycle01]] shows that the three-side has distinct neutral rotations with both five-sides. Hence the equal-(Phi) state graph has minimum degree at least two and contains a nontrivial cycle.

Thus every (Phi)-minimal state containing a three-support carries a bounded support, an order disturbance, or explicit neutral recurrence.

### 3. Rooted four-supports

Let (X) be a Hamiltonian four-support containing the distinguished root, and let (C) be a disjoint tight path of order at least six. By [[four_path_long_pair_escape01]], one of the following occurs:

1. (Xmid C) admits a two-path repartition with strictly smaller quadratic contribution;
2. the endpoint six-shell (Xcup{c_1,c_m}) is non-Hamiltonian and Hamiltonian five-vertex deletions exhibit an order disagreement;
3. (m=6), the endpoint six-shell is Hamiltonian, and there is a neutral rooted migration
[
4mid6longrightarrow6mid4.
]

Consequently, at a quadratic minimum, a rooted four-support beside a path of order at least seven forces an order disagreement.

### 4. Rooted five-supports

Let (X) be a Hamiltonian five-support containing the root and let (C=(c_1,ldots,c_m)), (mge6). If one endpoint extends (X), then
[
5mid mlongrightarrow6mid(m-1),
]
with quadratic change (12-2m). This is neutral for (m=6) and strict for (mge7).

Assume neither endpoint extends (X). By [[five_side_endpoint_core_m6_01]] and [[toolkit_common_endpoint_core_or_a_two_pair_root_exchange_split]], either a common endpoint-replacement core preserves the root or the non-root vertices of (X) split into two endpoint-specific pairs. In the exceptional split, [[toolkit_forces_four_core_disturbance_or_an_outer_hamiltonian_six_shell]] yields a four-core order disagreement, a Hamiltonian four-set, a positioned core reversal, or a Hamiltonian six-shell.

Hence failure of numerical descent at support order five already produces a bounded order-theoretic obstruction or a rooted six-support.

### 5. Rooted six-supports

Let (X) be a proper Hamiltonian six-support containing the root, and write the non-Hamiltonian complement as
[
H-X=Pmid Q.
]
By [[rooted_six_support_transfer_or_comparison_disturbance01]], there is a non-root label (din X) such that (X-d) remains Hamiltonian and ((Pcup Q)+d) has path-cover number two. Comparing a two-cover of ((Pcup Q)+d) with the displayed partition
[
Pmid Qmid{d}
]
gives one of three outcomes:

1. (d) attaches to exactly one old support, producing a root-preserving one-label pairwise transfer;
2. one old support is split into two comparison blocks, yielding a split displayed edge or separated blocks;
3. a comparison edge joins (P) directly to (Q).

Thus rooted descent from a deletion-cover lift remains controlled through support order six. The possible outcomes are strict quadratic descent, explicit neutral recurrence, order disagreement or reversal, a bounded Hamiltonian core, or a comparison-cover disturbance.


## From bounded supports to defect compression


### Prescribed-vertex reduction of a six-support

Let (U) be a proper Hamiltonian six-support whose complement is non-Hamiltonian of path-cover number two. By [[prescribed_vertex_six_to_five_retention01]], for every prescribed vertex (ain U) there is a Hamiltonian five-subset (Fsubset U), (ain F), such that (H-F) is again non-Hamiltonian with path-cover number two.

Thus a positioned Hamiltonian six-shell need not be treated as a terminal object. Any distinguished vertex carried by it can be retained while the shell is reduced from order six to order five.

In particular, the neutral (4mid6	o6mid4) migration from [[four_path_long_pair_escape01]] produces a Hamiltonian six-shell containing both displayed endpoints of the old six-path. Prescribing either endpoint yields a Hamiltonian five-support containing that endpoint with two-coverable complement.

The same reduction applies to the Hamiltonian outer six-shell from [[toolkit_forces_four_core_disturbance_or_an_outer_hamiltonian_six_shell]] whenever a displayed extender vertex is to be retained.


### Six-support comparisons reduce to path disturbance

The comparison alternatives in [[rooted_six_support_transfer_or_comparison_disturbance01]] reduce to a dichotomy. With one interclass edge, the removable label attaches to exactly one old complementary path and produces a root-preserving one-label pairwise transfer. With at least two interclass edges, the block-count identity forces one old support to occur in at least two comparison blocks. Hence either a displayed inherited edge is split between the two comparison paths, or one comparison path leaves that support through a nonempty exterior segment and later returns.

Thus the six-support stage has only two essential outputs:
[
	ext{one-label transfer}qquad	ext{or}qquad	ext{path disturbance}.
]

### The four-support size barrier

The same local machinery gives a global size restriction. By [[phi_minimum_with_four_support_is_small_or_disagrees01]], if a quadratic-minimal state contains a component of order four, then either it already belongs to the classified order-three regime, an order disagreement is present, or every component order lies in ({4,5,6}). In the last case the entire counterexample has order at most eighteen.

Hence, before any defect-line argument is used, the rooted descent has already compressed the low-support regime into:
- the classified order-three profiles;
- an explicit order disagreement;
- or one of six bounded size profiles with orders between four and six.


## Metadata

- ID: line_rooted_small_support_descent_from_deletion_cover_lifts
- Kind: line
- Version: 8
- Math version: 7
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Chunk 1 — crystallized, version 6: Rooted descent through bounded supports
- Chunk 2 — HOT, version 3: From bounded supports to defect compression
