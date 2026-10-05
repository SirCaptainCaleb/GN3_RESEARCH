# Toolkit migration — Five protected positions are impossible inside one face block

Preserved from the retired Toolkit Limbo object [[five_protected_positions_are_impossible]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T22:05:30.039408+00:00",
    "updated_at": "2026-10-04T23:33:14.591842+00:00",
    "archived_at": null,
    "original_id": "five_protected_positions_are_impossible",
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

If every chamber of a permutahedron face avoids the two-cover forbidden patterns on a common interval, no face block can contain five consecutive protected vertex positions.

## Statement

Let five consecutive vertex positions lie in one block of a permutahedron face, and suppose every chamber avoids 001, 011, and 0101 on the corresponding protected status interval. Then contradiction. Hence the protected width of any face block is at most four.

## Body

Write h(u,v,w)=1 when (u,v,w) is tight. Five vertices inside one face block may be placed in every order. Protection forbids epsilon_1=0 and epsilon_3=1 simultaneously, so every ordering (a,b,c,d,e) satisfies h(c,d,e)=1 => h(a,b,c)=1. Together with boundary antisymmetry, the seven orderings (20134),(02431),(13024),(03142),(14203),(14302),(20143) give the implication chain h(102)=1 => h(134)=0 => h(024)=1 => h(031)=0 => h(142)=0 => h(203)=0 => h(143)=1 => h(102)=0. Thus h(102)=0. The seven orderings (10234),(01432),(23014),(03241),(24103),(10342),(10243) similarly give h(102)=0 => h(234)=0 => h(014)=1 => h(032)=0 => h(142)=1 => h(103)=0 => h(243)=1 => h(102)=1, contradiction. Therefore five protected positions cannot lie in one block.

## Direct premises at migration

[
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
        "consumer_id": "paired_local_witnesses_splice_or_compress_centrally",
        "consumer_kind": "toolkit",
        "consumer_title": "Paired local witnesses splice or compress centrally",
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
