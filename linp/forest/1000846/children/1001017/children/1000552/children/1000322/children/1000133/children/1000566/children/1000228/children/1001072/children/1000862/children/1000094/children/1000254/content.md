# Zero slack forces the universal path forest to be a matching

## Statement

In the |D|=k critical-core normal form, if m+2c=2k then H-D has no forest joints. Hence every component of H-D is a single edge, m=c, and 3c=2k. Thus zero slack can occur only when 3 divides k, and the core reduces to c=2k/3 disjoint X-triples together with k pairwise edge-disjoint perfect D-colored matchings on the 2k vertices of X.

## Body

Assume the extremal |D|=k critical-core normal form and zero slack
  m+2c=2k.
Let F=H-D be the universal path forest.

By 1663a127e081, for every d in D the d-colored matching has exactly k edges, saturates all 2k forest-private vertices, and uses the entire degree-k star of d. In particular every edge of H meeting D contains exactly one D-vertex and its two X-vertices are forest-private.

Suppose F has a joint vertex v, i.e. d_F(v)=2. Since every edge meeting D uses only forest-private X-vertices, no edge through v meets D. Since H[X]=F, the only edges of H through v are its two forest edges. Thus
  d_H(v)=2.
But the dense-core threshold is k=floor(2ell/3)+1>=3 for ell>=4, contradicting delta(H)=k.

Hence F has no joint vertices. Every nonempty component of the path forest therefore consists of a single edge. Thus
  m=c.
Combining with zero slack gives
  3c=2k.

Consequently zero slack is possible only when 3 divides k, in which case c=2k/3 and X is partitioned into c disjoint triples, all vertices of X are forest-private, and the DXX color graph is k-regular on |X|=3c=2k vertices with each of the k colors a perfect matching.

Equivalently, the entire zero-slack critical core consists of:
- a matching F of c=2k/3 disjoint X-triples;
- k threshold vertices D;
- for each d in D, a perfect matching M_d on X;
with the M_d pairwise edge-disjoint and every hyperedge outside F equal to {d,x,y} for xy in M_d.
