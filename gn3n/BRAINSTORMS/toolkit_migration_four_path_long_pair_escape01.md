# Toolkit migration — A four-path beside a path of order at least six descends, disagrees, or makes the unique neutral migration

Preserved from the retired Toolkit Limbo object [[four_path_long_pair_escape01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T19:07:23.439641+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "four_path_long_pair_escape01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

A four-path beside a path of order at least six descends, disagrees, or makes the unique neutral migration.

## Statement

Let H be a boundary tournament, let X be a tight path on four vertices, and let P=(p_1,...,p_m) be a vertex-disjoint tight path of order m>=6. Regard X|P as a two-path cover of its union. Then at least one of the following holds: (1) V(X) union V(P) has a two-path cover with strictly smaller quadratic potential than 4^2+m^2; (2) with U=V(X) union {p_1,p_m}, the six-set H[U] is non-Hamiltonian and Hamilton paths on two distinct deletions U-{x}, x in V(X), have order disagreement; (3) m=6, H[U] is Hamiltonian, and U | (p_2,p_3,p_4,p_5) is a Phi-neutral 6|4 repartition of X|P. Thus outcome (3) is the only non-descending, non-disagreement possibility.

## Body

If H[V(X) union {p_1}] or H[V(X) union {p_m}] is Hamiltonian, move that endpoint from P into X and leave the inherited path on the other m-1 vertices of P. This changes the pair sizes from (4,m) to (5,m-1), with new Phi minus old Phi equal to 10-2m<0 for m>=6, giving outcome (1). Assume both endpoint five-sets are non-Hamiltonian. Apply the four-of-six theorem in smallset01 to U=V(X) union {p_1,p_m}. The deletions U-{p_1}=V(X) union {p_m} and U-{p_m}=V(X) union {p_1} are non-Hamiltonian, so all four deletions U-{x}, x in V(X), are Hamiltonian. If H[U] is non-Hamiltonian, astra004fourgooddisagree gives order disagreement between Hamilton paths on two of these deletions, giving (2). If H[U] is Hamiltonian, put M=(p_2,...,p_{m-1}); then U|M is a legal two-path cover of V(X) union V(P). Its potential change is 6^2+(m-2)^2-[4^2+m^2]=24-4m. This is strictly negative for m>=7, giving (1), and is zero exactly when m=6, giving (3).

## Direct premises at migration

[]

## Direct consumers at migration

[
    {
        "consumer_id": "phi_minimum_with_four_support_is_small_or_disagrees01",
        "consumer_kind": "toolkit",
        "consumer_title": "A quadratic minimum containing a four-support is small or has an order disagreement",
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
