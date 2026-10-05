# Toolkit migration — Dual-polarity witness reduction

Preserved from the retired Toolkit Limbo object [[dual_polarity_witness_reduction]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T23:07:02.953278+00:00",
    "updated_at": "2026-10-04T23:34:43.648542+00:00",
    "archived_at": null,
    "original_id": "dual_polarity_witness_reduction",
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

Selecting the nearest local inversion witness in either color direction makes every two-sided occurrence bounded near the center.

## Statement

Use local witnesses in both color directions and select the witness-location pair nearest the status-word center. A noncentered witness occurring on both reflected sides has start separation at most 3 for three-bit witnesses and at most 4 for four-bit alternating witnesses.

## Body

The local witnesses are the three patterns for a nonadjacent zero-to-one inversion together with their color complements. An interval avoiding all six has no unequal pair of bits at distance at least two, so an interval of length at least four is monochromatic. Between two reflected copies of the nearest selected witness there is no closer witness of either color direction. Their inward-facing bits are opposite. Hence the intervening interval has length at most two, giving the stated separation bounds. Centered self-reflecting witnesses are handled separately by the antipodal tie-break sign.

## Direct premises at migration

[
    {
        "premise_id": "two_cover_words_avoid_three_local_patterns",
        "premise_kind": "toolkit",
        "premise_title": "Two-cover status words avoid three local patterns",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "dual_polarity_terminal_span_two_branch_is_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "The dual-polarity terminal span-two branch is impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "every_terminal_local_witness_support_is_two_coverable",
        "consumer_kind": "toolkit",
        "consumer_title": "Every terminal local-witness support is two-coverable",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_alternating_witness_branch_is_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "The terminal alternating-witness branch is impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_disjoint_single_sided_witnesses_are_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal disjoint single-sided witness configurations are impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_local_witness_support_sharpens_to_ten",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal dual-polarity local-witness support is bounded by ten vertices",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
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
    },
    {
        "consumer_id": "terminal_span_two_block_has_order_two",
        "consumer_kind": "toolkit",
        "consumer_title": "A terminal span-two witness block has exactly two vertices",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_span_two_blocks_three_and_four_are_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal span-two blocks of order three or four are impossible",
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
