# Folded-cube cut rigidity, primitive walks, and rooted cycle obstruction

- Stable ID: note_nori_folded_cube_transit_conservation_20261016_r10917
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, folded-cube, orientation, cycle-counting, transit, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 5
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_folded_cube_semieulerian_alternating_girth_equivalence_20261015

## Research note

Let d=2m+1>=3, let G_d=Q_d/<antipode> be the odd folded cube with N=2^(d-1) vertices, and orient every edge arbitrarily. For a simple shortest odd cycle C of length d, define t(C) as the number of its vertices with one cycle edge entering and one leaving (transit vertices). Since the cycle length is odd, t(C) is odd. Let N_j be the number of unoriented d-cycles with j transits, and let k(v)=outdeg(v).

**THEOREM (unrestricted shortest-odd-cycle transit conservation).**
Every orientation of G_d satisfies
sum_{C of length d} t(C)=(d-2)! sum_{v in V} k(v)(d-k(v)),
and
sum_C (m+1-t(C))=(d-2)! sum_{v in V}(k(v)-m)(k(v)-m-1) >=0.
The number of unoriented shortest odd cycles is N(d-1)!/2. In particular their average transit count is at most m+1, with equality if and only if every vertex has outdegree m or m+1. Thus every orientation contains a shortest odd cycle with at most m+1 transits; if m is odd, this improves to at most m because the transit number is odd.

*Proof.* In G_d, every d-cycle is a word containing all d binary-circuit generators once. At any vertex v, each unordered pair {i,j} of the d incident generator labels extends to (d-2)! distinct unoriented d-cycles through v, because the other d-2 labels can be arranged arbitrarily. A cycle transits v iff its two incident oriented edges point in opposite directions. There are k(v)(d-k(v)) such pairs. Summing vertex-cycle incidences proves the first formula. Each unoriented cycle is counted in 2d rooted directed listings, so |C_d|=N d!/(2d)=N(d-1)!/2. Set d=2m+1 and subtract the first formula from (m+1)|C_d|; the displayed quadratic factorization follows. The factor (k-m)(k-m-1) is nonnegative for every integer k and vanishes only at k=m,m+1. QED.

**COROLLARY (directed pentagons and monochromatic Q5 geodesics).** For every orientation of G_5, let N_1 count almost-alternating pentagons (one transit) and N_5 count directed pentagons (five transits). Then
N_1-N_5=3 sum_v(k(v)-2)(k(v)-3) >=0.
Consequently every oriented directed pentagon forces an almost-alternating pentagon, without any degree hypothesis. In a near-balanced orientation, N_1=N_5; equivalently the number of rooted oriented red antipodal full geodesics in the corresponding legal Q5 coloring equals twice the number of directed pentagons in the folded quotient. In particular for near-balanced orientations, existence of an almost-alternating pentagon is equivalent to existence of a directed pentagon. The equivalence is a counting identity, not an independent proof of the unrestricted d=5 existence theorem.

*Proof.* An odd pentagon has transit count in {1,3,5}. The master identity with m=2 becomes 2(N_1-N_5)=6 sum_v(k(v)-2)(k(v)-3), proving the formula. The established folded-cube lift counts two rooted color-zero antipodal geodesics for each almost-alternating pentagon. QED.

**COROLLARY (seven-dimensional transit balance).** For every near-balanced orientation of G_7,
3N_1+N_3=N_5+3N_7.
More generally the master identity gives the complete orientation-dependent first moment of the shortest-cycle transit distribution in every odd dimension.

**Independent check.** For the legal near-balanced Q5 coloring obtained by adjoining c_4=x_0 to the vertex-balanced Q4 coloring c_0=x_1,c_1=x_0,c_2=1+x_1,c_3=1+x_0, enumeration of the 192 undirected pentagons gives (N_1,N_3,N_5)=(24,144,24) and mean transit 3. For the near-balanced Q7 coloring c_0=x_2,c_1=1+x_2,c_2=x_4,c_3=1+x_4,c_4=x_0,c_5=1+x_0,c_6=x_0, enumeration of the 23040 undirected shortest odd cycles gives (N_1,N_3,N_5,N_7)=(592,11024,10736,688), confirming mean transit 4 and 3*592+11024=10736+3*688.

**Research limitation.** If NORI1 were false, the corresponding near-balanced orientation would have N_1=0, which is consistent with the first-moment identity in d>=7. For d=5 it would force every pentagon to have precisely three transit vertices, equivalent to exclusion of directed pentagons. Without additional square-coherence information, this conservation law does not force a one-transit cycle. General graph countermodels from the shift-matching program show why first-moment estimates should not be mistaken for an existence mechanism.

