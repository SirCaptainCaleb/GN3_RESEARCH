# The K4,4 shadow extremal case forces a two-plus-three split on both five-sides

## Statement

In the extremal |E(F)|=16 case of a trapped order-thirteen 3|5|5 Astra-003 plateau, write F=K_{4,4} on sides A,C plus five isolated vertices R. For every reachable state X|P|Q with X a three-subset of A, each of P,Q contains exactly two vertices of C and three vertices of (A-X) union R. Moreover, for every x in X, exchanging x with any vertex of (A-X) union R is a legal 3|5 move, while exchanging x with either C-vertex on the chosen five-side is impossible.

## Body

Assume the extremal shadow-complement case from astra003support148: F is K_{4,4} on disjoint four-sets A,C, with the remaining five vertices R isolated in F.

The proof of astra003support148 shows that every G-triangle not wholly contained in R belongs to D. In particular, every three-subset X of A occurs as the three-side of some state X|P|Q in the trapped 3|5|5 component.

Fix such a state and x in X. No support in D can contain both an A-vertex and a C-vertex, because every A-C pair is an edge of F and therefore is absent from the two-shadow G. Hence for every c in C, the replacement X-x+c is not in D and in particular cannot arise from a legal one-move repartition of X with the five-side containing c.

On the other hand, the Johnson-projection lemma b47ce13d34b3 gives at least six successful replacements y outside X for each fixed x. There are exactly six vertices outside X that are not in C, namely the single vertex of A-X together with the five vertices of R. Since none of the four C-vertices can be successful, all six of these non-C vertices must be successful.

Now consider one five-side, say P. Apply four-of-six to the six-set P union {x}. Since P itself is Hamiltonian, at least three vertices y in P have (P-y) union {x} Hamiltonian, equivalently give successful 3|5 exchanges X-x+y. Every C-vertex of P is unsuccessful, so P must contain at least three vertices outside C. Therefore |P intersection C|<=2. The same argument gives |Q intersection C|<=2. Since P and Q partition the four vertices of C, both inequalities are equalities:

|P intersection C|=|Q intersection C|=2.

Thus each five-side contains exactly three vertices from (A-X) union R.

Finally, the preceding global replacement count already showed that every vertex of (A-X) union R is successful for each x in X. Hence on each side its three non-C vertices are all successful exchanges, whereas its two C-vertices are both unsuccessful.

So every all-A three-side state has the rigid 2C+3nonC split on each five-side, with an exact three-good/two-bad exchange pattern for every deleted coordinate x in X.
