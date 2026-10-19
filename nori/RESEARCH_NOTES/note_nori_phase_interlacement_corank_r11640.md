# Isolated chord bound for phase-immune return corank and ten-word Q6 phase forcing

- Stable ID: note_nori_phase_interlacement_corank_r11640
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, affine-holonomy, phase-immune, interlacement, corank, dimension-uniform, geodesic-root-count, Q6, Q10, transported-incidence
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_m5_parity_static_transport_certificate_r11626

## Research note

# Interlacement controls corank of phase-immune affine returns

Let m>=2. In a legal paired-flat Q_(2m) coloring write pair-parity p_i=x_(a_i)+x_(b_i) and first-member q_i=x_(a_i). Suppose the pair gates are affine in q, with possibly parity-dependent slopes:
 f_i(p,q)=a_i(p) dot q + theta_i(p_except_i),
where a_i(p)_i=0 and all phase truth-table entries theta_i(u) can be prescribed independently. Along a fixed pair-label word w=(i_1,...,i_(2m)) containing each label twice, put S_t=I+e_(i_t) a_(i_t)(p_t)^T, L=S_(2m)...S_1, M=L+I, and transported step vectors v_t=S_(2m)...S_(t+1)e_(i_t). The red antipodal return equation is
 Mq=1+sum_t v_t + sum_t v_t theta_(i_t)((p_t)_except_i_t).
Call w phase-immune if this equation is solvable for every phase assignment, allowing starting q to depend on the assignment.

Let H(w) be the chord-interlacement graph: two labels are adjacent if their occurrences alternate. Let I(w) be its isolated-label set.

**THEOREM (dimension-uniform isolated-chord corank bound).** Every phase-immune word obeys
 corank(L+I) <= |I(w)|.
In particular, if H(w) has no isolated labels, then phase immunity is equivalent to invertibility of L+I and the red antipodal starting root q is unique in the prescribed parity fiber for every phase assignment. Generally a phase-immune word gives no more than 2^|I(w)| red starting roots q for each phase assignment.

**PROOF.** First the vectors v_t span F2^m. If z annihilates all v_t, propagate the final covector backwards by z_(2m+1)=z, z_t=S_t^T z_(t+1). Since z dot v_t=(z_(t+1))_(i_t)=0, the transvection S_t^T leaves z_(t+1) unchanged; thus z_t=z at all steps and z_(i_t)=0 for every label. Hence z=0.

For label i with occurrences r<s, the two phase keys agree iff for each j !=i the number of occurrences of j strictly between r,s is even, i.e. iff no label interlaces i. For any z in ker(M^T), phase immunity implies z dot v_r=z dot v_s=0 for each nonisolated label, because those two occurrences read independent phase entries. For isolated i it implies z dot (v_r+v_s)=0, because both occurrences read the same phase entry. Consequently the linear map
 ker(M^T) -> F2^(I(w)), z |-> (z dot v_(first_i))_(i in I(w))
is injective: a vector in its kernel annihilates every v_t, hence vanishes. Thus the left nullity, namely corank M, is at most |I(w)|. If |I(w)|=0, M is invertible, which conversely makes the return equation solvable for every phase assignment. The root count is 2^corank M. QED.

**COROLLARY (single-phase fragility).** If H(w) has no isolated labels and M is singular, then from any phase assignment admitting a red w-geodesic, changing one independent phase truth-table entry destroys ALL red w-geodesics rooted in that parity fiber. For a nonzero z in ker M^T, the full span ensures some z dot v_t=1; that occurrence has a unique phase key, so toggling it violates z-orthogonality of the return right-hand side.

**SHARPNESS.** For m=5 take static odd slope masks (2,1,1,1,1), and word 2340101432. Its isolated labels are {2,3,4}. The symbolic transported return is phase-immune with corank(L+I)=3; the upper bound is attained and it gives eight red q-roots for every phase assignment.

**FINITE AUXILIARY CERTIFICATE.** A standard-library checker tested all 4096 parity-varying odd-slope systems for m=3 and all 30 admissible pair words, verifying the theorem in each of 122880 systems/words. There are 39936 phase-immune pairs: 26112 with corank zero and 13824 with corank one. A fixed ten-word portfolio, namely (021210,102120,120120,120201,120210,201201,201210,210102,210120,210210), has some phase-immune word for every slope system, thus strengthens the prior Q6 twelve-word fixed portfolio. It also verifies the m=5 sharpness example. Full self-contained proof nori_phase_interlacement_corank.md and independent checker nori_phase_interlacement_verifier.py.

**SCOPE.** The corank theorem works with parity-varying affine slopes, and its proof uses neither oddness nor a prescribed Boolean degree beyond affine q-dependence. It is an unconditional structural restriction on any candidate phase-immune word, but does not guarantee a phase-immune word in general dimensions or apply directly to gates nonlinear in q. NORI1 is unresolved.

## All-dimensional Gauss-Seidel determinant forcing

Let A be a zero-diagonal odd-row slope matrix independent of pair parity, while phase functions theta_i(p_except_i) are arbitrary Boolean functions. For any permutation pi of the pair labels let T_pi=S_(pi_m)...S_(pi_1), with S_i=I+e_i a_i^T; the double sweep w=pi pi has linear return matrix L_w=T_pi^2.

**THEOREM.** det(L_w+I)=det A over F2, and the word pi pi is phase-immune if and only if A is nonsingular. If A is nonsingular, that SAME prescribed word yields a red full antipodal geodesic from a unique starting q in EVERY prescribed parity fiber, for EVERY choice of nonlinear phase functions.

**PROOF.** Relabel so pi=(1,...,m), write A=B+C with B strictly lower triangular, and let delta=T_pi q+q. During one sweep each bit changes once; at step i,
 delta_i=(Aq)_i+sum_(j<i) a_ij delta_j.
Hence (I+B)delta=Aq and T_pi+I=(I+B)^(-1)A. As I+B has determinant one, det(T_pi+I)=det A. In characteristic two T_pi^2+I=(T_pi+I)^2, proving det(L_w+I)=det A. If A is nonsingular, every affine return equation has one q solution. If A is singular, the chord diagram of pi pi is fully interlaced (with no isolated chords). The isolated-chord theorem already proved in this note then precludes phase immunity. QED.

**GRAPH COROLLARY.** Interpret a_ij=1 as an arc j->i. Since det A counts directed spanning cycle covers modulo two, an odd number of cycle covers (including a unique cycle cover) guarantees a red full antipodal geodesic in every parity fiber for every phase assignment, using any double sweep. This is a graph-theoretic, unbounded-dimensional positive forcing condition, not a necessary condition.

**INDEPENDENT AUDIT.** The checker nori_double_sweep_gauss_seidel_check.py tested all 256 odd slope matrices at m=4 (88 nonsingular) and all 32768 at m=5 (10048 nonsingular), comparing the sweep rank and the phase-immune return condition against det A. All passed. Complete proof nori_double_sweep_gauss_seidel.md. For singular A other, partially noninterlaced words may still be phase-immune.
