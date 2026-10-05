# Toolkit migration — Two spare dimensions force a prescribed triple into one face block

Preserved from the retired Toolkit Limbo object [[two_spare_dimensions_force_three_vertices_into_one_block]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T22:28:56.429358+00:00",
    "updated_at": "2026-10-04T22:28:56.429358+00:00",
    "archived_at": null,
    "original_id": "two_spare_dimensions_force_three_vertices_into_one_block",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": null
}

## Simplified statement

The two-dimensional slack in the local-witness map can be spent on two relative-order coordinates, forcing any prescribed three vertices into one block of a balanced carrier face.

## Statement

If H has no two-cover and a,b,c are distinct vertices, augment the local-witness odd map by the pair-order signs g_ab and g_bc. Borsuk-Ulam still applies. In any positive zero carrier, both signs of each pair-order coordinate must occur, so a,b lie in one face block and b,c lie in one face block. Thus a,b,c lie in one common block.

## Body

The local-witness map has domain dimension n-2 and target dimension n-4. Append the two odd coordinates g_ab and g_bc. The augmented target has dimension n-2, so a zero exists. In its positive carrier face, if a,b were in different blocks their order would be fixed in every chamber and g_ab could not average to zero. Hence a,b share a block. Likewise b,c share a block, so a,b,c share one block.

## Direct premises at migration

[
    {
        "premise_id": "local_witness_path_topology",
        "premise_kind": "toolkit",
        "premise_title": "Local-witness path topology",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
