# Opposite-end degree bound fails even existentially

## Statement

The opposite-end degree conjecture 75e5875cac45 is false even in the existential sense. There is a 13-vertex linear 3-graph with global maximum path length L=6 and a globally maximum-rank nonspecial edge e={0,3,8} having exactly one longest path ending at e; the two free vertices at the opposite end of that path both have degree 5, whereas floor(2(L+1)/3)=4.

## Body

Take the 19 triples {(0,1,4),(5,8,9),(0,6,10),(3,4,12),(1,2,10),(4,5,11),(4,6,8),(9,11,12),(1,6,7),(2,3,9),(4,7,10),(0,2,7),(2,5,6),(0,3,8),(0,5,12),(1,3,5),(1,8,12),(3,6,11),(2,8,11)}. Pair-disjointness of the triples gives linearity. The degree sequence on vertices 0,...,12 is (5,5,5,5,5,5,5,3,5,3,3,4,4), so the global minimum degree is 3. Exact exhaustive induced-path enumeration in the intersection graph gives global maximum path length L=6. The edge e={0,3,8} has phi(e)=6 and exactly one longest induced path ending at it: (1,6,7)-(4,7,10)-(4,5,11)-(9,11,12)-(2,3,9)-e. Its penultimate intersection with e is vertex 3, so e is nonspecial with unique entrance 3. The first two edges intersect in 7, hence the two free opposite-end vertices are 1 and 6, and d(1)=d(6)=5>4=floor(14/3). Since this is the only longest path ending at e, there is no alternative longest state with a low-degree opposite endpoint. Thus both the universal and existential opposite-end 2/3 degree formulations fail. The low global minimum degree shows that this still does not refute the dense-core or global 3δ<=2L+2 conjectures.
