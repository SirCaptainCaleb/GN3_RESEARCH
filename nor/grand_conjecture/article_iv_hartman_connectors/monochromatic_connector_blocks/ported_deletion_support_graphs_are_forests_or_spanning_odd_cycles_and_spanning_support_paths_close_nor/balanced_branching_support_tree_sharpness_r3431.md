# A seven-label branching support tree is realizable by fully ported zero-path deletion covers

## Development

Statement:
Let A have seven labels. There is a family of seven genuinely realizable fully ported two-path deletion covers whose support graph is a branching tree with eight distinct supports, each of cardinality three, and contains no pair of complementary supports. It is realizable in the transitive tournament on A. Therefore support incidence alone cannot force complementary-support gluing, even for honest compatible zero-path witnesses.

Proof:
Take an eight-vertex tree with edges v0v1,v1v2,v2v3,v1v4,v4v5,v5v6,v6v7. It has seven edges, degree(v1)=3, and balanced bipartition classes {v0,v2,v4,v6} and {v1,v3,v5,v7}. Label its edges bijectively by A={1,...,7}. For each vertex v let S(v) be the set of edge labels e for which the minimum tree distance d(v,e) is odd. By the preceding parity-distance theorem, every |S(v)|=3. For every edge e_a=vw, the supports S(v),S(w) both omit a, and for every b≠a exactly one contains b; they partition A\{a}. Distinct v,w give distinct supports: for even distance their symmetric difference is the nonempty path-label set; for odd distance it is the complement of that label set, also nonempty since a branched tree has no path using all seven edges.

Put any transitive tournament orientation on A. For each v, order S(v) increasingly in its tournament order; this is a three-vertex path with all ternary colors zero and its initial and terminal pairs forward. For every a, the two paths on S(v),S(w) supplied by endpoints of e_a are thus bona fide fully ported disjoint zero paths covering A\{a}. The support graph of this chosen family is exactly the prescribed branching tree. By the complement criterion no two support vertices are complementary. Of course the transitive tournament itself has a spanning fully ported zero path and the NOR connector closes: the example only rules out inferring complementary supports from the selected deletion support graph.
