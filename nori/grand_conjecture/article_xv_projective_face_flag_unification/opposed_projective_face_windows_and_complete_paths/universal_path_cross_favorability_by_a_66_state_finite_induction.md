# Universal path cross-favorability by a 66-state finite induction

### All-dimensional cross-favorability on a common interaction path

Let \(f,g\) be arbitrary binary colorings of the undirected edges of \(Q_n\), \(n\ge2\), whose combined direction-interaction graph lies inside the path \(0-1-\cdots-(n-1)\). Edge colors in direction \(i\) depend only on the bits of the adjacent path directions. The colorings may have unrelated nonlinear local truth tables.

**Theorem 1 (computer-certified path cross-favorability).** For every \(n\ge2\),
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{1}
\]
A common root and two full dimension-simple antipodal geodesics with respective words \(0^*1^*\) and \(1^*0^*\) can be reconstructed in \(O(n)\) time from the local truth tables. The universal existence assertion follows from a finite 66-mask induction certificate described below, verified independently in Python and C++.

**Orientation criterion.** Choose a common starting cube vertex \(x\), and independent orientations \(u_i,v_i\in\{0,1\}\) of the interaction edge \(i,i+1\) for the \(f\)- and \(g\)-orders: bit one means dimension \(i\) precedes \(i+1\). The traversed colors at an interior direction \(i\) are
\[
a_i=F_i(x_{i-1}\oplus u_{i-1},x_{i+1}\oplus(1-u_i)),\quad
b_i=G_i(x_{i-1}\oplus v_{i-1},x_{i+1}\oplus(1-v_i)),
\tag{2}
\]
with the absent argument omitted at endpoints. The required monotone paths exist for this root and these orientations if and only if, for each adjacency \(i,i+1\),
\[
u_i=1\Rightarrow a_i\le a_{i+1},\qquad
u_i=0\Rightarrow a_{i+1}\le a_i,
\]
\[
v_i=1\Rightarrow b_i\ge b_{i+1},\qquad
v_i=0\Rightarrow b_{i+1}\ge b_i.
\tag{3}
\]
Necessity follows from dimension precedence. Conversely every orientation of an undirected path is acyclic. Conditions (3) prohibit a precedence edge pointing from color one to zero in the \(f\)-order, or zero to one in the \(g\)-order. Topologically order the first color class and then the second in the appropriate orientation. The resulting total direction orders give full geodesics from \(x\) with precisely the locally computed edge colors (2), hence the desired monotone words.

**The 64-state transfer.** After processing directions \(i,i+1\), retain
\[
s_i=(x_i,x_{i+1},u_i,v_i,a_i,b_i)\in\{0,1\}^6.
\tag{4}
\]
There are 256 possible pairs of four-entry interior truth tables. For each such label \(\ell\), and each state \(s_i\), choose the three new bits \(x_{i+2},u_{i+1},v_{i+1}\), evaluate \(a_{i+1},b_{i+1}\) by (2), and retain the successor state precisely if (3) holds. This defines a 64-state nondeterministic transfer table. At the left endpoint, the 16 pairs of unary tables each yield a 16-element starting state set \(I_h\); at the right endpoint, each unary pair defines an acceptance mask \(E_t\) whose states pass the final comparison.

Encode a state by the integer
\[
x_i+2x_{i+1}+4u_i+8v_i+16a_i+32b_i.
\tag{5}
\]
Encode a two-input table with input index \(L+2R\), assigning the low four bits of an eight-bit transfer label to \(F_i\) and the high four to \(G_i\). For a subset mask \(M\), let \(T_\ell(M)\) be the union of its successors under label \(\ell\).

