# Cyclic bi-surjective overlap and terminal defect exchange

### A universal terminal-defect repair with one reversed local color pair

Let \(n\ge3\). Let \(f,g\) be arbitrary cyclic-neighbor edge colorings of \(Q_n\), with
\[
f_i(x)=F_i(x_{i-1},x_{i+1}),\quad
g_i(x)=G_i(x_{i-1},x_{i+1})
\tag{1}
\]
and cyclic indices. Write
\[
D_i=\{(a,b): F_i(a,b)=0,\ G_i(a,b)=1\},\quad
E_i=\{(a,b): F_i(a,b)=1,\ G_i(a,b)=0\}.
\tag{2}
\]
Call a binary relation \(R\subseteq\{0,1\}^2\) **bi-surjective** if both of its projections onto \(\{0,1\}\) are surjective. Equivalently it is a complementary-pair relation \(\{00,11\}\) or \(\{01,10\}\), or contains at least three pairs.

**Lemma 1 (complementary input flip).** If \(R\) is bi-surjective, complementing one argument gives another relation \(R'\) with
\[
\boxed{R\cup R'=\{0,1\}^2.}
\tag{3}
\]
A composition of bi-surjective relations is again bi-surjective. In particular, whenever \(P,S\) are bi-surjective,
\[
\boxed{(P\circ R\circ S)\ \cup\
(P\circ R'\circ S)
=P\circ\{0,1\}^2\circ S
=\{0,1\}^2.}
\tag{4}
\]
*Proof.* Fix the argument that is not complemented. Surjectivity onto this argument guarantees at least one value of the other argument is permitted. Flipping that other argument permits the remaining value as well, proving (3). For a composition, each input has some intermediate continuation and every output has some incoming intermediate predecessor; this proves both projections are surjective. A full relation composed on either side with a bi-surjective relation stays full, giving (4). QED.

**Theorem 2 (bi-surjective terminal-defect cross-favorability).** Suppose some direction \(j\) has \(E_j\ne\varnothing\), and for every other direction \(i\ne j\) the relation \(D_i\) is bi-surjective. Then the two colorings share a starting root and a **single** full dimension-simple antipodal geodesic with respective color words
\[
\boxed{
f(P)=0^{n-2}\,\alpha\,1,\qquad
g(P)=1^{n-2}\,\beta\,0
\quad\text{for some }\alpha,\beta\in\{0,1\}.}
\tag{5}
\]
In particular \(A_0(f)\cap A_1(g)\ne\varnothing\). This holds for every \(n\ge3\), without any affine or oddness assumptions and without requiring three permitted local pairs.

*Proof.* Choose a neighbor input in \(E_j\), which requires color pair \((1,0)\) at direction \(j\). Place \(j\) last in the full direction order and some other direction \(k\) penultimate. At every earlier direction require color pair \((0,1)\), by choosing its local neighbor input in \(D_i\). Direction \(k\) is left unrestricted. Any pair of bit colors \((\alpha,\beta)\) at \(k\) is between \((0,1)\) and \((1,0)\) under the order making the first component increase and the second decrease, so these requirements produce (5).

It remains to realize all local neighbor inputs along one direction order and one starting root. Fix a tentative direction order \(\pi\). Every \(D_i\) requirement for \(i\ne j,k\) becomes a bi-surjective relation \(R_i^\pi\) on the two starting bits \(x_{i-1},x_{i+1}\); complementing one or both arguments according to the earlier steps preserves bi-surjectivity. Since \(j\) is last, its prescribed neighbor input fixes the starting pair \((x_{j-1},x_{j+1})\). The graph of the relations \(R_i^\pi\) on the starting bits has one cycle when \(n\) is odd, or two parity cycles when \(n\) is even, prior to deleting the unconstrained relations at \(j,k\).

If \(n\) is odd, choose any \(k\ne j\) penultimate. Removing relations at \(j,k\) splits the single root-bit cycle into two paths, one containing each of the two fixed bits at the endpoints of the removed \(j\)-edge. Along either path, bi-surjectivity allows an assignment to be propagated from that fixed endpoint through every relation, regardless of whether its arguments are read forward or backward. The two assignments combine, giving the desired root.

If \(n\) is even, take \(k=j+1\pmod n\) penultimate, put \(a=j+2\) and \(b=j+3\), and put \(a,b\) consecutively somewhere before \(k,j\). Consider two orders \(\pi,\pi'\), identical except that \(a,b\) are swapped. The sites \(a,b\) are adjacent on the interaction cycle and have opposite parities. Consequently the swap changes the observed bit \(x_b\) in the local relation \(R_a\), while leaving every other relation in the parity component containing site \(j\) unchanged. Let \(R_a'\) denote the changed relation; it is obtained from \(R_a\) by complementing the argument associated with \(x_b\).

Removing site \(j\) from its parity component opens a path between the fixed starting bits \(x_{j-1},x_{j+1}\). For orders \(\pi,\pi'\), its endpoint feasibility relations can be written
\[
P\circ R_a\circ S,\qquad P\circ R_a'\circ S,
\tag{6}
\]
where \(P,S\) are compositions of other bi-surjective relations and are themselves bi-surjective (empty products are identities, also bi-surjective). By Lemma 1, the **union** of the two endpoint relations is full. Therefore the prescribed pair at \(j\) is feasible under at least one of the two orders. In the *other* parity component, removal of the penultimate site \(k\) also opens a path. Its relations are all bi-surjective and its starting bits are unprescribed, so it can always be solved. The two parity components involve disjoint starting bits and their assignments combine.

Thus in either parity of \(n\) there is a full direction order and a common root satisfying all the chosen local pair requirements. The first \(n-2\) direction steps have pair \((0,1)\), the penultimate step has arbitrary pair \((\alpha,\beta)\), and the last step has pair \((1,0)\). The color words (5) follow, and both are monotone. QED.

**Corollary 3 (locally sparse overlap is sufficient).** In every dimension, the theorem permits each nonexceptional \(D_i\) to have just two of the four local neighbor inputs, provided these are the complementary assignments \(00,11\) or \(01,10\). This improves the preceding three-of-four single-exception repair. If instead \(D_j\ne\varnothing\), the earlier all-sites-nonempty cyclic overlap theorem supplies cross-favorability. Thus when all other \(D_i\) are bi-surjective, either a nonempty \(D_j\) or a nonempty \(E_j\) guarantees the desired common root.

**Constructive certificate and audit.** For odd \(n\), one prescribed order and two binary path propagations suffice. For even \(n\), try the two orders related by the adjacent transposition \(a,b\) and propagate binary path constraints for each. This produces the root and both monotone color words in \(O(n)\) operations given local four-entry truth tables. The proposed two-order construction was independently evaluated on 1,500 random cyclic-local pairs in dimensions three through eight; each computed root and full order yielded the color words (5).

**Closure role.** When one conditional core-coloring site lacks a simultaneous opposite-color input but admits the reversed input, an arbitrary large cyclic consistency obstruction can be eliminated using **one unrestricted penultimate direction**. The even-dimensional step is a local adjacent exchange whose two possibilities cover every endpoint assignment. Remaining potential obstructions must involve multiple deficient sites, locally one-sided \(D_i\) relations (both permitted pairs in one row or column), or sites where the conditional local functions agree everywhere. These are narrower targets than unrestricted cyclic locality and retain dimension-simpleness throughout.

## One arbitrary deficient direction: sharpened terminal exchange theorem

For cyclic-neighbor cube colorings f,g, let \(D_i=\{(a,b):f_i(a,b)=0,\ g_i(a,b)=1\}\). Call a binary relation *bi-surjective* when each of its two projections onto \(\{0,1\}\) is surjective.

**Theorem (one arbitrary defect).** If every \(D_i\), except possibly \(D_j\), is bi-surjective, there is a full dimension-simple antipodal geodesic traversing direction j last whose first n−1 edges all have the joint color pair (f,g)=(0,1). Hence \(f(P)=0^{n-1}*\) and \(g(P)=1^{n-1}*\), so both have the requested monotonicity. Direction j has **no local restriction**: \(D_j,E_j\) may both be empty.

*Proof.* Fix a dimension order ending in j. Every requirement \(D_i\) for i≠j becomes a bi-surjective binary relation \(R_i\) between starting bits \(x_{i-1},x_{i+1}\); the chosen order complements zero, one, or both input bits but preserves bi-surjectivity. The starting-bit constraint graph connects indices at distance two on the cyclic direction graph.

For odd n this is one cycle, with the relation at j removed. The remaining path of bi-surjective relations is always satisfiable by propagating from one endpoint. Thus every order with j last works in odd dimension.

For even n there are two independent parity cycles. Removing R_j opens one into a path; the other remains a cycle and may have inconsistent parity in a fixed order. Choose cyclically adjacent directions \(a=j+2\) and \(b=j+3\), all subscripts modulo n. Put a,b consecutively before j, and compare the two total orders obtained by swapping a and b. On the intact parity cycle, the only altered relation is \(R_b\): its new version \(R_b'\) is obtained by flipping the input associated with starting bit \(x_a\). The other altered relation is R_a, which lies on the opened path and causes no obstruction.

For any bi-surjective relation R on two bits, R together with its one-input-flipped relation R' covers all four input pairs. Composition of bi-surjective relations preserves bi-surjectivity. If P and S compose the remaining relations in the intact parity cycle, then
\[
(P\circ R_b\circ S)\cup(P\circ R_b'\circ S)
=P\circ\mathbb F_2^2\circ S=\mathbb F_2^2.
\]
At least one ordering therefore yields a cyclic composition admitting an equal initial and terminal bit. That cycle has a satisfying assignment. The opened path has one independently, and the two parity classes are disjoint, so their assignments combine. Every earlier edge then has pair (0,1).

Because (0,1) is the minimum of the four joint color pairs under the order in which f increases and g decreases, the final edge can have any pair and the resulting whole path is monotone in both senses. QED.

**Audit of scope.** The preceding terminal-defect result required \(E_j\ne\varnothing\) and used a free penultimate step. Neither is necessary. The tempting stronger statement that every prescribed order ending at j works is **false for even n**: a cycle of disequality relations has no fixed point when their number is odd. The proof above uses one adjacent transposition to repair that obstruction. This theorem is dimension-independent. Remaining induction targets: two exceptional sites and local relations that are nonempty but one-sided rather than bi-surjective.

## Two exceptional sites: one arbitrary and one merely nonempty

Retain the cyclic-local colorings f,g, opposite-color success relations \(D_i=\{(a,b):f_i(a,b)=0,\ g_i(a,b)=1\}\), and the definition of bi-surjective binary relations.

**Theorem (two-defect terminal repair).** Fix distinct cyclic directions j and k. Suppose \(D_j\) is completely arbitrary, \(D_k\ne\varnothing\), and \(D_i\) is bi-surjective for every \(i\notin\{j,k\}\). Then there is a full antipodal dimension-simple geodesic with j last and the joint pair (f,g)=(0,1) on every earlier edge. Thus \(A_0(f)\cap A_1(g)\ne\varnothing\). This holds for every n≥3, allowing \(D_k\) to be a singleton and allowing \(D_j\) to be empty.

**Relation lemma.** Let R be any nonempty binary relation on \(\mathbb F_2\), and let R' be obtained by flipping one of its two input bits. The union \(R\cup R'\) contains a complete row or a complete column. Let P,S be bi-surjective relations, or empty compositions interpreted as identity relations. Then
\[
\boxed{(P\circ R\circ S)\cup(P\circ R'\circ S)}
\]
contains at least one diagonal pair.

*Proof.* Choose any (a,b) in R. Flipping the second argument puts both (a,0),(a,1) in the union; flipping the first argument puts both (0,b),(1,b) there. If a row is full, the surjectivity of the right projection of P provides an initial bit x linked by P to its row index; surjectivity of the right projection of S supplies a continuation to output x. If a column is full, choose any final bit y reachable from the column index through S; surjectivity of the left projection of P supplies a preceding path from y. Either case yields a diagonal pair. \(\square\)

*Proof of the theorem.* Fix a direction ordering with j last. Each local \(D_i\) for i≠j becomes a binary relation \(R_i\) on start bits \(x_{i-1},x_{i+1}\), transformed by possible input flips prescribed by the ordering. Bi-surjectivity and nonemptiness are invariant under these flips.

For odd n, removing R_j from the sole cyclic relation graph leaves a path with one nonempty relation R_k and every other relation bi-surjective. Such a path is satisfiable: choose any pair in R_k, then propagate backward and forward through the bi-surjective relations. Hence any order with j last works.

For even n, the relation graph has two disjoint parity cycles; removing R_j opens one into a path, while the other remains a cycle.

If k lies in the opened path, that path is satisfiable by the preceding propagation argument. The intact cycle has all relations bi-surjective. Choose adjacent cyclic directions a=j+2 and b=j+3 and place them consecutively before j. Exchanging a,b flips one argument of the intact relation R_b (b has parity opposite j), while changing only R_a in the opened path. By the full-union property of a bi-surjective relation, one of the two orders admits a satisfying cyclic assignment. The opened path is satisfiable for either order independently.

If k lies in the intact cycle, the opened path consists solely of bi-surjective relations and is satisfiable. Choose one of the two neighbors a of k on the direction cycle with a≠j (possible for n≥4). Put k,a consecutively before j and compare their two orders. The exchange flips one argument of R_k, changing only R_a in the opened path. Write the intact cycle's composite in the two orders as P∘R_k∘S and P∘R_k'∘S, where P,S compose the remaining bi-surjective relations. By the relation lemma, at least one composite has a diagonal pair; thus the intact cycle is satisfiable in at least one order. The opened path remains satisfiable.

In all cases, the two disjoint relation components supply a common starting root realizing (0,1) at every nonfinal direction. The final direction j can have any joint color pair and preserves the nondecreasing f-word and nonincreasing g-word. \(\square\)

**Inductive significance.** This settles one fully arbitrary deficient direction **and** one additional direction whose overlap may be singleton, with all remaining directions bi-surjective. The next induction frontier is to handle two or more additional one-sided relations on the same remaining relation path or cycle. The argument uses a single local adjacent transposition and a complete-row/column completion property; it is independent of dimension and avoids averaging or path-family enumeration.

For every n>=3, let j be a cyclic direction, a=j+1, b=j-1. Define two cyclic-local edge colorings by f_j=g_j=0, f_a=x_j, g_a=1+x_j, f_b=1+x_j, g_b=x_j, and for all other directions f_i=0, g_i=1. Then D_j is empty, D_a and D_b prescribe opposite initial j bits, and all other D_i are full. Every starting root is simultaneously favorable for the two separate orientations: if x_j=0, f admits order (j,b,others,a) with word 0^(n-1)1, while g admits order (others,a,b,j) with word 1^(n-2)00; if x_j=1, interchange a and b. But there is NO single order that works for both. Its joint pair in direction j is always (0,0), between (0,1) and (1,0) in the order where f increases and g decreases. The a,b pairs before j are (0,1) and (1,0); crossing j interchanges them. Therefore any order has either a maximal (1,0) before j or a minimal (0,1) after j, which violates joint monotonicity. This proves that induction on deficient directions must preserve two potentially different orders from a common root, not require a common order. Valid in all dimensions and not a counterexample to cross-root existence.

### The two-defect theorem is a corollary of the earlier punctured-cycle endpoint criterion

The terminal-direction lemma in the nonlinear tree-incidence subsection says that arbitrary nonempty success relations D_i at every i other than j can be realized by some dimension order ending in j if and only if the right-bit projection of D_(j-1) intersects the left-bit projection of D_(j+1). Both neighbors read the unchanged starting bit x_j, proving necessity. The path of remaining incidence equations admits a topological order and root whenever that one endpoint condition holds, proving sufficiency.

This criterion already implies the one-arbitrary-defect and two-defect theorems of this subsection: if the other success relations are all bi-surjective then both boundary projections are full; if only one additional D_k is nonempty and all the rest bi-surjective, at most one boundary projection can be proper, so the projections intersect. The longer adjacent-exchange arguments give alternate constructions, but no new hypothesis is needed for these corollaries.

The unresolved induction case starts where both neighbors of j require opposite values of starting bit x_j. The separate-orders gadget of this subsection shows that such a mismatch can obstruct a common monotone dimension order while still permitting two favorable orders from every root. Thus a further induction must retain two witness orders from one root, rather than a single shared order.

## Constant deficient direction: conditional induction from cyclic to path interaction

Let f,g be arbitrary binary edge colorings on Q_n whose direction-i edge colors depend only on the two cyclically adjacent direction bits. Fix direction j and assume its color is the SAME CONSTANT c∈{0,1} in both colorings:
\[
\boxed{f_j=g_j=c.}
\]
Delete j to form the path of the other n−1 directions. For b∈{0,1}, denote the induced path-local fiber colorings by \(f^{(b)},g^{(b)}\), obtained by fixing initial bit x_j=b.

**Proposition (opposite-fiber extreme insertion).** If c=0 and for some b
\[
\boxed{A_0(f^{(1-b)})\cap A_1(g^{(b)})\ne\varnothing,}
\]
then \(A_0(f)\cap A_1(g)\ne\varnothing\). If c=1, the analogous sufficient condition is
\[
\boxed{A_0(f^{(b)})\cap A_1(g^{(1-b)})\ne\varnothing.}
\]

*Proof.* In the first case choose a common lower-dimensional root z. Start both full paths at (z,b). For f, traverse direction j FIRST (color zero), then follow a favorable full f^(1-b) geodesic from z. Its whole word is \(0\,0^*1^*\). For g, first follow a favorable full g^b path from z, and traverse j LAST (color zero); its word is \(1^*0^*0\). In the second case c=1, traverse j LAST in the f path, and FIRST in the g path, using the respective indicated fiber colorings. The resulting words \(0^*1^*1\) and \(1\,1^*0^*\) are favorable. Every direction appears once. \(\square\)

**Conditional path-to-cycle closure.** If arbitrary pairs of binary colorings whose direction-interaction graphs are contained in a path always have \(A_0(u)\cap A_1(v)\ne\varnothing\), then *every* cyclic-local pair with a common constant direction satisfies the same cross-favorability. This implication has no local overlap or favorable-root density assumptions.

**Limit and inductive target.** The universal cross-intersection assertion for two unrelated path-local colorings is an additional theorem to establish; the known unconditional paired-root theorem for ONE tree-local coloring does not by itself imply it for a pair. The existing single-deficient-direction example with common constant j supports the proposed induction: each root has two favorable orders, one starting with j and the other ending with j. The general induction should preserve such two-path boundary information rather than demand one common full order.

### Acyclic opposite-fiber corollary. Suppose f_j=g_j=c is constant in two cyclic-local cube colorings, and denote their induced colorings on the remaining direction path by f^b,g^b for initial j bit b. If c=0 and for some b either f^(1-b) or g^b has acyclic directed dependencies, then A0(f) intersects A1(g). For c=1 use f^b and g^(1-b). Proof: an acyclic-dependency coloring has every root favorable, while every path-local coloring has at least one root favorable in each orientation by the established tree paired-root theorem. The two relevant favorable sets therefore intersect. Insert j at the start of the zero-color path and at the end of the opposite path when c=0, reversing the insertion roles when c=1. Corollary: a failed common-root instance with constant j requires each of its four relevant path fibers to contain a directed cycle; because the undirected interaction graph is a path, every such cycle is a mutual influence pair between neighboring directions. This reduces the remaining constant-site obstruction to configurations with bidirected path feedback in both opposite fibers.### One arbitrary exceptional site on a cyclic pair

Let \(F_i,G_i\) be arbitrary binary two-neighbor edge-color functions indexed cyclically on \(n\ge3\) cube directions. Define
\[
D_i=\{(a,b):F_i(a,b)=0,\ G_i(a,b)=1\}.
\]
Call \(D_i\) bi-surjective when each input projection takes both binary values; its smallest possible form is the pair \(00,11\) or \(01,10\).

**Theorem.** If all \(D_i\), apart from one \(D_j\), are bi-surjective, then at least two roots support a *common* full dimension-simple geodesic, with direction \(j\) last, whose two color words are
\[
\boxed{0^{n-1}\alpha,\qquad 1^{n-1}\beta},
\quad\alpha,\beta\in\{0,1\}.
\]
The two functions at the exceptional direction \(j\) are unrestricted. In particular cross-favorability holds even if neither opposite-color pair occurs there.

*Proof.* Fix a direction permutation ending with \(j\). For each \(i\ne j\), the condition that the two colors at the direction-\(i\) step equal \((0,1)\) becomes a relation \(R_i\) between the root bits \(x_{i-1},x_{i+1}\). Since the traversal order merely complements some arguments, every \(R_i\) is bi-surjective. The relation graph on root bits uses the pairs \(\{i-1,i+1\}\), with the \(j\)-relation absent.

For odd \(n\), this is a path on all starting-bit variables. Bi-surjectivity permits a chosen bit to be extended across each relation, in either direction. Both choices of an initial endpoint bit therefore produce solutions.

For even \(n\), the relation graph comprises an open path and a separate cycle on the other parity class. The open path always admits at least two solutions. On the closed component, bi-surjective relations are either equality/inequality bijections or contain at least three pairs. Composing such relations preserves bi-surjectivity, and a composition containing any three-pair relation retains at least three pairs, so it has a diagonal pair and satisfies the cycle. If instead every relation on the closed component is a bijection, consistency is the parity of its equality/inequality signs.

Take two consecutive direction steps \(i=j+1,t=j+2\) at the beginning of the traversal, with \(j\) still last. Swap these two steps to obtain a second order. Only the two corresponding local relations change, by complementing one argument in each. The relation at \(i\) lies on the closed parity cycle; that at \(t\) lies on the open path. The swap therefore toggles the consistency parity of the closed cycle while the open path remains satisfiable. One of the two orders yields a root meeting every nonexceptional relation. The open path contributes at least two different roots.

Every nonexceptional edge then has first color zero and second color one. The terminal direction \(j\) has arbitrary colors \((\alpha,\beta)\); both complete words remain monotone. This proves the result. QED.

**Construction and audit.** Given the local truth tables, try at most two dimension orders and solve the binary path/cycle relations by two-state propagation. This uses \(O(n)\) operations. Independent exhaustive checks of all bi-surjective relation systems at the nonexceptional sites for \(n=3,4,5,6,7\) covered respectively \(49,343,2401,16807,117649\) systems with no failures. The theorem itself is not limited to these dimensions.

**Closure implication.** A cyclic pair without a common opposite-orientation root must have at least **two** sites whose simultaneous \((0,1)\) input relations are not bi-surjective. This strengthens the earlier terminal-defect theorem by placing **no condition** on the exceptional pair of edge-color functions.## Absorbing independent sets of exceptional cycle directions

Let \(f,g\) be arbitrary binary cycle-local colorings of \(Q_n\), \(n\ge3\), and write
\[
D_i=\{(a,b):F_i(a,b)=0,\ G_i(a,b)=1\}.
\]
Let \(S\subseteq\mathbb Z_n\) be a nonempty **independent set of the cycle**, meaning no two members of \(S\) are adjacent. Assume \(D_i\) is bi-surjective for every \(i\notin S\), with no restrictions on any \(F_i,G_i\) at sites in \(S\).

**Theorem (separated-defect absorption).** Suppose either (a) \(n\) is odd, (b) \(n\) is even and \(S\) meets both parity classes, or (c) \(n\) is even and \(S\) is a proper subset of one parity class. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{|S|}.}
\tag{3}
\]
For each of these roots, the two paths can share a prefix consisting of **all** directions outside \(S\), with its colors identically zero under \(f\) and identically one under \(g\). They may then traverse the exceptional directions in **different orders**, ascending by \(f\)-color and descending by \(g\)-color.

*Proof.* Choose a permutation \(\pi\) of all nonexceptional directions and postpone every direction of \(S\). For \(i\notin S\), the requirement \((F_i,G_i)=(0,1)\) gives a bi-surjective binary relation \(R_i^\pi\) between the starting bits \(x_{i-1},x_{i+1}\), with its input bits complemented according to the preceding directions of \(\pi\). Its bi-surjectivity is preserved. Consider the root-bit relation graph with edge \(\{i-1,i+1\}\) for each \(i\notin S\).

When \(n\) is odd, these potential relation edges form one cycle before deletion. Removing the \(|S|\) exceptional relations splits it into \(|S|\) disjoint paths, isolated single-vertex paths allowed. Every bi-surjective relation allows either bit at a starting endpoint to be propagated to its neighbor. Each path therefore has at least two satisfying assignments, independently. Their Cartesian product contains at least \(2^{|S|}\) common starting roots, for any chosen prefix order.

When \(n\) is even, the relation graph starts as two separate parity cycles. In case (b), the exceptional sites remove at least one relation from each parity cycle. Both become unions of paths, whose total number of connected components is \(|S|\). The same argument supplies at least \(2^{|S|}\) roots.

In case (c), the exceptional sites remove relations from one parity cycle, leaving \(|S|\) independent paths; the other parity cycle remains closed. If its bi-surjective relations contain a three-pair or full relation, their cyclic composition also contains at least three pairs and hence has a diagonal entry, giving a cyclic solution. Otherwise every relation on the closed cycle is a two-pair equality/inequality bijection, and solvability is the parity of its signs.

Since \(S\) does not exhaust its parity class, choose a nonexceptional direction \(t\) with the same parity as \(S\), and an adjacent direction \(i\) of opposite parity (also nonexceptional). Make \(i,t\) consecutive at the beginning of the common prefix; compare their two possible orders, keeping all other precedences unchanged. Swapping \(i,t\) complements one argument in each of the two corresponding root-bit relations. The relation at \(i\) belongs to the intact closed parity cycle, so its bijection sign toggles. The relation at \(t\) lies in an already open path component and remains bi-surjective. Therefore one of the two prefix orders makes the closed cycle satisfiable. All \(|S|\) path components still contribute two choices each, proving the root lower bound in (3).

For any such root, traverse the common prefix \(\pi\). Every step outside \(S\) has color zero for \(f\) and one for \(g\). Since \(S\) is independent in the **direction interaction cycle**, the colors of the remaining exceptional directions depend only on their neighbors **outside** \(S\), whose bits have all been toggled during the prefix. Therefore those colors are unaffected by the relative order in which the directions of \(S\) are subsequently traversed. Sort the exceptional suffix ascending by its \(f\)-colors to obtain a full \(0^*1^*\) word; independently sort it descending by its \(g\)-colors to obtain a full \(1^*0^*\) word. Both full paths start at the same root and traverse every direction once. Distinct root-bit solutions remain distinct paired roots. QED.

**Algorithm and audits.** The proof gives an \(O(n)\) method: select one or two prefix orders, propagate the root-bit relations on their path components and test the one possible closed component, then sort the exceptional suffix in each of the two binary color orders. An independent C++ verification exhausted all \(7^{n-|S|}\) choices of bi-surjective nonexceptional local relations for the representative configurations
\[
(n,S)=(7,\{0,2,4\}),\ (8,\{0,2\}),\
(8,\{0,3\}),\ (8,\{0,2,4\}),
\]
with respectively \(2401,117649,117649,16807\) systems and **no failures**. Random full edge-color checks in dimensions five through nine also passed. The all-dimensional theorem follows from the preceding proof, not from the finite tests.

**Sharp boundary for this prefix strategy.** If \(n\) is even and \(S\) is an entire parity class, every nonexceptional direction belongs to the other parity class. The remaining root-bit relation graph is one unbroken cycle, and there is no adjacent pair of nonexceptional directions to perform the parity-flipping swap. This can cause the common-prefix requirements to fail: for \(n=4\), take \(S=\{0,2\}\), and set the two nonexceptional relations to \(D_1=\{00,11\}\), \(D_3=\{01,10\}\). Their demands on the same pair of root bits are contradictory. This does **not** show a failure of cross-favorability; it only excludes the shared-prefix construction.

**Closure significance.** The number of deficient sites is not by itself the obstruction. Any number of pairwise nonadjacent sites can be postponed and individually sorted, except for the saturated checkerboard case on an even cycle. Remaining cyclic cross-favorability failures, if any exist, must involve **adjacent** deficient sites or that saturated checkerboard configuration. This is an all-dimensional combinatorial reduction in the number and placement of local obstructions, preserving dimension-simple geodesics throughout.### Separated defects in unicyclic NORI1 facets

**Corollary.** Let a binary edge coloring of a cube have a unicyclic direction-interaction graph, with arbitrary nonlinear pendant trees. Choose complementary attached-bit assignments for the two cyclic core orientations by the universal subtree-interface theorem, and let \(g^0,g^1\) be the resulting pair of cycle-local colorings. Write
\[
D_i=\{(a,b):g_i^0(a,b)=0,\ g_i^1(a,b)=1\}.
\]
If the sites at which \(D_i\) is not bi-surjective form an independent set of the core cycle, other than a whole parity class of an even cycle, then the full coloring has a paired root. The conclusion also holds when every site is bi-surjective.

*Proof.* For an empty exceptional set, use the one-arbitrary-defect theorem by choosing any direction last. Otherwise apply the separated-defect theorem to \(g^0,g^1\), obtaining at least \(2^{|S|}\) shared cycle roots with opposite monotone geodesics. The earlier opposite-bit subtree-interface lemma reconstructs their full cube paths from common roots, keeping every direction simple. QED.

The universal free-bridge correspondence lifts this to NORI1 for any antipodally odd coloring of the next-dimensional cube whose chosen facet has this interaction structure, with arbitrary odd bridge bits.

**Remaining cyclic obstruction.** Any failure of cross-favorability between two cyclic-local colorings must have adjacent non-bi-surjective sites or, in even dimension, an entire parity class of such sites. The former requires a coupled multi-direction seam; the latter retains one closed parity relation cycle without an available adjacent-swap repair. The present results do not establish that either obstruction can cause a counterexample.### Checkerboard saturation: only a pure parity-frustrated cycle resists the prefix method

Let \(n=2m\ge4\), and suppose the exceptional set \(S\) is one entire parity class of the direction cycle. Thus \(S\) contains \(m\) mutually nonadjacent directions, and each direction \(i\notin S\) has a bi-surjective relation
\[
D_i=\{(a,b):F_i(a,b)=0,\ G_i(a,b)=1\}.
\]

**Theorem (checkerboard relation-cycle criterion).** If the cyclic composition of the \(m\) relations \(D_i\), \(i\notin S\), contains a diagonal binary pair, then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^m.}
\tag{4}
\]
If every such \(D_i\) is a two-pair equality/inequality relation and their cycle parity is consistent, then the stronger bound \(2^{m+1}\) holds. In particular (4) holds whenever **at least one** nonexceptional \(D_i\) contains three or four input pairs.

*Proof.* Traverse all nonexceptional directions first, in any order. They are mutually nonadjacent, so each sees the starting bits of its two neighboring exceptional directions, unaffected by the prefix traversal. Their requirement \((F_i,G_i)=(0,1)\) gives the unmodified relations \(D_i\) on the \(m\) starting bits indexed by \(S\); these relations form one cycle. The starting bits on the \(m\) nonexceptional directions are entirely free.

If the relation-cycle composition has a diagonal pair, it admits at least one satisfying assignment of the exceptional root bits. Combined with the \(2^m\) free nonexceptional bits, this gives at least \(2^m\) valid starting roots for a common prefix of colors \(0\) under \(f\) and \(1\) under \(g\).

After the prefix, all nonexceptional bits have toggled. Every exceptional direction depends only on neighboring nonexceptional bits, so its edge colors are independent of the traversal order inside the exceptional suffix. Sort that suffix increasingly under \(f\) and decreasingly under \(g\) to obtain complete opposite monotone words from each of the counted starting roots.

Finally, a composition of bi-surjective Boolean relations is bi-surjective; once a three-pair relation occurs, every later composition contains at least three pairs, so its cyclic trace is nonempty. If all relations are two-pair bijections, the product is either identity or swap. The identity case supplies two satisfying assignments of the exceptional root bits, giving \(2^{m+1}\) full roots; the swap case has no solution for this prefix strategy. QED.

**Residual obstruction.** Hence a cyclic cross-root counterexample, if it exists, has either adjacent non-bi-surjective sites, or the following checkerboard-parity form: one entire parity class is deficient, every site of the other parity has an equality/inequality \(D_i\), and the XOR of these relation signs around that parity cycle is one. The latter condition is an obstruction to the *common-prefix construction*, not an established obstruction to cross-favorability itself. Restoring it requires letting at least one exceptional direction cross before some of the nonexceptional directions, potentially at different positions in the two monotone paths.


## Near-universal roots for cyclic majority gates

Let \(n\ge3\). Write a cycle-local coloring as \(h_i(x)=H_i(x_{i-1},x_{i+1})\). Fix direction \(j\) and a bit \(t\). Assume that for each \(i\ne j\), precisely three inputs of \(H_i\) have color \(t\), with unique minority input \((a_i,b_i)\); the table \(H_j\) is arbitrary.

**Lemma (co-singleton relations).** Let \(R_1,\ldots,R_m\) be Boolean binary relations omitting precisely one pair \((p_k,q_k)\). Their relational product is full, or omits precisely the pair \((p_1,q_m)\). The latter occurs if and only if \(q_k\ne p_{k+1}\) for all \(k<m\).

*Proof.* For \(R_1\circ R_2\) to omit \((s,t)\), both choices of the intermediate bit must fail. This forces \(s=p_1,t=q_2,q_1\ne p_2\). Otherwise the product is full. A full relation composed with a bi-surjective relation remains full. Induction proves the claim. \(\square\)

**Theorem (two exceptional roots).** Require direction \(j\) to be last (\(\epsilon=0\)) or first (\(\epsilon=1\)). Except for at most two starting roots, a full dimension-simple geodesic with that extreme position of \(j\) can be chosen with color \(t\) in every other direction. There are two failing roots if \(a_{j+1}=b_{j-1}\), and none otherwise. In the former case they are the two solutions of
\[
\boxed{x_j=a_{j+1}+\epsilon,\qquad
x_i+x_{i+1}=a_{i+1}+b_i
\quad(i=j+1,\ldots,j-2),}
\tag{MG1}
\]
where the second index range follows the cyclic path away from \(j\).

*Proof.* For an order of directions let \(u_i=1\) if \(i\) precedes \(i+1\). The direction-\(i\) edge reads
\((x_{i-1}+u_{i-1},x_{i+1}+1-u_i)\). Its color is \(t\) unless
\[
(u_{i-1},u_i)=(p_i,q_i)
=(a_i+x_{i-1},1+b_i+x_{i+1}).
\tag{MG2}
\]
When \(j\) is last, \(u_j=0,u_{j-1}=1\); when it is first, \(u_j=1,u_{j-1}=0\). The other orientation variables form a path and any assignment of them yields an acyclic order of all directions with \(j\) in the prescribed extreme position. Thus the required path exists precisely when the pair \((u_j,u_{j-1})=(\epsilon,1-\epsilon)\) belongs to the composition of the \(n-1\) relations excluding the forbidden pair (MG2) at each \(i\ne j\).

By the lemma, failure occurs precisely when
\(p_{j+1}=\epsilon,\ q_{j-1}=1-\epsilon,\ q_i\ne p_{i+1}\) for \(i=j+1,\ldots,j-2\). Substitution gives \(a_{j+1}=b_{j-1}\) and (MG1). These \(n-2\) consecutive pair-sum equations on the \(n-1\) bits outside \(j\) have two solutions once \(x_j\) is fixed. \(\square\)

**Corollary (paired roots).** The coloring \(h\) satisfies
\[
\boxed{|P(h)|\ge2^n-4.}
\tag{MG3}
\]
If \(a_{j+1}\ne b_{j-1}\), then every root is paired. For \(t=0\), the \(j\)-last word \(0^{n-1}*\) is nondecreasing and the \(j\)-first word \(*0^{n-1}\) is nonincreasing; for \(t=1\) the extreme roles reverse. Their exceptional root sets are disjoint because (MG1) prescribes opposite values for \(x_j\). \(\square\)


Corollary (two coloring root intersection). If two cyclic-neighbor colorings have, outside one common exceptional direction, three of four local inputs of a uniform target color in each coloring separately, then |A_0(f) intersection A_1(g)| >= 2^n-4. Proof: apply the preceding two-exception theorem to f with the extreme yielding a nondecreasing word, and independently to g with the extreme yielding a nonincreasing word. Each favorable-root set omits at most two roots; their intersection omits at most four. The exceptional direction functions and the two target colors are arbitrary.


### Three-quarter coverage with mixed parity and majority sites

For a cycle-local coloring \(h\) of \(Q_n\), \(n\ge3\), fix a direction \(j\) and a target color \(t\). Write \(R_i=\{(a,b):H_i(a,b)=t\}\) for \(i\ne j\).

**Theorem (one flexible site suffices for three-quarter coverage).** Suppose every \(R_i\), \(i\ne j\), is bi-surjective. If at least one of them has three or four pairs, then at least \(3\cdot2^{n-2}\) starting roots admit a full geodesic with direction \(j\) at either specified extreme (first, or last) and all other traversed edges colored \(t\). Consequently
\[
\boxed{|A_0(h)|,|A_1(h)|\ge3\cdot2^{n-2}.}\tag{MG5}
\]
If all the \(R_i\) are two-pair bijections, the same prescribed-extreme construction is possible from precisely \(2^{n-1}\) roots.

*Proof.* Fix an extreme for \(j\) and let \(u_i=1\) mean that \(i\) precedes \(i+1\) in the direction order. The extreme fixes \(u_j\) and \(u_{j-1}\) to opposite bits. As in the preceding theorem, the other comparisons form a path. At each site \(i\ne j\), the observed neighbor bits are
\((x_{i-1}+u_{i-1},x_{i+1}+1-u_i)\).

Every bi-surjective binary relation contains an equality or inequality matching. Choose a site \(k\) with \(|R_k|\ge3\). Restrict its relation to any three permitted pairs; at every other site restrict to a permitted matching
\[
a+b=\delta_i.
\]
The matching equations become
\[
u_{i-1}+u_i=x_{i-1}+x_{i+1}+1+\delta_i
\quad(i\notin\{j,k\}).\tag{MG6}
\]
They propagate the orientation bits uniquely from the two fixed endpoints along the two disjoint segments ending next to site \(k\). The inputs observed at \(k\) are consequently affine functions of the starting root, of the form
\[
\boxed{L(x)=x_j+x_{j+1}+x_k+\alpha,\qquad
R(x)=x_j+x_{j-1}+x_k+\beta,}\tag{MG7}
\]
where \(\alpha,\beta\) depend on the selected matchings and extreme order. These expressions follow by summing (MG6) along each segment: all interior bit contributions cancel in pairs. The formulas also hold when a segment is empty.

The linear map \(x\mapsto(L(x),R(x))\) has rank two. If \(k=j+1\), then \(L=x_j+\alpha\) and \(R\) contains \(x_{j-1}\); if \(k=j-1\), the analogous statement holds with \(R=x_j+\beta\). Otherwise \(x_{j+1}\) occurs in \(L\) but not \(R\), and \(x_{j-1}\) occurs in \(R\) but not \(L\). These indices are distinct because \(n\ge3\). Hence every input pair at \(k\) occurs at \(2^{n-2}\) roots. Only the one excluded pair fails the chosen restricted system, so it succeeds for \(3\cdot2^{n-2}\) roots. The unrestricted system permits at least these roots.

If all sites are matchings, propagate (MG6) through the entire open path. The fixed endpoint comparison holds if and only if one affine equation on the root bits is satisfied; its nonconstant linear part is \(x_{j-1}+x_{j+1}\). Thus precisely half the roots succeed. Finally, choose \(j\) last when \(t=0\) and first when \(t=1\) to obtain \(A_0\), and the opposite extreme to obtain \(A_1\). \(\square\)



### Near-universal paired roots for one arbitrary direction among parity sites

**Theorem (punctured affine-cycle root bound).** Let \(n\ge3\), fix \(j\), and color edges in directions \(i\ne j\) by
\[
h_i(x)=a_i+x_{i-1}+x_{i+1},
\]
with arbitrary offsets \(a_i\in\mathbb F_2\). The remaining edge-color function \(h_j=H(x_{j-1},x_{j+1})\) is arbitrary. Then
\[
\boxed{P(h)=V(Q_n)\quad(n\ {\rm even}),\qquad
|P(h)|\ge2^n-2\quad(n\ {\rm odd}).}\tag{PA1}
\]

*Proof.* Fix starting root \(x\). Let \(b_i=a_i+x_{i-1}+x_{i+1}\) for \(i\ne j\), and define \(u_i=1\) if direction \(i\) precedes \(i+1\). The color read at direction \(i\ne j\) is
\[
c_i=b_i+1+u_{i-1}+u_i.
\]
For all these colors to equal a prescribed \(t\), the \(n-1\) constraints on the path of orientation variables away from \(j\) have a unique solution once \(u_j\) is fixed, subject to the endpoint equation
\[
\boxed{u_j+u_{j-1}=(n-1)(1+t)+S(x),\qquad
S(x)=\sum_{i\ne j}b_i=\sum_{i\ne j}a_i+x_{j-1}+x_{j+1}.}
\tag{PA2}
\]

If \(n\) is even, take \(t=S(x)\); then (PA2) gives \(u_j+u_{j-1}=1\). Choose \(j\) last if \(t=0\), first if \(t=1\). The corresponding color word is \(0^{n-1}*\) or \(*1^{n-1}\), hence nondecreasing. Reversing the extreme choice gives \(*0^{n-1}\) or \(1^{n-1}*\), hence nonincreasing. The orientation is acyclic because \(j\) is an extreme, and the path constraints supply a total order. Thus every root is paired.

Suppose \(n\) is odd. If \(S(x)=1\), equation (PA2) again permits both extreme choices, independently of \(t\), yielding both monotone orientations. Now assume \(S(x)=0\). Choose \(u_j=u_{j-1}=s\in\{0,1\}\). The bit pair read at direction \(j\) is
\[
v_s=(x_{j-1}+s,\ x_{j+1}+1-s),
\]
and the two values \(v_0,v_1\) are complementary. Put \(t_s=H(v_s)\), and solve (PA2) with all other direction colors equal to \(t_s\). If the resulting orientation is acyclic, the full path is monochromatic \(t_s\), so \(x\in P(h)\).

An orientation of a simple cycle fails acyclicity precisely when every \(u_i=s\). Such an orientation has \(c_i=b_i+1\) at each \(i\ne j\). Therefore the selected construction can be cyclic only when all \(b_i\) equal a common bit \(r\) and \(t_s=1+r\). If the \(b_i\) are not constant, both choices of \(s\) work. If they are constant, the root can fail the construction only if
\[
H(v_0)=H(v_1)=1+r.
\tag{PA3}
\]
For these roots, \(S(x)=0\) implies
\(x_{j-1}+x_{j+1}=\sum_{i\ne j}a_i\). Thus \(\{v_0,v_1\}\) is the same complementary pair of two-bit inputs for every candidate root, independent of \(r\). If \(H\) takes different values on this pair, (PA3) never holds. Otherwise let its common value be \(h\); then (PA3) forces \(r=1+h\).

Finally, the \(n-1\) equations \(b_i=r\) for \(i\ne j\) form a path on the starting-bit indices: the edges \(\{i-1,i+1\}\) form one cycle for odd \(n\), and deletion of the \(j\)-edge opens it. Fixing one starting bit propagates all the others, leaving precisely two solutions, which are antipodal. Hence at most two roots can fail to be paired. \(\square\)



**Theorem (target-rich cyclic cross-favorability).** Let \(f,g\) be two arbitrary cycle-local binary edge colorings of \(Q_n\), \(n\ge3\). Suppose there is a direction \(j\) and independently chosen target bits \(t_f,t_g\) such that
\[
\boxed{
\{(a,b):F_i(a,b)=t_f\},\quad
\{(a,b):G_i(a,b)=t_g\}
\text{ are bi-surjective for every }i\ne j.}
\tag{TR1}
\]
No condition is imposed on \(F_j,G_j\). Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{n-1}.}
\tag{TR2}
\]
In particular every such pair is cross-favorable, irrespective of the strong connectivity of its union influence graph.

*Proof.* For each coloring \(h\in\{f,g\}\), one of two cases holds. If some nonexceptional target relation has at least three pairs, the preceding three-quarter coverage theorem gives
\[
|A_0(h)|,|A_1(h)|\ge3\cdot2^{n-2}.
\]
Otherwise all nonexceptional relations are two-pair matching relations. Then every \(H_i\), \(i\ne j\), is an affine neighbor-parity function, so the punctured affine-cycle theorem gives \(P(h)=V(Q_n)\) for even \(n\), and \(|P(h)|\ge2^n-2\) for odd \(n\). In particular, for every \(n\ge3\),
\[
|A_0(h)|,|A_1(h)|\ge2^n-2\ge3\cdot2^{n-2}.
\]
Thus both \(A_0(f)\) and \(A_1(g)\) contain at least three quarters of all roots. Inclusion-exclusion proves (TR2). \(\square\)

For a binary two-input function, a target preimage is bi-surjective precisely when it is a complementary-input matching, a three-point relation, or the full relation. Thus (TR1) allows arbitrary mixtures of neighbor-parity functions and three-to-one Boolean gates with a common majority target, as well as constant functions having that target. The common target may differ between \(f\) and \(g\). One-input projections and gates whose minority color is prescribed as the target are excluded by (TR1).

**Corollary (unicyclic interactions with attached trees).** Let an arbitrary cube-edge coloring have a unicyclic direction-interaction component with nonlinear pendant trees. Form the two induced cyclic core colorings \(g^0,g^1\) in the pendant-tree elimination theorem. If they satisfy (TR1) for some common exceptional core direction \(j\), then the full coloring has at least \(2^{m-1}\) paired roots, where \(m\) is the length of the core cycle. The universal bridge equivalence supplies monochromatic antipodal geodesics in every odd next-dimensional extension of this facet coloring.

*Proof.* Apply (TR2) to the two induced core colorings and lift each of the \(2^{m-1}\) common core roots through the opposite-bit pendant-tree interfaces. Distinct core roots give distinct full roots. Apply the bridge correspondence. \(\square\)



**Strengthening (independent exceptional directions).** In the target-rich cyclic cross-favorability theorem, the exceptional direction of \(f\) may differ from that of \(g\). Precisely, choose \(j_f,j_g\) independently, and require bi-surjectivity of the \(t_f\)-preimage for each \(F_i\), \(i\ne j_f\), and of the \(t_g\)-preimage for each \(G_i\), \(i\ne j_g\). The same bound
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{n-1}}
\]
holds. Indeed, each coloring's three-quarter favorable-root estimate is independent of the other's exceptional direction; their two favorable-root sets meet by inclusion-exclusion. The unicyclic pendant-tree corollary likewise allows distinct exceptional sites in its two induced core colorings.



