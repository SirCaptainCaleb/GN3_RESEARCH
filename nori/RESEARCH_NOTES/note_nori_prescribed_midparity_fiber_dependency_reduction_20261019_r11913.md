# Prescribed seam parity and terminal q-dependency core

- Stable ID: note_nori_prescribed_midparity_fiber_dependency_reduction_20261019_r11913
- Author: session_nori_r11913_1
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, three-pair-seam, q-dependency, dimension-reduction, computer-assisted
- Lifecycle: active
- Epistemic status: tested
- Current version: 7
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_1
- Updated session: session_nori_r11913_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Midpoint-prescribed seam and fiber-dependency reduction

For paired-flat gates f_i(p_-i,q_-i), define D_q by i→j when f_j depends on q_i. Call S q-outgoing-closed when every gate outside S ignores q_S; unrestricted dependence on p_S is permitted.

**Seam lemma (computer-assisted for three pairs).** Let 1≤r≤3. Internal pre-seam gate tables h_i^- are arbitrary and ignore their own pairs; post-seam tables satisfy h_i^+(p,q)=1+h_i^-(p,q+1), with 1 complementing all internal q bits. For any prescribed internal parity u AT the exterior seam, some red path traverses each of the 2r original internal directions once, crosses the seam once, and finishes at the internal antipode. The initial parity is free.

For r=1, use i,E,i. For r=2, the existing four-direction classification gives at least three admissible middle states per parity fiber; its exceptional mutual-unary-reader cases exclude four states, one in each parity fiber.

For r=3, translate u to 000. Let z_(i,4P+Q) be 48 independent pre-seam gate bits, indexed by other-pair parity P and first-member bits Q in F2². For root x, original-direction permutation π∈S6 and seam cut k∈[0,6], retain paths with middle parity 000. A step in direction 2i+ε at stage s∈{0,1} demands z_(i,4P+(Q XOR s11))=ε XOR s. Discard paths with contradictory demands on the same bit, and form a clause forbidding all demands of each remaining path. Of 40,320 rooted-cut candidates, 15,744 are internally consistent, producing 13,440 distinct blocking clauses of sizes five and six. A 220-clause subset is unsatisfiable: a standalone complete DPLL procedure with unit propagation closes in 405 nodes, maximum depth twelve. An independent SMT solver also finds UNSAT; an independent path generator confirms every core clause has a simple rooted original-direction path witness. Hence no gate assignment blocks every prescribed-midpoint completion.

**Transfer theorem.** Assume NORI1 in dimension 2(m-|S|). If S is nonempty, q-outgoing-closed, and |S|≤3, then any legal coloring c on Q_(2m) is successful and remains so after every legal paired-square switch. Proof: fix internal parity p_S=u. Outside gates ignore q_S, so they restrict to a legal odd paired-flat coloring on R=[m]\\S. Choose a red exterior full geodesic E from y to bar y. Its gates remain red when the internal state is held at parity u. At the exterior endpoints, internal gates obey the seam relation, so the prescribed-midpoint lemma supplies internal red caps, together using each original direction once. For a switch inside S, redo the caps under the new tables. For a switch outside S, choose u distinct from its prescribed internal parity v; E and the internal caps avoid both switched squares.

**Critical restriction.** In a least-dimensional NORI1 counterexample, and on both sides of a neighboring good-to-bad paired-square boundary, every nonempty q-outgoing-closed set has size at least four. Every terminal SCC of D_q therefore has at least four labels. In Q8 and Q10 any hypothetical counterexample has strongly connected D_q: a proper terminal four-label component in the five-label case leaves an exterior singleton whose gate must read an internal q bit by antipodal oddness, contradicting terminality.

The lemma is a dimension-uniform hypothesis-production mechanism requiring no restriction on nonlinear internal gates or on parity dependence of outside gates. Larger q-feedback components remain unresolved; the boundary-tournament specialization remains separate.

## Near-midpoint forcing and the fixed-cut obstruction

**Finite three-pair theorem.** For all pre-seam gate tables h_i^-, post-seam tables h_i^+(p,q)=1+h_i^-(p,q+111), and every prescribed seam parity u, a red completion exists with cut k in {2,3}; another exists with cut k in {3,4}. Both use every original direction once.

For u=000, enumeration of all roots, direction orders and the two permitted cuts produces 4,992 distinct blocking clauses in the 48 gate variables for each two-cut claim. Both CNFs are UNSAT. An independently verified geometric core for {2,3} has 1,473 clauses and standalone DPLL closes in 8,703 nodes; the {3,4} core has 1,273 clauses and DPLL closes in 7,189 nodes. Independent path enumeration validates all clauses. Vertex translation proves every u.