**Finite-state induction certificate.** There exists a family \(\mathcal B\) of 66 nonempty state-subset masks satisfying:
- Each of the 16 initial masks \(I_h\) contains a member of \(\mathcal B\).
- For each of 66 masks \(B\in\mathcal B\) and each of 256 interior labels \(\ell\), the mask \(T_\ell(B)\) contains some mask \(B'\in\mathcal B\).
- Each mask \(B\in\mathcal B\) intersects all 16 terminal acceptance masks \(E_t\).

Induction over the sequence of local truth tables therefore leaves a member of \(\mathcal B\) inside every reachable state set. Its intersection with the relevant right endpoint mask is nonempty, giving a common root and two valid orientation assignments. The orientation criterion proves (1).

**Reproducible finite verification.** Starting from the 16 endpoint masks, breadth-first closure under all 256 subset transitions has **3,191** distinct nonempty masks. All **816,896** state-set transitions were evaluated, and none of the 3,191 sets is disjoint from any of the 16 endpoint acceptance sets. Its inclusion-minimal antichain consists of **66** masks: 16 of size 16, 32 of size 28, and 18 of size 32. Checking the smaller inductive certificate requires **16,896** mask containment tests for transitions and **1,056** terminal nonempty-intersection tests; every test succeeds. Sorting the 66 masks numerically and writing each as sixteen lowercase hexadecimal characters followed by a newline gives SHA-256
\[
\texttt{3c0450114b54eb377ade6e7412b9b5bcd3bb8b8f999bb73b1eeaab59eefb7d4b}.
\tag{6}
\]
The finite certificate uses integer bit operations and no external solver. Independent Python and C++ subset implementations both found the same closure size. A separate root-and-path reconstruction checked 960 randomly generated instances in dimensions two through nine by reevaluating every edge color on both resulting full paths. Those additional tests are an audit, not the logical basis for the all-dimensional theorem.

**Corollary 2 (path forests).** If the union of the interaction graphs of \(f,g\) is a disjoint union of paths, then \(A_0(f)\cap A_1(g)\ne\varnothing\). Both favorable-root families factor as Cartesian products over independent components; apply Theorem 1 to each component.

**Corollary 3 (a jointly constant site closes arbitrary cyclic-local pairs).** Suppose \(f,g\) have cyclic-neighbor locality and some direction \(j\) has constant color in both colorings, \(f_j\equiv c\), \(g_j\equiv d\), with arbitrary \(c,d\in\{0,1\}\). Then \(A_0(f)\cap A_1(g)\ne\varnothing\). Fix the common initial \(j\)-bit \(t\), and remove direction \(j\), leaving a path-local pair on the remaining directions. In the \(f\)-order, traverse \(j\) first when \(c=0\), or last when \(c=1\). In the \(g\)-order, traverse \(j\) first when \(d=1\), or last when \(d=0\). The induced path colorings see a fixed \(j\)-bit equal to \(1-t\) or \(t\), independently for each ordering. Apply Theorem 1 to these two path colorings at a common lower-dimensional root, and reinsert \(j\) at the chosen extremes. Both full paths are monotone and start at the same root.

**Corollary 4 (unicyclic facets with a core-constant site).** Let a cube-edge coloring have a unicyclic undirected interaction graph, with arbitrary nonlinear pendant trees. If at one core direction \(j\) its edge-color function is independent of its two neighboring cycle bits (but may depend on its pendant-child bits), then the coloring has a paired root. The pendant-tree opposite-bit interface theorem yields two induced cycle-local colorings whose \(j\)-direction colors are constants, possibly different. Apply Corollary 3, then lift the two witnesses through the pendant trees. By the free-bridge correspondence, NORI1 holds for every antipodally odd next-dimensional extension of this facet class with unrestricted bridge colors.

**Algorithmic form.** Given the truth tables, propagate sets of at most 64 transfer states along the direction path, recording predecessors. Choose an accepted final state and backtrack the common starting bits and the two orientation strings. For each orientation, topologically sort its zero-color and one-color induced subgraphs in the required phase order. This constructs both full direction-simple paths in \(O(n)\) time and space.

**Proof-closure status.** This theorem resolves an all-dimensional **two-coloring** cross-root problem on interaction paths, eliminating the constant-site cyclic obstruction and supplying a gluing tool for subsequent separator inductions. Universal cross-favorability for arbitrary cycle-local pairs, and therefore unrestricted NORI1, remains open. A larger finite-state invariant or a handwritten classification of the remaining cyclic constraints is the next target.

### Unrestricted paired roots for all interaction graphs of degree at most two

**Corollary (unrestricted cyclic-local single-coloring closure).** Let an arbitrary binary edge coloring \(f\) of \(Q_n\) satisfy \(f_i(x)=F_i(x_{i-1},x_{i+1})\) at all directions, cyclic subscripts, without any further assumptions. Then
\[
\boxed{A_0(f)\cap A_1(f)\ne\varnothing.}
\tag{9}
\]

*Proof.* If each \(F_i\) is nonconstant, apply the nonlinear cyclic-local paired-root theorem established in the nonlinear-tree incidence and cycle-syndrome Subsection: either a monochromatic full geodesic exists or \(f\) belongs to the affine neighbor-parity exception family, also proved to have paired roots. If some \(F_j\) is constant, apply the path cross-favorability theorem above to the pair \((f,f)\) via Corollary 3, since both induced direction-\(j\) colors are constant. These cases exhaust all cyclic-local colorings. QED.

**Corollary (all degree-two interaction graphs).** Suppose the undirected direction-interaction graph of an arbitrary binary edge coloring of \(Q_d\) has maximum degree at most two. Then \(P(f)\ne\varnothing\). Every connected component is a path, a cycle, or a singleton. Paths have paired roots by the previously established nonlinear tree theorem, cycles by the preceding corollary, and singletons trivially. Cartesian factorization multiplies the paired-root sets of these independent factors. No affine or antipodal hypothesis is used.

**NORI1 consequence.** Every antipodally odd edge coloring of \(Q_{d+1}\) whose chosen lower \(Q_d\) facet has direction-interaction graph of maximum degree two admits a monochromatic full dimension-simple antipodal geodesic, with no further restriction on the odd vertical bridge colors.

**Remaining distinction.** Pure cycle-local paired-root existence is now established. Pendant-tree elimination on a unicyclic interaction graph generally creates two *different* conditional cycle colorings. Each is individually paired-root favorable, but their opposite-orientation feasible-root sets need not intersect merely from that fact. Universal cross-favorability for two arbitrary cycle-local colorings remains open, and is the remaining obstacle to unicyclic closure with unrestricted nonlinear pendant branches.

### Explicit 66-mask certificate

The finite induction basis from Theorem 1 consists of the following 66 unsigned 64-bit masks, in ascending numeric order, encoded as hexadecimal. Bit `s` indicates presence of the six-bit state of integer index `s` as defined in (5). Grouping into four entries per line is for legibility; the checksum in (6) uses one entry per line.

~~~text
000000000000ffff 000000003c3cc3c3 00000000c3c33c3c 00000000ffff0000
000033cc0000cc33 0000cc33000033cc 0000ffff00000000 0140314cc143fd7f
0280328cc283febf 03c0300cc0030c30 0410c413341cf7df 0820c823382cfbef
0c30c003300c03c0 100413c41c34dff7 11441144dd77dd77 13c41004dff71c34
1414d7d71414d7d7 1c34dff7100413c4 200823c82c38effb 22882288eebbeebb
23c82008effb2c38 2828ebeb2828ebeb 2c38effb200823c8 300c03c00c30c003
314c0140fd7fc143 328c0280febfc283 33cc0000cc330000 341cf7df0410c413
382cfbef0820c823 3c3cc3c300000000 40014c3143c17ffd 41417d7d41417d7d
43c17ffd40014c31 4411441177dd77dd 4c3140017ffd43c1 5555555555555555
77dd77dd44114411 7d7d41417d7d4141 7ffd43c14c314001 80028c3283c2bffe
8282bebe8282bebe 83c2bffe80028c32 88228822bbeebbee 8c328002bffe83c2
aaaaaaaaaaaaaaaa bbeebbee88228822 bebe8282bebe8282 bffe83c28c328002
c0030c3003c0300c c143fd7f0140314c c283febf0280328c c3c33c3c00000000
c4130410f7df341c c8230820fbef382c cc33000033cc0000 d7d71414d7d71414
dd77dd7711441144 dff71c3413c41004 ebeb2828ebeb2828 eebbeebb22882288
effb2c3823c82008 f7df341cc4130410 fbef382cc8230820 fd7fc143314c0140
febfc283328c0280 ffff000000000000
~~~

A standalone verifier need only (i) generate the sixteen left and right boundary masks and the 256-by-64 transition table according to equations (2)-(5); (ii) assert that every left boundary contains some listed mask; (iii) assert that every image of each listed mask under all 256 transition labels contains at least one listed mask; (iv) assert that every listed mask meets all sixteen right acceptance masks. These are finite bitset assertions and prove the unbounded-length theorem by induction. No enumeration of all colorings of an n-dimensional cube is required.


### Shared antipodally-even local functions close the cyclic two-coloring problem

Let \(f,g\) be arbitrary cyclic-neighbor colorings of the cube \(Q_n\), \(n\ge3\). Suppose a distinguished direction \(j\) has the same local function in the two colorings, \(f_j=g_j=H\), and
\[
\boxed{H(a,b)=H(1-a,1-b)\quad\text{for all }a,b\in\{0,1\}.}
\tag{10}
\]
The only such two-input Boolean functions are the two constants and the two neighbor-parity functions \(a\oplus b\) and \(1\oplus a\oplus b\).

**Theorem (shared-parity cyclic cross-favorability).** Under this assumption,
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{11}
\]
The two witness paths can be constructed in linear time using the finite-state path solver, and the reinsertion of \(j\) requires no search.

