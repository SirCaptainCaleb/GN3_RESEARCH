# Toolkit migration — A Phi-minimal 3|5 pair forces a complementary matching-block four-set

Preserved from the retired Toolkit Limbo object [[toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:44:43.605516+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        52
    ],
    "audited_math_version": null
}

## Simplified statement

If a Phi-minimal three-cover contains a 3-path T beside a 5-path C=(c1,...,c5), then some Hamiltonian four-set contains both endpoints c1,c5 and two vertices of T, while the complementary four-set consisting of the remaining T-vertex and c2,c3,c4 is non-Hamiltonian and hence a matching-block K4.

## Statement

Let H be a minimum counterexample and let a Phi-minimal spanning three-cover contain components T|C with |T|=3 and C=(c_1,c_2,c_3,c_4,c_5). Then there exists a two-set E subset V(T) such that S={c_1,c_5} union E is Hamiltonian. If w is the unique vertex of T-E, then F={w,c_2,c_3,c_4} is non-Hamiltonian. Therefore F is edge-orderable and its three opposite-edge perfect matchings occur as three consecutive blocks.

## Body

Apply prescribed_pair_mixed_four_supports01 with the prescribed pair {c_1,c_5} and the exterior three-set V(T). It gives a two-set E subset V(T) such that

S={c_1,c_5} union E

is Hamiltonian. Let w be the remaining vertex of T, and put

F={w,c_2,c_3,c_4}.

The sets S and F are complementary inside V(T) union V(C). If F were Hamiltonian, then S|F would be a two-cover of that union with component orders (4,4). Replacing the displayed pair T|C would therefore be a legal pairwise repartition

(3,5) -> (4,4).

Its quadratic-potential change is

4^2+4^2-3^2-5^2 = 32-34 = -2,

contradicting Phi-minimality. Hence F is non-Hamiltonian.

By smallset01, every non-Hamiltonian four-set is edge-orderable and its six ordinary edges occur in three consecutive opposite-edge matching blocks. Thus every Phi-minimal 3|5 pair carries a canonical local matching-block obstruction on one remaining 3-core vertex together with the three interior vertices of the displayed 5-path.

## Direct premises at migration

[
    {
        "premise_id": "prescribed_pair_mixed_four_supports01",
        "premise_kind": "toolkit",
        "premise_title": "Prescribed-pair mixed four-supports exist in every exterior three-set",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "smallset01",
        "premise_kind": "toolkit",
        "premise_title": "Small-order Hamiltonicity and structure",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "toolkit_gives_an_interior_end_edge_reversal_or_a_central_sandwich",
        "consumer_kind": "toolkit",
        "consumer_title": "The 3|5 matching-block residue gives an interior end-edge reversal or a central sandwich",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "toolkit_minimal_335_state_forces_a_cross_side_hamiltonian_five_support",
        "consumer_kind": "toolkit",
        "consumer_title": "A Phi-minimal 3|3|5 state forces a cross-side Hamiltonian five-support",
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