### Universal cross-favorability for two unary cycle-local colorings

**Theorem.** Suppose each site-local function of two unrelated edge colorings \(f,g\) of \(Q_n\), \(n\ge3\), is a constant or a possibly complemented projection of one neighboring bit. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2.}\tag{UC1}
\]
The combined influence digraph is allowed to be strongly connected.

**Root lemma.** Represent each nonconstant local function as \(h_i=x_{r(i)}+a_i\), where its reader \(r(i)\) neighbors \(i\). Reader cycles are reciprocal two-cycles or one full directed cycle; all other reader components are trees attached to cycles or rooted at constant directions. Unless the reader graph is a full directed cycle, \(x\in A_0(h)\) precisely when, for every reciprocal reader pair \(i\leftrightarrow j\),
\[
(x_i,x_j)\ne(1+a_j,1+a_i),\tag{UC2}
\]
and \(x\in A_1(h)\) precisely when \((x_i,x_j)\ne(a_j,a_i)\) for each pair.

*Proof.* The two local orders on a reciprocal pair have color words
\((x_j+a_i,x_i+1+a_j)\) and \((x_i+a_j,x_j+1+a_i)\). Both descend precisely at (UC2), and both ascend precisely at the second forbidden input. Otherwise choose monotone orders on the disjoint reciprocal pairs and shuffle their zero prefixes before their one suffixes; insert constant-colored singleton directions. Add reader-tree children outward from their parents: the new child reads color \(b=x_p+a_i\) immediately before the parent step, and \(1-b\) immediately after it. If the parent step has color \(c\), insert before if \(b\le c\), and afterward otherwise. This preserves nondecreasing order and does not affect earlier edge colors. Reverse the inequalities for nonincreasing order.