*Proof.* Delete direction \(j\), leaving a path on the other \(n-1\) directions. Fix the \(j\)-bit to one in \(f\), obtaining a path-local coloring \(f^{(1)}\), and fix it to zero in \(g\), obtaining a path-local coloring \(g^{(0)}\). By the universal path cross-favorability theorem, there exist a common starting bit assignment \(x\) on those \(n-1\) directions, a full nondecreasing path \(P_f\) from \(x\) in \(f^{(1)}\), and a full nonincreasing path \(P_g\) from \(x\) in \(g^{(0)}\).

Put \(p=H(x_{j-1},x_{j+1})\). By (10), this is also \(H(1-x_{j-1},1-x_{j+1})\), which is the color of direction \(j\) after all other directions have been traversed.

Choose the common full starting root to have \(j\)-bit \(p\). If \(p=0\), put \(j\) **first** in the \(f\)-path, giving the leading zero color, and **last** in the \(g\)-path, giving a trailing zero. The remaining \(f\)-steps then see bit \(j=1\), while the remaining \(g\)-steps see \(j=0\), matching the chosen path-fiber pair \(f^{(1)},g^{(0)}\). Thus the full words are \(0\,0^*1^*\) and \(1^*0^*\,0\).

If \(p=1\), instead put \(j\) **last** in the \(f\)-path and **first** in the \(g\)-path. The other \(f\)-steps again see \(j=1\), and the other \(g\)-steps again see \(j=0\). The color of \(j\) at either extreme is one, so the full words are \(0^*1^*\,1\) and \(1\,1^*0^*\). All directions occur once, and the full paths share their starting root. QED.

