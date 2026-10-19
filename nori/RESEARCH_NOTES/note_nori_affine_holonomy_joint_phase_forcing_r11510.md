# Dimension-uniform affine return holonomy, adaptive six-cube certificates, and nonlinear eight-cube phase transport

- Stable ID: note_nori_affine_holonomy_joint_phase_forcing_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, affine-holonomy, dimension-uniform, F2-linear-algebra, joint-compatibility, parity-certificates, fiberwise-Q6, nonlinear-Q8, root-order-transport, positive-forcing
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_q6_parity_fiber_sharp_q8_global_sat_r11510
- note:note_nori_cyclic_pair_gate_sensitivity_product_r11510

## Research note

# Affine red-return holonomy and cross-order parity forcing

**Dimension-uniform theorem.** Write the pair directions of an antipodally odd paired-flat Q_(2m) as P_i={a_i,b_i}, with q_i=x_(a_i) and pair parity p_i=x_(a_i)+x_(b_i) over F2. Assume each pair gate has an affine restriction to every parity fiber:
 f_i(p,q)=a_i(p) dot q + theta_i(p),
 where (a_i(p))_i=0, a_i(p) dot 1=1, and both a_i,theta_i ignore p_i. The phase functions may be nonlinear in the other p-bits. A red step with pair label i changes p_i to p_i+1 and q_i to q_i+1+f_i(p,q). Therefore for any pair-label word w with two appearances of each i, its red return map on a fixed starting parity fiber is affine:
 q_final=A_w(p) q + b_w(p,theta),
 where A_w is a product of elementary shears and b_w is affine in all phase truth values. A red full antipodal geodesic exists with that word precisely when
 (A_w(p)+I)q=1+b_w(p,theta).                    (AH1)
If r=rank(A_w+I), the word has either zero or 2^(m-r) successful starting q-states. If r=m it always has a unique witness independent of the phase values. If r=m-1, its success condition is one affine equation lambda_w(theta)=0, obtained by pairing 1+b_w with the unique nonzero left-null vector. A finite family of such words forces success for every phase assignment whenever the complementary failure equations lambda_w(theta)=1 are linearly inconsistent. This gives a root-and-order compatible parity certificate from the same coloring. Proof: compose the red shears and apply linear algebra over F2.

**The Q6 adaptive six-word theorem.** For m=3, antipodal oddness forces each fixed-p gate to be a signed unary reader of one of the other two q-bits. Each pair gate has four independently chosen reader selections and four independently chosen phase values, giving 12 selector bits and 12 phase bits in all. Translate the prescribed starting pair parity to zero. Any red geodesic must have a pair-label word using 0,1,2 twice without adjacent equal labels; there are 30 such words. A complete 4096-pattern selector audit using (AH1) gives:
 - In 3826 reader systems, some word has invertible A_w+I and succeeds for all phase values.
 - In the remaining 270 systems, a portfolio of at most SIX corank-one words has linearly inconsistent failure equations lambda_w=1. The deterministic certificate lengths are 1:126, 2:30, 3:46, 4:38, 5:18, 6:12.
Therefore every starting pair-parity fiber of EVERY legal paired-flat Q6 coloring contains a red full antipodal geodesic. This is a sharper algebraic proof of the prior complete 2^24-coloring enumeration, with an adaptive word portfolio independent of phase values. For one six-word pattern (selector mask 1370), the simultaneous failure equations on phase bits theta_0,...,theta_11 are:
 theta0+theta1+theta6+theta10=1;
 theta0+theta3+theta5+theta6+theta8+theta11=1;
 theta0+theta3+theta4+theta10=1;
 theta0+theta2=0;
 theta9+theta11=0;
 theta1+theta2+theta4+theta5+theta8+theta9=0.
Adding all equations gives 0=1. The corresponding word family is (010212,012012,012021,020121,021201,101202).
The standalone Python matrix/phase checker verifies all 4096 selector systems and runs 8000 independent red-step samples. A second C++ checker directly simulates EVERY phase assignment for the 270 exceptional systems: 270*4096=1,105,920 colorings, all successful. The Python checker additionally compared 64000 affine predictions against direct path simulation.

**Q8 parity-static odd-slope forcing theorem.** Let m=4 and strengthen the affine-fiber hypothesis by requiring a_i(p)=a_i independent of p, while allowing each phase gate theta_i(p_except_i) to be an arbitrary Boolean function of three other pair-parity bits. Each a_i is an odd three-input linear form, giving FOUR alternatives per i and 4^4=256 coefficient matrices. Every prescribed pair-parity fiber contains a red full antipodal geodesic for all 256 matrices and ALL 2^32 phase assignments. The proof uses a fixed portfolio of 17 pair-label words:
 01230123 01231230 10230231 20130132 30120123 01232310 23010132 02131320 03121230 12030321 13020231 10232301 20131302 21030312 30121203 31020213 32010123.
For every one of the 256 coefficient matrices, one of these words satisfies z dot (1+b_w(theta))=0 AS AN AFFINE POLYNOMIAL IN ALL 32 PHASE VARIABLES for every left-null vector z of A_w+I. Hence its return equation (AH1) is solvable for all phases. The first certified word for each matrix has corank 0 in 88 cases, corank 1 in 92 cases, and corank 2 in 76 cases, guaranteeing respectively 1,2,4 successful q-roots for that word in every fixed pair-parity fiber. A self-contained Python symbolic checker verifies the 256-by-17 cover. Independently developed C++ code computes all 33-bit affine polynomials and their left kernels and independently constructs red full paths in 32768 seeded phase assignments. This is a positive fiberwise result for nonlinear legal Q8 colorings: the phase gates may be completely unrestricted Boolean functions, but their q-slope matrices must remain unchanged across parity fibers.

**Research significance and limit.** The mechanism exploits simultaneous incompatibility of Boolean path failures, not a histogram, fixed root, prescribed near-full face, or a restricted influence graph. It supplies a dimension-uniform linear-algebraic toolkit and stronger finite Q6/Q8 forcing results. For arbitrary paired-flat Q_(2m) with m>=4, parity-fiber gates may be nonlinear in q and their derivative coefficients may change with p; the affine return-map theorem does not cover those colorings. The all-dimensional assertion that parity-static odd slopes always admit some phase-immune double-occurrence word remains unproved. NORI1 is still open.

**Complete files.** nori_affine_holonomy_forcing.md; nori_affine_holonomy_certificate.py; nori_affine_holonomy_independent.cpp; nori_affine_m4_static_transport.md; nori_affine_m4_static_cover.py; nori_affine_m4_static_independent.cpp; archive nori_affine_holonomy_research_bundle.zip.
