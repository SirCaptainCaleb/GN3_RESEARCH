# The entire contact-snake defect reduces to 0-1-1 ascending edges

## Statement

With one maximum endpoint path P_v chosen at every vertex, call an ascending nonspecial edge e={x,y,z} a 0-1-1 edge when x is its unique entrance, mu_x(e)=0, and mu_y(e)=mu_z(e)=1. Let U be the number of such edges. Then 3m<=(2ell-3)n+U for every P_ell-free linear triple system. Consequently U=O(n) would imply ex_L(n,P_ell^(3))<=(2/3)ell n+O(n), while any bound U<=(1-epsilon)m+O(n) with fixed epsilon>0 already improves the leading coefficient below one.

## Body

Use the clean-minus-double identity. Every clean incidence belongs to the unique entrance x of an ascending nonspecial edge e={x,y,z}. Partition the clean edges into two classes.

Paid clean edges: at least one terminal incidence of the same edge is double, i.e. mu_y(e)=2 or mu_z(e)=2.
Unpaid clean edges: both terminal incidences are single, so the contact signature is (0,1,1). Let U be their number.

Choose, for every paid clean edge, one of its double terminal incidences. Different clean edges give different chosen double incidences because the incidence remembers its hyperedge. Hence the paid clean edges inject into the D double incidences. Therefore
  C-D <= U.

The clean-minus-double inequality gives
  3m <= (2ell-3)n + C-D
      <= (2ell-3)n + U.                         (*)

Thus the whole leading-order obstruction to contact-snake counting is the 0-1-1 class.

There is additional structure on every 0-1-1 edge. Write q=phi(e) and p=phi(x)=q-1. Since the entrance incidence is clean, e is ascending. Let r_y=phi(y), r_z=phi(z). Both are at least q. If, say, r_y>=2q-1, then the long-terminal-path capture lemma 16d45ad1b1b2 forces every maximum r_y-edge path ending at y to contain all three vertices of e; in particular the chosen P_y would have mu_y(e)=2, contrary to the 0-1-1 hypothesis. Therefore
  q <= r_y,r_z <= 2q-2,
or equivalently
  p+1 <= phi(y),phi(z) <= 2p.
So every unpaid edge is an ascending two-branch transition from potential p to two strictly larger potentials lying within a factor two.

From (*) the quantitative consequences are immediate. If U<=Kn then
  m <= ((2ell-3+K)/3)n
      = (2/3)ell n+O(n).
More generally, if U<=(1-epsilon)m+Kn, then
  (2+epsilon)m <= (2ell-3+K)n,
giving leading coefficient 2/(2+epsilon)<1.

Thus future generalized-snake work can focus exclusively on bounding the 0-1-1 transition system, rather than all nonspecial or ascending edges.
