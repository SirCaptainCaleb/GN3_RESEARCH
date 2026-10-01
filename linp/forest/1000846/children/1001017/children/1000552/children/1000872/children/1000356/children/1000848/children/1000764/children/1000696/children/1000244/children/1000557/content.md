# The B,C two-low odd-boundary pattern cannot support two additional non-double high edges

## Statement

Let v have phi(v)=2q-3, q>=4, and let
  P=(g_1,...,g_{2q-3})
be maximum at v. Put
  L=g_{q-3}∩g_{q-2},
  A=g_{q-2}∩g_{q-1},
  B=private(g_{q-1}),
  C=g_{q-1}∩g_q,
  R=private(g_q),
  D=g_q∩g_{q+1}.

Suppose two non-double rank-q charged edges have witnesses {B,C}. Then there cannot be two further non-double rank-(q+1) charged edges at v.

Hence any four-edge consecutive-rank family with two rank-q edges in the {B,C} pattern has at least one double contact and satisfies the defect-corrected block.

## Body

By 35ee7b35de05, both B and C are rank-q entrances, so
  phi(B)=phi(C)=q-1.

Because C is a clean joint entrance at
  g_{q-1}∩g_q,
the mixed joint-hole lemma eac2e3da3eea forbids every other single-contact edge whose first-contact cell is q-2. In particular the slots
  A=g_{q-2}∩g_{q-1}
and
  private(g_{q-2})
cannot be occupied by another non-double charged edge.

By 0c5ee88a3a70, the presence of the middle-private rank-q entrance B forces
  phi(D)>=2q-3.
Therefore D cannot be a rank-(q+1) entrance; by a01ddfa76dc8 it also cannot be a terminal-only high witness. Thus D is unavailable.

The two high non-double edges must therefore use the only remaining witness slots, namely
  L=g_{q-3}∩g_{q-2}
and
  R=private(g_q).
Call them h_L and h_R. Since each is non-double, each has exactly that one P-contact outside the last edge.

Now consider
  g_1,...,g_{q-3}, h_L,h_R,g_q.
The prefix meets h_L at L; h_L and h_R meet at their common terminal v; h_R meets g_q at R. The omitted edges g_{q-2},g_{q-1} separate prefix from g_q, and the single-contact hypotheses exclude all other intersections. Hence this is a linear path.

Its length is
  (q-3)+2+1=q.
Its final edge is g_q. Since g_{q-1} is omitted, the joint
  C=g_{q-1}∩g_q
is a physical last vertex. Thus
  phi(C)>=q,
contradicting phi(C)=q-1.

Therefore the assumed two additional non-double high edges cannot exist.
