# Global diagonal-fiber compatibility, overlap connectivity, and sharp strong-orientation obstructions

- Stable ID: note_nori_joint_cyclic_orientations_sparse_fibers_20261017_r11435
- Author: Independent NORI1 researcher
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, global-diagonal-fibers, connected-overlap-graph, endpoint-rotation, directed-orientations, strong-connectivity, near-full-fibers, full-geodesic-obstructions, verified
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_1
- Updated session: session_nori_r11435_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_diagonal_fibers_directed_cycle_rigidity_20261017
- note:note_nori_profile_integrability_three_local_laws_20261016_r11254

## Research note

THEOREM (jointly cyclic label orientations with exponentially sparse full-geodesic fibers). For every k>=1 put n=4k+3. Partition the cube directions into k four-element sets B_r={4r,4r+1,4r+2,4r+3}, 0<=r<k, and auxiliary directions a=4k, b=4k+1, d=4k+2. Set E(x)=sum_r(x_(4r)+x_(4r+1)), with arithmetic in F_2. Define the following affine undirected-edge rules:
c_i(x)=sum_(j in B_r\{i})x_j+x_a+x_b for i in B_r;
c_a(x)=x_b+E(x), c_b(x)=x_d+E(x), c_d(x)=x_a.
For each signature z, orient a direction-i edge from x iff p_i(x)=z_i, where p_i(x)=x_i+c_i(x). Let A_z consist of the roots of directed full antipodal geodesics in this orientation.

CLAIMS. (1) The coloring is legal and its directed influence graph is strongly connected. (2) For EVERY signature z, each of the 2^(4k) three-dimensional faces with free directions {a,b,d} contains a directed six-cycle; these cycles are vertex-disjoint and cover 3/4 of the cube's vertices. (3) If z is constant on any four-direction block B_r, then A_z is empty. Consequently |{z:A_z nonempty}|<=8*14^k, whereas |{z:A_z empty}|>=8*(16^k-14^k). The supported-label fraction is at most (7/8)^k=exp(-Omega(n)). Thus simultaneous cyclicity of all 2^n orientations, extensive directed-cycle density for each one, and strongly connected influence do not imply that a positive fraction of labels have nonempty full-geodesic fibers.

PROOF OF LEGALITY AND CONNECTIVITY. Every rule ignores its own vertex bit. Complementing the vertex toggles each block rule because its three other block bits change parity and x_a+x_b is antipodally even. E is antipodally even, while the single auxiliary reader in c_a,c_b,c_d flips. Each B_r has a complete directed influence graph. Both a,b influence every B_r; the dimensions 4r,4r+1 influence a,b; the auxiliary rules have influence arcs b->a, d->b, a->d. This proves strong connectivity.

PROOF OF SIX-CYCLES. Fix an auxiliary face, so E is constant. Its three-dimensional source-label fingerprint is
(p_a,p_b,p_d)=(x_a+x_b+E,x_b+x_d+E,x_d+x_a).
Its image consists of the four even-parity three-bit words, each attained at one antipodal pair of face vertices. When z_A is even, the pair p_A=z_A consists of two sources; the other six vertices have outdegree one and form an induced undirected six-cycle, whose orientation is cyclic. When z_A is odd, the pair p_A=bar(z_A) consists of two sinks; each of the other six vertices has outdegree two, one edge pointing to a sink and one along the induced six-cycle. Again the six-cycle is directed. The auxiliary faces partition the n-cube, yielding 2^(4k) vertex-disjoint directed six-cycles for every z.

PROOF OF FIBER SPARSITY. Put t_r(x)=sum_(j in B_r)x_j+x_a+x_b. For all i in B_r one has p_i(x)=t_r(x). Along a directed full antipodal geodesic with label z, immediately before its direction-i step (i in B_r) we must have t_r=z_i. Every step in B_r toggles t_r; so do steps a and b; steps from other blocks and d leave t_r unchanged. If z_i is the same for all four dimensions i of B_r, then between each successive pair of those four steps t_r must be toggled again by at least one of a,b. The three intervening intervals are disjoint, while only two auxiliary steps a,b are available. Contradiction. Therefore z restricted to every B_r is nonconstant, with only 14 choices per block and 8 choices on the auxiliary directions.

