# One-direction path witnesses and a 2-SAT closure reduction

### One-direction completion gives a 2-SAT paired-root obstruction

Fix an edge coloring \(B\) of every direction of \(Q_d\) except one direction \(i\). Let \(X_e\) be the freely assigned color of each direction-\(i\) edge. Every full dimension-simple path \(P\) uses just one such edge \(e(P)\). Thus the requirement that its color word be nondecreasing or nonincreasing, denoted \(L_\uparrow(P)\) or \(L_\downarrow(P)\), is either false, true, \(X_{e(P)}=0\), or \(X_{e(P)}=1\).

**Theorem 1 (Boolean face of one-sided avoidance).** For any root set \(R\) and a chosen monotone orientation \(\sigma\), the completions \(X\) for which no root of \(R\) supports an orientation-\(\sigma\) full geodesic form either an empty family or one Boolean face: some variables are forced and all others are free. The face is empty precisely when a single full path works for both values of its variable or two full paths from roots of \(R\) cross the same direction-\(i\) edge and require opposite color values.

*Proof.* Avoidance is the conjunction of negations of the unary predicates \(L_\sigma(P)\) over all rooted full paths \(P\) from \(R\). These impose only one-variable conditions, so only the stated two inconsistencies can arise. QED.

**Theorem 2 (paired-root failure is 2-SAT).** The direction-\(i\) completions having no paired root in \(R\) are the solutions of
\[
\boxed{\Phi_{B,R}(X)=
\bigwedge_{r\in R}\ 
\bigwedge_{P,Q\text{ full from }r}
\left(\neg L_\uparrow(P)\lor\neg L_\downarrow(Q)\right).}
\tag{1}
\]
After simplification every clause contains at most two Boolean tests on individual variables. Hence the counterexample-completion family is a 2-CNF solution set, and is closed under ternary bitwise majority.

*Proof.* A root \(r\) is paired if and only if some nondecreasing path \(P\) and nonincreasing path \(Q\) from \(r\) both succeed. The clause forbids their simultaneous success. Each success test has at most one adjustable variable. Majority closure follows because if a ternary majority falsified a two-test clause, at least one of the three inputs would falsify both tests. QED.

**Corollary 3 (two-path universal restoration).** Fix a completed coloring \(g\) extending \(B\), and set \(R=A_\uparrow(g)\). Every second completion \(h\) satisfies \(A_\uparrow(g)\cap A_\downarrow(h)\ne\varnothing\) if and only if there is a nonincreasing full path from a root of \(R\) working for either value of its adjustable edge, or two paths from roots of \(R\) cross the same adjustable edge and require its two opposing values.

*Proof.* By Theorem 1, the family of completions avoiding all nonincreasing paths from \(R\) is empty precisely under the stated one- or two-path condition. QED.

**Example 4 (the root must adapt).** On \(Q_3\), take \(f_0(x)=x_2\) and \(f_1(x)=1-x_2\), with direction-2 edge colors free. No single root has a nonincreasing full path under every completion; nevertheless the nondecreasing favorable-root set is all eight vertices when direction-2 colors are zero. Two full paths rooted at \(000\) and \(001\) impose opposing conditions on the direction-2 edge based at \(000\), yielding the universal two-path restoration certificate.

**Independent check.** All 256 choices of outside coloring in three dimensions were enumerated. For every such choice the 2-CNF formula with all eight roots was unsatisfiable, confirming the published small-dimensional paired-root result through an independent implication-graph calculation.

**Closure perspective.** Through the universal bridge equivalence, the unresolved NORI1 conjecture reduces to proving that every full-root formula \(\Phi_{B,V(Q_d)}\) is unsatisfiable. This asks for a contradictory implication cycle derived from square exchanges and root reversal. The reduction is valid in all dimensions, but its universal unsatisfiability is not established.### Shared-site four-bit 2-SAT kernel

