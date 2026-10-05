# Toolkit migration — The dual-polarity terminal span-two branch is impossible

Preserved from the retired Toolkit Limbo object [[dual_polarity_terminal_span_two_branch_is_impossible]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T01:10:57.425487+00:00",
    "updated_at": "2026-10-05T01:11:24.702788+00:00",
    "archived_at": null,
    "original_id": "dual_polarity_terminal_span_two_branch_is_impossible",
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

Under nearest-witness selection using both inversion polarities, no disjoint single-sided terminal span-two configuration can occur.

## Statement

Assume a terminal disjoint single-sided configuration for the nearest dual-polarity local witness, with selected span-two type among 001,011,110,100. The protected central statuses are monochromatic. Then the chamber carrying the selected left witness necessarily contains a strictly closer witness of one of the six dual-polarity forbidden types, contradiction.

## Body

Let the selected reflected span-two witness pair have left and right starts, and consider a chamber carrying only the left occurrence. By the protected-band/terminal hypotheses, the four central statuses between the two determining windows are monochromatic. Normalize the eight relevant statuses so the left witness begins at position 1 and the reflected right witness would begin at position 6. There are four span-two types. If the selected left pattern is 001, continuation into the monochromatic center forces 011 beginning at position 2. If it is 110, continuation forces 100 beginning at position 2. If it is 011, the reflected-side boundary of the monochromatic center forces 110 beginning at position 5. If it is 100, that boundary forces 001 beginning at position 5. In each case the new witness belongs to the six dual-polarity patterns 001,011,0101,110,100,1010 and is represented by a witness edge strictly closer to the center than the selected reflected pair. This contradicts nearest-witness selection. Therefore no disjoint single-sided terminal span-two configuration exists in the dual-polarity framework.

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
        "premise_id": "protected_good_band_forces_thin_face_blocks",
        "premise_kind": "toolkit",
        "premise_title": "A protected good band forces thin face blocks",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
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
    },
    {
        "consumer_id": "terminal_local_witness_support_sharpens_to_ten",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal dual-polarity local-witness support is bounded by ten vertices",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
