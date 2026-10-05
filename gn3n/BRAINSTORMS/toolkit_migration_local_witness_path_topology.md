# Toolkit migration — Local-witness path topology

Preserved from the retired Toolkit Limbo object [[local_witness_path_topology]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T21:54:45.527977+00:00",
    "updated_at": "2026-10-04T23:33:12.851958+00:00",
    "archived_at": null,
    "original_id": "local_witness_path_topology",
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

No two-cover implies a two-dimensional family of balanced carrier faces for local forbidden witnesses, with every used tree edge paired in both orientations.

## Statement

If H has n vertices and no two-cover, the fixed-path local witness labels define an odd map from the permutahedron sphere S^(n-2) into an (n-4)-dimensional tree-edge space. Its zero set has dimension at least two, and in every zero carrier face each used witness edge appears in both orientations.

## Body

Put m=n-2. By [[local_bad_patterns_label_a_fixed_path]], every spanning order has a nonzero oriented edge label ell(pi) of a fixed path T_m, and ell(pi^rev)=-ell(pi). The edge-incidence vectors of T_m span a space W of dimension m-2. Average ell over the chamber vertices of each permutahedron face and extend over the barycentric subdivision. This gives a continuous odd map from the permutahedron boundary S^m to W. Bourgin--Yang gives a zero set of dimension at least 2. At any zero, the carrier-face expansion gives strictly positive coefficients on every chamber with weighted label sum zero. Because tree-edge incidence vectors are linearly independent, cancellation is edgewise: for every tree edge represented among the chamber labels, both orientations occur in the carrier face.

## Direct premises at migration

[
    {
        "premise_id": "local_bad_patterns_label_a_fixed_path",
        "premise_kind": "toolkit",
        "premise_title": "Local bad patterns label a fixed path",
        "compatibility_status": "confirmed",
        "premise_math_version": 2,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "local_witness_carriers_have_a_protected_central_band",
        "consumer_kind": "toolkit",
        "consumer_title": "Local-witness carriers have a protected central band",
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
        "consumer_id": "two_spare_dimensions_force_three_vertices_into_one_block",
        "consumer_kind": "toolkit",
        "consumer_title": "Two spare dimensions force a prescribed triple into one face block",
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
