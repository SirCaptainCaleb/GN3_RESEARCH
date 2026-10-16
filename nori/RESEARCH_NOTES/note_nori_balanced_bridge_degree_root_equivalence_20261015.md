# Degree-conditioned favorable-root characterization equivalent to unrestricted NORI1

- Stable ID: note_nori_balanced_bridge_degree_root_equivalence_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: balanced, bridge, root-reachability, closure-equivalence
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let d=2m-1, m>=2. Color the undirected edges of Q_d by an arbitrary binary coloring f, with z(u) the number of incident color-zero edges at u. Consider the degree conditions
\[
z(u)\in\{m-1,m\},\qquad z(u)+z(\bar u)=d
\quad\text{for every }u.
\tag{D1}
\]
Set L(f)=\{u:z(u)=m-1\} and write A_0(f) for roots admitting a full antipodal geodesic with color word 0^*1^*.

**Theorem 1 (balanced odd bridge correspondence).** With a distinguished bridge direction b, vertex-balanced antipodally odd edge colorings c of Q_(d+1) are in bijection with ordinary colorings f of Q_d satisfying (D1). The maps are
\[
c_i(u,0)=f_i(u),\qquad c_i(u,1)=1-f_i(\bar u)\quad(i\in[d]),
\qquad
c_b(u,t)=h(u):=z(u)-(m-1).
\tag{D2}
\]
Moreover c has a monochromatic full antipodal geodesic if and only if
\[
\boxed{A_0(f)\cap L(f)\ne\varnothing.}
\tag{D3}
\]

*Proof.* Suppose c is balanced and odd. Antipodal oddness prescribes every horizontal upper-facet color from the lower-facet coloring f. Put h(u)=c_b(u,t), independent of the bridge bit. The zero degree at the lower vertex (u,0) is z(u)+1-h(u)=m, hence z(u)=m-1+h(u). Global antipodal oddness makes h(\bar u)=1-h(u), giving z(u)+z(\bar u)=2m-1=d. Thus (D1) and (D2) follow. Conversely, if f satisfies (D1), then h(u)=z(u)-(m-1) takes values in {0,1} and satisfies h(\bar u)=1-h(u). The extension (D2) is undirected and antipodally odd. Its lower zero degree is m; the upper horizontal zero degree at (u,1) is d-z(\bar u)=z(u), so the upper total zero degree is again z(u)+1-h(u)=m. This establishes the bijection.

Because c is antipodally odd, it suffices to consider a color-zero full geodesic. Orient such a geodesic so its unique bridge crossing travels from (u,0) to (u,1); then its bridge edge is zero, so h(u)=0 and u belongs to L(f). Reverse the lower horizontal segment to obtain a zero-colored facet path starting at u. Apply antipodal translation within the lower cube to the upper horizontal segment, then reverse it; the resulting facet path continues from the lower segment's endpoint to bar u and is one-colored. The concatenation uses each of the d horizontal directions once and has word 0^*1^*. Thus u belongs to A_0(f).

Conversely, given u in A_0(f) intersect L(f), choose a nondecreasing full facet path from u to bar u and split it into its zero prefix u->w and one suffix w->bar u. In the full cube, traverse the zero prefix backwards from (w,0) to (u,0), cross the zero bridge above u, and traverse the antipodally translated reverse of the one suffix within the upper facet, ending at (bar w,1). The final vertex is antipodal to the initial one, all d+1 directions occur once, and every edge has color zero. This proves (D3). QED.

**Theorem 2 (degree-conditioned root principle equivalent to unrestricted NORI1).** Unrestricted NORI1 holds if and only if, for every m>=2 and every undirected binary edge coloring f of Q_(2m-1) satisfying (D1),
\[
\boxed{\exists\,u:\ z(u)=m-1\ \text{and some full }0^*1^*\text{ geodesic starts at }u.}
\tag{D4}
\]

*Proof.* If NORI1 holds, reconstruct c from any f via (D2) and apply (D3), proving (D4). Conversely assume (D4). Given a vertex-balanced antipodally odd c on Q_(2m), its lower facet f satisfies (D1) by Theorem 1, so (D4) and (D3) give a monochromatic full geodesic. The established counterexample-preserving reduction from arbitrary legal colorings to vertex-balanced even-dimensional legal colorings then proves unrestricted NORI1. QED.

**Closure implication.** (D4) localizes the outstanding universal forcing statement to one half of the vertices, selected by their horizontal zero degree. The zero-degree threshold is local, whereas membership in A_0(f) records full direction-simple reachability. The degree sum requirement z(u)+z(bar u)=d is indispensable to the balanced-extension bijection. The theorem supplies a graph-degree formulation for a possible Hall or extremal argument; it does not establish (D4).

**Corollary (positive degree-weighted two-phase trace).** Let R and B be the adjacency matrices of the color-zero and color-one subgraphs of f, let P be antipodal translation on Q_d, and let D_L be diagonal with D_L(u,u)=m-z(u) in {0,1}. If Z_0(c) counts *rooted oriented* color-zero full geodesics in the balanced odd extension (D2), then
\[
\boxed{
Z_0(c)=2\sum_{u\in L(f)}N^\uparrow_f(u)
=2\sum_{a=0}^d\operatorname{tr}\!\left(D_L R^aB^{d-a}P\right),
}
\tag{D5}
\]
where N^\uparrow_f(u) counts rooted full paths from u with nondecreasing color word.

*Proof.* Every all-zero full path in c has a unique orientation crossing its bridge from the lower facet to the upper. The seam conversion in Theorem 1 is a bijection between such orientations and rooted nondecreasing full paths of f starting in L(f); the reverse orientation doubles the count. The rank a of the seam is determined by the number of zero-colored edges in the facet path, including a=0 or d for monochromatic words. The summand (R^a B^{d-a})_(u,bar u) counts all paths with a zero steps followed by d-a one steps. Since their length equals the Hamming distance d, each is a full geodesic. Summing over L(f) and a proves the trace formula. QED.

In particular the degree-conditioned root principle (D4) is equivalent to strict positivity of the nonnegative matrix expression on the right of (D5), under (D1).
