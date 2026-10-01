# Binary doubling reduces spanning paths to additive rainbow-forest accounting

## Statement

Consider the standard doubling of an STS on an odd set U by a one-factorization on a disjoint set W of size |U|+1. If a spanning linear path uses a old blocks from U, then its mixed edges select a spanning linear forest on W with exactly a+1 components; each component is rainbow in the one-factorization, every color is used at most twice, and repeated colors occur exactly at U-joints between consecutive mixed hyperedges.

In the binary additive doubling W=F_2^d with color(pq)=p+q, let M be the unused nonzero colors and R the colors used twice. Then
|M|-|R|=a,
and the xor of all component endpoints equals xor(M) xor xor(R).

In particular a=0 is impossible: it would give a rainbow Hamiltonian path in the additive one-factorization, but the xor of all nonzero colors is zero whereas the xor of the colors along a Hamiltonian path equals the xor of its two distinct endpoints and is nonzero. Thus every spanning path in the binary doubled STS uses at least one old block.

## Body

Let P be a spanning |U|-edge linear path and let a be the number of old STS blocks it uses. Count joints of P lying in U and W. If b=|U|-a is the number of mixed blocks, incidence counting on U gives exactly 2a U-joints, hence |U|-1-2a W-joints.

Represent each mixed triple {x,p,q} by the matching edge pq on W. The selected graph has |W| vertices and b edges. Every W-vertex has degree one or two according as it is not or is a W-joint of P. A selected cycle is impossible, because its mixed hyperedges would have to occur cyclically as consecutive edges of a path. Hence the selected graph is a spanning linear forest. Its component count is
|W|-b=(|U|+1)-(|U|-a)=a+1.
Along each component, consecutive selected edges have distinct colors by properness, while nonconsecutive selected edges cannot share a color because the corresponding hyperedges would be nonconsecutive and intersect in the common color vertex. Thus every component is rainbow. A color may occur at most twice overall, and if repeated the two mixed hyperedges are consecutive and joined through that U-color.

Now specialize to W=F_2^d with additive color p+q. Let c=a+1 be the number of path components of the selected forest. If s colors are used once and r=|R| twice, then
s+2r=2^d-c.
The distinct used colors are exactly the complement of M among the 2^d-1 nonzero colors, so
s+r=(2^d-1)-|M|.
Subtracting gives |M|-|R|=c-1=a.

For xor accounting, the xor of all nonzero vectors of F_2^d is zero. Relative to that full set, the forest color multiset deletes M and adds one extra copy of each color in R, hence its xor is xor(M) xor xor(R). On each graph-path component, internal vertices cancel in the sum of edge colors and only the two endpoints remain. Xoring over all components proves the endpoint identity.

When a=0, the forest has one spanning component and M=R=emptyset. It would therefore be a rainbow Hamiltonian path using every nonzero color exactly once. But the xor of all nonzero colors is zero, while the edge-color xor along a Hamiltonian path equals the xor of its two distinct endpoints and is nonzero. Contradiction. This is the additive Maamoun--Meyniel obstruction in the binary-projective coordinates.

Thus the spanning-path problem in binary doubling reduces to coupling the missing/repeated-color equation to the geometry of the old blocks in U; the first nontrivial obstruction is already forced at a=0.
