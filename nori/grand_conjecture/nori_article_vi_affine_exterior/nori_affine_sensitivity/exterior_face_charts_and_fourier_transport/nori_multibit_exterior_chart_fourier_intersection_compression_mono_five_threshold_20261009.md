# Multibit exterior-chart Fourier intersection forces monochromatic five-geodesics below 2/9 combined error

# Exact multi-bit exterior-chart intersection, Fourier energy, and a physical monochromatic five-path threshold

**Setup.** Let n>=6, let c be an ACTIVE NORI coloring of actual physical ordered three-faces: c(bar F,rev pi)=1-c(F,pi). For an unordered three-coordinate free set T and an ordered orientation pi of T, let E=[n]\T. Every such actual physical face is determined by its fixed exterior bit string z∈F_2^E. Define the ±1 face-sign function
  f_pi(z)=(-1)^{c(F_z(T),pi)}.
The active law is exactly
  f_(rev pi)(bar z)=-f_pi(z).
Use the uniform probability measure on the exterior bit cube.

**THEOREM 1 (two arbitrary exterior charts intersect in their COMMON MEMORY).** Suppose for one ordered triple pi, two proposed Boolean predictors g_pi(z_A),h_pi(z_B) use coordinate subsets A,B⊆E and have respective ACTUAL mismatch probabilities
  alpha=Pr[f_pi(z)≠g_pi(z_A)],  beta=Pr[f_pi(z)≠h_pi(z_B)].
Write I=A∩B. Let P_K denote conditional expectation onto coordinates K, namely P_K f=E[f|z_K]. Then the genuine Fourier energy of f_pi outside the intersection I obeys the SHARP projection inequality
  E[(f_pi-P_I f_pi)^2]
     <= E[(f_pi-P_A f_pi)^2]+E[(f_pi-P_B f_pi)^2]
     <= 4(alpha+beta).
Equivalently, writing Walsh coefficients f_hat(S) for S⊆E,
  sum_(S not⊆I) f_hat(S)^2 <= 4(alpha+beta).
If both predictions are exact, the actual f_pi depends ONLY on shared exterior coordinates I, with no extra compatibility/cocycle condition. In particular if A∩B=∅ and alpha=beta=0, f_pi is CONSTANT on all its exterior bits.

**Proof.** The Walsh characters chi_S(z)=(-1)^(sum_(j∈S)z_j) form an orthonormal basis on F2^E. P_K retains precisely coefficients with S⊆K. Every S⊈I=A∩B violates S⊆A or S⊆B, so the nonnegative squared coefficients in the left sum appear in at least one of the two right sums. Conditional expectation P_A f minimizes mean squared distance among A-measurable functions, while g_pi is A-measurable. Hence E[(f-P_Af)^2]<=E[(f-g)^2]=4alpha for ±1 signs; similarly B. This proves both inequalities. When alpha=beta=0, orthogonal projection gives f=P_I f a.s., and on the finite cube this equality holds at EVERY actual exterior bit string. QED.

**Corollary 2 (canonical equivariant compressed memory).** Perform the construction simultaneously on all ordered orientations pi of any set of direction triples, taking chart intersections I_pi. Define m_pi(z_I)=E[f_pi|z_I], and its canonical Boolean majority predictor k_pi(z_I)=sign m_pi (tie choices arbitrary but chosen antipodally equivariantly between pi and rev pi). Under active NORI, if I_(rev pi)=I_pi, then m_(rev pi)(bar z_I)=-m_pi(z_I); consequently the majority labels can be chosen to satisfy
  k_(rev pi)(bar z_I)=-k_pi(z_I)
exactly. Thus simultaneous approximate charts canonically compress ACTUAL face color data to their shared exterior-memory coordinates, retaining the exact antipodal-reversal law. The compression error satisfies
  Pr[f_pi≠k_pi]<= 2(alpha+beta),