For a full directed reader cycle, prescribing every traversal color zero orients the reader precedences acyclically except at the two uniform initial reader-color patterns. At the all-zero pattern, a succession along the cycle gives the nondecreasing word \(0\,1^{n-1}\). At the all-one pattern every full order begins with color one and ends with color zero, so no nondecreasing order exists. Consequently \(A_0(h)\) omits precisely the all-one reader-pattern root, and, on complementing colors, \(A_1(h)\) omits precisely the all-zero root. \(\square\)

*Proof of the theorem.* If either coloring has a full reader cycle, its required favorable-root set misses one root, whereas the other has at least three favorable roots; hence the intersection has at least two.

Otherwise the sets \(E_f,E_g\) of reciprocal reader edges are matchings of the direction cycle. By the lemma, each matching-edge occurrence prohibits one assignment on the two endpoint root bits. An edge common to both matchings has no other incident constraint edge and permits at least two assignments. Remove these isolated double-edge components. The remaining edges occur singly, each permitting three of the four endpoint assignments. The constraint graph is a disjoint union of paths, isolated vertices, and possibly a simple cycle.

Each path and isolated vertex admits at least two assignments. A cycle admits one because the composition of three-pair Boolean relations is full or itself a three-pair relation, each having a diagonal pair. It admits at least two: given a satisfying assignment, either some one-bit flip is also satisfying, or every one-bit flip violates a clause. In the latter case each of the \(m\) variables needs a distinct blocking clause among the \(m\) edge clauses. Thus every clause has one true and one false signed atom in the original assignment. Complementing all bits also satisfies every clause. Taking products over components proves at least two common roots, and the root lemma gives their two opposite monotone full geodesics. \(\square\)

