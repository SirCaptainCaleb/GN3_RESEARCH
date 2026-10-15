# Critical-dimensional contraction of rational switch bivectors

### Critical-dimensional rational contraction for switch bivectors

The extreme-switch bivectors in this Article are rational two-vectors in the type-A reflection space. There is an explicit fixed contraction which preserves their zero sets and pairwise ray relations and takes values in a real vector space of dimension n-2. This corrects the previous target-dimension count: contraction by u of any skew tensor lies in u-perp.

Let n>=4 and W={z in R^n: sum_i z_i=0}. Represent every bivector Xi in Lambda^2W by its associated skew-symmetric matrix A_Xi, which annihilates the all-ones vector. Choose an integer M>2*3^{n-1}, put theta=2^{1/M}, and define
[
v=(	heta^{3^0},	heta^{3^1},ldots,	heta^{3^{n-1}}),qquad
u=v-rac1nleft(sum_{i=1}^n v_iight)mathbf1.
	ag{1}
]
The polynomial X^M-2 is irreducible over Q by Eisenstein at two. Put
[
H_u=Wcap u^perp,qquad
oxed{mathcal C_u(Xi)=A_Xi uin H_u.}
	ag{2}
]
Skew-symmetry gives u dot A_Xi u=0 and A_Xi1=0 gives membership in W. Thus dim H_u=n-2.

**Lemma 1 (linear dependence rigidity).** For two real skew-symmetric matrices A,B, if Av and Bv are linearly dependent for every real vector v and A is nonzero, then B=lambda A for some real scalar lambda.

*Proof.* The nonzero skew matrix A has rank at least two, so choose x,y with Ax and Ay independent. For each z with Az nonzero write Bz=lambda(z)Az. Applying the dependence assumption to x+y shows lambda(x)=lambda(y). For arbitrary z with Az nonzero, select one of x,y with A-image independent of Az; applying dependence to their sum gives the same scalar. For k in ker A, applying dependence to x+k and y+k shows Bk belongs to both span(Ax) and span(Ay), whence Bk=0. Therefore B=lambda A. QED.

**Theorem 2 (universal projective faithfulness).** For every rational bivector Xi in Lambda^2(W intersect Q^n),
[
oxed{Xi
e0impliesmathcal C_u(Xi)
e0.}
	ag{3}
]
For any two real-linearly independent rational bivectors Xi,Psi,
[
oxed{mathcal C_u(Xi),mathcal C_u(Psi)
	ext{ are real-linearly independent.}}
	ag{4}
]
Thus the map preserves positive rays, negative rays, and noncollinearity of pairs of nonzero rational bivectors.

*Proof.* Write A,B for the rational skew matrices representing Xi,Psi. Since A1=B1=0, we may replace u by v when evaluating Au or Bu. Each entry of Av is the value at theta of a polynomial sum_i a_i X^{3^{i-1}} with rational entries. Such a polynomial is nonzero for any nonzero matrix row and has degree at most 3^{n-1}<M. Hence Av is nonzero by the irreducibility of X^M-2. This proves (3).

If A and B are nonproportional, Lemma 1 says the columns Av and Bv are independent for some real vector v. Hence some two-by-two minor of the variable matrix [Az,Bz] is a nonzero homogeneous quadratic polynomial in the n entries of z. Substituting z_i=X^{3^{i-1}} maps distinct monomials of degree two to distinct powers of X: the base-three expansions of 3^{i-1}+3^{j-1}, including i=j, are different. Thus this minor becomes a nonzero rational polynomial of degree at most 2*3^{n-1}<M. It cannot vanish at theta. Its value at theta is a nonzero minor of [Au,Bu], proving (4). For real proportional rational tensors the scalar is rational and contraction preserves its sign. QED.

**Corollary 3 (one-skeleton map in the critical dimension).** Let an unrestricted boundary 3-tournament on n>=5 vertices have at least two switches on every full Hamilton order. At each complete flag pi define
[
F(pi)=mathcal C_uigl(Z_{a+1}(pi)wedge Z_{b+1}(pi)igr)in H_usetminus{0},
	ag{5}
]
with a<b the first and last switch positions. Then F(pi-reversed)=-F(pi). The previously established adjacent-exchange theorem shows that neighboring extreme-switch bivectors are never antiparallel. By Theorem 2 neither are their F-images. Radial normalization of straight-line edges therefore gives an antipodally equivariant map on the dual type-A one-skeleton into
[
oxed{S(H_u)cong S^{n-3}.}
	ag{6}
]
The contraction is fixed independently of the coloring. For NORI1 cube geodesics the same property holds across root-changing exchanges; only the two exceptional terminal dimension-order exchanges require nonlinear edge paths.

**Scope.** This algebraic result supplies the critical-dimensional odd vertex labels and their boundary one-skeleton interpolation. It does not produce a continuous map on the entire flag sphere; Borsuk--Ulam forbids such a map under the no-good-path hypothesis. In particular rank-three convex cancellations remain possible, as the preceding Subsection proves. The unfinished mathematical step is a coherent color-sensitive extension over the remaining rank-exchange cells while retaining the original full-path incidence constraints.
