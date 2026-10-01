# Deleting threshold-degree vertices leaves a universal path forest

## Statement

In the setting of 7de985881169, the induced subhypergraph H-D has edge set C and is a subhypergraph of every nonspecial witness path. Consequently H-D is a linear path forest: every nontrivial component is a subpath of a linear path, every vertex has degree at most two in H-D, and if c is the number of nonempty components then |E(H-D)|=(|V(E(H-D))|-c)/2<=|V(H)\D|/2. In particular every vertex v outside D has at least d_H(v)-2>=k-1 incident edges meeting D.

## Body

By 7de985881169, every edge avoiding D lies in every longest witness path P for any fixed nonspecial edge. Hence E(H-D) is a subset of E(P).

A subset of the edge set of a linear path has no intersections between nonconsecutive selected path edges. Each connected component of such a subset is therefore a linear path (with isolated selected edges allowed as one-edge paths). Thus H-D is a linear path forest and its maximum degree is at most two.

A t-edge linear 3-uniform path has exactly 2t+1 vertices. Summing over the c nonempty components of H-D gives
|V(E(H-D))|=2|E(H-D)|+c.
Hence
|E(H-D)|=(|V(E(H-D))|-c)/2<=|V(H)\D|/2.

Finally, if v∉D then d_H(v)>=k+1 by definition of D, while d_{H-D}(v)<=2. Therefore at least d_H(v)-2>=k-1 edges incident with v meet D.
