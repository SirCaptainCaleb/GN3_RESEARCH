# Penultimate-length extension and parallel-face endpoint exclusion

# Penultimate-length extension and parallel-face endpoint exclusion

Let \(n\ge3\). Color the undirected edges of \(Q_n\) by \(c:E(Q_n)\to\{0,1\}\), where \(c(\bar e)=1-c(e)\). Write \(x^i\) for the vertex obtained by flipping coordinate \(i\), and \(x^{ij}=(x^i)^j\). For a nonempty geodesic \(P\), let \(\sigma(P)\) be its number of edge-color changes.

**Lemma 1 (penultimate-length parity).** Let \(P\) be an \((n-1)\)-edge geodesic from \(u\) to \(v\), missing direction \(d\), with initial color \(s\), final color \(t\), and \(r=\sigma(P)\). If \(r\) is even, precisely one of the two \(d\)-edge extensions preserves \(r\) changes. If \(r\) is odd, either both preserve \(r\), or both introduce one additional change. For odd \(r\), preservation occurs if and only if \(c(uu^d)=s\).

*Proof.* Since \(v=\bar u^d\), the unused \(d\)-edges at \(u,v\) are antipodal, with colors \(a,1-a\), where \(a=c(uu^d)\). Prepending the edge at \(u\) introduces \([a\ne s]\) changes, while appending the edge at \(v\) introduces \([1-a\ne t]\) changes. Since \(t=s\oplus(r\bmod2)\), these indicators are complementary for even \(r\) and equal for odd \(r\). In particular, a monochromatic penultimate geodesic extends monochromatically. \(\square\)

**Lemma 2 (odd-change rotation).** If a full antipodal geodesic has an odd number \(r\) of color changes, there exists a full antipodal geodesic with \(r-1\) changes. Consequently, the minimum number \(\mu(c)\) of changes among full antipodal geodesics is even. In particular, the existence of a full geodesic with at most one change implies a monochromatic full geodesic.

*Proof.* Let the full geodesic have color word \(w_1,\ldots,w_n\), with \(r\) odd. Choose any change position \(k\), so \(w_k\ne w_{k+1}\). Cyclically move its first \(k\) coordinate directions to the end, using the vertex reached after those directions as the new root. The resulting full antipodal geodesic has color word
\[
(w_{k+1},\ldots,w_n,1-w_1,\ldots,1-w_k).
\]
Its internal changes within the two displayed blocks number \(r-1\). Since \(r\) is odd, \(w_n=1-w_1\), so the new join introduces no change. Thus its total is \(r-1\). A minimum over all full geodesics cannot be positive and odd. \(\square\)

**Theorem 3 (color-change-preserving completion across parallel faces).** Let \(F\) be an \((n-2)\)-face with fixed coordinates \(a,b\). Suppose a monochromatic geodesic \(P\) spans \(F\) and terminates at \(x\in F\). Then either a monochromatic full antipodal geodesic exists, or the following holds simultaneously for both adjacent faces: every geodesic \(Q\) spanning \(F^a\) and terminating at \(x^a\), or spanning \(F^b\) and terminating at \(x^b\), extends by two edges to a full antipodal geodesic \(R\) satisfying \(\sigma(R)=\sigma(Q)\).

*Proof.* Let \(s\) be the color of \(P\), and assume that no monochromatic full antipodal geodesic exists. By Lemma 1, no monochromatic \((n-1)\)-edge geodesic exists. Appending either \(a\)- or \(b\)-edge at \(x\) to \(P\) therefore forces
\[
c(xx^a)=c(xx^b)=1-s. \tag{1}
\]
The antipodal image of \(P\) spans \(F^{ab}\) and has color \(1-s\). It has \(x^{ab}\) as an endpoint: the other endpoint of \(P\) is \(x^{[n]\setminus\{a,b\}}\), whose antipode is \(x^{ab}\). Applying the same penultimate argument at \(x^{ab}\) yields
\[
c(x^{ab}x^a)=c(x^{ab}x^b)=s. \tag{2}
\]
Let \(Q\) span \(F^a\) and end at \(x^a\), with final color \(t\). If \(t=1-s\), append the route \(x^a,x,x^b\), whose two edges both have color \(t\) by (1). If \(t=s\), append \(x^a,x^{ab},x^b\), whose two edges both have color \(t\) by (2). Each concatenation uses every coordinate once and reaches the antipode of its starting vertex. Both appended edges agree with the terminal color, so no additional change occurs. The argument for \(Q\) spanning \(F^b\) is symmetric. \(\square\)

