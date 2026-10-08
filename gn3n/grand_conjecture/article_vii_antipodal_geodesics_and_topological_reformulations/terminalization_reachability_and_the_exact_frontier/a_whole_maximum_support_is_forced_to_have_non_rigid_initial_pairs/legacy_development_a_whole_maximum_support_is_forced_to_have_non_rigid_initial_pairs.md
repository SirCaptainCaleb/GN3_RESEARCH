# A whole maximum support is forced to have non-rigid initial pairs — preserved pre-item development

## The majority theorem has a supportwise contrapositive

Assume the odd uniform residue on n=2r+1 vertices and suppose, for contradiction, that no tight path of order r+1 exists.

Call an r-support S initial-rigid if it has at least one Hamilton order
P=(a,b,...)
for which a is a universal source of the centered tournament T_b, equivalently
(a,b,z)
is tight for every z outside {a,b}.

The majority-coloring theorem
[[a_majority_coloring_closes_universal_endpoint_pair_rigidity_and_yields_an_anchored_three_vertex_prefix]]
was proved after choosing one Hamilton order independently on every r-support. Its hypothesis is exactly that every chosen order has a universally rigid initial pair.

Therefore not every r-support can be initial-rigid. Otherwise choose, for each r-support S, one Hamilton order witnessing initial rigidity. The majority-coloring theorem then produces an actual (r+1)-path, contradiction.

Hence there exists an r-support S_* such that:

> Every Hamilton order P=(a,b,...) of H[S_*] has a non-universal initial pair.

For each such order there is therefore some vertex u outside {a,b} with
(u,b,a)
tight. The witness cannot be the third vertex of P, because (a,b,p_3) is tight and its boundary reverse is non-tight.

Thus one fixed maximum support S_* supplies a reversed-pair anchor for every Hamilton order on S_*.

## Each initial pair of S_* generates a fixed-terminal obstruction

Fix any Hamilton order P=(a,b,...) of S_* and choose a witness u with (u,b,a) tight.

By
[[an_unused_vertex_converts_a_reversed_endpoint_pair_match_into_an_actual_two_cover]],
no maximum r-path can end in the reversed ordered pair (b,a), because P begins with (a,b).

Choose a longest tight path ending in (b,a). Then
[[longest_reversed_pair_paths_force_a_large_endpoint_desert_and_a_two_edge_reversal_fan]]
applies: its order is between 3 and r-1, its first edge is reversed through every exterior vertex, and it creates a co-large family of r-supports on which its initial root is forbidden as an initial endpoint.

Consequently the surviving odd-uniform residue contains not merely one endpoint desert, but one such desert for every initial ordered pair realized by a Hamilton order of S_*.

The terminal analogue is obtained by applying the terminal form of the majority-coloring theorem: there is also an r-support T_* such that every Hamilton order ending (...,b,a) has a non-universal terminal pair, unless an (r+1)-path already exists.

## Why this strengthens the frontier

The current endpoint-growth obstruction was generated from one selected maximum word. The supportwise contrapositive removes that arbitrariness. Any closure argument may now choose the Hamilton order on S_* most convenient for a splice, exchange, or endpoint comparison, and the reversed-pair anchor is guaranteed to exist for that choice.

In particular, if a later argument can realize one ordered pair (a,b) as the initial pair of a Hamilton order on S_* with additional prescribed incidence data, no separate non-universality proof is required: the corresponding reversed anchor follows automatically.