EXPLICIT RED FULL PATH (the family is not a NORI1 counterexample). Choose root bits (0,0,1,1) on each B_r and (x_a,x_b,x_d)=(1,0,0). Traverse each block in the order (4r+2,4r,4r+3,4r+1), for all r, and then use a,b,d. Every block step has c_i=t_r+x_i=0 because t_r and the unflipped direction bit alternate 1,0,1,0. After all block steps E=0; the auxiliary edges (a,b,d) all have color zero.

INDEPENDENT VERIFICATION. Standard-library script /mnt/data/nori_global_joint_cycle_exp_sparse.py validates all edge rules, antipodal oddness, strong directed influence, antipode-free fingerprint image, and the induced directed six-cycle in every auxiliary face for k=1,2,3 (n=7,11,15). Tests encompass 128, 2048 and 32768 auxiliary-face/signature cases respectively. For k=1 it enumerates all 2^7*7!=645120 rooted full orders and obtains 112 supported labels, every supported fiber equal to the whole Q7, 16 empty fibers, and 5040 red rooted orders. For k=2 a 150000-path random sample visits all 1568 labels permitted by the upper bound; for k=3 a 100000-path sample obeys the upper bound. Only the upper bound is asserted dimension-uniformly; saturation in all dimensions is unproved.

LIMITATION AND RELATION. This obstruction concerns directed cycles of length six residing in auxiliary faces, not antipodally symmetric 2n-cycles. It prevents using the global existence or abundance of shorter directed cycles as a substitute for full-geodesic attainment. Stronger compatibility laws linking the positions of each signature to full antipodal cycles could still prove NORI1. The preexisting diagonal-fiber cycle rigidity note concerns individual fibers and selected cross-fiber mutations; this construction concerns ALL label orientations simultaneously.

## STRENGTHENING: classification of strongly connected label orientations

THEOREM. In the same n=4k+3 construction, O_z is strongly connected as a directed graph on ALL 2^n cube vertices if and only if at least one block B_r carries a nonconstant label z|_(B_r). Consequently for every k>=2 there are labels z with A_z EMPTY although O_z itself is strongly connected. For instance choose z|_(B_0)=0000 and z|_(B_1)=0011; the remaining label bits are arbitrary. Thus even strong connectivity of the corresponding ORIENTATION, not merely its directed influence graph, cannot force a directed full antipodal geodesic.

PROOF (sufficiency). Fix a block B_* on which z is nonconstant, and regard its four bits as an internal state; all other bits form an outer cube. For every fixed outer state, the orientation on the B_*-face is strongly connected. Indeed, for any internal direction i select another internal direction j with z_i different from z_j. On every i,j-square the common fingerprint p_i=p_j=t_*(x) toggles upon traversing either direction, so that square is a directed four-cycle. Therefore every internal cube edge belongs to a directed cycle. Since its undirected cube is connected, its orientation has a single strongly connected component: any edge between distinct components would lie in no directed cycle.

The internal four-bit state can consequently be adjusted arbitrarily while fixing all outer bits. In particular, its chosen special-bit parity x_(min B_*)+x_(min B_*+1) can be set to either value. This permits either direction of every auxiliary a-edge or b-edge in the OUTER projection: the outgoing condition for each such edge has coefficient one on E, and E can be freely adjusted through the internal state.

Every other outer edge is likewise traversable in both directions by a directed path after allowing internal-state adjustments. For a d-edge, p_d=x_d+x_a; if its outgoing condition fails, traverse a, then d, then a again. The first a-toggle makes d outgoing, and both a-toggles are available via internal-state adjustments. For an edge of another four-block B_s, p_i=t_s=parity(x|_(B_s))+x_a+x_b; if its outgoing condition fails, traverse a, then i, then a again. The a-toggle reverses t_s, making the i-edge outgoing. This argument applies to each orientation of every outer edge, from every chosen internal state. Since the outer cube is connected, arbitrary outer targets are reachable. Finally strong connectivity of the internal face over the target outer state reaches any prescribed terminal vertex. Thus O_z is strongly connected.

