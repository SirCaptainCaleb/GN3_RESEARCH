# Audit: weighted cube-boundary zeros remain in pole stars — preserved pre-item development

## Development

## Audit of §34: pole stars are not pole vertices

### Claim under audit
The weighted cube-boundary turn map in §34 is odd and continuous. Its non-pole-face localization argument is valid under the stated minimum-counterexample hypothesis. Its asserted closure does not follow.

### The gap
Let a zero lie in the relative interior of a barycentric simplex with flag F_0 < ... < F_m. The descent argument proves only that the smallest face F_0 is the bottom or top cube vertex. Such a flag can contain larger faces. Its geometric simplex is in the closed star of that vertex and usually contains points other than the vertex.

Consequently the argument does not prove that the value of the map at the bottom vertex is zero. Equation (5) of §34, and therefore equations (6)–(7), have not been established. Parameter variation may move a zero within a pole star.

### Explicit face-average example
This example tests the asserted geometric implication; it is not a coloring counterexample.

Take V={1,2,3}, r=2, c_0=c_1=c_2=1, and a_1=2, a_2=a_3=1. For every zero-facet permutation use the formal window at position f=1, so that the window comprises V. The zero-facet label with normal x is
L_x=a_x(3e_x-e_1-e_2-e_3).
Thus
L_1=(4,-2,-2), L_2=(-1,2,-1), L_3=(-1,-1,2).
Give antipodal top simplices the negative labels, average over incident top simplices at face barycenters, and interpolate on the barycentric subdivision.

At the bottom vertex b_0 the value is (2,-1,-1)/3, which is nonzero. For the ordinary edge E=[emptyset,{1}], the incident top simplices have normals 2 and 3, in equal numbers. Its barycenter value is (-1,1/2,1/2). Therefore
(3/5) Phi(b_0)+(2/5) Phi(b_E)=0.
The zero is the geometric point (1/5,0,0), strictly away from the pole. Its smallest ordinary face in the barycentric flag is nevertheless the pole.

There are no zeros on flags whose smallest face is not a pole in this example. Indeed the block functional of §34 is strictly positive on every incident label: a formal witness uses all three coordinates, whereas a non-pole face has at least two blocks. This gives a direct example of the very geometric conclusion used in §34 without its claimed pole-value conclusion.

### Stronger diagnosis: the bottom-link map has nonzero degree
Assume the minimum-counterexample hypotheses of §34, and use any of its positive parameters. Let K be the Freudenthal boundary triangulation and let L be the link of the bottom vertex in its barycentric subdivision. Then L is an (n-2)-sphere. The restriction Phi|L is zero-free, and its normalization has absolute degree one. Hence its extension across the bottom closed star must have a zero. Positive weight variation does not remove this obstruction.

#### Proof of zero-freeness on the link
A link vertex is b_F, where F is an ordinary simplex properly containing the bottom vertex. Write the chain defining F as
emptyset < A_1 < ... < A_t,
and put Z=V\A_t. Both A_1 and Z are nonempty.

For a flag F_0 < ... < F_m in L, choose the block-index functional beta of F_0. All labels of top simplices containing any F_i have beta(L)>=0, as in §34. If their positively weighted combination were zero, the average at F_0 would force every incident first-change window to lie in Z. Choose x in Z and a one-change order tau of Z\{x}, by minimality (if the set is too short to have a window, the requirement that a turn fit in tau is already impossible). A top refinement with full order (x,omega,tau), where omega orders V\Z, then has its first change entirely inside tau. No earlier change occurs, and tau has at most one change, contradicting that every full order is bad. Thus Phi|L is zero-free.

#### A zero-free homotopy on the link
For each F as above define
G_F=1_Z/|Z|-1_{A_1}/|A_1| in W_V.
Extend these labels affinely on L. If F_i refines F_0, its first block is contained in the first block of F_0, and its final block is contained in the final block of F_0. Consequently beta(G_{F_i})>0. Also beta(Phi(b_{F_i}))>=0.

For 0<t<=1 the affine map
H_t=(1-t)Phi+tG
is strictly positive under beta on each flag simplex, and is therefore zero-free. At t=0 it is zero-free by the previous paragraph. This homotopes the normalized link map to normalized G.

#### Degree of G
Realize the cube in R^V, with bottom vertex 0, and let P be orthogonal projection onto W_V. For a point q of the geometric link set R(q)=-Pq.

If F_i and F_j belong to the same flag, then
G_{F_i} dot (-P b_{F_j})>0.
To see this, coordinates in the first block of F_i enter the chain of F_j strictly before coordinates in the final block of F_i when F_j refines F_i. If F_i refines F_j, the first block of F_i lies in the first block of F_j, while its final block lies in the zero-coordinate block of F_j. In either case the average coordinate on the first block is strictly greater than on the final block. Since G_{F_i} has coordinate sum zero, projection does not change this dot product.

Bilinearity now gives G(q) dot R(q)>0 throughout every flag simplex. The straight homotopy from G to R is zero-free.

The geometric link meets each ray of the boundary of the positive orthant once. Projection P identifies these rays with the sphere in W_V: its inverse on rays sends z to z-min_v(z_v)1_V. Thus normalized Pq has degree +1 when used as the identifying orientation, and normalized R has degree (-1)^(n-1). In particular the absolute degree is one.

A zero-free extension over the closed star, which is an (n-1)-ball with boundary L, would extend this normalized sphere map into the sphere of W_V. That would force degree zero, a contradiction. This proves the diagnosis. Square.

### Repair obligation
The cube-boundary dimension gain has produced two local extension obstructions rather than closure. The bottom obstruction is already of degree one; the antipodal top obstruction is compatible with oddness. A valid repair must convert a zero inside a pole star into a one-change order, or replace the carrier by one whose link obstruction is incompatible with the coloring. Merely varying positive coefficients, or identifying a flag's smallest face with the location of its zero, cannot complete §34.

This is an audit of the proposed proof, not a refutation of the directed NOR conjecture.
