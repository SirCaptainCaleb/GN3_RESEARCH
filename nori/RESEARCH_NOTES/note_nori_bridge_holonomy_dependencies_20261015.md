# Bridge-distance holonomy of critical repair dependencies

- Stable ID: note_nori_bridge_holonomy_dependencies_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: dependency, geometry, metric
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9473_1
- Updated session: session_nori_r9473_1
- Disposition: none
- Successor: none

## Related references

- subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths

## Research note

**Theorem (bridge-distance holonomy).** Fix a facet F of Q_n and let P_e be full antipodal geodesics oriented from F to its opposite facet, each crossing a bridge at y_e and having a single strictly internal minority pivot e in F. Define e->f if P_e traverses bar f in the opposite facet. For any edge e of direction i in F put R_y(e)={l!=i:e_l!=y_l}, and d_y(e)=|R_y(e)|, the distance from y to edge e. If e->f then R_{y_e}(e) union {i} is a subset of R_{y_e}(f), hence d_{y_e}(f)>=d_{y_e}(e)+1. Proof: dir f=k has not flipped before the bridge, so k is not in R_{y_e}(e). Any l in R_{y_e}(e) flips after e but before the bridge, hence bar f_l=y_e_l and f_l!=y_e_l. Direction i flips at e and cannot flip again, so bar f_i=y_e_i and f_i!=y_e_i. Thus the inclusion. For a directed cycle e_1->...->e_t->e_1, sum the inequalities and reindex to obtain t<=sum_s[d_{y_(s-1)}(e_s)-d_{y_s}(e_s)]<=sum_s d_H(y_(s-1),y_s), using the 1-Lipschitz property of edge-distance. No cycle can occur when all bridge positions coincide. Moreover, if e->f and f->e, y=y_e,z=y_f, i=dir e,k=dir f, then y_i!=z_i and y_k!=z_k. For any l outside i,k with y_l=z_l, the two inclusion relations show e_l=f_l. If this common bit disagrees with y_l, l must be traversed after e and before the bridge on P_e; if it agrees, l must be traversed after the bridge and before bar f. Therefore every step before e or after bar f occurs in a direction where y,z disagree, outside i,k. If a_e counts the steps before e and b_e those after bar f, d_H(y,z)>=2+a_e+b_e>=3. The two bridges have the same color, hence are not antipodal; d_H(y,z)<=m-1 with m=n-1. Sharpness: in Q5, bit4 facet direction, prescribe colors (0,1,0,0,0) on the rooted full geodesics (root,order)=(1,(2,0,4,3,1)) and (5,(2,1,4,3,0)). These prescriptions occupy seven compatible antipodal edge-pair orbits and can be completed arbitrarily. The minority pivots e=(0,4),f=(1,1) are internal; P_e contains bar f=(1,28), P_f contains bar e=(0,26). Their bridge positions 4 and3 in Q4 have Hamming distance3. This is a legal coloring but not claimed bad. The metric obstruction localizes any cyclic critical-repair interactions to differing bridge positions, beyond fixed-bridge collisions.
