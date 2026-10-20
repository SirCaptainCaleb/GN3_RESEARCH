# Whole-gate packet nonlocality and three-site forcing

- Stable ID: note_nori_q8_three_site_gate_implication_without_pair_packet_20261019_r11913
- Author: session_nori_r11913_1
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, whole-gate, two-sat, Q8, computer-assisted, method-obstruction
- Lifecycle: active
- Epistemic status: tested
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_1
- Updated session: session_nori_r11974_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Three-site implication forcing without a two-site packet in paired-flat Q8

Pair directions as (0,1),(2,3),(4,5),(6,7). Put p_i=x_(2i)+x_(2i+1) and q_i=x_(2i) over F2. A red pair-i step traverses direction 2i+f_i(p_-i,q_-i). Gates ignore their own pair and satisfy f_i(p_-i,q_-i+111)=1+f_i(p_-i,q_-i); these rules give legal antipodally odd undirected edge colorings.

Freeze f_1,f_2,f_3 and leave f_0 arbitrary. For each frozen gate, pack P in [0,7] from the three outside p-bits and Q in [0,7] from the three outside q-bits in increasing pair order. Define t=Q for Q<4 and t=Q xor 7 otherwise. Its value is bit_(4P+t)(M_i)+(Q>=4) modulo 2. Set
M_1=0x73336337, M_2=0x12df3f0f, M_3=0x55555555.
Denote the 32 independent bits of f_0 by h_(4P+t).

**Finite proposition.** For any legal completion of f_0, there exists a red full antipodal geodesic starting in pair-parity fiber p=0000. Yet the generated no-path 2-SAT formula has no unit clauses and no pair of independent h-entries whose four possible joint assignments are all forbidden directly by paths.

**Forcing proof.** The following roots and original-direction words have their six nonfree steps red under the three frozen gates. Each word uses each original direction once. Making all steps red would require the given two free-gate entries:
* root 0x00, order 17035642: (h_0,h_16)=(1,0);
* root 0x00, order 70342561: (h_0,h_16)=(0,0);
* root 0x03, order 51362407: (h_8,h_16)=(1,1);
* root 0x3f, order 60571243: (h_8,h_16)=(0,1).

If none of these paths is red, the first two exclusions imply h_16=1, while the last two imply h_16=0. Therefore one listed path is red for every completion.

**Computer-assisted exhaustive check of packet absence.** Enumerate all sixteen roots in p=0000 and all permutations of directions 0,...,7. Simulate each path from its root and retain it when its six nonfree steps are red. Translate its two visits to pair 0 into demands on h-entries. Discard paths whose two demands contradict at the same entry. Otherwise record the forbidden conjunction, collapsing repeated equal demands into a unit. The enumeration gives 3268 paths passing the frozen-gate test, 2516 consistent two-demand paths, 388 distinct forbidden conjunctions, zero units, and zero pairs of distinct entries carrying all four possible forbidden binary assignments. Independently, a constrained depth-first path enumerator yields the same total of 3268 paths and confirms the absence of units and complete two-entry packets.

This is an obstruction to a universal DIRECT two-entry four-clause certificate in the legal nonlinear paired-flat model at m=4. It does not challenge the general whole-gate implication graph or the open unrestricted NORI1 statement. The forcing cycle above visits three entries.


## Unbounded separation of complete whole-gate packets

**Theorem (all m>=3).** In Q_(2m), group directions as (0,1),(2,3),...,(2m-2,2m-1). Freeze f_j(x)=x_0 for j=1,...,m-1, and leave f_0 any legal antipodally odd selector independent of its own pair. Index its truth-table entries by complementary orbits [y]={y,bar y} of the d=2m-2 exterior bits. A *complete two-site packet* comprises four frozen-red-compatible full direction-simple words forbidding all assignments to two distinct gate entries. Every such packet joins [y] to [y+E], where E=sum_(j=1)^(m-1)e_(2j) is the sum of exterior even directions. Conversely, each such orbit pair supports a complete packet. Its folded-cube distance is m-1 (the diameter). No unit clause arises. There are 2^(2m-4) packet pairs before exclusions.

For every prescribed antipodally paired square orbit S in pair zero, exclude the full words using either of its pair-zero red edges. Precisely 2^(2m-4)-1 complete packets remain, all at folded distance m-1. Hence for EVERY legal nonlinear completion of the free selector f_0, some red full antipodal geodesic avoids S. This refutes universal complete-packet forcing at any fixed bounded site distance, even when root freedom, direction simplicity, and global square avoidance all hold.

**Proof.** Let O=sum_(j=1)^(m-1)e_(2j+1), so E+O=1 on the exterior cube, and E_0=E,E_1=O. At a root with x_0=beta, each frozen pair j offers only original direction 2j+beta before traversing direction 0, and only direction 2j+1-beta afterward. Thus any full frozen-red-compatible word puts all E_beta directions before 0 and all E_(1-beta) directions after 0. Direction 1 can appear on either side. Between the pair-zero appearances lie t<=m-1 exterior steps from one of these two sets. If t=0, the two pair-zero directions demand contradictory selector values at one exterior argument. Otherwise the two gate arguments have folded distance t.

When 1<=t<m-1, representatives of the two antipodal argument orbits realizing distance t are unique up to simultaneous complementation. Because original directions 0 and 1 demand opposite selector values, and complementation flips both demands, at most two of the four assignments to these two entries can be forbidden. For t=m-1 the intervening directions comprise E or O, so the sites are [y] and [y+E]=[y+O]. Therefore all complete packets use these sites.

Conversely, fix any exterior y and let X=f_0(y), Y=f_0(y+E). For beta=0,1 consider two full direction words, with arbitrary internal order in E_beta and E_(1-beta):
 A_beta: E_beta, 0, E_(1-beta), 1, rooted at exterior y+E_beta and x_0=beta;
 B_beta: 1, E_beta, 0, E_(1-beta), rooted at exterior y and x_0=beta.
Every frozen pair step is red. The free-pair steps require respectively (X,Y)=(0,0),(0,1),(1,0),(1,1) for A_0,A_1,B_0,B_1, using f_0(y+O)=1+Y. All words use every original direction once. Thus each matching pair of sites supplies four contradictory demands and forces a red geodesic for any free-gate completion.

Translation by E is a fixed-point-free involution on the 2^(d-1) exterior antipodal orbits, hence there are 2^(d-2)=2^(2m-4) packet pairs. Omitting one site eliminates its one matching pair, leaving 2^(2m-4)-1>0 packets. Those paths avoid both switched squares because their two pair-zero steps visit neither forbidden exterior orbit. QED.

**Independent checks.** Full direction-word enumeration for m=4 yields 15 surviving packets after excluding one orbit, and a distinct constrained enumerator for m=5 yields 63. All occur at distances three and four, respectively; none occur at smaller distances, and neither enumeration has unit clauses. The theorem is analytic and holds at arbitrary rank.

**Research consequence.** A complete two-site packet cannot generally be produced by a bounded exterior move or solely from an extendable red (i,j,i) triple. This complements the preceding Q8 three-site contradiction. It leaves unbounded-distance packet generation and the unrestricted NORI1 critical-square implication open.
