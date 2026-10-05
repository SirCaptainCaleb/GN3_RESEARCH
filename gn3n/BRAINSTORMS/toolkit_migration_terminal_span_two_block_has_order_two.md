# Toolkit migration — A terminal span-two witness block has exactly two vertices

Preserved from the retired Toolkit Limbo object [[terminal_span_two_block_has_order_two]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T23:46:05.517485+00:00",
    "updated_at": "2026-10-04T23:46:39.025008+00:00",
    "archived_at": null,
    "original_id": "terminal_span_two_block_has_order_two",
    "audit_status": "failed",
    "math_version": 1,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": null
}

## Simplified statement

In the terminal disjoint-window span-two branch, the bridging block is necessarily the two-vertex case alpha=beta=1.

## Statement

Assume a terminal single-sided configuration for a nearest span-two witness of type 001/011 or 110/100 with disjoint determining windows. Then alpha=beta=1 and |B|=2.

## Body

By [[terminal_local_block_sharpens_to_four]], alpha,beta<=2 and |B|=alpha+beta. The two five-vertex determining windows are adjacent. Between their witness endpoints lie four central status coordinates. Because the selected witness is nearest among both inversion polarities, these four statuses avoid all six local witnesses. In a left-witness chamber their left endpoint has the inward color of that witness, so all four statuses have that color; in a right-witness chamber all four have the opposite color. Terminality says every chamber has exactly one side witness, hence these four central statuses are monochromatic in every chamber and their common color is the terminal state. An adjacent transposition can change at most four consecutive status coordinates. To change the terminal state it must change all four central coordinates, so only the swap at the unique position between the two determining windows can change the state; every adjacent swap of B at a neighboring position preserves it. If |B|>=3, this central Coxeter generator has a neighboring generator in B. The braid relation s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1} reaches the same chamber by two paths. The first path contains one occurrence of the central state-changing generator and the second contains two, while neighboring generators preserve the state, forcing opposite and equal terminal colors simultaneously. Contradiction. Therefore |B|<3. Both alpha and beta are positive, so alpha=beta=1 and |B|=2.

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
        "premise_id": "terminal_local_block_sharpens_to_four",
        "premise_kind": "toolkit",
        "premise_title": "Terminal local witness blocks have at most four vertices",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "terminal_disjoint_single_sided_witnesses_are_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal disjoint single-sided witness configurations are impossible",
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
