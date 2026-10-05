# Toolkit migration — Every four-side beside a nontrivial path has an endpoint-rooted Hamiltonian four-set

Preserved from the retired Toolkit Limbo object [[four_side_endpoint_lock_mixed_menu_m5_01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 4,
    "created_at": "2026-09-29T21:58:17.17584+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "four_side_endpoint_lock_mixed_menu_m5_01",
    "audit_status": "unaudited",
    "math_version": 3,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        48
    ],
    "audited_math_version": null
}

## Simplified statement

A four-side W beside any path P of order at least two forces a Hamiltonian four-set containing both displayed endpoints of P and two vertices of W; in a minimum counterexample its complement has path-cover number two.

## Statement

Let H be a minimum counterexample and let W|P|Q be a spanning three-cover with |W|=4 and P=(p_1,...,p_m), m>=2. Then there are distinct x,y in W such that {p_1,p_m,x,y} is Hamiltonian. This four-set is proper, and its complement is non-Hamiltonian with path-cover number two.

## Body

Choose any three distinct vertices \(a,b,c\in W\), and consider the five-set
\[
F=\{p_1,p_m,a,b,c\}.
\]
Apply the endpoint-pair Hamiltonicity theorem to the prescribed pair
\[
\{p_1,p_m\}\subset F.
\]
It yields a Hamiltonian four-subset of \(F\) containing both prescribed endpoints. Such a four-subset has the form
\[
U=\{p_1,p_m,x,y\}
\]
for distinct \(x,y\in\{a,b,c\}\subset W\).

Because \(Q\ne\varnothing\), the set \(U\) is a proper subset of \(V(H)\). The minimum-counterexample complement principle therefore gives
\[
\operatorname{pc}(H-U)=2,
\]
and \(H-U\) is non-Hamiltonian.

Thus every four-side beside a nontrivial displayed path already carries a Hamiltonian four-set containing both endpoints of that path. No endpoint-extension test, insertion obstruction, path-length threshold, or gap analysis is required.

## Direct premises at migration

[
    {
        "premise_id": "independence_number_at_most_two_in_every_boundary_tournament",
        "premise_kind": "toolkit",
        "premise_title": "Endpoint-pair Hamiltonicity graphs have independence number at most two in every boundary tournament",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 3,
        "premise_toolkit_limbo": false
    },
    {
        "premise_id": "mincex01",
        "premise_kind": "toolkit",
        "premise_title": "Minimum-counterexample calculus",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 3,
        "premise_toolkit_limbo": false
    }
]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
