# Parallel-face port-cocircuit exchange at corresponding terminals

# Flagged face-terminal completion and parallel-face exchange

Let \(n\ge4\), \(H_n=L(Q_n)/\langle\tau\rangle\), and let \((D_n,p)\) be the pointed dual binary matroid. Fix a binary cycle \(X\in Z(D_n)\) containing \(p\), and put \(d(t)=\mathbf1_{\{t\in X\}}\). Let
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_n),\ p\in Y,\ |Y|=n+1\}.
\tag{1}
\]
For any direction-distinct cube path \(P\) with successive edges \(e_1,\ldots,e_m\), let \(\mathscr T(P)\) be the ordered sequence of its \(m-1\) consecutive turns in \(H_n\), and set
\[
r_X(P)=\sum_{t\in\mathscr T(P)}d(t).
\tag{2}
\]
This is its number of edge-color changes, independently of the complementary choice of cube-edge coloring reconstructed from \(X\). For two paths ending at one cube vertex \(x\), define their terminal-phase disagreement by
\[
\epsilon_X(P,Q)=
\begin{cases}
d\bigl(\{\,[e_m(P)],[e_m(Q)]\,\}\bigr),&e_m(P)\ne e_m(Q),\\
0,&e_m(P)=e_m(Q),
\end{cases}
\tag{3}
\]
where the displayed turn is taken at their common terminal vertex. This quantity likewise depends only on \(X\).

**Theorem (face completion and opposite-phase certificate).** Let \(F\subset Q_n\) be a coordinate \(k\)-face with \(t=n-k\ge1\) exterior directions. Suppose \(P\subset F\) is a spanning geodesic ending at \(x\), and put \(r=r_X(P)\). Then
\[
\boxed{I(X)\le 2+2\left\lfloor\frac{r+t}{2}\right\rfloor.}
\tag{4}
\]
If another geodesic \(Q\subset F\), spanning \(F\) and terminating at the same \(x\), satisfies \(r_X(Q)\le r\) and \(\epsilon_X(P,Q)=1\), then
\[
\boxed{I(X)\le2+2\left\lfloor\frac{r+t-1}{2}\right\rfloor.}
\tag{5}
\]
If \(I(X)\ge r+t+2\), the labels on every turn joining two successive edges in any completion of \(P\) by all exterior directions are one. Equivalently, if the terminal edge of \(P\) has reconstructed color \(\rho\), then every exterior edge joining \(x^S\) to \(x^{S\cup\{i\}}\), for \(S\subsetneq T\), has color
\[
\boxed{c(x^S,x^{S\cup\{i\}})=1+\rho+|S|\pmod2.}
\tag{6}
\]
Equation (6) describes an intrinsic turn condition, since complementing \(c\) and \(\rho\) simultaneously preserves every displayed equality.

*Proof.* Append any permutation of the \(t\) exterior directions to \(P\), producing a full antipodal geodesic with at most \(r+t\) changes. A rooted full geodesic having \(z\) changes yields, by cyclic root rotation and the odd closing-turn parity, a rooted full geodesic with at most \(2\lfloor z/2\rfloor\) changes. The pointed-matroid identity \(I(X)=\mu+2\) proves (4).

For (5), choose an exterior geodesic \(W\) beginning at \(x\). Its first-edge color agrees with the final color of either \(P\) or \(Q\), because their terminal colors are opposite by (3). Appending \(W\) to that face geodesic adds at most \(t-1\) changes, giving (5) after cyclic root rotation.

Finally suppose \(I(X)\ge r+t+2\), equivalently \(\mu\ge r+t\). Every completion of \(P\) has at most \(r+t\) changes, so every one has precisely \(r+t\); in particular all \(t\) new comparisons, including the seam after the terminal edge of \(P\), are changes. For any subset \(S\) of exterior directions and \(i\notin S\), choose the completing order to traverse \(S\) first and \(i\) next. Its edge at rank \(|S|\) has color \(1+\rho+|S|\), proving (6). \(\square\)

**Corollary (terminal square signatures under a port obstruction).** Suppose \(I(X)\ge6\).

(a) Every spanning geodesic of any codimension-two face has \(r_X(P)\ge2\). If one has \(r_X(P)=2\) and ends at \(x\), with exterior directions \(a,b\), its exterior-square turn labels satisfy
\[
\boxed{
d_{ab}([x])=d_{ab}([x^{ab}])=0,\qquad
d_{ab}([x^a])=d_{ab}([x^b])=1.}
\tag{7}
\]
Any other face-spanning geodesic at the same terminal having at most two changes has terminal-phase disagreement zero with \(P\).

