# Parallel-face port-cocircuit exchange at corresponding terminals

# Parallel-face port-cocircuit exchange at corresponding terminals

Let \(n\ge4\), \(H_n=L(Q_n)/\langle\tau\rangle\), and let \((D_n,p)\) be the pointed binary matroid of the antipodal turn covering. Fix a port-containing binary cycle \(X\) of \(D_n\), let \(d_X(t)=\mathbf1_{\{t\in X\}}\) for turns \(t\in E(H_n)\), and put
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_n),\ p\in Y,\ |Y|=n+1\}.
\tag{1}
\]
For a direction-distinct cube path \(P=(e_1,\ldots,e_m)\), define the integer turn weight
\[
r_X(P)=\sum_{j=1}^{m-1}d_X(\{[e_j],[e_{j+1}]\}).
\tag{2}
\]
It equals the number of edge-color changes in \(P\) for either cube coloring recovered from \(X\). The pointed matroid formula says that the minimum switch count over all full antipodal geodesics is \(I(X)-2\). In particular, \(I(X)\) is even.

**Theorem (parallel-face intersection bound).** Fix two directions \(a,b\), a codimension-two face \(F\) in which their coordinates are fixed, and the neighboring face \(F^a\). Suppose \(P\subset F\) and \(Q\subset F^a\) span their faces and terminate at corresponding vertices \(x,x^a\). Write \(r=r_X(P)\) and \(s=r_X(Q)\). Then
\[
\boxed{
I(X)\le2+
\min\left\{
\max\bigl(r,2\lceil s/2\rceil\bigr),\
\max\bigl(s,2\lceil r/2\rceil\bigr)
\right\}.}
\tag{3}
\]
Consequently, a monochromatic face-spanning path matched to a path of at most one change in the adjacent face forces \(I(X)=2\). Two matched face-spanning paths with at most two changes each force \(I(X)\le4\).

*Proof.* Recover an antipodally odd cube-edge coloring \(c\) from \(X\). Write \(\rho,\sigma\) for the final colors of \(P,Q\), respectively. Label the four edges of the exterior square at their terminals:
\[
A=c(xx^a),\quad B=c(xx^b),\quad
C=c(x^ax^{ab}),\quad D=c(x^bx^{ab}).
\tag{4}
\]
Completing either face path by the two possible exterior square routes gives four full antipodal geodesics with respective switch counts
\[
\begin{array}{ll}
r+[\rho\ne A]+[A\ne C],&
r+[\rho\ne B]+[B\ne D],\\
s+[\sigma\ne A]+[A\ne B],&
s+[\sigma\ne C]+[C\ne D].
\end{array}
\tag{5}
\]
For every rooted full geodesic with \(z\) changes, cyclic rotation of the root gives another full geodesic with at most \(2\lfloor z/2\rfloor\) changes. Indeed, when \(z\) is odd, the closing antipodal comparison has value zero, and cutting the cyclic turn word at a changed comparison removes one switch. Thus any bound for a completion in (5) yields the corresponding even bound on \(I(X)-2\).

First prove
\[
I(X)-2\le M:=\max\{r,2\lceil s/2\rceil\}.
\tag{6}
\]
If \(r\) is even and \(M\ge r+2\), either completion of \(P\) has at most \(r+2\le M\) changes. If \(r\) is odd and \(M\ge r+1\), either completion has at most \(r+2\) changes, which is odd; cyclic reduction gives at most \(r+1\le M\). It remains to consider \(M=r\).

If \(r\) is even and both completions of \(P\) failed to yield at most \(r\) after cyclic reduction, each would introduce two new switches. Their square-edge constraints are
\[
A=B=1+\rho,\qquad C=D=\rho.
\tag{7}
\]
One of the two completing routes for \(Q\) then has both edges of color \(\sigma\), so it gives a full geodesic with at most \(s\le2\lceil s/2\rceil\le r\) changes, a contradiction.

If \(r\) is odd, \(2\lceil s/2\rceil\le r-1\). When \(s\le r-2\), any completion of \(Q\) has at most \(s+2\le r\) changes; cyclic reduction gives at most \(r-1\). The remaining case is \(s=r-1\), with \(s\) even. If both completions of \(Q\) failed to yield at most \(r-1\), they would both introduce two switches, forcing
\[
A=C=1+\sigma,\qquad B=D=\sigma.
\tag{8}
\]
One of the two routes completing \(P\) then consists of edges of color \(\rho\), producing \(r\) switches and hence at most \(r-1\) after cyclic reduction, again a contradiction.

This proves (6). Interchanging \(F\) and \(F^a\) proves
\(I(X)-2\le\max\{s,2\lceil r/2\rceil\}\). Taking the smaller bound proves (3). Substituting \((r,s)=(0,0),(0,1)\), or \(r,s\le2\), proves the consequences. \(\square\)

The theorem uses two marked face paths with **corresponding terminal vertices**, an additional geometric condition on top of their individual turn weights. It adds an inter-face intersection certificate to the single-face completion and exterior-star rigidity theorems. Both paths, their turns, and the matching of their terminals can be read from the direction-labeled cube covering, while their switch counts are simply incidences with the port cycle \(X\).
