# Cyclic Fourier decay, automorphism-free affine Hall certificates and graph-bias refinements

- Stable ID: note_nori_cyclic_rotation_fourier_weight_20261017_r11421
- Author: session_nori_r11421_1
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, affine, cyclic-rotation, Fourier, inversion-graphs, Hall, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11421_1
- Updated session: session_nori_r11421_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_affine_profile_fourier_inversion_graphs_20261017_r11401
- note:note_nori_affine_quotient_twin_order_action_20261017_r11413

## Research note

# Cyclic-rotation Fourier decay and an automorphism-free affine Hall certificate

Let A be binary n-by-n with diagonal zero and A1=1. Define b_i(pi)=sum_(j preceding i in pi) A_ij for every full direction order pi. Put K=ker A^T, q=dim K, and mu_hat(lambda)=E_pi (-1)^(lambda dot b(pi)) for lambda in K. Since A1=1, every lambda in K has even Hamming weight.

**Theorem 1 (weight-sensitive Fourier decay).** For any nonzero lambda in K of weight t,
|mu_hat(lambda)|<=sqrt((n-t)/(n(t+1))).
In particular mu_hat=0 for t=n; for t=n-1 its magnitude is at most 1/n; for t=n-2 the stronger bound 1/(n-1) holds. The bound holds without quotient-twin pairs, relabeling automorphisms, or special block structure.

*Proof.* Rotate the first label i in pi to the end. The affine permutation-profile difference is b(rot pi)+b(pi)=(I+A)e_i. For lambda in K this changes the sign (-1)^(lambda dot b) by (-1)^lambda_i. Averaging this equality over all n cyclic rotations gives
mu_hat(lambda)=E_pi [(-1)^(lambda dot b(pi)) S_lambda(pi)/n],
where S_lambda(pi)=sum_(k=0)^(n-1)(-1)^(number of lambda-marked labels in the first k positions).
Put N=n-t. The t marked positions divide the N unmarked positions into t+1 gaps of lengths g_0,...,g_t. These gap lengths are a uniformly random weak composition of N, and t is even. The marked positions contribute canceling signs, giving S_lambda=sum_(j=0)^t (-1)^j g_j. For a uniform weak composition, E[g_i]=N/(t+1), E[g_i(g_i-1)]=2N(N-1)/((t+1)(t+2)), and E[g_i g_j]=N(N-1)/((t+1)(t+2)) for i!=j. Since sum_(j=0)^t(-1)^j=1, expansion yields
E[S_lambda^2]=N+N(N-1)/(t+1)=n(n-t)/(t+1).
Cauchy-Schwarz proves the displayed Fourier bound. When N=2, S takes values -2,0,2. The two unmarked labels lie in gap positions of the same parity with probability (t+2)/(2(t+1)); hence E|S|/n=1/(n-1), proving the stronger final estimate.

**Theorem 2 (all-syndrome forcing and perfect matching).** If
sum_(0!=lambda in K) sqrt((n-|lambda|)/(n(|lambda|+1)))<1,
then b(pi) meets every coset modulo im A. Consequently every affine coloring c_i(x)=a_i+(Ax)_i attains all complete profiles globally, and its root-profile incidence graph has a perfect matching. In particular, if every nonzero lambda in K has weight at least d, the simpler condition
(2^q-1)*sqrt((n-d)/(n(d+1)))<1
suffices.

*Proof.* Characters of F2^n/im A are indexed by K. Fourier inversion expresses the probability of each quotient syndrome v as
P(v)=2^(-q) sum_(lambda in K)(-1)^(lambda dot v) mu_hat(lambda).
Theorem 1 bounds every P(v) below by 2^(-q) times one minus the displayed sum, which is positive. A requested profile w then admits an order pi with w-a-b(pi) in im A; solve Ax=w-a-b(pi). The affine quotient-transversal theorem supplies a bijective matching between roots and profiles.

**Theorem 3 (signed inversion graphs).** For any simple graph H on n labeled vertices, let t be its number of odd-degree vertices (always even) and Z(H)=E_pi (-1)^(number of H-edges inverted by pi). For t>=2,
|Z(H)|<=sqrt((n-t)/(n(t+1))).
This follows by the same cyclic-rotation proof, because moving the first label to the end flips the inversion sign precisely when that label has odd graph degree. When all vertices have odd degree, Z(H)=0; with one even-degree vertex and all others odd, |Z(H)|<=1/n, sharp for an even-leaf star. This does not establish the separately observed 1/3 bound for arbitrary nonempty H.

**Explicit Q6 certificate with trivial quotient automorphism group.** Let A have six integer row masks [52,41,25,52,32,4], bit zero the least significant. Every row has odd parity and zero diagonal. The left kernel is K={0,9,39,46}, q=2, with nonzero Hamming weights 2,4,4. The Fourier bound sum is
sqrt(2/9)+2sqrt(1/15)=0.9878023...<1.
All four affine syndromes therefore occur by Theorem 2. Independent enumeration of 720 full orders gives syndrome counts 216,216,144,144; the three nontrivial Walsh sums are 144,0,0. The quotient-edge labels [delta_ij] of the complete direction-label graph have only the identity as a color-preserving automorphism, verified by testing all 720 relabelings. Thus neither quotient-twin swaps nor the full prior relabeling symmetry theorem can certify the example. The undirected interaction graph is connected.

**Reproducibility and scope.** An independent checker verified the marked-gap second moment for all even t<=n<=10, the signed-graph Fourier bound on every graph through six vertices, all Q6 legality and syndrome counts, and the trivial quotient automorphism group. The file cyclic_rotation_fourier_decay_20261017.md contains the full derivation and rotation_fourier_weight_verify.py reruns the checks. This is a dimension-uniform Fourier/Hall forcing criterion for arbitrary legal AFFINE colorings, not a proof of unrestricted NORI1.

**Sharp-ended graph-bias inequalities and a stronger OPEN conjecture.** Let Z(H)=E_pi (-1)^inv_H(pi), and let t denote the even number of odd-degree vertices. The cyclic-rotation proof gives Z(H)=0 when t=n. When t=n-1 (necessarily n odd), it gives |Z(H)|<=1/n, with equality for a star of n-1 edges whose center has even degree. When t=n-2 (necessarily n even), the two-unmarked-gap L1 argument gives |Z(H)|<=1/(n-1), also sharp for a star with n-2 leaves and one isolated vertex.

Independent complete Walsh-Hadamard enumeration of all 2^21=2097152 undirected graphs on seven labeled vertices gives the following maxima stratified by odd-degree count t: t=0:1/3 (32767 nonempty Eulerian graphs), t=2:1/3 (688128 graphs), t=4:1/5 (1146880 graphs), t=6:1/7 (229376 graphs). The t>0 maxima are attained by t-edge stars plus isolated vertices. These computations motivate the **unproved** stronger inequality
|Z(H)|<=1/(t+1) for every graph H with t>=2 odd-degree vertices.
The proved theorem above gives only sqrt((n-t)/(n(t+1))) in general. No inference about the proposed universal inequality, or unrestricted NORI1, is made from the finite census.
