# Strict potential rise can occur above the edge rank at both terminals

## Statement

There is a 13-vertex, 10-edge linear 3-graph containing an ascending nonspecial edge e with edge rank φ(e)=4 and terminal vertex potentials 5 and 6. Hence a strict potential rise φ(u)>φ(v) does not force the lower terminal potential φ(v) to equal φ(e).

## Body

Take the ten triples (3,8,9), (1,6,7), (9,10,12), (0,1,4), (0,5,12), (3,6,12), (2,4,6), (2,7,12), (5,8,10), (4,7,11). Exact induced-path enumeration gives vertex potentials [6,6,5,5,5,6,5,5,5,5,6,5,3]. For e=(9,10,12), one has φ(e)=4, every longest path ending in e enters through vertex 12, and φ(12)=3, so e is ascending with unique entrance 12. Its terminal vertices are 9 and 10 with φ(9)=5 and φ(10)=6. Thus e is a strict-rise edge from terminal potential 5 to 6 although both terminal potentials exceed its edge rank 4. This fences the tempting intermediate claim that strict rise forces φ(e)=min{φ(u),φ(v)}.