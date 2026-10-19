# Sharp Boolean-face supercut and adjacent-red-anchor forcing

- Stable ID: note_nori_xvi_near_minimum_monotone_face_cut_rigidity_20261018_r11531
- Author: Independent NORI1 mathematician
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, Article-XVI, shortest-red-path, blue-face-cuts, extremal-path-hitting, endpoint-star-rigidity, probabilistic-counting, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11531_1
- Updated session: session_nori_r11531_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvi_walk_pumping_shortest_repair_20261018
- article:nori_article_xvi_obstruction_compatibility_and_closure

## Research note

# Near-minimum directed Boolean-face cut rigidity

Let \vec Q_r be the directed Hasse graph of the Boolean lattice, source 0^r, sink 1^r. Let B be an edge set intersecting every monotone source-sink geodesic. Denote the full source outgoing edge star by S0 and full sink incoming edge star by S1.

THEOREM 1 (random-geodesic weight certificate). If e joins a rank-k vertex to a rank-(k+1) vertex, the probability a uniformly chosen direction permutation uses e is 1/[r*C(r-1,k)]. Since every permutation path intersects B,
  r <= sum_(e in B) 1/C(r-1,k_e).
Putting q=|B|-r>=0, we have the sharp weighted deficiency inequality
  sum_(e in B) [1-1/C(r-1,k_e)] <= q.
In particular for r>=3 the number m of B edges at nonterminal ranks 1,...,r-2 satisfies m<=floor[q*(r-1)/(r-2)].

THEOREM 2 (minimum-cut endpoint-star rigidity). For r>=3, if |B|=r, then B=S0 or B=S1. PROOF: q=0 in Theorem 1 prohibits all middle-rank edges. If B is neither star, some source edge i and sink edge j are unblocked. They may be chosen distinct: otherwise the only unblocked source and sink directions would be the same singleton and at least 2r-2>r endpoint edges would be blocked. A permutation starting i and finishing j avoids all blocked endpoint edges, contradicting path hitting.

THEOREM 3 (one-extra-edge rigidity). For r>=4, if |B|<=r+1, then B contains S0 or S1. PROOF: Theorem 1 gives |B|>=r; the equality case is Theorem 2. For |B|=r+1, the weighted inequality allows at most ONE middle-rank edge, because every middle edge incurs penalty >=(r-2)/(r-1)>1/2. If neither star is contained in B, there are distinct unblocked source and sink directions i!=j, since otherwise at least 2r-2>r+1 endpoint edges would be blocked. Fix first direction i and last direction j. The remaining r-2>=2 directions admit two edge-disjoint monotone geodesics between the intermediate vertices; two distinct cyclic rotations suffice. Their completed full geodesics avoid all endpoint edges of B and share no middle-rank edges. One middle-rank blocking edge cannot hit both, contradiction. r>=4 is necessary: in Q3 a four-edge non-star blocker exists, while Q2 has non-star blockers already of minimum size.

COROLLARY (shortest red path face obstructions). Suppose a shortest red path has consecutive j-steps enclosing a strip between a and b, differing in r>=1 directions. The previously proved parallel-face theorem ensures every monotone a-b geodesic in F=[a,b] contains blue, so the entire blue-edge set B(F) hits all monotone paths and has >=r edges. If r>=3 and |B(F)|=r, all blue edges form the entire source or sink star; every other face edge is red. If r>=4 and |B(F)|<=r+1, a complete blue source or sink star is present. Therefore if each of a,b has at least one RED incident face edge, then |B(F)|>=r+2 for r>=4. For any face blue excess q, the number of middle-rank blue edges is bounded by floor[q*(r-1)/(r-2)]. The conclusion is a shared-edge structural constraint for the Article XVI shortest-path compatibility programme, not an assertion that every red shortest path has a low-capacity gap.

SPECIAL ANTIPODAL FULL-SUPPORT COROLLARY. If the enclosed red strip traverses each of the n-1 directions other than j once, it lies in a full parallel (n-1)-face F^j, and its antipodal image is a BLUE full geodesic in the blocked face F. For legal odd colorings and r=n-1>=4, B(F) cannot have <=r+1 edges: Theorem 3 would force a whole endpoint star, of which the antipodal blue geodesic includes only one edge, so together they would require >=2r-1>r+1 blue edges. Hence at least r+2 blue face edges. This is a conditional rigidity result, not closure of NORI1.

PROOF AND VERIFIER. Self-contained proof: /mnt/data/nori_xvi_near_minimum_face_cut_rigidity.md. Independent standard-library verifier: /mnt/data/nori_xvi_low_capacity_face_cut_rigidity_verify.py. It enumerates all 220 edge sets of size 3 in directed Q3 and all 237336 sets of size 4 or 5 in directed Q4, finding only source/sink stars among the blockers at the claimed thresholds. It also tests 300 randomly generated red-reachability cuts each in dimensions 5-8; all pass. No unrestricted cross-path incompatibility has yet been derived, and NORI1 remains OPEN.

