# Affine NORI syndrome theorem: full geodesic with at most change-map codimension switches

# Affine exterior-coloring: exact rank/coding-theory criterion for full NORI one-switch closure

Let n>=4 and let c be ANY binary coloring of physical ORDERED three-faces of Q_n, whose color is affine in the n−3 exterior cube bits. More explicitly, for every ordered distinct triple (i,j,k), there are coefficients h_(i,j,k)∈F2 and a_(i,j,k),t ∈F2 (t notin{i,j,k}) such that
 c(F,(i,j,k)) = h_(i,j,k) + sum_(t notin{i,j,k}) a_(i,j,k),t z_t  (mod 2).
The coefficient pattern is allowed to depend ARBITRARILY on the entire ordered triple; the only requirement is affine dependence on the actual exterior-bit assignment. A valid active NORI oddness condition imposes extra linear relations on these coefficients (a_revπ,t=a_π,t and the constant terms satisfy the corresponding complement relation), but the conclusions below do NOT require oddness.

Fix ANY full direction permutation pi=(p1,...,pn). For root x∈F2^n, let C_pi(x)∈F2^(n−2) be the consecutive ordered-three-face-window colors along the full antipodal pi-geodesic from x. Every coordinate of C_pi(x) is affine in x by the hypothesis and the fact that preceding cube flips only add a constant. Define the *change vector*
 D_pi(x)=(C_1+C_2, C_2+C_3,...,C_(n−3)+C_(n−2))∈F2^m, m=n−3.
Thus there exists an m×n binary matrix M_pi and offset b_pi such that
   D_pi(x)=b_pi+M_pi x.
The number of full-geodesic window-color switches is exactly the Hamming weight |D_pi(x)|.

**Theorem 1 (general affine codimension bound).** Put r_pi=rank_F2(M_pi), c_pi=m−r_pi. There is ALWAYS a root x with at most c_pi color changes along direction order pi. In particular,
  rank(M_pi)=n−3  =>  a fully MONOCHROMATIC full antipodal pi-geodesic;
  rank(M_pi)>=n−4 =>  a full antipodal pi-geodesic with AT MOST ONE change.
These statements hold even without the active NORI antipodal-reversal axiom.

**Proof (short syndrome decoder).** Let V=im(M_pi)⊆F2^m, of codimension c_pi. Choose any surjective linear quotient/syndrome map H:F2^m→F2^(c_pi) with ker H=V. The affine output set is b_pi+V, i.e. precisely the solutions y of H y=H b_pi. Because H has full row rank c_pi, it possesses c_pi LINEARLY INDEPENDENT columns. They form a basis of F2^(c_pi). Express syndrome H b_pi in that basis, using a subset of at most c_pi columns. Let y∈F2^m be its indicator vector, with |y|<=c_pi. Then H y=H b_pi, hence y belongs to b_pi+V, so y=D_pi(x) for some actual cube root x. The corresponding full pi-geodesic has at most c_pi changes. If c_pi=0 choose y=0; if c_pi=1 choose y=0 or a single unit coordinate. QED.

**Theorem 2 (exact affine NO-GOOD obstruction).** For a fixed pi the following are equivalent:
(i) EVERY root x yields at least two window-color changes;
(ii) (b_pi+im M_pi) ∩ {0,e_1,...,e_m}=empty;
(iii) with H a full-row-rank parity-check matrix for im M_pi and syndrome s=H b_pi, one has
   s != 0 and s != H e_j for EVERY j=1,...,m.
Consequently c_pi>=2, i.e.
  rank(M_pi)<=n−5.
Conversely if c_pi>=2 it is still possible that a good root exists: the syndrome condition in (iii), not rank deficiency alone, is exact.

Thus a hypothetical counterexample to the full ACTIVE NORI grand conjecture **within affine-exterior colorings** must have the incredibly restrictive property
   for EVERY direction order pi, rank_F2(M_pi) <= n−5
AND all its affine syndromes avoid zero and every single-column syndrome. This is a concrete finite set of linear-algebraic constraints spanning ALL coordinate permutations, and is a promising target for an exchange/descent or signed-root obstruction.

**Theorem 3 (counting root witnesses).** Every attainable y∈b_pi+im(M_pi) has exactly 2^(n−r_pi) root preimages. Therefore Theorem 1 supplies at least 2^(n−r_pi) distinct starting vertices witnessing at most c_pi switches along the same permutation. If active NORI oddness holds, reversing the full direction order pi↦rev(pi) produces the reversed-complemented color word at the SAME root, so the multiset of switching patterns and root witnesses is identical after reversing the m change coordinates. In particular any nonempty class of good paths comes in reversal-conjugate pairs of orders.

**Limitations.** The rank argument does NOT automatically produce an order pi with rank>=n−4; a coloring constant across each physical face's exterior bits (coordinate-only oriented-triple labeling) has M_pi=0 for every pi but can nevertheless have good permutations, as separate combinatorial arguments show. A nonlinear coloring in the exterior bits need not give an affine change map at all. Therefore this is a new PROVED structural and quantitative closure criterion for the affine subclass, not a universal solution of NORI.
