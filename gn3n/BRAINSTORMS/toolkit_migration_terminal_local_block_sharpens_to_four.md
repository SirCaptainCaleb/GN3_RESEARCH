# Toolkit migration — Terminal local witness blocks have at most four vertices

Preserved from the retired Toolkit Limbo object [[terminal_local_block_sharpens_to_four]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-04T23:39:38.499905+00:00",
    "updated_at": "2026-10-04T23:43:27.440675+00:00",
    "archived_at": null,
    "original_id": "terminal_local_block_sharpens_to_four",
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

In a disjoint-window terminal local-witness configuration, the bridging block contributes at most two positions to each determining window and therefore has order at most four.

## Statement

Assume a terminal single-sided configuration with disjoint left and right determining windows. Let alpha,beta be the numbers of positions of the bridging face block B in those windows. Then |B|=alpha+beta and alpha,beta<=2; hence |B|<=4.

## Body

By [[terminal_local_block_bound]], |B|<=alpha+beta. A chamber simultaneously fills alpha left-window positions and beta right-window positions with distinct vertices of B, so |B|>=alpha+beta; hence equality. Fix the outside block orders and fix a partition of B into the alpha vertices used on the left and the beta used on the right. Orders of those two sets vary independently. Terminality says exactly one of the two reflected witness states occurs for every pair of orders. Therefore, for this fixed support partition, the left witness indicator is constant over all orders of the alpha-set and the right indicator is constant over all orders of the beta-set. Both values occur for suitable support partitions because the carrier contains both witness orientations. Suppose a support with left witness value one had alpha>=3. Since B crosses the central side of the left determining window, its alpha positions form the inward suffix of that window; the final three positions form one whole consecutive triple whose status is prescribed by the forbidden pattern. Swap the first and third vertices of that triple. This preserves the support partition and all face constraints, but boundary antisymmetry flips that required status, so the same witness cannot remain present. Contradiction. Thus alpha<=2 whenever the left state occurs; applying the same argument to a right-state support gives beta<=2. Since both orientations occur, alpha,beta<=2 globally and |B|<=4.

## Direct premises at migration

[
    {
        "premise_id": "terminal_local_block_bound",
        "premise_kind": "toolkit",
        "premise_title": "Terminal local block bound",
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
        "consumer_id": "terminal_alternating_witness_branch_is_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "The terminal alternating-witness branch is impossible",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_span_two_block_has_order_two",
        "consumer_kind": "toolkit",
        "consumer_title": "A terminal span-two witness block has exactly two vertices",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    },
    {
        "consumer_id": "terminal_span_two_blocks_three_and_four_are_impossible",
        "consumer_kind": "toolkit",
        "consumer_title": "Terminal span-two blocks of order three or four are impossible",
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
