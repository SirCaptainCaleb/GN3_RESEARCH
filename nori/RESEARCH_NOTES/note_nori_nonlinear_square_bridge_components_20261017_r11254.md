# Square-bridge conservation and mixed-derivative incidence transitions

- Stable ID: note_nori_nonlinear_square_bridge_components_20261017_r11254
- Author: session_nori_r11254_2
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, square-bridge, root-profile-incidence, nonlinear-conservation, spectral-expansion, mixed-derivative, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11254_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_nonlinear_diagonal_graph_expander_20261016_r11254
- note:note_nori_profile_integrability_three_local_laws_20261016_r11254

## Research note

# Nonlinear square-bridge sheets versus connected full-profile incidence

Let c be a legal antipodally odd coloring of Q_n, and W_x its direction-indexed full-geodesic profiles. Its root-profile incidence graph has edges (x,w) whenever w lies in W_x; two roots are called incident-connected if they belong to the same connected component of this bipartite graph. For any two distinct dimensions i,j and square corner x, define
a= c_i(x)+c_i(x+e_j),  b=c_j(x)+c_j(x+e_i),  delta=a e_i+b e_j,
with arithmetic in F_2. Define the square-bridge graph B_c on Q_n by joining x to x+delta whenever delta is nonzero, for all squares and corners.

**Lemma (unrestricted square-bridge transport).** The roots x and x+delta share a complete direction-indexed profile; consequently every component of B_c lies in a root-side component of the incidence graph.

*Proof.* Choose any common suffix rho and let P=(x,(i,j,rho)) and Q=(x,(j,i,rho)). Their profiles differ by delta, because their suffixes use the same edges. If (a,b)=(1,0), one cyclic rotation of P yields a path rooted at x+e_i with profile w(P)+e_i=w(Q). If (a,b)=(0,1), one cyclic rotation of Q has root x+e_j and profile w(Q)+e_j=w(P). If (a,b)=(1,1), two cyclic rotations of P produce root x+e_i+e_j with profile w(P)+e_i+e_j=w(Q). In every case the two roots share a profile. The zero case contributes no edge. QED.

**Theorem (complete classification in the star Boolean family).** Fix n>=2, m=n-1 and a complement-odd Boolean function F:F_2^m -> F_2, F(y+1)=F(y)+1. Write vertices x=(t,y), where t is the bit in dimension 0. Define
c_0(t,y)=F(y),  c_j(t,y)=t for 1<=j<=m.
These are legal rules. The square-bridge graph B_c has precisely two components
C_epsilon={(t,y):t+F(y)=epsilon}, epsilon in F_2,
and each component is isomorphic to Q_m. The full root-profile incidence graph is connected if and only if F is nonaffine. If F is affine, its root-side incidence components are C_0,C_1. If F is nonaffine, there exists a complete profile simultaneously witnessed by roots from both C_0 and C_1; hence the square-generated root partition is strictly finer than incidence connectivity.

*Proof.* Squares between two leaf dimensions have delta=0. A square involving 0 and leaf j has delta=(F(y)+F(y+e_j))e_0+e_j. Its bridge changes (t,y) to (t+F(y)+F(y+e_j),y+e_j), preserving t+F(y). These are all m elementary leaf moves, so each level set C_epsilon is connected by them and is the graph of the function y -> epsilon+F(y) over Q_m. Thus there are two square-bridge components, both abstractly Q_m.

For the incidence graph, consider a rooted full geodesic from (t,y) and let B be the set of leaf dimensions preceding the central direction 0. The leaf profile entries are w_j=t for j in B and w_j=t+1 otherwise, while w_0=F(y+1_B). Setting z=x+w gives
z_leaf=y+(t+1)1+1_B, z_0=1+F(z_leaf),
using complement oddness. As B ranges over every leaf subset, the rooted profile set is
W_(t,y)=(t,y)+Z_F,   Z_F={(1+F(q),q):q in F_2^m}.
For any profile w=(u,v), its supporting roots are
S_w={(1+u+F(y+v),y):y in F_2^m}.
Their square-sheet labels are
t+F(y)=1+u+F(y+v)+F(y)=1+u+D_vF(y).
If F is affine, every Boolean derivative D_vF is constant, so each S_w lies in one sheet. Since every sheet is already square-bridge connected, the two sheets are the root-side incidence components.

