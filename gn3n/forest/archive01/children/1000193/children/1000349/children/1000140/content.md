# Failed-insertion data on the two deletion paths are locally independent

## Statement

Let P and Q be disjoint tight paths of orders at least four and let x lie outside them. Subject only to the boundary-tournament axioms, the local side-sign patterns witnessing failure of every displayed insertion of x into P and into Q may be prescribed independently on the two paths. In particular, the mere existence of one bounded failed-insertion obstruction window on each of P and Q does not force any relation between the two windows. Any alternating-exchange theorem starting from the deletion singleton must use cross-component triples, global no-two-cover information, or another nonlocal coupling.

## Body

Apply the arbitrary-side-sign failed-insertion construction of 7f28428bc739 separately to P and to Q. The path triples internal to P and Q are disjoint, and every reversal pair used to prescribe insertion failure or side signs on P involves x together with two P-vertices, while the corresponding constraints on Q involve x together with two Q-vertices. These are distinct ordered-triple reversal pairs, so the boundary-tournament axiom imposes no cross-coupling. Complete all remaining reversal pairs arbitrarily. Thus both insertion-failure patterns coexist with arbitrary independent choices.