LOCAL SQUARE-DESCENT COUNTEREXAMPLE IN DIMENSION SEVEN (finite directly checkable).
Take the legal antipodally odd Q7 coloring
c_0=x_2, c_1=1+x_2, c_2=x_4, c_3=1+x_4, c_4=x_0, c_5=1+x_0, c_6=x_0.
The first six rules form three complementary pairs and every vertex has three old red edges; the last rule adds either zero or one red edge. Thus the folded quotient orientation is near-balanced. In the folded Cayley model use even root x=0 and cyclic generator order
p=(0,1,3,2,5,4,6).
This cycle has t(C)=3. Evaluate the six adjacent swaps of p, retaining x=0, and the seventh cyclic swap of the last and first generators, using root shifted across the first generator to keep the same cyclic cycle. The resulting t values, in order, are
(5,3,5,3,5,3,3).
In particular no one-square exchange of this cycle produces a one-transit cycle. A breadth-first search in the adjacent-transposition graph on the 5040 orders from root x=0 finds the nearest one-transit order at distance three, for example p'=(0,2,1,5,3,4,6); no order at distance zero, one or two has t=1. This calculation can be verified by evaluating the seven local Boolean rules after every generator move and counting, at each visited folded vertex, whether its two cycle edges have opposite orientation statuses.

The example refutes the assertion that every non-optimal three-transit shortest odd cycle in a legal near-balanced folded-cube orientation admits a strictly improving single-square exchange. The global moment identity does not supply a local descent to a one-transit cycle. This is not a NORI1 counterexample: the coloring admits one-transit cycles, just not adjacent to the displayed cycle.


## Cubical cut forcing, directed-square surplus, and primitive quotient dynamics

Let d=2m+1>=3, N=2^(d-1), and orient the folded cube G_d so that every vertex has outdegree m or m+1, equivalently signed imbalance b(v)=outdeg(v)-indeg(v) in {-1,+1}. Let D be the directed adjacency matrix.

**Theorem 3 (maximum possible arc-strong connectivity).** Every nontrivial proper set U of quotient vertices has at least m arcs leaving U and at least m arcs entering U. Hence D is strongly connected and is m-arc-strong: for every ordered pair of vertices a,b there exist at least m arc-disjoint directed a-to-b paths. The bound is best possible, since half the vertices have outdegree m.

*Proof.* Identify G_d with the (d-1)-cube plus its antipodal matching. Its Fourier characters indexed by subsets of size k have adjacency eigenvalues
lambda_k=(d-1)-2k+(-1)^k.
The largest is lambda_0=d and the largest nontrivial one is d-4. For every subset W with s=|W|<=N/2, the standard spectral cut estimate therefore yields
|partial W| >= 4s(1-s/N) >= 2s.
A second estimate, valid for every simple d-regular graph, is
|partial W|>=s(d-s+1), since each vertex of W has at most s-1 neighbors in W.
Together they imply
|partial W|>=s+d-1.
Indeed for 1<=s<=d-1, s(d-s+1)-s=s(d-s)>=d-1. For s>=d-1, the spectral estimate gives |partial W|-s>=s>=d-1.
Choose the smaller side W of any nontrivial cut. Since |b(v)|=1, the difference between the number of outgoing and incoming arcs across this cut has absolute value at most s. Therefore each direction of crossing contains at least
(|partial W|-s)/2 >= (d-1)/2=m
arcs. The bound is sharp at the singleton cut of a vertex with outdegree m. Directed Menger's theorem gives the arc-disjoint path statement. QED.

**Theorem 4 (directed-square surplus identity).** Let Q_4 count the oriented four-cycles of G_d whose four edges form a consistently directed cycle. Let Q_0 count the four-cycles with two opposite source vertices and two opposite sink vertices (no transit corners). Then
Q_4-Q_0=N m/4,
so Q_4>=Nm/4=2^(2m-2)m.
This holds in every near-balanced orientation with no extra hypotheses.

