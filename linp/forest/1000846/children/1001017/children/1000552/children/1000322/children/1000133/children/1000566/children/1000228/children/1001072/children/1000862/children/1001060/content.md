# Free-end connector is either an inter-component bridge or a cycle-closing chord

## Statement

Assume the color-complete path-forest normal form c15cf7354428. Let C=(e_1,...,e_a) be a component of F=H[X], let x be a free last vertex of e_1, and let f={x,d,y} be the unique connector of color d through x. If y lies in a different forest component C' of length b, then H contains a linear path of length at least a+1+ceil(b/2). Hence P_ell-freeness forces a+ceil(b/2)<=ell-2. If y lies in C itself and j is the first path-edge index containing y, then j>=2 and e_1,...,e_j,f is a linear cycle of length j+1. Thus every threshold-color connector at a free forest end is either an inter-component bridge giving the displayed path lower bound, or a cycle-closing chord in its own component.

## Body

First suppose y lies in another component C'. Since d lies in D and all vertices of F lie in X, the connector f meets C only at x and C' only at y.

Orient C so that it has x as a last vertex; this uses all a edges. By the half-path endpoint-potential fact 8b1790d79d74 applied inside C', there is a subpath Q of C' of length at least ceil(b/2) having y as a last vertex. Orient Q away from y. Then
  C, f, Q
is a linear path: the only new consecutive intersections are C∩f={x} and f∩Q={y}, while distinct forest components are vertex-disjoint and d is outside X. Its length is at least
  a+1+ceil(b/2).
If H is P_ell-free, this length is at most ell-1, giving
  a+ceil(b/2)<=ell-2.

Now suppose y lies in C. Let j be the first index such that y∈e_j. We cannot have j=1, because then f and e_1 would share the two vertices x and y, contradicting linearity. Thus j>=2.

The sequence e_1,...,e_j is a path segment from x to y. The edge f meets its first edge only at x and its last edge only at y. If y is a joint of e_j and e_{j+1}, the latter edge is not included; by choice of the first occurrence and linearity no other segment edge contains y. Also f cannot meet another forest edge, since its only X-vertices are x and y. Therefore
  e_1,...,e_j,f
is a linear cycle of length j+1.
