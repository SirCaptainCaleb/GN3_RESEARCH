# Toolkit migration — The 3|5 matching-block residue gives an interior end-edge reversal or a central sandwich

Preserved from the retired Toolkit Limbo object [[toolkit_gives_an_interior_end_edge_reversal_or_a_central_sandwich]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:46:03.011787+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_gives_an_interior_end_edge_reversal_or_a_central_sandwich",
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

In a Phi-minimal 3|5 pair, choose the complementary non-Hamiltonian four-set F={w,c2,c3,c4} supplied by the endpoint-pair support lemma. Then either w reverses one of the two edges of the interior path (c2,c3,c4), or both (c2,c3,w) and (w,c3,c4) are tight.

## Statement

Let H be a minimum counterexample and let T|C be components of a Phi-minimal three-cover with |T|=3 and C=(c_1,...,c_5). Let w in T be chosen so that F={w,c_2,c_3,c_4} is the non-Hamiltonian matching-block four-set given by toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set. Then one of the following holds: (i) (w,c_3,c_2) is tight; (ii) (c_4,c_3,w) is tight; (iii) both (c_2,c_3,w) and (w,c_3,c_4) are tight.

## Body

Because F is a non-Hamiltonian four-set, smallset01 gives an edge order in which the three opposite-edge perfect matchings are consecutive blocks. Write

e_1=c_2c_3,  e_2=c_3c_4.

Since (c_2,c_3,c_4) is tight, e_1<e_2. The opposite-edge matching containing e_1 is

M_1={c_2c_3,wc_4},

and the matching containing e_2 is

M_2={c_3c_4,wc_2}.

Thus the matching blocks satisfy M_1<M_2. The third block is

M_3={c_2c_4,wc_3}.

There are exactly three possible block orders compatible with M_1<M_2.

If M_3<M_1<M_2, then wc_3<c_2c_3, so (w,c_3,c_2) is tight. This reverses the displayed edge (c_2,c_3).

If M_1<M_2<M_3, then c_3c_4<wc_3, so (c_4,c_3,w) is tight. This reverses the displayed edge (c_3,c_4).

If M_1<M_3<M_2, then c_2c_3<wc_3<c_3c_4. Hence both (c_2,c_3,w) and (w,c_3,c_4) are tight.

Therefore every Phi-minimal 3|5 pair yields an explicit interior end-edge reversal unless the unique middle-block sandwich configuration occurs.

## Direct premises at migration

[
    {
        "premise_id": "smallset01",
        "premise_kind": "toolkit",
        "premise_title": "Small-order Hamiltonicity and structure",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    },
    {
        "premise_id": "toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set",
        "premise_kind": "toolkit",
        "premise_title": "A Phi-minimal 3|5 pair forces a complementary matching-block four-set",
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
