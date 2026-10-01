# PG(3,2) contains a seven-edge linear cycle

## Statement

The Steiner triple system PG(3,2) contains a linear cycle of length 7. Consequently, for every odd q, its coordinatewise additive Z_q blow-up contains a linear cycle of length 7q and therefore a linear path of length 7q-1; since the blow-up has 15q vertices and 35q^2 edges, this construction cannot beat the asymptotic lower-bound coefficient 1/3.

## Body

Represent PG(3,2) on the nonzero vectors of F_2^4, encoded by integers 1,...,15, with blocks {x,y,x+y}. The following seven blocks form a linear cycle in the displayed cyclic order: {1,2,3}, {1,4,5}, {4,8,12}, {6,8,14}, {6,11,13}, {7,10,13}, {3,9,10}. Consecutive blocks, including the last and first, meet in exactly one point (respectively 1,4,8,6,13,10,3), while all nonconsecutive blocks are disjoint. Apply the certified additive cycle-lift lemma 547a87b3a337: an s-edge base linear cycle lifts to an sq-edge linear cycle in the additive Z_q blow-up for odd q. With s=7 this gives C_{7q}, and deleting one edge gives P_{7q-1}. The blow-up has n=15q and m=35q^2, so m/n=7q/3. Its first forbidden path length is at least 7q, hence (m/n)/ell<=1/3. Thus blowing up the exceptional P7-free PG(3,2) does not yield a leading-coefficient improvement in the natural additive model.
