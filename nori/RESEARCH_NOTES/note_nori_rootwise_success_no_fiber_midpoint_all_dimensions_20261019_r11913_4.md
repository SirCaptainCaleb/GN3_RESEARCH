# Rootwise full red geodesics with zero paired-midpoint collisions in prescribed fibers for every even dimension >=8

- Stable ID: note_nori_rootwise_success_no_fiber_midpoint_all_dimensions_20261019_r11913_4
- Author: session_nori_r11913_4
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, midpoint-collision, dimension-uniform, rootwise-success, method-obstruction, nonlinear-parity
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_4
- Updated session: session_nori_r11929_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvi_midpoint_tensor_product_and_scarcity_barrier_20261018_r11755
- note:note_dd297b14828b049d0221340b

## Research note

# Rootwise-successful paired-flat cubes without a prescribed parity-fiber midpoint collision

**Theorem.** For every integer m>=4 there exists a legal antipodally odd, vertex-balanced paired-flat coloring of Q_(2m) such that (i) every root starts a red full antipodal geodesic using each original direction once, yet (ii) in every pair-parity fiber whose first four parity bits are zero, no red half-sweep from a root meets a red half-sweep from its antipode when both half-sweeps use every pair label once.

This refutes the *fiberwise* two-order midpoint assertion, including with universal rootwise red-geodesic existence. It does not refute global two-order midpoint existence or unrestricted NORI1.

## Base coloring on Q8 and legality

Number the original directions 0,...,7, grouped in pairs (2i,2i+1), i=0,...,3. Set p_i=x_(2i)+x_(2i+1) and q_i=x_(2i), over F2. At each vertex the red direction in pair i is 2i+f_i(p,q). For j!=i, pack p_j and q_j in increasing pair-label order, least significant bit first, into three-bit integers P and Q. Put

M_0=0xffffc0f0, M_1=0x5a505f55, M_2=0xcccccc33, M_3=0x00005a55,

and define f_i(p,q)=bit_(4P+min(Q,7-Q))(M_i)+[Q>=4] (mod 2), where bit_k(M) is binary digit k of M, least significant first.

Every f_i ignores its own pair. Under q->q+1111, Q->7-Q and f_i changes by one. Therefore the coloring is undirected, antipodally odd, and balanced, with one red edge from each pair at every vertex. Each hexadecimal nibble of every M_i belongs to {0,F,A,5,C,3}: for a fixed p, f_i is a complementary q-bit, possibly complemented. The choice of reader and sign can depend on p.

## Checkable certificate: no collision in p=0000

Let F_pi(q) denote the q-part of the endpoint of the four red pair moves, in order pi in S4, beginning at (p,q)=(0000,q). Define S_y={q: F_pi(q)=y for some pi}, for y=0,...,15. Encode S_y as a 16-bit mask, with bit q indicating membership. The 16 masks, in increasing y order, are:

d174 fa80 471d af02
0177 8b2c 40dd e238
90b2 54d5 068e 1557
3d02 4d4d 7c80 7171

Each mask contains no two positions q and 15-q. Thus S_y and its image under q->15-q are disjoint for every y. No pi,rho,q satisfy F_pi(q)=F_rho(15-q); equivalently the pair-midpoint collision count W_(0000) is zero. The masks follow by enumerating the 24 permutations and applying the red pair move
(p,q)->(p+e_i, q+(1+f_i(p,q))e_i).

## Red full geodesics nevertheless exist from every root

From x=0, the eight original directions (0,2,1,7,5,3,6,4) give the all-red vertex sequence (0,1,5,7,135,167,175,239,255). Full-direction subset recursion verifies red full antipodal reachability from every one of the 256 roots. At a state (p,q,U), try each original direction d outside U for which f_(floor(d/2))(p,q)=d mod 2; update p by e_(floor(d/2)), update q by e_(floor(d/2)) precisely if d is even, and enlarge U by {d}. Accept when U comprises all eight original directions. Memoized evaluation over all 256 initial roots returns success in each case. This recursion counts only paths traversing distinct original directions. The half-sweep enumeration and full-direction recursion were implemented independently.

## Lift to arbitrary m>=4

