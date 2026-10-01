# Nonspecial middle edges have strict half-path edge rank

## Statement

Let P=(g_1,...,g_L) be a linear path.

(1) If L=2q-1 and the middle edge g_q is nonspecial, then
  phi(g_q)>=q+1.

(2) If L=2q, then each of the two middle edges g_q,g_{q+1} has edge rank at least q+1. Moreover, if g_q is nonspecial with phi(g_q)=q+1, its unique entrance is the central joint
  g_q intersect g_{q+1};
and if g_{q+1} is nonspecial with phi(g_{q+1})=q+1, its unique entrance is the same central joint.

## Body

For any path edge g_t, the prefix
  g_1,...,g_t
is a t-edge linear path ending in g_t, while the reversed suffix
  g_L,g_{L-1},...,g_t
is an (L-t+1)-edge linear path ending in g_t. Hence
  phi(g_t)>=max{t,L-t+1}.

If L=2q, this immediately gives edge rank at least q+1 for t=q and t=q+1. If g_q is nonspecial and has edge rank exactly q+1, then the reversed suffix
  g_{2q},...,g_q
is a longest path ending in g_q. Its entrance label into g_q is
  g_q intersect g_{q+1},
so by uniqueness that vertex is the unique entrance of g_q. The argument for g_{q+1} uses the forward prefix and is identical.

Now let L=2q-1 and t=q. Both the forward prefix
  g_1,...,g_q
and the reversed suffix
  g_{2q-1},...,g_q
have q edges and end in g_q. If phi(g_q)=q and g_q were nonspecial, both would be longest paths ending in g_q. Their entrance labels are respectively
  g_{q-1} intersect g_q
and
  g_q intersect g_{q+1},
which are distinct vertices of the internal path edge g_q. This contradicts uniqueness of the entrance. Therefore a nonspecial middle edge must satisfy phi(g_q)>=q+1.
