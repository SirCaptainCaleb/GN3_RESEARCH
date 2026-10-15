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
