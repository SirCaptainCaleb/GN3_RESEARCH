# Every endpoint deletion cover has a bounded restoration reversal

## Statement


Let H be a boundary tournament with pc(H)>2. Let
A=(d,a_1,...,a_m), m>=2,
be a displayed tight path, and let T=P|Q be any two-cover of H-d.

Let S be the displayed T-component containing a_1. Then restoration of d immediately before a_1 forces an explicit tight reverse triple in the radius-two neighborhood of a_1 in S.

More precisely:

- if a_1 is the first vertex of S, then S is not a singleton; writing w for its successor, (w,a_1,d) is tight;

- if a_1 has predecessor u in S, and v is the predecessor of u when it exists while w is the successor of a_1 when it exists, then at least one of
(d,u,v), (a_1,d,u), (w,a_1,d)
among the triples whose vertices exist is tight.

The terminal-end symmetric statement holds for a displayed path (...,a_m,d), by inserting d immediately after a_m.

No support-compatibility, crossing-count, or inherited-order hypothesis on T is required.


## Body


Let S be the T-component containing a_1.

First suppose a_1 is initial in S. If S consists only of a_1, then replacing it by the two-vertex path (d,a_1), while leaving the other T-component unchanged, gives a spanning two-cover of H, impossible. Hence S has a successor w.

Prepend d to S. The only new consecutive triple is (d,a_1,w). If it were tight, the modified S together with the unchanged other T-component would form a spanning two-cover of H. Therefore (d,a_1,w) is non-tight, and boundary antisymmetry gives the tight reverse triple
(w,a_1,d).

Now suppose a_1 is not initial in S. Let u be its predecessor, let v be the predecessor of u when one exists, and let w be the successor of a_1 when one exists. Insert d immediately between u and a_1.

Every consecutive triple of the modified path is inherited from S except the following triples that exist:
(v,u,d),
(u,d,a_1),
(d,a_1,w).

If all existing new triples were tight, the modified component together with the unchanged other T-component would be a spanning two-cover of H, impossible. Hence at least one existing new triple is non-tight. Reversing that failed triple by boundary antisymmetry gives respectively
(d,u,v),
(a_1,d,u),
or
(w,a_1,d)
tight.

This proves the initial-end assertion. The terminal-end statement follows by the symmetric insertion of d immediately after the surviving neighbor of d. ∎
