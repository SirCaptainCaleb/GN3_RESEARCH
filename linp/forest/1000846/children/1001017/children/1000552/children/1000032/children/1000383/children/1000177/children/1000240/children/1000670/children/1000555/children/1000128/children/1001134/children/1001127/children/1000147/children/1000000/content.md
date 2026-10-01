# A higher-rank internal edge on a maximum endpoint path forces a suffix return unless the path leaves through its unique entrance

## Statement


Let
  R=(g_1,...,g_L)
be a maximum endpoint path with last vertex x, so phi(x)=L. Let h=g_j be an internal edge of R, with j<L and edge rank
  r=phi(h)>L.
Put
  z=g_j intersect g_{j+1},
the path joint through which R leaves h toward x.

If z is terminal at h, then every maximum r-edge path Q with last edge h and last vertex z has a common vertex with the suffix
  g_{j+1},...,g_L
other than z.

Consequently:

(a) if h is special, this suffix return is forced;

(b) if h is nonspecial with unique entrance y, the suffix return is forced unless z=y.

Thus a higher-rank internal edge can avoid a forced return into the remaining suffix only when it is nonspecial and the host path leaves h through its unique entrance.


## Body


Assume z is terminal at h. By definition,
  phi(h,z)=phi(h)=r,
so there is an r-edge linear path Q whose last edge is h and whose last vertex is z.

Suppose Q has no common vertex with the suffix g_{j+1},...,g_L other than z. Then concatenate Q with
  g_{j+1},...,g_L.
The concatenation is a linear path ending at x: Q meets g_{j+1} at its last vertex z, and by assumption there is no further intersection with the suffix.

Its length is
  r+(L-j).
Because r>L and j<L, this is strictly larger than L, contradicting phi(x)=L. Hence the claimed suffix return is unavoidable.

If h is special, every vertex of h is terminal at h, so in particular z is terminal at h.

If h is nonspecial, its unique entrance y is the only vertex of h that is not terminal at h; the other two vertices are terminal at h. Therefore the only case not covered by the first paragraph is z=y.
