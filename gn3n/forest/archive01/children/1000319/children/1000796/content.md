# Path-complement defects record uncovered vertices but not path-cover disjointness

## Statement

For a tight path P in H write D(P)=V(H)-V(P). For any two tight paths P,Q, D(P)∩D(Q)=V(H)-(V(P)∪V(Q)); hence D(P) and D(Q) are disjoint exactly when the two path supports together cover V(H). This condition is necessary for P,Q themselves to be the two components of a path cover, but it is not sufficient: P and Q may overlap, while a path cover is a partition into disjoint supports, and deleting overlap vertices from a tight path need not preserve tightness. For a genuine deletion cover H-x=P|Q, one still has D(P)=V(Q)∪{x}, D(Q)=V(P)∪{x}, and D(P)∩D(Q)={x}. Thus complements of path supports record uncovered vertices faithfully but lose the essential overlap/disjointness constraint, so they are not by themselves an exact dual model for two-cover obstruction.

## Body

The identity D(P)∩D(Q)=V(H)-(V(P)∪V(Q)) is elementary. My earlier version incorrectly inferred a two-cover merely from D(P)∩D(Q)=∅. That inference loses the requirement that the two cover components have disjoint supports. If P and Q overlap, their union may cover all vertices while neither can necessarily be trimmed to remove the overlap: deleting an internal vertex of a tight path can create a new unchecked consecutive triple. Hence complement-disjointness detects coverage by two possibly overlapping path supports, not a path-cover partition. The deletion-cover calculation remains valid because there P and Q are genuinely disjoint and partition H-x. Any viable dual obstruction formulation therefore has to retain disjointness/ownership data, trimability, or an equivalent global constraint.
