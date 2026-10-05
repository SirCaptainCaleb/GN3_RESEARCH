# Toolkit migration — Status averages localize at permutahedron face boundaries

Preserved from the retired Toolkit Limbo object [[permutahedron_face_status_localization]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T20:33:57.189495+00:00",
    "updated_at": "2026-10-04T23:33:04.263244+00:00",
    "archived_at": null,
    "original_id": "permutahedron_face_status_localization",
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

For any ordered-partition face of the permutahedron, the average sign status over all compatible spanning orders vanishes at every triple window contained in one block; hence only the two status positions adjacent to each block boundary can have nonzero average.

## Statement

Let H be a boundary 3-tournament and F=B_1|...|B_k a face of the permutahedron, with chamber vertices the spanning orders obtained by permuting vertices inside each block. For a chamber pi let lambda_i(pi)=+1 for a tight triple in positions i,i+1,i+2 and -1 otherwise. If positions i,i+1,i+2 lie in one block of F, then the average of lambda_i over all chambers of F is zero. Consequently the face-average status vector is supported on at most the positions b_j-1,b_j adjacent to the k-1 block boundaries b_j, and therefore on at most 2(k-1) coordinates.

## Body

# Status averages localize at permutahedron face boundaries

Let `H` be a boundary 3-tournament and let

`F=B_1|...|B_k`

be a face of the permutahedron. Its chamber vertices are the spanning orders obtained by arbitrarily ordering the vertices inside each block while preserving the block order. For a chamber `pi`, define the sign status

`lambda_i(pi)=+1`

when the ordered triple in positions `i,i+1,i+2` is tight, and `lambda_i(pi)=-1` otherwise.

Suppose positions `i,i+1,i+2` all lie in the same block of `F`. Pair every chamber `pi` with the chamber obtained by swapping the vertices in positions `i` and `i+2`. This swap stays inside the same block and hence inside `F`. The ordered triple at positions `i,i+1,i+2` is replaced by its boundary flip, so boundary antisymmetry gives

`lambda_i(pi')=-lambda_i(pi)`.

The pairing is fixed-point free. Therefore the average of `lambda_i` over all chamber vertices of `F` is zero.

Let `b_j=|B_1|+...+|B_j|` be the position of the boundary between `B_j` and `B_{j+1}`. A three-position window fails to lie in a single block only if it starts at `b_j-1` or `b_j` for some block boundary. Hence every nonzero coordinate of the face-average status vector lies in

`{b_j-1,b_j : 1<=j<k}`

with indices restricted to the valid status range. In particular the average is supported on at most `2(k-1)` coordinates.

This is a global structural cancellation valid for every boundary tournament. It uses only the ordered-partition description of permutahedron faces and boundary antisymmetry; it has no minimum-counterexample hypothesis.

## Direct premises at migration

[]

## Direct consumers at migration

[
    {
        "consumer_id": "auxiliary_singleton_face_cut_imbalance",
        "consumer_kind": "toolkit",
        "consumer_title": "Auxiliary singleton faces reduce to tournament cut imbalance",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "convex_root_balance_and_bourgin_yang",
        "consumer_kind": "section",
        "consumer_title": "Convex root balance and Bourgin–Yang multiplicity",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 20,
        "consumer_toolkit_limbo": false
    },
    {
        "consumer_id": "disjoint_status_windows_form_boolean_cubes",
        "consumer_kind": "toolkit",
        "consumer_title": "Disjoint internal status windows form Boolean cubes",
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
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
