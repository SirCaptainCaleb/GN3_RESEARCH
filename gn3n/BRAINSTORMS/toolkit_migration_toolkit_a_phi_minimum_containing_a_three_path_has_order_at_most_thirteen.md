# Toolkit migration — A Phi-minimum containing a three-path has order at most thirteen

Preserved from the retired Toolkit Limbo object [[toolkit_a_phi_minimum_containing_a_three_path_has_order_at_most_thirteen]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:43:17.45993+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_a_phi_minimum_containing_a_three_path_has_order_at_most_thirteen",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        52
    ],
    "audited_math_version": null
}

## Simplified statement

In a minimum counterexample, if a Phi-minimal spanning three-cover has a component of order three, then the other two components have orders at most five. Since every component has order at least three and |V(H)|>10, the only possible size multisets are 3|3|5, 3|4|4, 3|4|5, and 3|5|5.

## Statement

Let H be a minimum counterexample and let C be a spanning three-cover minimizing Phi in its pairwise-repartition component. If one component of C has order three, then |V(H)|<=13. More precisely, the size multiset of C is one of {3,3,5}, {3,4,4}, {3,4,5}, {3,5,5}.

## Body

By toolkit_minimal_three_covers_have_no_components_of_order_one_or_two, every component of C has order at least three. Let one component T have order three. By three_vertex_component_long_neighbor_rotation01, T cannot sit beside a path of order at least six in a Phi-minimal state. Therefore each of the other two components has order at most five.

Hence |V(H)|<=3+5+5=13. On the other hand mincex01 gives |V(H)|>10. Writing the other two component orders as 3<=a<=b<=5 and requiring 3+a+b>10 leaves exactly

(3,3,5), (3,4,4), (3,4,5), (3,5,5).

Thus every Phi-minimal state of order at least fourteen has all three component orders at least four, and the entire three-component residue is confined to these four bounded profiles.

## Direct premises at migration

[
    {
        "premise_id": "mincex01",
        "premise_kind": "toolkit",
        "premise_title": "Minimum-counterexample calculus",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    },
    {
        "premise_id": "three_vertex_component_long_neighbor_rotation01",
        "premise_kind": "toolkit",
        "premise_title": "A three-vertex component beside a path of order at least six strictly descends",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "toolkit_minimal_three_covers_have_no_components_of_order_one_or_two",
        "premise_kind": "toolkit",
        "premise_title": "Quadratic-minimal three-covers have no components of order one or two",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "phi_minimum_with_four_support_is_small_or_disagrees01",
        "consumer_kind": "toolkit",
        "consumer_title": "A quadratic minimum containing a four-support is small or has an order disagreement",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
