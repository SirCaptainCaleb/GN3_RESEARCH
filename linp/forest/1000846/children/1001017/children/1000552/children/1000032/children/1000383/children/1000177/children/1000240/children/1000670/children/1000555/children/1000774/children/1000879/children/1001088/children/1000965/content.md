# Half-rank q,(q+1)^3 obstructions have a visible high entrance

## Statement

At phi(v)=2q-2, fix a maximum v-path and a charged rank-q edge e. Its entrance is the universal central joint. Each rank-(q+1) charged competitor has a selected witness in four surrounding slots L,A,B,R. If two competitors have entrances absent, their opposite-terminal witness slots are necessarily {L,B} or {L,R}. Hence among three rank-(q+1) competitors at least one entrance is visible on the path; that visible entrance has potential q.

## Body

Let v have p=2q-2, let e={x,v,u} be the charged rank-q edge, and fix a maximum path
  P=(g_1,...,g_p)
ending physically at v.

By cf6ab8703be5,
  x=g_{q-1} cap g_q
is the universal central entrance of e on P.

Let h be a charged ascending rank-(q+1) edge through v. Apply the path-relative witness localization 220a14637b5f with Q=q+1. The possible private witness positions are g_{q-1},g_q, and the possible joint witness positions are
  g_{q-2} cap g_{q-1},
  g_{q-1} cap g_q=x,
  g_q cap g_{q+1}.
Since h and e already share v, h cannot contain x by linearity. Thus every selected witness of a high edge belongs to exactly four slots:
  L = g_{q-2} cap g_{q-1},
  A = private(g_{q-1}),
  B = private(g_q),
  R = g_q cap g_{q+1}.

Suppose two distinct high edges h_1,h_2 have their entrances absent from P. Then their selected witnesses are their opposite terminals, so each is a terminal-only one-vertex contact with P. Order them by first occurrence.

By df8ad4c65be0, the earlier contact has first occurrence index at most
  (q+1)-3=q-2.
Among {L,A,B,R}, only L has first occurrence at most q-2. Hence the earlier witness is L.

By f0c177137b7f, the later contact has last occurrence index at least
  p-(q+1)+3
  =(2q-2)-(q+1)+3
  =q.
Among the remaining slots, A has last occurrence q-1, while B has q and R has q+1. Hence the later witness is B or R.

Therefore any pair of absent-entrance high competitors has witness slots
  {L,B} or {L,R}.

In particular three high competitors cannot all have entrances absent. Indeed order their terminal witnesses by first occurrence. Applying df8ad4c65be0 to the second and third would force the second also to have first occurrence <=q-2, hence also to occupy L, impossible because distinct edges through v have disjoint non-v pairs and selected witnesses are distinct.

Thus among any three rank-(q+1) charged competitors in the half-rank q,(q+1)^3 configuration, at least one has its entrance visible on P. Every visible high entrance has potential exactly q.
