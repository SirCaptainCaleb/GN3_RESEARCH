# Nonlinear diagonal laws with diameter-four expanding root-profile incidence

- Stable ID: note_nori_nonlinear_diagonal_graph_expander_20261016_r11254
- Author: session_nori_r11254_2
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, root-profile-incidence, nonlinear-conservation, spectral-expansion, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11254_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_anchored_profile_transport_radius_two_20261016_r11254
- note:note_nori_profile_root_incidence_disconnected_20261016_r10917

## Research note

# Nonlinear diagonal law and expander incidence

Write W_x(c) for the direction-indexed full-geodesic profiles from root x, and Z(c)={x+w:w in W_x(c), x in Q_n}.

**Boolean graph theorem.** Let F:F_2^m -> F_2 satisfy F(y+1)=F(y)+1. On Q_(m+1) write x=(t,y), and set c_0(t,y)=F(y), c_j(t,y)=t for 1<=j<=m. This coloring is legal and antipodally odd. For EVERY root x,
W_x(c)=x+Z_F,   Z_F={(1+F(q),q):q in F_2^m}.
Indeed, if B is the subset of leaf directions preceding 0, then w_0=F(y+1_B), w_j=t for j in B and w_j=t+1 otherwise. Thus z=x+w satisfies z_leaf=y+(t+1)1+1_B, and z_0=t+F(y+1_B)=1+F(z_leaf). All subsets B occur, so all q occur. Each root supports 2^m profiles, and each profile has 2^m supporting roots. The root-profile incidence graph has adjacency x+w in Z_F. Its connected components are the cosets of span(Z_F+Z_F), which fills F_2^(m+1) if and only if F is nonaffine. This follows because the graph of 1+F has full affine span if and only if F is nonaffine.

**Uniform expander theorem.** Put F=Maj on three bits, with Maj(q)=q_1q_2+q_1q_3+q_2q_3, and take r independent four-dimensional copies C_r. Then for N=4r,
Z(C_r)=Z_4^r,  |Z(C_r)|=8^r=2^(3N/4),  aff Z(C_r)=F_2^N.
For every x, W_x(C_r)=x+Z(C_r). All full profiles are globally attainable; every root and every profile has incidence degree 8^r. The incidence graph is connected, has DIAMETER FOUR, and its normalized second absolute adjacency eigenvalue is 1/2.

Proof of diameter: Z_4={(1+Maj(q),q):q in F_2^3} and
2Z_4=F_2^4 minus {e_0,e_1+e_2+e_3}.
For leaf difference h, the first-bit difference is Maj(q+h)+Maj(q). It is always zero for h=0, always one for h=111, and takes both values for other h. Because |Z_4|=8 and |2Z_4|=14, any translate of Z_4 meets 2Z_4, and any two translates of 2Z_4 intersect. Therefore 3Z_4=4Z_4=F_2^4. Product sumsets give 3Z(C_r)=4Z(C_r)=F_2^N, proving incidence distances at most three between sides and at most four on one side. The root pair 0,e_0 requires four steps because e_0 is absent from 2Z_4.

Proof of expansion: the normalized incidence matrix is a Walsh-diagonalized convolution kernel 8^(-r)1_(Z_4^r)(x+w). Put s_j=(-1)^(q_j). Then
(-1)^Maj(q)=(s_1+s_2+s_3-s_1s_2s_3)/2.
Thus the uniform law on Z_4 has Walsh coefficient 1 for the trivial character, coefficient of absolute value 1/2 for four nontrivial characters, and zero otherwise. Product Fourier coefficients multiply, so the largest nontrivial singular value is 1/2. The normalized bipartite adjacency eigenvalues are the positive and negative singular values.

**Consequence.** Connected, regular, diameter-four, dimension-uniform expanding root-profile incidence with full affine span can exclude an exponentially growing number of diagonal signatures x+w: only the fraction 2^(-r) occurs. The family satisfies NORI1 and even allows anchored radius-one transport (x,w)->(x+e_i,w+e_i), since x+w is preserved. Consequently incidence expansion alone cannot force diagonal-signature saturation, and nonlinear diagonal constraints need not obstruct monochromatic geodesics.
