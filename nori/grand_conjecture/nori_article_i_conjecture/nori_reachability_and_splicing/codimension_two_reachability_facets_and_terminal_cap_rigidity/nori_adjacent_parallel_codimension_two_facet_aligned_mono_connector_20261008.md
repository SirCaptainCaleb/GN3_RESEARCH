# Aligned monochromatic geodesics in adjacent codimension-two facets force full antipodal closure

# Adjacent parallel (n-2)-facet monochromatic geodesics with matching antipodal endpoints force closure

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n, n>=3. Fix distinct directions a,b and U=[n]\{a,b}. Consider two adjacent U-dimensional parallel facets F_0,F_1, whose exterior (a,b) bits differ only in direction a. Suppose each facet contains a monochromatic antipodal *U-geodesic* joining the SAME projected unordered antipodal endpoint pair \(\{r,\bar_U r\}\subset Q_U\). The respective internal coordinate orders and colors may differ.

**Theorem (two-facet synchronization).** Under these hypotheses Q_n contains a monochromatic FULL n-edge antipodal geodesic.

**Proof.** Reverse either U-geodesic if needed, so their oriented roots are x and y=x⊕e_a and their endpoints are z=x⊕U, w=y⊕U=z⊕e_a. Let the geodesic colors be q and r (each a bit). Suppose no monochromatic full geodesic exists. By the standard top-rank extension lemma, there is no monochromatic (n-1)-edge geodesic anywhere: an (n-1)-geodesic has a unique missing direction and its two endpoint extension edges are antipodal with opposite colors, so its own color matches at least one of them.

Thus BOTH missing-coordinate edges (a and b) incident to x and z have color 1-q, since either matching q would extend the first path to a monochromatic (n-1)-geodesic. Similarly both missing-coordinate edges incident to y and w have color 1-r. The a-edge {x,y} is shared by the two root endpoints, so 1-q=1-r, hence q=r. The b-edge {y,y⊕e_b} has color 1-q, by the second path's root blockage. Its antipodal edge is {z,z⊕e_b}: indeed bar(y)=z⊕e_b and bar(y⊕e_b)=z. By antipodal oddness this latter b-edge has color q, contradicting blockage of the first path's endpoint z. Thus a monochromatic full antipodal geodesic exists. \(\square\)

**Uncolored reachability-label interpretation.** For each U-parallel facet F indexed by exterior bits t∈{0,1}^{\{a,b\}}, let
\[
M_U(t)=\{\{r,\bar_Ur\}:\text{an undirected monochromatic full U-geodesic in facet }F_t\text{ joins these projected endpoints}\}.
\]
Colors are NOT part of these sets. If M_U(t) and M_U(t⊕e_a) have a common label, grand closure follows by the theorem. Antipodal oddness gives M_U(t⊕e_a⊕e_b)=M_U(t) (the two paths' colors are complemented but existential monochromaticity is preserved). Thus there are only two independent sets of projected endpoint-pair labels, namely M_U(00)=M_U(11) and M_U(01)=M_U(10), and their intersection forces closure. A hypothetical counterexample requires these two sets to be disjoint for EVERY U. This is a concrete compatible-reachability-label coincidence across two adjacent facet charts.

**Scope.** The lemma concerns the original antipodally odd EDGE-colored proving ground. A spanning U-geodesic in a facet is a special reachability witness; the proof uses undirected edge-color preservation under path reversal and the single exposed-edge completion rule. For ordered-three-face NORI, crossing a facet seam creates additional ordered windows, so the same synchronization cannot be transferred without bridge-memory conditions.
