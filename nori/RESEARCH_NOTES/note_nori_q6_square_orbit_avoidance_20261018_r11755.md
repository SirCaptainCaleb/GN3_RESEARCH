# Q6 paired-flat square-orbit avoidance and Q4 forced incidence

- Stable ID: note_nori_q6_square_orbit_avoidance_20261018_r11755
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, square-switch, square-avoidance, Q4, Q6, finite-enumeration, transfer-gap
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11755_2
- Updated session: session_nori_r11992_9
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Paired-flat square-orbit avoidance in dimension six

Let the directions of Q_(2m) be paired as P_i={2i,2i+1}. For each i, the gate f_i depends only on the directions outside P_i, with f_i(bar z)=1+f_i(z). The two P_i-direction colors are f_i and 1+f_i. A square-pair orbit consists of a square supported on P_i and its antipodal square.

**Proposition 1 (four-dimensional obstruction; proved).** Every paired-flat Q4 coloring has eight rooted red full geodesics, and each meets all four square-pair orbits, once apiece.

*Proof.* Write A,B for the two direction pairs. Two consecutive steps from one pair have opposite colors, so every red full path has pair-word ABAB or BABA. An odd Boolean rule on the two exterior bits reads precisely one of them, plus a constant. For ABAB, the first B-step must use the bit read by the A-rule; the second A-step must use the bit read by the B-rule. The order of the four directions is therefore determined. Requiring the initial A- and B-steps to be red fixes two independent root bits; two remain free. This gives four red paths for ABAB, and likewise four for BABA. Within each pair, the exterior states at its two steps differ in one bit and hence represent different antipodal square-pair orbits. Every red path therefore visits both orbits of each pair. QED.

**Proposition 2 (six-dimensional avoidance; exhaustive computational proof).** Every paired-flat legal coloring of Q6 has a red full antipodal geodesic avoiding any prescribed square-pair orbit.

*Verification.* There are 3*2^(6-3)=24 independent square-pair parameters. Relabeling the three pairs and translating the exterior bits acts transitively on parameter orbits, so fix orbit S=0. Enumerate all 2^6*6!=46,080 rooted full direction orders. For a step in direction d belonging to P_i, write z for the exterior assignment and z0=min(z,bar z). The red requirement on the indexed parameter x_(i,z0) is
x_(i,z0) = [z != z0] + [d=2i+1] (mod 2).
Discard paths meeting S, and discard paths placing contradictory requirements on a repeated parameter. There are 9,216 paths meeting S, 25,216 paths avoiding S with inconsistent requirements, and 11,648 consistent avoiding paths. Deduplication leaves 5,824 partial parameter assignments. The union of their satisfying Boolean subcubes contains all 2^24=16,777,216 assignments. The independent path enumerator checks the antipodal endpoint condition, and a separately implemented binary MILP containing the negation of all 5,824 certificates was reported infeasible by HiGHS. Source checker: nori_q6_square_avoidance.cpp (independent executable; no externally validated proof log). Thus the finite claim follows from the exhaustive bitset enumeration and its stated encoding.

**Transfer scope.** In Q4, retaining an unaffected path is impossible for every switched orbit; a witness must be replaced after the flip. In Q6, avoidance holds. In higher dimension, a six-direction face obtained by freezing other directions need not satisfy oddness under the six-direction antipode, so the Q6 theorem alone yields no full-class induction. A lifting theorem must transport a six-direction avoiding witness across complementary exterior fibers while also inserting the remaining directions in a monochromatic order. The non-odd frozen-face phenomenon is the explicit missing implication.

## Two-square-orbit strengthening (verified 19 October 2026)

**Theorem (computer-assisted).** Every legal paired-flat coloring of \(Q_6\) has a red full antipodal geodesic avoiding any prescribed two distinct antipodal square-pair orbits.

*Certificate.* The twenty-four square-pair orbits consist of eight for each of three direction pairs. Pair permutations and vertex translations preserve the coloring class and act transitively on these twenty-four orbits. Normalize the first forbidden orbit to orbit \(0\). Independently check every second orbit \(t\in\{1,\ldots,23\}\). For each of the \(2^6 6!=46,080\) rooted full orders, reject any path meeting either forbidden orbit or placing contradictory red requirements on a shared gate parameter. Every surviving path determines a partial assignment to the twenty-four independent antipodally paired gate parameters. Mark all \(2^{24}\) assignments extending at least one surviving partial assignment. In each of the twenty-three cases the bitset contains all \(16,777,216\) assignments; results are recorded in q6_pair_audit.txt. The standalone C++ verifier nori_q6_pair_avoidance.cpp independently constructs all orbit labels, all red path certificates and the coverage bitset, selecting \(t\) by command-line argument.