**Symmetric gate obstruction.** For pair labels i,j,k set
h_i(p,q)=p_j q_k + p_k q_j + (1+p_j)(1+p_k)q_j q_k (mod 2).
The identical gate table for each label has mask 0x6AC8. For seam parity 000, no red completion has cut 3. Such a cut would yield a red one-step-per-pair path and a blue one-step-per-pair path from the same root with complementary endpoints, obtained by antipodal reversal of the post-seam segment. By pair-permutation symmetry it suffices to consider root q=000,001,011,111. The corresponding RED endpoint sets R and BLUE endpoint sets B are:
000: R={011,101,110}; B={000}.
001: R={010,100,110}; B={010,100,110,111}.
011: R={001,010,011,111}; B={001,010,011}.
111: R={000}; B={011,101,110}.
For each row R is disjoint from {b+111:b∈B}. This proves failure of the halfway cut without SAT. Direct enumeration finds successful cuts 1,2,4,5, with 42 rooted words for each.

**Dimension-uniform method obstruction.** For each r>=3 and each cut k∈{0,...,2r}, there are legal r-pair seam data with prescribed seam parity 0 for which k fails. If k!=r, take h_i^-=0 for every pair, hence h_i^+=1: one step per pair must occur on each side, so only cut r can work. If k=r, use the preceding three-pair symmetric obstruction plus r-3 constant gates. Each added pair contributes one step on either side, so a cut of r would force the prohibited three-step cut in the core. Arbitrary interleaving of the extra pairs does not change the argument. The constructions retain original-direction simplicity and the shared antipodal seam relation.

These seam data can be embedded in legal paired-flat colorings by adding exterior pairs a,b with f_a=q_b and f_b=q_a, and letting each internal gate use h^- at q_a=0 and h^+ at q_a=1. An exterior red antipodal geodesic crosses between those two stages.

**Boundary of the result.** Flexible cuts are essential for a general seam argument. The two near-midpoint finite theorems do not extend by themselves to four or more internal pairs, and they do not settle unrestricted NORI1 or the original-vertex-simple boundary-tournament requirement.

## Sharp six-of-eight midpoint capacity and robust exterior-switch transport

**Finite capacity theorem (computer-assisted).** In a three-pair seam with arbitrary pre-seam gates h_i^-, post-seam gates h_i^+(p,q)=1+h_i^-(p,q+111), and prescribed internal seam parity u, at least six of the eight middle q-states support a red completion using every original direction once. The bound is sharp.

*Proof and certificate.* Translate to u=000. For each middle q∈F2^3, enumerate all roots, 6! direction orders, and seven seam cuts that reach middle parity 000 and that q. Retain consistent Boolean demands z_(i,4P+(Q XOR s11))=epsilon XOR s. Each q contributes 1,968 distinct geometric blocking clauses in 48 unrestricted gate bits. If three distinct q-states all failed, their union of blocking clauses would be simultaneously satisfiable. Under translation of all internal q-bits and permutation of pair labels, the 56 three-element sets fall into just three orbits, represented by {0,1,2}, {0,1,6}, {0,3,5}, with sizes 24,24,8. Each representative's blocking CNF is UNSAT. Its independently validated geometric UNSAT core has respectively 980, 685, and 442 clauses. Standalone complete DPLL gives respectively 2,039, 681, and 1,129 nodes and an independent Boolean solver agrees. Thus at most two middle q-states can fail in each prescribed parity fiber. To see sharpness, pre-seam table masks (0x9438,0xCCCC,0xCC33) have successful midpoint q-states {2,3,4,5,6,7}, independently checked by full rooted-direction enumeration. The first two q-states have no completion.

**Parameterized dimension-uniform exterior transport.** Let S be three internal pair labels, and assume every outside gate ignores q_S (arbitrary dependence on p_S is allowed). Let U⊆F2^3 be the set of internal parity settings u for which the fixed-u exterior restriction admits a red full antipodal geodesic; write t=|U|>0. Replace all gates of S by any other legal paired-flat internal gates. In addition, change colors along k legal antipodally paired square-switch orbits supported in direction pairs outside S. If k≤3t−1, the resulting coloring has a red full antipodal geodesic.

