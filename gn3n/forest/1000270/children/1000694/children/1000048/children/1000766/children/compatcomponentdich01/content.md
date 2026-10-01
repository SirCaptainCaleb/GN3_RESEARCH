# Compatibility components force a large common reconfiguration family or a uniform incompatibility triple

## Statement

Let H be a minimum counterexample, let D be a set of m>=5 deletion labels, and choose one deletion cover F_v of H-v for each v in D. Form the compatibility graph G on D. Then at least one of the following holds.

1. Some connected component K of G has |K|>=ceil(m/4). Consequently one component of the pairwise-repartition graph on spanning covers with at most three components, containing no cover with at most two components, contains a canonical state with a three-vertex middle path associated with every label in K.

2. There exist three labels a,b,c in D such that F_a,F_b,F_c are pairwise incompatible of one uniform broad type: either all three pairs are support-incompatible, or all three pairs are support-compatible but order-incompatible.

In particular, if outcome 2 is absent, a linear fraction of any chosen deletion-cover family is synchronized inside one trapped pairwise-repartition component.

## Body

If G has at most four connected components, one of them has order at least ceil(m/4). Outcome 1 then follows directly from eb169fd62ac1.

Suppose instead that G has at least five connected components. Choose one label from each of five distinct components, and consider the corresponding five deletion covers. No two chosen labels are adjacent in G, so the five covers are pairwise incompatible.

Because H is a minimum counterexample, |V(H)|>10 by mincex01. Hence there is at least one vertex outside the five chosen labels. The hypotheses of compatfiveuniform25 therefore apply. That theorem yields three of the five covers whose three pairwise incompatibilities have one common broad type: either all three pairs are support-incompatible, or all three are support-compatible but order-incompatible. This is outcome 2.

Thus one of the two outcomes always holds. ∎