For m>4 retain the four base gates, independent of all added pairs. For each new pair j>=4 define f_j(p,q)=q_0. This is a legal paired-flat coloring and retains antipodal oddness and balance.

Given a core red full geodesic from any specified root, the original direction 0 occurs once and changes q_0. Insert, before this step, one red direction from every new pair, and, after it, the other red direction from each new pair. All new gates depend only on q_0, all old gates ignore the added pairs, and q_0 changes between the two insertion groups. Hence every inserted edge is red, the extended path uses all 2m original directions once, and this construction works from every prescribed extended root.

If two extended red half-sweeps from antipodal roots with core parity 0000 had a common endpoint, deleting new-pair steps and projecting to the old four pairs would give two core red half-sweeps with matching endpoints from antipodal old roots. Each projected half uses every old pair once, contradicting the displayed sixteen-mask certificate. Therefore the parity-fiber obstruction holds for every m>=4.

## Product amplification: almost all parity fibers can fail midpoint forcing

**Corollary.** For every k>=1 there is a legal balanced paired-flat coloring of Q_(8k) in which every vertex starts a red full antipodal geodesic, whereas precisely 15^k of its 16^k pair-parity fibers admit a red two-order midpoint collision. Hence the proportion of midpoint-positive parity fibers is (15/16)^k, which tends to zero exponentially. For any even n>=8, a coloring exists with universal rooted red-geodesic success and midpoint-positive fiber proportion at most (15/16)^floor(n/8).

**Proof.** In the base Q8 coloring, direct enumeration gives W_p=0 precisely at p=0000; all other fifteen parity fibers have W_p>0. If legal paired-flat colorings c,d have m and l direction pairs, respectively, a red pair half-sweep in their disjoint Cartesian product restricts to one red half-sweep in each factor. Conversely, each pair of factor half-sweep orders has binom(m+l,m) interleavings. Thus for each initial pair-parity (p,r),

W_(p,r)(c square d) = binom(m+l,m)^2 W_p(c) W_r(d).

Consequently the set of midpoint-positive fibers in the product is the Cartesian product of those sets in the factors. The k-fold product of the base Q8 coloring has 15^k midpoint-positive fibers out of 16^k. Every prescribed root starts a red full antipodal geodesic by concatenating red full geodesics from the corresponding factor roots, each using its disjoint original direction set once.

For even n=8k+2r with 0<=r<4, append r direction pairs whose gates read q_0 of the core, leaving all core gates unchanged. The preceding rootwise-success lifting argument applies. Any red half-sweep collision in the extended coloring projects, after deleting the new-pair moves, to a red half-sweep collision in the core from the projected antipodal roots. Thus each midpoint-negative core parity remains midpoint-negative for all choices of the added pair parities, giving the asserted upper bound.

This excludes dimension-uniform positive-density or asymptotically full-fiber midpoint forcing, even when every original root has a red full antipodal geodesic. The global existence question remains open.

**Scope.** The zero-collision restriction concerns a specified initial parity fiber and the one-visit-per-pair half-sweep sector. The constructed colorings remain successful for full red antipodal geodesics. The result supplies no hypothetical strict critical square or counterexample to unrestricted NORI1. It rules out a fiberwise two-order midpoint forcing theorem even under universal rooted success.

## Complete-halfwalk strengthening of the Q8 obstruction

For the same four legal Q8 gates, let H_x be the set of vertices reached from x by four red steps, allowing repeated pairs, directions, and backtracking. An independent direct walk enumeration proves 24<=|H_x|<=62 for all 256 roots. Since every four-step endpoint belongs to one bipartition class containing 64 antipodal vertex pairs, the cardinality threshold |H_x|>64 would force a red eight-step antipodal walk, hence a red full geodesic. This forcing criterion is not attained at ANY root, although the coloring has a red full geodesic from every root. Moreover H_x has no complementary pair for x in {86,90,102,106,150,154}. Thus even complete halfwalks, rather than only one-visit-per-pair sweeps, do not yield a rootwise antipodal-collision property under universal rooted success. Independent verifier: nori_complete_midwalk_expansion_obstruction.py. This is a finite method obstruction; it establishes no analogous support bound in every dimension.
