# Zero-slack critical cores collapse to a one-factorized graph plus disjoint triples

## Statement

In the extremal |D|=k color-complete critical-core normal form, the zero-slack case m+2c=2k forces H-D to be a matching of single hyperedges. In particular every forest component has length one, m=c, and 3c=2k. Moreover the DXX color graph G on X has |X|=2k vertices, is k-regular, and its k colors are perfect matchings (a 1-factorization of G).

## Body

By 1663a127e081, when
m+2c=2k,
every edge incident with every d∈D is a DXX edge whose two X-endpoints are forest-degree-one vertices. In particular no edge meeting D contains a forest joint.

Suppose H-D had a component of length at least two. Then that component has a forest joint x, i.e. a vertex with d_{H-D}(x)=2.

The vertex x lies in X=V(H)\D, so by the dense-core setup d_H(x)>=k+1. But x lies in no edge meeting D, because every edge meeting D has its X-endpoints forest-private. Therefore all edges through x lie in H-D. Since H-D is a path forest, x has exactly its two forest edges and
d_H(x)=2,
contradicting k+1>=3.

Thus H-D has no joints. Every nonempty path component consequently consists of a single hyperedge. Hence m=c.

Combining with zero slack gives
3c=m+2c=2k,
so c=2k/3. In particular 3 divides 2k.

Each one-edge component has three forest-private vertices, so
|X|=3c=2k.

Again by 1663a127e081, for every d∈D all k edges through d are DXX edges pairing forest-private vertices. Since every X-vertex is now forest-private, the d-colored edges form a matching saturating all 2k vertices of X, hence a perfect matching of size k.

Therefore the DXX graph G on X is k-regular and properly edge-colored by the k vertices of D, with every color class a perfect matching.
