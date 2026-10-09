# Bichromatic root diamonds and mixed terminal cap obstruction

# Bichromatic root diamonds and mixed terminal cap obstruction

Suppose a cube root lies on monochromatic four-edge geodesics of both colors. Their root-square certificates form an opposite-color diamond. At its boundary, the two ordered terminal windows can obstruct one another, and maximality of the monochromatic branches imposes strong local color equalities on mixed-class caps.

## Actual physical-face transposition blockers for opposite-color same-root reversed-tail diamonds

Let n>=5 and let c be ANY binary coloring of physical ordered 3-faces (antipodal oddness not needed). Suppose two GENUINE length-four MONOCHROMATIC geodesics begin at SAME ROOT x, end at SAME PHYSICAL ENDPOINT y, have four pairwise distinct used directions a,b,c,d and specifically direction orders
  P0=(c,a,b,d), color 0 in BOTH windows,
  P1=(a,c,d,b), color 1 in BOTH windows.
These are exactly the two-color diamonds constructed in NORI's item nori_bichromatic_hub_same_root_reverse_tail_opposite_color_diamond_20261008 at a bichromatic hub when opposite-color common-edge certificates are absent. The common midpoint hub is z=x xor {a,c}, and y=x xor {a,b,c,d}. The first TWO and last TWO directions are swapped between the two paths.

Fix ANY fresh unused coordinate e∉{a,b,c,d}.

**Theorem 1 (exact append blocker).** Appending e to P0 and P1 gives two ACTUAL length-five geodesics with window-color words respectively
  (0,0, A_e),  where A_e = c(F(y;{b,d,e}),(b,d,e)),
  (1,1, B_e),  where B_e = c(F(y;{b,d,e}),(d,b,e)).
Crucially, A_e and B_e refer to two ORDERS OF THE SAME PHYSICAL THREE-FACE through their COMMON endpoint y. If neither length-five extension is monochromatic, then
  (A_e,B_e)=(1,0).
If the two order colors are equal, at least ONE extension is monochromatic; if (A_e,B_e)=(0,1), BOTH are monochromatic.

**Theorem 2 (exact prepend blocker).** Prepending e to P0 and P1 gives two ACTUAL length-five geodesics with window-color words respectively
  (C_e,0,0), where C_e=c(F(x;{a,c,e}),(e,c,a)),
  (D_e,1,1), where D_e=c(F(x;{a,c,e}),(e,a,c)).
Again C_e,D_e are two ordered colors on the SAME PHYSICAL three-face, now through common root x. If neither prepended length-five path is monochromatic, then
  (C_e,D_e)=(1,0).
Equal order colors guarantee at least one monochromatic extension; (0,1) guarantees both.

**Proof.** For append, the only new color window consists of the last two directions of P0/P1 followed by e, respectively (b,d,e) and (d,b,e), whose physical free-face has common endpoint y. The first two window colors are 0,0 and1,1 by hypothesis. Appended path monochromatic iff A_e=0 for P0 and iff B_e=1 for P1; simultaneous failure iff (1,0). For prepend, the new window has e followed by first two directions of each path, respectively (e,c,a) and (e,a,c), and through same root x. Prepend P0 stays monochromatic iff C_e=0 and prepend P1 stays monochromatic iff D_e=1; simultaneous failure iff (1,0). QED.

**Corollary 3 (active NORI no-grand constraints in dimension n=6).** In Q_6 a length-five monochromatic directed geodesic can be extended via its only unused coordinate to a FULL one-switch antipodal geodesic, irrespective of the last window color. Hence if the ACTIVE grand conjecture hypothetically fails in Q_6 and a two-color four-edge diamond as above exists, for BOTH unused coordinates e,f it is NECESSARY that at the relevant physical faces:
  c(F(y;{b,d,e}),(b,d,e))=1,
  c(F(y;{b,d,e}),(d,b,e))=0,
  c(F(x;{a,c,e}),(e,c,a))=1,
  c(F(x;{a,c,e}),(e,a,c))=0,
and likewise substituting f for e. These are four precise ordered-face transposition defects per unused direction. They are compatible with the active antipodal reversal law locally; no false contradiction is claimed.

**Corollary 4 (higher-dimensional conditional extension).** If n>6 and an opposite-color rank-(n−2) geodesic diamond can be constructed with two distinct final ordered directions swapped between its colors, then an equal-color pair on EITHER shared physical extension face (root or endpoint) produces a MONOCHROMATIC (n−1)-edge path. Extending by the final unused direction gives grand closure. The theorem therefore identifies an exact physical three-face adjacent-transposition obstruction to lifting a color-flexible diamond across its remaining coordinates. A general existence theorem for such near-spanning diamonds is NOT known.

