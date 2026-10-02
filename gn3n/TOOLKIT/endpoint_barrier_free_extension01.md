# Endpoint-barrier layers can be freely extended without changing the initial five-window

**Summary:** Endpoint-barrier layers can be freely extended without changing the initial five-window.

## Statement

Let B be any boundary tournament on distinct vertices q_0,q_1,q_2,z,z' such that (q_0,q_1,q_2) is tight and, for each r in {z,z'}, both (q_1,q_0,r) and (q_2,q_1,r) are tight. Then for every m>=7, B extends to a boundary tournament on q_0,...,q_{m-1},z,z' in which Q=(q_0,...,q_{m-1}) is a tight path and, for each r in {z,z'}, all three left endpoint-barrier triples (q_{i+1},q_i,r), i=0,1,2, and all three right endpoint-barrier triples (r,q_{i+1},q_i), i=m-4,m-3,m-2, are tight. In particular the six common endpoint-barrier layers impose no further restriction on the induced initial five-set {q_0,q_1,q_2,z,z'} beyond the two left barriers already present there.

## Body

Adjoin fresh vertices q_3,...,q_{m-1}. Preserve every reversal-pair choice of B. Prescribe the remaining consecutive triples needed for Q to be tight, namely (q_i,q_{i+1},q_{i+2}) for 1<=i<=m-3; the i=0 triple is already tight in B. For each r in {z,z'}, prescribe the third left barrier (q_3,q_2,r) tight and the three right barriers (r,q_{i+1},q_i) for i=m-4,m-3,m-2 tight. The first two left barriers are already present in B by hypothesis.

Because m>=7, the right-barrier indices begin at i>=3, so every right-barrier triple contains a fresh q-vertex and none is a triple entirely inside B. The third left barrier also contains q_3. The consecutive-Q triples and all new barrier triples occupy distinct reversal pairs: a consecutive Q-triple has three q-labels, a barrier triple has one exterior root; among barrier prescriptions the left and right index ranges are disjoint, and the two roots z,z' give different vertex triples. Hence no prescribed tight triple is the reverse of another prescribed tight triple. Complete every still-unassigned reversal pair arbitrarily. The result is a boundary tournament extending B with the asserted tight path and barriers. Since B is unchanged, any Hamiltonian or non-Hamiltonian property of the initial five-set is unchanged as well.

## Metadata

- ID: endpoint_barrier_free_extension01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
