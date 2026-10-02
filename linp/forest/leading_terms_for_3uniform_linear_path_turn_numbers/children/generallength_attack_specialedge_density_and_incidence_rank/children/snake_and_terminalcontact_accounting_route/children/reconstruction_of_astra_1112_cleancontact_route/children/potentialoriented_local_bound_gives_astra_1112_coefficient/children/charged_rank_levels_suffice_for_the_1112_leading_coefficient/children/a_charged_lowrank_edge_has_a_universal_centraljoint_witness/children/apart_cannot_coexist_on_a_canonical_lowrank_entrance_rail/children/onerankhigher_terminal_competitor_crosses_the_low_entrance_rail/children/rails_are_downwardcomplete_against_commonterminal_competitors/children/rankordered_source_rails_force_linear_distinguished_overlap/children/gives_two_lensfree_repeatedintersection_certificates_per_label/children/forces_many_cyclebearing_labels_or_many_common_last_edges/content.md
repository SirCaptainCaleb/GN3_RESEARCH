# A same-type overlap packet forces many cycle-bearing labels or many common last edges

## Statement


Retain f84b001e0a61. Thus there are indices a,b and a set I of size M, together with one fixed type X or U, such that for every i in I a label y_i lies on both maximum source paths R_a,R_b, where
  y_i=x_i in type X,
  y_i=u_i in type U,
and every maximum endpoint path P_i ending at y_i has at least two common vertices with each of R_a,R_b.

Choose one such maximum endpoint path P_i for every i, and let h_i be its last edge. Then for every i in I at least one of the following holds:

(1) P_i union R_a contains a linear cycle;

(2) P_i union R_b contains a linear cycle;

(3) h_i belongs to E(R_a) intersect E(R_b).

If C is the number of indices i for which (1) or (2) holds, then
  |E(R_a) intersect E(R_b)| >= (M-C)/3.

Hence either at least M/2 labels are cycle-bearing with one of the two hosts, or
  |E(R_a) intersect E(R_b)| >= M/6.

In type U, every edge h_i arising from alternative (3) has edge rank at least p. Consequently the second outcome strengthens to: R_a and R_b share at least M/6 distinct hyperedges of edge rank at least p.


## Body


Fix i in I. The vertex y_i is the last vertex of P_i and lies on R_a. By f84b001e0a61, P_i and R_a have at least two common vertices. Apply 41100a9882dd with P=P_i and A=R_a. Either P_i union R_a contains a linear cycle, or the last edge h_i of P_i is an edge of R_a.

Apply the same argument with A=R_b. Hence if neither union contains a linear cycle, then h_i belongs to both R_a and R_b.

The labels y_i are distinct. In type X this follows from linearity of the distinct parent edges e_i through v; in type U it follows for the same reason because the opposite terminals u_i are pairwise distinct. If h_i=h_j for distinct i,j, then the distinct last vertices y_i,y_j both belong to that common 3-edge. Thus a fixed hyperedge can equal h_i for at most three indices. Therefore the M-C non-cycle indices yield at least (M-C)/3 distinct common hyperedges of R_a and R_b. The M/2 versus M/6 dichotomy follows.

Finally suppose the packet is type U. Then y_i=u_i and phi(u_i)>=p by the minimum-terminal hypothesis in f84b001e0a61. Since P_i is a maximum endpoint path of length phi(u_i) ending at u_i with last edge h_i,
  phi(h_i) >= phi(u_i) >= p.
Thus every common edge supplied by a non-cycle U-label has edge rank at least p.
