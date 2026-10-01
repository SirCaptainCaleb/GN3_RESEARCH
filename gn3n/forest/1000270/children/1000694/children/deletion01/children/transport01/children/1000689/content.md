# Boundary second-type pivots reduce to matching-block four-kernels

## Statement

Let H-x=P|Q be an exact deletion two-cover in a minimum counterexample. If the failed-insertion obstruction on P is second-type at the first or last gap, then the four-set consisting of x and the adjacent three path vertices is either Hamiltonian, with non-Hamiltonian exact-two-coverable complement, or is edge-orderable and non-Hamiltonian with explicitly forced matching-block order. At the first gap the matching {p0x,p1p2} is the top block; at the last gap the three matching blocks have a unique order.

## Body


# Boundary second-type pivots reduce to matching-block four-kernels

Let H be a minimum counterexample and let

H-x=P|Q,

where P=(p_0,...,p_m), m>=2, be an exact deletion two-cover. Apply the local failed-insertion theorem to x and the displayed order of P.

## Left boundary pivot

Assume its second alternative occurs at the first gap p_0|p_1. Put

a=p_0, b=p_1, c=p_2, z=x,

and X={a,b,c,z}.

The second-type pivot relations give

(b,a,z), (b,z,a), (z,b,c)

tight. The original path gives (a,b,c) tight, and endpoint-hook forcing gives (c,z,a) tight.

If H[X] is Hamiltonian, then H-X is non-Hamiltonian and has path-cover number exactly two by the minimum-counterexample calculus.

Assume H[X] is non-Hamiltonian. Its comparison digraph cannot be cyclic. Indeed the triples

(b,a,z), (b,z,a)

give, on the three ordinary edges ab,az,bz,

ab -> az  and  bz -> az.

Thus the comparison orientation on the three-vertex subset {a,b,z} is transitive, not cyclic. But every non-Hamiltonian four-vertex boundary tournament with cyclic comparison digraph is the exceptional cyclic K4, and every three-vertex subset of that K4 has cyclic comparison orientation. Hence H[X] is edge-orderable.

By the matching-block classification for a non-Hamiltonian edge-ordered K4, its three opposite-edge perfect matchings occur as strict blocks. Set

M_0={ab,cz},
M_1={ac,bz},
M_2={az,bc}.

The tight triple (a,b,c) gives ab<bc, hence M_0<M_2. The tight triple (b,z,a) gives bz<az, hence M_1<M_2. Therefore M_2 is the top block, and exactly one of

M_0<M_1<M_2,
M_1<M_0<M_2

holds.

## Right boundary pivot

Assume instead that the second-type obstruction occurs at the last gap p_{m-1}|p_m. Put

a=p_{m-2}, b=p_{m-1}, c=p_m, z=x,

and again X={a,b,c,z}.

The second-type pivot relations give

(c,b,z), (c,z,b), (a,b,z), (z,c,b)

tight. The original path gives (a,b,c) tight, and endpoint-hook forcing gives (c,z,a) tight.

If H[X] is Hamiltonian, again H-X is non-Hamiltonian with path-cover number exactly two.

Assume H[X] is non-Hamiltonian. On the three-set {b,c,z}, the tight triples

(c,b,z), (c,z,b)

give

bc -> bz  and  cz -> bz,

so this comparison triangle is transitive. Therefore the cyclic non-edge-orderable K4 is again impossible, and H[X] is edge-orderable.

Use the same three matchings M_0,M_1,M_2. Now

(a,b,c) gives M_0<M_2,
(c,z,b) gives M_0<M_1,
(c,b,z) gives M_2<M_1.

Hence the block order is forced uniquely:

M_0<M_2<M_1.

Thus every boundary second-type insertion obstruction is reduced to the same small-set frontier as the other local cases: either a Hamiltonian four-window with an exact-two-cover complement, or a rigid non-Hamiltonian edge-orderable K4 with explicitly known matching-block geometry.
