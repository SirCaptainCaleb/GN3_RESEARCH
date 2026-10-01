# The fixed-entrance conflict system has a five-fourths integrality gap over fractional packing

## Statement

In the fixed-entrance setup of eb40ddcc33ca with q>=4, let K_q be the conflict hypergraph on W whose hyperedges are the four forbidden singleton positions
{a_1},{b_1},{b_{q-2}},{z_{q-2}}
together with every two-vertex singleton-contact conflict supplied by the fixed-entrance splice between the forward part of g_i and the backward part of g_{i+2}, 1<=i<=q-3.

Then the fractional matching number is exactly
nu^*(K_q)=q+1,
whereas the minimum vertex-cover number is
tau(K_q)=2q-2-ceil((3q-8)/4).
Thus tau(K_q)=(5/4+o(1)) nu^*(K_q). In particular, no fractional packing of the complete one-anchor singleton-contact constraints can improve the old q+1 marked-vertex lower bound; the improvement from local slope 3/2 to 11/8 is intrinsically an integral independence/cover phenomenon.

## Body

Give every vertex capacity one in the fractional matching linear program. If L is the total weight placed on singleton hyperedges and E is the total weight placed on two-vertex conflict edges, then
L+2E<=|W|=2q-2.
There are only four singleton hyperedges and each has weight at most one, so L<=4. Therefore
L+E <= (2q-2+L)/2 <= q+1.
Hence nu^*(K_q)<=q+1.

Equality is attained by the explicit disjoint constraint family from 236389970703: the four singleton hyperedges together with q-3 disjoint conflict pairs partition W. Assigning weight one to those q+1 hyperedges is a fractional matching. Thus nu^*(K_q)=q+1.

For the integral cover number, a set T⊆W meets every hyperedge of K_q exactly when its complement is a set of permitted singleton-contact positions: it avoids the four individually forbidden positions and contains no conflict pair. Hence
tau(K_q)=|W|-alpha(K_q),
where alpha(K_q) is the maximum size of such an independent set. The exact four-state transfer solved in eb40ddcc33ca gives
alpha(K_q)=ceil((3q-8)/4).
Since |W|=2q-2, the displayed formula for tau follows.

Finally,
tau(K_q)/(q+1) -> 5/4.
The disjoint matching from 236389970703 is therefore already optimal among all fractional combinations of the same singleton and pair constraints. The later 43/48 improvement is possible only because the overlapping conflict edges have a substantially larger integral cover number than their fractional packing lower bound.
