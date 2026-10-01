# The zero-slack contracted triple graph has a Hamilton path

## Statement

In the zero-slack critical-core model 13500728c22f, contract each forest triple F_i to one node and join two nodes in a simple graph R whenever at least one DXX connector joins their triples. Then every node of R has degree at least c/2, where c=2k/3 is the number of forest triples. Consequently R always has a Hamilton path. If c>=3, then R has a Hamilton cycle by Dirac's theorem.

## Body

Fix a forest triple F_i. In the DXX graph G, each of its three vertices has degree k, and no G-edge lies inside F_i because such an edge together with F_i would repeat the pair of its two X-endpoints in two hyperedges. Hence exactly 3k G-edge incidences leave F_i.\n\nFor any other forest triple F_j, there are only 3*3=9 possible simple graph edges of G between F_i and F_j. Therefore at least\nceil(3k/9)=ceil(k/3)\ndistinct other forest triples receive a connector from F_i.\n\nSince zero slack gives c=2k/3 and in particular k is divisible by 3, this lower bound is exactly\nk/3=c/2.\nThus delta(R)>=c/2.\n\nIf c=2, then delta(R)>=1, so R=K_2 and hence R has a Hamilton path. If c>=3, Dirac's theorem gives a Hamilton cycle in R; deleting one cycle edge yields a Hamilton path.