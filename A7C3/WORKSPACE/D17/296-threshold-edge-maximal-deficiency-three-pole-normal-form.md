# An edge-maximal optimal threshold cell has canonical nearest-edge flow and at most three source/sink poles

**Workspace:** D17
**State:** established
**Key:** `threshold-edge-maximal-deficiency-three-pole-normal-form`

**Summary:** In an edge-ordered complete graph with increasing path-cover number three, choose a generic threshold cell B_tau with maximum matching n-3 and, among such cells, maximum edge count. Every adjacent threshold move must delete rather than add one bipartite edge. This forces an exact nearest-edge rule: the incident edge immediately below tau_v is active into v, and the incident edge immediately above tau_v is active out of v. Hence the physical threshold digraph is acyclic; its sources are exactly vertices whose cut lies below all incident labels, its sinks exactly those above all incident labels, and every other vertex has canonical active incoming and outgoing nearest-edge arcs. There are between one and three sources and between one and three sinks because each source/sink forces an unmatched bipartite copy in every maximum matching. Completeness gives every source-to-sink arc. If there are three sources/sinks, the unmatched copies of every maximum matching are exactly those poles; otherwise at least one unmatched copy is an internal defect at a vertex that still has a canonical threshold incidence. Thus G22 Hall focus reduces an edge-maximal optimal cell to a finite THREE-POLE versus INTERNAL-DEFECT normal form.


### 1. Extremal optimal threshold cell

Work in the integrable edge-ordered setting of accepted R932/R936. Let G=K_V have n vertices and suppose

  pc_inc(G)=3.

For a generic threshold vector tau write B_tau for the balanced bipartite threshold graph

  u_out v_in in B_tau  iff  tau_u < lambda(uv) < tau_v.

Accepted threshold duality gives

  max_tau nu(B_tau)=n-3.

Threshold space is cut into finitely many generic cells by the hyperplanes tau_v=lambda(vu). Inside one cell B_tau is constant. Choose an optimal cell C with

  nu(B_tau)=n-3

whose threshold graph has maximum possible edge count |E(B_tau)| among all optimal cells.

Crossing one facet of a generic cell changes exactly one threshold relation tau_v ? lambda(vu), hence toggles exactly one directed bipartite edge. If a neighboring cell added an edge to B_tau, its matching number could not decrease and cannot exceed n-3 because pc_inc(G)=3. It would therefore also be optimal but would have more edges, contradicting the choice of C. Consequently

  EVERY FACET MOVE AWAY FROM C TOGGLES ONE CURRENT EDGE OFF; NO ADJACENT MOVE ADDS AN EDGE.   (TH.1)

This is a finite history-free local maximum, not a statement that arbitrary multi-facet threshold motion is impossible.

### 2. The nearest edge below every cut is an incoming threshold edge

Fix v. Among incident ordinary edges vu whose labels lie below tau_v, suppose at least one exists and let p(v) be the endpoint of the largest such label:

  lambda(vp(v)) = max{lambda(vu): lambda(vu)<tau_v}.

The lower facet of the v-coordinate crosses tau_v downward through lambda(vp(v)). If tau_{p(v)}>lambda(vp(v)), then before the crossing both thresholds lie above that label and no B-edge on vp(v) is present, while after the crossing

  tau_v < lambda(vp(v)) < tau_{p(v)}

would ADD v_out p(v)_in. This is forbidden by (TH.1). Therefore

  tau_{p(v)} < lambda(vp(v)) < tau_v,

so the current threshold graph contains

  p(v)_out v_in.                                           (TH.2)

Thus whenever v has any incident label below its cut, the immediately lower incident edge is already an active incoming edge of B_tau.

### 3. The nearest edge above every cut is an outgoing threshold edge

Dually, if some incident label lies above tau_v, let s(v) satisfy

  lambda(vs(v)) = min{lambda(vu): lambda(vu)>tau_v}.

