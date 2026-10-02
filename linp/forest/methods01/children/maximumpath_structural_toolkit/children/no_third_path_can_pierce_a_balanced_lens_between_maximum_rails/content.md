# No third path can pierce a balanced lens between maximum rails

## Statement

Let two maximum endpoint paths contain a clean internal lens with equal-length sides. No nontrivial third path can have a clean subpath joining an interior vertex of one lens side to an interior vertex of the other. The two complementary hybrid replacements have total length larger than the two original lens sides by twice the third-segment length, so one replacement beats a maximum endpoint path.

## Body


Let Q and R be maximum endpoint paths containing a clean internal balanced lens between common vertices a,b. Let the Q-side and R-side of the lens both have edge length t.

Let T be any linear path having a subpath W from a vertex s in the interior of the Q-side to a vertex r in the interior of the R-side. Assume:
- the interior of W is disjoint from both lens sides;
- W meets the two lens sides only at s and r;
- the two hybrid replacements obtained by using W preserve linearity with the exterior portions of Q and R.

Write l=|W|>=1.

As in b5d44965d984, cut the Q-side at s and the R-side at r. Form the two complementary a-b hybrids:
  H_1 = (a-to-s on Q), W, (r-to-b on R),
  H_2 = (a-to-r on R), reverse(W), (s-to-b on Q).

The pieces of the two original lens sides are partitioned between H_1,H_2, while W is used once in each. Hence
  |H_1|+|H_2|
   = |L_Q|+|L_R|+2|W|
   = 2t+2l
   >2t.

Thus one hybrid has length at least t+1. Replacing the corresponding t-edge lens side inside Q or R by that hybrid gives an endpoint-preserving path longer than a maximum endpoint path, contradiction.

Therefore no nontrivial third path can cleanly cross from the interior of one side of a balanced lens to the interior of the other.

In particular, for an elementary lens between two source rails in a 0-1-1 obstruction, every other source rail is forbidden from piercing the lens with a clean segment. Any apparent crossing must instead hit a lens boundary, have an additional intersection that subdivides the lens, or route entirely outside at least one side.
