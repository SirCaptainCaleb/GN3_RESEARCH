# Clean-retained switchers satisfy four-fifths cell packing

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v with last vertex v. Let X be a family of ascending nonspecial edges e={x,v,u}, e!=g_p, such that each edge has exactly one off-v contact with P and that contact is its unique entrance x.

For R<p let X_{\\le R}={e in X: phi(e)<=R}. Then, whenever X_{\\le R} is nonempty,
  |X_{\\le R}| <= (4/5)(2R-p-1)+7/5.
In particular, if the ranks of X are ordered
  rho_1<=...<=rho_a,
then
  rho_i >= ceil((4p+5i-3)/8)
for every i.

Consequently, writing x_i for the entrance of the edge of rank rho_i,
  sum_{i=1}^a phi(x_i)
  >= (p/2)a + (5a^2-17a)/16.

Applied to the clean-retained part X_v of a low-defect switching family at a p-center, if the terminal-retained part U_v has size o(p), then a=(5/8-o(1))p and
  sum_{f in X_v} phi(x_f) >= (445/1024-o(1))p^2.

## Body

Fix R<p. By the central-window localization 49080cbf1371, every member of X_{\le R} has its entrance in the common central window. Write
  J_k=g_k intersect g_{k+1}
for joint slots and
  P_k=private(g_k)
for private slots. The eligible joint indices are
  p-R+1 <= k <= R-1,
so there are
  N=2R-p-1
eligible joint cells. Eligible private indices are the same interval with its first index removed.

For each eligible index k let j_k in {0,1} record occupancy of J_k by an X-edge and let p_k in {0,1} record occupancy of P_k. Linearity makes each slot carry at most one edge. Put o_k=1 when p_k+j_k>0.

Two splice exclusions give the only constraints needed.

First, eac2e3da3eea says that if j_k=1, then the immediately preceding first-contact cell is empty:
  j_k=1 => o_{k-1}=0.                                    (1)

Second, 08f894b8cb5e says that a clean private entrance two positions later forbids the earlier private slot:
  p_k=1 => p_{k-2}=0.                                    (2)

We now prove the purely one-dimensional packing bound. Scan the eligible cells from left to right. Before processing a cell, retain the state
  (p_{k-1},p_{k-2},o_{k-1}).
Under (1)-(2), only the following five states are reachable:
  A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,1), E=(1,1,1).
Give them potentials
  psi(A)=0,
  psi(B)=-4/5,
  psi(C)=-3/5,
  psi(D)=-6/5,
  psi(E)=-7/5.

For every allowed transition, if w=p_k+j_k is the number of occupied slots in the new cell, direct inspection gives
  w <= 4/5 + psi(old)-psi(new).                          (3)
For completeness, the allowed transitions, written as old --(p_k,j_k;w)--> new, are:
  A--(0,0;0)-->A,
  A--(0,1;1)-->B,
  A--(1,0;1)-->D,
  A--(1,1;2)-->D,
  B--(0,0;0)-->A,
  B--(1,0;1)-->D,
  C--(0,0;0)-->A,
  C--(0,1;1)-->B,
  D--(0,0;0)-->C,
  D--(1,0;1)-->E,
  E--(0,0;0)-->C.
Substitution of the five displayed potentials verifies (3) in each case.

Summing (3) over the N eligible cells telescopes. Since the range of psi has width 7/5,
  |X_{\le R}| <= 4N/5+7/5
               = (4/5)(2R-p-1)+7/5.                    (4)

Now order the X-ranks rho_1<=...<=rho_a and set R=rho_i. Then i<=|X_{\le rho_i}|, so (4) gives
  5i <= 8rho_i-4p+3,
hence
  rho_i >= ceil((4p+5i-3)/8).                           (5)

Because each X-edge is ascending, its entrance has potential rho_i-1. Dropping only the ceiling gain in (5),
  sum_i phi(x_i)
  >= sum_{i=1}^a (4p+5i-11)/8
  = (p/2)a + (5a^2-17a)/16.                            (6)

Finally, for a low-defect switching family b032348c1a8a gives total switching size (5/8-o(1))p. If |U_v|=o(p), then a=|X_v|=(5/8-o(1))p. Substituting in (6),
  (p/2)(5p/8) + (5/16)(25p^2/64) - o(p^2)
  = (5/16+125/1024-o(1))p^2
  = (445/1024-o(1))p^2.
