# Port cogirth, short intersections, and contraction inheritance

Let \(M\) be a finite binary matroid and let \(p\in E(M)\) belong to a circuit and a cocircuit. Define the **port cogirth**
\[
g_p(M)=\min\{|Y|:Y\in\mathcal C^*(M),\ p\in Y\},
\]
where \(Z(M)\) denotes the binary cycle space. For an even positive integer \(b\), define the **short-port intersection property** \(P_b(M,p)\) by
\[
\boxed{\forall X\in Z(M)\ (p\in X),\quad
\exists Y\in\mathcal C^*(M):
p\in Y,\ |Y|=g_p(M),\ |X\cap Y|\le b.}\tag{1}
\]
Cycle–cocircuit orthogonality over \(\mathbb F_2\) forces every intersection in (1) to have positive even cardinality.

In Article XI's pointed dual \(D_n\), shortest port cocircuits are the cyclic turn encodings of antipodal geodesics, and every port-containing binary cycle encodes an antipodally odd cube-edge coloring. Thus \(P_4(D_n,p)\) is equivalent to the unrestricted two-switch conjecture, while \(P_2(D_n,p)\) is equivalent to monochromatic NORI1.

**Proposition 1 (small port cogirth).** Every pointed binary matroid with \(g_p(M)\le5\) has \(P_4\). Every pointed binary matroid with \(g_p(M)\le3\) has \(P_2\).

*Proof.* Fix any shortest port cocircuit \(Y\). For every binary cycle \(X\ni p\), the intersection \(X\cap Y\) is nonempty, even, and of size at most \(g_p(M)\). The asserted bounds follow. \(\square\)

**Theorem 2 (port-cogirth-preserving contraction inheritance).** Let \(T\subseteq E(M)\setminus\{p\}\), put \(M_0=M/T\), and assume
\[
g_p(M)=g_p(M_0).\tag{2}
\]
For any positive even \(b\), if \(P_b(M_0,p)\) holds, then \(P_b(M,p)\) holds.

*Proof.* Write \(S=E(M)\setminus T\). Take any binary cycle \(X\in Z(M)\) with \(p\in X\). The restriction \(X_0=X\cap S\) is a binary cycle of \(M/T\), and \(p\in X_0\). Choose by \(P_b(M_0,p)\) a cocircuit \(Y\ni p\) of \(M_0\) satisfying \(|Y|=g_p(M_0)\) and \(|X_0\cap Y|\le b\). Cocircuits of \(M/T\) are precisely the cocircuits of \(M\) disjoint from \(T\). Hence \(Y\) is a cocircuit of \(M\), and (2) makes it shortest among those containing \(p\). Finally \(Y\subseteq S\) gives
\[
|X\cap Y|=|X_0\cap Y|\le b.
\]
\(\square\)

**Corollary 3 (cubical contraction class).** Suppose a pointed binary matroid \(M\) has a contraction \(M/T\cong D_n\), with \(p\notin T\), and \(g_p(M)=n+1\). Then \(P_b(D_n,p)\) implies \(P_b(M,p)\). For \(b=2,4\), the universal \(P_b\) assertion over all such matroids and all \(n\ge3\) is equivalent to the respective cube conjecture, since the class includes \(M=D_n\) with \(T=\varnothing\).

The theorem applies without restrictions on the number of elements, representational rank, or other circuits of \(M\). The port cogirth equality is essential to lifting a *minimum-size* cocircuit from the contraction.
