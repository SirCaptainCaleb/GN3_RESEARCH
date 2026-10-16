# Three-nonlinear dimension-uniform closures by frozen three- and four-direction cores

- Stable ID: note_nori_three_nonlinear_internal_reader_six_pivot_closure_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, balanced, three-nonlinear, four-pivot, closed-branch, Fourier
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**All-internal-reader three-exception closure (dimension-uniform).** Let c be a vertex-balanced antipodally odd binary edge coloring of Q_n with precisely three nonunary signed edge rules s_a,s_b,s_c, where s_i=(-1)^(c_i), chi_j=(-1)^(x_j), and s_i ignores bit i. Suppose s_a+s_b+s_c=epsilon_a chi_a+epsilon_b chi_b+epsilon_c chi_c, with each epsilon in {+1,-1}. Then c admits a zero-colored full antipodal geodesic, regardless of n or the nonlinear dependence on other bits.

Proof. Vertex balance gives sum_i s_i=0. Thus the remaining unary signed rules sum to -epsilon_a chi_a-epsilon_b chi_b-epsilon_c chi_c. Pair opposite-signed rules with the same reader. The remaining three unmatched unary directions u_a,u_b,u_c have signed rules -epsilon_a chi_a,-epsilon_b chi_b,-epsilon_c chi_c respectively; all other unary rules form pointwise complementary pairs.

Take core T={a,b,c,u_a,u_b,u_c}. Freeze any assignment of bits outside T. Normalize the three exceptional bits by replacing chi_i with epsilon_i chi_i, so their normalized bits y_a,y_b,y_c have signed characters chi_i'=(-1)^(y_i). The three unmatched unary signed rules become -chi_a',-chi_b',-chi_c'. Throughout this frozen T-face, s_a+s_b+s_c=chi_a'+chi_b'+chi_c'.

