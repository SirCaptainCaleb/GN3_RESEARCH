# No third path can cleanly pierce any clean lens between maximum endpoint paths

## Statement

Let Q,R be maximum endpoint paths and let two common vertices bound any clean lens between them, with arbitrary side lengths A,B. No third path can cleanly pierce from the interior of one lens side to the interior of the other. The two complementary hybrids have total length A+B+2l; if one does not beat the Q-side length A, the other necessarily beats the R-side length B. Thus the earlier no-piercing theorem does not require a balanced lens.

## Body

Let Q and R be maximum endpoint paths ending at x and y. Let a,b be two common vertices such that the Q-side L_Q and R-side L_R form a clean lens. Write
  A=|L_Q|,
  B=|L_R|.

Let T be a third linear path having a clean subpath W of length l>=1 from an interior vertex s of L_Q to an interior vertex r of L_R. Assume, as in the standard piercing setup, that:
- the interior of W is disjoint from both lens sides;
- W meets the lens sides only at s,r;
- the two complementary a-b hybrids preserve linearity with the exteriors of Q and R.

Form
  H_1=(a-to-s on Q), W, (r-to-b on R),
  H_2=(a-to-r on R), reverse(W), (s-to-b on Q).

The original lens-side pieces are partitioned between H_1,H_2 and W is used once in each, so
  |H_1|+|H_2|=A+B+2l>A+B.                           (1)

If |H_1|>A, replace the Q-side L_Q by H_1. By the clean-piercing hypothesis this gives a linear path ending at x of length
  |Q|-A+|H_1|>|Q|=phi(x),
contradiction.

Otherwise |H_1|<=A. Then from (1),
  |H_2|=A+B+2l-|H_1|
       >=B+2l
       >B.
Replace the R-side L_R by H_2. This gives a linear path ending at y longer than R, contradiction.

Therefore no such clean piercing W exists.

No equality A=B is required. Balancedness was useful for other lens bookkeeping, but not for the piercing exclusion itself.