PROOF (necessity). Suppose every z|_(B_r) is constant. At a source of O_z one needs p_(B_r)=z|_(B_r) and p_A=z_A. For each fixed auxiliary state and each block, the four initial block bits can be selected to prescribe both the block parity and its special-bit parity x_(4r)+x_(4r+1), independently. In particular E can be fixed to zero while prescribing all desired t_r values. On a face with E=0 the map from auxiliary states to p_A surjects onto the four even-parity triples. If z_A has even parity, select an auxiliary state with p_A=z_A, then choose the block states to give p_(B_r)=z|_(B_r). This produces a source of O_z. If z_A has odd parity, its complement has even parity; apply the preceding construction to bar(z), yielding a sink of O_z. Either a source or sink prevents strong connectivity on a nontrivial cube. The classification follows.

INDEPENDENT CHECK. The separate standard-library script /mnt/data/nori_global_joint_scc_verify.py checks the strong-connectivity criterion by forward and reverse reachability in the orientation itself, independently of the influence graph. It exhaustively tests all 128 signatures on Q7 and samples signatures on Q11 and Q15, including strongly connected signatures with a constant block and thus empty A_z. Earlier verifier /mnt/data/nori_global_joint_cycle_exp_sparse.py independently establishes the empty-fiber block obstruction in every dimension by proof and checks finite instances. The strengthened assertion remains a theorem for every k>=1 by the argument above.

## GENERALIZATION TO EVERY ODD DIMENSION N>=11

THEOREM. Let B_1,...,B_k be any partition of n-3 directions into k>=2 even-sized blocks, |B_r|=2m_r>=4, and retain auxiliary a,b,d. In E use the first two directions of each block and keep c_i(x)=sum_(j in B_r\{i})x_j+x_a+x_b and the same auxiliary rules c_a=x_b+E, c_b=x_d+E, c_d=x_a. All assertions of legality, strong directed influence, and 2^(n-3) disjoint directed auxiliary six-cycles in EVERY orientation remain valid. Furthermore every label of a directed full antipodal geodesic satisfies |wt(z|_(B_r))-m_r|<=1 for every block. Consequently

|{z:A_z nonempty}| <= 8 prod_r [C(2m_r,m_r-1)+C(2m_r,m_r)+C(2m_r,m_r+1)].

For m>=2 the ratio S_m=[C(2m,m-1)+C(2m,m)+C(2m,m+1)]/2^(2m) decreases strictly with m, and S_2=7/8. The ratio identity
S_(m+1)/S_m=((2m+1)(3m+4))/(2(m+2)(3m+1))<1
proves this claim. Hence the fraction of supported labels is at most (7/8)^k.

The strongly connected ORIENTATION classification also remains valid: O_z is strongly connected iff z is nonconstant on at least one block. Choosing one constant block and one nonconstant block gives an orientation that is strongly connected while A_z is empty. The direct proof of this classification in the preceding section uses only even block sizes at least four: nonconstant block labels make every internal direction edge lie on a directed square, and four initial block bits suffice to prescribe total parity independently of the chosen special-pair parity.

PROOF OF THE WEIGHT RESTRICTION. For a full directed path, list in temporal order the 2m_r labels of its B_r steps. The associated bit t_r changes after every B_r step and also upon either of the two auxiliary steps a,b. Divide the list of B_r labels into up to three consecutive segments, according as the corresponding steps occur before the first of a,b, between these two steps, or after the second. Within each segment the labels alternate, since t_r toggles after every B_r step and no a,b-step occurs inside the segment. Each segment has difference between the number of ones and zeros of absolute value at most one. Therefore the total difference has absolute value at most three. Since there are 2m_r labels, this difference is even, hence has absolute value at most two. Equivalently |wt(z|_(B_r))-m_r|<=1. This proves the support bound. All six-cycle and strong-connectivity proofs from the equal-sized case apply word for word.

COROLLARY (ALL ODD n>=11). Partition n-3 into as many blocks of size four as possible, replacing one four-block with a six-block when n-3 is congruent to two modulo four. The number of blocks is k=floor((n-3)/4)>=2. For every such odd n there exists a legal affine coloring with strongly connected directed influence such that every O_z contains 2^(n-3) vertex-disjoint directed six-cycles, a positive fraction at least 1-(7/8)^k of labels have empty A_z, and some labels have O_z itself strongly connected although A_z is empty. The empty-fiber proportion tends to one exponentially as n tends through ALL odd dimensions.

