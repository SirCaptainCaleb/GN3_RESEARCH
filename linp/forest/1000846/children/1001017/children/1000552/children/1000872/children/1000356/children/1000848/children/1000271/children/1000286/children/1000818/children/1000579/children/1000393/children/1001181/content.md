# Reciprocal source-rail contacts force the balanced one-low terminal lens

## Statement

Let e_i={x_i,v,u_i} and e_j={x_j,v,u_j} be source-clean 0-1-1 edges through the same assigned terminal v, with maximum source paths Q_i,Q_j, and suppose each foreign edge meets the other source rail. If Q_i and Q_j have exactly one common vertex, then the cross-contacts are reciprocal-terminal: Q_i meets e_j at u_j and Q_j meets e_i at u_i.

Consequently, in a one-low four-edge source-clean block with low edge e_0 and high edges e_1,e_2,e_3, if each Q_0,Q_i is uniquely intersecting, then u_0 lies on all three high rails and the high rails cannot all be pairwise uniquely intersecting. More precisely, if Q_i,Q_k and Q_j,Q_k are unique, then Q_i and Q_j share u_0 and u_k.

In the minimal residue where Q_1,Q_3 and Q_2,Q_3 are unique and V(Q_1)∩V(Q_2)={u_0,u_3}, the vertices u_0,u_3 are internal on Q_1,Q_2, the two Q_1/Q_2 segments between them form a clean balanced lens, and u_0 occurs at the same joint index on Q_1,Q_2,Q_3.

## Body

For the first assertion, if Q_i met e_j at the entrance x_j, then x_j would lie on both Q_i and Q_j. A unique intersection at x_j is impossible: unique-intersection alignment for equal-length maximum source paths makes the unique common vertex an internal joint of both paths, whereas x_j is the designated last vertex of Q_j in its clean source-path witness. Hence the mandatory foreign contact is u_j, and symmetrically Q_j meets e_i at u_i.

Now take the one-low block. Unique low-high intersections therefore force every high rail Q_i to contain u_0. If Q_i,Q_k and Q_j,Q_k are also unique, reciprocal-terminal rigidity for those high-high pairs forces both Q_i and Q_j to contain u_k. Thus Q_i,Q_j share u_0 and u_k, so the three high rails cannot all be pairwise uniquely intersecting.

In the stated minimal residue, applying this with k=3 gives the two common vertices u_0,u_3 of Q_1,Q_2. Linearity of the four incident edges makes them distinct from the high sources x_1,x_2, so both are internal vertices of Q_1,Q_2. Consecutive common vertices delimit a clean internal lens; the clean-lens balance lemma makes its two sides equal in length. Finally Q_1∩Q_3=Q_2∩Q_3={u_0}; universal aligned-joint rigidity places u_0 at the same joint index on all three high rails.