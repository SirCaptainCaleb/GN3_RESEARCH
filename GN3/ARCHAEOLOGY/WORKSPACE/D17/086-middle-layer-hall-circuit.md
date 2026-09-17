# Minimal endpoint-Hall circuits and closed-cycle order conflict

**Workspace:** D17
**State:** working
**Key:** `middle-layer-hall-circuit`

**Summary:** Inclusion-minimal Hall deficiency yields the factor-critical endpoint circuit, near-perfect functional endpoint graphs, the quiet alternating common-core normal form, its complete common-anchor P4 grid, and the exact closed-cycle order-conflict residual.

### 6. Inclusion-minimal Hall deficiency forces a source-labelled order conflict

Use ALL endpoint realizations, not the one-order selection of sections 1-2. Let L be the set of Hamilton k-supports and let R_H be the set of Hamilton (k-1)-supports. Join S in L to R=S-{x} when some actual Hamilton path on S exposes x as a physical endpoint. In the uniform residue every k-set belongs to L. The conjectural Endpoint-Deletion Hall target asks whether no (k+1)-path forces a matching saturating L; in the uniform residue such a matching is numerically impossible because C(2k+1,k)>C(2k+1,k-1).

Assume Hall fails and choose an inclusion-minimal deficient family F subseteq L. Put N=N(F) and m=|F|. Then
  |N|=m-1,
and for every S in F,
  N(F-{S})=N.
Indeed minimality gives |N(F-{S})|>=m-1, while N(F-{S}) subseteq N and Hall deficiency gives |N|<=m-1. Hence equality throughout. In particular EVERY R in N has at least two distinct neighbors in F; if R had unique neighbor S then removing S would remove R from the neighborhood. Also every S has at least two endpoint neighbors, supplied by the two physical endpoints of any Hamilton order on S. Thus a minimal Hall witness is automatically an order-valued multi-completion object rather than a single Johnson cycle.

Fix R in N and two distinct incident supports R+{x}, R+{y}. Choose actual endpoint-realizing Hamilton paths P_x,P_y and delete x,y, obtaining actual Hamilton orders Q_x,Q_y on the SAME support R. There are two cases.

(ORDER-CONFLICT) Q_x and Q_y are different literal orders. Then accepted R435 applies directly to this same-core pair and yields a source-labelled reversed old state, reverse trimer, or vertex-simple tight cycle. This output retains R and the two physical completion labels x,y.

(ALIGNED CORE ORDER) Q_x=Q_y=:Q. Orient P_x,P_y according to the endpoint role of x,y. If the two completions occur on opposite sides of Q, then x,Q,y or y,Q,x is a literal Hamilton path on R+{x,y}, of order k+1, contradiction. Hence in a no-growth branch they occur on the SAME side. Treat the tail case; the head case is exact dual. Write
  Q=(a,m_1,...,m_{k-2})
so
  P_x=(a,m_1,...,m_{k-2},x),
  P_y=(a,m_1,...,m_{k-2},y).
Delete the common opposite endpoint a and put M=(m_1,...,m_{k-2}). Uniform k-set Hamiltonicity supplies an actual Hamilton path K on
  V(M) union {x,y}.
The two literal paths (M,x) and (M,y) are inherited from P_x,P_y. Compare K separately with them using R435. If either comparison has a reverse-order encounter, we again obtain a source-labelled R435 output, now on a one-vertex extension of the actual path (M,x) or (M,y). If BOTH comparisons are order-monotone, then K encounters all M vertices in the displayed order, x after all of M, and y after all of M. Therefore necessarily
  K=(M,x,y) or K=(M,y,x).
But (a,m_1,m_2) is tight from P_x (and P_y), so for k>=4 prepending a to K gives a literal tight path on k+1 vertices.

Consequently, in the live smallest-counterexample range, an inclusion-minimal Hall-deficient endpoint family forces EITHER the desired (k+1)-path OR a very specific same-core/source-labelled R435 order-conflict. The Hall obstruction cannot remain a purely combinatorial deficient family or a support-only bicyclic graph.

This does NOT yet prove the endpoint-deletion matching conjecture: generic existence of an R435 output is not closure (compare the standing R483 fence). The remaining theorem is an ORDER-CONFLICT CURRENTIZATION statement for this source. One must consume a same-(k-1)-core order mismatch Q_x != Q_y, or the one-vertex-extension mismatch K versus (M,x)/(M,y), using the full uniform k-support reservoir to produce a k+1 path or a boundary-reversed Hamilton dimer on one fixed k-support. The physical completion labels and actual path orders above must be retained.

