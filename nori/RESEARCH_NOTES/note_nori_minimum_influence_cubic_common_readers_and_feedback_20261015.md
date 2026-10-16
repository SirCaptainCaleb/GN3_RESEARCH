# Minimum-influence three-nonlinear cubic rigidity and no-feedback closure

- Stable ID: note_nori_minimum_influence_cubic_common_readers_and_feedback_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, balanced, three-nonlinear, influence-minimality, Fourier, feedback, closure
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Minimum-influence rigidity theorem for balanced NORI1.** Write s_i=(-1)^(c_i) and chi_j(x)=(-1)^(x_j). For a vertex-balanced antipodally odd coloring of Q_n, define M=sum_i |Read(c_i)|. Assume the proven balanced zero-, one-, and two-nonunary closure results.

**Theorem.** If M=n+6 and c has at least three nonunary direction rules, then there are precisely three nonunary directions E={a,b,c}, and they all have the same three-element essential-reader set R={p,q,r}, disjoint from E. Writing chi_R=chi_p chi_q chi_r, their signed rules, up to permutation of E, take the form
s_a=sigma chi_R,
s_b=(alpha_p chi_p+alpha_q chi_q+alpha_r chi_r-sigma chi_R)/2,
s_c=(beta_p chi_p+beta_q chi_q+beta_r chi_r-sigma chi_R)/2,
where sigma and all alpha_i,beta_i lie in {+1,-1} and alpha_p alpha_q alpha_r=beta_p beta_q beta_r=sigma. Their sum S=s_a+s_b+s_c is a sum of either one or three distinct signed singleton characters on R, never the 2+1 coefficient pattern.

*Proof.* Antipodal oddness forces every direction rule to have a nonempty odd Fourier spectrum. A unary rule has one essential reader, and every nonunary odd rule has at least three. If k>=3 rules are nonunary, M>=n+2k, so equality M=n+6 implies k=3, all three with three essential readers. An odd signed Boolean function of three essential bits has a nonzero Fourier coefficient on their cubic product. This coefficient is either +/-1, attained by signed parity, or +/-1/2, attained by a signed majority of three signed inputs. Indeed its odd Fourier expansion has only three linear terms and the cubic term; by the four antipodal truth-pair values, vanishing cubic coefficient would force a signed singleton character. The sum of the three exceptional signed functions is a linear combination of singleton characters, because balance makes it minus the sum of the remaining unary rules. Consequently all cubic Fourier coefficients cancel. Each of the three rules contributes one nonzero cubic coefficient on its own reader triple, and with only three terms none can be supported on a triple appearing only once. Therefore the three reader triples coincide, say R. Since each rule ignores its own edge direction, R is disjoint from E. Three nonzero numbers in {+/-1,+/-1/2} sum to zero only when they comprise sigma,-sigma/2,-sigma/2 for sigma in {+/-1}. Thus one rule is sigma chi_R and the other two have the displayed majority expressions. Boolean-valuedness requires their three linear input signs to have product sigma. The signed sum equals (alpha_p+beta_p)chi_p/2+(alpha_q+beta_q)chi_q/2+(alpha_r+beta_r)chi_r/2. The alpha and beta sign triples have the same product, hence disagree in an even number of places, either zero or two. The sum therefore has three nonzero singleton coefficients or one. QED.

**No-feedback block lemma (general, not restricted to three exceptional directions).** Let E be any set of directions such that (i) every direction outside E has a unary odd edge rule, (ii) every rule in E depends only on bits outside E, and (iii) starting from any reader of an E-rule and iterating the unary reader-parent map never reaches E. Then c admits a color-zero full antipodal geodesic, in every dimension; vertex balance is not needed.

*Proof.* Let U be the union of all E-reader directions and their forward parent-map closures. By (iii), U lies outside E and is closed under unary parents. The coloring on U is an autonomous odd all-unary coloring, hence has a zero full antipodal geodesic from some y to bar y by the established one-reader theorem. Every E-rule depends only on U and ignores all E bits. By oddness, for each e in E, the color of its edge at U-state y and its color at bar y are complementary. Traverse first all E-directions whose colors are zero at y, then the U geodesic, then all remaining E-directions, which now have color zero. The E steps do not affect any other edge color in the core. This gives a zero full antipodal path on T=E union U, independently of every frozen exterior assignment. The established uniform frozen-core absorption theorem extends it through the remaining unary fringe, including cycles. QED.

**Necessary obstruction at minimum influence.** If a balanced counterexample attained M=n+6, its three nonlinear rules would all read a common external triple R, and at least one direction in R would have a unary reader chain eventually reaching E. Equivalently its directed influence graph would contain a directed cycle passing through a nonlinear direction and a reader direction in R. If no such feedback existed, the no-feedback block lemma would produce the forbidden full geodesic. Thus a least-influence counterexample must exhibit nonlinear-unary feedback, not merely a triple of nonlinear functions on the same three bits. This necessary condition is dimension-uniform.

**Scope.** The theorem classifies the extremal influence level M=n+6 and excludes counterexamples at that level without such reader feedback; it does not show the remaining feedback configurations are soluble and therefore does not settle NORI1.

Sharp feedback witness: on Q6 with chi_j=(-1)^(x_j), define s0=chi3*chi4*chi5, s1=(chi3+chi4+chi5-chi3*chi4*chi5)/2, s2=(chi3-chi4-chi5-chi3*chi4*chi5)/2, s3=chi0, s4=-chi3, s5=-chi0. Every rule is odd and ignores its own bit. The sum of six rules vanishes. Directions 0,1,2 are nonunary, each reading {3,4,5}; thus M=12=n+6. The influence graph has cycle 0->3->0. The direction order (3,1,4,0,5,2) from the all-zero root is a zero-colored full antipodal geodesic. Independent path DP finds 48 favorable zero roots and 208 total oriented rooted zero full geodesics. This illustrates sharpness of the influence bound for balanced odd colorings, while feedback is necessary, not sufficient, for a counterexample at minimal influence.
