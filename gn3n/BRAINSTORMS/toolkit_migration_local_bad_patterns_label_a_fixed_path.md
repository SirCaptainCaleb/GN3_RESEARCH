# Toolkit migration — Local bad patterns label a fixed path

Preserved from the retired Toolkit Limbo object [[local_bad_patterns_label_a_fixed_path]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-04T21:52:47.77953+00:00",
    "updated_at": "2026-10-04T23:33:10.790055+00:00",
    "archived_at": null,
    "original_id": "local_bad_patterns_label_a_fixed_path",
    "audit_status": "passed",
    "math_version": 2,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": 2
}

## Simplified statement

For spanning orders, the forbidden patterns 001, 011, and 0101 admit a reverse-complement-equivariant labeling by oriented edges of one fixed path once an external antipodal gauge is fixed; any positive zero balance is edgewise.

## Statement

Fix a boundary tournament on n vertices and an antipodal sign g on spanning orders, for example the relative-order sign of two fixed vertices. The forbidden status patterns 001, 011, and 0101 can be encoded by oriented edges of a fixed path T_m, m=n-2, so that the label of pi^rev is the negative of the label of pi. The edge-incidence vectors are nonzero and linearly independent up to orientation, so any positive convex zero balances each used edge separately.

## Body

Let pi be a spanning order with bad status word w of length m=n-2. By [[two_cover_words_avoid_three_local_patterns]], w contains 001, 011, or 0101. A length-three witness beginning at i is associated with the pair i and m-1-i; a 0101 witness beginning at i is associated with i and m-2-i. Reverse-complement preserves the underlying pair and reverses its witness orientation. The non-loop edges from these two reflections form one path on the start-position coordinates; the unique centered self-pair lies at an endpoint. Replace that self-pair by a pendant edge to a new vertex. Fix an antipodal sign g on spanning orders, g(pi^rev)=-g(pi), such as the sign of the relative order of two fixed underlying vertices. Fix an ordering of the path edges. For each bad order choose the first path edge represented by one of its forbidden-pattern occurrences. If exactly one witness orientation of that edge occurs, use it. If both orientations occur, use g(pi) to choose the edge orientation. On the centered pendant edge use the two centered length-three pattern types when they are exchanged by reverse-complement, and use g for a self-reverse-complement centered alternating pattern. This gives a nonzero oriented edge label ell(pi) with ell(pi^rev)=-ell(pi). The incidence vectors of the edges of a tree are linearly independent, so any positive relation sum lambda_pi ell(pi)=0 balances the two orientations of every used edge separately. The construction is a statement about spanning orders equipped with an antipodal gauge, not about binary words alone.

## Direct premises at migration

[
    {
        "premise_id": "two_cover_words_avoid_three_local_patterns",
        "premise_kind": "toolkit",
        "premise_title": "Two-cover status words avoid three local patterns",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "local_witness_path_topology",
        "consumer_kind": "toolkit",
        "consumer_title": "Local-witness path topology",
        "compatibility_status": "confirmed",
        "premise_math_version": 2,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "local_witness_topology_and_the_finite_terminal_theorem",
        "consumer_kind": "section",
        "consumer_title": "Local-witness topology and the finite terminal theorem",
        "compatibility_status": "confirmed",
        "premise_math_version": 2,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": false
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
