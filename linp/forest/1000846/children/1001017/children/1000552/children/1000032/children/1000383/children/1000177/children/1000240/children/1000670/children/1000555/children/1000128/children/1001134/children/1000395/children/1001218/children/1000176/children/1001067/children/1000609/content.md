# Forward common-anchor chords pay quadratic deficit or source-rail reintersection

## Statement

Let h be an ascending nonspecial anchor of rank q terminal at v, and let
  Q=(g_1,...,g_{q-1},h)
be a longest q-edge h-path ending at v. Put
  R=(g_1,...,g_{q-1}),
and let y be the endpoint of R adjacent to the anchor entrance side, so phi(y)=q-1 and R ends at y.

Let F be a family of distinct ascending nonspecial edges
  e={x_e,v,u_e}
terminal at v, each of rank r_e<=q, such that both x_e,u_e lie on R and x_e occurs before u_e in the orientation of R toward y. For each e choose a clean maximum source path S_e ending at x_e.

Call e simple-forward if S_e has no vertex on the R-side from u_e to y. Put
  delta_e=q-r_e.

Then for every simple-forward e,
  the R-suffix from u_e to y has at most delta_e-1 edges.

Consequently, if the simple-forward edges are ordered so that
  delta_1<=...<=delta_m,
then
  delta_i >= ceil((i+1)/2)
for every i, and hence
  sum_{i=1}^m delta_i >= sum_{i=1}^m ceil((i+1)/2) >= m^2/4.

Equivalently: among forward-oriented whole chords on one common anchor, a family with small total anchor-rank deficit must contain many edges whose clean source rails reintersect the far anchor suffix. In particular every forward whole chord of rank q or q-1 necessarily has such a second source/anchor intersection.

## Body

Fix a simple-forward edge e of rank r. Apply the endpoint-slack dichotomy ed412ed8e3b1 to the avoiding path R, with the endpoint y on the side of u_e opposite x_e. Since R is the precursor of a rank-q ascending anchor, phi(y)=q-1. The reintersection branch is excluded by the definition of simple-forward, so
  t_e <= phi(y)-r = q-1-r = delta_e-1,              (1)
where t_e is the number of R-edges in the suffix from u_e to y.

Now order the simple-forward edges by nondecreasing deficits delta_i. Fix i. For each j<=i, (1) gives
  t_j <= delta_j-1 <= delta_i-1.
Thus all distinct opposite terminals
  u_1,...,u_i
lie in the union of the final delta_i-1 edges of R.

A linear path segment of d edges has 2d+1 vertices. Therefore the final delta_i-1 edges contain at most
  2(delta_i-1)+1=2delta_i-1
vertices. The u_j are pairwise distinct: two distinct edges through v cannot share another vertex by linearity. Hence
  i <= 2delta_i-1,
which rearranges to
  delta_i >= ceil((i+1)/2).

Summing yields the displayed quadratic deficit bound. The weaker estimate m^2/4 follows immediately.

Finally, if delta_e is 0 or 1, (1) would force t_e<1, impossible because u_e is distinct from y and lies on R before its endpoint. Hence such an edge cannot be simple-forward and its clean source rail must reintersect the far suffix.

No paid-cell hypothesis, terminal-singleness, minimum-terminal orientation, or near-extremal assumption is used beyond the existence of the common whole-chord anchor and clean source rails.