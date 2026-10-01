# Cheap witness-avoiding singleton deletion forces an exact threshold bridge

## Statement

For a witness-avoiding set S, the density deficit updates exactly by r(H-S)=r(H)+|N(S)|-d|S|. In a vertex-minimal equality obstruction, a cheap singleton deletion w that preserves density at least d and a nonspecial witness need not contradict minimality; instead H-w has a degree-at-most-d vertex u. Linearity then forces d_H(u)=d+1, d_{H-w}(u)=d, and a unique hyperedge through {u,w}.

## Body


Let H be a vertex-minimal counterexample to the equality-layer assertion S_ell at density threshold d. Fix a nonspecial edge e together with a witness path P for e.

Let S⊆V(H)\V(P). Then e and its witness survive in H-S, and nonspeciality survives as well: deleting vertices cannot create a new entrance witness, while P still certifies the old rank and entrance. Let N(S) denote the set of hyperedges meeting S.

If H has deficit r,
  |E(H)|=d|V(H)|-r,
then
  |E(H-S)|
   =|E(H)|-|N(S)|
   =d(|V(H)|-|S|)
      -[r+|N(S)|-d|S|].
Hence
  r(H-S)=r+|N(S)|-d|S|.                           (1)

In particular, at equality r=0, if
  |N(S)|<=d|S|,
then H-S still has density at least d and retains a nonspecial edge.

Vertex-minimality does NOT imply a contradiction: S_ell may simply hold in H-S. What it does imply is that H-S contains a vertex u with
  d_{H-S}(u)<=d.

Now specialize to S={w}, with w outside P, and assume the deletion is cheap:
  d_H(w)=|N({w})|<=d.
Then H-w retains density at least d and nonspeciality. Hence there exists u!=w with d_{H-w}(u)<=d.

If H itself is a counterexample to S_ell, then delta(H)>=d+1. By linearity, deleting w removes at most one edge incident with u, since two distinct edges containing both u and w would share the pair {u,w}. Therefore
  d_H(u)-1 <= d_{H-w}(u) <= d,
while d_H(u)>=d+1.
Consequently
  d_H(u)=d+1,
  d_{H-w}(u)=d,
and exactly one hyperedge contains the pair {u,w}.

Thus every cheap witness-avoiding singleton deletion in a minimal counterexample forces an exact threshold bridge from the deleted vertex to a degree-(d+1) survivor. This is the precise lift-back alternative missing from the invalid packet-expansion argument.