**Corollary (responsive or even-shared unicyclic closure).** Consider a coloring whose connected undirected interaction graph is unicyclic with arbitrary nonlinear pendant trees. If either (i) every cycle site has an antipodally responsive pendant interface as in the adaptive-polarization theorem, or (ii) some nonresponsive cycle site has a common induced two-input color function \(H\) invariant under complementing both cycle-neighbor bits, then the coloring has a paired root. The free-bridge equivalence proves NORI1 for antipodally odd extensions of these facets with unrestricted odd bridge colors.

*Proof.* Case (i) is the established adaptive-polarization theorem. In case (ii), choose complementary pendant polarizations at every cycle site. The induced cycle colorings share the function \(H\) at the nonresponsive site. The theorem supplies compatible core paths, and the opposite-bit subtree interface lifts them to full paths from one starting root. QED.

**Unresolved shared-site classes.** The remaining nonconstant shared local functions are the four projections/complements, and the eight unbalanced nonlinear two-input truth tables. The endpoint-extension proof above fails for these functions because their values can change when both neighbor bits are complemented; this is a limitation of the extreme-insertion construction, not a counterexample to cross-favorability.

**Audit.** A separate implementation used the path root solver on arbitrary random cyclic pairs with shared even functions \(H\in\{0,6,9,15\}\) in dimensions three through seven. It inserted direction \(j\) according to the observed value \(p\), then independently evaluated every edge color along both complete paths. All 360 tested instances satisfied the claimed opposite monotonicities.
### Two disjoint opposite-fiber lifts through a shared even site

Under the shared parity theorem hypotheses, remove the distinguished direction j and define
\[
R_{10}=A_0(f^{(1)})\cap A_1(g^{(0)}),\qquad
R_{01}=A_0(f^{(0)})\cap A_1(g^{(1)}).
\]
These are cross-favorable root sets of two pairs of path-local colorings.