**Corollary 4 (one-change parallel-face endpoint exclusion).** In a counterexample to the monochromatic antipodal-geodesic assertion, a monochromatic geodesic spanning \(F\) and terminating at \(x\) excludes every geodesic with at most one color change spanning \(F^a\) and terminating at \(x^a\), or spanning \(F^b\) and terminating at \(x^b\).

*Proof.* Theorem 3 would yield a full antipodal geodesic with at most one change; Lemma 2 would make it monochromatic. \(\square\)



Theorem 3 strengthens parallel-face endpoint exclusion to a monochromatic path paired with a path having one color change.

**Theorem 5 (synchronized opposite-phase switch splicing).** Let \(n\ge4\), let \(F\) be a codimension-two face with fixed coordinates \(a,b\), and put \(D=[n]\setminus\{a,b\}\). Suppose there are two geodesics spanning adjacent faces,
\[
P:\quad u\ \xrightarrow[\text{color }s]{A}\ z\
\xrightarrow[\text{color }1-s]{B}\ x
\quad\text{in }F,
\]
\[
Q:\quad u^a\ \xrightarrow[\text{color }1-s]{A}\ z^a\
\xrightarrow[\text{color }s]{B}\ x^a
\quad\text{in }F^a,
\]
where \(A,B\) are a partition of \(D\) into two nonempty direction sets. The paths may traverse directions within \(A\) and within \(B\) in different orders. All edges within each displayed block have the displayed color. Then the coloring has a monochromatic full antipodal geodesic.

*Proof.* Write \(h=c(zz^a)\).

If \(h=s\), the following two length-\((n-1)\) monochromatic geodesics of color \(s\) exist:
\[
u\ \xrightarrow{P|_A}\ z\ \xrightarrow{a}\ z^a\
\xrightarrow{Q|_B}\ x^a,
\]
and
\[
x^a\ \xrightarrow{(Q|_B)^{\rm rev}}\ z^a\
\xrightarrow{a}\ z\
\xrightarrow{(P|_A)^{\rm rev}}\ u.
\]
Both use every direction in \(D\cup\{a\}\) once. Their missing \(b\)-edges at the displayed terminal vertices are \(x^ax^{ab}\) and \(uu^b\), which are antipodal; consequently one has color \(s\). Appending it yields a monochromatic full geodesic.

If \(h=1-s\), use instead the monochromatic \((n-1)\)-edge paths of color \(1-s\)
\[
u^a\ \xrightarrow{Q|_A}\ z^a\
\xrightarrow{a}\ z\
\xrightarrow{P|_B}\ x,
\]
and its reversal
\[
x\ \xrightarrow{(P|_B)^{\rm rev}}\ z\
\xrightarrow{a}\ z^a\
\xrightarrow{(Q|_A)^{\rm rev}}\ u^a.
\]
Their terminal missing \(b\)-edges, \(xx^b\) and \(u^au^{ab}\), are antipodal, so one has color \(1-s\). Again appending that edge gives a monochromatic full antipodal geodesic. \(\square\)

**Corollary 6 (phase coherence at a matched switch).** In a counterexample to NORI1, two one-change geodesics spanning adjacent codimension-two faces, with corresponding initial vertices, change vertices, and final vertices, must have the same initial edge color (and hence the same final edge color).

*Proof.* If their initial colors differed, their monochromatic blocks would satisfy Theorem 5. \(\square\)

**Role of the hypotheses.** The paths need only have matching initial, change, and terminal vertices across the \(a\)-translation; their within-block direction orders can differ. The conclusion arises from two competing monochromatic \((n-1)\)-edge routes whose missing edges form an antipodal pair. The central unresolved configuration for this method is two aligned one-change paths with the same phase.


**Theorem 7 (monochromatic-arm interface obstruction).** Continue to assume \(c(\bar e)=1-c(e)\), and fix adjacent \((n-2)\)-faces \(F,F^a\) with remaining fixed direction \(b\). Let \(P\) span \(F\) from \(u\) to \(x\), and let \(Q\) span \(F^a\) from \(u^a\) to \(x^a\). Suppose \(w\) is an interior vertex of \(P\) for which \(w^a\) is an interior vertex of \(Q\). All path portions mentioned below are nonempty.