*Proof.* Group the k switched square orbits by their internal S parity signature u. Among t available successful signatures, one has at most two associated orbits. Choose its exterior red full geodesic E_u and freeze the internal state during E_u at parity u. The internal state of a square and that of its antipodal square form one complementary pair of q-states in this parity fiber, so the two selected exterior orbits exclude at most four of its eight q-states. For the NEW internal gates, the seam-capacity theorem gives at least six successful middle q-states. Choose one outside the excluded set, insert its red internal caps around E_u, and obtain a red full geodesic that never traverses any changed outside edge. It remains red in the modified coloring. Arbitrary nonlinear new internal gates, outside dependence on p_S, arbitrary root choices, shared-edge consistency, and each original direction's single use are retained.

If NORI1 holds in exterior dimension 2(m−3), all eight parity restrictions are successful, so t=8 and up to 23 exterior square-switch orbits may be changed along with arbitrary replacement of all three internal gates. This conclusion is dimension-uniform, conditional on the explicitly stated smaller-dimensional NORI1 hypothesis. Success of an original coloring alone need not give a successful fixed-u exterior restriction when outside gates read p_S.

**Limits.** The capacity theorem concerns a three-pair terminal block. It does not provide a seam-completion theorem for an arbitrary-size strongly connected q-dependency core, nor the original-vertex-simple boundary-tournament specialization.

## Strongly connected nonlinear seam cores with exponentially sparse midpoint support

**Theorem (dimension-uniform method obstruction).** For each integer k≥2 there is a legal seam instance with r=3k internal pair labels, prescribed middle pair parity 0^r, and a strongly connected q-dependency digraph, whose successful middle q-set M has cardinality 6^k. Therefore |M|/2^r=(3/4)^k tends to zero, despite full directed q-feedback. The example also embeds in a legal antipodally odd paired-flat cube with two exterior pairs.

*Gates.* Partition the r internal pair labels into triples B_t indexed modulo k. In block B_t, for i∈B_t let j,l be the other two labels and designate a_{t+1} in the next block. Define the stage-0 red selector
h_i(p,q)=(q_j+q_l)(p_j OR p_l OR q_(a_{t+1}))
over F2. Define the stage-1 gate by the seam law h_i^+(p,q)=1+h_i(p,q+1_r). Every h_i ignores its own pair. Its dependence on q_j and q_l is essential (choose p_j=1), and its dependence on q_(a_{t+1}) is essential (choose p_j=p_l=0, q_j≠q_l). Thus each block has all internal q-arcs and the blocks have cyclic linking arcs. The entire digraph is strongly connected.

*Upper bound from a path invariant.* Fix a middle vertex z with p=0 and q uniform, either 000 or 111, on some triple B. Under the standard seam transformation, completion at z is equivalent to finding red and blue original-direction-simple paths from z and bar z to one common endpoint, respectively, with complementary used-direction sets. The red path from z initially has q constant on B, so its first move in B necessarily uses the even member 2i, changing q_i and p_i from its initial parity 0 to 1. Thereafter, for j≠i within B, the other two q-bits differ and p_i=1; hence h_j=1 and every red j-move uses its odd member, preserving q_j. For the already used label i, the other two q-bits agree, so h_i=0 and a second red i-move would reuse original direction 2i. Simplicity prohibits that. Thus every red path from z changes at most one q-bit in B. Along any blue path from bar z, the three q-bits remain uniform: h_i=0 and every blue move is an odd member, preserving q_i. Its q triple is uniformly complementary to that of z. The red and blue endpoints cannot coincide. This remains true under arbitrary movements in other blocks because every invoked selector is independent of the cyclic exterior reader when it matters. Therefore any middle state with a uniform q-triple in some block is forbidden. At most 6^k middle states remain.

*Lower bound by protected red/blue paths.* In one triple with middle parity 000 and nonuniform q, there are red and blue three-step paths from z and bar z to the same endpoint, with complementary direction sets, such that every traversed selector is insensitive to the exterior q reader. It suffices by permutation symmetry to check two middle q representatives:

q=001: middle cube vertex z=3, RED word (0,4,3) from z, BLUE word (1,2,5) from bar z; both end at vertex 26.

q=011: middle vertex z=15, RED word (4,2,1) from z, BLUE word (5,0,3) from bar z; both end at vertex 25.