because for a ±1 random bit with conditional mean m, conditional majority error (1-|m|)/2 <=(1-m²)/2, and averaging plus Theorem1 gives the bound. This is an approximate FACE-COLOR atlas, not yet a PATH-WITNESS correspondence; root alignment remains obligatory.

**THEOREM 3 (disjoint multi-bit charts force true monochromatic five-geodesics).** Fix ANY six distinct directions V⊆[n]. For EVERY ordered triple pi using distinct directions in V suppose that there exist TWO binary predictors on DISJOINT exterior-coordinate sets A_pi,B_pi⊆[n]\supp(pi), with error rates alpha_pi,beta_pi whose sum satisfies
  alpha_pi+beta_pi < 2/9.
The sets and predictors can vary arbitrarily with pi; there is NO bound on their sizes or complexity. Then c contains a genuine MONOCHROMATIC FIVE-EDGE cube geodesic supported on some five directions in V, and indeed one fixed such direction order is monochromatic from a POSITIVE fraction of the actual Q_n roots. For n=6 this immediately proves FULL antipodal one-switch grand closure for this subclass, by appending the one missing coordinate.

**Proof.** For disjoint A_pi,B_pi, I_pi=∅, so Theorem1 gives
  1-(E f_pi)^2 = Var(f_pi) < 4*(2/9)=8/9,
and hence |E f_pi|>1/3. Define q(pi)∈{0,1} as the unique majority physical face color, equivalently (-1)^q(pi)=sign E f_pi. The actual minority error for pi is
  e_pi = (1-|E f_pi|)/2 < 1/3.
The active NORI law f_(rev pi)(bar z)=-f_pi(z) gives E f_(rev pi)=-E f_pi, so
  q(rev pi)=1-q(pi).
Thus q is a genuine COORDINATE-ONLY reversal-odd ordered-three-face labeling on V. By the team's proved six-direction monochromatic-facet theorem (Item nori_six_direction_monochromatic_facet_transfer_20261008), there are five distinct directions p1,...,p5 in V and one color q0 such that
  q(p1,p2,p3)=q(p2,p3,p4)=q(p3,p4,p5)=q0.
Now choose an ACTUAL uniform cube starting root x and traverse the five directions in that order. Each of its three physical ordered-face windows has a uniformly distributed exterior bit string (each prefix XOR is a bijection of root bits), so its probability of color different from q0 equals the appropriate e_pi<1/3. By the union bound, the probability that ANY of its three real window colors differs from q0 is <1; hence a strictly positive fraction of roots witness ALL THREE actual windows in color q0. These are literal monochromatic five-edge geodesics, with no formal face substitution or root mismatch. If n=6 there is just one missing direction r, and appending r adds one last ordered-three-face window, so the resulting full antipodal geodesic has at most one switch. QED.

**Independent majority-bias version.** The proof of Theorem3 shows the broader sufficient condition: if for all oriented triples in a six-support, the ACTUAL exterior face-color frequency has a unique majority of size >2/3, there is a literal five-edge monochromatic geodesic. The two-chart hypothesis is only one geometrically meaningful way of forcing this bias.

**Exact no-go and correct scope.** Arbitrarily nonlinear higher-degree exterior parity functions can be maximally unpredictable from every low-memory disjoint chart. In the legal NORI coloring
  c(F,pi)=h(pi)+sum_(j outside supp(pi)) z_j
where h(rev pi)=h(pi)+(n-2 mod2), each face-sign has zero Fourier mean whenever n>=5. In fact all its Fourier energy lies at the top exterior character, making Theorem3 inapplicable, while Item nori_affine_exterior_three_residue_chain_eight_monochromatic_roots_20261008 proves that this SAME family has exactly eight monochromatic full geodesic roots for every prescribed complete direction order. Thus the present sufficient low-memory gluing certificate and the prior high-memory linear-parity extraction solve complementary subclasses. Unrestricted NORI closure remains OPEN: a valid proof needs either a topological mechanism forcing an actual root-coupled reachability overlap without spectral hypotheses, or a finite-memory decomposition covering genuinely arbitrary exterior Boolean functions.