For each exceptional rule s_a, fix the three unmatched unary bits as well as all frozen outside bits. Its dependence on b,c has vanishing mixed discrete difference: the sum s_a+s_b+s_c has no mixed (b,c) term, s_b ignores b, and s_c ignores c. Since s_a is Boolean-valued, it is therefore either constant or a signed one-bit character in b or c. The same holds cyclically for s_b,s_c. The sum of the three rules is chi_a'+chi_b'+chi_c', with coefficient +1 at each exceptional direction and no constant. Thus all three rules must be positive one-bit characters, using the three distinct exceptional readers in one of the two derangements: (s_a,s_b,s_c)=(chi_b',chi_c',chi_a') or (chi_c',chi_a',chi_b'). The choice can depend arbitrarily on the three unmatched unary bits and the frozen exterior state.

We construct a zero full T-geodesic from any root whose normalized exceptional bits contain both zero and one. If just one bit i is one, traverse u_i first (its color is zero), then keep all other unmatched unary bits frozen during the three exceptional steps. Traverse i next: its two possible readers both equal zero, so the edge is zero. All exceptional bits are now zero. For the remaining two exceptional directions j,k, choose their order so the final direction reads i, which remains zero; such a choice exists under either derangement. The middle exceptional edge sees both possible readers zero, and the last sees its selected reader i equal zero. Finally traverse u_j,u_k: both are zero-colored since their exceptional reader bits are now one.

If two exceptional bits i,j are one and the remaining bit k is zero, traverse u_i,u_j first. Freeze the three unmatched unary bits for the exceptional portion. The derangement sends precisely one of the exceptional directions i,j to reader k. Traverse that direction first, while its reader k is zero. Then traverse the other initially-one exceptional direction; both its possible readers are zero. Then traverse k; both its possible readers are zero. Finally traverse u_k, whose reader k is now one. Every step is zero-colored. This construction works for every frozen exterior assignment and every choice of the nonlinear selector.

Thus each frozen T-face admits a zero full antipodal T-geodesic. The established uniform frozen-core absorption theorem in this same Subsection extends such a core geodesic across an arbitrary unary exterior fringe, including reader cycles. Hence c has a zero full antipodal geodesic on all n directions. QED.

**Rooted strengthening.** For the frozen six-direction core above, a zero full core geodesic exists from all 48 roots whose normalized exceptional triple is neither 000 nor 111, independently of the selector. Roots with triple 000 cannot succeed: the final exceptional direction is attempted after its two reader bits both became one, so its signed color is negative. Roots with triple 111 cannot succeed: before any exceptional step both possible reader bits are one, and unary steps do not change exceptional bits. Independent DP over all 256 Boolean selectors on the three unmatched unary bits confirms the same set of 48 successful roots for each selector; the preceding proof is not dependent on finite enumeration.

**General three-exception residue trichotomy.** More broadly, let E be the three nonunary directions, and let U be all other directions with unary signed rules epsilon_i chi_(p(i)). Balance implies S=sum_(e in E)s_e=sum_j k_j chi_j with integer k_j. Because S is a sum of three signs, max_x |S(x)|=sum_j |k_j|<=3. Since n is even, |U|=n-3 is odd, hence sum_j |k_j| is odd. It is therefore either 1 or 3. The case S=+/-3 chi_j would force all three exceptional rules to be the same unary signed character, contrary to their definition. Accordingly S has one of these three forms, with signs arbitrary and reader indices distinct where shown: (I) chi_p; (II) 2 chi_p+chi_q; (III) chi_p+chi_q+chi_r. The unary rules can be arranged into pointwise complementary same-reader pairs plus respectively one or three unmatched unary rules. The theorem above closes subcase (III) when {p,q,r}=E. The remaining residue patterns and reader-incidence configurations are open here.

**Frozen-state unaryization for three exceptions.** For any balanced coloring whose only nonunary rules are a,b,c, each exceptional rule restricted to a frozen assignment of all other bits is either constant or a signed character in one of the other two exceptional bits. This uses only balance, direction consistency, and the unary character property of all remaining rules. In particular a three-nonlinear counterexample cannot exploit a mixed two-bit interaction inside its exceptional three-face; all complexity is in changes of those local types with the outside state.

**Second closed three-exception subbranch: two internal readers and one unmatched external reader.** Let the three exceptional directions be a,b,c, and suppose their signed sum equals epsilon_a chi_a+epsilon_b chi_b+epsilon_p chi_p with p outside {a,b,c}. Pair the other unary rules by opposing same-reader signs. Three unmatched unary directions u_a,u_b,u_p have signed rules -epsilon_a chi_a, -epsilon_b chi_b, -epsilon_p chi_p. Suppose p=u_a or p=u_b. Then c admits a zero-colored full antipodal geodesic in every dimension, with arbitrary nonlinear dependence on the remaining directions.

*Proof.* Absorb the epsilon signs into normalized bit labels a,b,p. By symmetry swap a,b if needed, and suppose p=u_a. The core T={a,b,c,p,u_b,u_p} consists of six different directions. Freeze arbitrary bits outside T. Within T, balance implies
s_a+s_b+s_c=chi_a+chi_b+chi_p,
s_p=-chi_a, s_(u_b)=-chi_b, s_(u_p)=-chi_p.
For any core vertex with a=b=p=0, all three exceptional signed colors are positive, since their sum is 3. Each exceptional edge rule is independent of its own bit, so positive exceptional edges also extend to vertices differing only in that direction's bit.

There are two explicit zero full T-geodesics, both valid independently of the selector, and for arbitrary initial c and unmatched-unary bits.

(i) Start with normalized (a,b,p)=(0,1,0), and traverse
u_b, b, c, a, p, u_p.
The u_b edge is positive because b=1. The b edge is positive because toggling only b brings its vertex to a=b=p=0, where s_b=+1. The c and a edges are positive because a=b=p=0 when they are traversed (c is an independent bit, and s_a ignores a). After a, a=1, so the p edge, with s_p=-chi_a, is positive. After p, p=1, so the u_p edge, with s_(u_p)=-chi_p, is positive.

(ii) Start with normalized (a,b,p)=(1,0,1), and traverse
u_p, p, a, c, b, u_b.
The u_p edge is positive because p=1. The p edge is positive because a=1. After p, (a,b,p)=(1,0,0); the a edge is positive by comparison with the saturated all-zero triple. After a, (a,b,p)=(0,0,0), so c and b are positive. Finally u_b is positive because b=1.

Thus every frozen six-direction core has a zero full antipodal T-geodesic, with no restriction on the exceptional switching selector or outside bits. Apply the existing uniform frozen-core absorption theorem to the unary exterior. QED.

**Rigid coefficient pruning for three exceptions.** In the residue trichotomy S=sum_(e in E)s_e, the pattern S=epsilon 2chi_p+eta chi_q with p different from q cannot occur with all three exceptional rules nonunary if either p or q lies in E. If p lies in E, the two other exceptional rules must each contribute epsilon chi_p to the frozen exceptional-bit expansion (only those two can read p), forcing them to be unary. If q lies in E but p does not, freeze outside E; the signed constant term 2epsilon chi_p demands two exceptional rows be constant epsilon chi_p, while the remaining row supplies eta chi_q. The row with index q cannot read q, hence is one of the two constants, forcing that exceptional rule to be unary globally. Therefore a possible three-nonunary coloring in the 2+1 residue pattern must have both reader indices outside E.

**Computation audit and obstruction to a smaller frozen core.** For the second closure theorem above, the frozen exceptional rules have three possible local configurations, assigning two of the rules the distinct positive characters chi_a,chi_b and the third the constant chi_p. The configuration may be selected arbitrarily at each of the eight states of the three unmatched unary bits. Enumeration of all 3^8=6561 selector maps confirms a positive zero full core geodesic for every map. The two displayed direction orders give a non-enumerative proof. Omitting p and u_p and freezing chi_p=-1 can instead produce a five-direction core with no zero antipodal full path (even with each exceptional rule frozen to a constant/unary type); hence the additional reader pivot p is essential to this frozen-core argument.


**Strengthening: the second closure needs only a FOUR-direction frozen core.** Under the second subbranch above, assume after sign normalization that S=s_a+s_b+s_c=chi_a+chi_b+chi_p with p outside E={a,b,c} and signed unary rule s_p=-chi_a. Let T={a,b,c,p}, freezing every other direction, including the other two unmatched unary directions. At a vertex with a=b=p=0 the exceptional sum is +3, so every exceptional direction is zero-colored. Undirected edge consistency then also makes the b-edge zero when a=p=0,b=1.

Choose the core starting bits (a,b,p)=(0,1,0), with c arbitrary, and traverse the core directions in the order
\[
\boxed{b,\ c,\ a,\ p.}
\]
The b-edge is zero by self-bit invariance from the saturated state (a,b,p)=(0,0,0). After b, the exceptional c-edge and a-edge are zero since all three characters chi_a,chi_b,chi_p equal +1. The a-step ends with a=1, so s_p=-chi_a=+1 and the p-edge is zero. This constructs a zero full four-direction T-geodesic for every frozen exterior state, with no need to inspect any nonlinear selector and no need to move the unmatched directions reading b and p. The uniform frozen-core absorption theorem now completes the full coloring. If s_p=-chi_b instead, exchange labels a and b. Hence the branch is fully closed even without building or enumerating the six-pivot core.

This four-step saturation certificate is especially useful for future three-exception cases: one can force all exceptional signs positive by making their signed sum +3, and use invariance of each edge rule under flipping its own bit to advance into or out of that saturated state.
