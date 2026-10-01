# Exact minimal equality obstructions admit a balanced d-outregular incidence orientation

## Statement

In the simultaneous strengthened S_ell induction, after the strict layer is excluded, let H be a vertex-minimal exact-density counterexample with |E(H)|=d|V(H)|. Then every proper nonempty induced H[W] has at most d|W|-1 edges. Equivalently every nonempty proper S meets at least d|S|+1 hyperedges. Hall therefore assigns every hyperedge to one incident vertex so that each vertex is assigned exactly d hyperedges.

## Body

Work in the simultaneous induction for the strengthened assertion S_ell, with
  d=floor(2ell/3).
Assume the strict layer has already been excluded on the current vertex size using the smaller-order induction, so let H be a vertex-minimal counterexample to S_ell with exact density
  |E(H)|=d|V(H)|,
minimum degree at least d+1, and a nonspecial edge.

CLAIM 1: every proper nonempty induced subhypergraph J=H[W] satisfies
  |E(J)|<=d|W|-1.                                    (1)

Suppose instead |E(J)|>=d|W|. Repeatedly delete from J any vertex of current degree at most d. Each deletion preserves the inequality
  |E(current)|>=d|V(current)|.
The process cannot delete all the way to fewer than three vertices while preserving this inequality (for d>=1 a 3-uniform hypergraph on fewer than three vertices has no edges, and on three vertices has at most one edge <3d). Hence it stops at a nonempty induced subhypergraph J_0 with
  delta(J_0)>=d+1
and
  |E(J_0)|>=d|V(J_0)|.

The graph J_0 remains linear and P_ell-free. It cannot have all edges special in its own snake structure: if all were special, the certified snake accounting 599c2c0d2adf with s=m would give
  3|E(J_0)|<=(2ell-3)|V(J_0)|<3d|V(J_0)|,
contradicting its density. Thus J_0 contains a nonspecial edge.

Since W is proper, J_0 has fewer vertices than H, so J_0 is a smaller counterexample to S_ell, contradicting vertex-minimality. This proves (1).

CLAIM 2: every nonempty proper S⊂V(H) meets at least d|S|+1 hyperedges.

Indeed, with W=V(H)\S,
  |N_H(S)|
   =|E(H)|-|E(H[W])|
   >=dn-[d(n-|S|)-1]
   =d|S|+1.                                         (2)
(The case W empty is excluded because S is proper.)

CLAIM 3: H admits a balanced incidence orientation assigning each hyperedge to one of its three vertices so that every vertex is assigned exactly d edges.

Form the bipartite incidence graph between d formal copies of every vertex v and the hyperedges of H, joining each copy of v to every hyperedge containing v. Hall's condition for a set of vertex copies reduces to (2): for any set S of underlying vertices, its hyperedge neighborhood has size at least d|S| (indeed d|S|+1 unless S=V(H), while for S=V(H) the neighborhood has size |E(H)|=dn=d|V(H)|). Thus there is a matching saturating all dn vertex copies.

Because H itself has exactly dn hyperedges, that matching also uses every hyperedge exactly once. Orient each hyperedge toward the matched incident vertex. Then every vertex is the chosen source of exactly d hyperedges.

Equivalently, every exact minimal equality obstruction in the simultaneous induction has a d-outregular orientation of its hyperedges.
