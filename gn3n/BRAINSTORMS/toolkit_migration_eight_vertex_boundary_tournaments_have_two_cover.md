# Toolkit migration — Every eight-vertex boundary tournament has a two-cover

Preserved from the retired Toolkit Limbo object [[eight_vertex_boundary_tournaments_have_two_cover]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T01:15:15.30356+00:00",
    "updated_at": "2026-10-05T01:16:03.959881+00:00",
    "archived_at": null,
    "original_id": "eight_vertex_boundary_tournaments_have_two_cover",
    "audit_status": "passed",
    "math_version": 1,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": 1
}

## Simplified statement

Every boundary tournament on eight vertices has path-cover number at most two.

## Statement

Let H be a boundary tournament on eight vertices. Then pc(H)<=2.

## Body

Choose any six vertices S. By [[smallset01]], S contains a Hamiltonian five-subset F. The remaining three vertices V(H)-F admit a tight three-vertex order by boundary antisymmetry. Thus F and its three-vertex complement form a spanning two-cover.

## Direct premises at migration

[
    {
        "premise_id": "smallset01",
        "premise_kind": "toolkit",
        "premise_title": "Small-order Hamiltonicity and structure",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "every_terminal_local_witness_support_is_two_coverable",
        "consumer_kind": "toolkit",
        "consumer_title": "Every terminal local-witness support is two-coverable",
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
