# Monotone triangle contractions and directional excess in antipodal turn cycles

Let \(n\ge3\), let \(H_n=L(Q_n)/\langle\tau\rangle\), and write \(\alpha\) for the monodromy of the double covering \(L(Q_n)\to H_n\). An antipodally odd edge coloring \(c\) induces a binary turn weight \(d\) by
\[
d([\{e,f\}])=c(e)\oplus c(f)
\]
for cube edges \(e,f\) incident at one vertex. For a cycle \(C\) of \(H_n\), put \(w_d(C)=\sum_{t\in C}d(t)\), with the sum taken in the integers.

Consider a simple cycle \(C\) of length \(r\) with \(\alpha(C)=1\). Lift its cyclically ordered vertices to cube edges
\[
e_1,e_2,\ldots,e_r,e_{r+1}=\tau e_1.
\]
For \(1\le j\le r\), let \(u_j\) be the common endpoint of \(e_j,e_{j+1}\), and put \(u_0=\tau u_r\). Each pair \(u_{j-1},u_j\) consists of endpoints of \(e_j\). Write
\[
s(C)=|\{j:u_{j-1}=u_j\}|,
\qquad
m_i(C)=|\{j:u_{j-1}\ne u_j,\ e_j\text{ has direction }i\}|.
\]
These numbers are invariant under cyclic reindexing, reversal, and antipodal choice of lift. Since \(u_r=\tau u_0\), each \(m_i(C)\) is positive and odd. Hence, writing
\[
q(C)=\sum_{i=1}^n\frac{m_i(C)-1}{2},
\]
we obtain the directional-excess identity
\[
\boxed{|C|=n+s(C)+2q(C).}\tag{1}
\]

**Theorem 1 (monotone contraction of a stationary contact).** If \(s(C)>0\), there is a simple cycle \(C'\) of \(H_n\) such that
\[
\alpha(C')=1,\qquad |C'|=|C|-1,\qquad
s(C')=s(C)-1,\qquad q(C')=q(C),
\tag{2}
\]
and, simultaneously for every admissible turn weight \(d\),
\[
\boxed{w_d(C')\le w_d(C).}\tag{3}
\]
The difference \(w_d(C)-w_d(C')\) is either \(0\) or \(2\).

*Proof.* Choose an index \(j\) with \(u_{j-1}=u_j=v\), and cyclically reindex the lift so that \(2\le j\le r-1\). The three cube edges \(e_{j-1},e_j,e_{j+1}\) are distinct and meet at \(v\). Therefore the two turns
\[
[\{e_{j-1},e_j\}],\quad [\{e_j,e_{j+1}\}]
\]
can be replaced by the single turn \([\{e_{j-1},e_{j+1}\}]\). This removes the vertex \([e_j]\) from \(C\). Since \(C\) is simple and \(r\ge n+1\ge4\), the resulting closed walk \(C'\) is a simple cycle of length \(r-1\). The symmetric difference of the two cycles is a triangle of the clique of turns at \(v\). This triangle has monodromy zero, establishing \(\alpha(C')=\alpha(C)=1\).

The contact vertices of every retained cube edge are unchanged: the two contacts of the removed edge coincide at \(v\). Thus the removed index is the only one counted by \(s\), and the coordinate traversal counts \(m_i\) remain unchanged. This proves (2).

Set \(a=c(e_{j-1})\), \(b=c(e_j)\), and \(z=c(e_{j+1})\). All three colors are compared at the same cube vertex, and
\[
\begin{aligned}
w_d(C)-w_d(C')
&=(a\oplus b)+(b\oplus z)-(a\oplus z)\\
&=2\,\mathbf1_{\{a=z\ne b\}}\ \ge0.
\end{aligned}\tag{4}
\]
The replacement depends only on \(C\), so (3) holds for every antipodally odd edge coloring at once. \(\square\)

**Corollary 2 (moving-cycle normal form).** Every simple cycle \(C\) with \(\alpha(C)=1\) admits a sequence of \(s(C)\) triangle contractions ending at a simple cycle \(C^\circ\) with
\[
\alpha(C^\circ)=1,\quad s(C^\circ)=0,\quad
|C^\circ|=n+2q(C),\quad
w_d(C^\circ)\le w_d(C)
\tag{5}
\]
for every admissible \(d\). Consequently, if \(q(C)=0\), the terminal cycle is a length-\(n\) antipodal-geodesic cycle.

*Proof.* Repeatedly apply Theorem 1. The quantity \(s\) decreases by one at each contraction while \(q\) is preserved. When \(s=0\), (1) gives the length in (5). For \(q=0\), that length is \(n\), and the odd-girth characterization identifies the cycle with a full antipodal geodesic. \(\square\)

**Corollary 3 (weighted stability immediately above odd girth).** For every admissible \(d\),
\[
\boxed{
\min_{\substack{C\text{ simple}\\\alpha(C)=1,\ |C|\le n+1}}w_d(C)
=
\min_{\substack{C\text{ simple}\\\alpha(C)=1,\ |C|=n}}w_d(C).
}\tag{6}
\]
In particular, the minimum \(\mu(c)\) of the number of color changes on a full antipodal geodesic satisfies
\[
\mu(c)=
\min_{\substack{C\text{ simple}\\\alpha(C)=1,\ |C|\le n+1}}
w_d(C)-1.
\tag{7}
\]

*Proof.* Odd girth gives \(|C|\ge n\). If \(|C|=n+1\), identity (1) forces \(s(C)=1\) and \(q(C)=0\), so Theorem 1 supplies a length-\(n\) cycle of no greater weight. The reverse inequality follows by inclusion. Equation (7) then follows from cyclic rotation of a full antipodal geodesic: its cyclic turn weight is odd, and omitting any turn of weight one as the terminal seam yields a rooted geodesic with \(w_d(C)-1\) changes. \(\square\)

**Corollary 4 (the first repeated-direction obstruction).** Let \(C\) have \(\alpha(C)=1\) and \(|C|=n+2\). Either \(s(C)=2,q(C)=0\), in which case \(C\) contracts through a length-\((n+1)\) cycle to a length-\(n\) cycle without increasing any admissible turn weight, or \(s(C)=0,q(C)=1\). In the latter case every contact traverses a cube edge, and its direction sequence traverses one coordinate three times and each other coordinate once.

More generally, if \(\mu(c)\ge4\), every monodromy-one cycle \(C\) with \(w_d(C)\le3\) has \(q(C)\ge1\). Thus a low-weight circuit obstructed from shortening to a geodesic must include repeated coordinate traversal.

*Proof.* The dichotomy at length \(n+2\) follows from \(s+2q=2\), with \(s,q\) nonnegative integers. Apply Corollary 2 in the first case. In the second, \(\sum_i(m_i-1)/2=1\) with all \(m_i\) odd and positive, yielding the asserted direction counts. Finally, if \(q(C)=0\) and \(w_d(C)\le3\), Corollary 2 yields a length-\(n\) cycle of weight at most three, and (7) gives \(\mu(c)\le2\). \(\square\)

The contractions use only triangles within cube-edge stars and work simultaneously for every representative of the admissible switching class. Their scope is determined by the directional excess \(q\). After all stationary contacts are removed, further shortening must address coordinate directions traversed at least three times; such steps need not admit a non-increasing triangle contraction.
