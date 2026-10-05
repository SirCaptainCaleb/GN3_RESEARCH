# Toolkit migration — Local-witness carriers have a protected central band

Preserved from the retired Toolkit Limbo object [[local_witness_carriers_have_a_protected_central_band]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T21:56:49.481474+00:00",
    "updated_at": "2026-10-04T23:34:35.680346+00:00",
    "archived_at": null,
    "original_id": "local_witness_carriers_have_a_protected_central_band",
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

Order the fixed witness path from its centered pendant edge outward. In any balanced carrier face, the innermost occurring label determines a common central band in which every chamber avoids all three forbidden two-cover patterns; both reflected orientations of the first possible bad witness occur at the band boundary.

## Statement

In the local-witness path topology, order the edges of T_m from the centered pendant edge outward and choose the first represented edge in each bad word. If F is a zero carrier face and e is the earliest path edge occurring among its chamber labels, then no chamber of F contains a forbidden-pattern witness on any earlier edge, while F contains labels in both orientations of e. Hence all chamber status words have a common central interval free of 001, 011, and 0101, so that interval has two-cover form 1*0* or 1*010*.

## Body

Use the path T_m from [[local_bad_patterns_label_a_fixed_path]] and order its edges starting at the pendant edge for the centered witness and then moving outward along the path. Choose the first represented edge under this order when labeling a bad word. Let F be a zero carrier face supplied by [[local_witness_path_topology]], and let e be the earliest tree edge occurring among the chamber labels of F. By definition of the selected label, every chamber of F contains no forbidden-pattern occurrence represented by an edge earlier than e. Tree-edge balance gives chambers labeled by both orientations of e. The edges earlier than e represent exactly the reflected pairs of forbidden-pattern locations closer to the center of the status word. Therefore all chambers have a common central band containing no occurrence of 001, 011, or 0101, and the first possible bad witness is realized on both reflected sides by chambers of F. By [[two_cover_words_avoid_three_local_patterns]], any binary word segment avoiding these three patterns has the restricted local form 1*0* or 1*010* on that band.

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
        "consumer_id": "far_double_witnesses_are_frozen_or_breakable",
        "consumer_kind": "toolkit",
        "consumer_title": "Far symmetric witnesses are frozen or breakable",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
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
    },
    {
        "consumer_id": "protected_good_band_forces_thin_face_blocks",
        "consumer_kind": "toolkit",
        "consumer_title": "A protected good band forces thin face blocks",
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
