# Toolkit migration — Quadratic-minimal three-covers have no components of order one or two

Preserved from the retired Toolkit Limbo object [[toolkit_minimal_three_covers_have_no_components_of_order_one_or_two]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:26:43.68038+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_minimal_three_covers_have_no_components_of_order_one_or_two",
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

In a minimum counterexample, every Phi-minimal spanning three-cover has all three component orders at least three. A singleton beside an s-path with s>=3 repartitions as 2|(s-1), and a two-vertex component beside an s-path with s>=4 repartitions as 3|(s-1), strictly decreasing Phi.

## Statement

Let H be a minimum counterexample and let P_1|P_2|P_3 be a spanning three-cover that minimizes Phi=sum |P_i|^2 in its pairwise-repartition component. Then |P_i|>=3 for each i.

## Body

Suppose first that one component is a singleton (x). Since |V(H)|>10, among the other two components one has order s>=5, say C=(c_1,...,c_s). The pair (x,c_1) is a tight path of order two by definition, while (c_2,...,c_s) is the inherited suffix of C. Thus the pairwise repartition

(x)|C  ->  (x,c_1)|(c_2,...,c_s)

changes the affected component orders from (1,s) to (2,s-1). Its potential change is

2^2+(s-1)^2-1^2-s^2 = 4-2s < 0,

contradicting Phi-minimality.

Suppose instead that one component has order two. The other two component orders sum to more than eight, so one has order at least five. The general two-vertex balancing lemma repartitions (2,s) to (3,s-1), with potential change 6-2s<0. Again this contradicts Phi-minimality.

Therefore every component of a Phi-minimal spanning three-cover has order at least three.

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
        "premise_id": "toolkit_two_vertex_middle_component_forces_strict_quadratic_descent",
        "premise_kind": "toolkit",
        "premise_title": "Any two-vertex component beside a path of order at least four strictly descends",
        "compatibility_status": "confirmed",
        "premise_math_version": 2,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "quadratic_potential_and_pairwise_repartition_absolute_minima",
        "consumer_kind": "section",
        "consumer_title": "Absolute minima",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": false
    },
    {
        "consumer_id": "toolkit_a_phi_minimum_containing_a_three_path_has_order_at_most_thirteen",
        "consumer_kind": "toolkit",
        "consumer_title": "A Phi-minimum containing a three-path has order at most thirteen",
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
