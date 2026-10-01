# A nonregular minimal counterexample has at least k threshold-degree vertices

## Statement

In an edge-minimal counterexample at threshold k=floor(2ell/3)+1, let D be the degree-k vertices. If V(H)\D is nonempty, then |D|>=k. Indeed every higher-degree vertex has at least k-1 cross-edges into D, which hit distinct D-vertices by linearity; equality |D|=k-1 would force every vertex of the path forest H-D to have degree two, impossible. If |D|=k, then H-D has no isolated vertices, every path endpoint has degree k+1 and its k cross-edges hit every vertex of D.

## Body

Let k=floor(2ell/3)+1, D={v:d_H(v)=k}, and X=V(H)\D. By 324fa959c567, H[X]=H-D is a linear path forest and every v in X has at least k-1 incident edges meeting D.

Fix v in X. Distinct edges through v have disjoint non-v vertex sets by linearity. Therefore two distinct edges through v that meet D cannot use the same vertex d in D; otherwise both hyperedges would contain the pair {v,d}. Consequently the edges through v meeting D inject into D. Hence
  |D| >= k-1
whenever X is nonempty.

We can exclude equality. Suppose |D|=k-1. Then every v in X has at most k-1 incident edges meeting D, hence exactly k-1 such edges. Since v notin D, d_H(v)>=k+1. Therefore
  d_{H[X]}(v) >= (k+1)-(k-1)=2.
But H[X] is a path forest, so d_{H[X]}(v)<=2. Thus every v in X has degree exactly 2 in H[X].

A nonempty finite path forest cannot have every vertex degree 2: every nonempty path component has vertices of degree at most 1 (indeed two endpoints for a component with at least one edge, or degree 0 for an isolated vertex). Contradiction.

Therefore every nonregular edge-minimal counterexample satisfies
  |D|>=k.

A little more follows in the equality case |D|=k. For any v in X,
  d_{H[X]}(v)<=2
and v has at most k cross-edges because those edges inject into the k vertices of D. Hence d_H(v)<=k+2. Since d_H(v)>=k+1, every higher-degree vertex has degree k+1 or k+2. If v is an endpoint of a nontrivial component of H[X], then d_{H[X]}(v)=1, so v must have exactly k cross-edges and d_H(v)=k+1; in particular its cross-edges use every vertex of D exactly once. Isolated vertices are impossible, because they would require at least k+1 cross-edges into only k distinct vertices of D.

Thus |D|=k forces H-D to have no isolated vertices, every path endpoint to be pairwise adjacent (through distinct hyperedges) to all k vertices of D, and every vertex outside D to have degree k+1 or k+2.