Fix edge colors of two cube colorings f,g outside one direction j. Require the j-edge colors in both to be the same four-entry local Boolean function H(x_(j-1),x_(j+1)). Then the sixteen candidate functions H giving disjoint root sets A0(f) and A1(g) are the satisfying assignments of a Boolean formula with clauses of width at most two, on the four entries of H.

*Proof.* Every full dimension-simple path uses one j-edge. With other colors fixed, success in a chosen monotone orientation is either always true, always false, or requires one chosen truth-table bit of H to have value zero or one. To forbid a pair of successful paths from the same root, conjoin the disjunction of their two negated success conditions. These are two-clause conditions on four variables. There are at most eight unit clauses and twenty-four clauses on distinct variable pairs, so 32 nontrivial clause types suffice. QED.

**Fourteen-pair certificate.** If no H gives disjoint cross-root sets, the failure formula is unsatisfiable. Its implication digraph has eight signed variable states. A variable and its negation lie in one strongly connected component, so two simple directed paths connecting them, with at most seven edges each, give a contradiction. Each implication edge originates in one rooted pair of full geodesics. Thus at most fourteen rooted path pairs suffice to certify all sixteen cases of H simultaneously.

**Four pairs can be necessary.** In Q5 with j=0, fix outside cyclic-local truth tables f_1..f_4=(5,0,5,12) and g_1..g_4=(10,15,10,3). Full-path enumeration produces twenty different nonempty pair-success patterns, each covering four of the sixteen H. Four path pairs cover all choices and no three do.

The shared-even-site theorem rules out H=0,6,9,15 as possible failures for cycle-local outside colorings. The remaining projection and unbalanced nonlinear cases are therefore a fixed four-variable implication-graph closure problem, independent of cycle dimension.

## Binary implications are essential in unrestricted one-direction 2-SAT

The full-root paired-root failure formula for the free edge-direction variables is 2-CNF in every dimension. The following affine exterior Q4 coloring disproves a proposed strengthening that would derive unsatisfiability exclusively from opposing unit clauses.

Fix
\[
f_0(x)=x_3,\qquad f_1(x)=1-x_3,\qquad f_2(x)=0,
\]
and leave \(f_3(x)=h(x_0,x_1,x_2)\) arbitrary. Set \(A=h(0,0,0)\) and \(B=h(1,1,1)\). Three rooted path-pair certificates force a paired root for every assignment:

- From binary root 0001 (integer 1), order (0,3,1,2) has color word \(0,A,0,0\). When \(A=0\), it is monochromatic, so badness requires \(A=1\).
- From root 0000, orders (0,2,1,3) and (3,0,1,2) give \(0,0,1,B\) and \(A,1,0,0\). Badness therefore requires \(\neg A\lor\neg B\).
- From root 0010 (integer 2), orders (0,2,3,1) and (1,3,0,2) give \(0,0,B,0\) and \(1,A,1,0\). Badness therefore requires \(\neg A\lor B\).

The three necessary clauses
\[
\boxed{A,\qquad\neg A\lor\neg B,\qquad\neg A\lor B}
\tag{IC1}
\]
are inconsistent. This supplies a transparent three-path-pair 2-SAT refutation for **all** values of the unrestricted h function.

However, an independent enumeration of the 16 roots and 24 direction orders found that every unary clause in the full paired-root failure formula requires \(h(y)=1\); all eight such requirements occur, but no unary clause requires \(h(y)=0\), and there is no empty clause. Thus opposing unary clauses alone do not establish the contradiction even under affine exterior rules.

**Interpretation.** This is not a new dimension-specific closure result: Q4 closure was already known. It rejects a putative *general proof mechanism*. A grand theorem via one-direction 2-SAT must generate coupled binary implications or another global invariant; counting conflicting singleton repairs cannot suffice.


## Dimension-uniform obstruction to unary-only 2-SAT closure

The earlier Q4 affine example extends to every dimension with a stronger and more transparent conclusion. This is a negative theorem about a proposed *universal proof mechanism*, not a restricted proof of NORI1.

