# Every vertex deletion of a 12-vertex 5-regular linear triple system has a spanning P5

## Statement

Let H be a 12-vertex 5-regular linear 3-uniform hypergraph. Then for every vertex z, the deletion H-z contains a spanning five-edge linear path.

## Body

Fix z in V(H). Since H is 5-regular, |E(H)|=12*5/3=20, and deleting z removes exactly five edges. Hence H-z has 11 vertices and 15 edges.

Suppose H-z contained no P_5^(3). The certified exact P_5 extremal theorem says that an 11-vertex P_5-free linear triple system has at most 15 edges, with equality only for the unique extremal system G_0. Thus H-z would have to be isomorphic to G_0.

But the degree sequence is incompatible. In a 5-regular 12-vertex linear triple system, each vertex z is paired inside its five incident triples with exactly ten of the other eleven vertices, leaving a unique uncovered mate z*. After deleting z, the mate z* loses no incident edge and still has degree 5, while every other remaining vertex loses exactly the unique edge containing its pair with z and hence has degree 4. Therefore
  deg(H-z) = (5,4,4,4,4,4,4,4,4,4,4).

On the other hand, in the standard one-factorization representation of the P_5 extremal G_0, the six base vertices have degree 5 and the five color-center vertices have degree 3, so
  deg(G_0) = (5,5,5,5,5,5,3,3,3,3,3).

The degree sequences differ, contradiction. Hence H-z contains a P_5. Since a five-edge linear 3-uniform path uses 11 vertices and H-z itself has 11 vertices, this P_5 is spanning in H-z.

As z was arbitrary, every one-vertex deletion of H contains a spanning P_5.
