# Color-terminal collisions on a rank-monotone terminal path point only backward

## Statement

Let
v_0v_1...v_k
be a simple path in the terminal-pair graph of ascending nonspecial edges. Let
E_i={x_i,v_{i-1},v_i}
be the parent hyperedge of graph edge v_{i-1}v_i, with rank r_i=phi(E_i), and assume
r_1<=r_2<=...<=r_k.

Suppose the graph path is rainbow, and some entrance color x_i equals a nonincident path vertex v_j. Then necessarily
j<=i-2.
Moreover
phi(v_j)=r_i-1,
and every terminal-path edge incident with v_j has rank at most r_i-1.

Thus every obstruction to strong-rainbowness on a nondecreasing-rank rainbow terminal path is a strictly backward color-terminal chord. In particular no entrance color can hit a later nonincident terminal vertex.

## Body

Because E_i is ascending with unique entrance x_i,
phi(x_i)=r_i-1.
If x_i=v_j, this gives phi(v_j)=r_i-1.

Every path edge E_s incident with v_j uses v_j as a terminal, not as its entrance: its entrance is the rainbow color x_s, and properness/linearity prevents x_s from being the incident terminal v_j. Hence
r_s=phi(E_s)<=phi(v_j)=r_i-1.

Assume for contradiction that j>=i+1. Then E_j is a path edge incident with v_j (and if j=k one may instead use E_k). Since the ranks are nondecreasing and j>=i,
r_j>=r_i.
But the preceding terminal bound gives r_j<=r_i-1, a contradiction.

The cases j=i-1 or j=i are incident to E_i and cannot occur because x_i is distinct from both terminals v_{i-1},v_i. Therefore any color-terminal collision satisfies j<=i-2.