Status: complete internal reduction, working/expository only. No canonical theorem status is asserted.

### 7. The minimal Hall witness is a factor-critical endpoint circuit

Retain the all-endpoint bipartite graph and an inclusion-minimal deficient left family F from section 6. Write N=N(F) and m=|F|, so |N|=m-1 and every proper left subfamily satisfies Hall.

First, for EVERY chosen root support S_* in F, the balanced graph between F-{S_*} and N has a perfect matching M. Indeed every subset of F-{S_*} is a proper subset of F and hence satisfies Hall, while the two sides both have size m-1.

Second, alternating reachability from the unmatched root is total. Orient every nonmatching incidence left-to-right and every matching incidence right-to-left. Let X be the reachable left supports from S_* and Y the reachable right cores. Every neighbor of X is reachable, so Y=N(X). Every reachable right core is matched to a reachable nonroot support, and every reachable nonroot support is reached through its matched core. Thus M restricts to a bijection Y <-> X-{S_*}, giving |Y|=|X|-1. If X were a proper subfamily of F it would itself be Hall-deficient, contradicting minimality. Therefore X=F and Y=N.

Third, EVERY actual endpoint incidence S-R in the Hall circuit belongs to some near-perfect matching. Choose a perfect matching of F-{S}. It matches R to some T != S. Replacing the matched edge T-R by S-R leaves T unmatched and still matches every core of N. Thus the full endpoint circuit has no disposable incidence: each endpoint realization can be made part of a matching saturating all right cores.

These facts are purely matching-theoretic consequences of the inclusion-minimal Hall obstruction, but they retain the physical meaning of every incidence: S-R means that some actual Hamilton path on S exposes the unique vertex S-R as an endpoint.

### 8. A near-perfect matching produces a spanning functional endpoint graph

Fix a root S_* and a perfect matching M of F-{S_*} onto N. For each core R in N let S_R be its matched support. Choose an ACTUAL Hamilton path P_R on S_R that exposes the matched completion vertex S_R-R. Let R^+ be the other endpoint-deletion core of that same path. Since S_R lies in F, every endpoint-deletion core of P_R belongs to N.

Create a directed edge

  R -> R^+

labelled by the matched support S_R. Different right cores have different matched supports, and two different supports cannot determine the same unordered pair of endpoint cores because the union of that pair is the support. Hence the underlying graph is simple. There are |N| vertices and |N| such matched-support edges, every vertex has outdegree exactly one, and loops are impossible because the two path endpoints are distinct. Consequently every connected component contains exactly one directed cycle, of length at least three.

Choose any actual Hamilton path on the unmatched root S_* and add its endpoint-core edge. The resulting selected endpoint graph spans ALL cores N and has |N|+1 support-labelled edges. This is the correct selected skeleton of the whole Hall witness: the matching covers every right core, while the unmatched root supplies the single excess support. It is stronger than choosing one arbitrary path on every k-set with no matching coherence.

The full all-endpoint Hall graph remains active around this skeleton. A support may have further endpoint realizations not used by its selected path; those are genuine additional Hall incidences and must be retained as possible matching exchanges, not discarded.

### 9. Quiet matching cycles have an alternating common-core normal form

Consider one directed cycle of the matched functional graph,

  R_0 -> R_1 -> ... -> R_{t-1} -> R_0,

where the edge R_i -> R_{i+1} is the actual Hamilton path P_i on the matched support S_i. Let x_i=S_i-R_i be its matched completion and let y_i=S_i-R_{i+1} be its other endpoint. At the shared core R_i there are two inherited Hamilton orders: delete y_{i-1} from P_{i-1}, and delete x_i from P_i.

Suppose first that these two literal core orders agree at every R_i; call the common order Q_i. If the two completion vertices y_{i-1},x_i occur on opposite sides of Q_i, then y_{i-1},Q_i,x_i or its reversed-side analogue is a literal tight path on k+1 vertices. Thus in a no-growth branch the two completions occur on the SAME side of Q_i.

Let s_i record whether the matched endpoint x_i is the head or tail endpoint of P_i. The other endpoint y_i has the opposite role. At R_i the incoming completion y_{i-1} therefore has side opposite s_{i-1}, while x_i has side s_i. Same-side completion forces

  s_i = opposite(s_{i-1}).

