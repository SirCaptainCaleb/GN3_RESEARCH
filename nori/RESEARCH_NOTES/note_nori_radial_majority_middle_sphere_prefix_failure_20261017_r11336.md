# Radial incidence twins with independent square curvature and geodesic transport

- Stable ID: note_nori_radial_majority_middle_sphere_prefix_failure_20261017_r11336
- Author: session_nori_r11348_1
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, radial-colorings, root-profile-incidence, Hamming-sphere, square-curvature, prefix-transport, balanced, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11336_1
- Updated session: session_nori_r11348_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For every even n=2m>=4 define c_i(x)=1 if sum_(j ne i)x_j >=m, and 0 otherwise. It ignores bit i and is complement odd because the other 2m-1 input bits have complementary threshold halves. **Theorem:** at every root x the attainable complete direction-indexed profiles satisfy W_x={w:|x+w|=m}.

Proof. Before dimension i is traversed, its bit is still x_i. An upward step at current Hamming weight h has color one iff h>=m; a downward step has color one iff h-1>=m. Thus x_i+w_i=1 precisely when that step increases the distance of the Hamming weight from the middle layer m. An antipodal path starts at weight k and ends at 2m-k, which are equidistant from m, so it has m outward and m inward steps.

Conversely prescribe a profile with m outward steps and m inward steps. Partition its directions into U_plus,U_minus,D_plus,D_minus by initial bit zero/one and outward/inward requirement, with sizes q,s,p,r respectively. They satisfy p+q=m, p+r=k, q+s=2m-k and s-p=q-r=m-k. If k<=m, begin with m-k inward upward steps to reach middle height m, then pair each remaining outward downward step with an inward upward step, and every remaining inward downward step with an outward upward step, returning to m after each pair; finish with m-k outward upward steps. If k>=m, interchange upward and downward steps and begin with k-m inward downward steps. All counts match by the identities above. This orders every direction and realizes the prescribed profile.

Root-profile incidence is therefore the Hamming-distance-m bipartite graph. Its roots split into two parity components, each of cardinality 2^(n-1). Roots at distance two share a profile, and such moves connect every parity class. The degree is binomial(n,m). The normalized spectrum is obtained by Walsh transform of the middle Hamming sphere: characters of odd weight have coefficient zero, and characters of weight 2r have coefficient (-1)^r binomial(m,r)/binomial(2m,2r). The two unit coefficients correspond to the two parity components. The ratio of successive interior absolute coefficients is (2r+1)/(2(m-r)-1), giving largest interior magnitude 1/(n-1).

Define one-shot prefix transport: x and x+1_S are joined if some full geodesic at x begins with prefix S and toggling the S entries of its profile yields another attainable profile at x. Such pairs share a profile after rotating by S. For the radial coloring, every full geodesic from zero records zero on its first m directions and one on its last m directions. Toggling any proper prefix gives profile weight m+k or 3m-k, greater than m. The only available nontrivial prefix is the full path, giving the antipodal root. Thus the zero-root prefix component is {0,1^n}, whereas the complete incidence component contains 2^(n-1) roots. For odd N>=5, append directions j>=4 with rules c_j=x_0 to the four-dimensional radial instance, so rooted profiles factor as W_old times F2^(N-4); projection carries each prefix transport step to an old prefix step or leaves its old root fixed. The separation therefore persists for every N>=4. Enumeration at n=4,6,8 checked all rooted geodesics with no discrepancy.

## General radial incidence twins and curvature engineering

Let n=2m>=4 and let g:{0,...,n-1}->F_2 obey g(h)+g(n-1-h)=1. Define the radial legal coloring c_i^g(x)=g(sum_(j != i)x_j). There are 2^m such colorings.

**Theorem (universal middle-sphere incidence).** Every admissible g satisfies W_x(c^g)={w:|x+w|=m} at every root x. In particular all 2^m colorings have the same bipartite root-profile incidence graph, its two parity components, its perfect matchings, its degree binomial(n,m), and nontrivial normalized component spectrum bounded by 1/(n-1). At root zero, every attained profile appears on (m!)^2 distinct direction orders for every admissible g.

*Proof of necessity.* Put z_i=x_i+w_i. For an upward step crossing height layer h to h+1, z_i=g(h); a downward step across the same layer has z_i=1+g(h). Swapping two consecutive upward steps or two consecutive downward steps preserves the multiset of the two z values. Swapping consecutive steps of opposite signs also preserves their sum as an integer: the two z values are complementary in both orders. Since adjacent swaps connect all full direction orders, |z| is independent of the order. If the starting root has weight k<=m, traverse all n-k initially zero directions before the k initially one directions. The k layers crossed in both directions contribute k one-bits, while the remaining layers from k through n-k-1 contain m-k complementary pairs of g-values, so contribute m-k further one-bits. Thus |z|=m. The case k>m follows by antipodal symmetry, which complements the profile along an unchanged order.