The colorings also admit a red full geodesic: choose in each block a root with m_r ones and m_r zeros, the first two selected special bits both zero, and auxiliary root (x_a,x_b,x_d)=(1,0,0). Within each block traverse its original 0-bits and 1-bits alternately, beginning with bit value m_r+1 modulo two; this equals the initial t_r. All block edge colors vanish, E remains zero after every block is completed, and the auxiliary order (a,b,d) is red.

INDEPENDENT GENERALIZED CHECK. The verifier /mnt/data/nori_joint_evenblock_general_verify.py checks n=13 with blocks of sizes four and six: all edge color identities and antipodal oddness, 100000 random rooted full orders satisfying the middle-three-layer signature restrictions, 8192 auxiliary face-label six-cycle tests, and forward/reverse reachability of a strongly connected orientation whose first block signature is constant and whose second block signature is nonconstant. The theorem is dimension-uniform by proof, not by extrapolation from the finite checks.

## Radial energy and shortest nongeodesic directed antipodal paths, all odd dimensions

UNRESTRICTED ENERGY IDENTITY. In O_z the outgoing condition p_i(x)=x_i+c_i(x)=z_i implies c_i(x)=x_i+z_i. Thus every directed red edge increases d_H(.,z) by one and every directed blue edge decreases it by one. Any directed walk of length L from x to y therefore contains

B=[L+d_H(x,z)-d_H(y,z)]/2

blue edges. In particular, a directed closed walk is red-blue balanced, and a directed walk of length n+2k from z to bar z has precisely k blue edges. The colors on successive traversals of any one dimension alternate red, blue, red,...; every direction's first traversal from z is red.

SHARP THEOREM. In EVERY odd dimension n>=11 there is a legal affine coloring c and label z with O_z strongly connected on ALL vertices, A_z empty, and directed distance dist_(O_z)(z,bar z)=n+2. Its directed influence graph is also strongly connected, and all the label orientations contain directed six-cycles in auxiliary 3-faces.

CONSTRUCTION. Partition n-3 dimensions into two even blocks B0,B1 with |B0|=n-7>=4 and |B1|=4, plus auxiliary directions a,b,d. For a designated two-element subset {s_r,t_r} in each block let E=x_(s_0)+x_(t_0)+x_(s_1)+x_(t_1). Take c_i=sum_(j in B_r,j!=i)x_j+x_a+x_b for i in B_r and c_a=x_b+E, c_b=x_d+E,c_d=x_a. The rules satisfy own-direction independence and antipodal oddness. Every block direction has the source fingerprint p_i(x)=t_r(x)=sum_(j in B_r)x_j+x_a+x_b.

For labels z constant on the four-element B1, a directed full geodesic would need three separate external parity resets between four B1 steps; only a and b can reset this bit, providing only two steps. Hence A_z is empty. If the label is nonconstant on B0, every B0 edge belongs to a directed square obtained from an opposite-label partner direction, and each B0-face is strongly connected. By adjusting internal B0 states, one may traverse auxiliary a,b edges in either direction. Any obstructed B1 or d step can be sandwiched between two permitted a-steps, because the first a-step toggles its outgoing condition. Therefore the full orientation O_z is strongly connected; its influence graph is strongly connected by the bidirectional couplings of the blocks and the auxiliary 3-cycle.

EXPLICIT Q11 SEED. Let B0=(0,1,2,3), B1=(4,5,6,7), (a,b,d)=(8,9,10), special pairs (0,1),(4,5), and root-label z=e_0. The word of directions

(0,1,4,8,2,5,8,3,6,10,9,7,8)

gives a directed walk from z to bar z with color sequence

(0,0,0,0,0,0,1,0,0,0,0,0,0).

Every direction occurs once except a=8, occurring three times, so its length is 13.