(i) If \(P[u,w]\) and \(Q[w^a,x^a]\) are both monochromatic in color \(s\), then either a monochromatic full antipodal geodesic exists or \(c(ww^a)=1-s\).

(ii) If \(Q[u^a,w^a]\) and \(P[w,x]\) are both monochromatic in color \(t\), then either a monochromatic full antipodal geodesic exists or \(c(ww^a)=1-t\).

In particular, if both (i) and (ii) hold at the same projected vertex with \(s\ne t\), a monochromatic full antipodal geodesic exists.

*Proof.* The coordinate supports of \(P[u,w]\) and \(Q[w^a,x^a]\) are complementary within \(D=[n]\setminus\{a,b\}\), since their projected starts and ends are \(u,x\) and \(w\) occurs along both spanning geodesics. If \(c(ww^a)=s\), concatenating \(P[u,w]\), the \(a\)-edge, and \(Q[w^a,x^a]\) gives a monochromatic geodesic of length \(n-1\), which extends by Lemma 1. Thus failure of the monochromatic full-path conclusion forces \(c(ww^a)=1-s\). The proof of (ii) uses \(Q[u^a,w^a]\), the reverse \(a\)-edge, and \(P[w,x]\). Both directions use every coordinate in \(D\cup\{a\}\) once. When \(s\ne t\), the two required values \(1-s\) and \(1-t\) for the same \(a\)-edge are incompatible. \(\square\)

**Corollary 8 (ordered-switch separator).** Suppose \(P,Q\) are as in Theorem 7, with projected coordinate orders agreeing. Their words have one change each:
\[
w(P)=s^k(1-s)^{m-k},\qquad
w(Q)=(1-s)^\ell s^{m-\ell},
\quad m=n-2,\quad 1\le k,\ell<m.
\]
Let \(z_r\) be their common projected vertex after the first \(r\) coordinate directions. If no monochromatic full antipodal geodesic exists, then:
\[
\begin{cases}
c(z_rz_r^a)=s,&k<\ell,\ k\le r\le\ell,\\
c(z_rz_r^a)=1-s,&\ell<k,\ \ell\le r\le k.
\end{cases}
\]
If \(k=\ell\), a monochromatic full geodesic necessarily exists.

*Proof.* When \(k<\ell\), at each \(r\in[k,\ell]\) the \(Q\)-prefix and \(P\)-suffix are both monochromatic of color \(1-s\). Apply Theorem 7(ii). When \(\ell<k\), at each \(r\in[\ell,k]\) the \(P\)-prefix and \(Q\)-suffix have color \(s\). Apply Theorem 7(i). If \(k=\ell\), both arm conditions hold at \(z_k\), in opposite colors. \(\square\)

**Corollary 9 (oppositely oriented switch-band intersection).** Consider two pairs \((P,Q)\) and \((P',Q')\) of adjacent-face spanning one-change geodesics as in Corollary 8, having the same initial vertex \(u\in F\) and the same initial color \(s\) on their \(F\)-paths. The paired paths within each pair have a common projected coordinate order, though the orders of the two pairs may differ. Suppose the first pair has split indices \(k<\ell\), the second has split indices \(\ell'<k'\), and there is a vertex \(w\in F\) lying on both projected chains at a rank
\[
k\le d_F(u,w)\le\ell,\qquad
\ell'\le d_F(u,w)\le k'.
\]
Then a monochromatic full antipodal geodesic exists.

*Proof.* Corollary 8 applied to the first pair requires \(c(ww^a)=s\) in the absence of a monochromatic full geodesic, while the second pair requires \(c(ww^a)=1-s\). \(\square\)

These interface conditions provide a reachability-based target: in a hypothetical counterexample, switch bands of opposite orientation and initial phase \(s\) must avoid sharing a projected vertex. This moves the problem from single-path endpoint colors to the intersection geometry of entire families of colored maximal chains; obtaining such an intersection unconditionally remains open.


## Theorem 10 (parallel-face switch bound)

