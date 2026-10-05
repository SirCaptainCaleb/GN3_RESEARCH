# Toolkit migration — A leaf support reduces endpoint comparison to path disturbance, reversal, descent, or an omission swap

Preserved from the retired Toolkit Limbo object [[toolkit_to_path_disturbance_reversal_descent_or_an_omission_swap]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:29:38.202404+00:00",
    "updated_at": "2026-10-03T14:46:26.014622+00:00",
    "archived_at": "2026-10-03T14:46:26.014622+00:00",
    "original_id": "toolkit_to_path_disturbance_reversal_descent_or_an_omission_swap",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        51
    ],
    "audited_math_version": null
}

## Simplified statement

In the support-forest leaf case, endpoint comparison has no diffuse direct-cut interaction residue: it reduces to order/path disturbance, endpoint reversal, a two-cover, strict quadratic descent, or a neutral compatible omission swap.

## Statement

Let H be a minimum counterexample and choose deletion covers whose selected support graph is a forest. If H-x=P|Q corresponds to a leaf edge with P the leaf support and y is a displayed endpoint of Q, then the selected deletion cover at y yields an order disagreement, a displayed inherited edge of P or Q-y split between its two paths, a leave-and-return path segment through exterior vertices, a tight triple reversing the displayed endpoint edge of Q, a two-cover of H, a strict quadratic-potential decrease from the singleton lift at y, or a Phi-neutral omission swap to another deletion cover compatible with the selected cover at y.

## Body

Let H be a minimum counterexample. Choose one deletion cover F_v for each vertex v, and let J be the selected support graph. Assume J is a forest. Let
H-x=P|Q
be a selected deletion cover whose support P is a leaf of J, and let y be an endpoint of the displayed path Q. Put B=Q-{y}, with the inherited order.

By the leaf-support endpoint comparison, the selected deletion cover F_y has one of the following properties:

(i) an edge of F_y joins a surviving vertex of P to a surviving vertex of B; or

(ii) a displayed edge of P has its endpoints in different paths of F_y.

In case (ii) the asserted split-edge outcome already holds.

Assume case (i). Regard H-x=P|Q as the base deletion cover, regard y as the displayed endpoint of Q, and compare it with F_y. Apply the direct-mixed-edge disturbance theorem to the displayed path Q, its endpoint y, and the comparison cover F_y.

If the surviving vertices of B do not occur in inherited relative order inside the paths of F_y, there is an order disagreement. Otherwise that theorem gives at least one of the following:

1. an inherited edge of B has its endpoints in different paths of F_y;
2. one path of F_y leaves B through a nonempty exterior segment and later returns to B;
3. a tight triple reverses the displayed endpoint edge of Q incident with y;
4. H has a two-cover;
5. the singleton lift F_y|{y} admits a strict quadratic-potential decrease by one pairwise repartition;
6. the endpoint restoration is Phi-neutral and, after omitting the unique transferred vertex, gives another deletion cover compatible with F_y on their common domain.

Combining case (ii) with these alternatives proves the statement.

Thus, for a leaf support in the selected support forest, an ordinary edge joining the two old supports is not an additional terminal configuration. It immediately resolves into one of the listed order-theoretic, path-theoretic, or potential-theoretic alternatives.

## Direct premises at migration

[
    {
        "premise_id": "leaf_endpoint_singleton_triangle01",
        "premise_kind": "toolkit",
        "premise_title": "Leaf endpoint comparison forces direct mixing or splits the old support",
        "compatibility_status": "optimistic",
        "premise_math_version": 3,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "path_disturbance_endpoint_reversal_descent_or_an_omission_swap",
        "premise_kind": "toolkit",
        "premise_title": "Two deletion covers with a direct mixed edge force path disturbance, endpoint reversal, descent, or an omission swap",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    }
]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
