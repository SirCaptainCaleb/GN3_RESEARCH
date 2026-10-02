# Disjoint outer maximum rails force aligned gates past half the shorter rail

## Statement

Let
  A=(a_1,...,a_m), B=(b_1,...,b_n), C=(c_1,...,c_\ell)
be maximum endpoint paths ending at vertices x_A,x_B,x_C with
  phi(x_A)=m, phi(x_B)=n, phi(x_C)=ell.
Assume
  V(A)∩V(B)={y},  V(B)∩V(C)={z},  V(A)∩V(C)=emptyset,
and assume the unique intersections are aligned joints:
  y=a_r∩a_{r+1}=b_r∩b_{r+1},
  z=b_s∩b_{s+1}=c_s∩c_{s+1}.

Then:
- if r<=s, r>=ceil(m/2);
- if s<=r, s>=ceil(ell/2).
Consequently
  min{r,s} >= ceil(min{m,ell}/2).

In particular this applies automatically whenever each adjacent rail pair has lengths differing by at most one, by the existing unique-intersection alignment lemmas.

## Body

Suppose first that r<=s. Traverse A backwards from its last vertex x_A to y, then B forward from y to z, then C forward from z to its last vertex x_C.

Because A meets B only at y, B meets C only at z, and A is disjoint from C, these three pieces concatenate to a linear path. Its length is
  (m-r)+(s-r)+(ell-s)
  = m+ell-2r.
It ends at x_C, whose endpoint potential is ell. Hence maximality at x_C gives
  m+ell-2r <= ell,
so
  2r>=m
and therefore
  r>=ceil(m/2).

If s<=r, use the symmetric route: traverse C backwards from x_C to z, then B backwards from z to y, then A forward from y to x_A. Its length is
  (ell-s)+(r-s)+(m-r)
  = m+ell-2s.
It ends at x_A, whose endpoint potential is m. Thus
  m+ell-2s <= m,
so
  2s>=ell
and
  s>=ceil(ell/2).

In the first case min{r,s}=r>=ceil(m/2)>=ceil(min{m,ell}/2); in the second min{r,s}=s>=ceil(ell/2)>=ceil(min{m,ell}/2).

If adjacent rail lengths differ by at most one, the hypotheses that unique intersections are aligned joints follow from 5854d853a44b and 80c9c39fb602, yielding the final application.