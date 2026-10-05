# Toolkit migration — Terminal span-two blocks of order three or four are impossible

Preserved from the retired Toolkit Limbo object [[terminal_span_two_blocks_three_and_four_are_impossible]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T23:49:33.771224+00:00",
    "updated_at": "2026-10-04T23:51:21.783055+00:00",
    "archived_at": null,
    "original_id": "terminal_span_two_blocks_three_and_four_are_impossible",
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

In the terminal disjoint-window span-two branch, the bridging block cannot have order three or four. Hence the only surviving block size is two.

## Statement

Assume a terminal nearest span-two witness with disjoint determining windows. Under the audited bound alpha,beta<=2 and |B|=alpha+beta, the cases |B|=3 and |B|=4 contradict boundary antisymmetry together with the fact that the four central statuses are monochromatic in every chamber.

## Body

The four status positions between the two reflected span-two witness windows avoid all six nearer local witnesses. Thus in every terminal chamber they are monochromatic; write their common value as the terminal state. For |B|=3, by symmetry take alpha=1,beta=2 and write a block order as (x,y,z). The state depends only on the singleton left support, so write it C(x). The central triples give h(x,y,z)=C(x). Reordering the same support as (x,z,y) gives h(x,z,y)=C(x). Boundary antisymmetry then gives h(y,z,x)=1-C(x). But in the chamber with B-order (y,z,x), the same central triple equals C(y). Hence C(y)=1-C(x) for every distinct x,y. On three vertices this is impossible. For |B|=4, alpha=beta=2. The state depends only on the unordered left support pair; write it C({x,y}). For every block order (x,y,z,w), a central triple gives h(x,y,z)=C({x,y}). Reversal and the order (z,y,x,w) give C({y,z})=1-C({x,y}) for every three distinct x,y,z. Thus every two edges of K4 sharing a vertex would have opposite C-colors. Taking three edges incident with one vertex gives an immediate contradiction. Therefore neither block size three nor four can occur, leaving only alpha=beta=1 and |B|=2.

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
        "consumer_id": "every_terminal_local_witness_support_is_two_coverable",
        "consumer_kind": "toolkit",
        "consumer_title": "Every terminal local-witness support is two-coverable",
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
