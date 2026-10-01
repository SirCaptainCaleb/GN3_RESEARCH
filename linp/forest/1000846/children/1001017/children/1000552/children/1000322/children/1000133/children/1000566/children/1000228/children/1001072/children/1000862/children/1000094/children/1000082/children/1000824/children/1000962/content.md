# Color-run accounting is the natural zero-slack near-spanning target

## Statement

In a zero-slack critical core, let a linear path P use:
- a forest-triple edges;
- b_1 threshold colors on exactly one DXX edge each;
- b_2 threshold colors on exactly two consecutive DXX edges each.
Assume no threshold color occurs in two separated places of P, as required by linearity. Then
|E(P)|=a+b_1+2b_2,
the number of D-vertices used by P is b_1+b_2,
and the number of X-vertices used is
2|E(P)|+1-(b_1+b_2).
In particular, if P uses all k threshold colors exactly once as color-runs, then
|E(P)|=k+a+b_2.
Thus constructing a forbidden P_ell with all colors used reduces to finding a color-run path with
a+b_2=ell-k.
For k=floor(2ell/3)+1, the required surplus ell-k is about k/2.

## Body

Every edge of a zero-slack core is either a forest triple contained in X or a DXX connector.

In a linear hypergraph path, a fixed threshold vertex d∈D can occur in at most two path edges, and if it occurs twice those two edges must be consecutive. Thus the DXX edges decompose uniquely into color-runs of length one or two. Let b_1,b_2 count those runs.

The total number of path edges is therefore
L=a+b_1+2b_2.

Each color-run uses exactly one D-vertex, and different runs must use distinct threshold vertices: if the same d occurred in two separated runs, the corresponding nonconsecutive hyperedges would intersect at d. Hence the number of D-vertices on P is
r=b_1+b_2.

A 3-uniform linear path with L edges has 2L+1 vertices. The remaining vertices of P lie in X, so the X-count is
2L+1-r
=2(a+b_1+2b_2)+1-(b_1+b_2).

If every threshold color is used as exactly one run, then r=k and
b_1+b_2=k.
Consequently
L=a+(b_1+b_2)+b_2
 =k+a+b_2.

Therefore an ell-edge path using all k colors exists exactly when one can arrange color-runs and forest triples so that
a+b_2=ell-k.

The residue-specific required surplus is:
- ell=3m, k=2m+1: ell-k=m-1;
- ell=3m+1, k=2m+1: ell-k=m;
- ell=3m+2, k=2m+2: ell-k=m.
Thus only about one third of the color runs need to be doubled/augmented by forest triples. This is substantially less demanding than a rainbow Hamilton path through the contracted forest triples and is the natural target suggested by the same-color double-jump lemma 4abe5aca5308.