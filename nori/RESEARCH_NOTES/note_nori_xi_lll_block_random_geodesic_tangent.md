# Lovasz local lemma block-random geodesic idea

- Stable ID: note_nori_xi_lll_block_random_geodesic_tangent
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: LLL, antipodal-cube, random-geodesic, square-exchange, research-tangent
- Lifecycle: active
- Epistemic status: open
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Exploratory Lovász-local-lemma (LLL) tangent for the edge-colored antipodal cube; preserve as a research note only, not a theorem toward unrestricted NORI1.

Fix any antipodally odd 2-coloring c of the edges of Q_n. Uniformly choose a starting vertex x and a permutation of coordinate directions. For each j=1,...,n-1 let E_j be the event that the jth and (j+1)st geodesic edges disagree. The simultaneous avoidance of all E_j is a monochromatic full antipodal geodesic. The naive randomization does NOT have a bounded dependency graph: the vertex before turn j depends on all earlier chosen directions.

Let t(v) be the number of color-one incident cube edges at v. For uniformly random starting x and coordinate permutation, the turn vertex at any fixed j is uniform on Q_n, and its ordered incoming and outgoing directions are uniform among all distinct directions, so
 P(E_j)=2^{-n} Σ_{v∈Q_n} [2 t(v)(n−t(v))/(n(n−1))].
This gives a local-star-bias statistic but can be approximately 1/2 for balanced star colorings; no LLL conclusion follows without additional structural bounds.

A conditional block-randomized criterion: partition the coordinate set into disjoint blocks B_1,...,B_m; fix the root and block order but independently uniformly permute directions INSIDE each block. Each block has fixed entry and exit vertices. Let A_i be the event that its internal path has a color change, and F_i that the last edge of block i disagrees with the first edge of block i+1. Each A_i uses one random block choice and each F_i uses two adjacent block choices; every bad event is independent of all but at most four other bad events. Thus, by symmetric LLL, if all these bad-event probabilities are at most 1/(5e), there exists a choice of internal block permutations with no internal or seam disagreements, i.e. a monochromatic full antipodal geodesic. This is only a sufficient criterion and is not shown to hold for an arbitrary coloring or partition/root.

Possible future approach: use lopsided permutation LLL or independent local square reroutings with a verified repair-density hypothesis from Article XI's square-curvature and circuit–cocircuit geometry. The existence of a dependency graph and a uniform bad-event probability bound are the unresolved bottlenecks. Random square repairs cannot be assumed independent without proof. Do not promote this tangent to the manuscript absent an unrestricted implication; priority remains pointed-matroid duality and legal gallery exchange.