For every step of these paths, either q_j=q_l or p_j OR p_l=1, so h_i is independent of q_(a_{t+1}); checking the red and blue selector in each case gives the stated color. Pair-label permutation generates all six nonuniform q states. For a global middle vertex with nonuniform q in every triple, concatenate the protected red paths over blocks and concatenate the protected blue paths over blocks. Their endpoints agree blockwise, their direction sets partition all 2r original directions, and arbitrary interleaving preserves edge colors because cross-readers are inactive on the chosen steps. Undo the blue-path seam transformation to obtain the required red completion. Thus every one of the 6^k candidate middle states succeeds, proving |M|=6^k.

*Legality in a larger cube.* Adjoin two exterior pairs a,b with red gates f_a=q_b and f_b=q_a. On internal pair i choose its gate f_i=h_i when q_a=0, and f_i=1+h_i(p,q_S+1_S) when q_a=1. Each gate ignores its own pair, and simultaneous complementation of all q-bits changes its value by 1. A red exterior full geodesic exists that changes q_a from 0 to 1; cap paths before and after it have the two stated seam stages. The terminal q-dependency component S contains 3k≥6 labels and is strongly connected, consistent with the necessary minimum-core restrictions. No conclusion for unrestricted good-to-bad square boundaries or boundary-tournament simple paths is claimed.

*Implication.* Even restricting to a single strongly connected nonlinear q-core does not supply a dimension-independent positive fraction of admissible midpoint fiber states. The existential seam completion statement for arbitrary r remains open. This obstruction corrects attempts to extrapolate the six-of-eight capacity theorem as a uniform fractional bound.

## Pairwise midpoint exclusion is fully realizable

**Proposition (three internal pairs).** For any prescribed seam parity u and any two different middle q-states a,b, legal pre-seam gate tables exist for which the successful middle-state set is F2^3 minus {a,b}. The preceding six-of-eight theorem shows that no three states can simultaneously fail.