Let \(n\geq 3\), and let \(c\) be an edge coloring of \(Q_n\) satisfying \(c(\bar e)=1-c(e)\). Let \(F\) be an \((n-2)\)-face with exterior directions \(a,b\). Suppose that \(P\subseteq F\) and \(Q\subseteq F^a\) are long geodesics terminating at corresponding vertices \(x\) and \(x^a\), respectively. Write \(r=\sigma(P)\), \(s=\sigma(Q)\), and
\[
\mu(c)=\min\{\sigma(R):R\text{ is a full antipodal geodesic of }Q_n\}.
\]
Then
\[
\boxed{\mu(c)\leq\max\{r,2\lceil s/2\rceil\}.} \tag{10.1}
\]
By interchanging \(F,F^a\), one obtains
\[
\boxed{
\mu(c)\leq
\min\bigl\{\max(r,2\lceil s/2\rceil),\,
\max(s,2\lceil r/2\rceil)\bigr\}.
} \tag{10.2}
\]
In particular, \(\mu(c)\leq\max(r,s)\) unless \(r=s\) is odd, in which case \(\mu(c)\leq r+1\). When \(r\neq s\) and \(\max(r,s)\) is odd, the stronger inequality \(\mu(c)\leq\max(r,s)-1\) holds.

*Proof.* Put \(p=c(\text{last edge of }P)\) and \(q=c(\text{last edge of }Q)\), and label the four edges of the square at \(x\) by
\[
A=c(xx^a),\qquad B=c(xx^b),\qquad
C=c(x^ax^{ab}),\qquad D=c(x^bx^{ab}).
\]
As \(P\) and \(Q\) each traverse every direction other than \(a,b\) once, adjoining either of the two possible two-edge square routes gives a full antipodal geodesic. The resulting switch numbers are
\[
\begin{array}{ll}
r+[p\neq A]+[A\neq C],&
r+[p\neq B]+[B\neq D],\\
s+[q\neq A]+[A\neq B],&
s+[q\neq C]+[C\neq D].
\end{array}\tag{10.3}
\]
By Lemma 2, any full geodesic with \(t\) changes implies \(\mu(c)\leq 2\lfloor t/2\rfloor\).

Set \(M=\max\{r,2\lceil s/2\rceil\}\). If \(r\) is even and \(M\geq r+2\), either completion of \(P\) has at most \(r+2\leq M\) changes. If \(r\) is odd and \(M\geq r+1\), every completion of \(P\) has at most \(r+2\) changes; since \(r+2\) is odd, Lemma 2 yields \(\mu(c)\leq r+1\leq M\). It remains to consider \(M=r\).

First suppose \(r\) is even. If \(\mu(c)>r\), the first two completions in (10.3) must each introduce two new changes: an increase of zero produces at most \(r\) changes, and an increase of one produces \(r+1\) changes, reducible to \(r\) by Lemma 2. Therefore
\[
A=B=1-p,\qquad C=D=p.
\]
One of the two square routes completing \(Q\) has both edges in color \(q\), so it introduces no additional changes. This gives \(\mu(c)\leq s\leq 2\lceil s/2\rceil\leq r\), a contradiction.

Now suppose \(r\) is odd. Then \(2\lceil s/2\rceil\leq r-1\). If \(s\leq r-2\), either completion of \(Q\) has at most \(s+2\leq r\) changes, which by Lemma 2 gives \(\mu(c)\leq r-1\). The remaining possibility is \(s=r-1\), necessarily even. Assuming \(\mu(c)>r\), each of the two completions of \(Q\) in (10.3) must introduce two changes, since at most one new change would give at most \(r\) changes and hence at most \(r-1\) after parity reduction. Thus
\[
A=C=1-q,\qquad B=D=q.
\]
Whichever value \(p\) has, one of the two square routes completing \(P\) consists of two edges of color \(p\). The resulting full geodesic has \(r\) changes; parity reduction gives \(\mu(c)\leq r-1\), again a contradiction.

This proves (10.1). Swapping \(F\) with \(F^a\) proves (10.2), and the final claims follow because \(\mu(c)\) is even. \(\square\)

**Geometric interpretation.** The terminal square has four candidate completions, two from each face. If the two completions of one path are both forced to exceed the proposed bound, their bridge-edge colors force a low-switch completion of the other. The bound is uniform in the dimension of the cube and in both face-path switch counts.