**Theorem (additive multiplicity).** If \(f_j=g_j=H\) with \(H(a,b)=H(1-a,1-b)\), then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge |R_{10}|+|R_{01}|
\ge2\kappa_{\mathrm{path}}(n-1).}
\tag{12}
\]
Here \(\kappa_{\mathrm{path}}(m)\) is the minimum cross-orientation root intersection for arbitrary pairs of path-local colorings of \(Q_m\), positive in every dimension by the 66-state theorem.

*Proof.* The previous theorem injectively lifts each root \(x\in R_{10}\) to the full root whose deleted j-bit is \(H(x_{j-1},x_{j+1})\). Construct a second lift from \(R_{01}\) with deleted j-bit \(1-H(x_{j-1},x_{j+1})\). When \(H(x)=0\), place j first in the f-geodesic and last in the g-geodesic. Their remaining steps see the j-bit as 0 and 1, respectively, so they follow the selected \(f^{(0)},g^{(1)}\) paths; the inserted j-edge has color zero at both extremes. When \(H(x)=1\), place j last in f and first in g. Again the remaining steps see j-bits 0 and 1, while the inserted edge has color one at either extreme. Both full paths retain their required monotone words. The images of the two lifts are disjoint because for the same lower root x their initial j-bits are complementary. The stated count follows. QED.

**Finite values.** Independent complete enumeration gives \(\kappa_{\mathrm{path}}(2)=2,\ \kappa_{\mathrm{path}}(3)=4,\ \kappa_{\mathrm{path}}(4)=4,\ \kappa_{\mathrm{path}}(5)=6\), from 5, 17, 117 and 729 distinct favorable-root masks respectively. Therefore cyclic pairs with a shared even local function have at least 4, 8, 8, 12 common roots in dimensions 3, 4, 5, 6. The general theorem needs no finite census.

**Inductive implication.** The parity gluing lemma preserves two disjoint full-root families. For shared projections or unbalanced nonlinear functions, the extreme-insertion method is insufficient; an induction must allow the deleted direction to cross at an interior seam.

### Antipodal-input seam gluing beyond even local functions

Let \(f,g\) be arbitrary cyclic-neighbor colorings of \(Q_n\), \(n\ge3\), sharing one local edge-color function \(H\) at direction \(j\):
\[
f_j(a,b)=g_j(a,b)=H(a,b).
\]
Delete \(j\) to obtain four path-local fiber colorings \(f^{(0)},f^{(1)},g^{(0)},g^{(1)}\), and define
\[
R_{10}=A_0(f^{(1)})\cap A_1(g^{(0)}),\qquad
R_{01}=A_0(f^{(0)})\cap A_1(g^{(1)}).
\]
Both are nonempty by the universal path cross-favorability theorem. Define the **antipodal-input agreement set**
\[
E_H=\{x\in Q_{n-1}:H(x_{j-1},x_{j+1})=
H(1-x_{j-1},1-x_{j+1})\}.
\]

**Theorem (localized double-fiber lifting).**
\[
\boxed{
|A_0(f)\cap A_1(g)|
\ge |R_{10}\cap E_H|+|R_{01}\cap E_H|.
}
\tag{15}
\]

*Proof.* Fix \(x\in R_{10}\cap E_H\), and put \(b=H(x_{j-1},x_{j+1})\). The shared local function also has color \(b\) after both neighboring directions have toggled. Assign starting bit \(x_j=b\). If \(b=0\), insert \(j\) at the beginning of the nondecreasing \(f^{(1)}\)-path and the end of the nonincreasing \(g^{(0)}\)-path. If \(b=1\), insert \(j\) at the end of the \(f^{(1)}\)-path and the beginning of the \(g^{(0)}\)-path. These two full paths start at the same vertex and have the desired monotone color words.

For \(x\in R_{01}\cap E_H\), instead assign starting bit \(x_j=1-b\). When \(b=0\), insert \(j\) first in the \(f^{(0)}\)-path and last in the \(g^{(1)}\)-path. When \(b=1\), insert \(j\) last in \(f^{(0)}\) and first in \(g^{(1)}\). Again both words remain monotone and the starting root is common. Each lift is injective; at a given lower root the two lifts choose opposite starting bits for direction \(j\), so their images are disjoint. Counting gives (15). QED.

**Corollary (classification of the remaining shared-site obstruction).** The sixteen two-input functions \(H\) divide into three classes:

1. For the four complement-even functions \(H=0,6,9,15\), the set \(E_H\) is the entire lower cube; (15) recovers the full double-fiber theorem.
2. For the eight unbalanced nonlinear functions, \(E_H\) is one of the two parity classes \(x_{j-1}\oplus x_{j+1}=0\) or \(1\). Consequently cross-favorability follows if either \(R_{10}\) or \(R_{01}\) meets that parity class. **A hypothetical failure requires both cross-root sets to be confined to the opposite parity class.**
3. For the four projections/complements, \(H(a,b)\ne H(1-a,1-b)\) for every input, so \(E_H=\varnothing\). The extreme-insertion theorem supplies no witness and an interior crossing is indispensable for this method.

This separates the unresolved shared-site cycle problem into *parity-rigid path interfaces* for unbalanced nonlinear functions and *intrinsically interior crossing* for projections. It does not claim these obstructions can occur in a full counterexample.

**A finite rigidity example.** Take \(n=5,j=0\) and the outside local truth tables
\[
(F_1,F_2,F_3,F_4)=(12,10,12,10),\qquad
(G_1,G_2,G_3,G_4)=(12,5,3,10),
\]
using neighbor-input index left plus twice right. The two opposite-fiber path cross-root sets both consist of the four lower roots whose adjacent endpoint bits satisfy \(x_1=x_4=0\). Let \(H(a,b)=a\wedge b\), with truth table 8. Its agreement set is the opposite endpoint-parity class \(x_1\ne x_4\). Hence (15) gives the zero lower bound, and no witness is produced by that extreme-insertion construction. Nevertheless direct full-path enumeration finds eight common roots in the original five-cube. The example demonstrates that one must allow nonextreme insertion when the path interfaces are parity-rigid.

**Closure direction.** The next useful induction lemma is not universal endpoint-parity flexibility, which is false for arbitrary path-local pairs. It should say that **when both opposite-fiber cross-root sets are parity-rigid on the wrong side, the deleted shared direction can be inserted at an interior seam**. Proving this for unbalanced \(H\), together with a distinct projection-site exchange, would finish the shared-site cross-favorability theorem and thus every unicyclic interaction graph by adaptive pendant polarization.
### Majority partition theorem for shared cyclic sites

Let \(f^H,g^H\) be two arbitrary cyclic-neighbor colorings agreeing on one local two-input function \(H\), while all remaining local tables are fixed independently. The failed choices
\[
\mathcal F=\{H:A_0(f^H)\cap A_1(g^H)=\varnothing\}
\]
form a majority-closed subset of the sixteen four-bit Boolean tables by the previously established shared-site 2-CNF theorem. They exclude the four antipodally even tables \(0,6,9,15\) by the shared-parity gluing theorem.

**Theorem.** \(|\mathcal F|\le8\). More precisely, at least one member of each triple
\[
(1,2,12),\quad(3,4,14),\quad(5,8,11),\quad(7,10,13)
\]
is cross-favorable.

*Proof.* The twelve other tables form the four disjoint triples displayed above. Their coordinatewise three-element majorities are respectively \(0,6,9,15\). If all members of one triple failed, majority closure would make its even majority fail, contradicting shared-parity gluing. Thus each triple contributes at most two failures. QED.

The bound eight is optimal for an abstract majority-closed subset disjoint from the even tables: the solutions of \(h_{00}\ne h_{11}\) constitute eight assignments and obey both properties. This does not establish attainability by cyclic cube colorings.

**Polarization corollary.** If at one cycle direction the attached-tree choices realize all three shared tables from one of these triples, while leaving the other induced cycle rules fixed, choosing the appropriate attached-bit polarization guarantees a cross-favorable core pair. The existing opposite-bit tree interface then lifts the pair to a paired root of the original cube coloring. The shared-site conjecture for a *fixed arbitrary* \(H\) remains open.### Two symmetry prototypes for the shared-site closure problem

Suppose two arbitrary cyclic-neighbor cube-edge colorings \(f,g\) share one local two-input edge-color rule \(H\) at direction \(j\). The cross-root existence statement is unchanged if we simultaneously apply to both colorings any of the following: complement either neighboring input bit by a cube translation; exchange the two neighboring directions by reflecting the cycle; or complement both edge-color bits. For the last operation, \(A_0(1-f)\cap A_1(1-g)=A_1(f)\cap A_0(g)\), which is the antipodal translate of \(A_0(f)\cap A_1(g)\).