**Extension and audits.** Apply the argument componentwise for any common direction-interaction graph of maximum degree two. Exhaustive computation of all \(6^4=1296\) unary \(Q_4\) colorings and \(6^5=7776\) unary \(Q_5\) colorings confirmed the root lemma for every coloring, with minimum cross-root intersection cardinalities two and six respectively. The lower bound two is attained by alternating reciprocal pairs in even dimension, whose combined influence graph is bidirected around the entire cycle.



**Sharpness in every even dimension.** Let \(n=2m\ge4\), with cyclic indices, and define two unary colorings by
\[
f_i(x)=
\begin{cases}1+x_{i+1},&i\text{ even},\\x_{i-1},&i\text{ odd},\end{cases}
\qquad
g_i(x)=
\begin{cases}1+x_{i-1},&i\text{ even},\\x_{i+1},&i\text{ odd}.\end{cases}
\]
The reciprocal reader pairs of \(f\) are the edges \((0,1),(2,3),\ldots\), while those of \(g\) are the complementary perfect matching \((1,2),(3,4),\ldots,(n-1,0)\). Applying the root lemma, a root belongs to \(A_0(f)\) precisely when no even-edge pair \((x_i,x_{i+1})\) is \((1,0)\); it belongs to \(A_1(g)\) precisely when no odd-edge pair is \((1,0)\). Therefore simultaneous favorability imposes
\[
x_0\le x_1\le\cdots\le x_{n-1}\le x_0,
\]
and hence
\[
\boxed{A_0(f)\cap A_1(g)=\{0^n,1^n\}.}
\]
Each undirected neighbor edge belongs to one reciprocal reader matching, so the combined directed influence graph contains both arc orientations on every edge and is strongly connected. Thus the lower bound two in the unary cross-favorability theorem is optimal in every even dimension, even under maximal union-feedback connectivity.