If F is nonaffine, at least one first derivative D_(e_j)F(y) is nonconstant: constant first derivatives in all m dimensions would imply F affine by integration along cube edges. For w=e_j (central profile bit zero), the displayed sheet label 1+D_(e_j)F(y) takes both values. Thus S_(e_j) meets both sheets. Its two supporting roots are connected by a common profile, merging the two square components into one incidence component. QED.

**Quantitative all-dimensional example.** For every n>=4 choose F(y)=Maj_3(y_1,y_2,y_3), ignoring any remaining leaf variables. Here Maj_3=y_1y_2+y_1y_3+y_2y_3 over F_2. It is complement-odd and nonlinear. Both square-bridge components have 2^(n-1) roots, and the incidence graph is connected. For any leaf-profile vector v whose first three bits are neither 000 nor 111, D_vF is a nonconstant affine Boolean function and is balanced. Hence for each such complete profile w=(u,v), its 2^(n-1) supporting roots split into 2^(n-2) roots in each square-bridge component. The qualifying v form six of the eight three-bit patterns; therefore three quarters of the 2^n full profile words bridge the two square components with equal support on both sides. The remaining two classes have support within one component of B_c.

The nonlinearity of F produces the separation starting in n=4. For n=2,3 every complement-odd F on m<=2 inputs is affine, so the two connectivity partitions coincide in this family.

**Interpretation.** Every local square-bridge edge is a valid root-profile incidence connection, yet even the transitive closure of all such edges can have two nonlinear components while the full incidence graph is connected and every complete profile is globally attainable. The obstruction concerns generating root-incidence components from single-square exchanges; it does not negate NORI1 or the perfect-matching question. It supplies a rigorous reason to incorporate relations among multiple gallery moves, rather than inferring incidence connectivity from the square-bridge graph alone.

**Corollary (exponential square-bridge fragmentation with expanding incidence).** For every r>=1 there is a legal coloring of Q_(4r) for which the square-bridge graph has 2^r connected components, each isomorphic to Q_(3r), while the complete root-profile incidence graph is connected, 8^r-regular, has diameter four, and has largest nontrivial normalized adjacency eigenvalue of absolute value 1/2.

*Proof.* Take the Cartesian product of r four-dimensional majority-star colorings. Squares involving dimensions from different blocks have zero cross derivatives and contribute no square-bridge edges. Within each block there are two square-bridge components isomorphic to Q_3. Thus the product square-bridge components are indexed by r independent binary sheet labels, and each is Q_(3r).

The four-dimensional complete incidence relation is x+w in Z_4, where Z_4={(1+Maj_3(q),q):q in F_2^3}; the eight signatures are represented by integer masks {1,3,5,6,9,10,12,14}. The root-profile incidence of the r-block coloring has relation x+w in Z_4^r and is 8^r-regular. The difference set Z_4+Z_4 contains 14 of the 16 vectors; threefold and fourfold sumsets fill F_2^4, showing diameter four for the block and every product. The normalized Walsh transform of the uniform measure on Z_4 has nonzero coefficients 1 at the trivial character and coefficients of absolute value 1/2 at the four characters represented by masks {3,5,9,15}. Under Cartesian product, the coefficients multiply. Hence the second absolute normalized adjacency eigenvalue remains 1/2 for all r. This proves the assertions. QED.

In particular, the square-bridge graph can lose a factor of 2^r in connectivity even when the complete incidence graph has dimension-independent spectral expansion and diameter four.

**Three-dimension defect certificate.** In the star family, take two distinct leaf dimensions i,j and a leaf state y such that the mixed Boolean derivative
D_iD_jF(y)=F(y)+F(y+e_i)+F(y+e_j)+F(y+e_i+e_j)
equals one. Set
x=(1+F(y+e_j),y),  x'=(1+F(y+e_i+e_j),y+e_i).
Both roots support the same complete profile e_j, by the supporting-root formula. Their square-bridge sheet labels differ by
[t+F(y)]+[t'+F(y+e_i)]=D_iD_jF(y)=1.
Thus a nonzero mixed derivative gives an explicit common-profile bridge between the two local square components, using only the rules on the three-dimensional face in dimensions {0,i,j} to locate the two roots. Conversely if every mixed derivative vanishes, F is affine and there is no such crossing. This identifies the failure of square-bridge completeness with nonlinear two-leaf interaction, rather than with the size or density of local square-bridge components.
