# The nine-set of a trapped local 4|5|a minimum has only 4|5 two-covers

## Statement

Let H be a boundary tournament and let C=X|Y|P be a Phi-minimal three-cover in a trapped connected component of the pairwise-repartition graph, with |X|=4, |Y|=5, and |P|=a>=7. Put W=X union Y. Then H[W] is non-Hamiltonian, and every two-cover of H[W] has component-order multiset {4,5}. Equivalently H[W] has no Hamiltonian induced subset of order at least six. Thus the local 4|5|a basin contains a rigid nine-vertex residue whose maximum tight-path order is exactly five.

## Body

Apply the product-bound theorem 0645d2daab03 to the pair X|Y of orders 4,5 and the third path P of order a>=7. Its threshold is (4-3)(5-3)+4=6, so a>6 satisfies the hypothesis. Thus every two-cover of W=X union Y has both sides at least four. Since |W|=9, its only possible two-cover order multiset is {4,5}. The same theorem excludes every Hamiltonian support of order at least |W|-3=6. The displayed path Y has order five, so the maximum tight-path order in H[W] is exactly five. Trappedness also excludes a Hamilton path on all of W, since merging X|Y would produce a spanning two-cover with P. This replaces the former separate normalization-and-descent proof by the uniform product bound.
