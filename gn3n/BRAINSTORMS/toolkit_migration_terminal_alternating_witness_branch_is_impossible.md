# Toolkit migration — The terminal alternating-witness branch is impossible

Preserved from the retired Toolkit Limbo object [[terminal_alternating_witness_branch_is_impossible]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T23:42:52.315133+00:00",
    "updated_at": "2026-10-04T23:43:29.251742+00:00",
    "archived_at": null,
    "original_id": "terminal_alternating_witness_branch_is_impossible",
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

A terminal disjoint-window configuration cannot have nearest witness type 0101 or 1010. Hence every surviving terminal local-witness obstruction is of span-two type and has support at most ten vertices.

## Statement

Assume a terminal single-sided disjoint-window configuration for the nearest dual-polarity witness and suppose its type is 0101 or 1010. Then the bridging block has alpha=beta=2 and order four. Protection from the closer span-two witness makes the left occurrence depend only on the first block vertex and the right occurrence only on the last. The identity that exactly one side occurs for every block permutation forces both state functions to be constant, contradicting occurrence of both orientations.

## Body

By [[terminal_local_block_sharpens_to_four]], alpha,beta<=2 and |B|=alpha+beta. Consider type 0101; the complemented case 1010 is identical. In the left six-position determining window write the four statuses s1,s2,s3,s4. The witness is 0101. The span-two witness one step closer to the center tests s2 against s4. Since the selected alternating witness is nearest, every chamber has s2=s4. The first two statuses lie outside B when alpha<=2, so a chamber realizing 0101 forces s1=0 and s2=1 globally on the face, hence s4=1 globally. If alpha=1 then s3 also lies outside B and is fixed; the left witness would therefore be either present in every chamber or absent in every chamber, incompatible with a terminal carrier having both reflected orientations. Thus alpha=2. The left witness is now equivalent to s3=0, and s3 depends only on the first of the two B-vertices in the left suffix. Symmetrically beta=2 and the right witness depends only on the last B-vertex in the right prefix. Therefore B has four vertices. For a chamber whose B-order is (x,y,z,w), write L(x) and R(w) for the two witness indicators. Terminality gives L(x)+R(w)=1 for every distinct x,w. Given any w1,w2, choose x distinct from both; then R(w1)=R(w2). Hence R is constant, and then L is constant. This contradicts that the balanced carrier supplies chambers of both witness orientations. Therefore no terminal alternating-witness configuration exists.

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
        "consumer_id": "terminal_disjoint_single_sided_witnesses_are_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal disjoint single-sided witness configurations are impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_local_witness_support_sharpens_to_ten",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal dual-polarity local-witness support is bounded by ten vertices",
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
