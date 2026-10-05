# Toolkit migration — Terminal dual-polarity local-witness support is bounded by ten vertices

Preserved from the retired Toolkit Limbo object [[terminal_local_witness_support_sharpens_to_ten]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-04T23:52:43.644528+00:00",
    "updated_at": "2026-10-05T01:11:36.534429+00:00",
    "archived_at": null,
    "original_id": "terminal_local_witness_support_sharpens_to_ten",
    "audit_status": "unaudited",
    "math_version": 2,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": 1
}

## Simplified statement

In the nearest dual-polarity local-witness reduction, every terminal configuration is centered or overlapping and is supported on at most ten actual vertices.

## Statement

Assume the nearest dual-polarity local-witness reduction reaches a terminal configuration. The disjoint single-sided alternating branch is impossible, and the disjoint single-sided span-two branch is impossible. Therefore any terminal configuration is centered or overlapping; by the dual-polarity reflected-witness bound, its determining support has order at most ten.

## Body

Use the nearest-witness ordering for all six local patterns 001,011,0101,110,100,1010. By [[terminal_alternating_witness_branch_is_impossible]], no disjoint single-sided terminal configuration of alternating type 0101 or 1010 exists. By [[dual_polarity_terminal_span_two_branch_is_impossible]], no disjoint single-sided terminal configuration of span-two type 001,011,110,100 exists. Hence every terminal dual-polarity configuration is centered or has overlapping reflected determining windows. The dual-polarity reduction [[dual_polarity_witness_reduction]] bounds the reflected start separation by at most three for a span-two witness and at most four for an alternating witness. The union of the two determining windows therefore uses at most eight actual vertices in the span-two case and at most ten in the alternating case. Thus every terminal configuration has actual support at most ten. This version deliberately does not use the separate one-polarity two-vertex toggle normal form.

## Direct premises at migration

[
    {
        "premise_id": "dual_polarity_terminal_span_two_branch_is_impossible",
        "premise_kind": "toolkit",
        "premise_title": "The dual-polarity terminal span-two branch is impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "dual_polarity_witness_reduction",
        "premise_kind": "toolkit",
        "premise_title": "Dual-polarity witness reduction",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "terminal_alternating_witness_branch_is_impossible",
        "premise_kind": "toolkit",
        "premise_title": "The terminal alternating-witness branch is impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

{
    "body": "Centered cases occupy one five- or six-vertex determining window. By [[dual_polarity_witness_reduction]], a reflected double occurrence has start separation at most three for a span-two witness and at most four for an alternating witness, so the union of its two determining windows has at most eight or ten vertices. By [[terminal_alternating_witness_branch_is_impossible]], no disjoint single-sided alternating terminal configuration survives. In the disjoint span-two branch, [[terminal_local_block_sharpens_to_four]] leaves block sizes two, three, or four, and [[terminal_span_two_blocks_three_and_four_are_impossible]] eliminates sizes three and four. Thus alpha=beta=1 and the bridging block has two vertices. The two five-vertex determining windows are adjacent, so their union has exactly ten vertices. Hence every terminal configuration in the reduction is supported on at most ten actual vertices.",
    "statement": "Assume the local-witness reduction has reached a terminal configuration. Centered witnesses use at most six vertices; reflected double/overlapping witnesses use at most eight vertices for span-two type and ten for alternating type; the disjoint single-sided alternating branch is impossible; and the surviving disjoint span-two branch has a two-vertex bridging block, hence total determining support ten. Therefore every terminal configuration has support at most ten.",
    "audited_by": 148,
    "created_at": "2026-10-05T01:11:36.534429+00:00",
    "research_id": "terminal_local_witness_support_sharpens_to_ten",
    "audit_status": "passed",
    "math_version": 1,
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "simplified_statement": "Every terminal configuration in the nearest dual-polarity local-witness reduction is supported on at most ten actual vertices."
}
