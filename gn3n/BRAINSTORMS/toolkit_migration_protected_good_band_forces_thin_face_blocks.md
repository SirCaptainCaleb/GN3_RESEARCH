# Toolkit migration — A protected good band forces thin face blocks

Preserved from the retired Toolkit Limbo object [[protected_good_band_forces_thin_face_blocks]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T21:57:36.886747+00:00",
    "updated_at": "2026-10-04T23:34:37.547378+00:00",
    "archived_at": null,
    "original_id": "protected_good_band_forces_thin_face_blocks",
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

A common forbidden-pattern-free status interval cannot contain two disjoint three-position windows internal to face blocks; hence at most one block has protected width at least three, and that width is at most five.

## Statement

Let F be a permutahedron face and J an interval of status positions such that every chamber avoids 001, 011, and 0101 on J. Then no i<j in J with j-i>=3 can have both vertex windows i..i+2 and j..j+2 lying wholly inside face blocks. Consequently at most one block has protected width at least three, and no block has protected width at least six.

## Body

If two such internal windows existed, [[disjoint_status_windows_form_boolean_cubes]] would give a chamber with epsilon_i=0 and epsilon_j=1. Since j-i>=3, [[two_cover_words_avoid_three_local_patterns]] forces 001, 011, or 0101 between i and j, contradicting that J is protected. Two distinct blocks with internal protected triple windows would therefore be impossible. A single block with six protected vertex positions contains two disjoint internal triple windows, also impossible.

## Direct premises at migration

[
    {
        "premise_id": "disjoint_status_windows_form_boolean_cubes",
        "premise_kind": "toolkit",
        "premise_title": "Disjoint internal status windows form Boolean cubes",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "local_witness_carriers_have_a_protected_central_band",
        "premise_kind": "toolkit",
        "premise_title": "Local-witness carriers have a protected central band",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
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
        "consumer_id": "five_protected_positions_are_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "Five protected positions are impossible inside one face block",
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
