# Every whole chord on a canonical common anchor has a second source-rail intersection

## Statement

Let
  h={y,v,w}
be an ascending nonspecial edge of rank q with unique entrance y and terminal v, and let
  R=(g_1,...,g_{q-1})
be a canonical maximum source rail ending at y, so R,h is a longest q-edge h-path and R avoids v,w.

Let
  e={x,v,u}
be any distinct ascending nonspecial edge terminal at the same vertex v, and suppose both non-v vertices x,u lie on R. Let S be any canonical maximum source rail ending at the unique entrance x of e.

Then
  |V(S) intersect V(R)| >= 2.
In particular, besides the distinguished common vertex x, the source rail S has another intersection with the common anchor precursor R.

Thus every source-clean whole chord on one canonical common anchor automatically carries a second source/anchor intersection; the remaining issue is only where that second intersection lies relative to x and u.

## Body

Because e and h are distinct edges through v, their non-v vertices are disjoint by linearity. In particular x!=y. The path R is a maximum endpoint path ending at y: h is ascending of rank q, so phi(y)=q-1 and R has q-1 edges. Likewise S is a maximum endpoint path ending at x.

By hypothesis x lies on R. Suppose for contradiction that
  V(S) intersect V(R)={x}.
Apply the certified unique-intersection theorem 5854d853a44b to the two maximum endpoint paths S and R, whose endpoints x and y are distinct. It says their unique common vertex x must be an internal joint on both paths, at the same path index.

But x is the last vertex of S, so it cannot be an internal joint of S. This contradiction proves that S and R have at least one additional common vertex.

No terminal-singleness, paid certificate, minimum-terminal assignment, or potential comparison between v and u is used.
