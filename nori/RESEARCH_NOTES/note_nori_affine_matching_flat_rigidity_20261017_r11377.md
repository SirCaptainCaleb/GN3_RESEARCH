# Matching flats: full linear rank and exponential realizability gap

- Stable ID: note_nori_affine_matching_flat_rigidity_20261017_r11377
- Author: session_nori_r11387_1
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, affine, matching-flat, square-exchange, linear-rank, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11377_1
- Updated session: session_nori_r11387_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Theorem (matching-flat packing for every legal affine coloring). Let A be n-by-n over F2 with A_ii=0 and A*1=1, and c_i(x)=a_i+(Ax)_i. Put b_i(pi)=sum of A_ij over directions j preceding i in pi. Then W_x=a+Ax+B(A), B(A)={b(pi):pi in S_n}. Form an undirected graph G with ij an edge iff A_ij or A_ji equals one. If M is ANY maximal matching of G of size k, every W_x contains an affine subspace of dimension n-k. Thus every rooted affine profile set has at least 2^ceil(n/2) members. This is sharp in each dimension.

Proof. Let P be the 2k matched directions and T the unmatched directions. Maximality gives A_uv=A_vu=0 for distinct u,v in T. Fix an order of the k matched pairs. For any subset S of T, place S before all pairs and T\S after them, with fixed internal order within the unmatched blocks; choose the internal order of each pair independently. For u in T, its permutation-dependent profile bit b_u is 0 if u is in S, and equals sum over matched j of A_uj=1 otherwise, since the row of A has odd sum and the other unmatched directions do not influence it. The unmatched profile entries determine S. Swapping the adjacent matched pair i,j changes b by delta_ij=A_ij e_i+A_ji e_j, nonzero because ij is an interaction edge. The vectors for different pairs have disjoint supports. Moving an unmatched direction u from late to early changes b by v_u=e_u+Ae_u, because Ae_u vanishes on all unmatched directions. Consequently all generated profile words form an affine translate of the span of the |T|+k=n-k vectors v_u (u in T) and delta_ij (ij in M). The v_u have distinct unmatched entries, and the remaining delta vectors are independent on disjoint matched pairs. Their span has dimension n-k. This proves the theorem.

Theorem (rigidity of equality). Equality |W_x|=2^ceil(n/2) holds if and only if the rules, after relabeling, consist of reciprocal independent pairs c_p=a_p+x_q, c_q=a_q+x_p covering every direction when n is even; if n is odd they cover all but one direction h, and c_h=a_h+sum_(j in S)x_j, with S an odd-sized subset of the paired directions. In every equality case W_x is an affine ceil(n/2)-flat.

Proof. Every pair i,j can be adjacent in a permutation, and neighboring transpositions connect the permutation group, so the direction span V of aff B(A) is spanned by delta_ij. A vector lambda belongs to V-perp precisely when lambda_i A_ij=lambda_j A_ji for every pair. Form the graph H containing the mutual dependency edges A_ij=A_ji=1. Every lambda in V-perp is constant on each connected H-component. One-way dependencies A_ij=1,A_ji=0 force lambda_i=0 and hence kill the H-component of i. Thus dim V-perp equals the number of H-components without outward one-way dependencies. In each such free component C, every row indexed by C reads only directions in C, symmetrically. Every vertex of H[C] has odd degree by A*1=1; the handshaking lemma implies |C| is even and at least two. Therefore dim V-perp<=floor(n/2), giving dim V>=ceil(n/2). If |W_x|=2^ceil(n/2), the affine flat constructed above fills W_x, so dim V=ceil(n/2). We must have floor(n/2) free two-vertex H-components. When n is even these cover all directions and are independent reciprocal pairs. When n is odd they cover all but one direction h, which can read an odd subset of the paired directions while all paired rows remain autonomous. Conversely each pair permits two independent profile patterns according to its relative order; the leftover reader, if present, can be placed before or after all pairs to realize either profile bit independently. This proves both directions.

Finite audit: exhaustive counts of minimum-size rooted affine profile families among legal interaction matrices are 6/8 at n=3, 3/256 at n=4, and 120/32768 at n=5. For n=5 the rigidity classification predicts 5 choices of leftover reader, 3 reciprocal pairings, and 8 odd reader-support choices, giving 120. A separate direct matching-flat constructor passed randomized tests through n=8.