**Potential connection to topological carriers.** Theorem1 removes all higher face-color gluing obstruction for two overlapping exterior MEMORY subcubes: only their intersection survives. An eventual topological proof must glue CERTIFIED good-path/root states rather than only Boolean face-color functions, and cannot assume this Fourier compression preserves a chosen witness.

## Elevation: arbitrary many overlapping memory charts and a full-geodesic transfer test

**THEOREM 4 (multi-chart Fourier-Helly projection).** For one ACTUAL ordered physical triple pi, let m>=2 predictor functions g_j(z_(A_j))∈{±1} on arbitrary exterior bit supports A_j⊆E, with actual binary mismatch probabilities alpha_j against f_pi. Set I=∩_(j=1)^m A_j. For each nonempty Fourier support S⊆E which is NOT contained in I, define its chart-exclusion multiplicity
  kappa(S)=#{j∈[m]: S not⊆A_j} >=1,
and kappa=min_(S not⊆I) kappa(S). If I=E no nontrivial compression is requested. Then
  E[(f_pi-E[f_pi|z_I])²]
    =sum_(S not⊆I) fhat_pi(S)²
    <= (1/kappa)*sum_j E[(f_pi-E[f_pi|z_(A_j)])²]
    <= (4/kappa)*sum_j alpha_j.
In particular exact simultaneous chart representations always factor uniquely through the intersection I; this is the exact Boolean-coordinate analogue of a Helly property for face-color DATA, with no topology or root-memory assumptions.

When the A_j are pairwise disjoint and m>=2, I=empty and kappa>=m-1. Therefore the true exterior color-sign bias obeys
  1-(E f_pi)² <= (4/(m-1))*sum_j alpha_j.
If for EVERY oriented triple pi in one fixed six-support V there are such m=m_pi pairwise-disjoint chart predictors satisfying
  (1/(m_pi-1))*sum_j alpha_(pi,j) < 2/9,
then by the same physical six-direction majority argument as Theorem3, a GENUINE monochromatic five-edge geodesic supported on V exists. Every actual root is considered in the probability calculation. At n=6 it gives full one-switch antipodal closure.

**Proof.** Every Fourier character chi_S with S not⊆I is missing from at least kappa of the conditional expectation projections onto A_j, so the sum of m projection residual energies counts its squared coefficient at least kappa times. Each individual residual is at most 4alpha_j by least-squares optimality against the predictor g_j. Sum the inequalities and divide by kappa. For pairwise disjoint A_j, a NONEMPTY S can be contained in at most ONE A_j, so kappa>=m-1. The majority and root-extraction arguments of Theorem3 apply exactly when the displayed averaged error bound is strictly <2/9. QED.

**COROLLARY (root-faithful lifting of ANY known coordinate-only full witness).** For arbitrary n>=5, fix an ACTUAL NORI coloring c and a coordinate-only reversal-odd profile q(pi) on ordered distinct triples in [n]. Let p=(p1,...,pn) be a FULL direction order with AT MOST ONE switch in the profile color word q(p1,p2,p3),...,q(p_(n-2),p_(n-1),p_n). Put
  e_j=Pr_(uniform physical root x)[the jth ACTUAL ordered-face window of P(x,p) disagrees with q(p_j,p_(j+1),p_(j+2))].
If Σ_(j=1)^(n-2) e_j<1, then some genuine FULL rooted antipodal geodesic P(x,p) has EXACTLY the same window-color word as q along p, hence at most one switch. Proof: each window is a true physical ordered three-face whose fixed exterior bit string is uniformly distributed under a uniform full starting root. A union bound on the n-2 mismatch events gives a root with ZERO mismatch. This is an explicit exact ROOT EXTRACTION statement; it can transfer existing coordinate-only closure on a prescribed order to physical colorings sufficiently close on the relevant face charts. No general coordinate-only full closure in arbitrary n is assumed.
