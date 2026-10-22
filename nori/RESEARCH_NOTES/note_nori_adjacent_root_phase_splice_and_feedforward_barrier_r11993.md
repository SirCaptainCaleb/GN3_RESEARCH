# Adjacent-root phase splice and antipodally separated successful roots

- Stable ID: note_nori_adjacent_root_phase_splice_and_feedforward_barrier_r11993
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, critical-square, cross-root-splice
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11993_1
- Updated session: session_nori_r11993_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Adjacent-root phase splice and feed-forward root-connectivity obstruction (session session_nori_r11993_1).

SETTING. Work in a legal antipodally odd coloring of Q_n. Fix an antipodal pair S of alternating squares. Assume every red full antipodal geodesic meets S once, and no vertex of S is a successful red root. A live flag (x,v) means that a red full antipodal geodesic from root x traverses vertex v. Let phi_x(v) count whether its S-edge precedes v. This is well defined: two red prefixes from x to v use the same direction subset; attaching the same red suffix would contradict the common one-hit hypothesis if their crossing counts differed. Reversal gives phi_bar(x)(v)=1-phi_x(v).

PROVED ADJACENT-ROOT SPLICE. If x and y=x xor e_j are successful red roots and (x,v),(y,v) are live flags, then phi_x(v)=phi_y(v).

Proof. Take A=x xor v, B=y xor v and relabel roots so that j is absent from A; hence B=A union {j}. Concatenate a red prefix x->v using A with a red suffix v->bar(y) using the complement of B. This red path uses each direction other than j once. By antipodal oddness, precisely one of the edges x--y and bar(y)--bar(x) is red. If x--y is red, prepend y->x; otherwise append bar(y)->bar(x). This makes a red full antipodal geodesic, rooted at y or x respectively. Its extra connector is outside S because x,y are successful and no S vertex is a successful root. Its S-crossing count equals phi_x(v)+1-phi_y(v), which must equal one. Therefore the phases agree. QED.

For fixed v, let K_v be the set of red full-geodesic roots admitting a red path through v. The phase is constant along connected components of the root-cube induced graph Q_n[K_v], while antipodal reversal takes phi to 1-phi. Consequently the assumed strict one-hit and S-root-exclusion hypotheses prohibit any connected component of K_v containing two antipodal roots. This is a full-class conditional square-repair mechanism respecting root freedom, shared edges, arbitrary nonlinear gates and original-direction simplicity.

ANALYTIC SOURCE OBSTRUCTION, ALL m>=3. Partition the directions of Q_(2m) into pairs (0,1),(2,3),... . At each vertex let the red selected direction of pair i be 2i+f_i(x), with f_0=x_2, f_1=x_0, and f_j=x_0 for all j>=2. These selectors ignore their own pair and change under antipodal complementation, hence define legal vertex-balanced paired-flat colorings.

THEOREM. The successful red root set U is {x : x_0 xor x_2=1}. It is the disjoint union of two (2m-2)-dimensional subcubes distinguished by (x_0,x_2)=(0,1),(1,0); antipodality exchanges these components. Thus Q_(2m)[U] has no connected antipodal pair, and neither does any induced K_v.

Proof. Project a red full geodesic to the first four directions. Old gates are independent of later dimensions, so the projected path is a red full direction-simple Q4 geodesic for gates f_0=x_2,f_1=x_0. If (x_0,x_2)=(1,1), the initially red odd directions 1,3 do not change either selector, blocking use of directions 0,2. If (x_0,x_2)=(0,0), the necessary use of both original members of each pair requires 2 to occur strictly between 0 and 1 and 0 strictly between 2 and 3, an impossible temporal order. For (x_0,x_2)=(1,0), the Q4 red word (3,0,2,1) works; for (0,1), the Q4 red word (1,2,0,3) works, for arbitrary remaining core bits. In each successful core word the original direction 0 occurs once and changes x_0. For each added pair j>=2 insert its initially selected red direction 2j+x_0 before the step in direction 0, and its other direction 2j+1-x_0 afterward. Every added selector reads x_0 and old gates ignore the new bits, so all inserted edges are red and all original directions are used once. This extends a red full geodesic from every root in U. The projection argument excludes every other root. Antipodal separation follows because each edge within U changes only bits other than 0,2. QED.