**Theorem (all-dimensional one-direction necessity of binary implications).** Fix any \(n\ge4\), distinguish the last direction \(h=n-1\), and fix every other direction-edge color on \(Q_n\) by
\[
\boxed{ f_0(x)=x_h,\qquad f_1(x)=1-x_h,\qquad
 f_j(x)=0\ (2\le j<h).} \tag{UI1}
\]
Leave all direction-\(h\) edge colors \(X_y=f_h(y)\), \(y\in Q_{n-1}\), as independent Boolean variables.

The paired-root failure 2-CNF \(\Phi_B(X)\), after simplifying constant-success rooted path conditions, has the following properties:

(i) It has no empty clause.

(ii) Every unit clause requires \(X_y=1\); in fact **all** \(2^{n-1}\) positive units \(X_y\) occur. There is no unit requiring \(X_y=0\). Thus its unit clauses alone are consistent.

(iii) Let \(A=X_{0^{n-1}}\), \(B=X_{1^{n-1}}\). The full formula contains the three clauses
\[
\boxed{A,\qquad B,\qquad\neg A\lor\neg B,} \tag{UI2}
\]
which are inconsistent. Consequently the full formula is unsatisfiable and every assignment of all \(X_y\) admits a paired root.

These statements hold in every dimension \(n\ge4\), independently of the number of freely assigned direction-\(h\) edges.

*Proof of (i).* A path whose nondecreasing word succeeds both when its single free edge is zero and when it is one must have every fixed-color edge before direction \(h\) of color zero and every fixed-color edge after \(h\) of color one. If the initial \(h\)-bit is zero, direction 1 has color one before \(h\) and zero after \(h\), so neither placement is permitted. If that bit is one, direction 0 has the same obstructing pattern. Thus no nondecreasing full path succeeds independently of \(X\). By reversing the inequalities, an analogous obstruction to a bridge-independent nonincreasing path is supplied by direction 0 at initial \(h\)-bit zero and by direction 1 at bit one. Consequently no rooted pair of paths yields an empty clause.

*Proof of (ii).* Without bridge-independent path success, a unit clause can only come from rising and falling paths from the same root that cross the same direction-\(h\) edge and require the same value there. Suppose that required value is one. Because direction 2 is constantly zero, it must precede the bridge in the nondecreasing path and follow the bridge in the nonincreasing path. But two paths from the same root that cross the same bridge edge have the same **set of directions** before that crossing: it is the set of bits on which the common outside root differs from the bridge location. This contradicts the two required placements of direction 2. Hence there are no units forbidding the value one.

Conversely fix any bridge location \(y\). Start with outside root \(z=y\oplus e_0\) and \(h\)-bit zero. The full direction order
\[
0,\ h,\ 1,\ 2,\ 3,\ldots,h-1
\]
crosses the bridge at \(y\). Its color word is all zero when \(X_y=0\): direction 0 has color zero before \(h\), direction 1 has color zero after \(h\), and all other non-h directions have constant color zero. This single monochromatic path establishes both rising and falling favorability at its root, so paired-root failure requires \(X_y=1\). The construction works for every \(y\).

*Proof of (iii).* The first two clauses of (UI2) are the units just proved. Put \(K=(3,4,\ldots,h-1)\), possibly empty. At root \(0^n\) the two full direction orders
\[
\begin{aligned}
P_\uparrow&=(K,\ 0,\ 2,\ 1,\ h),\\
P_\downarrow&=(h,\ 0,\ 1,\ 2,\ K)
\end{aligned}
\]
have respective edge-color words
\[
0^{|K|},\,0,0,1,B
\quad\text{and}\quad
A,1,0,0,0^{|K|}.
\]
If \(A=B=1\), the first word is nondecreasing and the second nonincreasing. Their common root is paired. Therefore badness also requires \(\neg A\lor\neg B\), completing the contradiction. \(\square\)

