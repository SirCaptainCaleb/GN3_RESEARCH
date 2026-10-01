# A third cross-edge cannot pierce a balanced lens between maximum rails

## Statement

Let two maximum endpoint paths contain a clean internal lens whose two sides have equal length. No hyperedge can have one contact in the interior of each lens side and otherwise be disjoint from the two host rails. The two hybrid routes obtained by crossing through that edge have total length two more than the two original lens sides, so one hybrid is longer and gives an endpoint-preserving path longer than one of the maximum rails.

## Body


Let Q and R be maximum endpoint paths, and suppose two common vertices a,b bound a clean internal lens:
- the Q-side L_Q from a to b and the R-side L_R from a to b are internally vertex-disjoint from each other and from the complementary host rail as required for endpoint-preserving exchange;
- both are internal to their respective endpoint paths;
- by 390e818020e1 they have the same edge length t.

Let f be a hyperedge not belonging to either lens side. Suppose
  f={v,s,r}
where v lies outside V(Q union R),
  s is an internal vertex of L_Q,
  r is an internal vertex of L_R,
and f has no other contact with Q union R. (In the 0-1-1 source-rail application, v is the common assigned terminal and the two contacts s,r are the two non-v vertices of one offending edge.)

Cut L_Q at s and L_R at r. There are two complementary hybrid a-b routes:
  H_1 = (a-to-s along L_Q), f, (r-to-b along L_R),
  H_2 = (a-to-r along L_R), f, (s-to-b along L_Q).

Because the lens is clean, its two sides have disjoint interiors, and f meets them only at s,r, both H_1,H_2 are linear paths. Moreover the pieces used by H_1 and H_2 partition the two original lens sides, while each hybrid uses f once.

Hence
  |H_1|+|H_2| = |L_Q|+|L_R|+2 = 2t+2.

Therefore at least one hybrid has length at least t+1.

If |H_1|>=t+1, replace L_Q inside Q by H_1. The clean-lens hypotheses make this an endpoint-preserving linear path with the same physical endpoint as Q and length at least |Q|+1, contradicting maximality of Q.

If |H_2|>=t+1, replace L_R inside R by H_2 and contradict maximality of R.

Thus no such interior cross-edge f can exist across a balanced clean lens between maximum endpoint paths.
