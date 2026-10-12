# Corresponding-switch crossover and odd-defect cancellation

# Corresponding-switch crossover and odd-defect cancellation

Let \(c:E(Q_n)\to\{0,1\}\) be an antipodally odd coloring of undirected cube edges, \(n\ge4\). Fix exterior directions \(a,b\) and adjacent codimension-two faces \(F,F^a\) with common free-coordinate set \(D=[n]\setminus\{a,b\}\). Let \(P\subset F\), \(Q\subset F^a\) span their faces and terminate at corresponding vertices \(x,x^a\). Both paths start at corresponding vertices \(u,u^a\), since each uses every coordinate in \(D\). For any edge-colored geodesic \(T\), denote its number of changes by \(\sigma(T)\). Put \(\mu(c)=\min\{\sigma(R):R\text{ is a full antipodal geodesic}\}\).

**Lemma 1 (penultimate completion).** Every \((n-1)\)-edge geodesic \(T\) with \(t\) changes gives
\[
\mu(c)\le 2\lceil t/2\rceil. \tag{1}
\]

*Proof.* Its unused-direction edges at the initial and final vertices are antipodal, so their colors differ. When \(t\) is even, the initial and final colors of \(T\) agree and one of prepending or appending the unused edge preserves \(t\). When \(t\) is odd, either extension has at most \(t+1\) changes. Each extension is a full antipodal geodesic. \(\square\)

**Theorem 2 (interior crossover).** Suppose \(w\) is interior to \(P\) and the corresponding vertex \(w^a\) is interior to \(Q\). Decompose \(P=P_-P_+\) at \(w\) and \(Q=Q_-Q_+\) at \(w^a\). Set \(h=c(ww^a)\). Denote the last colors of \(P_-,Q_-\) by \(\lambda_P,\lambda_Q\), and the first colors of \(P_+,Q_+\) by \(\rho_P,\rho_Q\). Then both inequalities hold:
\[
\begin{aligned}
\mu(c)&\le 2\left\lceil
\frac{\sigma(P_-)+\sigma(Q_+)+[\lambda_P\ne h]+[h\ne\rho_Q]}{2}
\right\rceil,\\
\mu(c)&\le 2\left\lceil
\frac{\sigma(Q_-)+\sigma(P_+)+[\lambda_Q\ne h]+[h\ne\rho_P]}{2}
\right\rceil.
\end{aligned}\tag{2}
\]

*Proof.* The prefixes \(P_-\) and \(Q_-\) use the same coordinate set \(S\subset D\), because their starting vertices correspond and their endpoints correspond. Each suffix uses \(D\setminus S\). The paths
\[
P_-\, (ww^a)\, Q_+,\qquad
Q_-\, (w^aw)\, P_+
\]
therefore traverse every direction in \(D\cup\{a\}\) once and omit only direction \(b\). Their change counts are the expressions inside the ceiling operations in (2), prior to division by two. Apply Lemma 1. \(\square\)

**Corollary 3 (balanced opposite-phase switches).** Suppose both paths switch at \(w,w^a\), in opposite phases:
\[
(\lambda_P,\rho_P)=(z,1-z),\qquad
(\lambda_Q,\rho_Q)=(1-z,z). \tag{3}
\]
Let \(r=\sigma(P)\), \(s=\sigma(Q)\), \(i=\sigma(P_-)\), \(j=\sigma(Q_-)\). Then
\[
\mu(c)\le
\begin{cases}
2\lceil(s-1+i-j)/2\rceil,&h=z,\\
2\lceil(r-1+j-i)/2\rceil,&h=1-z.
\end{cases}\tag{4}
\]
When \(i=j\),
\[
\boxed{\mu(c)\le 2\left\lceil\frac{\max\{r,s\}-1}{2}\right\rceil.}\tag{5}
\]
In particular, when \(r=s=k\) is odd and the two opposite-phase switches have equal numbers of preceding changes,
\[
\boxed{\mu(c)\le k-1.}\tag{6}
\]
Thus matched opposite-phase three-switch geodesics force \(\mu(c)\le2\), while the one-switch case forces \(\mu(c)=0\). The two direction orders may differ on both sides of \(w\); the common intermediate vertex and the balanced change counts are sufficient.

*Proof.* If \(h=z\), the first crossover in Theorem 2 introduces no change at either junction. Since \(Q\) switches at \(w^a\), its suffix has \(s-j-1\) internal changes, giving the first branch of (4). If \(h=1-z\), the second crossover introduces no junction changes and its suffix has \(r-i-1\) changes. If \(i=j\), either branch implies (5); for odd \(k\), the latter becomes \(k-1\). \(\square\)

An improvement for odd switch counts is also available without a corresponding interior vertex.

**Proposition 4 (terminal-square alternative).** Suppose \(P,Q\) each have an odd number \(k\) of changes, and their final colors \(p,q\) differ. Label the four edges of the square at \(x\) by
\[
A=c(xx^a),\quad B=c(xx^b),\quad
C=c(x^ax^{ab}),\quad H=c(x^bx^{ab}).
\]
Then either \(\mu(c)\le k-1\), or the square colors alternate:
\[
\boxed{A=H\ne B=C.}\tag{7}
\]
Moreover, (7) is the sole square coloring that prevents the terminal-square completion argument itself from reducing the bound to \(k-1\).

*Proof.* Apply antipodal reversal to \(P\) and \(Q\): reverse their antipodal images. These geodesics terminate at \(x^{ab},x^b\), respectively. Because their switch count \(k\) is odd, their last colors are \(p,q\), respectively. Thus there are four face-spanning paths terminating at the four corners, with last colors \(p,q,p,q\) in cyclic order. If any of
\[
A=C=p,\qquad B=H=p,\qquad A=B=q,\qquad C=H=q \tag{8}
\]
holds, append the indicated monochromatic two-edge square route to its compatible face path. The resulting full geodesic has \(k\) changes. Since \(k\) is odd, root rotation across any change gives a full geodesic with \(k-1\) changes.

For the remaining case, swap color names so that \(p=0,q=1\), and suppose none of (8) holds. Necessarily \(A\ne B\): if both are 1, the third equality in (8) holds; if both are 0, avoiding \(B=H=0\) forces \(H=1\), avoiding \(C=H=1\) forces \(C=0\), and then \(A=C=0\). The symmetric argument gives \(C\ne H\). Also \(A\ne C\), since \(A=C=0\) is forbidden, while \(A=C=1\), together with \(A\ne B\) and \(C\ne H\), would force \(B=H=0\). These inequalities give \(A=H\) and \(B=C=1-A\), establishing (7). Conversely, an alternating square satisfies none of (8). \(\square\)

Theorem 2 exploits a common intermediate vertex, Corollary 3 cancels a synchronized opposite-phase switch, and Proposition 4 characterizes the remaining terminal-square pattern when two odd-switch paths have different final colors. No endpoint-coincidence or synchronized-interior-switch existence claim is assumed.