**Logical consequence for grand-theorem closure.** A universal one-direction 2-SAT proof cannot rely only on empty clauses, opposing unit requirements, or counting singleton edge repairs. Even for (UI1), with unrestricted bridge coloring and unbounded dimension, **all** unit requirements are mutually consistent while a binary clause makes the full obstruction impossible. Any general implication-graph argument must capture interactions between at least two bridge variables. This does not by itself establish NORI1 for other outside colorings, and is not offered as a closure proof.

**Independent audit.** A separate path-word evaluator checked the displayed witness orders and word identities for every pair \((A,B)\in\{0,1\}^2\) and dimensions \(4\le n\le11\). A separate complete one-direction path-predicate enumeration in dimensions 4, 5, and 6 confirmed absence of bridge-independent paths, absence of negative units, and presence of all positive units.


## Arbitrary bridge folding gives a unary completion formula

Let f be any ordinary binary coloring of Q_d. On Q_d times {0,1}, use f in the lower facet and its complemented antipodal image in the upper facet:
\[
C(f,h)_j(x,0)=f_j(x),\qquad
C(f,h)_j(x,1)=1-f_j(\bar x)\quad(j\le d).
\]
Give the joining edge at y color h(y), where h is arbitrary. No relation between h(y) and h(bar y) is assumed.

**Theorem (one-switch folding at the same bridge).** The following conditions are equivalent:

1. C(f,h) has a full antipodal geodesic with at most one switch.
2. C(f,h) has a monochromatic full antipodal geodesic.
3. Some y satisfies y in A_(h(y))(f).
4. C(f,h) has a paired root.

Moreover a path in condition 1 crossing the joining edge at y produces a monochromatic path crossing that same joining edge.

*Proof.* Reverse a path from condition 1 if needed so that it begins in the lower facet. Write its word as a h(y) b, where a precedes the joining edge and b follows it. Let its horizontal starting point be r. Reverse its lower-facet prefix, giving a path y to r. Apply horizontal antipodal reflection to its upper-facet suffix and reverse that suffix, giving a lower-facet path r to bar y. Their direction sets are disjoint and exhaust the d horizontal directions. The concatenation therefore has full f-word
\[
v=\operatorname{rev}(a)\,\operatorname{rev}(1-b),
\]
where 1-b complements every bit.

If h(y)=0 and the original word is nondecreasing, a is all zero and rev(1-b) is nondecreasing. If h(y)=0 and the original word is nonincreasing, b is all zero and rev(a) is nondecreasing. Thus y belongs to A_0(f). If h(y)=1, the two cases similarly give a nonincreasing v, placing y in A_1(f). This proves 1 implies 3.

Given 3, split its face certificate at the seam between h(y) and 1-h(y). Reverse the initial segment in the lower facet, cross the joining edge at y, then follow the reversed antipodal image of the terminal segment in the upper facet. All these edges have color h(y); their directions are disjoint and exhaust the full cube, and the endpoints are antipodal. This proves 3 implies 2 at the same joining edge. A monochromatic path makes its endpoints paired, proving 2 implies 4. A paired root supplies a one-switch path, proving 4 implies 1. QED.

**Corollary (complete Boolean-face description).** The full-root paired-root failure formula for this exterior is equivalent to the unary formula
\[
\boxed{
\Phi_f(h)=
\bigwedge_{y\in A_0(f)}h(y)
\ \land\
\bigwedge_{y\in A_1(f)}\neg h(y).
}
\tag{BF1}
\]
It is inconsistent precisely when P(f) is nonempty. If P(f) is empty, its solution set is a Boolean face: h is one on A_0(f), zero on A_1(f), and unrestricted at the empty roots
\[
E(f)=Q_d\setminus(A_0(f)\cup A_1(f)).
\]
Every solution has
\[
A_0(C(f,h))=A_1(C(f,h))=\varnothing.
\tag{BF2}
\]
Thus all global root orientations disappear simultaneously throughout the entire completion face.

