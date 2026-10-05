# Toolkit migration — Paired local witnesses splice or compress centrally

Preserved from the retired Toolkit Limbo object [[paired_local_witnesses_splice_or_compress_centrally]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-04T22:00:03.752062+00:00",
    "updated_at": "2026-10-04T23:34:39.25432+00:00",
    "archived_at": null,
    "original_id": "paired_local_witnesses_splice_or_compress_centrally",
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

Opposite innermost local witnesses either let the protected band expand, give a symmetric double witness, or force the first bad witness into constant distance from the status-word center.

## Statement

In a local-witness zero carrier, let e be the innermost used witness edge. If opposite e-witnesses can be separated by a face-block boundary, blockwise splicing removes e and moves the selected witness outward. Otherwise one block spans the protected corridor. Then the reflected witness starts differ by at most 7 for 001/011 and at most 8 for 0101, unless a chamber already carries both reflected e-witnesses.

## Body

Use opposite orientations of the innermost edge e supplied by [[local_witness_carriers_have_a_protected_central_band]]. If one chamber contains both reflected e-witnesses, keep that as a symmetric double-witness outcome. Otherwise choose chambers carrying the left-only and right-only witnesses. If a face-block boundary separates their determining windows, splice the good left side of the right-witness chamber with the good right side of the left-witness chamber. The new chamber has no e-witness, while all earlier edges are absent throughout the carrier, so the selected witness moves outward. If no such expansion is possible, one block spans the central protected gap. By [[five_protected_positions_are_impossible]], that block contains at most four consecutive protected positions. A 001/011 witness uses five determining vertex positions, giving reflected start separation at most 7; a 0101 witness uses six, giving separation at most 8.

## Direct premises at migration

[
    {
        "premise_id": "five_protected_positions_are_impossible",
        "premise_kind": "toolkit",
        "premise_title": "Five protected positions are impossible inside one face block",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 2,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "local_witness_carriers_have_a_protected_central_band",
        "premise_kind": "toolkit",
        "premise_title": "Local-witness carriers have a protected central band",
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

null
