# A backward color-terminal collision forces double blocking of the colliding source rail

## Statement

Retain the setting of c9a012c1b82e. Let
v_0v_1...v_k
be a rainbow terminal-pair path with nondecreasing parent ranks r_1<=...<=r_k, and suppose
E_i={x_i,v_{i-1},v_i}
has a color-terminal collision x_i=v_j with j<=i-2.

Let R_i be any canonical source rail of E_i: an (r_i-1)-edge path ending at x_i such that R_i,E_i is a longest r_i-edge path, so R_i avoids the terminals v_{i-1},v_i.

Then E_{j+1} has at least two distinct vertices on R_i. If j>=1, E_j also has at least two distinct vertices on R_i. Moreover the additional R_i-contact vertices supplied by E_j and E_{j+1} are distinct.

Thus every interior backward collision forces the two terminal-path edges adjacent to the hit vertex to be double blockers of the colliding edge's maximum source rail.

## Body

By c9a012c1b82e,
phi(v_j)=r_i-1,
and every terminal-path edge incident with v_j has rank at most r_i-1. In particular
r_{j+1}<=r_i-1,
and, when j>=1,
r_j<=r_i-1.

Consider E_{j+1}. It contains v_j=x_i. Suppose it had no other vertex on R_i. Then, since R_i ends at x_i=v_j,
R_i,E_{j+1}
would be a linear path of length r_i ending in E_{j+1}. This exceeds the edge rank
phi(E_{j+1})=r_{j+1}<=r_i-1,
a contradiction. Hence E_{j+1} has a second R_i-contact.

The same argument applies to E_j when j>=1.

Finally E_j and E_{j+1} are consecutive distinct hyperedges and already intersect in v_j. By linearity they cannot share any second vertex. Therefore their respective additional R_i-contact vertices are distinct.