**Research strategy.** The present color-free reachability diamond provides same-root SAME-SUPPORT reversed tails. To upgrade it into a complementary-support grand witness, attempt a sequence of actual root/terminal-order exchanges that either (i) extends one of the mono colors by a fresh coordinate (eliminating a terminal tail), or (ii) accumulates transposition defects whose antipodal sign product around a closed compatible memory cycle is odd. The local blockers alone do not close grand NORI.

## A bichromatic hub forbids every monochromatic near-spanning core across each mixed omitted pair in a counterexample

Fix an active NORI ordered-three-face coloring of \(Q_n\), \(n\ge6\). Assume the **no-common-colored-certified-edge** alternative B of the square-edge-shadow dichotomy, so the connectedness theorem supplies a *bichromatic hub* \(z\) and two disjoint sets \(A,B\subset[n]\) of certified middle-edge directions of colors \(0,1\), respectively, \(|A|,|B|\ge2\), with at most one remaining isolated direction. The proved mixed-class selector rigidity says that every actual ordered face through \(z\) with middle free direction in \(A\) or \(B\), and one outer direction in the opposite class, has color equal to the middle-direction class.

**Theorem (all cross-pair codimension-two caps are uniform; immediate extension).** Choose **any** \(a\in A\), \(c\in B\) and write
\[
U=[n]\setminus\{a,c\},\qquad r=z|_U.
\]
For each \(i\in U\) and **every** cube vertex \(x_t\) whose \(U\)-coordinates equal \(r\) (the four choices of the omitted \(a,c\) bits), the genuine geometric cap labels obey
\[
\boxed{
c(F(x_t;\{a,c,i\}),(a,c,i))=1,\qquad
c(F(x_t;\{a,c,i\}),(c,a,i))=0.}
\tag{1}
\]
The values are independent of \(i\) and the two omitted-coordinate exterior assignments. Consequently **any monochromatic \((n-2)\)-edge geodesic** spanning all coordinates in \(U\), rooted at any \(x_t\) above projected root \(r\), forces a full NORI antipodal geodesic with at most one change.

**Proof.** Both cap faces in (1) have free coordinates \(\{a,c,i\}\), so varying the \(a,c\) bits of \(x_t\) leaves each physical face literally unchanged. At \(z\), the first ordered triple has middle direction \(c\in B\) and adjacent outer direction \(a\in A\), so its color is 1 by the mixed selector. The second has middle direction \(a\in A\) and adjacent outer direction \(c\in B\), so its color is 0. This proves (1).

Let \(P\) be any monochromatic \(U\)-spanning geodesic, with color \(q\), rooted at \(x_t\), first direction \(i\), last direction \(j\). If \(q=0\), **prepend** the omitted directions in order \((a,c)\) to \(P\), choosing the new root \(x_t\oplus e_a\oplus e_c\) so that the resulting path reaches \(x_t\) after the first two steps. Its first three window colors are \((1,s,0)\) for some \(s\in\{0,1\}\), and every later window is 0. The word changes color exactly once regardless of \(s\). If \(q=1\), instead **append** the omitted directions in order \((c,a)\) after \(P\). Its last three window colors are \((1,s,0)\), using the cap reversal-odd identity
\[
c(F(y_t;\{j,c,a\}),(j,c,a))
=1-c(F(x_t;\{a,c,j\}),(a,c,j))=0,
\]
where \(y_t=x_t\oplus\chi_U\) is the endpoint of \(P\) and the opposite physical face is used; all earlier windows are 1. Thus again exactly one change occurs. Both extensions use each coordinate exactly once. \(\square\)

**Corollary (uniform forbidden four-facet bundles under hypothetical grand failure).** If the grand conjecture fails and alternative B holds, then for **every** bichromatic hub \(z\) and **every** cross-class pair \(a\in A(z)\), \(c\in B(z)\), none of the four \(U\)-parallel facets based at projected root \(z|_U\) contains a monochromatic full \(U\)-geodesic **from its projected root**. Equivalently the four-facet monochromatic first–last memory graph \(\mathcal H_U(z|_U)\) is **empty**, not merely bipartite. In particular, there are at least \(|A||B|\ge2(n-3)\) distinct forbidden omitted-coordinate pairs (because \(|A|,|B|\ge2\) and \(|A|+|B|\ge n-1\), the product is at least \(2(n-3)\)) at each such hub.

This is a substantial strengthening of the generic four-facet cap-memory odd-cycle criterion: *every* near-spanning monochromatic core with a cross-class omitted pair is a grand-closure certificate, irrespective of its first and last directions or color.

**Exact open forcing implication.** The theorem does not supply a near-spanning monochromatic geodesic in any chosen facet; arbitrary ordered-face colorings can lack such paths at prescribed roots. A dimension-independent grand proof would follow if the physical-face incidences and antipodal symmetry guaranteed that at some bichromatic hub of alternative B, at least one of these \(4|A||B|\) root/facet cases has a monochromatic \(n-2\)-direction geodesic. The theorem isolates a concrete *global monochromatic-core transversal problem* in place of the broader one-change condition.