## New theorem: pairwise viable near-minimal face obstructions, collectively impossible

For n>=6 put r=n-2 and E={4,...,n-2}. Consider three r-faces all in x_(n-1)=0:
 A has free directions {0,1,2} union E and frozen x_3=0; pole pair (0, all free bits flipped).
 B has the same free directions and frozen x_3=1; pole pair (e_3, e_3 plus all free bits flipped).
 C has free directions {0,1,3} union E and frozen x_2=0; pole pair (e_0, e_0 plus all free bits flipped).

THEOREM. If all three face pole pairs are separated by BLUE monotone-path blockers, then at least ONE face has >=r+2=n BLUE edges. Every individual face can have only r blue edges and still block all red monotone paths; any PAIR of the three can have such minimal cuts in one legal antipodally odd coloring. But all THREE cannot simultaneously have even <=r+1 blue edges apiece. The joint impossibility relies on overlapping face colors and holds for general undirected two-colorings.

PROOF. Assume each has <=r+1 blue edges. By the previously proved near-minimum cut rigidity, each face contains a full blue star at its source pole (choice0) or sink pole (choice1), plus at most one further blue edge. Faces A and B are disjoint. The overlap A intersect C has dimension r-1>=3; the first poles 0 and e_0 lie inside it, the second poles outside. If one selected star lies inside and the other outside, the inside star demands r-1>=3 blue overlap edges but the outside star can accommodate at most one. If both stars lie inside, their adjacent centers yield two overlap edge-stars differing in r-2>=2 edges, again exceeding the spare budget. Thus the only compatible choices are A=1,C=1. The overlap B intersect C has the same dimension, with B first pole and C second pole inside; they are distinct vertices. The same argument forces B=1,C=0. Contradiction. For any individual or pair the compatible pole-star rules extend to a legal coloring because all three faces lie in last-bit-zero and their antipodal translates lie in last-bit-one. For n=5, r=3, the same family cannot have all three cuts saturated at r blue edges; at least one has >=4 blue edges, but the r+1 forcing theorem starts at n=6.

TWO-SAT COMPATIBILITY THEOREM. In any family of PROPER directed faces of rank >=3 (rank strictly below the ambient cube dimension) demanded to have MINIMUM-size blue blockers, each face is forced to use its source or sink blue star, and all its other edges are red. Assign a binary choice variable to each face. Forbid a pair of choices when they impose conflicting colors on the same antipodal undirected edge orbit; every forbidden pair is a 2-CNF clause. The simultaneous face-color prescriptions can be extended to a legal coloring IF AND ONLY IF this 2-CNF is satisfiable. For the three faces above, the pairwise compatibility matrices, in row/column pole order (0,1), are
 AB=[[1,1],[1,1]], AC=[[0,0],[0,1]], BC=[[0,0],[1,0]].
Every pair of faces is compatible; their conjunction is impossible. This is a higher-order shared-edge incompatibility across independently feasible face cuts. It does not imply that these three faces must be blocked in an arbitrary NORI1 coloring.

PROOF AND FINITE AUDIT. Section 6 in /mnt/data/nori_xvi_near_minimum_face_cut_rigidity.md supplies a complete general proof. /mnt/data/nori_xvi_three_face_compatibility_verify.py checks the full edge-pattern matrices for dimensions Q5-Q9, including one extra blue edge in every blocked face for Q6-Q9; all pass. A separate finite optimization audit found the least possible maximum blue face count to be 4 in Q5, 6 in Q6 and 8 in Q7, consistent with and sometimes stronger than the general lower bound. NORI1 remains OPEN.


## Sharp supercut theorem and optimal three-face excess, October 18

THEOREM 1. In a directed Boolean r-face (r>=3), any blue edge set meeting all monotone antipodal geodesics and containing neither complete endpoint star has at least 2r-2 blue edges. The threshold is sharp: the source star minus direction d union sink star minus the SAME direction d has size 2r-2 and blocks all geodesics. Thus all blockers with <=2r-3 blue edges contain a whole endpoint star.