**Failure of a universal favorable-root density bound.** For the single coloring \(h_{2k}=x_{2k+1}\), \(h_{2k+1}=x_{2k}\) on \(Q_{2m}\), the root lemma gives
\[
|A_0(h)|=|A_1(h)|=3^m,\qquad |P(h)|=2^m.
\]
Thus \(|A_0(h)|/2^{2m}=(3/4)^m\to0\), despite abundant paired roots. Any dimension-uniform cyclic cross-root proof relying on both favorable-root sets occupying more than half the cube cannot cover even these unary colorings.



### Global unary-reader cross-favorability: arbitrary reader graphs

The preceding unary cyclic theorem is a special case of the following dimension-uniform result, whose proof does not require any common interaction graph.

**Theorem (global two-color unary-reader closure).** Let \(n\ge2\) and let \(f,g\) be two arbitrary edge colorings of \(Q_n\), each direction function being either constant or of the form \(h_i(x)=x_{r(i)}+a_i\), with an arbitrary reader \(r(i)\ne i\). Reader maps and offsets may differ between the two colorings. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2.}\tag{GU1}
\]

**Root-cycle lemma.** For a unary coloring \(h\), let \(\mathcal C(h)\) denote the vertex-disjoint directed cycles of its functional reader digraph \(i\mapsto r(i)\), with constants terminating other reader chains. All reader cycles have length at least two. Then for any root \(x\),
\[
\begin{aligned}
x\in A_0(h)&\iff
\forall C\in\mathcal C(h)\ \exists i\in C:
x_{r(i)}+a_i=0,\\
x\in A_1(h)&\iff
\forall C\in\mathcal C(h)\ \exists i\in C:
x_{r(i)}+a_i=1.
\end{aligned}\tag{GU2}
\]

