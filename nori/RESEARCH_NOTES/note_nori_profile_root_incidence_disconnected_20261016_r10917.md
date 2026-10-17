# Uniform full-profile frequencies coexist with exponentially fragmented root fibers

- Stable ID: note_nori_profile_root_incidence_disconnected_20261016_r10917
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, profile-support, root-fiber, product-obstruction, all-dimensions
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_partial_profiles_one_switch_equivalence_20261016_r10917

## Research note

For r>=1 let (a_j,b_j)=(2j,2j+1), j=0,...,r-1. On Q_(2r) define c_(a_j)(x)=1+x_(b_j), c_(b_j)(x)=1+x_(a_j) in F2. These rules yield a legal antipodally odd coloring.

THEOREM A. A root x realizes a full direction-color profile w if and only if, for all j, w_(a_j)+w_(b_j)=1+x_(a_j)+x_(b_j) mod2. Each admissible root-word pair is realized by (2r)!/2^r full direction orders. Every profile has 2^r supporting roots and (2r)! rooted full geodesics, so full profiles have a uniform global frequency even though each is supported on a fraction 2^(-r) of the roots. Each root admits 2^r full profiles. The bipartite root-profile incidence graph is the disjoint union of 2^r copies of K_(2^r,2^r). Root supports for two target profiles differing in one bit are disjoint.

PROOF. If direction a_j precedes b_j, their colors are (1+x_(b_j),x_(a_j)); in the reverse order they are (x_(b_j),1+x_(a_j)). These two choices are complementary and have the same XOR. Fixing a compatible target pair therefore forces one of the two precedence relations. All r pairs are independent and the number of interleavings is (2r)!/2^r. The r parity equations leave two root-bit assignments per pair. Grouping roots and profiles by their pair parities proves the incidence decomposition.

THEOREM B (bridge setting). Add one new bit t=2r, with c_t(x)=x_0, and leave the old rules independent of x_t. This gives a legal coloring of Q_(2r+1). For each prescribed profile w on the first 2r directions, the supporting roots satisfy the same r pair parity equations, hence number 2^(r+1), or fraction 2^(-r) of all roots. At each eligible root there are (2r+1)!/2^r rooted full geodesics matching the prescribed old colors. Thus every target old-direction pattern occurs on 2(2r+1)! rooted full geodesics, independent of w. Neighboring prescribed patterns have disjoint supporting-root sets. Nevertheless the FULL profile support is all of F2^(2r+1): placing t before or after direction zero yields both colors of t at each eligible root. Its full root-profile incidence graph decomposes as 2^r copies of K_(2^(r+1),2^(r+1)).

OPTIONAL FULL WORD COUNTS. A full word w on Q_(2r+1) occurs on (2/3)(2r+1)! rooted paths when w_t=w_1, and on (4/3)(2r+1)! paths otherwise. This follows by counting the three relative positions of t, a_0 and b_0 after imposing their internal precedence, then summing the two possible eligible root states.

AUDIT. The independent C++ enumerator nori_partial_profile_root_separation.cpp exhausts all roots and all direction permutations in Q3,Q5,Q7, confirming root counts 4,8,16 for each old pattern and full path multiplicities 12,240,10080. An exhaustive audit of all legal Q4 colorings found at least 8 of 16 supporting roots for each prescribed three-bit profile; the exhibited Q5 coloring has just 8 of 32 roots for four-bit profiles, refuting extrapolation of that half-root bound.

CONSEQUENCE. Even uniform global full-profile counts and surjective complete profile support do not imply that nearby target profiles can be witnessed from a common starting root. There can be exponentially many components in the root-profile incidence graph. This blocks profile-gluing arguments resting only on independent witnesses or total frequencies, but does not refute NORI1: the displayed colorings have monochromatic full geodesics.TENSORIZATION ADDENDUM (arbitrary independent antipodally odd colorings). Let c and d be legal colorings of Q_a and Q_b. Define their Cartesian product coloring on Q_(a+b), with first a direction rules depending only on the first factor and the remaining b rules only on the second. Write M_c(x,w) for the number of full direction permutations from root x with complete profile w. Then
M_(c box d)((x,y),(u,v))=binom(a+b,a) M_c(x,u) M_d(y,v).
Consequently the rootwise support is W_((x,y))(c box d)=W_x(c) times W_y(d), the supporting-root set of profile (u,v) is S_u(c) times S_v(d), and the global word multiplicity satisfies M_(c box d)(u,v)=binom(a+b,a)M_c(u)M_d(v). Under a uniform random root and uniform random full direction permutation, the factor profiles are independent. PROOF: every full permutation projects to independent permutations of the two disjoint direction sets; conversely any two factor orders admit binom(a+b,a) interleavings, all giving the same factor paths and colors.

For the pair gadget of the parent note, these formulas also show a striking conditional-information separation. With X a uniform cube root, P a uniform direction permutation, and W the resulting complete profile in Q_(2r), W is globally uniform on all 2^(2r) binary words, but W reveals the r-bit parity signature (X_(a_j)+X_(b_j))_j through W_(a_j)+W_(b_j)=1+X_(a_j)+X_(b_j). Conditional on X, W is uniform over just 2^r words. Hence the Shannon mutual information between root and profile is I(X;W)=r bits, despite W being perfectly uniform. This illustrates mathematically why global profile counts cannot substitute for compatible rooted witnesses.
