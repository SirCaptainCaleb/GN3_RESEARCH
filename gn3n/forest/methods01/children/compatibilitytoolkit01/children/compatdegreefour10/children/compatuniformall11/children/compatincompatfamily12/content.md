# Low compatibility degree yields large pairwise-incompatible deletion families

## Statement

Assume the low-degree branch of compatdegreefour10, so the compatibility graph G on m chosen deletion covers has maximum degree at most four. Then G is 5-colorable and hence contains an independent set I of size at least ceil(m/5). Equivalently, the chosen deletion covers indexed by I are pairwise incompatible. In particular, if m>=26 there are six pairwise incompatible chosen deletion covers; coloring each incompatible pair by whether it is support-incompatible or support-compatible but order-incompatible, Ramsey R(3,3)=6 gives three labels whose three pairwise incompatibilities all have the same broad type.

## Body

# Proof

A graph of maximum degree at most four is greedily 5-colorable. Therefore one color class has size at least ceil(m/5). Since a color class is independent in the compatibility graph, the corresponding deletion covers are pairwise incompatible.

If m>=26, then ceil(m/5)>=6. Choose six labels in one independent set. Every pair of their covers is incompatible. Color each pair red when the two covers are support-incompatible, and blue when they are support-compatible but order-incompatible. By the classical Ramsey theorem R(3,3)=6, among the six labels there is a monochromatic triangle.

Thus one obtains three chosen deletion covers whose three pairwise incompatibilities are uniformly support-incompatible, or three whose pairwise support partitions agree but whose path orders are pairwise incompatible.