*Proof.* In G_d every two-edge wedge with distinct incident directions lies in one four-cycle, determined by the sum of its two generators. There are S=N*binom(d,2)/4 distinct four-cycles. A four-cycle has zero, two, or four transit corners; four transit corners is equivalent to consistent cyclic orientation. Let Q_2 count the intermediate type. Each vertex v has outdegree k(v) in {m,m+1}; the number of transit wedges at v is k(v)(d-k(v))=m(m+1). Therefore
2Q_2+4Q_4=N m(m+1),
while Q_0+Q_2+Q_4=S=N m(2m+1)/4.
Subtracting twice the second equation from the first gives
2(Q_4-Q_0)=N m/2,
hence Q_4-Q_0=Nm/4. QED.

The more general version for arbitrary orientations is
Q_4-Q_0=Nm/4-(1/2)sum_v(k(v)-m)(k(v)-m-1);
thus near balance is the sharp equality case for the surplus.

**Theorem 5 (primitivity of every near-balanced folded orientation).** The matrix D is primitive: for all sufficiently large positive integers L, every entry of D^L is positive.

*Proof.* Theorem 3 makes D irreducible (the digraph is strongly connected). Theorem 4 gives a directed cycle of length four. The underlying G_d is nonbipartite because its d binary-circuit generators form an odd closed cycle; strong connectivity therefore forces some directed cycle of odd length. To see this last assertion, if all directed cycles were even, the parity of the length of a directed walk from a fixed root to any target would be well defined: two contrary parities could both be closed via a directed return path, yielding an odd directed closed walk. Assigning each vertex its well-defined walk parity would bipartition the underlying graph, contradiction. Since a strongly connected directed graph has cycle lengths with greatest common divisor dividing both four and an odd number, its period is one. Irreducibility and period one imply primitivity by the Perron-Frobenius theorem. QED.

**Graph-coloring interpretation and limits.** Every legal odd-dimensional NORI1 coloring whose quotient orientation is near balanced admits red-blue alternating cube walks corresponding to arbitrarily long directed walks in the folded quotient. In particular, any source-target quotient pair admits a directed walk of every sufficiently large length. This is a nontrivial uniform existence theorem but it does not force the shortest odd walk of length d, which is the NORI1 goal. The previously constructed shift-matching countermodels have no directed four-cycles, so they cannot satisfy the surplus identity even if strongly connected. More generally, an arbitrary strongly connected directed graph with a directed square and a directed odd cycle is primitive, but need not contain a one-transit shortest odd cycle. We do not claim to derive NORI1 from primitivity.


## Uniform quadratic diameter and positivity threshold

**Theorem.** For d=2m+1>=3, N=2^(d-1), and every near-balanced orientation D of folded G_d, the directed diameter Delta satisfies
Delta <=2(d+2)(d-1)ln 2+4.
For all integers L>=14Delta every entry of D^L is positive. In particular D^L is entrywise positive whenever L>=28(d+2)(d-1)ln2+56.

*Proof of diameter.* The established arc-cut bound and its proof show that every nonempty S with |S|<=N/2 has at least |S|/2 outgoing arcs. Each external vertex receives at most m+1 arcs, hence an outward BFS grows by a factor at least alpha=1+1/(2(m+1)) while below half the graph. The same bound holds for reversed BFS. After K=ceil(ln N/ln alpha)+1 steps, both BFS sets exceed N/2, so intersect, giving Delta<=2K. Since ln alpha>=1/(2m+3), we obtain Delta<=2(d+2)(d-1)ln2+4.

*Proof of power threshold.* By the directed-square surplus theorem there is a directed four-cycle. Strong connectivity plus nonbipartiteness implies an odd directed cycle. Moreover an odd directed cycle of length ell<=2Delta+1 exists: choose for each v a directed path P_v from a fixed root to v and path Q_v back, both length <=Delta. If every P_vQ_v and every P_u+(u->v)+Q_v had even length, parity of P_v would bipartition the underlying graph, contradiction. Thus one of these closed walks is odd; one of its constituent directed cycles is odd and no longer.

Take a vertex a on a directed four-cycle, a vertex b on the short odd cycle, and directed paths a->b, b->a of length <=Delta. Insert the odd cycle either zero or one times, selecting the odd resulting closed walk at a, of length H<=4Delta+1. There are closed directed walks of lengths 4 and H at a. Since H is odd, gcd(4,H)=1, and every integer at least 3(H-1) is a nonnegative combination of 4 and H. Given any u,v, fix directed paths u->a and a->v of total length <=2Delta. Every L>=14Delta leaves at least 12Delta>=3(H-1) steps to fill by those two closed walks. Hence (D^L)_(u,v)>0. QED.