*Constructive sufficiency.* For k<m, any target with |x+w|=m demands t one-bits among the n-k upward directions, where m-k<=t<=m. Traverse all levels from k to n-k upward, inserting k up-down oscillations along the way. The baseline gives m-k upward directions whose z entry is one. Among the baseline levels there are some with g=0 and some with g=1, because they are paired under h -> n-1-h. Put t-(m-k) oscillations at levels with g=1 and the remaining m-t at levels with g=0. Every oscillation uses one unused initially zero direction and one unused initially one direction, and returns to its starting height. This yields t upward one-bits and m-t downward one-bits. Direction labels can be freely assigned within the upward and downward steps, giving any prescribed target word. If k=m, use t of the m oscillations across level m in the up-down direction and the remaining m-t across level m-1 in the down-up direction when g(m)=1; reverse these choices when g(m)=0. Since g(m)+g(m-1)=1, any t in {0,...,m} occurs. Antipodal symmetry handles k>m. This proves the theorem. At zero, the successive edge colors are g(0),...,g(n-1), with m ones. To produce a given weight-m indexed word, assign the m directions requiring color one to the m one positions and the others to the zero positions, giving (m!)^2 orders.

**Theorem (curvature classification).** Let kappa(t)=g(t)+g(t+1), for 0<=t<=n-2. On any i,j square whose other n-2 bits contain t ones, the two initial-order profiles differ by kappa(t)(e_i+e_j). The word kappa is a palindrome with kappa(t)=kappa(n-2-t) and kappa(m-1)=1. Conversely every such palindrome arises from two complement-odd radial rules differing by global color complementation. Therefore one shared root-profile incidence relation admits 2^(m-1) distinct radial square-curvature patterns.

Proof. The square derivatives in both directions equal g(t)+g(t+1). Complement oddness gives the palindrome symmetry and the middle entry. Conversely fix the first g-value and integrate the prescribed derivative; the palindrome and center condition guarantee the complement-odd identity. Two initial values yield complementary functions.

**Theorem (classification of one-shot prefix and square transport).** At root zero the radial profile values along every order are g(0),...,g(n-1). For a prefix set S of size k>0, toggling its bits changes the profile weight to m+k-2G(k), where G(k)=sum_(h<k)g(h) as an integer. Such a prefix is a valid root-transport step precisely when G(k)=k/2. Every k-subset is available if this condition holds.

For the affine member g(h)=h mod 2, every even k is valid, every odd k is invalid, and this holds at every starting root: explicitly w_i(x,pi)=x_i+(|x| mod 2)+(p_i mod 2), where p_i is its position in the order. Thus its one-shot prefix transport graph comprises two complete parity-class graphs. Its square curvature is kappa(t)=1 on every layer, so its square-bridge graph comprises the two Hamming-distance-two parity graphs.

For the threshold member g(h)=1 when h>=m, its only valid nontrivial prefix length at zero is n; the same holds at the antipode, giving a two-root prefix component {0,1^n}. Its curvature kappa(t) is one only for t=m-1. Thus its square-bridge graph comprises (i) the Johnson graph on roots of weight m, (ii) a connected graph joining roots of weight m-1 with those of weight m+1 by two-bit flips, and (iii) isolated vertices of every other weight. The second graph is connected because adjacent (m-1)-subsets share an (m+1)-superset, and every (m+1)-subset contains an (m-1)-subset. The number of isolated roots is 2^n-binomial(n,m-1)-binomial(n,m)-binomial(n,m+1). This is asymptotic to 2^n. In contrast the affine member has no isolated square-bridge roots.

**Balanced incidence twins.** On Q_(2n), append for each old direction i a new reader direction n+i colored 1+c_i^g(x_old). The coloring is legal and balanced because its old-new direction pairs have opposite colors at every vertex. Placing each reader before or after all old steps independently realizes any new-direction profile without changing the old one. Therefore W_(x,y)^(lift)={w:|x+w|=m} times F_2^n, independently of g. Mixed old-reader square bridges do not alter the old-root bits, so the differing old-root square-bridge projections persist: full even-parity class for the affine member versus the single old root zero for the threshold member. One-shot prefix connectors similarly project to the old-prefix relation. By starting with the four-dimensional instance and appending further complementary reader pairs, balanced incidence twins with these contrasting transport behaviors exist in every even ambient dimension N>=8. Their rooted profile affine hulls have codimension one.

This theorem does not resolve NORI1: all displayed radial colorings satisfy it and possess translation perfect matchings. It proves instead that full rooted-profile support, all incidence components, their Hall properties and spectra, and even rooted multiplicities at zero do not determine the local square curvature or the geodesic-order transport geometry. Finite checks in Q4 and Q6 covered all admissible radial rules, every root and every direction order; square-bridge component classifications were also verified in Q8.
