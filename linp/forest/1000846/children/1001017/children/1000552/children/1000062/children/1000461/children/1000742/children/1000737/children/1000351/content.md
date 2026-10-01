# Type-A vertices force an exact saturated rank-minus-one terminal fan

## Statement

Let v be Type A with p=phi(v)>=5. Then v has exactly 2p-5 nonspecial terminal edges, all of rank at most p-1, and at least one has rank p-1.

Fix a rank-(p-1) nonspecial terminal edge h through v and a longest
  P=(g1,...,g_{p-1}=h)
ending in h with last vertex v. Put
  W=V(P)\h
and
  C=g_{p-3}\g_{p-4},
so |W|=2p-4 and |C|=2.

For every other nonspecial terminal edge f through v:
1. f meets W\C;
2. the sets (f\{v})∩(W\C) are singletons and, as f varies, partition W\C;
3. f has at most one additional P-contact, necessarily in C.

Consequently at most two of the 2p-6 edges f!=h are double-blocking on P, and at least 2p-8 are single-blocking.

## Body

By a57057ab0001, a Type-A vertex v of potential p has exactly 2p-5 nonspecial terminal edges, every one has rank at most p-1, and at least one has rank exactly p-1. The same theorem shows that all special edges through v have rank p and every nonspecial source edge at v is ascending of rank p+1. Hence the incident edges through v of rank at most p-1 are exactly those 2p-5 nonspecial terminal edges.

Choose one rank-(p-1) member h and a longest (p-1)-edge path
  P=(g1,...,g_{p-1}=h)
ending in h at last vertex v.

Apply the incident low-rank capacity theorem a570ca900001 with q=p-1. In its proof,
  W=V(P)\h
has size 2q-2=2p-4, and for q>=4 the excluded cell is
  C=g_{q-2}\g_{q-3}=g_{p-3}\g_{p-4},
which has size two.

The theorem proves that every other edge f through v of rank at most q has a contact in W\C. There are exactly
  (2p-5)-1=2p-6
such edges f!=h, while
  |W\C|=(2p-4)-2=2p-6.

Because all these edges contain v, linearity implies that their contact sets in W are pairwise disjoint. Since each of the 2p-6 edges has at least one contact in the 2p-6 element set W\C, equality forces:
- each edge has exactly one contact in W\C;
- every vertex of W\C is used by exactly one edge.

Any further contact of such an f with P must therefore lie in C. An edge f cannot contain both vertices of C, because both belong to the single path edge g_{p-3}; then f and g_{p-3} would share two vertices, contradicting linearity. Thus each f has at most one additional C-contact.

Finally, the two vertices of C can be used by at most two distinct f, again because the f share v and their non-v contact sets are disjoint. Hence at most two f are double-blocking, while at least
  (2p-6)-2=2p-8
have exactly one P-contact.