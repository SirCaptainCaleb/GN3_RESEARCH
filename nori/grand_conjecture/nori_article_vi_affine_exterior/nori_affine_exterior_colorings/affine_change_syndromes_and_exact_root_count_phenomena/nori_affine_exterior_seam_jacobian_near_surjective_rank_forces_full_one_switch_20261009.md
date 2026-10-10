# Near-full affine exterior seam Jacobian rank forces a full one-switch geodesic

# Full antipodal geodesic from near-full affine exterior Jacobian rank

Let n>=4. Consider any binary coloring of PHYSICAL ordered 3-faces Q_n such that for each ordered direction triple t=(a,b,c), its color as a function of the fixed exterior bits x_j (j∉t) is affine over F_2:
  c_t(x)=a_t + Σ_(j∉t) b_(t,j) x_j.
For legal NORI reversal-odd colorings the coefficients satisfy b_(reverse t,j)=b_(t,j) and
  a_(reverse t)=1+a_t+Σ_(j∉t)b_(t,j).
The theorem below does not require this global antipodal symmetry.

Fix any FULL direction order p=(p1,...,pn), put t_i=(p_i,p_(i+1),p_(i+2)), i=1,...,n−2, and let W_p(x) be the (n−2)-window color word of the genuine antipodal path rooted at x in order p. The seam/switch vector D_p(x)∈F_2^(n−3) is defined by
  D_(p,i)(x)=W_(p,i)(x)+W_(p,i+1)(x).
Because each physical window uses the prefix-toggled exterior bits, D_p is itself an AFFINE map
  D_p(x)=M_p x+d_p.
Its (n−3)×n Boolean coefficient matrix is given explicitly by
  (M_p)_(i,j) = 1[j∉t_i] b_(t_i,j) + 1[j∉t_(i+1)] b_(t_(i+1),j)  mod 2.
All prefix effects contribute only to d_p.

**THEOREM (near-surjective seam rank forces grand geodesic).** If rank_F2(M_p)>=n−4 for even ONE full direction order p, then an ACTUAL full antipodal geodesic with at most ONE ordered-three-face color change exists. A suitable starting cube vertex is obtained by solving at most n linear equations over F2.

**Proof.** Let m=n−3, so D_p(F_2^n) is an affine subspace L⊂F_2^m of dimension rank(M_p)>=m−1. If rank=m, then L=F_2^m, containing zero. If rank=m−1, L is an affine hyperplane given by a nonzero linear functional ℓ·y=ε. When ε=0, zero belongs to L. When ε=1, choose any i with ℓ_i=1; then the unit vector e_i belongs to L. In each case some x has D_p(x) in {0,e_1,...,e_m}; its physical window word has at most one switch. QED.

**Exact consequence for a hypothetical AFFINE-exterior NORI counterexample.** For EVERY n-direction order p, its seam Jacobian rank must be at most n−5. In particular any affine-exterior Q7 counterexample has rank(M_p)<=2 simultaneously for all 7! orders. A single nonzero 3×3 minor in any Q7 seam Jacobian closes the conjecture for that coloring. This is a concrete low-rank matrix obstruction independent of color intercepts.

**Connection to nonlinear exterior cohomology.** The teammate's median second-cohomology theorem (nori_median_boolean_hessian_injection_second_cohomology_20261009) gives exact detection of NONAFFINE face fibers by mixed exterior square differences. Thus the unrestricted grand project admits a natural split: (1) nonzero Boolean Hessian / face-fiber curvature, and (2) zero Hessian plus an exceptionally low-rank seam Jacobian in EVERY direction order. The present theorem settles every high-rank member of branch (2), while branch (1) needs a local-to-global path extraction mechanism.

**Further frontier.** Classify reversal-odd affine coefficient tensors b_(t,j) for which ALL order-wise matrices M_p have rank≤n−5. Determine whether the residual low-rank tensors necessarily admit a one-switch direction sequence by a tournament/path-exchange argument.

**THEOREM 2 (complete linear-code syndrome extraction).** For ANY full order p, let m=n−3, let H_p be an ℓ×m full-row-rank Boolean matrix whose row space is the left kernel of M_p (so ℓ=m−rank M_p), and let s_p=H_p d_p. Then an actual good full geodesic of this FIXED order p exists if and only if
  s_p∈{0,H_p e_1,...,H_p e_m}.
Proof: the affine switch-word image is exactly {y∈F_2^m:H_p y=s_p}; zero and the unit vectors represent precisely the words of at most one switch. Membership and a witnessing cube root are found by Gaussian elimination. This is an exact coding-theoretic criterion for EVERY affine exterior coloring, independent of global oddness.

**THEOREM 3 (canonical two-parity obstruction at corank 2).** Suppose rank M_p=m−2. If this order p has NO good starting root, then there are DISJOINT NONEMPTY seam index sets I,J⊂[m] such that for EVERY cube root x,
  Σ_(i∈I)D_(p,i)(x)=1  and  Σ_(j∈J)D_(p,j)(x)=1
modulo 2. Conversely these two fixed odd parity constraints imply every word has at least two switches.

Proof: H=H_p has two independent rows, and absence of good roots means s=Hd is neither zero nor any column of H. Because rank(H)=2, its columns contain two distinct nonzero vectors u,v, and the third nonzero vector u+v must be s. Apply an invertible 2×2 change of row basis sending u→(1,0), v→(0,1), s→(1,1). Every H column lies in {(0,0),(1,0),(0,1)}, since (1,1)=s is excluded. The two row supports I,J are therefore disjoint and nonempty; H D(x)=s gives both odd parity identities. Conversely two disjoint parity-one constraints require at least one switch in each support. QED.

**Q7 implication.** For an affine-exterior Q7 counterexample all order-wise ranks are ≤2. At the extremal rank2, every bad order carries an exact pair of disjoint odd-switch index sets among its four seams. Seek incompatibility between these paired parity partitions under physical adjacent transpositions and antipodal reversal. The remaining ranks0,1 require separate control.