This refutes the proposed unrestricted source lemma that a successful paired-flat coloring must contain a cube vertex v for which K_v has an antipodally connected component. It holds in all even dimensions >=6 and already has coupled feed-forward dependence, so independent-product structure is not required. The missing full-class proof step must exploit *global unavoidability of the same prescribed square*, not merely success, balanced gates, or density of successful roots. The examples remain successful and do not constitute a critical good-to-bad boundary or refute NORI1. An independent red subset-reachability check verified the stated successful-root criterion in Q6 and Q8.
 
## Cross-root two-direction curvature lemma and short witnessed repair

Continue under simultaneous strict square-critical assumptions: all red full geodesics meet one selected antipodal alternating-square support S once; no S vertex starts a red full antipodal geodesic. Let successful roots x,y both admit red full paths through a common vertex v. Put A=x xor v, B=y xor v, assume A strictly contained in B and B minus A equals {a,b}. Assume phi_x(v) != phi_y(v).

**Theorem (all-dimensional, nonlinear).** At the same root vertex y, binary colors c_d (zero=red) obey D_b c_a(y)=D_a c_b(y)=1+c_a(y)+c_b(y) modulo 2.

Proof. Since x,y are successful and no S vertex is a successful root, x,y lie outside S. Any length-two connector between x and y avoids S because its first and last edges each touch an endpoint outside S. The same holds between their antipodes. If one of these connectors were red, the support-preserving splice from the previous theorem would make a red full antipodal geodesic with S-hit number phi_x(v)+1-phi_y(v), either zero or two, contradicting the critical hypothesis. By antipodal oddness a red connector on the antipodal side corresponds to a blue two-step connector from y to x. Thus both two-step routes from y to x have mixed colors. Write u=c_a(y), w=c_b(y), alpha=D_b c_a(y), beta=D_a c_b(y). The two routes have color pairs (u,w+beta), (w,u+alpha). Their mixed-color conditions imply alpha=beta=1+u+w. QED.

If u=w, both derivatives equal 1 and the square has opposite-color endpoint stars. If u!=w, both derivatives equal 0 and its perimeter colors alternate. Both alternatives matter: alternating-square curvature alone omits the endpoint-star pattern.

**Constructive nonlinear Q6 example.** Use paired-flat gate masks (0xff00,0x60f9,0x32b3), S in pair 1 at exterior assignments 3,12. The red paths (root 29, directions 035214) and (root 9, directions 043521) both meet S once internally and pass through v=52. They have A={0,3,5}, B={0,2,3,4,5}, and crossing phases 0,1. At y=9, in directions a=2,b=4, the colors are c_2=0,c_4=1, while D_4 c_2=1 and D_2 c_4=0, violating the displayed critical relation. The antipodal connector 54->38->34 is red and has direction word 42. Splicing produces the red full path from 29 with word 035142 and vertex sequence 29,28,20,52,54,38,34, which avoids S. The repair uses two internal-one-hit witnesses as inputs, with no prior avoiding witness.

**Finite source obstruction and scope.** Replacing the third mask by 0x32b2 leaves an S-root-free orbit at the same exterior assignments, with 32 crossing red geodesics, but direct enumeration finds no opposite-phase comparable live root pair differing by two directions. Other red geodesics avoid S. Therefore root exclusion and the mere existence of internal-hit witnesses cannot furnish the hypothesized pair. The unresolved source theorem must additionally exploit GLOBAL unavoidability at this same S. The present all-dimensional derivative law may be combined with critical curvature at switched hits and integrability on overlapping cube faces. It does not itself settle NORI1.
