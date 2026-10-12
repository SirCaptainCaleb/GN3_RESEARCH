# Metric loop lifting and the geodesicity-excess certificate

Let \(H\) be a finite connected graph with a nontrivial covering-monodromy cochain \(a\), let
\[
D=M\!\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*
\]
be the corresponding pointed binary lift with port \(p\), and fix an admissible signature \(d=a+\delta f\). Let \(S=\operatorname{supp}(d)\), \(X_d=S\cup\{p\}\in Z(D)\), and \(H_0=(V(H),E(H)\setminus S)\). Define
\[
\mathscr L(d)=\left\{e=uv\in S:
u,v\text{ belong to the same connected component of }H_0\right\}.
\]
For \(e\in\mathscr L(d)\), write \(\ell_e=\operatorname{dist}_{H_0}(u,v)\), and put \(\ell_*(d)=\min_{e\in\mathscr L(d)}\ell_e\). As usual the minimum of an empty family is infinite.

**Theorem 1 (metric loop-lifting identity).** The minimum cardinality of a port cocircuit intersecting \(X_d\) in two elements is
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\
p\in Y,\ |X_d\cap Y|=2}}|Y|
=\ell_*(d)+2.}
\tag{1}
\]
In particular, a two-point-intersection port cocircuit exists if and only if the monochromatic-component quotient \(J_d\) has a loop. Its minimum size is determined by the shortest zero-disagreement path connecting the endpoints of a changed turn that becomes a loop in \(J_d\).

*Proof.* Given \(e=uv\in\mathscr L(d)\), take a shortest \(u\)-to-\(v\) path \(P\) in \(H_0\). Since \(P\) is simple and does not use \(e\), the edge set \(C=P\cup\{e\}\) is a simple cycle in \(H\), with precisely one changed turn. Its covering monodromy is
\[
\alpha(C)=\langle a,C\rangle
=\langle d,C\rangle=1.
\]
Consequently \(Y=C\cup\{p\}\) is a port cocircuit of \(D\) meeting \(X_d\) precisely in \(\{e,p\}\), and \(|Y|=\ell_e+2\).

Conversely, every cocircuit \(Y\) containing \(p\) corresponds to a simple monodromy-one cycle \(C=Y\setminus\{p\}\) of \(H\). If \(|X_d\cap Y|=2\), the cycle \(C\) contains precisely one edge \(e=uv\) from \(S\), and every other edge is in \(H_0\). Thus \(C\setminus\{e\}\) is a zero-turn path joining \(u\) to \(v\), of length at least \(\ell_e\). Therefore \(|Y|\ge\ell_*(d)+2\). Both inequalities establish (1). \(\square\)

For the cube, the existence of at least one such loop follows from the known unrestricted monochromatic antipodal-path theorem (Wu–Yang, 2026), as already recorded in Article XI. The nontrivial question is the distance of the corresponding lifted loop.

## Cube geodesicity as a zero-turn distance equality

For \(n\ge3\), put \(H_n=L(Q_n/\tau)\) and retain the notation of Theorem 1. Write
\[
g_{p,2}(d)=\min\{|Y|:Y\in\mathcal C^*(D_n),\
p\in Y,\ |X_d\cap Y|=2\}.
\]

**Theorem 2 (even resource-excess distance theorem).** For every antipodally odd edge coloring of \(Q_n\), the minimum \(g_{p,2}(d)\) is finite and satisfies
\[
\boxed{g_{p,2}(d)=n+1+2q_*(d),\qquad
\ell_*(d)=n-1+2q_*(d)}
\tag{2}
\]
for a nonnegative integer \(q_*(d)\). Every minimum-cardinality port cocircuit with two-point intersection is represented by a stationary-free odd-monodromy turn cycle whose lifted moving walk travels each cube coordinate an odd number of times. Its repeated-direction excess is \(q_*(d)\).

In particular, the monochromatic NORI1 conjecture is equivalent to the metric condition
\[
\boxed{
\forall d\text{ admissible on }H_n,\quad
\ell_*(d)=n-1.}\tag{3}
\]
A counterexample, if one exists, must satisfy \(\ell_*(d)\ge n+1\). Equivalently, every changed turn whose endpoints lie in one zero-turn component would have zero-turn distance at least \(n+1\).

*Proof.* The unrestricted monochromatic antipodal-path theorem, together with Article XI's odd-girth duality, guarantees the existence of an odd-monodromy turn cycle of integer turn cost one. Thus Theorem 1 makes \(g_{p,2}(d)\) finite. Choose such a simple cycle \(C\) of the least possible length \(r\).

If \(C\) has a stationary contact, the balanced star-triangle shortcut removes the corresponding stationary edge-state vertex, yields a shorter simple odd-monodromy cycle, and does not increase integer turn cost. The new cost is still a positive odd integer, so it must equal one, contrary to minimality. Therefore \(C\) has no stationary contacts.

Its cyclic edge-state lift is consequently a walk of \(r\) cube edges from a vertex \(x\) to its antipode \(\tau x\). Each coordinate direction occurs an odd number of times; writing its multiplicity as \(1+2k_i\) gives
\[
r=\sum_{i=1}^n(1+2k_i)=n+2\sum_i k_i.
\]
Set \(q_*(d)=\sum_i k_i\). Since \(r=g_{p,2}(d)-1\), Theorem 1 yields (2). If \(q_*=0\), the walk changes each coordinate once and hence is an antipodal geodesic. Its cyclic turn cost is one; place the unique changed turn at the closing seam to obtain a monochromatic full geodesic. Conversely, every monochromatic full antipodal geodesic has a cyclic turn cycle of length \(n\), cost one, and produces \(g_{p,2}\le n+1\). Since the deck displacement is \(n\), no odd-monodromy turn cycle has fewer than \(n\) turns, so equality follows. This proves (3). \(\square\)

**Corollary 3 (a graph-distance sufficient condition).** Suppose a deck-odd cube coloring has at least one changed turn whose endpoints lie in a common zero-turn component of \(H_n\) of graph diameter at most \(n-1\). Then it has a monochromatic antipodal geodesic.

*Proof.* Such a turn has \(\ell_e\le n-1\); Theorem 2 forces \(\ell_*\ge n-1\), so \(\ell_*=n-1\), and (3) applies. \(\square\)

This metric reformulation isolates the full remaining obstruction as the presence of repeated coordinate directions in a shortest zero-turn lift of a changed-turn loop. The pointed cographic restriction minor records which loops exist, while the distances \(\ell_e\) require the zero-turn component geometry discarded by that minor. A universal short-port result therefore needs a hypothesis controlling these **loop-lifting distances**, rather than only its circuit and cocircuit incidence algebra.