TWO-DIRECTION LIFT. Suppose a directed antipodal walk for a given even B0 is known, starting at its label z, with B1 constant. Adjoin new dimensions u,v to B0, preserving the designated special pair. Complement all OLD initial B0 bits of z, set z_u=0,z_v=1, and preserve all other bits. Because the old block has even cardinality, its parity is invariant under complementation; the new pair adds one to the parity. Consequently the common fingerprint t_0 throughout all old walk stages changes by one, while the labels z_i of ALL old B0 steps also change by one, so their outgoing constraints remain satisfied. The special-pair parity E is unchanged since both special bits were complemented, so every auxiliary and B1 step remains directed. Insert the two new steps CONSECUTIVELY AT THE BEGINNING, ordering u,v or v,u so that their labels 0 and 1 match the successive toggling values of t_0. The old path then follows unchanged (after relabeling); the pair leaves E unchanged. Both inserted steps are red since each direction has not previously occurred. The result is a directed antipodal walk of length old_length+2 with the same one blue edge. The enlarged B0 remains nonconstant and B1 constant. Iterate from the seed to obtain every n=11+2t.

Every cube walk from a vertex to its antipode has length at least n and congruent to n modulo two. Length n would be a directed full geodesic, impossible since A_z is empty. Our constructed path has length n+2, proving sharpness.

INDEPENDENT CHECK. The verifier /mnt/data/nori_radial_detour_sharp_verifier.py checks every edge of the constructed directed antipodal walk and the one-blue count for n=11,13,15,17,19. It separately checks strong connectivity by complete forward and reverse reachability in n=11,13,15. Full mathematical manuscript: /mnt/data/nori_radial_energy_and_sharp_antipodal_detour.md.

LIMITATION. This invalidates forcing a full geodesic at a chosen label from strong connectivity plus a shortest possible positive antipodal detour, even with only one blue edge. The constructions still have monochromatic full geodesics at other roots; they do not refute NORI1.


## Global overlap connectivity of the full diagonal family

THEOREM. For every legal antipodally odd coloring of Q_n, n>=2, let A_z be its diagonal root fibers and S={z:A_z nonempty}. Join two distinct supported labels z,z' when their Hamming distance is at most two and |A_z intersect A_z'|>=2n-2. This supported-label graph is connected. Further, the bipartite incidence graph between all cube roots and S is connected; for every cube edge xy there exists a z with both x,y in A_z; and A_z=A_(bar z), with each A_z invariant under root complementation.