## Higher-index NORI forcing is an ANTIPODAL PATH of doubly certified physical edges, not merely one overlap edge

Let X be a finite regular CW (in particular simplicial/cubical) complex with a free cellular involution τ, and suppose X=A∪τ A, for subcomplex A; put C=A∩τA (automatically τ-invariant).

**GENERAL THEOREM (componentwise equivariant two-shore bridge).** If every CONNECTED COMPONENT of C is distinct from its τ-image, then there is a τ-equivariant continuous map X→S¹ (target antipodal). Consequently w_1(X/τ)²=0. Its contrapositive is
  w_1(X/τ)² !=0
    => SOME connected component of C is τ-INVARIANT.
This conclusion is strictly stronger than the preceding theorem nori_equivariant_two_shore_overlap_dimension_bounds_antipodal_index_20261008 when C contains many edges and cells yet its components all occur in antipodal pairs. No upper dimension bound on C is needed.

**Proof.** The finite complex C has finitely many connected components, each a closed and open subcomplex. By hypothesis τ pairs them with no fixed component. Choose one component from each τ-pair and assign constant value +1 to all its points; assign −1 on the image component. This is a continuous equivariant map g:C→S^0={−1,+1}. Embed S^0 as the two boundary endpoints of a closed upper semicircle H_+⊂S¹. Because H_+ is homeomorphic to an interval, the map g extends continuously from C to A with image in H_+ (either by barycentric interpolation on a triangulation of A or the elementary Tietze theorem for finite polyhedra). Write G:A→H_+ for this extension. On τA define F(x)=−G(τx), mapping to the opposite lower semicircle. On C the prescriptions agree: −G(τx)=−g(τx)=g(x)=G(x). The gluing lemma gives continuous F:X→S¹, satisfying F(τx)=−F(x). Pulling back the antipodal S¹ double cover implies w_1²=0 on X/τ. QED.

**NORI APPLICATION (actual two-color overlap geometry).** In an active NORI coloring n>=5, let X=X_c be the genuinely certified-center square complex, let A=X_0 be the subcomplex containing all physical cube vertices and all actually color-0-certified middle-pair squares and their boundary edges, and τA=X_1 be the corresponding color-1 complex. The overlap
  C=X_0∩X_1
contains ALL cube vertices; its one-skeleton consists EXACTLY of physical cube edges e for which K(e)={0,1}, i.e. edges lying in honest centered mono-four middle-pair squares of BOTH colors. A square of X is in C iff it has both color certificates; any such square has all boundary edges doubly certified. Therefore connectivity of C is equivalent to connectivity of this PHYSICAL BICHROMATIC COMMON-EDGE GRAPH H whose vertex set is all physical cube vertices and whose edge set is {e:K(e)={0,1}}.

**COROLLARY (higher index forces an antipodal chain of genuine color-flexible edges).**
If
   w_1(X_c/τ)^2 !=0,
then for some actual cube vertex z, there is a sequence
  z=z_0,z_1,...,z_m=bar z
of adjacent physical cube vertices such that EVERY physical edge {z_(j−1),z_j} is certified by a genuine monochromatic centered four-edge geodesic of color0 AND (possibly different) one of color1. As z and bar z differ in ALL n coordinates, necessarily m>=n. The chain can reuse coordinate directions; it is NOT automatically geodesic or witness-compatible.

**Proof.** The general theorem supplies a τ-invariant connected component C0 of C. Pick any physical vertex z in C0 (every nonempty subcomplex component contains vertices). Because τC0=C0, its antipode bar z also lies in C0. Connectivity of a finite CW complex implies connectivity of its 1-skeleton: cell attachments of dimension at least2 cannot connect distinct 1-skeleton components. Thus z and bar z are joined by a path in the 1-skeleton C0^(1), precisely the doubly-certified physical edges. Hamming distance between endpoints is n, so every such edge path has length >=n. QED.

**Position in the NORI program.** This isolates a very tangible topological-to-combinatorial task. A proof forcing w_1² nonzero would guarantee a FULL ANTIPODAL CHAIN of opposite-color certificates, not only a local bichromatic edge. To close the GRAND geodesic conjecture, one would still need a directional-no-repeat, ordered-terminal-memory coherent extraction from that chain (or find a different higher-index carrier if the actual X_c has index one, as the valid coordinate-only no-go example shows). No universal positive w_1² is claimed.

These diamonds provide many genuine short paths, but a monochromatic long core exists only when its terminal cap agrees with one of the diamond branches. The exact incompatibility conditions are preserved rather than silently filled by a color-only argument.
