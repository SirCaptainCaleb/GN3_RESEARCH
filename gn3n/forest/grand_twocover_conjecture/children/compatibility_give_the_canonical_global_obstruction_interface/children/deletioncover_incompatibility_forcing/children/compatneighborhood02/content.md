# Compatibility neighborhoods are unions of paths and cycles

## Statement

Let H be a boundary tournament with pc(H)>2, choose one deletion cover F_x for each label x in a set D, and let G be the compatibility graph on D. For every vertex d of G, the induced graph G[N_G(d)] has maximum degree at most two. Hence every connected component of G[N_G(d)] is a path or a cycle, and if k=d_G(d), then at most k pairs of vertices in N_G(d) are compatible with each other, so at least binom(k,2)-k pairs are incompatible. Moreover, if da is an adjacent-slot compatibility edge in the sense of compatedgecodeg02, then a has degree at most one in G[N_G(d)].

## Body

# Proof

Fix d in V(G). For a neighbor a of d, the degree of a inside G[N_G(d)] is exactly the number of labels c such that c is adjacent to both d and a; equivalently,

deg_{G[N(d)]}(a)=|N_G(d) intersect N_G(a)|.

By compatedgecodeg02 every compatibility edge has at most two common neighbors. Therefore deg_{G[N(d)]}(a)<=2 for every a in N_G(d), proving Delta(G[N_G(d)])<=2.

A finite simple graph of maximum degree at most two is a disjoint union of paths, cycles, and isolated vertices. If k=|N_G(d)|, such a graph has at most k edges. Thus among the binom(k,2) unordered pairs of compatible partners of F_d, at most k pairs are themselves compatible, and at least binom(k,2)-k pairs are incompatible.

For the refinement, if da is an adjacent-slot compatibility edge, compatedgecodeg02 gives at most one common neighbor of d and a. Hence deg_{G[N(d)]}(a)<=1.

The statement is purely graph-theoretic once the certified edge-codegree bound is known; no minimum-counterexample hypothesis or fixed-order analysis is used.

## Consequence for the compatibility route

High compatibility degree at one deletion label cannot create a dense compatible cluster. Instead, k compatible partners of one cover automatically generate quadratically many pairwise incompatibilities among themselves. Thus either the compatibility degree is globally small, or any locally high compatibility degree creates a large secondary disagreement family on the same label set. This gives a natural second-stage counting input for the deletion-cover incompatibility route.