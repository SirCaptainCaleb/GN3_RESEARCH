# A unique source-rail intersection forces reciprocal terminal contacts

## Statement

Let e_i={x_i,v,u_i} and e_j={x_j,v,u_j} be two source-clean 0-1-1 edges through the same assigned terminal v, and let Q_i,Q_j be their maximum source paths ending at x_i,x_j. Assume each foreign edge meets the other source rail, as in the two-rank source-rail block. If V(Q_i) intersect V(Q_j) is a singleton, then Q_i meets e_j at u_j and Q_j meets e_i at u_i. Equivalently, if either cross-contact is a source hit, the two source rails have at least two common vertices.

## Body

Suppose Q_i meets e_j at x_j. Since Q_j ends at x_j, the vertex x_j lies on both source rails. If it were their unique common vertex, the universal aligned-joint lemma would force x_j to be a path joint of Q_j. But x_j is the designated last vertex of Q_j and, in the clean source path witnessing the ascending edge e_j, occurs only on the last path edge rather than as an internal joint. Thus x_j cannot be the unique rail intersection. Therefore a uniquely intersecting pair cannot have the contact Q_i with e_j at x_j, so its mandatory contact is u_j. The same argument with i and j reversed forces the other contact to be u_i. Hence unique rail intersections are precisely reciprocal-terminal cross-contact states.
