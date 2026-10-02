# The reciprocal terminal-exchange residue of an odd tight U_11 collision is impossible

## Statement

Retain the odd tight U_11 color-terminal collision of ac73dd583c10:
  r_i=2m+1,
  r_j=m+1,
  r_{j+1}=m+2.
Let
  A=R_j=(a_1,...,a_m)
and
  B=R_{j+1}=(b_1,...,b_{m+1})
be the chosen maximum source paths.

Then alternative (3) of ac73dd583c10 cannot occur.

Consequently every odd tight collision has at least one of the following additional structures beyond its forced central linear 3-cycle:
(1) the maximum m-edge prefix Q=(g_1,...,g_m) of the colliding source path and R_j contain a linear cycle;
(2) R_j and R_{j+1} have at least two common vertices.

## Body

Assume alternative (3) of ac73dd583c10. Thus A and B have exactly one common vertex z, an aligned internal joint at the same index k, and
  E_{j+1} intersect V(A)={v_{j+1}},
  E_j intersect V(B)={v_{j-1}}.
Also, by 9b00516e2965 and ac73dd583c10, the last edge a_m is the middle host edge g_m of the original colliding source path, and
  v_{j+1} belongs to a_m.

Because B is the chosen source path of E_{j+1}, it avoids the terminal v_{j+1}. Hence z!=v_{j+1}. Since v_{j+1} lies on the last edge a_m, it lies strictly on the suffix side of z in A. By 080bb595a7d0 the other reciprocal terminal v_{j-1} also lies on the suffix side of z in B.

We first show k=m-1. Suppose k<=m-2. The sequence
  a_1,...,a_k,
  b_{k+1},...,b_{m+1},
  E_{j+1},
  a_m
is a linear path. The first two blocks meet only at z because A and B have unique intersection z. The edge E_{j+1} meets B only at its unique entrance x_{j+1}, the last vertex of B, and meets A only at v_{j+1}, which lies in a_m. Its third vertex x_i is absent from both source paths. Finally a_m is disjoint from the A-prefix and from the displayed B-block because k<=m-2 and z is the unique A-B intersection. The displayed path has
  k+(m+1-k)+1+1=m+3
edges and ends at x_j, contradicting
  phi(x_j)=m.
Therefore k=m-1.

Now z=a_{m-1} intersect a_m=b_{m-1} intersect b_m. Since v_{j-1} lies on the suffix side of z in B, it belongs to b_m or b_{m+1}. It cannot belong to b_{m+1}. Otherwise
  b_1,...,b_{m-1},a_m,E_j,b_{m+1}
is a linear path of length m+2 ending at x_{j+1}, contradicting phi(x_{j+1})=m+1. Thus v_{j-1} lies on b_m. It is not z, and it cannot be the joint b_m intersect b_{m+1}, because then it would also belong to b_{m+1}. Hence v_{j-1} is the private vertex of b_m.

Finally consider
  a_1,...,a_{m-1},b_m,E_j,E_{j+1}.
The A-prefix meets b_m only at z. The edge E_j meets b_m exactly at v_{j-1} and is disjoint from the A-prefix, while E_{j+1} is disjoint from both the A-prefix and b_m and meets E_j exactly at the common terminal x_i. Therefore this is a linear path of length
  (m-1)+1+1+1=m+2
ending in E_{j+1} through the terminal x_i.

But phi(E_{j+1})=m+2 and E_{j+1} is nonspecial with unique entrance x_{j+1}. We have produced a longest E_{j+1}-ending path entering through the wrong vertex x_i, a contradiction.

Hence alternative (3) is impossible, leaving only alternatives (1) and (2) of ac73dd583c10.