Cross the upper v-facet upward through lambda(vs(v)). If tau_{s(v)}<lambda(vs(v)), the move would add s(v)_out v_in. By (TH.1) this is impossible. Hence

  tau_v < lambda(vs(v)) < tau_{s(v)},

and the current graph contains

  v_out s(v)_in.                                           (TH.3)

Therefore every nonterminal cut has a canonical active outgoing nearest-edge arc.

### 4. Physical threshold digraph and exact source/sink characterization

Let D_tau be the directed physical graph with arc u->v whenever u_out v_in belongs to B_tau. Every such arc satisfies tau_u<tau_v, so D_tau is acyclic.

By (TH.2), v has indegree zero in D_tau exactly when no incident edge label lies below tau_v, equivalently

  tau_v < min_{u!=v} lambda(vu).                            (TH.4)

By (TH.3), v has outdegree zero exactly when

  tau_v > max_{u!=v} lambda(vu).                            (TH.5)

Call these physical vertices threshold SOURCES and threshold SINKS respectively. Every other vertex has at least one canonical incoming and one canonical outgoing arc, supplied by its immediate lower and upper incident labels.

Because arcs strictly increase tau, D_tau has at least one source and at least one sink.

### 5. There are at most three poles on either side

A threshold source v has no incoming B_tau edge, so the right copy v_in is isolated. Every matching in B_tau leaves it unmatched. Since a maximum matching has size n-3, exactly three right copies are unmatched; hence

  1 <= |Sources(D_tau)| <= 3.                               (TH.6)

Dually a threshold sink has isolated left copy v_out, so

  1 <= |Sinks(D_tau)| <= 3.                                (TH.7)

Moreover every threshold source s and every threshold sink t are joined by a current threshold arc. Indeed sourcehood gives

  tau_s < lambda(st),

while sinkhood gives

  lambda(st) < tau_t.

Therefore

  s_out t_in in B_tau                                     (TH.8)

for EVERY source-sink pair. The pole sets span a complete directed bipartite source-to-sink grid.

### 6. The exact three-pole case

If there are exactly three threshold sources, their three isolated right copies already account for all right-side matching deficiency. Hence every maximum matching of B_tau saturates every non-source right copy. If there are exactly three threshold sinks, every maximum matching saturates every non-sink left copy.

In particular, when both pole sets have order three, every size-(n-3) matching compiles to a three-path increasing cover whose path sources are exactly the three threshold sources and whose path terminals are exactly the three threshold sinks. The six unmatched copies are forced by the threshold cell itself, not by a chosen representative.

If one pole set has size one or two, at least one of the three unmatched copies on that side is an INTERNAL DEFECT: an unmatched copy of a physical vertex that nevertheless has a canonical threshold edge on that side by (TH.2) or (TH.3).

Thus an edge-maximal optimal deficiency-three cell has only two global obstruction types:

1. THREE-POLE: the full deficiency is carried by three physical threshold sources and/or sinks; or
2. INTERNAL-DEFECT: some unmatched matching defect lies at a vertex possessing a canonical nearest-edge threshold incidence.          (TH.9)

### 7. Research role and fence

This normal form does not prove R888. A local edge-maximal cell can still be escaped by a multi-facet motion, and an internal defect need not be augmentable by its one canonical nearest-edge arc. The gain is a finite structural quotient for G22 Focus B: there is no diffuse local threshold obstruction. Every non-pole vertex is two-sidedly active in a canonical way, there are at most three source and three sink poles, all source-sink pairs are present, and any deficiency not literally carried by those poles is an internal alternating-reachability problem.

The next Hall target is therefore sharp: eliminate INTERNAL-DEFECT cells by alternating reachability/threshold exchange, or show that a THREE-POLE cell admits a global threshold deformation or matching recombination to deficiency at most two.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R932"
    },
    {
        "relation": "dependency",
        "revision_id": "R936"
    }
]
```