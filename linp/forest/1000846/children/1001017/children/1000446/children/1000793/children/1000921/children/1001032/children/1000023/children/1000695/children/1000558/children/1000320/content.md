# The one-special local equality type is impossible

## Statement

Let v have p=phi(v)>=3 and local slack pattern
  a(v)=0, b(v)=1.
Then this configuration is impossible.

Consequently, if equality holds in 7cae1cb001ac, every vertex must be Type A:
  a(v)=2, b(v)=0,
and hence every vertex lies in exactly four special edges. Therefore the special-edge subhypergraph is 4-regular on vertices and
  3s=4n.

## Body

Suppose a(v)=0,b(v)=1. Then
  t_ns(v)=2p-3,
  d_D^-(v)=2p-2,
so v lies in exactly one special edge.

Fix a maximum p-edge path P ending at v. From the chosen-path compensation 3a0d8866aba9,
  B_v<=b(v)=1.
If the last edge h were nonspecial terminal at v, then the h-in-F estimate from 672725540541 gives
  D(v)>=max(0,t_ns(v)-2p+5)=2.
Since D(v)<=B_v, this would imply B_v>=2, contradiction.

Thus every maximum p-edge path ending at v has a special last edge. Because there is exactly one special edge through v, every maximum endpoint path ends in that same special edge.

Hence every nonspecial terminal edge e through v has phi(e)<=p-1: if phi(e)=p, terminality of v for e supplies a maximum p-edge path ending with nonspecial last edge e, contradiction.

All t_ns(v)=2p-3 nonspecial terminal edges therefore have rank at most p-1. Applying 0e550ff0eadd with q=p-1 gives
  t_ns(v)<=2(p-1)-3=2p-5,
contradiction.

Thus Type B is impossible. Under equality in 7cae1cb001ac only Type A remains. Its special-incidence count is
  2+a-b=4
at every vertex, so summing special incidences gives 3s=4n.
