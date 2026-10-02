# A repeated longest-path three-window forces a linear synchronized exterior family

## Statement

Let C be a fixed three-consecutive-vertex subpath of a globally longest tight path, and suppose a concentrated witness family supplies h pairwise vertex-disjoint exterior pairs using C, with endpoint pool U of order 2h. Then there exist u in U and a set W subseteq U-{u} of size at least ceil((h-1)/120) such that every five-set C union {u,w}, w in W, is Hamiltonian and, after choosing Hamilton orders, one of the following holds uniformly. (1) There is one fixed Hamiltonian order R of C union {u} and every w in W extends R at the same endpoint. (2) There are fixed distinct a,b in C union {u} such that (a,w,b) is tight for every w in W; consequently every three distinct vertices of W together with a,b induce a Hamiltonian five-set.

## Body

By 644d120d08e0, the Hamiltonicity graph on U, joining u,v when H[C union {u,v}] is Hamiltonian, has average degree at least h-1. Choose u of degree d>=h-1 and put D=C union {u}. Every neighbor v of u gives a Hamiltonian five-set D union {v}. Apply 3031be84eb72 to D and the neighbor set N(u). It supplies a subset W of size at least ceil(d/120)>=ceil((h-1)/120) with either the common-endpoint-extender structure or the common parallel-middle structure. In the latter case, 3031be84eb72 also gives Hamiltonicity of every five-set formed from a,b and three vertices of W.