This theorem is intrinsic to legal affine edge-color rules. It does not settle affine NORI1: the constructed affine subspace can fail to project surjectively onto the cokernel of A.

**Theorem (nonlinear anti-flat expander examples).** For every sufficiently large n there exists a legal antipodally odd NONLINEAR coloring of Q_n such that each rooted profile set has 2^(n-1) members, has full affine span F2^n, and contains no affine subspace of dimension k=ceil(2 log_2(n-1)+4). Its bipartite root-profile incidence graph is connected, regular of degree 2^(n-1), and has all nontrivial normalized singular values at most 1/2. Hence dense rooted profile support and spectral expansion cannot extend the affine flat-packing theorem to arbitrary nonlinear colorings.

*Proof.* Write m=n-1>=16, and choose F:F2^m->F2 uniformly among functions satisfying F(q+1)=1+F(q). The 2^(m-1) Boolean values on antipodal pairs are independent fair bits. Define legal star rules c_0(t,y)=F(y), c_j(t,y)=t for j=1,...,m. Direct enumeration of the subset of leaves preceding central direction 0 gives W_(t,y)=(t,y)+Z_F, Z_F={(1+F(q),q):q in F2^m}. Thus all rooted supports have degree 2^m. An affine k-flat in Z_F projects injectively to an affine k-flat L in the leaf-input space on which F restricts to an affine function.

If L does not contain the all-ones direction, the restriction values on its 2^k points are independent and the probability of affineness is 2^(k+1-2^k). If L contains the all-ones direction, its 2^(k-1) antipodal pairs carry independent assignments, and the fraction yielding affine complement-odd functions is 2^(k-2^(k-1)). There are at most 2^(m(k+1)) affine k-flats in F2^m. Therefore the probability that F is affine on at least one such flat is bounded by 2^(m(k+1)+k+1-2^(k-1)), which is tiny for m>=16 and k=ceil(2 log_2 m+4).

For the spectral assertion, characters diagonalize convolution by the uniform generator set Z_F. The trivial Fourier coefficient is one. A nontrivial coefficient vanishes unless it reads the central bit and the leaf character has odd weight. In the remaining cases it is the mean of 2^(m-1) independent fair signs. Hoeffding's inequality and the union bound give probability at most 2^(m+1)*exp(-2^(m-4)) that ANY nontrivial absolute coefficient is at least 1/2. The sum of the two failure probabilities is below one for every m>=16. Thus some complement-odd F simultaneously avoids all k-flats and has a nontrivial spectral radius below 1/2. This implies incidence connectivity. Such F cannot be affine; therefore the graph Z_F has full affine span, since a nontrivial affine relation on its graph would express F as an affine function. QED.

**A six-dimensional obstruction to deducing affine NORI1 from a single matching-flat.** Let A have binary row masks [52,32,2,52,2,2], direction 0 least significant. Each row has odd weight and zero diagonal, so A is legal. It has rank 3, and its permutation-profile set B(A) consists of all 32 binary words w satisfying w_1+w_5=1; hence B(A)+im A=F2^6 and the associated affine coloring attains every global profile. Nevertheless its interaction graph has six maximal matchings, all perfect, and for every one of them the three matching-flat generators delta_ij together with the columns of A span only a five-dimensional space. Thus the sufficient test L_M+im A=F2^n fails for every maximal matching even though global profile surjectivity holds.

The six maximal matchings, written by direction indices, are {(0,2),(1,4),(3,5)}, {(0,2),(1,5),(3,4)}, {(0,4),(1,2),(3,5)}, {(0,4),(1,5),(2,3)}, {(0,5),(1,2),(3,4)}, and {(0,5),(1,4),(2,3)}. In every case rank[A | delta_(pair1) | delta_(pair2) | delta_(pair3)]=5. Direct enumeration of 720 direction orders gives |B(A)|=32 and the single affine profile relation above. Therefore the existence of a large affine flat inside every rooted profile set is not, alone, a proof of the unrestricted affine NORI1 conjecture.


