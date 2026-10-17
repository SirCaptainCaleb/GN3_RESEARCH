# One-switch bridge equivalence, seven-wise support, and profile multiplicity

- Stable ID: note_nori_partial_profiles_one_switch_equivalence_20261016_r10917
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, profile-support, one-switch, all-dimensions, seven-wise-surjectivity
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_all_odd_rooted_rainbow_deficit_20261016

## Research note

# Partial geodesic color profiles and arbitrary one-switch paths

Fix an integer k>=1. For a legal antipodally odd undirected edge 2-coloring c of Q_n, define its full-geodesic direction-indexed profile support W(c) subset F_2^n. Write P(k) for the statement: for every n>k, every such c, and every k-element direction subset J, the projected support pi_J W(c) is the full F_2^J. Write U(k) for the statement: every ARBITRARY two-color undirected-edge coloring f of Q_k admits a full antipodal geodesic whose color word changes at most once. The geodesic stipulation in U(k) matters.

THEOREM (dimension-uniform partial-profile bridge equivalence). The following are equivalent:
(i) U(k);
(ii) P(k);
(iii) P(k) restricted to n=k+1 alone.
Further, under (i), the path in P(k) can be chosen so that all n-k unprescribed directions occur consecutively in one middle block. The colors on this middle block are unrestricted.

PROOF (i=>ii). Fix n>k, target profile w in F_2^J, and any assignment a to bits outside J. In the J-dimensional face with outside bits a, define an arbitrary coloring f_i(z)=c_i(z,a)+w_i (binary sum). By U(k) choose an antipodal full geodesic whose color word is 0^p1^(k-p), reversing it if necessary. Denote its first root by y and its unique switch vertex by x, so the red prefix from y to x uses direction set S, and the blue suffix from x to bar_J y uses the complementary direction set J\\S.

Build an n-dimensional full geodesic beginning at (x,a). First traverse the 0-prefix backwards from x to y, using only S; these edges have original color w_i. Next traverse all n-k outside directions in any order, reaching (y,bar a); their colors are not constrained. Finally traverse the reflected blue suffix backwards from (y,bar a) to (bar_J x,bar a). The deck-odd relation c_i(bar_J z,bar a)=1+c_i(z,a) shows that reflecting a blue f_i=1 edge gives original color w_i on the paired opposite face. Hence every prescribed J direction has its target color, each direction appears once, and the endpoints (x,a) and (bar_J x,bar a) are antipodal. The middle block is consecutive by construction. This proves P(k).

PROOF (iii=>i). Fix arbitrary f on Q_k and adjoin one new bit t. For old directions put
c_i(z,0)=f_i(z),  c_i(z,1)=1+f_i(bar_J z)
(binary sum); for the new direction put c_t(z,t)=z_1 (choose any old bit; for k=1 use the sole bit). These rules ignore their own bits and satisfy global antipodal oddness. P(k) in Q_(k+1), with prescribed old-direction profile all zero, supplies a full geodesic with all k old-direction edges red. It crosses the new direction once, splitting into two old-direction blocks. If the path starts in t=0, the first block is a red f-path from x to y and the second block, after reflection by bar_J, gives a blue f-path from x to bar_J y. Joining the reverse of the red first block to the blue second block yields a full y-to-bar_J y geodesic with at most one red-to-blue switch. If the original path starts in t=1, reflect its first block and keep the second to obtain the same two-arm configuration with the roles swapped; reversing orientation yields at most one red-to-blue switch. Every old direction occurs once. Thus U(k). Implication (ii=>iii) is immediate.

COROLLARY (dimension-uniform bounded-support surjectivity). For every n>k with 1<=k<=7, and every legal coloring c of Q_n, each k-direction projection of W(c) equals F_2^k. The reason is that U(k), the arbitrary-coloring one-switch GEODESIC statement, has been verified through k=7 using finite SAT, as explicitly separated into Conjecture 4 and Theorem 5 of Kirchweger, Peitl, Subercaseaux and Szeider (2025), From the Finite to the Infinite: Sharper Asymptotic Bounds on Norin's Conjecture via SAT, arXiv:2511.08386. It would be invalid to infer the k=8 statement from their separate verification of the antipodal MONOCHROMATIC geodesic conjecture in dimension eight.

