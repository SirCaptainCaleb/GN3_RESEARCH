# Q4 red geodesic extremizers and obstruction to local unary compression

- Stable ID: note_nori_q4_red_geodesic_count_extremizers_20261016_r10917
- Author: session_nori_r10917_3
- Primary home: subsection:complementary_rank_geodesic_counting_and_parity_blindness
- Labels: NORI1, enumeration, full-geodesic-count, extremizer, unary-compression, counterexample
- Lifecycle: active
- Epistemic status: computational
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction

## Research note

Let c be a legal antipodally odd binary edge coloring of Q_4, and let N_0(c) be the number of ordered full antipodal geodesics consisting entirely of color-zero edges.

**Finite exhaustive classification (computer-assisted).** Among all 2^16 legal colorings, the minimum of N_0 is eight, attained by 48 colorings. Every minimizer is unary, c_i(x)=x_{r(i)}+epsilon_i, with a reciprocal two-cycle on core directions a,b; the two remaining directions read different core directions. For each core reader j, its two child rules have opposite signs epsilon_i. Conversely the resulting binom(4,2)*2*2^2=48 colorings all attain N_0=8.

**Exhaustive certificate.** Label each of the 16 antipodal pairs of undirected edges by direction i and the smaller of e and ((15 xor e) & ~(1<<i)), with e_i=0. A sixteen-bit assignment of representative edge colors determines the whole legal coloring. For each root x and subset S of [4], let D_x(empty)=1, and
D_x(S)=sum_{i in S}[c_i(x xor 1_S)=0]D_x(S without i).
Then N_0(c)=sum_{x in Q_4}D_x([4]). Iteration over masks 0,...,65535 gives minimum 8 and frequency 48. Classifying all attaining masks by their unary reader and sign choices gives the description above. A separate direct path enumeration for representative mask 63 returns eight paths, from roots 4,5,6,7 in direction order (1,2,3,0) and roots 8,9,10,11 in order (0,3,2,1).

**Local rule-compression obstruction (proved finite calculation).** Fix the three unary rules
c_1(x)=x_3,\quad c_2(x)=1+x_1,\quad c_3(x)=x_2
on Q_4, and vary the remaining rule c_0=F(x_1,x_2,x_3) over all antipodally odd Boolean functions F of these three bits. For y in {0,2,4,6,8,10,12,14} (encoded by the bits 1,2,3), let W(y) be the number of pairs (root x, direction order pi) for which all three nonzero-direction edges are red and the direction-zero step occurs when (x_1,x_2,x_3) has encoding y, without testing the zero-edge color. Enumeration of the 24 orders and 16 roots gives
W(0)=8, W(2)=12, W(4)=4, W(6)=8,
W(8)=4, W(10)=8, W(12)=0, W(14)=4.
For every F, the red full-path count equals sum_{F(y)=0} W(y). Antipodal oddness makes F(y)+F(14 xor y)=1, so its minimum is
min(8,4)+min(12,0)+min(4,8)+min(8,4)=12.
It is achieved by the unique F choosing red on y=14,12,4,8. In algebraic normal form,
F=1+x_2+x_1 x_2+x_3+x_1 x_3+x_2 x_3.
This is nonlinear. Direct substitution of the six unary rules F=x_j+epsilon, j in {1,2,3}, epsilon in F_2, gives N_0 in {16,32}. Thus every unary replacement is strictly worse than the nonlinear minimizing F:
min_{odd F} N_0(c)=12 <16=min_{unary F} N_0(c).
Accordingly, any attempt to prove that global N_0-minimizers may be taken unary through independent, non-increasing one-rule substitutions fails already in dimension four. The global minimum eight still has only unary minimizers.

**Scope.** The full four-dimensional classification is supported by complete finite enumeration; the local rule-compression refutation also has the explicit eight-entry traffic certificate above. No dimension-uniform global compression theorem is established. The proposed inequality N_0(c)>=2^(n-1), compatible with enumerated minima 2,4,8 in dimensions 2,3,4, is an unproved strengthening of NORI1.

**Dimension-uniform edge-orbit traffic minimization lemma (proved).** Fix n>=2, a direction i, and all legal antipodally odd rules c_j for j different from i. For each undirected direction-i edge e, let T_i(e) count rooted ordered full antipodal geodesics whose direction-i edge is e and whose other n-1 edges are all red. This count does not depend on c_i. Each full geodesic uses direction i once, so when c_i varies with c_i(bar e)=1+c_i(e),
N_0(c)=sum_{O={e,bar e}}( [c_i(e)=0]T_i(e)+[c_i(bar e)=0]T_i(bar e)),
where the sum ranges over antipodal pairs of direction-i undirected edges. Consequently
min_{odd c_i} N_0(c)=sum_{O={e,bar e}} min(T_i(e),T_i(bar e)).
*Proof.* Partition rooted full direction orders by the direction-i edge they traverse. Each full geodesic has one direction-i edge, and it is entirely red if all other edges and this edge are red. The values of c_i on distinct antipodal direction-i edge pairs can be selected independently with one red representative per pair. Minimizing the contribution of each pair yields the formula. QED.

Every global N_0-minimizer chooses, in each antipodal direction-i edge pair, a red representative with no greater traffic than its antipodal partner. The Q_4 traffic table above shows that this locally optimal choice can be nonlinear even when the global N_0-minimizers are all unary.