Consequently a set of fewer than three square-pair orbits cannot meet every red full geodesic of a paired-flat \(Q_6\) coloring. This is a finite result; the oddness of a six-direction frozen face generally fails in larger paired-flat cubes, so the theorem does not justify unrestricted higher-dimensional avoidance.


## Whole-gate two-site forcing certificate (20 October 2026)

Fix a prescribed antipodal square orbit S in pair P_0 of Q_6, normalize its independent gate-table site to 0, and fix the remaining gates h_1,h_2. The independent odd gate tables h_1,h_2 are each eight-bit masks. A rooted direction-simple full path is an *avoiding prepath* when it uses no edge of S and every edge in P_1,P_2 is red; its two P_0 steps prescribe compatible Boolean requirements on at most two sites of the unspecified gate h_0.

**Computer-assisted strengthening.** For every one of the 2^16 settings of (h_1,h_2), one of the following certificates occurs:

(a) Two avoiding prepaths prescribe opposite values at the same gate-0 site. Thus every h_0 satisfies one of the two paths.

(b) There are two distinct gate-0 sites a,b, neither equal to S, and four avoiding prepaths whose red requirements at (a,b) run through all four pairs (0,0),(0,1),(1,0),(1,1). Thus every h_0 satisfies one of the four paths.

The exhaustive census yields 61,936 fixed-gate settings of type (a), and 3,600 remaining settings of type (b). In every type-(b) setting at least three distinct unordered site pairs furnish all four requirements; their mean number is 13.6733. This is a stronger short-certificate explanation of Proposition 2: for each setting of two complete odd gates, at most four predetermined path patterns cover all 256 assignments of the third gate. It does not strengthen the already-recorded two-forbidden-orbit theorem.

**Reproduction.** Enumerate 64 roots and 720 permutations of all six original directions. On each edge in pair i, calculate the exterior four-bit word z, representative z_0=min(z,15-z), and the required independent gate bit b=[z != z_0] XOR [direction is 2i+1]. Retain only prepaths avoiding S whose two edge requirements in each fixed pair are consistent. There are 11,648 such prepaths before imposing h_1,h_2. For each of the 65,536 masks (h_1,h_2), retain a prepath if all its requirements on these masks are satisfied. For prepaths constraining one site of h_0, record the required bit in U[site]. For prepaths constraining two distinct sites a,b, record the ordered pair of required values in a four-bit mask C[a,b]. Verify that either some U[site] contains both values or some C[a,b] equals 15; also enumerate both disjoint cases and the minimum number of complete rectangles. A standalone verifier is nori_q6_rectangle_audit.cpp, created in session session_nori_r11992_9; its output is 'unit 61936 no_unit 3600 rectangles 3600 no_rectangles 0 min=3'. The independent previously recorded full-assignment coverage check remains valid.

**Dimension-uniform interpretation and gap.** The identical two/four-prepath condition is sufficient in Q_(2m), for any m and any nonlinear gates: it selects a red full antipodal geodesic avoiding S for every assignment of h_i. Repeated-site prepaths correspond to red full geodesics within a face with the switched pair frozen: the two pair-i edges must bracket all outside dimensions, their outside arguments are antipodal, and the two choices of the first red pair member give opposite one-site requirements. Such a face witness extends using the two distinct members of the omitted pair, by oddness. At a hypothetical strict good-to-bad square boundary, no red frozen-face geodesic can exist, because its red full extension would traverse zero or two switched edges and transport across the switch. The unresolved full-class statement is to force a mixed-site contradiction, or some weaker repairing path, from this face-free condition together with balance, global square unavoidability, and strict internal one-hit witnesses. There is no established reduction from the six-cube certificate to this unrestricted situation. In particular, freezing all other pairs generally destroys antipodal oddness of the induced six-cube coloring.

## Face-free classification in Q6 and a higher-dimensional transfer obstruction

