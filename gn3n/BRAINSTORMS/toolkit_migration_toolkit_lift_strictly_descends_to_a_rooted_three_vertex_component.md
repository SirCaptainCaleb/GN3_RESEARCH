# Toolkit migration — Every deletion-cover singleton lift strictly descends to a rooted three-vertex component

Preserved from the retired Toolkit Limbo object [[toolkit_lift_strictly_descends_to_a_rooted_three_vertex_component]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T04:31:28.375046+00:00",
    "updated_at": "2026-10-03T14:43:12.126335+00:00",
    "archived_at": "2026-10-03T14:43:12.126335+00:00",
    "original_id": "toolkit_lift_strictly_descends_to_a_rooted_three_vertex_component",
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

Every deletion-cover singleton lift in a minimum counterexample has a one-step strict Phi descent to a three-cover whose new 3-component contains the deleted label and two consecutive endpoint vertices of one deletion-cover path.

## Statement

Let H be a minimum counterexample and H-x=P|Q a deletion cover. Then one of P,Q has order r>=4. If R=(r_1,...,r_r) is such a component, the singleton lift P|Q|{x} admits one pairwise repartition replacing R|{x} by a tight three-vertex path on {x,r_1,r_2} and the inherited tail (r_3,...,r_r). The quadratic potential decreases by 4(r-3).

## Body

Let H be a minimum counterexample and let
H-x=P|Q
be a deletion cover. Its singleton lift is
P|Q|{x}.

First, |V(H)|>=8. For |V(H)|<=6, partition V(H) into two sets of order at most three; every set of order at most three has a Hamilton tight path. For |V(H)|=7, choose any five-set S. If S is Hamiltonian, deleting an endpoint of a Hamilton order leaves a Hamiltonian four-set. If S is non-Hamiltonian, the five-set small-order theorem gives a Hamiltonian four-subset of S. In either case H has a Hamiltonian four-set whose complementary three-set is Hamiltonian, yielding a two-cover. Thus a minimum counterexample has order at least eight.

Since |P|+|Q|=|V(H)|-1>=7, at least one of P,Q has order r>=4. Let
R=(r_1,...,r_r)
be such a path.

By boundary antisymmetry, exactly one of
(x,r_1,r_2)
and
(r_2,r_1,x)
is tight. Let T be the resulting tight path on {x,r_1,r_2}. The inherited tail
R'=(r_3,...,r_r)
is also a nonempty tight path. Hence
R|{x}
may be replaced in one pairwise repartition by
T|R'.

Only the component orders r and 1 change, becoming 3 and r-2. Therefore
Phi_new-Phi_old
=9+(r-2)^2-r^2-1
=12-4r
=-4(r-3)<0.

Thus every deletion-cover singleton lift admits a one-step strict quadratic descent to a three-cover in which the deleted label x lies in a three-vertex component together with two consecutive vertices taken from an endpoint of one displayed deletion-cover path. The terminal pair (r_{r-1},r_r) gives the symmetric construction.

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
    }
]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