*Proof.* The theorem identifies existence of any full monotone orientation, any paired root, and a matched bridge site. Their common absence is precisely (BF1). QED.

If e=|E(f)| and P(f) is empty, there are 2^e arbitrary bridge completions in (BF1), of which 2^(e/2) are antipodally odd. Indeed reversal gives A_1(f)=bar A_0(f); hence E(f) is antipodally invariant, the forced values already obey oddness, and each empty antipodal pair permits two odd choices.

**Corollary (individual bridge criticality).** At any completion satisfying (BF1), changing one joining-edge color creates a monochromatic full geodesic if and only if its site lies in A_0(f) union A_1(f). At an empty site the changed coloring still has no full one-switch path. This holds for individual joining edges, throughout the completion face, without an oddness requirement on h.

**Closure consequence.** Every antipodally odd cube coloring has the displayed complemented-antipodal relation between the facets of any direction. Thus the full-cube bridge layer admits this unary normal form. The coupled binary implications needed for a grand proof lie in the arbitrary ordinary facet f and its own one-direction completion problem. A proof must establish P(f) nonempty for arbitrary f, or force a contradiction among the constraints from several facet choices. Varying joining edges at empty sites alone remains entirely inside the Boolean face (BF1).


**Independent folding audit.** A direct path evaluator checked 802816 full paths in dimensions three through five. These included every lower-facet coloring and every lower-root direction order for facet dimensions two and three, with an independently selected unrestricted bridge table for each coloring, plus sampled paths in facet dimension four. Among these paths, 396577 had at most one switch. Folding each at its joining edge produced a full face path in the orientation selected by that edge's color in every case. The dimension-uniform proof above supplies the theorem.


## Long-range 2-SAT clauses in a dimension-uniform affine exterior

The family (UI1) also provides a precise obstruction to proofs that inspect only clauses linking bridge sites at bounded Hamming distance. Fix \(n\ge4\), \(h=n-1\), and put \(J=\{2,\ldots,h-1\}\), \(|J|=n-3\).

**Theorem.** In the full-root one-direction paired-root failure formula for
\[
f_0(x)=x_h,\qquad f_1(x)=1-x_h,\qquad
f_j(x)=0\quad(2\le j<h),
\]
with independent missing-direction colors \(X_y\), the following hold:

1. Every unit is positive, and each \(X_y\) occurs as a positive unit; there are no empty clauses, as already proved in (UI1).
2. If the formula contains a binary clause \(\neg X_y\lor\neg X_z\), then \(y\) and \(z\) differ in every bit indexed by \(J\), so
\[
\boxed{d_H(y,z)\ge n-3.}\tag{NL1}
\]
3. For every \(y\), the formula contains
\[
\boxed{\neg X_y\lor\neg X_{y+\mathbf1_J}.}\tag{NL2}
\]
These latter clauses pair all bridge sites in a perfect matching at distance \(n-3\).

*Proof.* Every direction in \(J\) is colored zero. A rising path requiring bridge color one must traverse every direction of \(J\) before its bridge, since a subsequent zero would violate nondecreasing order. A falling path requiring bridge color one must traverse every such direction after its bridge, since a preceding zero would violate nonincreasing order. The two paths generating a binary clause start at the same root, so the XOR of their bridge sites has all the J-bits set. This proves (2).

For (3), start at any root with outside bits \(x\) and height zero. The rising direction order \((2,\ldots,h-1,1,h,0)\) gives word
\[
0^{n-3},1,X_{x+\mathbf1_J+e_1},1;
\]
the falling order \((1,h,0,2,\ldots,h-1)\) gives word
\[
1,X_{x+e_1},1,0^{n-3}.
\]
If both displayed bridge variables are one, both monotone paths exist from this shared root, so the absence of paired roots implies their negated disjunction. Varying \(x\) proves (NL2), and translation by the nonzero vector \(\mathbf1_J\) is a fixed-point-free involution. \(\square\)