*Proof.* Restrict a full traversal to the directions in a reader cycle \(C\). If every initial reader color equals one, the first step in that cycle sees its reader not yet traversed and has color one, whereas the last sees its reader already traversed and has color zero. Thus no nondecreasing full traversal is possible. Likewise, uniform initial reader color zero forbids a nonincreasing traversal.

Conversely, for a nonuniform initial reader-color pattern on \(C\), require each traversed color to be zero. This prescribes relative precedences on its directed cycle, forming an acyclic orientation unless every initial reader color is identical. A topological order consequently realizes an all-zero word. At the uniform-zero pattern, the successive cyclic order has word \(0\,1^{|C|-1}\), which is nondecreasing. Thus the first test of (GU2) is sufficient on each reader cycle. Select such a local order on every disjoint reader cycle and shuffle their steps with zero prefixes preceding one suffixes; add constant sites as singleton steps. Incorporate all attached reader trees outward from their parents: a new child with initial parent-reader color \(b\) can be inserted before its parent with color \(b\), or after with color \(1-b\). One choice preserves nondecreasing order, and already present edge colors are unaffected. This proves the first equivalence. Complementing the coloring proves the second. \(\square\)

*Proof of the theorem.* Each cycle in \(\mathcal C(f)\) forbids just one full assignment on its reader-cycle root bits, namely the assignment making all its initial reader colors one. Similarly each cycle in \(\mathcal C(g)\) forbids one assignment making all its initial reader colors zero. Let \(\mathcal F\) be the combined family of these constraints and write \(m=|\mathcal F|\).

