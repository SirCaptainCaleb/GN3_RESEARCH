# Toolkit migration — Far symmetric witnesses are frozen or breakable

Preserved from the retired Toolkit Limbo object [[far_double_witnesses_are_frozen_or_breakable]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T22:28:15.064039+00:00",
    "updated_at": "2026-10-04T23:34:41.553157+00:00",
    "archived_at": null,
    "original_id": "far_double_witnesses_are_frozen_or_breakable",
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

When reflected local-witness determining windows use disjoint sets of face blocks, absence of a single-sided witness forces both witness indicators to be constant across the entire face.

## Statement

Let F be a permutahedron face and let L,R be indicators of two reflected forbidden-pattern occurrences whose determining windows meet disjoint sets of face blocks. If F contains a chamber with L=R=1 and contains no chamber with exactly one of L,R equal to 1, then L=R=1 for every chamber of F.

## Body

The chamber set of a permutahedron face is the Cartesian product of the permutation sets of its blocks. If the left and right determining windows meet disjoint sets of blocks, then L depends only on one factor set X and R only on a disjoint factor set Y. Assume some chamber has L=R=1. Choose x_0 in X with L(x_0)=1 and y_0 in Y with R(y_0)=1. If L were not identically one, choose x_1 with L(x_1)=0. The product chamber (x_1,y_0) would have (L,R)=(0,1), a forbidden single-sided witness. Hence L is identically one. The same argument shows R is identically one. Thus a far symmetric double witness can avoid the single-sided branch only by being frozen on both sides throughout the face.

## Direct premises at migration

[
    {
        "premise_id": "local_witness_carriers_have_a_protected_central_band",
        "premise_kind": "toolkit",
        "premise_title": "Local-witness carriers have a protected central band",
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
