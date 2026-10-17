# Connected linear obstruction to reversal-aligned paired-root geodesics

- Stable ID: note_nori_linear_reverse_order_gluing_obstruction_r11435
- Author: unspecified; session provenance retained
- Primary home: subsection:dihedral_full_path_symmetry_and_the_root_gluing_obstruction
- Labels: NORI1, ordinary-facets, paired-root, reversal-order, Kendall-distance, dimension-uniform, negative-result, geodesic-exchange, connected-influence
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_4
- Updated session: session_nori_r11435_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Connected linear obstruction to near-reverse paired geodesics

**Status:** proved negative result about ordinary cube-edge colorings in the projective facet-bridge program; not a NORI1 counterexample.

An ordinary undirected cube-edge coloring consists of rules g_i(x+e_i)=g_i(x), with no required antipodal oddness. A rooted full geodesic is *rising* when its edge-color word is 0*1*, and *falling* for 1*0*. A root is *paired* if it supports a rising and a falling order. d_KT is Kendall inversion distance, or minimum adjacent swaps.

**Theorem.** For every k>=1 there is an ordinary coloring on Q_(3k+1) with nonconstant rules in every direction and a connected undirected influence graph, having a paired root but satisfying, for EVERY paired root x and EVERY rising/falling witness pair (pi,sigma):
 d_KT(sigma,rev(pi)) >= k.
Consequently a universal paired-root bridge cannot be obtained by insisting on bounded-distance reversal alignment of witness orders.

**Local obstruction.** On Q3 define g_0=x_2, g_1=1+x_2, g_2=x_0+x_1 (arithmetic mod 2). All rules are nonconstant, and the directed influence graph is strongly connected. At root 0, pi=(2,1,0) rises with word 001, and sigma=(1,0,2) falls with word 100.

No root admits a rising order pi for which rev(pi) is falling. To prove this, fix root x and order pi; let a_i be the color of direction-i's edge traversed in pi, and b_i the color of that edge's antipodal mate. At the SAME root, rev(pi) traverses precisely those antipodal mates in reverse direction order. Therefore both required monotonicities mean both a_(pi_1),...,a_(pi_3) and b_(pi_1),...,b_(pi_3) are nondecreasing. Our rules yield b_0=1-a_0, b_1=1-a_1, and b_2=a_2. If a_0 differs from a_1, the required relative positions of directions 0 and 1 for monotonicity in a and b are incompatible. Hence a_0=a_1=t. The first two rules differ by 1 and read only x_2; equality holds precisely when direction 2 lies strictly between directions 0 and 1 in pi. Monotonicity of a with equal endpoint values t then forces a_2=t; monotonicity of b with endpoints 1-t forces b_2=1-t. But b_2=a_2, contradiction.

**Connected amplification.** Partition the first 3k directions into blocks B_b=(3b,3b+1,3b+2), b=0,...,k-1, and define
 G_(3b)=x_(3b+2), G_(3b+1)=1+x_(3b+2), G_(3b+2)=x_(3b)+x_(3b+1) mod 2.
For the new hub direction h=3k put G_h=OR_{b<k} x_(3b).
Each rule ignores its own bit and is nonconstant. The hub reads one bit of each block; each block's undirected influence graph is connected, so the full graph is connected.

At the zero root, a rising order first uses h, then the pair (3b+2,3b+1) for each block, then direction 3b of each block; word 0^(2k+1)1^k. A falling order first uses direction 3b+1 of each block, then h, then (3b,3b+2) in each block; word 1^k0^(2k+1). The hub's value is zero at both crossings, because none of its input bits x_(3b) has flipped yet. Thus root zero is paired.

For an arbitrary paired root x and any rising pi, falling sigma, restrict both orders to directions of B_b. Block colors are independent of every direction outside that block, so the restrictions pi_b,sigma_b are rising/falling paths for the preceding Q3 gadget from the projected root. The local obstruction implies sigma_b != rev(pi_b), hence their Kendall distance is >=1. The discordant direction pairs within distinct blocks are disjoint and contribute separately to the full Kendall distance, giving
 d_KT(sigma,rev(pi)) >= sum_b d_KT(sigma_b,rev(pi_b)) >= k.
This proves the theorem for ALL roots and ALL witness pairs. QED.

**Verification and scope.** Q3 full enumeration gives paired rising and falling paths at all eight roots, with minimum reversal-alignment distance one. The stated paths in dimensions 4,7,10,13 were independently computed. A checker is preserved in the research session as reversal_alignment_obstruction.py, with expanded proof in reversal_alignment_linear_obstruction.md. The result excludes a tempting strengthened order-gluing step for arbitrary ordinary facets in Article XV. It does not exclude arbitrary-order paired roots, and the constructed colorings are not required to satisfy NORI1 antipodal oddness.