Cycles within one reader digraph are vertex-disjoint. Therefore every constraint has at least two variables, while each variable belongs to at most two constraints, at most one from each coloring. Every collection of \(k\) constraints consequently touches at least \(k\) variables, since its total variable incidences lie between \(2k\) and twice its number of distinct variables. By Hall's marriage theorem, assign to every constraint a different one of its variables. Set that designated variable opposite to its forbidden value within its assigned constraint. Since no variable is designated twice, every constraint is satisfied regardless of the values of the other variables. The \(n-m\) undesignated variables are free, giving at least \(2^{n-m}\) common roots.

If \(m<n\), this is already at least two. If \(m=n\), all constraint cycles have length two and every variable occurs in both colorings' constraint families. Thus those families are two perfect matchings on the \(n\) variables. Their union consists of alternating even cycles and doubled edges. On a doubled edge, its two forbidden pairs leave at least two assignments. On a simple alternating cycle, each edge forbids one pair. A satisfying assignment exists by the preceding Hall argument. If no single-variable flip of that assignment is satisfying, every variable must have a different blocking edge clause. Since the cycle has equally many variables and clauses, each clause then has one true and one false signed atom, so complementing all bits gives a second satisfying assignment. Hence every component has at least two assignments. This proves (GU1). \(\square\)

