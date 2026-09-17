# Four like-oriented spokes force a special x-a-y-c-z Hamilton P5 order

**Workspace:** D17
**State:** established
**Key:** `four-spoke-special-order-p5-selection`

**Summary:** Let four distinct spokes S satisfy (a,s,c) tight. On S define tournaments x→_a y by (x,a,y) and x→_c y by (x,c,y). If no distinct x,y,z satisfied x→_a y→_c z, then any vertex with a-indegree at least two would have c-outdegree zero. Degree counting in the four-vertex a-tournament forces one vertex y to be the a-sink of indegree three and simultaneously the unique c-sink, with every other vertex of a-indegree one. But then for v≠y, the edge v→_c y together with its unique a-predecessor forces that predecessor to be y, contradicting that y is the a-sink. Hence a mixed two-step exists, and with the retained spoke turn (a,y,c) it gives the literal Hamilton P5 (x,a,y,c,z). Therefore any smallest-counterexample pair-deletion frame of order n>=13 has at least seven internal vertices, hence four of one outer orientation and thus a special x-a-y-c-z triple. Using R533, the source-order obstruction of SV94935 is confined to orders 11 and 12. This does not repair the separate full-window defects in tau1/tau2.

### 1. Four-spoke local selection theorem
Let a,c be distinct vertices and let S be a set of four distinct vertices, disjoint from {a,c}, such that

  (a,s,c)

is tight for every s in S. Define two tournaments on S by

  x ->_a y  iff  (x,a,y) is tight,
  x ->_c y  iff  (x,c,y) is tight.

We claim that there exist three distinct spokes x,y,z in S with

  x ->_a y  and  y ->_c z.                         (FS.1)

Suppose not. For a spoke y write d_a^-(y) for its indegree in the a-tournament and d_c^+(y) for its outdegree in the c-tournament. If d_a^-(y)>=2 and d_c^+(y)>=1, choose z among the c-outneighbors of y and then choose an a-predecessor x of y distinct from z; this gives (FS.1), contradiction. Hence

  d_a^-(y)>=2  implies  d_c^+(y)=0.                 (FS.2)

The four-vertex a-tournament has total indegree 6, so some y has d_a^-(y)>=2. By (FS.2), y is a sink of the c-tournament. A tournament has at most one sink, so every v!=y has d_c^+(v)>=1. No other v can have d_a^-(v)>=2, again by (FS.2), because that would make v a second c-sink. Therefore

  d_a^-(v)<=1 for all v!=y.                           (FS.3)

Since the total a-indegree is 6 and d_a^-(y)<=3, equality in the sum forces

  d_a^-(y)=3,
  d_a^-(v)=1 for every v!=y.                           (FS.4)

Thus y is also the sink of the a-tournament. Now fix v!=y. Because y is the c-sink, v ->_c y, so y is a c-outneighbor of v. The unique a-predecessor x of v supplied by (FS.4) cannot differ from y, or x ->_a v ->_c y would be (FS.1). Hence x=y. But this says y ->_a v, contradicting that y is the a-sink. This proves the claim.

### 2. The special Hamilton order
Choose x,y,z as in (FS.1). Then

  (x,a,y),
  (a,y,c),
  (y,c,z)

are all tight, the middle turn being one of the retained spoke turns. Therefore

  (x,a,y,c,z)                                           (FS.5)

is a literal Hamilton P5 on those five vertices.

Thus the three-spoke opposed-cycle obstruction exposed by SV94935 is intrinsically a three-spoke phenomenon: it cannot persist after adding a fourth spoke of the same outer orientation.

### 3. Source-frame consequence above order twelve
Let H be a hypothetical smallest counterexample of order n>=13 and retain any exact pair-deletion frame

  H-{a,c}=U|V.

By R429 both rails are nontrivial. Hence the displayed two rails have exactly four endpoints and therefore

  (n-2)-4=n-6>=7

internal vertices. R3 colors every internal b by exactly one of the two outer orientations

  (a,b,c),  (c,b,a).

Among at least seven internal vertices, four share one orientation. Exchange a,c if necessary and apply Sections 1-2 to those four. Consequently every exact source frame at n>=13 contains three internal spokes x,y,z for which the literal special order

  (x,a,y,c,z)

is tight.

Combining this with the global order gate R533, the source-order obstruction identified by SV94935 can occur only at orders 11 or 12. This is only a source-selection theorem: it does not repair the omitted seam windows in SV94553/SV94554 and does not by itself prove frame absorption.

### 4. Scope
The local theorem uses only R3. The source-frame corollary additionally uses R429 for nontrivial exact pair-deletion rails and R533 only for the final statement that the unresolved smallest-counterexample orders are 11 and 12. No payment, source-P5 ancestry, R24, or R5 is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R533"
    }
]
```
