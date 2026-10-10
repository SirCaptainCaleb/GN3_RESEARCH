# All-root geodesic complex: exact f-vector, Euler characteristic, median simple connectivity and integral orientation

# Exact f-vector, Euler characteristic, median simple connectivity, and integral orientation of the all-root geodesic complex

Let n>=2. Write K_n for the simplicial complex on {0,1}^n whose simplices lie in some full n-edge antipodal cube geodesic. The earlier Item nori_all_root_geodesic_pseudomanifold_20261008 proves that K_n is a closed connected n-dimensional pseudomanifold with each ridge in two chambers and connected chamber dual graph.

**Theorem 1 (exact f-vector).** If S(n,k) is the Stirling number of the second kind, then f_0(K_n)=2^n, and for every 1<=k<=n,
f_k(K_n)=2^(n-1)[k!S(n,k)+(k+1)!S(n,k+1)]
        =2^(n-1) sum_(j=0)^k (-1)^j binom(k,j)(k+1-j)^n.
In particular f_n=2^(n-1)n!, and the 1-skeleton is the complete graph on 2^n vertices.

*Proof.* A set of k+1>=2 vertices belongs to a geodesic precisely when it can be ordered v_0,...,v_k with nonempty pairwise-disjoint coordinate-change sets D_i between successive vertices. Conversely such a sequence extends to a full antipodal geodesic by resolving each D_i into singleton flips and appending the unused coordinates. Choosing v_0 gives 2^n choices; assigning each coordinate to one of the k nonempty ordered D_i, or the possibly empty unused set D_0, gives the stated inclusion-exclusion count, equivalently k!S(n,k)+(k+1)!S(n,k+1). The endpoints of the ordered sequence are uniquely the pair at maximal Hamming distance, and the order of its interior vertices is uniquely determined by increasing distance from the first endpoint. Hence every unordered simplex is counted exactly twice, for the two orientations. Every cube-vertex pair lies on a geodesic.

**Corollary 2 (Euler characteristic).** chi(K_n)=2^(n-1).

*Proof.* Sum (-1)^k f_k. All Stirling terms with index >=2 cancel between adjacent k. The residual sum over k>=1 is -2^(n-1) S(n,1)=-2^(n-1), added to f_0=2^n.

**Theorem 3 (simple connectivity).** pi_1(K_n)=0, so H_1(K_n;Z)=0.

*Proof.* The 1-skeleton is complete. For any three cube vertices u,v,w, let m be the coordinatewise majority vertex. Then m lies on a shortest cube geodesic between every pair from {u,v,w}. Consequently the triangles (u,v,m), (v,w,m), (w,u,m) all occur as 2-simplices whenever nondegenerate. They fill the 3-edge loop (u,v,w,u); if a vertex coincides with m the original triangle is already a simplex. Every edge loop in the complete 1-skeleton decomposes into triangular loops. Thus every loop contracts.

**Theorem 4 (orientation and 2-torsion).** For n>=2,
H_n(K_n;Z)=Z if n is even; H_n(K_n;Z)=0 if n is odd.
For odd n, H_(n-1)(K_n;Z) contains exactly one cyclic 2-primary torsion factor; for even n, H_(n-1)(K_n;Z) has no 2-primary torsion. (The order of that factor for odd n is unspecified.)

*Proof.* Encode a rooted directed n-geodesic by (x,p), with p a permutation of coordinates, and orient its simplex [v_0,...,v_n] using coefficient sign(p). Exchanging adjacent directions p_i,p_(i+1) swaps sign(p); the two chambers share the ridge obtained by deleting the rank-i vertex, with the same inherited vertex ordering, so boundary coefficients cancel. Under a forward root slide (x,p_1,...,p_n) -> (v_1,p_2,...,p_n,p_1), the common ridge [v_1,...,v_n] appears with boundary coefficient +1 in the first chamber and (-1)^n in the second; the permutation rotation has sign (-1)^(n-1), so coefficients again cancel. Adjacent swaps and root slides connect all rooted chambers, as proved in the earlier pseudomanifold Item.

However, the rooted descriptions (x,p) and (bar x,reverse(p)) define the very same geometric simplex with opposite vertex order. Reversing p multiplies sign(p) by (-1)^(n(n-1)/2) and reversing n+1 vertices multiplies the simplicial orientation by (-1)^(n(n+1)/2). The product equals (-1)^(n^2)=(-1)^n. Therefore the coherent rooted chamber orientations descend to the actual closed pseudomanifold exactly when n is even. Every integral top cycle on a connected closed pseudomanifold has a common signed absolute chamber coefficient, because each ridge is in precisely two facets. Odd root-reversal monodromy forces that coefficient to vanish. The claimed top integral homology follows.

The preexisting mod-2 top fundamental cycle gives H_n(K_n;F_2)=F_2. By the universal coefficient theorem, this group is H_n(K_n;Z) tensor F_2 plus Tor(H_(n-1)(K_n;Z),F_2). The stated parity cases force respectively one or zero cyclic 2-primary factors in H_(n-1)(K_n;Z).

**Interpretation for NORI.** chi(K_n)=2^(n-1) equals the number of antipodal-edge midpoint fixed points of the complementation action established in the previous Item. The carrier is simply connected in every dimension, but integral orientation is available precisely in even dimensions. An equivariant grand-closure argument using this carrier must accommodate its fixed locus and, in odd dimensions, its orientation local system. These invariants alone do not imply a good full geodesic for arbitrary ordered-three-face colorings.

**Corollary (canonical order-two Bockstein cycle in odd dimensions).** Let n be odd. Choose any integral lift C of the mod-2 top fundamental cycle by assigning coefficient +1 to one arbitrarily oriented representative of every n-simplex. Every ridge lies in two facets, so the integral boundary is even: partial C=2B for an integral (n−1)-chain B. Because partial^2 C=0 and integral chain groups are torsion free, partial B=0. The class [B] satisfies 2[B]=0. It is nonzero: if B=partial D, then C−2D would be a nonzero integral top cycle (each top coefficient remains odd), contradicting H_n(K_n;Z)=0. Hence [B] has exact order two, is independent of lift, and equals the integral Bockstein of the mod-2 top fundamental class. The preceding universal-coefficient argument shows it is the unique nonzero element of H_(n−1)(K_n;Z) annihilated by two. This supplies an explicit parity-sensitive cycle for testing future color-dependent obstruction cochains.
