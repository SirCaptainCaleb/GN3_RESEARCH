# Terminal potentials of an ascending edge are at most three times its rank

## Statement

Let e={x,u,v} be an ascending nonspecial edge of a finite linear 3-graph, with unique entrance x and rank q=φ(e). Then φ(u),φ(v)<=3q-3. Equivalently q>=ceil((max{φ(u),φ(v)}+3)/3). In particular, for a potential-oriented charged edge at v, q>=ceil((φ(v)+3)/3).

## Body

Fix a terminal v of e and put p=φ(v). If p<=2q-2, then p<=3q-3 immediately. Assume p>=2q-1 and choose a p-edge path P ending at v. By 16d45ad1b1b2, the other terminal u occurs among the final q-2 precursor edges of P. Hence there is a prefix R of P ending at u with length r>=p-q+1. The same lemma says that x occurs within the final q-1 edges of R. Along a linear path, if a vertex occurs among the final q-1 edges of an r-edge path, then some prefix ending at that vertex has length at least r-q+1: if the occurrence is a joint of two consecutive edges, end at the earlier of those two. Thus φ(x)>=r-q+1>=p-2q+2. Since e is ascending, φ(x)=q-1. Therefore q-1>=p-2q+2, i.e. p<=3q-3. The argument is symmetric for the other terminal u.