The preceding cyclic sharpness example realizes two common roots in every even dimension, so the global lower bound cannot be improved.

**Independent audit.** The characterization (GU2) and lower bound (GU1) were independently checked by enumeration of all full direction orders on random arbitrary reader graphs: 400 independent coloring pairs in dimension four, 500 in dimension five, and 90 in dimension six, checking every root in each instance. All tests passed.



### Simultaneous orientation control for several unary reader colorings

The Hall argument generalizes to an arbitrary finite family of unary reader colorings.

**Theorem (multi-coloring reader-cycle Hall criterion).** Let \(h^{(1)},\ldots,h^{(q)}\) be unary-reader edge colorings of \(Q_n\), and prescribe for each coloring either a nondecreasing \(0^*1^*\) or a nonincreasing \(1^*0^*\) full antipodal geodesic from a shared root. Let \(\mathcal F\) be the family of all directed reader cycles of the \(q\) colorings, counted separately for each coloring, and put \(m=|\mathcal F|\). Assume the bipartite incidence graph between \(\mathcal F\) and the \(n\) direction bits has a matching that covers every cycle. Then at least
\[
\boxed{2^{n-m}}
\]
starting roots satisfy all \(q\) prescribed favorable-orientation requirements simultaneously. The full geodesics may use different direction orders.

In particular, the hypothesis holds whenever every directed reader cycle in every coloring has length at least \(q\), because each direction bit occurs in at most one cycle per coloring, hence in at most \(q\) cycles altogether.

*Proof.* By the root-cycle characterization (GU2), each directed reader cycle \(C\) contributes a single forbidden full pattern on the starting bits indexed by \(C\). Its pattern depends on the prescribed orientation and that coloring's offsets, but not on any other coloring. Match each cycle \(C\) to a distinct direction bit \(i(C)\in C\). Assign \(x_{i(C)}\) the value opposite the forbidden value at that bit in this cycle. This violates the forbidden pattern of \(C\), independently of the values assigned to its other bits. Since matching representatives are distinct, all assignments are compatible. The remaining \(n-m\) root bits are free; every resulting root satisfies all reader-cycle conditions, and (GU2) provides all required full paths.

For the sufficient length condition, any \(k\) cycles contribute at least \(qk\) variable incidences; each direction occurs in at most \(q\) of those cycles. Their union therefore has at least \(k\) distinct variables. Hall's theorem supplies the required matching. \(\square\)

For \(q=2\) no extra length hypothesis is necessary, since every reader cycle has length at least two. The earlier global two-color theorem improves the resulting positive bound to the sharp uniform lower bound of two, including the saturated matching case \(m=n\). For \(q\ge3\), the Hall count remains a general constructive existence and multiplicity theorem whenever its stated incidence condition is met.