(b) Every spanning geodesic of any codimension-three face has at least one change. If one has precisely one change, its exterior three-cube has the rank-alternating edge colors (6), and any other path at the same terminal with at most one change has the same final phase.

*Proof.* In codimension two, a path with \(r\le1\) would make the right-hand side of (4) at most four, contrary to \(I(X)\ge6\). With \(r=2\), the extremal condition \(I(X)\ge r+t+2=6\) yields (6). The two exterior edges at the original corner have equal colors, the two at the opposite corner have equal colors, and the two mixed corners see different incoming and outgoing colors. This gives (7). Different terminal phases would invoke (5) and yield \(I(X)\le4\). The proof in codimension three is identical with \(r=1,t=3\). \(\square\)

The preceding certificates concern two face paths at a common terminal. A second transport law uses paths in *adjacent* codimension-two faces, even if their last colors have no prescribed relation.

**Theorem (parallel-face port intersection bound).** Fix two directions \(a,b\), a codimension-two face \(F\) in which their coordinates are fixed, and its neighbor \(F^a\). Suppose \(P\subset F\) and \(Q\subset F^a\) span their faces and terminate at corresponding vertices \(x,x^a\). Put \(r=r_X(P)\), \(s=r_X(Q)\). Then
\[
\boxed{
I(X)\le2+
\min\left\{
\max\bigl(r,2\lceil s/2\rceil\bigr),\
\max\bigl(s,2\lceil r/2\rceil\bigr)
\right\}.}
\tag{8}
\]
In particular, if \(r=0,s\le1\), then
\[
\boxed{I(X)=2,}
\tag{9}
\]
and if \(r,s\le2\), then \(I(X)\le4\).

*Proof.* Reconstruct an edge coloring \(c\), and write \(\rho,\sigma\) for the last edge colors of \(P,Q\). Label the four exterior square edges
\[
A=c(xx^a),\quad B=c(xx^b),\quad
C=c(x^ax^{ab}),\quad D=c(x^bx^{ab}).
\]
Completing \(P\) and \(Q\) along the two square routes gives four full antipodal geodesics with change numbers
\[
\begin{array}{ll}
r+[\rho\ne A]+[A\ne C],&
r+[\rho\ne B]+[B\ne D],\\
s+[\sigma\ne A]+[A\ne B],&
s+[\sigma\ne C]+[C\ne D].
\end{array}
\tag{10}
\]
Each is at least \(I(X)-2\), after the parity reduction explained in the first proof. We establish
\[
I(X)-2\le M:=\max\{r,2\lceil s/2\rceil\},
\tag{11}
\]
then interchange \(F,F^a\) for the other term in (8).

If \(r\) is even and \(M\ge r+2\), either completion of \(P\) suffices. If \(r\) is odd and \(M\ge r+1\), a completion of \(P\) has at most \(r+2\) changes and hence an even reduction of at most \(r+1\). It remains to consider \(M=r\). If \(r\) is even and both completions of \(P\) were insufficient, their two additional comparisons would have to be changes, forcing
\[
A=B=1+\rho,\qquad C=D=\rho.
\]
One of the routes completing \(Q\) then consists of two edges in its final color \(\sigma\), producing a full path with at most \(s\le2\lceil s/2\rceil\le r\) changes, a contradiction.

If \(r\) is odd, \(2\lceil s/2\rceil\le r-1\). When \(s\le r-2\), any completion of \(Q\) has at most \(r\) changes and its parity reduction gives at most \(r-1\). Otherwise \(s=r-1\), which is even. If both completions of \(Q\) were insufficient, both would add two changes, forcing
\[
A=C=1+\sigma,\qquad B=D=\sigma.
\]
One of the routes completing \(P\) is then monochromatic in its final phase \(\rho\), giving \(r\) changes and hence at most \(r-1\) after rotation, again a contradiction. This proves (11) and therefore (8). The cases (9) and \(r,s\le2\) follow by direct substitution, using \(I(X)\ge2\). \(\square\)

Theorems (4)--(8) transfer codimension-two terminal methods to the cycle–cocircuit problem with only two additional pieces of combinatorial data: the selected partial paths and their endpoints. All switch counts and relative terminal phases are read from the port-cycle incidence vector, and every conclusion bounds intersection with a minimum port cocircuit. The need for *jointly witnessed terminals* is retained; it cannot be replaced by intersections of unmarked support sets.