These symmetries partition the 16 Boolean functions of two inputs into four orbits, with truth-table code indexed by left-bit plus twice right-bit:
\[
\begin{array}{c|c|c}
\text{type}&\text{codes}&\text{representative}\\
\hline
\text{constant}&0,15&0\\
\text{parity}&6,9&a\oplus b\\
\text{projection}&3,5,10,12&a\\
\text{unbalanced}&1,2,4,7,8,11,13,14&a\land b.
\end{array}
\tag{17}
\]

**Theorem (two-prototype sufficiency).** To prove cross-favorability for *every* pair of cycle-local colorings sharing one local function, it is sufficient to prove just the two cases
\[
\boxed{H(a,b)=a,\qquad H(a,b)=a\land b.}
\tag{18}
\]
The constant and parity cases were established by the shared-even-site theorem, and the listed symmetries carry all other local functions to the two representatives. Conversely the unrestricted shared-site claim includes both representatives. QED.

**Finite audit.** For \(Q_6\), exhaustive enumeration of the \(16^5=1,048,576\) choices of other local truth tables per fixed shared function, followed by deduplication of nondecreasing favorable-root masks and full pairwise comparison, gave:
\[
\begin{array}{c|r|r|r}
H&\text{distinct masks}&\min |A_0|&\min|A_0(f)\cap A_1(g)|\\
a&6539&27&7\\
a\land b&15859&36&12.
\end{array}
\tag{19}
\]
The census uses rooted subset dynamic programming with bit-parallel root masks, not SAT or integer optimization. These results verify the claim for this finite dimension only. The unbounded shared-site assertion remains open.### Cyclic transfer using 64 boundary states and two monodromy bits

Let \(f_i(x)=F_i(x_{i-1},x_{i+1})\) and \(g_i(x)=G_i(x_{i-1},x_{i+1})\) be two arbitrary cyclic-neighbor cube-edge colorings, with \(n\ge3\). For a common starting root \(x\), let \(u_i\) and \(v_i\) be the orientations of cycle edge \(i,i+1\) induced by the first and second dimension orders; bit one means direction \(i\) precedes direction \(i+1\). Their traversed colors are
\[
c_i=F_i(x_{i-1}\oplus u_{i-1},x_{i+1}\oplus(1-u_i)),\quad
d_i=G_i(x_{i-1}\oplus v_{i-1},x_{i+1}\oplus(1-v_i)).
\tag{20}
\]
The monotone-word conditions on cycle adjacency \(i,i+1\) are
\[
u_i=1\Rightarrow c_i\le c_{i+1},\quad
u_i=0\Rightarrow c_{i+1}\le c_i,\quad
v_i=1\Rightarrow d_i\ge d_{i+1},\quad
v_i=0\Rightarrow d_{i+1}\ge d_i.
\tag{21}
\]

**Theorem (64-state cyclic monodromy criterion).** The common opposite-orientation root set \(A_0(f)\cap A_1(g)\) is nonempty if and only if there is a cyclic closed walk in the following 64-state transfer, with **both** orientation bits attaining zero and one during the walk.

At site \(i\) retain \(s_i=(x_i,x_{i+1},u_i,v_i,c_i,d_i)\in\{0,1\}^6\). Its transition from \(s_{i-1}\) to \(s_i\), labeled by \((F_i,G_i)\), chooses \(x_{i+1},u_i,v_i\), calculates the two colors in (20), and checks (21) for the preceding adjacency. The cyclic condition matches the state after \(n\) transitions to the starting state. Two additional flags record whether any \(u_i\) differs from its initial value and whether any \(v_i\) differs from its initial value; acceptance requires both flags set.

*Proof.* Two full direction orders from the same root give a closed walk satisfying these conditions. Conversely, the closed walk provides consistent starting bits and two orientations of the direction cycle. An oriented cycle is acyclic precisely when its edge-orientation bits are not all identical. Both flags set therefore guarantee acyclicity of the two precedence relations. The local inequalities (21) prevent precedence arrows pointing from the later monotone color phase into the earlier phase. Topologically sort the first color class and then the second for each path, respecting the corresponding precedence edges. This gives two full dimension-simple geodesics from the same root, with nondecreasing f-word and nonincreasing g-word. QED.