**Corollary.** Restrict this formula to unit clauses and binary clauses whose bridge sites have Hamming distance strictly less than \(n-3\). The restricted 2-CNF is satisfiable by setting every \(X_y=1\): no retained clause contains two negative occurrences, all units are positive, and there are no empty clauses. But the full formula is unsatisfiable because (NL2) contradicts the positive units. Therefore, as \(n\) grows, no refutation confined to **original** implication clauses of a fixed bounded geometric radius can prove all such completions good. Deriving long-range implications from local ones is not excluded.

This is an obstruction to an attempted universal proof technique, not a proof of NORI1. Independent path enumeration in dimensions four through six and a direct formula check through dimension eleven corroborate the argument.


## A two-path global certificate target for grand closure

The paired-root completion formula retains useful local information. For dimension-uniform closure, a weaker-looking universal assertion gives a sharper certificate target.

**Theorem (equivalent global two-path formulations).** The following assertions, each quantified over all dimensions, are equivalent:

1. Every antipodally odd cube-edge coloring has a monochromatic full antipodal geodesic.
2. Every ordinary cube-edge coloring f has A_0(f) nonempty.
3. For every exterior coloring B leaving one direction i uncolored, at least one of the following occurs:
   - one full path has a nondecreasing color word for both values of its direction-i edge;
   - two full paths, permitted to have different roots, traverse the same direction-i edge and have nondecreasing words when that edge has value zero and value one, respectively.

*Proof.* Assertion 1 gives the universal paired-root theorem through the odd bridge construction, and therefore gives 2. Applying 2 to an odd coloring supplies a full path with at most one switch, which root sliding makes monochromatic; thus 2 gives 1.

For a fixed exterior B, the completions with A_0 empty form the Boolean face obtained by forbidding every ascending full-path predicate. Each predicate is false, true, or a required value of its one direction-i edge. This avoidance face is empty precisely when a predicate is true independently of the edge value or two predicates require opposite values at the same edge. This is precisely assertion 3. If neither witness exists, the consistent unary requirements provide an ordinary completion with A_0 empty, contradicting 2. Conversely either witness guarantees A_0 nonempty in every completion. QED.

The theorem gives a certificate involving at most two complete direction orders for each exterior, assuming the grand assertion holds. The roots must remain free to differ. Here the unary formula forbids every ascending full path at every root. The earlier 2-CNF forbids simultaneous rising and falling paths at a common root. Their unit requirements differ: the family (UI1) has consistent units in the paired-root formula, while the two paths below give opposing units in the one-sided formula. Thus (UI1)'s binary-implication obstruction is compatible with this global two-path target. A proof of assertion 3 for all exteriors would close NORI1 in all dimensions.

### Two paths can be necessary

In Q_4 leave direction 3 free and fix
\[
f_0(x)=x_3,\qquad f_1(x)=1-x_3,\qquad f_2(x)=0.
\]
For any joining site y in Q_3, start at (y,0) and use order (3,2,1,0). Its word is
\[
h(y),0,0,1,
\]
which is ascending precisely when h(y)=0. Starting at (bar y,0) and using order (2,0,1,3) instead gives
\[
0,0,1,h(y),
\]
which is ascending precisely when h(y)=1. Both paths traverse the same free edge.

There is no single full path ascending for both possible values of its free edge. Such a path would require every edge before direction 3 to be zero and every edge after it to be one. If directions 0 and 1 occur on the same side of direction 3, their colors are opposite, contradicting that requirement. If they occur on different sides, their colors are equal, again contradicting the required zero before and one after. Thus the two-path alternative is essential.

### The missing global lemma

The unresolved statement is the witness dichotomy in assertion 3 for an arbitrary pair of exterior facets. It asks for a universal ascending path or opposing ascending requirements at one common edge. A proof must retain the roots and direction supports of both witnesses. For complemented-antipodal exterior facets, the preceding bridge theorem identifies this dichotomy with a paired root of the lower facet; the unary normal form alone supplies no additional contradiction there.