PROOF. A rooted full-geodesic state is (x,pi), with direction-indexed profile w and label ell=x+w. Cyclic root rotation T carries (x,(i_1,...,i_n)) to (x+e_(i_1),(i_2,...,i_n,i_1)). It complements the i_1 profile bit while also toggling the i_1 root bit, so ell is unchanged. Swapping adjacent directions j,k at fixed root changes w only in j,k, hence HammingDistance(ell,ell')<=2. Continue a geodesic by its antipodal copy to a symmetric isometric 2n-cycle. An adjacent swap replaces one midpoint and its antipode while retaining the other 2n-2 vertices. Every retained cycle vertex belongs to both associated diagonal fibers, so if labels differ, their intersection contains at least 2n-2 roots. All path states are connected by such operations: adjacent transpositions generate all orders at a fixed root; to flip any chosen root direction i, first place i at the beginning of the order and rotate. Root-bit flips reach every root. Projecting this connected state graph to supported labels proves the connected-overlap claim.

For any cube edge x--(x+e_i), take a full path starting at x with leading direction i. The path and its first cyclic rotation have the same label, so both endpoints belong to one A_z. The root cube is connected and each supported label has incident roots, proving bipartite incidence connectedness. Reversing the order at fixed root complements all profile bits, so ell goes to bar ell; complementing the root with the same order complements both x and w, leaving ell unchanged. This gives A_z=A_(bar z) and antipodal root invariance.

OPTIMALITY OF TWO-BIT LABEL TRANSITIONS IN ODD DIMENSIONS. For n=2r+1>=5, partition the first 2r directions into pairs (a_j,b_j), prescribe c_(a_j)=x_(b_j), c_(b_j)=x_(a_j), and prescribe the last rule c_h=x_(a_1). Every signature z of a full directed geodesic has z_(a_j)+z_(b_j)=1 for every pair. Conversely every signature satisfying all these equations is supported: set the pair precedence according to z and choose x_h to satisfy the last bit, placing h after the paired directions. The supported-label set is therefore an affine set containing 2^(r+1) labels; its induced Hamming-one graph has 2^r components, each an edge, because only the final bit can change by one. Thus a universal supported-label connectivity conclusion cannot require every transition to change only one label bit, even for odd dimensions.

INDEPENDENT VERIFICATION. /mnt/data/nori_allfiber_overlap_verify.py exhaustively enumerates all 64 legal Q3 colorings and 100 sampled legal Q4 and Q5 colorings. It constructs every rooted direction order, each diagonal fiber, cyclic-root edge coverage and square-swapped overlaps, then checks connectedness.

## Maximum-size non-self-labeling fiber with strongly connected orientation

THEOREM. There is a legal Q5 coloring with strongly connected label orientation O_0 and A_0=Q5 minus {0,31}. This is the largest fiber possible while 0 is absent, because all fibers are invariant under antipodality.

SEED CERTIFICATE. For each i from 0 to 4, read the other four input bits in ascending direction-index order to form a four-bit integer t_i(x). Define c_i(x) as bit t_i(x), least significant bit indexed zero, of the corresponding truth-table integer:
i=0: 0x6969;
i=1: 0xc69c;
i=2: 0xd694;
i=3: 0x94d6;
i=4: 0xe698.
These five tables ignore their own input bit and obey c_i(bar x)=1+c_i(x). In O_0 an i-edge is outgoing from x precisely if p_i(x)=x_i+c_i(x)=0. Independent complete-vertex directed reachability checks show that every vertex is reachable from zero and can reach zero. Enumerating all 32 roots and all 120 full direction orders, or equivalently using dimension-subset reachability, yields A_0={1,2,...,30}. The verifier /mnt/data/nori_nearfull_scc_truth_table_verify.py reproduces every claim from the five displayed tables. The independent verifier /mnt/data/nori_nearfull_scc_fiber_verify.py checks the same seed with an antipodal edge-orbit encoding.

LIFTING THEOREM, ALL n>=5. Retain the five old rules on Q_n, independent of new vertex bits, and for each new direction j>=5 put c_j(x)=x_0. This defines a legal coloring. Its orientation O_0 is strongly connected and
A_0(Q_n)=(Q5 minus {0,31}) times Q_(n-5),
so |A_0|=30*2^(n-5)=(15/16)*2^n, while 0 and its antipode are excluded.

PROOF. Any directed full n-geodesic projects to a directed full five-geodesic in the initial five directions, because old rules ignore added bits. Conversely let an old root u belong to A_0(Q5), and select its directed full five-geodesic. For a new direction j, the outgoing constraint p_j=x_j+x_0=0 is satisfied either at the starting old root or after the five old flips, since the latter toggles x_0. Insert each new step at the appropriate end of the old path; new flips affect neither old rules nor other new rules. This constructs a directed full geodesic from every extended root with old projection in A_0(Q5). Hence the displayed fiber formula holds.

For strong connectivity, fix any assignment of new bits. The induced old five-cube has the seed strongly connected orientation. For any new dimension j, a directed edge from its zero side to its one side exists at old states with x_0=0, whereas one from its one side to its zero side exists at old states with x_0=1. The old strong connectivity allows either old state to be reached within every new-bit slice. Thus one can traverse every new-bit edge in either direction by suitable internal paths. The graph of new-bit assignments is a connected cube, so the entire orientation is strongly connected.

VERIFICATION. /mnt/data/nori_nearfull_scc_truth_table_verify.py checks all old edge identities, directed strong connectivity and full diagonal fibers for dimensions n=5,6,7,8. The all-dimensional result follows from the preceding proof. A complete mathematical exposition is in /mnt/data/nori_global_fiber_overlap_and_nearfull_scc.md.

LIMITATION. These theorems establish connectivity of the entire supported diagonal-fiber overlap system, but demonstrate that such connectivity and near-total size of a strongly connected orientation's fiber do not themselves yield self-labeling. NORI1 remains open.
