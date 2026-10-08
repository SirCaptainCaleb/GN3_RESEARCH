# Isoperimetry forces exponentially many missing exterior facets in each maximal-reachability fiber

# Exponential separator bound for antipodally split maximal-reachability fibers

Maintain the setup of the terminal-fiber theorem: assume a hypothetical counterexample to the antipodally odd UNDIRECTED edge-geodesic conjecture, with global maximum monochromatic-geodesic length m<n and deficit d=n-m>=2. For a fixed projected maximal endpoint pair in an m-dimensional U-facet, let C⊆Q_d be the set of exterior facet assignments supporting a monochromatic U-geodesic. C is antipodally invariant, and its occupied connected components are paired freely by antipodality. Write z=2^d-|C| for the number of missing facets.

**Theorem (isoperimetric antipodal gap).** If C is nonempty, then
\[
z\ \ge\ \max\left\{
2\left\lceil\frac d2\right\rceil,\ 
\frac{2^d}{2d+1}
\right\}.
\]
As z is even, it can be rounded UP to the next even integer. A stronger implicit bound valid for each actual z is
\[
d z\ \ge\ \frac{2^d-z}{2}
\log_2\!\left(\frac{2^{d+1}}{2^d-z}\right).
\]
In particular, no occupied maximal fiber can have all but o(2^d/d) of its exterior facets present as d tends to infinity. The bound holds for arbitrary antipodally invariant cube vertex subsets whose induced connected components are antipode-free; it is independent of the details of the original edge coloring after the terminal-fiber constraint is established.

**Proof.** Choose exactly one component from each antipodal pair of components of Q_d[C], and let A be the union of these selected components. Then the complementary selected union is bar A, C=A disjoint_union bar A, and |A|=a=(2^d-z)/2. Crucially there are NO cube graph edges between A and bar A; such an edge would place two selected components into one connected component. Thus every cube edge from A to its complement has its other endpoint in Z=Q_d\C, and
\[
|\partial_E A|\le d|Z|=dz.
\]

We prove the standard binary-cube edge expansion estimate using elementary induction:
\[
|\partial_E W|\ge |W|\log_2(2^d/|W|)
\quad\text{for every }W\subseteq Q_d.
\]
For d=0 it is immediate. Decompose W into its slices W_0,W_1⊆Q_{d-1}, with sizes a_0,a_1 and a=a_0+a_1. Its boundary size equals the two within-slice boundaries plus |W_0 triangle W_1|, and the latter is at least |a_0-a_1|. Applying induction yields at least
\[
a_0\log_2(2^{d-1}/a_0)+a_1\log_2(2^{d-1}/a_1)+|a_0-a_1|.
\]
Write p=a_0/a. The displayed quantity equals
\[
a\log_2(2^d/a)+a\,[H_2(p)+|2p-1|-1],
\]
where H_2(p)=-p log_2 p-(1-p)log_2(1-p) (with 0 log 0=0). The bracket is nonnegative because concavity of binary entropy gives H_2(p)≥2 min(p,1-p)=1-|2p-1|. This completes the induction.

Apply this expansion estimate to A, obtaining dz≥a log_2(2^d/a), which after substituting a=(2^d-z)/2 gives the implicit inequality. Because a≤2^{d-1}, the logarithm is at least 1, so dz≥(2^d-z)/2, hence z(2d+1)≥2^d. The independent d-vertex-disjoint-antipodal-routes lemma gives z≥d, and antipodal invariance gives z even, hence z≥2 ceil(d/2). QED.

**Topological meaning.** Any hypothetical counterexample forces every nonempty parallel-facet label fiber at the globally maximum reachability rank to be missing a quantitatively large antipodal separator. In high codimension d this is exponentially many absent facet positions (at least order 2^d/d), strengthening the previous d-missing-facet bound. To prove grand closure by double counting one still needs an independent lower bound on coverage or overlap across different U and endpoint labels; this is the remaining open link.
