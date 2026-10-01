# A source rail couples its two terminal stars into one alternating blocker system

## Statement

Let e={x,u,v} be an ascending nonspecial edge of rank q>=2, with unique entrance x and terminals u,v. Let
  R=(g_1,...,g_{q-1})
be a canonical maximum source rail ending physically at x, so R,e is a q-edge path and R avoids u,v. Put
  W=V(R) minus {x},
so |W|=2q-2.

For w in {u,v}, let T_w be any family of distinct nonspecial edges f!=e through w such that w is a terminal of f and phi(f)<=q+1. Then every f in T_w meets W in one or two vertices. Let S_w and B_w count the one-contact and two-contact members of T_w, and let M_w be the set of two-vertex contact pairs of the B_w members.

Then:
(1) M_u and M_v are matchings on W and are edge-disjoint.
(2) M_u union M_v is a simple maximum-degree-two graph whose nontrivial components are alternating paths and even alternating cycles.
(3) If p is the number of path components, isolated vertices included, then
    p=(2q-2)-(B_u+B_v).
(4) If U_w is the number of vertices of W unused by all contacts from T_w, then
    S_u+S_v+U_u+U_v=2p.
(5) Writing d_w^*=1+|T_w|=1+S_w+B_w for the truncated star count including e,
    2d_w^*=2q+S_w-U_w,
and hence
    d_u^*+d_v^*=2q+S_u+S_v-p.

Thus the two terminal stars of one ascending edge are not independent: on the common source rail their double contacts form a single alternating path-cycle system, and its open-chain defects are exactly the single/unused contact defects of the two stars.

## Body

Fix w in {u,v}. By downward-completeness of canonical source rails (1c8aac8aa4dd), every f in T_w meets R, since phi(f)<=q+1. Because f and e are distinct edges through w, linearity gives f intersect e={w}. In particular f contains neither x nor the other terminal of e. Hence every R-contact of f belongs to W.

The edge f has only two vertices different from w, so it meets W in one or two vertices. Distinct edges through w cannot share a second vertex, so the two-vertex contact sets of the double-contact members are pairwise disjoint: M_w is a matching.

If the same pair {a,b} were an edge of both M_u and M_v, the corresponding hyperedges {u,a,b} and {v,a,b} would share a and b, violating linearity. Thus M_u,M_v are edge-disjoint. Their union has maximum degree at most two, and every degree-two vertex is incident with one edge of each matching. Therefore its nontrivial components are alternating paths and even alternating cycles.

Since |W|=2q-2 and the union has B_u+B_v edges, the standard path-cycle identity gives
  p=|W|-|M_u union M_v|
   =(2q-2)-(B_u+B_v),
where isolated vertices count as path components.

For a fixed w, the B_w doubles occupy 2B_w vertices of W and the S_w singles occupy S_w further distinct vertices, so
  2q-2=2B_w+S_w+U_w.
Summing over w=u,v and using the displayed formula for p gives
  S_u+S_v+U_u+U_v=2p.

Finally d_w^*=1+S_w+B_w. Combining this with
  2q-2=2B_w+S_w+U_w
gives
  2d_w^*=2+2S_w+2B_w
          =2q+S_w-U_w.
Summing over u,v and eliminating U_u+U_v via the preceding defect identity yields
  d_u^*+d_v^*=2q+S_u+S_v-p.