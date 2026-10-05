# Toolkit migration — The unresolved four-side endpoint lock is a four-label second-type gap network

Preserved from the retired Toolkit Limbo object [[four_side_endpoint_lock_gap_network01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T22:00:41.068558+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "four_side_endpoint_lock_gap_network01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put M=(p_2,...,p_{m-1}). Then at least one of the following holds: (1) there is a legal pairwise repartition of X|P with component orders (5,m-1) and quadratic-potential change 10-2m<=0; (2) H contains a proper Hamiltonian induced set of order four or five meeting both X and V(M), with non-Hamiltonian path-cover-two complement; (3) m>=7 and each x in X has a second-type failed-insertion obstruction at a distinct displayed gap g(x) of M. In outcome (3), for every distinct x,y in X, if |g(x)-g(y)|=1 then the explicit adjacent-gap cross triple supplied by 36fccff06d48 is tight, while if |g(x)-g(y)|>=2 then x and y are joined by the tight interval path through the displayed subinterval of M between their obstruction gaps. Thus the sole unresolved branch is a complete four-label gap network, not a single connector.

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put M=(p_2,...,p_{m-1}). Then at least one of the following holds: (1) there is a legal pairwise repartition of X|P with component orders (5,m-1) and quadratic-potential change 10-2m<=0; (2) H contains a proper Hamiltonian induced set of order four or five meeting both X and V(M), with non-Hamiltonian path-cover-two complement; (3) m>=7 and each x in X has a second-type failed-insertion obstruction at a distinct displayed gap g(x) of M. In outcome (3), for every distinct x,y in X, if |g(x)-g(y)|=1 then the explicit adjacent-gap cross triple supplied by 36fccff06d48 is tight, while if |g(x)-g(y)|>=2 then x and y are joined by the tight interval path through the displayed subinterval of M between their obstruction gaps. Thus the sole unresolved branch is a complete four-label gap network, not a single connector.

## Body

Apply four_side_endpoint_lock_mixed_menu_m5_01. If its first or second outcome occurs we are done. Otherwise every vertex of X is noninsertable into the displayed interior path M, and assume no mixed Hamiltonian four/five-support exists. Apply insert01 to each x in X. A first-type obstruction would, by 0425e03e2aa3 exactly as in the predecessor proof, give either a mixed Hamiltonian four-set or a cyclic non-Hamiltonian four-set whose extension by another X-label is a mixed Hamiltonian five-set. Hence every x has a second-type obstruction at some displayed gap g(x). If two labels x,y had the same gap, the equal-gap case of 36fccff06d48 would give a mixed Hamiltonian four-set, contradiction. Thus the four gaps are distinct, so M has at least five vertices and m=|M|+2>=7. Now fix x!=y. If their gaps differ by at least two, the separated-gap case of 36fccff06d48 gives the stated tight interval connector. If their gaps are adjacent, that theorem gives either a mixed Hamiltonian five-set on x,y and three consecutive vertices of M, contradicting the absence of outcome (2), or its explicit adjacent-gap cross triple. Therefore the cross triple must occur. This proves the complete pairwise network.

## Direct premises at migration

[]

## Direct consumers at migration

[
    {
        "consumer_id": "four_side_gap_network_disturbance01",
        "consumer_kind": "toolkit",
        "consumer_title": "Four-label gap networks force a mixed four-set, an outer-edge reversal, or a spaced middle configuration",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 3,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[
    {
        "new_id": "mixed_two_by_three_hamiltonian_four01",
        "old_id": "four_side_endpoint_lock_gap_network01",
        "reason": "The supposed hard four-side gap-network branch assumes the absence of a mixed Hamiltonian four/five-support. Choosing any two four-side vertices and any three interior-path vertices already forces a mixed Hamiltonian four-set, so that branch is impossible.",
        "created_at": "2026-10-03T04:05:43.438094+00:00",
        "session_id": 48
    }
]

## Retained passed-version snapshot at migration

null
