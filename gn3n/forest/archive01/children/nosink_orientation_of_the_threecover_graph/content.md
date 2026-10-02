# No-sink orientation of the three-cover graph

## Statement

Orient each legal pairwise repartition move P|Q|R -> P'|Q'|R by a canonical order-independent potential built from component sizes together with endpoint obstruction signatures, with strict priority on merge moves. Conjecture that every three-cover component avoiding a two-cover has no sink under this orientation. Since the state graph is finite, that would force a directed cycle; then show the signature part of the potential strictly changes around any directed cycle, contradiction.

## Body

Why it might matter globally:
Astra-003 already packages the problem as escape from trapped three-cover components. A successful canonical orientation would turn local escape lemmas into a global termination theorem without classifying component sizes or orders.

Plausible first attack:
At a Phi-minimal trapped state, record for each ordered pair of components which endpoints of the larger component fail to enlarge the smaller one Hamiltonianly. Order these six endpoint-failure bits lexicographically after the size potential. Prove that whenever a pairwise repartition preserves Phi, one of these obstruction bits must improve unless the two components are already mergeable.