# Crossing equal-length source-path exchanges have constant rank-position slack unless two source paths meet twice

## Statement

Let R be a maximum endpoint path. For i=1,...,m let e_i={x_i,v,u_i} be distinct ascending nonspecial edges terminal at the common vertex v, with edge ranks r_i. Let S_i be canonical maximum source paths for e_i ending at x_i.

For each i suppose there is a common vertex z_i of R and S_i such that the R-segment I_i=R[z_i,x_i] and the S_i-segment S_i[z_i,x_i] are distinct, internally vertex-disjoint, and have equal edge length. Suppose the intervals I_i are pairwise crossing on R. For every pair i!=j assume that, when S_i and S_j have exactly one common vertex, the pair satisfies the crossing-exchange hypotheses of 20606dbd4cd9. Let kappa_R(x_i) be the host-prefix coordinate of the chosen occurrence of x_i.

Then either some pair S_i,S_j has at least two common vertices, or the quantities
  phi(x_i)-kappa_R(x_i)
are all equal.

Consequently, if all r_i lie in an integer interval [Q-D,Q] and the coordinates kappa_R(x_i) are pairwise distinct, then either m<=D+1 or some pair S_i,S_j has at least two common vertices.

The coordinate-injectivity hypothesis in the counting consequence is essential; distinct host vertices alone do not imply distinct prefix-edge coordinates in a 3-uniform linear path.

## Body

Canonical source paths of common-terminal ascending edges are pairwise intersecting by 0c885137ea8c. Assume no pair S_i,S_j has at least two common vertices. Then every pair has exactly one common vertex.

By hypothesis, each such pair satisfies the crossing-exchange assumptions of 20606dbd4cd9. Therefore for every i!=j,
  phi(x_i)-kappa_R(x_i)=phi(x_j)-kappa_R(x_j).
Hence all rank-position slacks have one common value.

For the counting consequence, assume in addition that r_i∈[Q-D,Q] and that the coordinates kappa_R(x_i) are pairwise distinct. Since e_i is ascending,
  phi(x_i)=r_i-1∈[Q-D-1,Q-1],
which contains D+1 integer values. Common slack gives
  phi(x_i)=kappa_R(x_i)+sigma.
Distinct kappa_R(x_i) therefore imply distinct phi(x_i), so m<=D+1.

The former proof incorrectly inferred coordinate injectivity from distinctness of the host vertices. No component-size assertion from 85d576d60e7e is used.
