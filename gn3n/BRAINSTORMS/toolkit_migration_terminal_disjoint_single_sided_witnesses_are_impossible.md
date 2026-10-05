# Toolkit migration — Terminal disjoint single-sided witness configurations are impossible

Preserved from the retired Toolkit Limbo object [[terminal_disjoint_single_sided_witnesses_are_impossible]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T00:03:31.065243+00:00",
    "updated_at": "2026-10-05T00:03:31.065243+00:00",
    "archived_at": null,
    "original_id": "terminal_disjoint_single_sided_witnesses_are_impossible",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        145
    ],
    "audited_math_version": null
}

## Simplified statement

The last two-vertex terminal bridge collapses, so terminal local-witness obstructions are only centered or reflected double/overlapping configurations.

## Statement

In the nearest dual-polarity local-witness reduction, no terminal disjoint single-sided configuration exists. The alternating branch is already impossible; in the remaining span-two branch the two-vertex bridge would have to flip four central protected statuses, which creates a closer span-two witness in one endpoint chamber.

## Body

Assume a terminal disjoint span-two configuration. By [[terminal_span_two_block_has_order_two]], the bridging block has order two and the four consecutive status coordinates between the reflected determining windows are monochromatic in every chamber. Both terminal colors occur. The chamber graph of the carrier face is connected. To change the common terminal color, all four central coordinates must change simultaneously; the existing two-vertex theorem identifies the unique central swap of the bridge vertices as the only possible state-changing generator. Hence some adjacent chambers differ only by this bridge swap and have central blocks CCCC and (1-C)^4. Let a be the status immediately to the left of the four central coordinates. The bridge swap does not change a. The three-bit window (a,C,C) is one status step closer to the center than the selected left span-two witness, so nearestness forbids it and forces a=C. In the swapped chamber the same closer window is (a,1-C,1-C), forcing a=1-C, contradiction. Therefore no two-vertex terminal span-two bridge exists. Together with the previous larger-block and alternating exclusions, no terminal disjoint single-sided local-witness configuration survives. The remaining terminal outcomes are centered witnesses and reflected double/overlapping witnesses.

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
        "premise_id": "terminal_alternating_witness_branch_is_impossible",
        "premise_kind": "toolkit",
        "premise_title": "The terminal alternating-witness branch is impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "terminal_span_two_block_has_order_two",
        "premise_kind": "toolkit",
        "premise_title": "A terminal span-two witness block has exactly two vertices",
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
