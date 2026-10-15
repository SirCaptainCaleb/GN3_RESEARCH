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
