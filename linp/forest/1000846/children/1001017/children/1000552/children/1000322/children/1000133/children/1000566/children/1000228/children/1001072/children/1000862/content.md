# Extremal threshold-set size yields a color-complete path-forest lift

## Statement

Assume the setting of ee2c9575cf8f with |D|=k, and put X=V(H)\D. Let P be the set of vertices of forest-degree one in H[X]. For every x∈P, d_H(x)=k+1 and for every d∈D there is a unique hyperedge {x,d,y_d} with y_d∈X. These k edges are all the edges through x meeting D, each contains exactly one D-vertex, and the vertices y_d are pairwise distinct. Consequently, if G is the simple graph on X in which xy is colored d whenever {d,x,y}∈E(H), then G is properly edge-colored by D and every x∈P has degree and color-degree exactly k, seeing every color once. Equivalently, for each d∈D the d-colored edges form a matching on X that saturates P.

## Body

By ee2c9575cf8f, when |D|=k the forest H[X] has no isolated vertices. Let x have d_{H[X]}(x)=1.

Since x∉D, d_H(x)>=k+1. Hence x is incident with at least k edges meeting D. On the other hand, distinct edges through x have disjoint sets of D-vertices: if two such edges both contained d∈D, they would share the pair {x,d}, contradicting linearity. Because D has only k vertices and every cross-edge contains at least one D-vertex, there are at most k cross-edges through x.

Thus x has exactly k cross-edges and d_H(x)=k+1.

The D-vertex sets used by these k cross-edges are k pairwise disjoint nonempty subsets of a k-element set D. Therefore each is a singleton and together they partition D. Hence for each d∈D there is exactly one edge f_d through x containing d, and f_d contains no other D-vertex. Write f_d={x,d,y_d}; then y_d∈X.

If d≠d', then y_d≠y_{d'}, since otherwise f_d and f_{d'} would share the two vertices x and y_d. Thus the y_d are pairwise distinct.

Define G on X by placing a graph edge xy of color d exactly when {d,x,y} is a hyperedge with one D-vertex. Linearity of H implies each color class is a matching and no pair xy receives two colors, so G is a properly edge-colored simple graph. The preceding paragraph shows that every forest-degree-one vertex x has exactly one incident edge of every color d∈D.