In particular every legal coloring of every Q_n with n>=8 produces all 128 colors on any chosen seven directions along some full geodesic. This is a covering-array statement about complete profiles, not a claim that all 2^n full profiles occur or that the geodesic is monochromatic.

QUANTITATIVE/LOGICAL LIMITATION. P(k) for any fixed k<n is not sufficient by itself to imply monochromatic full paths. For example the formal subset F_2^n minus {0^n,1^n} projects onto F_2^J for every proper J, yet omits both monochromatic profiles. This formal support need not be realizable by a legal cube coloring, but shows that the projection property alone does not force NORI1. In fact the all-dimensions version of P(k) is equivalent to the degree-k arbitrary one-switch problem U(k), not to unrestricted NORI1.

COMPUTATIONAL AUDIT. A self-contained C++ program nori_profile_one_switch_bridge_certificate.cpp exhaustively enumerates all 2^12=4096 arbitrary Q3 edge colorings and all eight target three-bit profiles, constructs a one-switch geodesic in the normalized coloring, and builds/verifies the resulting legal Q4 full geodesic with the target prescribed profile: all 32768 trials pass. It also checks 10000 sampled arbitrary Q4 colorings, with all 16 targets each, by building the prescribed Q5 bridge. Separately, a C++ enumeration of all 65536 legal Q4 colorings verified that every three-direction profile projection is surjective. These finite checks validate the constructive reduction but are not needed for its proof.

RELATION TO EXISTING NORI WORK. The published NORI notes prove two-direction projection surjectivity and establish the stronger paired-root A(f) intersect antipode(A(f)) bridge for monochromatic geodesics. The present theorem isolates the strictly weaker ordinary one-switch existence A(f) nonempty as the condition for fixing just the directions J. It connects the finite arbitrary-coloring one-switch results to dimension-uniform local profile support without asserting the paired-root requirement.

SHARPENING 1 (one dimension suffices, whichever larger dimension). For any fixed n>k, U(k) is equivalent to the statement that every legal antipodally odd coloring of that single Q_n has every k-direction profile projection surjective. Indeed, if U(k) fails, choose an arbitrary Q_k coloring f with no one-switch full geodesic, and build the paired-face legal coloring c on Q_(k+1) from the converse proof. No full geodesic of c has the all-red pattern on its first k directions. For any larger n, retain all existing old-direction edge rules independent of the additional bits and assign to every extra direction the rule c_i(x)=x_1 reading an original bit. This remains legal under simultaneous complementation of all n bits. Any full geodesic projects to a full geodesic on the first k+1 directions with the same old-direction colors, so the forbidden pattern persists. Thus failure of U(k) produces a partial-profile failure in EVERY n>k, not only in dimension k+1.

SHARPENING 2 (deterministic profile multiplicity). Assume U(k). Fix n>k, a legal c, J of size k, target w, and m=n-k. Let M(c,J,w) count rooted ordered full geodesics with direction-profile restriction w. Then
M(c,J,w)>=2^m m!.
Proof: for each of the 2^m assignments a of the m outside bits, apply U(k) to the normalized restriction f_i(z)=c_i(z,a)+w_i and construct the three-block full geodesic from the forward proof, starting in outside face a. For any of the m! permutations of outside directions, use it as the middle block; the old-direction colors remain w regardless of the order of that middle block, as its endpoints are a and bar a. These are 2^m*m! distinct rooted ordered geodesics, since their initial outside assignments or direction orders differ.

FINITE AUDIT AND LIMITATION. A separate exhaustive C++ enumerator nori_profile_multiplicity_q4.cpp counts every rooted full geodesic of each of the 65536 legal Q4 colorings. For each of the eight patterns on directions 0,1,2, the minimum count over all colorings equals 32, whereas the uniform bridge bound supplies only 2. Thus the bridge multiplicity result need not be sharp. It does not give a monochromatic all-direction geodesic without also fixing the remaining directions, which would require the unresolved U(n) or stronger paired-root condition.
 ROOT-DENSITY COROLLARY. For every target word on k directions, the bridge construction supplies at least 2^(n-k) distinct starting vertices of Q_n supporting a full geodesic with that prescribed profile. Distinct outside-bit assignments give distinct starting vertices. Thus U(k) implies that at least a fraction 2^(-k) of cube roots support each prescribed k-direction pattern, independently of n. For k<=7 this is unconditional by the published finite one-switch geodesic checks. It does not assert constant root density for wholly monochromatic full geodesics.