For u=000, represent each gate by its 16-bit mask with bit index 4P+Q (P,Q are the other pairs' parity and first-member bits). Representatives for forbidden {000,001}, {000,011}, and {000,111}, respectively, are the triples
(0x8149,0xCC33,0xCCCC), (0x0000,0xC465,0x9AC8), and (0x9A6A,0x966D,0x9671).
A standalone two-stage subset DP confirms their respective successful sets are {2,3,4,5,6,7}, {1,2,4,5,6,7}, and {1,2,3,4,5,6}. The DP starts with R_s(empty,z)=1 and sets R_s(A,z)=OR_(d in A)[R_s(A\\{d},z) AND (stage-s red edge at z XOR (A\\{d}) in direction d)]; a completion at middle z exists iff some A has R_0(A,z)=R_1(D\\A,z)=1. Each successful path uses every original direction once. Translating both original bits of any pair changes its middle q bit while keeping its parity, and relabeling pairs permutes the three q bits. These symmetries carry the three representatives to every unordered pair {a,b}. An independent Python script verifies all 28 pairs by this method.

**Method limit.** For forbidden {000,111}, the three remaining antipodal q-pairs can be excluded by three exterior switched-square orbits. Thus a three-orbit uniform avoidance theorem cannot follow solely from the six-of-eight capacity statement. Extra information relating the outside red path to the switched-edge supports is necessary. This does not assert that three legal switches destroy all full-cube witnesses.

## No proper frozen exterior red geodesic in cyclic reader systems; sharp four-block interleaving

**Dimension-uniform method obstruction.** For every m>=2, let the legal paired-flat gate system be f_i(p,q)=q_(i+1 mod m). The q-dependency graph is one strongly connected directed cycle. For every nonempty proper pair-label subset S and R=[m]\\S, every slice with the S-pairs frozen has NO red full exterior geodesic on the original directions belonging to R. Indeed the directed cycle contains an arc i→i+1 from R into S; the red selector f_i=q_(i+1) is constant while the S-state is frozen, so a red exterior-only path cannot use both distinct members of pair i.

Despite this obstruction, red full antipodal geodesics exist, and the minimum number of contiguous S-versus-R blocks in such a geodesic is four. A directed cycle crosses the cut in both orientations. The two visits to a pair in R reading a pair in S must straddle the unique q-flipping red even step of that reader in S; hence the R-directions cannot form one contiguous block. The symmetric argument forces two S-blocks. Thus at least four blocks are necessary.

For an explicit four-block witness, let A and B be any topological orders of the induced directed paths i→i+1 within S and R. Set the initial within-pair bits q_j=1 if the predecessor label j-1 lies in S, and q_j=0 otherwise; initial pair parities are arbitrary. The full pair-word A,B,reverse(A),B is red: its blocks select respectively odd members of S, even members of R, even members of S, and odd members of R. This follows inductively from the ordering and the fact that each gate reads the next pair's current q-bit. Thus every original direction occurs once. The construction and lower-bound argument work uniformly for every m and every proper cut; finite code independently checks all cuts through m=9.

**Research implication.** No amount of improvement to a SINGLE-SEAM theorem that first finds a red full exterior path in a frozen slice can establish unrestricted NORI1 from global success. Even successful fully q-strongly-connected colorings may have no such exterior paths for any proper cut. A full-class transfer requires interleaved outside/internal directions or a mechanism that manufactures a suitable frozen exterior path from substantially stronger assumptions. The separate boundary-tournament simple Hamiltonian conclusion remains open.

## Failure of universal four-block interleaving even with full q-feedback and free roots

**Theorem (affine strongly connected four-pair obstruction, with an all-dimension extension).** For every m≥4 there is a legal paired-flat coloring of Q_(2m), red-successful from EVERY root, and a nontrivial partition of pair labels into groups S and R, such that any red full antipodal geodesic has at least five contiguous S/R blocks. In the base dimension Q8, the q-dependency graph is strongly connected and every root has a five-block red geodesic.

*Four-pair gates.* Write x_(2i)=q_i and x_(2i+1)=p_i+q_i over F2. For S={1,3}, R={0,2}, put
f_0=1+q_1+q_2+q_3+p_1;
f_1=1+q_0+p_2;
f_2=q_1+p_3;
f_3=q_0.
Every gate ignores its own pair. All have odd total q-influence, so their value changes under simultaneous complementation of transverse q. Thus the original undirected edge coloring is legal and antipodally odd. Its q-influence arcs include 1→0,2→0,3→0,0→1,1→2,0→3; hence D_q is strongly connected.

*Root-independent lower bound.* Let w be any permutation of the eight original directions, and denote by I_i(w) the directions strictly between its two occurrences of pair i. For a red geodesic, the selector values f_i at those two visits must differ by one, because the two different members of pair i are used. The four necessary equations are
sum_(d in I_i(w)) [1_(d/2 in P_i) + 1_(d even)1_(d/2 in Q_i)] = 1 mod 2,
where
P_0={1}, Q_0={1,2,3};
P_1={2}, Q_1={0};
P_2={3}, Q_2={1};
P_3=empty, Q_3={0}.
These are identities in the SAME gate functions, independent of the root. Of 8!=40,320 original-direction permutations, 14,976 have at most four contiguous S/R blocks; direct exhaustive enumeration shows none satisfies all four necessary equations. The attached compact Python verifier enumerates these words and tests the equations independently of any red-path DP. Hence no red geodesic has four or fewer blocks.

*Success with five blocks from every root.* The independently implemented subset-state DP on all 256 roots finds a five-block red antipodal geodesic from each root (and verifies every used edge). From root 0, direction order (3,4,1,6,0,5,2,7) is red, uses every original direction once, and ends at 255. Its group sequence is S,R,R,S,R,R,S,S: five blocks. For reproducibility, the gate tables as 64-bit masks, using the six other original-direction bits in increasing order, are respectively 0x3C3CC3C33C3CC3C3, 0x5AA55AA55AA55AA5, 0xF0F00F0F0F0FF0F0, 0xAAAAAAAAAAAAAAAA.

*Extension to all m≥4.* Adjoin new pair labels j≥4 with gates f_j=q_0. Retain the original four gates, which ignore the new pairs, and assign all new labels to R. Every full red geodesic in the enlarged coloring projects, on deleting the new directions, to a full red geodesic in the base Q8; deletion cannot increase its number of S/R blocks, so five blocks are necessary globally. Conversely, take a red base geodesic from any original root. Its q_0 flips once, when direction 0 is used. Insert each new pair's first red direction before that flip and its remaining red direction afterward. These new steps leave original gates unchanged and each pair uses both its original directions. This gives a red full antipodal geodesic from every enlarged root. All gates remain legal and antipodally odd. Strong connectivity of the full D_q is asserted only for the base Q8.

**Closure implication and restraint.** This defeats the universal four-block/two-seam normalization even inside affine gate systems with strong q-feedback and complete root freedom. Any attempted proof of unrestricted NORI1 from a bounded two-seam repair must supply further critical-boundary hypotheses that exclude this example, or allow more interleavings. The construction is successful, so it is no counterexample to NORI1, the good-to-bad square-switch theorem, or the separate boundary-tournament requirement.