**Algorithmic corollary.** The criterion gives an \(O(n)\)-time decision and witness-construction algorithm with fixed constants. Enumerate 64 initial states, propagate four 64-bit state masks tracking the change flags, then test cyclic return with both flags set. Store predecessors to recover the common root and two orientation vectors; topologically sort to obtain the complete paths. This reduces the earlier team's 512-state cyclic transfer to 64 boundary states plus two flags, and shares its state representation with the successful 66-mask path induction.

**Independent audit.** A C++ cyclic transfer implementation was compared with an unrelated bit-parallel rooted monotone-path dynamic program for 20,000 random cyclic-local pairs in each of dimensions 3,4,5 and 10,000 pairs in each of dimensions 6,7. All **80,000** decisions agreed. These tests check the implementation; the theorem follows from the transfer equivalence proof.

**Closure target.** Universal cyclic cross-favorability is equivalent to the assertion that every sequence of the 256 transfer labels has a closed walk satisfying both change flags. The statement remains open. An all-word fixed-point invariant extending the eight-prototype path induction would prove the cyclic cross-root theorem and, by pendant-tree elimination, close every unicyclic interaction coloring. A closed walk without the two flags is insufficient: it can represent a directed cycle in an attempted dimension order.### Rigidity at the eight-failure threshold

Fix two cycle-local colorings outside a shared direction, and let \(\mathcal F\subseteq\{0,\ldots,15\}\) be the truth-table codes of the shared local functions for which opposite-orientation cross-favorability fails. The preceding 2-CNF theorem makes \(\mathcal F\) closed under bitwise ternary majority, and the shared-even theorem excludes \(0,6,9,15\). The majority partition theorem shows \(|\mathcal F|\le8\).

**Theorem (classification of equality).** If \(|\mathcal F|=8\), then \(\mathcal F\) must be one of two eight-element sets:
\[
\boxed{
\mathcal F=\{H:h_{00}\ne h_{11}\}
\quad\text{or}\quad
\mathcal F=\{H:h_{01}\ne h_{10}\}.
}
\tag{22}
\]
Thus an eight-function failure set is determined by disagreement of one *antipodal pair* of input entries.

*Proof, with a 81-choice finite certificate.* Partition the twelve codes outside \(\{0,6,9,15\}\) into the four triples
\[
T_0=(1,2,12),\quad T_6=(3,4,14),\quad
T_9=(5,8,11),\quad T_{15}=(7,10,13).
\]
Their ternary bitwise majorities belong respectively to the four excluded codes. Since \(|\mathcal F|=8\), it contains two elements of each triple. There are only \(3^4=81\) possibilities, obtained by specifying one omitted entry in each triple. Check closure under majority for all unordered triples of distinct included codes; repeated-entry majority gives an already included code automatically. The following direct finite check describes the entire verification:
\[
\begin{array}{l}
\text{for }(q_0,q_6,q_9,q_{15})\in\{0,1,2\}^4:\\
\quad S=\bigcup_{t\in\{0,6,9,15\}}\bigl(T_t\setminus\{T_t[q_t]\}\bigr);\\
\quad\text{retain }S\text{ if }\ (a\&b)\,|\,(a\&c)\,|\,(b\&c)\in S\\
\qquad\text{for all distinct }a,b,c\in S .
\end{array}
\]
Only two subsets survive:
\[
\{1,3,5,7,8,10,12,14\},
\qquad
\{2,3,4,5,10,11,12,13\}.
\]
The first is \(h_{00}\ne h_{11}\), the second \(h_{01}\ne h_{10}\), proving (22). The verification has 81 candidate sets of size eight and at most 56 three-element checks per set; it requires no SAT or optimization algorithm. QED.

**Caution.** Both equality patterns are possible *abstractly* as 2-CNF solution families, since each is defined by the conjunction of the two clauses expressing unequal bits. This classification does not exhibit cycle-local colorings with eight failures. The finite six-dimensional census with a shared projection or conjunction found no failures for any of the sixteen common functions.

**Closure implication.** If a hypothetical shared-site obstruction fails for half the possible local functions, it must localize to a single antipodal input-pair disagreement. Excluding these two extreme patterns via a square-exchange or path-monodromy argument would improve the universal guaranteed-success count from eight to nine. To prove the full shared-site theorem, the remaining smaller majority-closed failure sets must ultimately also be ruled out.
