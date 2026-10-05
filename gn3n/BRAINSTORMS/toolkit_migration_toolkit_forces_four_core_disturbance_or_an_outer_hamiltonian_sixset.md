# Toolkit migration — The root-exchange split forces four-core disturbance or an outer Hamiltonian six-set

Preserved from the retired Toolkit Limbo object [[toolkit_forces_four_core_disturbance_or_an_outer_hamiltonian_sixset]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:45:45.587939+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_forces_four_core_disturbance_or_an_outer_hamiltonian_sixset",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        51
    ],
    "audited_math_version": null
}

## Simplified statement

A rooted five-side's exceptional root-exchange pattern immediately yields four-core order disturbance, a Hamiltonian four-set, a positioned core reversal, or a Hamiltonian six-set on the two non-root extenders.

## Statement

Let C be a four-set and x,a,b distinct exterior vertices. Suppose C∪{x}, C∪{a}, C∪{b} are Hamiltonian while C∪{x,a} and C∪{x,b} are non-Hamiltonian. Then at least one of the following holds: two chosen Hamilton orders on the three five-sets disagree on the relative order of C; there is a Hamiltonian four-set inside C∪{x,a,b}; a tight triple through one vertex of C reverses a displayed core edge between two extenders; or C∪{a,b} is Hamiltonian.

## Body

Let C be a four-vertex set and let x,a,b be distinct vertices outside C. Assume
C union {x},
C union {a},
C union {b}
are Hamiltonian, while
C union {x,a}
and
C union {x,b}
are non-Hamiltonian.

Choose Hamilton paths P_x,P_a,P_b on the three Hamiltonian five-sets. Apply the blocked four-core extension-star theorem with center r_0=x and leaves r_1=a,r_2=b. Its center-leaf non-Hamiltonicity hypotheses are exactly the two displayed assumptions.

The theorem gives at least one of four outcomes:

1. two of P_x,P_a,P_b have a relative-order disagreement on C;
2. there is a Hamiltonian four-set contained in C union {x,a,b};
3. for two extenders among x,a,b and some c in C, a tight triple through c reverses a displayed core edge of one of the chosen five-paths;
4. the outer-pair six-set C union {a,b} is Hamiltonian.

In particular, apply this to the exceptional branch of the rooted-five endpoint refinement. There X is a Hamiltonian five-set with root x, C=X-{x}, and a,b are the two exterior endpoints. Failure of a root-preserving common removable label forces x to be the unique common removable label, so both C union {a} and C union {b} are Hamiltonian; the original X=C union {x} is Hamiltonian, while the bad endpoint-extension hypothesis gives non-Hamiltonicity of C union {x,a}=X union {a} and C union {x,b}=X union {b}. Hence the exceptional root-loss branch always yields one of the four outcomes above.

## Direct premises at migration

[
    {
        "premise_id": "blocked_fourcore_star_outer_sixset01",
        "premise_kind": "toolkit",
        "premise_title": "A blocked center in a four-core extension star forces a complete outer-pair six-set or positioned disturbance",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    },
    {
        "premise_id": "toolkit_common_endpoint_core_or_a_two_pair_root_exchange_split",
        "premise_kind": "toolkit",
        "premise_title": "A rooted five-side has a root-preserving common endpoint core or a two-pair root-exchange split",
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
