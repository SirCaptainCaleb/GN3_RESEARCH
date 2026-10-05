# Toolkit migration — Terminal local block bound

Preserved from the retired Toolkit Limbo object [[terminal_local_block_bound]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T22:46:18.202729+00:00",
    "updated_at": "2026-10-04T23:33:22.928199+00:00",
    "archived_at": null,
    "original_id": "terminal_local_block_bound",
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

A terminal bridging block has size at most the total number of positions it contributes to the two local determining windows.

## Statement

If a terminal carrier block contributes alpha positions to the left determining window and beta positions to the right, and every chamber realizes exactly one of the two local states while both sides occur somewhere, then the block has size at most alpha+beta.

## Body

The left state depends on an ordered alpha-tuple from the block and the right state on an ordered beta-tuple. Compatible tuples are disjoint. If the block had at least alpha+beta+1 vertices, the bipartite disjointness graph on these ordered tuples would be connected. The identity that exactly one side occurs on every compatible pair would then force both state functions to be constant, contradicting occurrence of both sides. Hence the block has size at most alpha+beta.

## Direct premises at migration

[]

## Direct consumers at migration

[
    {
        "consumer_id": "local_witness_topology_and_the_finite_terminal_theorem",
        "consumer_kind": "section",
        "consumer_title": "Local-witness topology and the finite terminal theorem",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": false
    },
    {
        "consumer_id": "terminal_local_block_sharpens_to_four",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal local witness blocks have at most four vertices",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_local_witnesses_have_twelve_vertex_support",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal local-witness obstructions have support at most twelve",
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
