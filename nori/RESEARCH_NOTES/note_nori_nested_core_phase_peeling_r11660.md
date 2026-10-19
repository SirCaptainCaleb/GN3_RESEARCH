# All-dimensional nested-core phase-immune forcing and odd-matrix peeling conjecture

- Stable ID: note_nori_nested_core_phase_peeling_r11660
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, affine-holonomy, dimension-uniform, phase-immune, principal-minor, odd-indegree-peeling, nested-chords, constructive-forcing
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_phase_interlacement_corank_r11640
- note:note_nori_m5_parity_static_transport_certificate_r11626

## Research note

# Nested-core phase immunity and odd-matrix peeling

Let a legal paired-flat Q_(2m) coloring have gate rules f_i(p,q)=sum_(j!=i) a_ij q_j + theta_i(p_except_i) over F2. The arbitrary Boolean phase functions may be nonlinear. The parity-independent slope matrix A has zero diagonal and A1=1.

**ALL-DIMENSIONAL THEOREM.** Select an ordered sequence of outer pair labels i_1,...,i_k and denote by R the remaining labels (|R|>=2). Suppose det A[R,R]=1 and sum_(s<t) a_(i_t,i_s)=0 for every t. Then, for ANY permutation pi of R, the pair word
  w=i_1 ... i_k pi pi i_k ... i_1
gives precisely 2^k all-red full antipodal geodesics rooted in EVERY prescribed initial pair-parity fiber, for EVERY Boolean phase assignment. The order depends only on A, never on the phase truth tables.

**PROOF.** Each red pair step is an invertible operation. Select arbitrarily the k outer q-bits just after their first steps. During the core double sweep pi pi, these bits and their parities remain fixed. The core linear return on q_R obeys det(L_R+I)=det A[R,R]=1 by the Gauss-Seidel determinant theorem, so its red antipodal return equation has one solution for every affine phase offset. Thus all core q-bits end complemented. Reinsert outer steps in reverse. At the second visit to label i_t, all deeper pair bits have completed their antipodal changes, earlier outer bits are fixed, and every other pair parity equals its value at the first visit; theta_(i_t) ignores its own parity, so its phase is unchanged. The gate color changes by
  sum_(j in R union {i_(t+1),...,i_k}) a_(i_t,j)
  =1+sum_(s<t) a_(i_t,i_s)=1.
The second red step therefore traverses the other member of pair i_t, finishing that pair antipodally. Reverse induction closes every outer pair. The initial k-step red prefix is invertible, giving one initial root per chosen k-bit outer state, hence 2^k witnesses. QED.

**GRAPH AND CHORD INTERPRETATION.** Orient an influence arc j->i when a_ij=1. The core has odd directed cycle-cover parity. The outer vertices can be deleted so that each removed vertex receives even incoming influence from earlier deletions, equivalently odd indegree in the current remaining graph because A1=1. The resulting word has k isolated chords in its interlacement graph and return corank k; it saturates the earlier isolated-chord bound.

**FULL FINITE AUDIT.** A subset-DP peeling algorithm and an independent symbolic affine-return verifier checked ALL odd zero-diagonal matrices through m=5. Every matrix admits a valid peel, and the nested word is phase-immune with corank k. Counts by k are: m=3 (2,6); m=4 (88,76,92); m=5 (10048,8378,6035,8307). The standalone symbolic checker evaluated all 32768 m=5 matrices and confirmed the root-count statement. It also checked every eligible single-outer-label principal minor: 6, 224, and 39360 matrix/label pairs in dimensions m=3,4,5 respectively. As illustration, slope row masks (2,1,1,1,1) admit peel (2,3,4), core {0,1} and word 2340101432, producing eight phase-independent red starting roots in every parity fiber. Exploratory random tests found valid peels in 200000 six-pair systems and additional samples through nine pairs; these are not proofs in those dimensions.

**OPEN ODD-MATRIX CONJECTURE.** Every zero-diagonal binary A satisfying A1=1 admits ordered deletions with even incoming parity from previously deleted vertices, leaving a nonsingular principal submatrix. Proving this would establish fiberwise red-geodesic existence for ALL parity-static affine paired-flat legal colorings of every even dimension, despite arbitrary nonlinear parity phases. This remains UNPROVED. Fully general NORI1 (parity-varying slopes or q-nonlinear gates) also remains open.

**REPRODUCIBILITY.** Full proof nori_nested_sweep_elimination.md; standalone exhaustive certificate nori_nested_sweep_certificate.py. Session session_nori_r11510_3.

**STRONGER COROLLARY: PARITY-VARYING AFFINE SLOPES.** The nested forcing proof does not require slopes independent of pair parity. Let f_i(p,q)=a_i(p) dot q+theta_i(p_except_i), with a_i(p) odd-weight, zero on self, and independent of p_i. Fix a prescribed starting parity, outer labels i_1,...,i_k, and an inner double-occurrence pair word v on complementary labels R. Let p^(t) be the parity state before the first outer occurrence of i_t; require sum_(s<t) a_(i_t)(p^(t))_(i_s)=0 for every t. Along the inner parity trajectory after the outer prefix, let L_(R,v) be the homogeneous affine-return matrix acting on inner q_R, using time-dependent slope shears evaluated at each visited parity. If det(L_(R,v)+I)=1, then the nested word i_1...i_k v i_k...i_1 gives precisely 2^k red full antipodal starting q-roots in the prescribed parity fiber, for ANY choices of phase truth tables. Proof: the inner return equation has a unique q_R solution for each arbitrary fixed postprefix outer q-state; during nested return, each outer gate has the same coefficients and phase at its two occurrences because all other parities are restored and it ignores its own parity. Its output changes by the odd sum of slope entries on inner labels, hence the two red steps traverse opposite directions. The first outer prefix is bijective. This is an all-dimensional positive criterion, not a universal existence theorem for parity-varying slopes. A separate simulator tested 2000 random five-pair systems with varying slope tables and nonlinear phases; for each, it directly simulated all 32 starting q-states and found precisely eight red antipodal roots for the selected nesting.
