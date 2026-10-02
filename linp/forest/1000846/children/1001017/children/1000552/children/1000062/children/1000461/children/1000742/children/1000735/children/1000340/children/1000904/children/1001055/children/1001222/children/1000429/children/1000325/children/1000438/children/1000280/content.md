# Consecutive flat rotation outputs are impossible at every potential level

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Suppose two consecutive host edges g_j,g_{j+1} both occur in the flat ascending branch (3) of the general rotation-output theorem 6205fe95ecf8, relative to occupied blocker cells on P. Then this is impossible.

Equivalently, among all occupied cells whose output has rank exactly p and is nonspecial ascending through its forward joint, those cells form an independent set in the path-cell order.

## Body

If g_j lies in branch (3) of 6205fe95ecf8, then
  phi(g_j)=p
and its unique entrance is the forward joint
  z_j=g_j intersect g_{j+1},
with
  phi(z_j)=p-1.

The other two vertices of g_j are terminals of the rank-p edge. A longest p-edge path ending in g_j through z_j may choose either as physical endpoint, so both have endpoint potential at least p.

If g_{j+1} also lay in branch (3), its unique entrance would be z_{j+1}=g_{j+1} intersect g_{j+2}. Hence its backward joint z_j would be a terminal of the rank-p edge g_{j+1}, forcing
  phi(z_j)>=p.
This contradicts phi(z_j)=p-1.

Thus two consecutive output edges cannot both be flat ascending of rank p.