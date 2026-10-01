# Zero-slack nonspecial witnesses alternate exactly and all colored connectors are special

## Statement

In the zero-slack critical-core model 13500728c22f, every nonspecial witness path contains all c=2k/3 forest triples and therefore alternates exactly between forest triples and DXX connectors. Consequently every nonspecial edge is a forest triple, every DXX edge is special, and every nonspecial edge has rank exactly
q=2c-1=4k/3-1.

## Body

Let F_1,...,F_c be the forest triples. By the universal-core lemma 7de985881169, every edge avoiding D lies in every nonspecial witness path. In zero slack the edges avoiding D are exactly F_1,...,F_c. Thus any longest path P witnessing a nonspecial edge contains every F_i.

Consider any DXX edge h={d,u,v} that lies on P. The two X-vertices u,v belong to unique forest triples, say F_i,F_j. They are distinct because no DXX edge can have both X-endpoints in one F-triple: that would repeat the pair {u,v} already contained in F_i.

Since F_i and F_j also occur as hyperedges of P, linearity of P forces each of them to be consecutive to h. If, say, F_i were not consecutive to h, then h and F_i would be nonconsecutive path edges sharing u, impossible.

Thus every DXX edge on P is an interior path edge flanked precisely by the two forest triples containing its endpoints. In particular:
- no two DXX edges are consecutive;
- no DXX edge can be the first or last edge of P;
- between every two consecutive forest triples in P there is exactly one DXX connector.

Since P contains all c forest triples, it therefore has the form
F_{i_1},C_1,F_{i_2},C_2,...,C_{c-1},F_{i_c}
and has exactly
2c-1=4k/3-1
edges.

Its last edge is a forest triple. Hence a DXX edge cannot be nonspecial: if it were, its longest witness path would, by the same universal-core argument, contain all forest triples and therefore would have to end in a forest triple, contradiction.

Therefore every DXX edge is special, every possible nonspecial edge lies in the forest matching, and every such nonspecial edge has the forced rank q=2c-1.