# Toolkit migration — Terminal local-witness obstructions have support at most twelve

Preserved from the retired Toolkit Limbo object [[terminal_local_witnesses_have_twelve_vertex_support]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T23:07:22.145901+00:00",
    "updated_at": "2026-10-04T23:34:46.005009+00:00",
    "archived_at": null,
    "original_id": "terminal_local_witnesses_have_twelve_vertex_support",
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

Every terminal obstruction in the nearest local-witness reduction is determined by at most twelve actual vertices.

## Statement

After selecting the nearest local witness in both color directions, centered cases use at most six vertices, reflected double cases at most ten, and a terminal single-sided bridging-block case at most twelve actual vertices.

## Body

Centered witnesses are themselves supported on one determining window, of size five or six. By [[dual_polarity_witness_reduction]], a reflected double occurrence has start separation at most three for a three-bit witness and at most four for a four-bit witness, so the union of its two determining windows has at most eight or ten vertices. In the single-sided terminal case, let the bridging block contribute alpha and beta positions to the two determining windows. [[terminal_local_block_bound]] gives block size at most alpha+beta. Adding the outside portions of two size-five windows gives at most ten vertices; for two size-six windows, at most twelve. Thus every terminal local-witness configuration has actual support at most twelve.

## Direct premises at migration

[
    {
        "premise_id": "dual_polarity_witness_reduction",
        "premise_kind": "toolkit",
        "premise_title": "Dual-polarity witness reduction",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "terminal_local_block_bound",
        "premise_kind": "toolkit",
        "premise_title": "Terminal local block bound",
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