**Analytic explanation of the 3,600 unit-free cases.** Freeze the two original dimensions of pair P_0. On the resulting Q4, the red selectors in pairs P_1,P_2 are Boolean functions a of the two P_2 vertex bits and b of the two P_1 vertex bits. This Q4 has a red full geodesic if and only if both a and b are nonconstant. Necessity follows because a constant gate never selects both original members of its pair. For sufficiency choose a P_2 edge across which a changes and a P_1 edge across which b changes; select endpoints so that the pair order P_1,P_2,P_1,P_2 uses a red member at the first visit of each pair and its other member at the second. Opposite P_0 faces have complementary restrictions determined by antipodal oddness. There are two independent opposite-face pairs; on each, (a,b) may be any of 16^2 function pairs, of which 16^2-14^2=60 have at least one constant function. Consequently the number of outer-gate settings without red Q4 geodesics on any P_0-frozen face is 60^2=3,600. This checks the computational unit-clause count and identifies the remaining settings as two simultaneous one-gate-constant face obstructions. The four-corner certificate still requires the separate path audit.

**Dimension-uniform obstruction to extending the constancy reduction.** For any odd k>=3, work in Q_(2k+2) with pairs P_0,...,P_k and write p_j=x_(2j)+x_(2j+1) over F_2. Choose arbitrary legal f_0, and for 1<=j<=k put
  f_j(x)=x_0 + sum_(1<=l<=k, l!=j) p_l.
These gates ignore their own pair, and complementing all original vertex bits reverses x_0 while leaving every p_l unchanged; hence they are legal antipodally odd paired-flat selectors. When P_0 is frozen, every restricted f_j is nonconstant, depending on k-1>=2 other pair parities. Nevertheless every such frozen Q_(2k) face has NO red full geodesic.

**Proof.** Suppose a red full geodesic existed on a frozen face. Write its sequence of pair labels, each label 1,...,k appearing twice, and let C_jl be 1 if the occurrences of j and l alternate, and 0 otherwise. Between the two occurrences of j, parity p_l changes precisely when C_jl=1; C_jl=C_lj. To use both original members of pair j red, the two evaluations of f_j must differ, so 1=sum_(l!=j) C_jl mod 2 for every j. Summing over j gives k=2 sum_(j<l) C_jl=0 mod 2, contradicting odd k. This proves the obstruction. In Q8 (k=3), the three fixed outer masks in the canonical 32-site gate indexing are each 0xaa5555aa. An independent original-direction path audit finds zero one-site unit requirements and 225 complete two-site rectangles avoiding the normalized P_0 square orbit. Thus reciprocal interactions can prohibit all frozen-face red paths without eliminating mixed-site forcing.

**Consequence for transfer.** The Q6 characterization 'every red-free frozen face has a constant outside gate' fails already in a legal Q8 coloring, even when all three outside gates depend reciprocally on other outside pair parities. An unrestricted proof must generate mixed-site forcing without assuming a constant outside gate or an acyclic outside influence graph. The example is successful for every choice of f_0 by the audited rectangle certificate; it is no counterexample to NORI1 or switch preservation.

**Why the unit-free class equals the face-free class.** In an arbitrary P_0-frozen Q4 with nonconstant outside gates a,b, let E(a),E(b) denote the numbers of bichromatic edges in their respective two-bit argument squares. The standard two-pair path count is R=2 E(a)E(b) rooted red full geodesics. Each nonconstant Boolean function on Q2 has at least two bichromatic edges, so R>=8. At any chosen root, the pair-label word must alternate; the starting pair determines the entire red step sequence because one member of each pair is red at every vertex. Thus at most two red full geodesics start at one root. By reversal, each antipodal root pair contributes at most four rooted paths. At least two distinct antipodal root pairs therefore support red full geodesics in the frozen face. Given a prescribed forbidden square orbit S, at most one of these root pairs indexes S. Choose another red face path and bracket it by the two original directions of P_0; the two choices of initial member give opposing one-site requirements at a site different from S. Conversely every such opposing unit pair arises from red frozen-face paths because the two P_0 steps must bracket all four outside steps. Hence the unit-conflict and red-face-existence conditions are equivalent, and the 61,936/3,600 split has an analytic explanation independent of the longer implication-graph computation.
