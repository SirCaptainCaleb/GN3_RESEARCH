# In the p=5 pattern 4555, three rank-five competitors force an early-blocking edge

## Statement

Let v satisfy phi(v)=5. Suppose f={x,v,u} is a potential-charged ascending nonspecial edge of rank four, so phi(x)=3, and let R=(r1,r2,r3) be a canonical three-edge entrance path ending at x and avoiding v,u.

Let h={y,v,z} be any potential-charged ascending nonspecial edge of rank five through v. Then:

(1) h meets R.

(2) If h misses r1, then it misses r2 and therefore meets r3 only.

(3) If h meets r1, then it also meets r2. In particular the pattern “r1 and r3 but not r2” is impossible.

Consequently, among distinct rank-five edges through v, at most two can miss r1; hence any three such rank-five charged edges force at least one edge meeting both r1 and r2.

## Body

First h must meet R. If h were disjoint from R, then R,f,h would be a five-edge linear path ending in h: R,f is the canonical four-edge witness for f through entrance x; f and h meet exactly at v; and R avoids v,u and is disjoint from h by assumption. This five-edge path enters the nonspecial rank-five edge h through v, which is a terminal of h, contradicting its unique rank-five entrance.

For (2), suppose h misses r1 but meets r2. Then
  r1,r2,h,f
is a four-edge linear path. The consecutive intersections are r1∩r2, the r2-h contact, and h∩f={v}. The edge f is disjoint from r1,r2 because R ends at x, so x lies only in r3, while R avoids v,u. Since h misses r1, all nonconsecutive pairs in the displayed sequence are disjoint. The last edge is f, and x is not in h, so x is a last vertex. This gives phi(x)>=4, contradicting phi(x)=3.

Thus if h misses r1 it also misses r2. Since h must meet R, it meets r3. By linearity h meets r3 in only one vertex, so this is a pure late contact.

For (3), suppose h meets r1 but misses r2. If h also missed r3, then
  h,r1,r2,r3
would be a four-edge linear path ending at x, contradicting phi(x)=3.

Thus h would have to meet r3. But then
  r2,r1,h,f
is a four-edge linear path: h misses r2 by assumption; f is disjoint from r1,r2; and the consecutive intersections are r2∩r1, the r1-h contact, and h∩f={v}. Again x is a last vertex of f, giving phi(x)>=4, contradiction. Hence every h meeting r1 also meets r2.

Finally, if h misses r1, its unique rail contact lies on r3 and cannot be x, because h and f already share v and f contains x; otherwise h and f would share two vertices. The edge r3 has only two vertices other than x. Distinct rank-five edges through v have disjoint non-v pairs, so at most two distinct h can miss r1. Therefore any three rank-five charged edges through v force at least one to meet both r1 and r2.
