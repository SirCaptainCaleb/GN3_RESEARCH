# Toolkit migration — A mixed two-vertex middle forces strict quadratic descent

Preserved from the retired Toolkit Limbo object [[toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:19:32.540265+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent",
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

In a minimum counterexample, any spanning three-cover A|(z,w)|C in the mixed two-vertex attachment case admits a single pairwise repartition that strictly decreases the quadratic potential. On a side of order at least five, a Hamiltonian local four-set gives the move t|2 -> (t-2)|4, while a non-Hamiltonian local four-set forces the move t|2 -> (t-1)|3.

## Statement

Let H be a minimum counterexample and let A|(z,w)|C be a spanning three-cover with |A|=r, |C|=s, r,s>=2. Assume the mixed attachment case of toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern: one middle vertex z attaches to both exposed ends and the other vertex w reverses both. Then a single pairwise repartition strictly decreases Phi=sum |P_i|^2.

## Body

Put a=a_{r-1}, b=a_r, c=c_1, d=c_2. Since H is a minimum counterexample, n=|V(H)|>10. Hence r+s=n-2>8, so at least one of r,s is at least five. By symmetry suppose r>=5.

Consider the local four-set L={a,b,z,w} on the union of the components A and (z,w).

If L is Hamiltonian, choose a Hamilton path on L. The inherited prefix A_0=(a_1,...,a_{r-2}) is tight. Therefore A|(z,w) can be pairwise repartitioned as A_0|L, with the empty prefix omitted when necessary. The two affected component orders change from (r,2) to (r-2,4). The potential change is

(r-2)^2+4^2-r^2-2^2 = 16-4r < 0

because r>=5.

Assume L is non-Hamiltonian. The mixed-case inner-reversal lemma supplies the tight triples (a,b,z), (w,b,a), and (w,z,b). By the non-Hamiltonian four-set matching-block classification, the opposite-edge matchings {bw,az}, {ab,wz}, {bz,aw} occur as consecutive blocks. The known inequalities bw<ab<bz force this block order. Hence bw<wz, so (b,w,z) is tight.

Thus A|(z,w) can be pairwise repartitioned as

(a_1,...,a_{r-1}) | (b,w,z).

The affected orders change from (r,2) to (r-1,3), and the potential change is

(r-1)^2+3^2-r^2-2^2 = 6-2r < 0.

Therefore the side of order at least five always yields a strict one-step quadratic descent, regardless of whether its local four-set is Hamiltonian. The argument is symmetric when s>=5. Since one of r,s is at least five, every mixed two-vertex attachment state strictly descends.

## Direct premises at migration

[
    {
        "premise_id": "mincex01",
        "premise_kind": "toolkit",
        "premise_title": "Minimum-counterexample calculus",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": false
    },
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
        "premise_id": "toolkit_a_two_vertex_middle_path_forces_an_endpoint_reversal_pattern",
        "premise_kind": "toolkit",
        "premise_title": "A two-vertex middle path forces an endpoint-reversal pattern",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "toolkit_across_a_two_vertex_middle_forces_the_adjacent_inner_reversal",
        "premise_kind": "toolkit",
        "premise_title": "A one-sided tight join across a two-vertex middle forces the adjacent inner reversal",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "toolkit_minimal_two_vertex_middle_has_a_doubled_same_side_reversal",
        "consumer_kind": "toolkit",
        "consumer_title": "A quadratic-minimal two-vertex middle has a doubled same-side reversal",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[
    {
        "new_id": "toolkit_two_vertex_middle_component_forces_strict_quadratic_descent",
        "old_id": "toolkit_a_mixed_two_vertex_middle_forces_strict_quadratic_descent",
        "reason": "The general 2|s balancing move gives strict descent without attachment analysis.",
        "created_at": "2026-10-03T04:26:22.015476+00:00",
        "session_id": 52
    }
]

## Retained passed-version snapshot at migration

null
