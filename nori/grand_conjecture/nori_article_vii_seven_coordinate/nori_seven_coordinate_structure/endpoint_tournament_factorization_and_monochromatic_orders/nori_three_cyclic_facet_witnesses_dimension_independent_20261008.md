# Three compatible cyclic facet witnesses force full coordinate-order closure

Let h be any binary labeling of ordered triples of distinct elements of an n-element direction set. Position independence is assumed; reversal oddness is unnecessary for the following criterion. Fix a cyclic direction order p_0,...,p_{n-1}, with subscripts modulo n, and let w_i=h(p_i,p_{i+1},p_{i+2}). A full rotation at i has n-2 window colors w_i,...,w_{i+n-3}. Its facet deletion has n-3 colors w_i,...,w_{i+n-4}, obtained by traversing n-1 directions and omitting the last direction of that rotation. Call a word good when it has at most one change.

**Theorem (three cyclic facet witnesses).** If n>=7 and at least three of these n facet deletions are good, at least one full rotation is good.

More precisely, if every full rotation is bad, the circular word w either has at least six changes and no good facet deletion, or has exactly four changes and at most two good facet deletions. For n=6 the corresponding maximum is four good deletions.

**Proof.** Put d_i=w_i XOR w_{i+1}; let K be the number of 1s in the circular difference word d. K is even. A full rotation is bad precisely when its interval of n-3 consecutive differences contains at least two 1s. A good facet deletion has at most one 1 in its n-4 consecutive differences.

Assume all full rotations are bad. Then every good facet deletion has exactly one internal 1: zero internal 1s would yield a good full rotation on appending one difference. Moreover the differences immediately before and after its internal interval must both equal 1, because extending at either end must produce at least two changes. The four differences outside a good facet interval account for all other changes. Hence K<=5, and evenness gives K<=4. K=0 or K=2 contradicts badness of every full rotation: with two changes, start an interval immediately after either change to obtain at most one change, since the interval omits at least three differences. Thus a good facet deletion forces K=4.

Write delta_1,...,delta_4 for the positive cyclic gaps between these four changes; their sum is n. A good deletion corresponds exactly to a pair of consecutive gaps whose sum is n-3. Indeed, its outside bounding changes lie n-3 difference positions apart and it has exactly one intervening change. Conversely, such a gap pair determines the good deletion uniquely.

Three good deletions would give three of the four equalities delta_i+delta_{i+1}=n-3. Any three form a consecutive chain around the four-gap cycle, forcing delta_1=delta_3 and delta_2=delta_4 after cyclic relabeling. Consequently n=sum delta_i=2(n-3), so n=6. This is impossible for n>=7. Therefore there are at most two good deletions. If there is no good deletion, the count is zero; K is at least four, and if K is four this is still covered by the second alternative. QED.

**Dimension-six sharpness.** The circular word 001001 has four switches. Every full four-color rotation is bad, while four of its six three-color facet deletions are good. Thus the n>=7 threshold in the three-witness theorem is necessary at the word level.

**Counting corollary.** If h has no good full n-order, and n>=7, the total number of good (n-1)-orders over all n omitted directions is at most 2(n-1)!. Each cyclic direction order contributes exactly n facet orders, every facet order belongs to exactly one such cycle, and there are (n-1)! cycles. Thus an average good-order proportion exceeding 2/n across the n coordinate facets forces closure.

**Face-dependent extension.** For a general ordered-three-face coloring, a cyclic direction order is followed from a starting vertex for 2n moves, changing each direction twice and returning to the start. Let w_0,...,w_{2n-1} be its ordered-face window colors. This circular trace has length N=2n. Set L=n-3. If every full n-move segment is bad, and G of its (n-1)-move facet segments are good, then
G L <= 2N,
and hence G<=floor(4n/(n-3)).

To prove the bound, let the positive cyclic gaps between the changes of w be delta_1,...,delta_K, summing to N. Badness of every full segment implies delta_i+delta_{i+1}<=L: an interval of L differences immediately after a change must contain the next two changes. A good facet segment has exactly one internal change and both bounding differences equal 1, so it corresponds exactly to a gap pair with sum L. Summing those equalities over all G good segments counts each positive gap at most twice; therefore G L<=2 sum delta_i=2N. In particular, for n>=16, five good facet segments on one doubled antipodal coordinate cycle force a good full segment. This argument uses no coloring symmetry.

**Research frontier.** The criterion gives an all-dimensional target for facet transfer. For the coordinate-only reversal-odd problem, it suffices to construct three good facet orders lying on one common cyclic direction order. Existence of a separately chosen good order in each facet does not yet provide this compatibility. For face-dependent NORI, the analogous target is more than floor(4n/(n-3)) compatible good facet segments on one doubled antipodal cycle. These are proved sufficient conditions; constructing the required compatible family remains open.

**Verification.** The switch-gap proof was checked against every circular binary word of length n for n=6,...,12; when every full rotation failed, the maximum good-deletion count was four at n=6 and two at each tested n>=7. The proof establishes the dimension-independent statement.