This is a global proof target with a constant number of path witnesses. Its universal validity remains conjectural. It avoids the need to prove a prescribed-root assertion or a dimension-independent favorable-root density bound.


## Counterexample-preserving facet pivot and an imbalance interval

This gives a dimension-preserving operation on **arbitrary hypothetical paired-root-free ordinary cube colorings**. Unlike a bounded-reader reduction, it places no restriction on the internal edge-color rules.

Fix d>=2 and let f be a binary undirected-edge coloring of Q_d with
\[
P(f)=A_0(f)\cap A_1(f)=\varnothing.
\]
Put \(R=A_0(f)\), \(S=A_1(f)=\bar R\), and \(E=Q_d\setminus(R\cup S)\). Thus R and S are disjoint and E is antipodally invariant. An *admissible bridge selector* is a Boolean function h on Q_d obeying
\[
h(\bar x)=1-h(x),\qquad h|_R=1,\qquad h|_S=0.
\tag{FP1}
\]
Such functions exist, with one free bit for each antipodal pair in E.

Build an antipodally odd coloring C on Q_(d+1) with old direction colors f_i(x) on the height-zero facet, colors \(1-f_i(\bar x)\) at height one, and height-direction color h(x). The established bridge-folding theorem says C has no monochromatic full antipodal geodesic. For each old direction j, take the lower j-facet of C and denote its induced ordinary Q_d coloring by \(T_{j,h}(f)\).

**Theorem (facet-pivot closure).** For every admissible h and every j,
\[
\boxed{P(T_{j,h}(f))=\varnothing.}\tag{FP2}
\]
The opposite j-facet is the complemented antipodal image of this pivot, and also has no paired root.

*Proof.* If any j-facet of C admitted a paired root, the free-bridge theorem in the j-direction would produce a monochromatic full antipodal geodesic of C, contrary to its construction. Antipodal oddness gives the asserted relation of opposing facets. \(\square\)

**Theorem (imbalance interval).** Let \(M=d2^{d-1}\) be the total number of edges in Q_d and let \(m=2^{d-1}\). For k different from j, let \(L_{k,j}\) and \(U_{k,j}\) denote the counts of one-colored direction-k edges of f within the j=0 and j=1 facets. Put
\[
D_j=\sum_{k\ne j}(L_{k,j}-U_{k,j}),\quad
r_{j,0}=|R\cap\{x_j=0\}|,\quad
r_{j,1}=|R\cap\{x_j=1\}|.
\]
As h ranges over all admissible selectors, the number \(W(T_{j,h}(f))\) of one-colored edges attains **every integer** in
\[
\boxed{
\left[(d-1)2^{d-2}+D_j+r_{j,0},\
(d-1)2^{d-2}+D_j+m-r_{j,1}\right].
}\tag{FP3}
\]
The interval has length
\[
\boxed{\delta(f)=m-|A_0(f)|=|E|/2.}\tag{FP4}
\]
Every complementary total \(M-W(T_{j,h}(f))\) also occurs among paired-root-free Q_d colorings.

*Proof.* In the lower j-facet of C, each old direction k different from j has a height-zero slice contributing \(L_{k,j}\) one-edges and a height-one slice contributing \(2^{d-2}-U_{k,j}\), since the latter is the complemented antipodal copy of the original j=1 slice. The height-direction contributes
\[
H_j(h)=|\{x:x_j=0,\ h(x)=1\}|.
\]
Consequently
\[
W(T_{j,h}(f))=(d-1)2^{d-2}+D_j+H_j(h).
\]
The values of h on R are forced to one and on S to zero. By \(S=\bar R\), the j=0 slice has \(r_{j,0}\) forced ones and \(r_{j,1}\) forced zeros. Every empty antipodal root pair has one representative in the j=0 slice, whose h value can be chosen independently. Thus H_j attains all integers from \(r_{j,0}\) to \(m-r_{j,1}\). Its range length is \(m-|R|=|E|/2\). The opposite j-facet has colors \(1-T_{j,h}(f)(\bar z)\) and therefore M minus the one-edge count. \(\square\)

