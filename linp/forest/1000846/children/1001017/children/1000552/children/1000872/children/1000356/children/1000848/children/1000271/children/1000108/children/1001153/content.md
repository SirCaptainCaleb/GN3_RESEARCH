# The visible-entrance C branch of the one-low odd-boundary obstruction is impossible

## Statement

Retain the source-clean one-low setting of 18cdb6e257aa at
  p=phi(v)=2q-3, q>=4.
If the unique rank-q edge has its witness
  C=g_{q-2}∩g_{q-1}
as its visible entrance, then the four-edge all-single configuration is impossible.

Hence any surviving source-clean q,(q+1)^3 all-single state has the low edge
  e={x,v,C}
with x absent from P_v and C its sole terminal contact on P_v.

## Body

If C is the visible entrance of the rank-q edge, then
  phi(C)=q-1.
The clean-joint hole lemma at C forbids A, so since four of A,B,C,D,E are occupied, the occupied set is exactly
  {B,C,D,E}.

Because B and C are occupied, E cannot be a visible entrance: a clean joint entrance at E=g_{q-1}∩g_q would forbid first-contact cell q-2 and therefore both B and C. Thus the high edge h_E using E is terminal-only. Let h_B be the high edge using B. Both are single-contact on P_v.

Consider the reversed suffix excluding the final v-edge:
  g_{p-1},g_{p-2},...,g_q,h_E,h_B,g_{q-2}.
The reversed path suffix has p-q=q-3 edges. It meets h_E only at E on g_q; h_E and h_B meet exactly at v; h_B meets the final retained edge g_{q-2} only at its private contact B. The omitted edge g_{q-1} separates g_q from g_{q-2}, and the single-contact hypotheses exclude all other intersections. Hence the displayed sequence is linear.

Its length is
  (q-3)+2+1=q.
Its final edge is g_{q-2}; since the predecessor h_B meets g_{q-2} at B, while g_{q-1} is omitted, the joint
  C=g_{q-2}∩g_{q-1}
is a last vertex.

Thus
  phi(C)>=q,
contradicting phi(C)=q-1.

Therefore C cannot be the visible low entrance. Since 18cdb6e257aa already forces the low witness to C, it must be terminal-only.
