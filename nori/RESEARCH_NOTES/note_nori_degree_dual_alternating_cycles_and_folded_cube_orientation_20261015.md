# Antipodal degree duality, alternating-cycle normal form and universal degree-pattern realization

- Stable ID: note_nori_degree_dual_alternating_cycles_and_folded_cube_orientation_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: balanced, bridge, alternating-cycles, folded-cube, degree-realization
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let d=2m-1>=3, and let f be an undirected binary edge coloring of Q_d. Write z_f(u) for its incident color-zero degree, tau for the antipodal involution, and f#(e)=1-f(tau e). Let M_a(f,u) count rooted full antipodal geodesics with color word 0^a 1^(d-a).

**Theorem 1 (dual preservation of roots and seam reversal).** For every f,u,a,
M_a(f#,u)=M_(d-a)(f,u). Consequently A_0(f#)=A_0(f), where A_0 is the set of roots admitting 0*1* full geodesics.

*Proof.* Given a rooted full antipodal geodesic, reverse its vertex sequence and apply the antipodal involution. Its endpoints are again u and bar u, and its new color word under f# is the reverse and bitwise complement of the original word. The transformation is involutive. QED.

**Theorem 2 (degree-duality alternating circuits).** The relation z_f(u)+z_f(bar u)=d for every u is equivalent to z_f#(u)=z_f(u) for every u. Under this relation, the set D={e:f(e)=f(tau e)} has equally many f-zero and f-one incident edges at every vertex. Consequently D admits a partition into edge-disjoint color-alternating cycles. Flipping the edge colors along each cycle successively transforms f into f# while preserving the full vertex-degree sequence at every stage.

*Proof.* The f#-zero degree at u is d-z_f(bar u). On D the color-dual reverses f, and outside D it agrees with f. Equality of degrees forces the incident f-zero and f-one counts on D to agree. Orient f-zero D-edges from even cube vertices to odd, and f-one D-edges from odd to even. The resulting directed graph has equal indegree and outdegree at each vertex, so decomposes into directed cycles, which alternate colors because the cube is bipartite. Switching each such cycle preserves all degrees and exhausts D. QED.

**Theorem 3 (universal odd realization of near-half degree assignments).** Suppose h:Q_d->{0,1} satisfies h(bar u)=1-h(u), and precisely 2^(d-2) of the even-parity cube vertices have h(u)=1. Then there exists an antipodally odd undirected edge coloring g of Q_d with
z_g(u)=m-1+h(u) at every vertex.

*Proof.* As d is odd, each antipodal vertex orbit has a unique even representative. Let G=Q_d/<tau>, a d-regular folded cube with N=2^(d-1) vertices. Assigning opposite colors to the two edges in each antipodal edge orbit is equivalent to orienting the associated edge of G: its source is the orbit whose even representative is incident with the selected zero edge. Thus the zero-degree of an even representative equals its outdegree.

For v in V(G) with even representative u, put t(v)=2h(u)-1, and prescribe r(v)=(d+t(v))/2=m-1+h(u). Then sum_v t(v)=0 by the parity-balance assumption, and sum_v r(v)=|E(G)|. For any U subset V(G), let delta(U) be its edge boundary. Its full inverse image S in Q_d is antipodally invariant, has |S|=2|U|, and |boundary_Qd S|=2|delta(U)|. The cube edge-isoperimetric bound |boundary_Qd S| >= min(|S|,2^d-|S|) implies
|delta(U)| >= min(|U|,N-|U|).
Since every t(v) is +-1 and its total sum vanishes,
|sum_(v in U) t(v)| <= min(|U|,N-|U|) <= |delta(U)|.
It follows that
sum_(v in U)r(v)-|E_G(U)|=(|delta(U)|+sum_(v in U)t(v))/2>=0
for every U. The standard integral-flow criterion for orientations with prescribed outdegrees therefore provides the required orientation. Its antipodally odd coloring has the prescribed zero degrees at even representatives; at odd representatives the antipodal symmetry gives d-r(v)=m-1+h(bar u). QED.

**Corollary 4 (connectedness at fixed degree profile).** Any two cube edge colorings with identical incident zero degrees are related by a sequence of alternating-cycle color switches preserving all those degrees. Indeed the symmetric difference of their zero-edge sets has equal numbers of edges of each type at every vertex; directing the two types in opposite bipartition directions gives an Eulerian graph, whose directed cycles alternate types. In particular, every degree-admissible f of the balanced-bridge formulation is connected by such switches to some antipodally odd coloring with its same degrees, by Theorem 3.

**Relevance to closure.** The low-degree set L={u:z_f(u)=m-1} can be any antipodal transversal with equal even and odd counts. Its vertex pattern alone therefore supplies no additional feasibility restriction; a proof of the degree-conditioned root principle must exploit incidence of colored edges. The dual operation preserves every favorable root and its degree data, while individual alternating-cycle switches need not preserve favorable roots. The connected exchange space provides a precise possible extremal program, without proving grand closure.