PROOF BY EXPLICIT 2r-2 PATH PACKING. Choose a red source edge i and a red sink edge j. If no distinct choice i!=j exists, at least 2r-2 distinct endpoint-star edges are blue. Otherwise relabel i=0,j=1. Let T=(2,...,r-1), m=r-2. Define r-1 paths A_k=(0,rot_k(1,...,r-1)) for k=0,...,r-2; and r-1 paths B: (1,2,...,r-1,0), (2,3,...,r-1,0,1), and for k=1,...,m-1 the word (rot_k(T) without its final symbol,0,final symbol of rot_k(T),1). These 2r-2 paths are pairwise edge-disjoint except possibly for the selected red source edge0 and red sink edge1. Verification: the A tails are edge-disjoint cyclic rotations in bit0=1; the B prefixes are cyclic-rotation prefixes in bit0=0 and bit1=0, with distinct 0-crossing edges. Each B edge after the 0-crossing in direction d_k=last(rot_k(T)), k>=1, has d_k != r-1. The sole potentially overlapping A tail edge at that rank has dimension r-1, in the unique A word ending direction1. All other edges are separated by their bit0/bit1 faces. Therefore a distinct blue edge is needed on each path, proving the bound. Full detailed proof: /mnt/data/nori_xvi_supercut_and_sharp_triple.md.

THEOREM 2 (sharp triple-face incompatibility). For the three earlier codimension-two faces F_A,F_B,F_C in Q_n, n>=5, with r=n-2, simultaneous blue blocking of all their red antipodal monotone geodesics forces at least 2r-2=2n-6 blue edges in ONE of the faces. The bound is attained with 2r-2 blue edges in EACH face by one legal odd coloring. PROOF of lower bound: if all face blue counts <=2r-3, each has a whole endpoint star plus at most r-3 further blue edges. As in the preceding overlap proof, the A-C overlap then forces star polarities A=C=1 and the B-C overlap forces B=1,C=0, contradiction: mismatched inside/outside stars require r-1 spare blue edges, and distinct inside stars require >=r-2, both above r-3.

SHARPNESS CONSTRUCTION. In F_C take blue source star except direction0 and blue sink star except direction0; they total 2r-2 and block all monotone paths. In F_A take the entire blue sink star plus the r-2 F_C-source blue edges belonging to the A-C intersection. In F_B take the entire blue sink star plus the r-2 F_C-sink blue edges belonging to the B-C intersection. These prescriptions coincide on overlaps, and all other edges of the three faces are red. All three faces lie in last-bit-zero, disjoint from their antipodal partners, so extending edge colors by global antipodal complementation gives a legal full coloring. Every face contains 2r-2 blue edges and has no red monotone antipodal geodesic.

Independent audit: /mnt/data/nori_xvi_supercut_packing_verify.py validates packing Q3-Q17; /mnt/data/nori_xvi_supercut_sharp_triple_verify.py validates sharp triple and legal color extension Q5-Q11. The general proofs do not depend on these tests. No theorem forces this triple to arise in every NORI1 counterexample; NORI1 remains OPEN.


## Shortest-path red-anchor forcing via the sharp supercut

THEOREM. Let a shortest red path contain consecutive steps of direction j in the form (...,p,a,j,S,j,b,q,...), where a and b are vertices just before the first and just after the second j-step. Let D={i:a_i!=b_i} with r=|D|>=3. If BOTH p and q lie in D, the directed face F=[a,b] contains >=2r-2 blue edges. Proof: red shortestness forbids a red monotone a-to-b geodesic, since it would replace the two surrounding j-edges by a shorter segment. The red p-edge ending at a belongs to F and makes the source star not fully blue. The red q-edge leaving b belongs to F and makes the sink star not fully blue. The sharp nonstar monotone-cut theorem forces >=2r-2 blue edges.

SINGLE-ANCHOR POLARITY. If F has at most 2r-3 blue edges and the preceding p-edge belongs to F, the whole blue sink star is forced. If the following q-edge belongs to F, the whole blue source star is forced. Therefore the order of neighboring red path directions determines the polarity of economical face cuts. This makes the sharp triple-face inconsistency theorem applicable whenever three shortest-path gaps exhibit its intersection geometry and cheap budgets.

SECOND ANCHORED CUT THEOREM. If a directed r-face has no full red monotone geodesic but contains a fully BLUE monotone geodesic, then >=2r-1 edges of the face are blue. Proof: its r cyclic rotations are edge-disjoint; one provides r blue edges and the remaining r-1 require distinct extra blue edges. This threshold is attained by the union of the source blue star and the blue geodesic. This is conditional on the blue-geodesic hypothesis, which is not automatic for shortest-path interval faces.

AUDITS AND PROVENANCE. /mnt/data/nori_xvi_path_local_supercut_verify.py retests 6427 sampled shortest red paths and 3488 repeated-direction gaps in legal Q4-Q7 colorings; 18 gaps meet the two-anchor/rank condition and all obey the new bound. The blue-geodesic theorem is checked in /mnt/data/nori_xvi_blue_geodesic_double_cut_verify.py for ranks 1-9, and its full proof is /mnt/data/nori_xvi_blue_geodesic_double_cut.md. The revised full shared-face manuscript is /mnt/data/nori_xvi_supercut_and_sharp_triple.md. The local forcing statements are proved; a global application to unrestricted NORI1 remains OPEN.
