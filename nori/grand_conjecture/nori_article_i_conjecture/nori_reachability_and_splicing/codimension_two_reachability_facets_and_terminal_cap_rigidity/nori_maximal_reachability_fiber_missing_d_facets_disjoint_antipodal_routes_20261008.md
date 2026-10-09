# Every occupied maximal-reachability facet fiber omits at least d antipodally symmetric facets

# Quantitative missing-facet bound for maximal-reachability antipodal fibers

Assume an antipodally odd binary UNDIRECTED edge coloring of Q_n has no monochromatic full antipodal geodesic. Let m<n be the global maximum monochromatic geodesic length; the top-rank extension lemma gives d=n-m>=2. Fix a size-m direction set U and projected endpoint antipodal pair {r,r⊕U}. Let C=C(U,r)⊆Q_d be the exterior-coordinate assignments whose U-facets contain a monochromatic geodesic joining that projected pair. As established in the terminal-fiber theorem, C is antipodally invariant, while no connected component of the induced cube graph Q_d[C] contains an antipodal pair.

**Theorem (d disjoint geodesics give d missing facets).** If C is nonempty, then
\[
|Q_d\setminus C|\ge 2\left\lceil\frac d2\right\rceil
=\begin{cases}d,&d\text{ even},\\d+1,&d\text{ odd}.\end{cases}
\]
Consequently
\[
|C|\le 2^d-2\left\lceil\frac d2\right\rceil .
\]
More precisely, for every t∈C there are d pairwise internally vertex-disjoint full antipodal geodesics in the exterior Q_d from t to \bar t, and EACH contains at least one absent vertex of C.

**Proof.** Write the d exterior coordinates in any cyclic order a_1,...,a_d. For j=1,...,d, take the antipodal geodesic G_j from t whose direction word is the cyclic rotation
\[
(a_j,a_{j+1},...,a_d,a_1,...,a_{j-1}).
\]
At rank k with 1<=k<=d-1, the vertices along these paths are t⊕S_{j,k}, where S_{j,k} is the cyclic arc of k consecutive coordinates beginning at a_j. For a fixed k<d, all these cyclic arcs are distinct. Different k produce distinct Hamming ranks. Thus the d paths have disjoint interiors.

Since C contains t and \bar t but no path inside C can connect them, every G_j must contain an interior vertex outside C. Their interior sets are disjoint, giving at least d absent vertices. Moreover Q_d\C is antipodally invariant because C is, so the number of absent vertices is even. The bound follows. QED.

**Consequences.** If m=n-2 then d=2 and at most two of the four parallel facets carry a given projected maximal label, recovering the exact adjacent-facet exclusion. If m=n-3 then d=3, at least four of the eight parallel facets omit that label, so every occupied maximal-support fiber has size <=4. More generally the theorem forces a uniform antipodal separator of cardinality at least d for EVERY projected maximal reachability label. A dimension-independent counting proof could compare this forced deficit over all U and endpoint pairs with an independently established lower bound on coverage by maximal monochromatic geodesics; such a coverage bound is not yet proved.

The theorem is phrased entirely in terms of uncolored existence of monochromatic geodesics in parallel facets.
