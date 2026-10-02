# The half-rank four-slot gadget has a three-edge conflict graph with forced cross-blockers

## Statement

In the top-boundary q,(q+1)^3 four-slot normal form, let
 a=g_{q-2}∩g_{q-1},
 b=private(g_{q-1}),
 x=g_{q-1}∩g_q,
 c=private(g_q),
 d=g_q∩g_{q+1}.
Every occupied slot y is the unique entrance of a rank-(q+1) high edge h_y={y,v,z_y}.

Then the slot pairs {a,c}, {a,d}, and {b,d} are conflict pairs in the following precise sense.

(A) If a and r are occupied, where r∈{c,d}, then at least one of:
  z_r ∈ V(g_1∪...∪g_{q-2}),
  z_a ∈ V(g_1∪...∪g_{q-2}∪g_q)
must hold.

(B) If b and d are occupied, then at least one of:
  z_b ∈ V(g_{q+1}∪...∪g_{2q-3}),
  z_d ∈ V(g_{q+1}∪...∪g_{2q-3}∪g_{q-1})
must hold.

Consequently every three-of-four entrance pattern on {a,b,c,d} forces at least one explicit opposite-terminal cross-blocker, because every 3-subset contains one of the conflict pairs ac,ad,bd.

## Body

For (A), assume a and r∈{c,d} are occupied and neither blocker alternative holds. Consider
  g_1,...,g_{q-2}, h_a, h_r, g_q.

The prefix ends at a because a=g_{q-2}∩g_{q-1} and g_{q-1} is omitted, so h_a meets the prefix consecutively at its entrance a. The edges h_a,h_r meet exactly at v. The edge h_r meets g_q consecutively at its entrance r: c is private in g_q, while d=g_q∩g_{q+1} and g_{q+1} is omitted.

By the assumed failure of the blocker alternatives, z_r is absent from the prefix, while z_a is absent from both the prefix and g_q. Also z_r cannot give a second g_q contact because h_r already meets g_q at r and linearity forbids two common vertices. Thus there are no nonconsecutive intersections, and the displayed sequence is linear.

Its length is
  (q-2)+2+1=q+1.
Its last edge is g_q. Since g_{q-1} is omitted, x=g_{q-1}∩g_q is a last vertex. Hence phi(x)>=q+1, contradicting phi(x)=q-1.

Therefore one of the two alternatives in (A) is forced.

For (B), assume b,d are occupied and neither blocker alternative holds. Consider the reversed-suffix splice
  g_{2q-3},g_{2q-4},...,g_{q+1}, h_d, h_b, g_{q-1}.

The retained suffix has q-3 edges. Its last edge g_{q+1} meets h_d consecutively at d. The edges h_d,h_b meet at v. The edge h_b meets g_{q-1} at its private entrance b. The omitted edge g_q separates g_{q+1} from g_{q-1}, so those path edges are disjoint.

By the assumed failure of the blocker alternatives, z_b is absent from the retained suffix and z_d is absent from both the retained suffix and g_{q-1}. Linearity forbids z_b from giving a second contact with g_{q-1}. Hence the splice is linear.

Its length is
  (q-3)+2+1=q.
The last edge g_{q-1} contains x, and g_q is omitted, so x is a last vertex. Thus phi(x)>=q, contradicting phi(x)=q-1.

Finally, the four possible occupied triples are abc, abd, acd, bcd. They contain respectively the conflict edges ac; ad and bd; ac and ad; bd.