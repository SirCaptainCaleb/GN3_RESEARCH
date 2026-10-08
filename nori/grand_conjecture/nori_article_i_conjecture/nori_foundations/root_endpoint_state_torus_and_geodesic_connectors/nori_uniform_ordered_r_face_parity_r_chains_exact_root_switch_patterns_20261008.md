# Ordered r-face parity theorem: exactly 2^r roots for every switch pattern and nonlinear fault tolerance

# Uniform ordered-r-face exterior parity: r independent chains, exactly 2^r roots for every switch pattern

Fix integers 1<=r<n. Let Q_n have a binary coloring of ORDERED PHYSICAL r-dimensional cube faces of the form
 c(F,(i_1,...,i_r)) = h(i_1,...,i_r) + Σ_(t notin {i_1,...,i_r}) a_t z_t  (mod2),
where h is an arbitrary binary function of ordered distinct direction r-tuples, the vector a∈F2^n is FIXED (the same a across all ordered r-faces), and z_t denotes the exterior bit of the physical face. This is genuinely face-local and independent of its choice of corner. No antipodal oddness is needed.

A full antipodal n-edge geodesic with root x and direction order pi=(p_1,...,p_n) has L=n−r+1 consecutive ordered-r-face window colors. Its change vector has m=L−1=n−r bits.

**Theorem 1 (r-chain exact controllability).** Suppose in each of the r index progressions
  q, q+r, q+2r,... <= n  (q=1,...,r)
there is AT MOST ONE position t with a_(p_t)=0. Then the root-to-change map
  D_pi:F2^n -> F2^(n−r)
is affine and SURJECTIVE. Each of its 2^(n−r) output change patterns is realized by exactly 2^r distinct cube roots. In particular, exactly 2^r roots yield a fully MONOCHROMATIC antipodal geodesic along pi, and exactly
  2^r * binom(n−r,t)
roots yield precisely t consecutive ordered-r-face window color changes (0<=t<=n−r).

**Proof.** Moving from r-window j=(p_j,...,p_(j+r−1)) to window j+1 removes p_j after that coordinate has been flipped and adds p_(j+r) before that coordinate has been flipped. Let h_j=h(p_j,...,p_(j+r−1)), and denote the binary root bits by x_i. Then
 C_j+C_(j+1)
  = h_j+h_(j+1) + a_(p_j)(1+x_(p_j)) + a_(p_(j+r)) x_(p_(j+r)).
Thus requiring any prescribed binary switch pattern y_j gives the (n−r) affine linear equations
  a_(p_j)x_(p_j) + a_(p_(j+r))x_(p_(j+r))
   = y_j+h_j+h_(j+1)+a_(p_j),   j=1,...,n−r.
The left-hand sides connect position indices j and j+r, partitioning into r disjoint path systems (forest). On each chain, all but at most one variable have coefficient1; the path incidence matrix with one possible zero column has full ROW rank (#vertices−1), so there is exactly one unrestricted variable per chain and exactly two solutions per chain, independently of the right-hand side. The full map is therefore onto with exactly 2^r roots per change pattern. QED.

**Theorem 2 (any h, at most r zero coefficients -> full monochromatic geodesic).** If a has at most r zero coordinates, choose pi placing those zeros into DISTINCT residue chains modr. Then Theorem 1 gives a MONOCHROMATIC FULL antipodal geodesic, for ANY ordered-tuple function h. This is stronger than the corresponding at-most-one-switch NORI-type conjecture for this broad affine-exterior subclass.

**Theorem 3 (exact full-parity counts).** If all a_i=1 then EVERY permutation pi is admissible. The number of fully monochromatic DIRECTED antipodal geodesics is EXACTLY 2^r n!, and the number of directed antipodal geodesics whose window word has at most one change is EXACTLY
   2^r (n−r+1) n!.
This counts starting roots and full ordered direction sequences; each path is uniquely specified by them. The proportions among the 2^n n! total full antipodal geodesics are respectively 2^(r−n) and (n−r+1)2^(r−n).

**Theorem 4 (arbitrary nonlinear corrupted window types).** Under the surjectivity hypothesis of Theorem1 for some chosen pi, suppose another physical ordered-r-face coloring c' agrees with c on the physical face colors of all but k of the L consecutive ordered-r-direction window TYPES of pi (for every exterior-bit assignment); the exceptional k types may be ARBITRARY NONLINEAR functions of their exterior bits. Then there is a full antipodal pi-geodesic of c' with at most k window color changes, witnessed by at least 2^r roots. Proof: choose a baseline binary color-word shape whose nonexceptional runs are constant and the endpoint colors across each internal length-ell corrupted block differ by ell modulo2. Any arbitrary replacements in that block create at most ell changes, by parity of transitions. Because D_pi of c is onto, realize that baseline change vector with 2^r roots, each of which inherits the <=k bound under the corruption. For k=1, this gives FULL one-switch closure even with one completely arbitrary nonlinear r-face-window type.

**Antipodal-reversal oddness compatibility.** For ordered-r-face NORI-type axiom c(bar F,rev pi)=1+c(F,pi), the common-a coloring satisfies it iff
  h(rev pi)+h(pi)=1+Σ_(t notin support(pi))a_t
for every ordered r-tuple. Since r>=2 implies pi and rev pi differ, choosing one member of each reversal pair and assigning the other by this equation is consistent for every a. When r=1, reversal fixes pi, so the axiom requires Σ_(t≠i)a_t=1 for every i; Theorems 1–4 do not depend on this axiom and remain valid separately.

**Research significance and limitations.** This generalizes the ordered-three-face modulo-three chain theorem to every window arity r, and explains the fixed residual 2^r root degrees as the codimension of an r-path incidence forest, not as a numerical coincidence. It also transfers the nonlinear-exception robustness argument to arbitrary r. The hypotheses require one common exterior affine coefficient vector a for nonexceptional windows. Arbitrary active NORI order-three-face colorings may vary nonlinearly with exterior bits at MANY triple types, so the unrestricted grand conjecture is NOT resolved.
