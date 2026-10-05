# Toolkit migration — Every terminal local-witness support is two-coverable

Preserved from the retired Toolkit Limbo object [[every_terminal_local_witness_support_is_two_coverable]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T01:16:22.411953+00:00",
    "updated_at": "2026-10-05T01:16:43.385906+00:00",
    "archived_at": null,
    "original_id": "every_terminal_local_witness_support_is_two_coverable",
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

Every finite terminal support arising from the nearest dual-polarity local-witness reduction has path-cover number at most two.

## Statement

Assume the nearest dual-polarity local-witness reduction has reached any terminal finite support. Then the induced boundary tournament on that support has path-cover number at most two.

## Body

Centered span-two and centered alternating witnesses use at most five and six actual vertices, respectively; partition into subsets of order at most three to obtain a two-cover. By [[dual_polarity_witness_reduction]], reflected double span-two supports have order at most eight and reflected alternating supports have order at most ten. The former are two-coverable by [[eight_vertex_boundary_tournaments_have_two_cover]], and the latter by [[ten_vertex_boundary_tournaments_have_two_cover]]. In the disjoint single-sided branch, [[terminal_alternating_witness_branch_is_impossible]] removes alternating type, [[terminal_local_block_sharpens_to_four]] and [[terminal_span_two_blocks_three_and_four_are_impossible]] reduce span-two type to the two-vertex bridging toggle, and [[terminal_two_vertex_toggle_forces_two_cover]] gives an explicit two-cover. Hence every terminal support in the local-witness reduction is two-coverable.

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
        "premise_id": "eight_vertex_boundary_tournaments_have_two_cover",
        "premise_kind": "toolkit",
        "premise_title": "Every eight-vertex boundary tournament has a two-cover",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "ten_vertex_boundary_tournaments_have_two_cover",
        "premise_kind": "toolkit",
        "premise_title": "Every ten-vertex boundary tournament has a two-cover",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "terminal_alternating_witness_branch_is_impossible",
        "premise_kind": "toolkit",
        "premise_title": "The terminal alternating-witness branch is impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "terminal_local_block_sharpens_to_four",
        "premise_kind": "toolkit",
        "premise_title": "Terminal local witness blocks have at most four vertices",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "terminal_span_two_blocks_three_and_four_are_impossible",
        "premise_kind": "toolkit",
        "premise_title": "Terminal span-two blocks of order three or four are impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "terminal_two_vertex_toggle_forces_two_cover",
        "premise_kind": "toolkit",
        "premise_title": "One-polarity two-vertex toggle has a canonical local two-cover",
        "compatibility_status": "confirmed",
        "premise_math_version": 3,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

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
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
