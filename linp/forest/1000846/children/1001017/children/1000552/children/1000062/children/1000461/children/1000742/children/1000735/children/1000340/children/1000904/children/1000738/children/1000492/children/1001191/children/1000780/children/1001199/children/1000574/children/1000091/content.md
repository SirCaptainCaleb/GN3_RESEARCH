# Gap-one top-rank edges either pay to alignment or move nondecreasingly in potential

## Statement

Let e={x,v,u} be ascending nonspecial of rank q with phi(v)=q+1 and v terminal. Then either phi(u)=q, in which case u is rank-aligned (its maximum ascending-terminal rank equals phi(u)); or phi(u)>=q+1=phi(v). Thus every top-rank edge at a gap-one vertex either lands on an aligned terminal one level lower or is nondecreasing in endpoint potential.

## Body


Let H be a finite linear 3-graph. Let
  e={x,v,u}
be an ascending nonspecial edge of rank q, with v terminal and
  phi(v)=q+1.

Since e has rank q and u is a terminal vertex of e, there exists a q-edge path ending in e through the unique entrance x with physical last vertex u. Hence
  phi(u)>=q.

Therefore exactly one of the following holds.

(ALIGNED-DROP)
  phi(u)=q.
Then e is a rank-phi(u) ascending edge terminal at u. In particular, if q(u) denotes the maximum rank of an ascending edge terminal at u, then
  q(u)>=q=phi(u),
while always q(u)<=phi(u); hence q(u)=phi(u). Thus u belongs to the aligned set V_0.

(NONDECREASING)
  phi(u)>=q+1=phi(v).
Then the opposite terminal has potential at least that of v.

Consequently every rank-(phi(v)-1) ascending edge terminal at a gap-one vertex v either has its opposite terminal in V_0 at potential phi(v)-1, or is potential-nondecreasing away from v.

Now orient each such top-rank edge from v toward u whenever phi(u)>=phi(v); if phi(u)=phi(v)-1, mark the edge as paid-to-alignment. The resulting directed top-rank gap-one graph has no potential-decreasing arcs except those terminating at V_0.

Hence for any set W of gap-one vertices disjoint from V_0, every top-rank edge incident to W which does not leave W upward in potential either:
- joins two vertices of equal potential inside W; or
- pays directly to an aligned terminal outside W at the immediately lower level.

This is an exact structural dichotomy, requiring no conjectural oriented-degree bound.
