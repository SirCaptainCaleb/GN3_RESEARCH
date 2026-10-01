# Arbitrary Latin blow-ups lift base cycles to near-spanning route paths

## Statement

Let T be a fixed linear 3-graph containing a linear cycle C_s of length s>=3. Blow up each base vertex by q and replace every base triple independently by an arbitrary transversal design TD(3,q). Then the blow-up contains a linear path of length sq-o(q).

More precisely, after cyclically labeling one joint cluster X_0={a_0,...,a_{q-1}}, for q-o(q) consecutive obligations t one can choose pairwise internally resource-disjoint lifted s-edge routes R_t from a_t to a_{t+1}; these concatenate to one path.

Consequently, if T has v vertices and m edges, the full blow-up has qv vertices and q^2m edges and its normalized density at its first forbidden path length is at most
  m/(vs)+o(1).
In particular, for the four-cycle in AG(2,3), every arbitrary-Latin affine-plane blow-up has a path of length 4q-o(q), so its normalized density is at most 1/3+o(1). Thus arbitrary local Latin fillings cannot amplify the affine-plane construction above the one-third asymptotic coefficient.

## Body

Write the fixed base cycle as E_1,...,E_s. Let X_0,...,X_{s-1} be its successive joint clusters and P_1,...,P_s the private clusters. Label X_0={a_0,...,a_{q-1}} cyclically.

For each obligation t and each choice of one vertex in every intermediate joint cluster X_1,...,X_{s-1}, the s Latin squares determine uniquely an s-edge lifted route from a_t to a_{t+1}. The internal resources of this route are the chosen s-1 joint vertices and one private vertex in each P_i, hence 2s-1 resources in total. Thus every obligation has exactly q^{s-1} possible routes.

The route family is sparse in the sense needed for a matching argument. Fixing one internal resource removes one degree of freedom, so a resource vertex belongs to Theta(q^{s-2}) routes for each obligation. Any pair of resource constraints leaves at most s-3 free intermediate coordinates, and after the obligation coordinate is included the resulting pair-codegrees are O(q^{s-2}). For s=4 this specializes to the earlier 8-uniform route hypergraph: obligation degree q^3, resource degree q^3 after summing over obligations, and pair-codegree O(q^2)=o(q^3).

Fix p>0 and put h=floor((1-p)q). Independently reserve every vertex in each of the 2s-1 internal resource classes with probability p; call the remaining vertices main. Standard Janson lower-tail estimates for these fixed-uniformity route families give a partition for which, uniformly over the h prescribed obligations,
  # all-main routes
    =((1-p)^{2s-1}+o(1))q^{s-1},
  # all-reserve routes
    =(p^{2s-1}+o(1))q^{s-1}.
The same concentration, with one main resource fixed and the h obligations varying, gives main-resource degree
  ((1-p)^{2s-1}+o(1))q^{s-1}.
Every pair-codegree remains O(q^{s-2})=o(q^{s-1}).

Form the 2s-uniform auxiliary hypergraph whose vertices are the h obligation vertices together with the main vertices in the 2s-1 resource classes, and whose edges are the all-main lifted routes. It is asymptotically regular with negligible pair-codegrees. Pippenger's near-perfect matching theorem therefore gives a matching covering all but o(q) obligations. The chosen routes are pairwise disjoint in all internal resources.

Repair the remaining o(q) obligations greedily using only reserved resources. For each uncovered obligation there are Theta_p(q^{s-1}) all-reserve routes. After k=o(q) repairs only O_s(k) reserved resources have been consumed, and each consumed resource forbids only O(q^{s-2}) candidate routes for the next obligation. Hence the total forbidden count is o(q^{s-1}), so an unused all-reserve route remains. Main and repair routes are automatically mutually resource-disjoint.

We have now chosen one route R_t for every t=0,...,h-1. Since R_t runs from a_t to a_{t+1}, the routes concatenate in natural order. Consecutive routes meet exactly in their common prescribed X_0 endpoint, nonconsecutive routes use distinct X_0 vertices, and all internal resources are pairwise disjoint. Thus they form one linear path of length
  sh=s floor((1-p)q).
Letting p tend to zero sufficiently slowly gives sq-o(q).

This also subsumes the earlier four-cycle packing result: for s=4 the construction chooses q-o(q) internally disjoint four-edge laps, but the reserve repair strengthens the earlier path-forest conclusion by arranging all selected obligations consecutively and therefore stitching them into one path of length 4q-o(q).

Finally the full blow-up of T has |V|=qv and |E|=q^2m, so its edge/vertex density is mq/v. If ell_q is one more than its maximum path length, then ell_q>=sq-o(q), and therefore
  (|E|/|V|)/ell_q
    <= (mq/v)/(sq-o(q))
    = m/(vs)+o(1).
For AG(2,3), v=9,m=12 and s=4, yielding 1/3+o(1). More generally, a fixed-template arbitrary-Latin blow-up can beat one third only if its base template has circumference strictly below 3m/v.
