# Antipodal signed matchings and perfect-square Pfaffians

- Stable ID: note_nori_signed_complex_structures_pfaffian_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, complex-structures, Pfaffian, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For a legal antipodally odd edge coloring c on Q_n, write T_i|x>=|x+e_i>, P|x>=|bar x>, and S_i|x>=(-1)^{c_i(x)}|x+e_i>. Undirected consistency gives S_i^2=I and S_i^T=S_i; antipodal oddness gives PS_iP=-S_i. Thus J_i=S_iP is real orthogonal skew with J_i^2=-I, for every direction i. Its support joins x to x+1+e_i. Flipping one legal antipodal direction-i edge orbit reverses two distinct skew matching blocks, so Pf(J_i) is independent of c and equals plus or minus one (depending only on fixed basis order). For J(t)=sum t_i J_i and odd n>=3, the complementary-direction moves have even Hamming weight and preserve vertex parity. The antipode exchanges parity blocks and conjugates J(t) to its negative. Their Pfaffians agree up to fixed sign, giving Pf(J(t))=sigma_n Pf(J_even(t))^2. For even n, all J_i interchange parity, so J(t) has block form [0,B;-B^T,0] and Pf(J(t)) is, up to fixed sign, det B. The F2 linear map L=I+11^T carries e_i to 1+e_i: when n even L^2=I, giving a dual ordinary cube; when n odd L has kernel span(1) and image even-parity subspace, giving two folded-cube sectors. Important limitation: for n=3 the legal unary coloring c_0=x_1,c_1=x_0,c_2=x_1 gives Pf(J_even(t))=-t_0^2+t_1^2+t_2^2, so nonzero signed combinations may be singular. For c_0=x_1,c_1=x_2,c_2=x_0 the quadratic is -(t_0^2+t_1^2+t_2^2). Therefore a sign-definite-Pfaffian closure argument fails. This is a dimension-uniform algebraic structural theorem, not a NORI1 proof.
