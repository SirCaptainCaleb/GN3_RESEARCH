# Lens-free flat cycles force the two adjacent edges to be exact opposite-terminal single blockers on every entrance rail

## Statement

Let
  C=(e_0,...,e_{c-1}),  c>=4,
be a flat gap-one terminal cycle with
  e_i={x_i,t_i,t_{i+1}},
indices modulo c, where every e_i is ascending nonspecial of rank p-1, every terminal t_i has phi(t_i)=p, and every private entrance x_i has phi(x_i)=p-2.

For each i let
  R_i=(r_1,...,r_{p-2})
be a canonical maximum entrance rail ending physically at x_i such that R_i,e_i is a longest (p-1)-edge path ending in e_i. Assume the residual is entrance-rail lens-free in the sense that no two distinct rails R_i,R_j contain a balanced elementary lens.

Then, for every i,
  e_{i-1} intersect V(R_i) = {t_{i-1}},
  e_{i+1} intersect V(R_i) = {t_{i+2}}.
In particular e_{i-1} and e_{i+1} are exact one-contact blockers on R_i, through the two opposite terminal colors of e_i, and neither neighboring entrance x_{i-1},x_{i+1} lies on R_i.

Moreover the first R_i-edge containing t_{i-1} and the first R_i-edge containing t_{i+2} each has index at most p-4.

Thus every lens-free flat gap-one cycle canonically embeds, on each entrance rail, the two opposite-terminal single blockers needed by the two-terminal shared-rail system.

## Body

Fix i. The edge e_{i-1} is a distinct ascending nonspecial edge of rank p-1 terminal at t_i. Since R_i is a canonical source rail for the rank-(p-1) edge e_i, downward-completeness of canonical source rails (1c8aac8aa4dd) forces e_{i-1} to meet R_i.

Relative to the common terminal t_i, the two non-t_i vertices of e_{i-1} are x_{i-1} and t_{i-1}. The rail R_i avoids t_i and t_{i+1}, the two terminals of e_i. If x_{i-1} belonged to R_i, then c2d109a240a9 would imply that R_i and R_{i-1} share at least two vertices and hence contain a balanced elementary lens, contrary to the lens-free hypothesis. Therefore x_{i-1} is absent from R_i, so the forced contact is t_{i-1}. Since e_{i-1} has no other non-t_i vertex available, this contact is unique:
  e_{i-1} intersect V(R_i)={t_{i-1}}.

The same argument at the other terminal t_{i+1}, using e_{i+1}, gives
  e_{i+1} intersect V(R_i)={t_{i+2}}.

For the positional assertion, consider the forward adjacent blocker e_{i+1}. The short cycle arc e_{i+1},e_i meets R_i only at t_{i+2} and x_i: the first equality above gives the unique e_{i+1}-contact, while R_i,e_i is a linear path and hence e_i meets R_i only at x_i. Thus the d=1 case of 6a28d8bc3cc4 applies and places the first occurrence of t_{i+2} by rail-edge index at most p-4. Reversing the cycle orientation gives the same bound for t_{i-1}.

Finally the two blockers are through different terminals t_i and t_{i+1} of e_i, so on the common source rail R_i they are exactly the opposite-terminal one-contact blockers appearing in the two-terminal coupling framework.