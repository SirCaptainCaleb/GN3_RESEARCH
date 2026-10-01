# At p=2q-3 two rank-q edges force a double in every four-edge consecutive-rank family

## Statement

Let v have p=phi(v)=2q-3, q>=4, and fix a maximum p-edge path P ending at v.

Suppose four assigned potential-charged ascending nonspecial edges at v have ranks in {q,q+1}, with exactly two of rank q. Then at least one of the four edges is double on P.

Equivalently, an all-single four-edge family cannot contain two rank-q edges.

## Body

Assume for contradiction that all four edges are non-double.

By 35ee7b35de05, the two rank-q witness patterns are {A,B} or {B,C}, with
  A=g_{q-2}∩g_{q-1},
  B=private(g_{q-1}),
  C=g_{q-1}∩g_q,
and B a rank-q entrance.

The {B,C} pattern is impossible by 7c96100c3167. Thus only {A,B} remains.

Introduce
  L=g_{q-3}∩g_{q-2},
  E=private(g_{q-2}),
  R=private(g_q),
  D=g_q∩g_{q+1}.

First D is unavailable by 0c5ee88a3a70: the middle-private rank-q entrance B forces phi(D)>=p, while D would have potential q if it were a rank-(q+1) entrance; terminal-only use of D is excluded by a01ddfa76dc8.

Next E is unavailable. Since B is a rank-q entrance, the prefix
  Q_B=(g_1,...,g_{q-1})
is a canonical (q-1)-edge entrance path ending physically at B, and Q_B followed by the rank-q B-edge is a longest q-edge path through its entrance. A high edge whose sole P-contact were E would meet Q_B in exactly one private contact on its edge r_{q-2}. But c448268039f5 says any clean single-contact competitor on a canonical rank-q entrance rail must occur at a private position j<=q-3. Contradiction.

If C is occupied by a high non-double edge, it cannot be a visible entrance: a clean joint entrance at C would, by eac2e3da3eea, forbid the preceding contact cell q-2, which already contains the low witness A. Hence any high edge at C is terminal-only.

Thus the two high witnesses must be chosen from {L,C,R}.

No pair containing L is possible. Let h_L be the high edge whose sole contact is L and let f_A be the low rank-q edge whose sole contact is A. Then
  g_1,...,g_{q-3}, h_L,f_A,g_{q-1}
is linear: the omitted g_{q-2} separates the retained path pieces, and the single-contact hypotheses remove all extra intersections. Its length is q and its final edge g_{q-1} can end physically at B. Hence phi(B)>=q, contradicting phi(B)=q-1.

The sole remaining pair is {C,R}. Let h_C be the C-edge and let f_A again be the low A-edge. Then
  g_1,...,g_{q-2}, f_A,h_C,g_q
is linear and has length
  (q-2)+2+1=q+1.
Its final edge g_q can end physically at R. But R is necessarily the visible entrance of the high edge using slot R, so phi(R)=q. This contradiction eliminates {C,R}.

Therefore an all-single four-edge family with two rank-q members cannot exist. At least one edge is double on P.