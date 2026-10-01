# Every equality-layer witness omits many above-threshold vertices

## Statement

Let ell>=5 and d=floor(2ell/3). In an n-vertex linear 3-graph with |E(H)|=dn and minimum degree at least d+1, every path P of length at most ell-1 omits at least 4d-2ell vertices of degree at least d+2. More precisely, the total outside excess E_O=sum_{v outside P}(d(v)-(d+1)) satisfies E_O>=n(2d-1-|V(P)|/2)+|V(P)|(d+3/2). Thus a nonspecial equality-layer witness omits at least d, d-2, or d-1 genuinely above-threshold vertices according as ell is 0,1,2 mod3.

## Body


Fix ell>=5 and d=floor(2ell/3). Let H be an n-vertex linear 3-graph with
  |E(H)|=dn
and minimum degree at least d+1, as in a vertex-minimal equality-layer obstruction. Let P be any q-edge path with q<=ell-1, put
  S=V(P),  s=|S|=2q+1,
and O=V(H)\S.

Define the outside excess
  E_O = sum_{v∈O}(d_H(v)-(d+1)).
Then
  sum_{v∈O}d_H(v)=(d+1)(n-s)+E_O.

By linearity every vertex has degree at most (n-1)/2, so
  sum_{v∈S}d_H(v) <= s(n-1)/2.
Using sum_v d_H(v)=3dn gives
  3dn <= s(n-1)/2 +(d+1)(n-s)+E_O,
hence
  E_O >= n(2d-1-s/2)+s(d+3/2).                       (1)

Now let h be the number of outside vertices with degree at least d+2, i.e. positive excess. Every such vertex has excess at most
  (n-1)/2-(d+1)
  = (n-2d-3)/2
  < n/2.
Therefore
  E_O < h n/2,
so
  h > 2E_O/n.                                         (2)

From (1),
  2E_O/n
  >= 4d-2-s + [2s(d+3/2)]/n
  > 4d-2-s.
Since s<=2ell-1,
  h > 4d-2-(2ell-1)
    = 4d-2ell-1.
The right side is an integer, so
  h >= 4d-2ell.                                       (3)

Thus every P_ell-free equality-layer witness omits at least 4d-2ell vertices of degree at least d+2.

Evaluating by residues:
- ell=3r, d=2r: h>=2r=d;
- ell=3r+1, d=2r: h>=2r-2=d-2;
- ell=3r+2, d=2r+1: h>=2r=d-1.

For ell>=5 these are positive; even the weakest residue ell≡1 mod3 forces d-2 high-degree outside vertices.

This is independent of nonspeciality: it holds for every path of length at most ell-1 in an exact-density minimum-degree-(d+1) graph. Applied to a nonspecial witness, it gives a large reservoir of omitted vertices with at least one extra degree unit beyond threshold.
