# Every NORI coloring has either a two-color common edge or an opposite-color same-root reversed-tail monochromatic diamond

# Bichromatic hubs force a same-root, same-endpoint, reversed-tail monochromatic diamond

Let \(n\ge6\), and let \(c\) be an active NORI coloring of actual ordered three-faces. Consider the no-common-certified-edge alternative B of Item \`nori_center_square_bichromatic_edge_or_antipodally_odd_edge_shadow_20261008\`. From the bichromatic-hub theorem, choose a cube vertex \(z\) supporting genuine centered monochromatic four-edge connectors of both colors. Let \(A=A(z)\) be the directions of its physical incident **certified** edges of color 0 and \(B=B(z)\) the certified directions of color 1. Under alternative B these sets are disjoint, both have size at least two, and at most one other direction is isolated. The preceding proved mixed-class rigidity, Item \`nori_bichromatic_hub_shadow_mixed_triple_middle_selector_rigidity_20261008\`, gives the **actual face-color identity**
\[
c(F_z(a,b,c),(a,b,c))
=
\begin{cases}
0,&b\in A,\\
1,&b\in B
\end{cases}
\tag{1}
\]
whenever the middle direction lies in a color class and at least one adjacent direction lies in the opposite class.

**Theorem (opposite-color, same-root two-tail diamond).** Choose any distinct \(a,b\in A\) and \(c,d\in B\). At the **same root**
\[
x=z\oplus e_a\oplus e_c
\tag{2}
\]
the following two *actual* length-four geodesics both end at
\[
y=x\oplus e_a\oplus e_b\oplus e_c\oplus e_d
 =z\oplus e_b\oplus e_d:
\tag{3}
\]
\[
\begin{array}{c|c|c|c}
\text{direction word}&\text{window 1}&\text{window 2}&\text{monochromatic color}\\
(c,a,b,d)&c(F_z(c,a,b),(c,a,b))=0&c(F_z(a,b,d),(a,b,d))=0&0\\
(a,c,d,b)&c(F_z(a,c,d),(a,c,d))=1&c(F_z(c,d,b),(c,d,b))=1&1.
\end{array}
\tag{4}
\]
The two paths traverse precisely the **same four directions** from the same starting vertex to the same endpoint, but their first two directions are swapped and their **last two directions are reversed**. Therefore the exact color-free reversed-tail root profile \(L_x\) contains *both*
\[
\boxed{
((b,d),\{a,c\})\in L_x,\qquad
((d,b),\{a,c\})\in L_x,
}
\tag{5}
\]
witnessed by genuinely monochromatic four-edge paths of **opposite colors**.

**Proof.** The path from \(x\) with order \((c,a,b,d)\) reaches \(z\) after its first two moves, because \(x\oplus e_c\oplus e_a=z\). Its two actual face windows thus coincide with those of the centered four-connector \(P_z(c,a,b,d)\). Formula (1) applies to both windows: their middle directions \(a,b\) are in \(A\), and respectively \(c,d\) are opposite-class neighbors. Their colors are 0. Similarly the order \((a,c,d,b)\) reaches the same center \(z\) after its first two moves, and both of its windows have middle directions \(c,d\in B\) with opposite neighbors \(a,b\in A\); their colors are 1. The shared starting point, endpoint and supports follow by commuting the four distinct Boolean coordinate flips. The ordered terminal pairs of the two paths are \((b,d)\) and \((d,b)\), and the outside supports are both \(\{a,c\}\); hence (5). \(\square\)

**Corollary (unconditional local topological extraction dichotomy).** Every active NORI coloring in dimension \(n\ge6\) has at least one of the following honest witness structures:

* **Shared-edge case:** a physical cube edge is contained in certified monochromatic middle-pair squares of both colors (alternative A of the edge-shadow theorem).
* **Same-root reversed-terminal case:** two monochromatic four-edge geodesics of opposite colors have identical endpoints and supports, with their ordered terminal pairs reversed as in (5).

Both alternatives represent actual **color-free physical path coincidences**, not numerical averages of labels. The second provides a literal edge (one-simplex) between the two terminal-memory labels within one root profile, with separate colors on its two witness paths.

**Exact limitation and extension target.** The grand theorem requires the **complementary** support \(D_J\setminus\{a,c\}\) for the *reversed* terminal pair, not the **same** support \(\{a,c\}\) certified in (5). For \(n\ge6\), equality of outside supports is not sufficient: one needs a root-preserving reachability operation that trades support on one side for its complement, or a fixed-point/Hex mechanism forcing a second intersection across the two oppositely ordered terminal basins. The diamond supplies a potentially useful *local terminal-order exchange operator*, but it is not itself a full one-change antipodal geodesic.

**Research priority.** Seek a certificate-preserving deformation or a carrier in which these reversed-tail diamonds allow one to switch between the two terminal memories **at fixed root and fixed physical endpoint**, while separately increasing the used-direction support. This links the bichromatic-hub topology to the already proved exact complementary-support extraction formulation, without claiming that local diamonds automatically concatenate.

## Elevation: an entire connected two-color rank-two root graph

The diamond is not isolated. Fix the same bichromatic hub \(z\) and the two certified direction classes \(A,B\), where \(p=|A|\ge2\), \(q=|B|\ge2\), and \(p+q\ge n-1\ge5\). Form the **rank-two root set**
\[
H_z=\{\,x_{a,c}=z\oplus e_a\oplus e_c:\ a\in A,\ c\in B\,\}.
\]
Identify it with \(A\times B\). Join \(x_{a,c}\) to \(x_{b,d}\) when \(a\ne b\) and \(c\ne d\). This graph is exactly the categorical/tensor product \(K_p\times K_q\). Every one of its edges admits **two distinct actual monochromatic four-edge geodesics of opposite colors**, with the same starting and ending vertices:
\[
(c,a,b,d)\ \text{of color }0,\qquad
(a,c,d,b)\ \text{of color }1,
\tag{6}
\]
or, for the opposite graph-edge orientation, the independently certified words obtained by swapping a with b and c with d (ordinary path reversal alone need not preserve ordered-face colors). Both have the same four-coordinate support \(\{a,b,c,d\}\) and both pass through the common physical center \(z\) after two moves. The original theorem proves their colors and terminal-order exchange; exchanging indices \(a,b\) or \(c,d\) does not affect the argument.

Since \(p,q\ge2\) and \(p+q\ge5\), at least one of \(p,q\) is at least 3. Therefore \(K_p\times K_q\) is **connected**, indeed of diameter at most 3: distinct indices in both coordinates are adjacent; two vertices sharing their \(B\)-index are joined by a two-step walk using a third distinct \(A\)-index when \(p\ge3\); two vertices sharing their \(A\)-index are joined by an odd walk of length 3 using two other \(A\)-indices when \(q=2\) and \(p\ge3\); when \(q\ge3\) the symmetric construction gives a two-step walk for the latter case. For \(p=2,q\ge3\), interchange \(A,B\).

Thus **at least \(pq\ge6\) distinct physical roots**, all lying at Hamming distance two from the same hub, form a connected graph in which *every graph edge has a real monochromatic geodesic witness of EACH color*. This gives a bounded-diameter **bidirectionally color-flexible rank-two reachability carrier**, significantly stronger than two isolated competing certificates.

The two colors on an edge are witnessed by different direction orders but the SAME geometric endpoints and support; they do not by themselves allow edge-path concatenation into one monochromatic **geodesic**, because successive rank-two root transitions may reuse directions. The grand proof obligation is to lift this connected two-color carrier to a certified higher-rank carrier while preserving no-repetition of coordinates and reversed terminal-memory compatibility.


## Elevation: a fully labeled commuting permutohedral 2-cell

The two monochromatic paths in (4) are the diagonal corners of a **complete square of commuting adjacent swaps**. With \(a,b\in A\) and \(c,d\in B\) distinct and the same root \(x=z\oplus e_a\oplus e_c\), examine all four direction orders obtained by freely swapping the first two and/or the last two directions:
\[
\begin{array}{c|c|c}
\text{ordered four-direction path from the common root }x&
\text{first actual window color}&\text{second actual window color}\\\hline
(c,a,b,d)&0&0\\
(a,c,b,d)&1&0\\
(c,a,d,b)&0&1\\
(a,c,d,b)&1&1.
\end{array}
\tag{7}
\]
**Every** row traverses precisely the same support \(\{a,b,c,d\}\), meets the same physical central vertex \(z\) after two steps, and ends at the same vertex \(y=z\oplus e_b\oplus e_d\). For the two mixed rows, the face-color identities from the mixed-middle selector theorem give respectively
\[
c(F_z(a,c,b),(a,c,b))=1,\quad
c(F_z(c,b,d),(c,b,d))=0
\]
and
\[
c(F_z(c,a,d),(c,a,d))=0,\quad
c(F_z(a,d,b),(a,d,b))=1.
\]
Consequently the four **actual geodesics** have the four different possible two-bit window-color words \(00,10,01,11\), with all changes at most one (since there are only two windows).

The first-two-position adjacent transposition toggles **only the first color bit**, the last-two-position adjacent transposition toggles **only the second color bit**, and the two transpositions commute. Thus the ordinary permutohedral square of four paths carries a **color-label isomorphism with the binary unit square**. The map from this local 2-cell to \(\{0,1\}^2\) satisfies exact one-bit adjacency and contains all four labels, precisely the local label completeness desired in a cubical-Sperner mechanism.

**Unconditional certified dichotomy, sharpened.** Every active NORI coloring in dimension \(n\ge6\) has either (A) a physical cube edge shared by monochromatic middle-square certificates of both colors, **or** (B) a **fully labeled commuting permutohedral square** of four actual same-root, same-endpoint geodesics with ordered-face color words \(00,10,01,11\).

**No premature extraction.** This full-label square has only **four edge directions and two ordered-face windows**; when \(n\ge6\) it is not a full antipodal path. The cubical-Sperner grand proof would require extending or assembling such square cells into a **dimension-\((n-2)\)** legally rooted/geodesic-labeled cubical carrier, with verified antipodal or boundary restrictions and an extraction of one full path of at most one change. In particular, attaching arbitrary prefix/suffix coordinate moves changes exterior face bits and may destroy the four labels. The result proves a genuine local cubical packet, not a global cubical grid.


## Elevation: a genuine dimension-independent defect-descent exchange

The four-corner label square (7) is stable in a stronger sense when appended to an **arbitrary common tail** of as-yet unused coordinate directions. Fix any permutation \(T\) of \([n]\setminus\{a,b,c,d\}\), and form full antipodal geodesics \(P_{00},P_{10},P_{01},P_{11}\) from the same root \(x\) by appending \(T\) to the four listed four-direction prefixes. They all reach the SAME cube vertex after their first four moves, so **every ordered-three-face window beginning at position \(5\) or later** is common to all four paths.

More precisely, switching only the **first two** directions changes only the **first** window color and leaves all remaining \(n-3\) window colors **exactly unchanged**:
\[
w(P_{00})=(0,0,\mathcal W_{bd}),\quad
w(P_{10})=(1,0,\mathcal W_{bd}),
\tag{8}
\]
\[
w(P_{01})=(0,1,\mathcal W_{db}),\quad
w(P_{11})=(1,1,\mathcal W_{db}),
\tag{9}
\]
where \(\mathcal W_{bd}\) and \(\mathcal W_{db}\) are the actual ordered-face color tails from window positions \(3,\ldots,n-2\), depending on the last-two direction order \((b,d)\) or \((d,b)\), respectively. The tails can be arbitrary and no exterior-bit independence beyond physical face locality is assumed.

**Proof of the one-bit invariance.** The two paths \(P_{00},P_{10}\) have the same root, traverse the same **set** \(\{a,c\}\) in their first two moves, and have **identical direction suffixes from position 3 onward**. Thus every window beginning at position 3 or later has exactly the same ordered free directions and the same physical exterior face bits in the two paths. Their second windows are different physical faces but both are color 0 by (7), while the first windows have colors 0 and 1. The other pair \(P_{01},P_{11}\) works identically with second-window color 1. \(\square\)

Let \(D(P)\) be the total number of adjacent ordered-three-face color changes along a full geodesic. Equations (8)-(9) imply the **strict descent identities**
\[
\boxed{D(P_{10})=D(P_{00})+1,\qquad
D(P_{01})=D(P_{11})+1.}
\tag{10}
\]
Consequently, **no globally minimum-defect full antipodal geodesic** (minimizing over all roots and all direction orders) can have either of the two mixed-prefix patterns \((a,c,b,d,T)\) or \((c,a,d,b,T)\) at one of the shadow-rigid bichromatic hubs, for *any* order \(T\) of the remaining directions.

This is an actual local-to-global strict defect-decreasing adjacent transposition, valid in every dimension \(n\ge6\). It is considerably stronger than the generic four-window locality bound, but applies only when the prefix is positioned at the certified two-class bichromatic hub with the specified mixed-coordinate order. The remaining grand-closure challenge is to prove that, under hypothetical failure, some minimum-defect full path **must** contain a repairable mixed-prefix configuration of this kind (possibly after an endpoint root slide or a certified involutive rotation). Neither (10) nor mere existence of a bichromatic hub ensures that encounter.