**Alternating-color consequence.** Every near-balanced legal coloring of an odd-dimensional cube has a red-blue alternating antipodal cube walk of every sufficiently large odd length from every even root; antipodal translation gives the complementary blue-red assertion from every odd root. The quotient-directed walks lift to alternating cube walks because edge color reverses on the antipodal paired lift. Every closed subwalk in the bipartite cube has even length, so deleting closed subwalks preserves alternation and gives a simple alternating antipodal path of length O(d^2) from every root. These paths may repeat direction labels and are not asserted to be geodesics.

**Finite independent audit.** For the Q5 lift of balanced Q4 coloring (c0,c1,c2,c3)=(x1,x0,1+x1,1+x0) with c4=x0, the quotient orientation has diameter four and primitive exponent five. For the Q7 coloring (x2,1+x2,x4,1+x4,x0,1+x0,x0), the corresponding values are five and six. The universal quadratic bound is not claimed sharp.

**Boundary.** Positive powers of the ordinary directed adjacency matrix do not imply the folded common-out-neighbor trace positivity that characterizes a shortest one-transit odd cycle. This theorem supplies a guaranteed alternating path of quadratic length, not unrestricted NORI1.


## Failure of the rooted shortest directed circuit assertion at seven generators

**Computer-certified counterexample.** Let V=F_2^6 with generator list g=(1,2,4,8,16,32,63), with integers interpreted as six-bit vectors under XOR. This is the folded seven-cube, since sum(g_i)=0 and no proper nonempty subset of the seven generators sums to zero. Enumerate its 224 unoriented edges by increasing u=0,...,63, and at each u by generators g_0,...,g_6, retaining an edge (u,u xor g_i) only when u<u xor g_i. The following 56 hexadecimal digits encode 224 orientation bits in that enumeration order, most significant bit first; one means u->(u xor g_i), zero means the reverse:
863e4ccb9661d4ca4f661c66351f5ab5265b9aca29374d6d9aa85420

Direct finite verification gives all of the following:
(a) 32 vertices have outdegree three and 32 have outdegree four; thus the orientation is near balanced and corresponds to a legal antipodally odd Q7 coloring.
(b) No directed seven-cycle using every generator once passes through vertex zero.
(c) There are 6762 rooted directed shortest generator-rainbow seven-cycles in total, through other vertices.
(d) There are 72 consistently directed squares, compared with the universal lower bound 48.
(e) The directed diameter is six, and the adjacency matrix is primitive with its first entrywise-positive power at exponent eight.

**Independent small-state certificate for (b).** Define a Boolean recurrence on subsets S of the seven generators. Let z(S)=XOR_{i in S}g_i. Put R(empty)=true and
R(S)=OR_{i in S}(R(S without i) AND [z(S without i)->z(S) is an oriented edge]).
The counts of reachable subsets of sizes 0,1,2,3,4,5,6,7 are
(1,3,7,14,17,12,3,0).
There are 57 reachable subsets in total; the maximal reachable masks are
0x3f, 0x5f, 0x67, 0x79, 0x7e.
The full mask 0x7f is unreachable. As an independent checksum, the 128-bit mask with its S-th bit set precisely when R(S) is true is
570300a2fec2feffd78bd5a300020003.
The recurrence is only 128 states, and does not require enumerating 5040 generator permutations.

**Translation to the ordinary Q7 coloring.** Given even-parity x in F_2^7, let q be its first six bits and put y=q xor (63 if q has odd parity, else 0). For a direction i, define c_i(x)=0 if the folded edge y->(y xor g_i) is oriented outward, and c_i(x)=1 otherwise. On odd-parity x define c_i(x)=c_i(x xor e_i). This obeys undirected edge consistency and c_i(bar x)=1+c_i(x) mod2. At ordinary all-zero root there is no full red-blue-red-blue-red-blue-red antipodal geodesic, corresponding to statement (b). Nevertheless a red monochromatic full geodesic from that same root has direction order
(0,1,3,6,2,5,4).
The coloring has 2584 rooted ordered red monochromatic full geodesics in total. Thus this is a counterexample to the proposed rootwise alternating geodesic strengthening, NOT to NORI1.

**Interpretation.** Strong directed connectivity, aperiodicity, many directed squares, an O(d^2) diameter and a polynomial primitive exponent do not force a specified vertex to lie on a shortest directed odd circuit. A proof strategy that first seeks an alternating-color full geodesic from every prescribed root is disproved in dimension seven, even though the same legal coloring admits a monochromatic full geodesic at the failing root. The obstruction is about selecting each generator once, not ordinary directed reachability.