**Strengthening (asymptotically maximal expansion and shattering).** In the random complement-odd star construction above, the spectral assertion can be strengthened from a fixed upper bound 1/2 to a bound tending to zero: for all m>=16, one can choose F for which the largest nontrivial normalized singular value of the root-profile incidence operator is at most 2^(-m/4), while Z_F contains no affine subspace of dimension k=ceil(2log_2 m+4). Indeed, for odd leaf characters beta, every nontrivial Fourier coefficient is the average of N=2^(m-1) independent Rademacher signs. Hoeffding gives
Pr(|mu_hat(beta)|>2^(-m/4)) <= 2exp(-N*2^(-m/2)/2) = 2exp(-2^(m/2-2)).
A union over at most 2^m characters has probability <=2^(m+1)exp(-2^(m/2-2)). Together with the affine-flat union bound proved above, the total failure probability is below one for m>=16. Consequently the incidence graph has normalized spectral gap at least 1-2^(-m/4), tending to one, while the largest affine flat has logarithmic dimension.

Moreover W_(t,y)=(t,y)+Z_F projects bijectively onto all m leaf-direction profile bits: its VC dimension is at least m=n-1. Thus shattering almost all directions, having cardinality 2^(n-1), full affine span, and nearly maximal incidence expansion do not imply internal affine flats of linear dimension. This contrasts directly with the sharp affine matching-flat theorem.
**Exponential failure of exhaustive maximal-matching-flat coverage.** For every r>=1, a legal affine Q_(4r) coloring has 14^r attainable rooted profiles, but the union of all flats supplied by the maximal-matching construction contains only 12^r. Therefore the captured proportion is (6/7)^r, tending to zero.

Proof. On Q4 let c_0=x_3,c_1=x_0,c_2=x_1,c_3=x_2. For a rooted order pi from zero, its profile entry in direction i is one iff the cyclic predecessor i-1 occurs earlier than i. The only infeasible patterns are 0000 and 1111, since each prescribes a cyclic ordering; every nonconstant pattern is a directed acyclic system of precedence constraints and is attainable. Thus B={1,...,14}, in integer masks. The undirected interaction graph is the four-cycle. Its two maximal matchings are {(0,1),(2,3)} and {(0,3),(1,2)}. Choosing either order for the two matched pair-blocks gives four flats, with profile sets {4,6,12,14}, {1,3,9,11}, {2,3,6,7} and {8,9,12,13}. Their union has twelve elements and omits precisely masks 5 and 10.

Take r Cartesian copies. The full rooted profile set is B^r, of size 14^r. Any maximal matching of the disjoint union of r four-cycles is the union of a perfect matching within each cycle, so any associated global flat projects into the twelve-element union in each block. Conversely any tuple of locally matching-flat profiles is attained by concatenating their blockwise matching orders, furnishing a global maximal-matching flat. Therefore the union of all global flats is the r-fold product of the twelve-element local union, having cardinality 12^r. This proves the claim. Each coloring is legal, has monochromatic full geodesics, and has a perfect root-profile matching by the established unary-reader theorem.

**Complete linear coverage, despite exponentially incomplete realizable coverage.** For any legal affine matrix A, let V=span{delta_ij:i<j}, delta_ij=A_ij e_i+A_ji e_j. Let L_M be the direction space of the affine flat produced by any maximal matching M. Then
V=span_M L_M
and
im A+V=F2^n.
Thus the family of all matching-flat directions collectively spans the full cokernel of A, even though its union of attainable affine flats may miss the proportion 1-(6/7)^r of rooted profiles in the cyclic four-block construction.

*Proof.* Every L_M is contained in V: its matched-pair generators are delta_ij, and for any unmatched direction u its generator (I+A)e_u equals sum_(j in P)delta_(uj), where P is the matched vertex set, because no two unmatched directions interact and row u has odd parity. Conversely any interaction edge ij extends to a maximal matching M, and then delta_ij belongs to L_M. These two inclusions give V=span_M L_M.

For lambda in V-perp the relations lambda_i A_ij=lambda_j A_ji hold for every i,j. Summing in i yields
(A^T lambda)_j=sum_i A_ij lambda_i=lambda_j sum_i A_ji=lambda_j,
where the last equality is the legality condition that every row of A has odd parity. Hence A^T lambda=lambda. A vector annihilating im A+V lies in ker A^T and V-perp, so it must vanish. Therefore im A+V=F2^n. QED.

This isolates the obstruction to affine NORI1 in the realizability of combinations of permutation exchanges, not in any missing ambient linear direction.