**Corollary (extremal-bias inequality).** If a paired-root-free Q_d coloring exists, define
\[
B_d=\max_{P(g)=\varnothing}|W(g)-M/2|.
\]
For every such f,
\[
\boxed{
B_d\ge
\frac{2^{d-1}-|A_0(f)|}{2}
+\max_j\left|D_j+\frac{r_{j,0}-r_{j,1}}2\right|.
}\tag{FP5}
\]
In particular, if f has at least one empty root, its pivot family contains at least two paired-root-free colorings of the **same dimension** with different one-edge totals; by color complementation one may choose one having positive total edge-color imbalance. More generally the attainable bad one-edge totals contain a full interval of \(|E|/2+1\) consecutive integers, and its reflected interval.

*Proof.* The interval in (FP3) has midpoint
\[
M/2+D_j+(r_{j,0}-r_{j,1})/2
\]
and half-width \(\delta(f)/2\). Its endpoints and their reflected counterparts have maximum deviation from M/2 equal to the right side of (FP5) for that j. Maximize over j. \(\square\)

**Strategic significance and limit.** The pivot operation can move a hypothetical arbitrary obstruction through many same-dimensional colorings and vary global color imbalance without modifying the original nonlinear core. This is a route to extremizing counterexamples by imbalance or empty-root deficiency, not a classification by a bounded number of reader hubs. The inequality is necessary if bad colorings exist; it does not force B_d beyond the independent edge-transversal upper bound and hence does not prove NORI1. The full simultaneous-facet consistency conditions cannot by themselves refute badness: whenever a paired-root-free facet exists, the admissible selectors (FP1) produce legal bad odd extensions satisfying every facet condition.

**Independent arithmetic audit.** The j-facet one-edge count was checked in 600 random nonlinear instances across dimensions two through six, using two separately computed evaluations of the pivot coloring and the formula above. The counterexample-preservation argument is analytic and follows from the bridge-folding equivalence.


### Probabilistic form of the facet-pivot imbalance interval

Under the hypotheses and notation of the preceding facet-pivot theorems (FP1)--(FP5), choose an admissible bridge selector h **uniformly** by making its \(\delta(f)=|E|/2\) free antipodal-pair bits independent fair coins.

**Corollary (binomial counterexample ensemble).** For every old direction j,
\[
\boxed{
W(T_{j,h}(f))
\ \stackrel{\mathrm{law}}{=}\
(d-1)2^{d-2}+D_j+r_{j,0}
+\operatorname{Bin}(\delta(f),1/2).
}\tag{FP6}
\]
Therefore
\[
\boxed{
\mathbb E W(T_{j,h}(f))
=M/2+D_j+\frac{r_{j,0}-r_{j,1}}2,\qquad
\operatorname{Var}W(T_{j,h}(f))=\delta(f)/4.
}\tag{FP7}
\]
Every coloring in this entire random ensemble remains paired-root-free if the input f is. No locality, linearity, vertex-balance, or restriction on the dependency graph is assumed.

*Proof.* Each antipodal pair of empty roots contributes one free h-value on the j=0 slice and thus one independent Bernoulli(1/2) indicator to the number of one-colored height edges. Every other h-value on that slice is forced by the rising/falling favorable-root sets. The horizontal color count is constant under h and is the term already derived in (FP3). Summing the independent indicators proves (FP6), while elementary binomial moments and \(\delta=m-r_{j,0}-r_{j,1}\) yield (FP7). Counterexample preservation follows from (FP2). \(\square\)

This provides a probabilistic extremization mechanism in **the same dimension**. It is conditional on a hypothetical paired-root-free input. Unlike global pseudorandom padding, its fluctuation parameter is the number of *empty roots* of that input. A closure proof must establish a contradiction between these unavoidable fluctuations and an independent global obstruction on the achievable color imbalance; the current general edge-transversal lower bound is too weak to do so.
