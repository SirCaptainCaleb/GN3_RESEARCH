# A third of the labels share one trapped reconfiguration component unless four covers realize a classified incompatibility pattern

## Statement

Let H be a minimum counterexample, let D be a set of m>=4 deletion labels, choose one deletion cover F_v of H-v for each v in D, and form their compatibility graph G. Then at least one of the following holds.

1. Some connected component K of G has |K|>=ceil(m/3). Consequently one trapped pairwise-repartition component contains a canonical state with a three-vertex middle path associated with every label in K.

2. Three chosen deletion covers have all three pairwise incompatibilities of one broad type: either all three pairs are support-incompatible, or all three pairs are support-compatible but order-incompatible.

3. Four chosen deletion covers are pairwise incompatible and their support-compatibility graph is a four-vertex path P4.

4. Four chosen deletion covers are pairwise incompatible and their support-compatibility graph is two disjoint edges 2K2.

Thus, outside the uniform-triple and two classified mixed four-cover interfaces, at least one third of any chosen deletion-cover family is synchronized inside one trapped pairwise-repartition component.

## Body

If G has at most three connected components, one of them has order at least ceil(m/3), and eb169fd62ac1 gives outcome 1.

Suppose G has at least four connected components. Choose one label from each of four distinct components. Their chosen deletion covers are pairwise incompatible, because no compatibility edge joins distinct connected components.

Since H is a minimum counterexample, |V(H)|>10 by mincex01, so there is a vertex outside these four labels. If three of the four covers have their three pairwise incompatibilities all of one broad type, outcome 2 holds.

Otherwise the four covers satisfy the hypotheses of compatfourpattern26. Their support-compatibility graph is therefore, up to relabeling, either P4 or 2K2, giving outcome 3 or outcome 4.

Hence one of the four outcomes always holds. ∎