Hence every fully order-aligned directed cycle is EVEN. Write t=2h.

The alternating side relation gives much more than parity. Reverse the cyclic indexing if necessary so that at R_0 the two completion vertices are head completions. Write

  Q_0=(M,z_0),

where M is the ordered (k-2)-vertex prefix. Since P_0 prepends its matched completion x_0,

  P_0=(x_0,M,z_0),
  Q_1=(x_0,M).

At R_1 the completions are tails, so

  P_1=(x_0,M,z_1),
  Q_2=(M,z_1).

Iterating around the cycle gives distinct physical labels x_0,...,x_{h-1} and z_0,...,z_{h-1}, with z_h=z_0, such that for every j modulo h

  Q_{2j}=(M,z_j),
  Q_{2j+1}=(x_j,M),
  P_{2j}=(x_j,M,z_j),
  P_{2j+1}=(x_j,M,z_{j+1}).

All x_j are distinct because the odd-index cycle cores are distinct; all z_j are distinct because the even-index cores are distinct; and X={x_j} is disjoint from Z={z_j}, since x_j=z_l would identify the odd core M+x_j with the even core M+z_l. Therefore the 2h cycle labels are distinct exterior vertices of M, so

  2h <= |V(H)-M| = k+3.

Thus a fully aligned Hall cycle is not an arbitrary Johnson cycle. It is an alternating rectangle cycle around one fixed ordered (k-2)-core M.

### 10. No-growth amplifies an aligned cycle to a complete common-anchor P4 grid

Write M=(a,...,b), with a and b its first and last vertices. Fix x=x_j. The aligned cycle supplies TWO actual Hamilton k-paths with the same head segment,

  (x,M,z_j),   (x,M,z_{j+1}),

and z_j != z_{j+1}. Let w be any vertex outside M union {x}. At least one of those two paths omits w. Prepending w to that path would produce k+1 vertices, so its only new initial turn (w,x,a) is bad. R3 therefore gives

  (a,x,w) tight.

Hence for every x in X and every w outside M union {x}, (a,x,w) is tight.

Dually, for a fixed z=z_j the cycle supplies TWO actual Hamilton k-paths with the same terminal segment,

  (x_{j-1},M,z),   (x_j,M,z).

Every w outside M union {z} is omitted by at least one of them. Appending w would create k+1 vertices, so (b,z,w) is bad and R3 gives

  (w,z,b) tight.

Since X and Z are disjoint and both lie outside M, these two saturation statements combine to give, for EVERY x in X and z in Z,

  (a,x,z) tight,
  (x,z,b) tight.

Therefore

  (a,x,z,b)

is a literal tight P4 for every pair (x,z) in X x Z, not merely for the h cycle edges. In particular the two cyclic wrap seams of every selected cycle path (x,M,z) are the complete reversals of these certified turns, so both wrap seams are bad: every selected path on the quiet aligned cycle is automatically in the R579 double-fail branch.

This complete common-anchor P4 grid is a genuine global consequence of the CLOSED matching cycle. It is unavailable from one arbitrary same-core order conflict or from endpoint richness at one core.

### 11. Exact remaining obstruction after retaining the Hall circuit

The Director-level target is now sharper. Do NOT reduce the Hall witness to an arbitrary pair Q_x,Q_y.

For any near-perfect matching, the matched endpoint graph has at least one directed cycle. Along such a cycle either:

1. some shared core carries different incoming and outgoing inherited Hamilton orders. This is now a CLOSED-CYCLE order conflict tied to a near-perfect matching and to the complete alternating reachability structure, not a free-standing R435 packet; or
2. every shared order aligns, in which case the cycle is even and collapses to the fixed-M alternating normal form above, with the complete P4 grid (a,X,Z,b).

The full all-endpoint incidence graph must remain present in both branches. Any additional endpoint realization of a cycle support is an actual Hall incidence and, by section 7, can itself be placed in a near-perfect matching. A successful next theorem should use those matching exchanges and/or the complete grid to force one of:

* an endpoint core outside the current closed neighborhood, contradicting Hall completeness;
* a verified matching improvement that destroys the deficient circuit;
* a boundary-reversed Hamilton dimer on one fixed k-support; or
* directly a tight path on k+1 vertices.

Generic R435 output, a support-only cycle, or another isolated P4 is not closure. Uniform Middle-Layer Growth remains open. The results in sections 7-10 are complete internal arguments in this development revision and are working/expository only; no canonical theorem status is asserted.




## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
