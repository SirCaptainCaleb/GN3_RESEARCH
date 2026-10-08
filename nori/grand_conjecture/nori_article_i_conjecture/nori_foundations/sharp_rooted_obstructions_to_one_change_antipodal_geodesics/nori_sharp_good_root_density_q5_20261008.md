# Sharp Q5 root density: at least 30 good starts, and at most two adjacent bad starts

# Sharp density of good starting vertices in dimension five

Let \(c\) be a binary coloring of ordered three-faces of \(Q_5\), with
\[
c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi).
\]
Call a starting vertex *bad* if every five-coordinate geodesic from it has at least two color changes. Such a geodesic has three windows, so every bad rooted word is \(010\) or \(101\).

**Theorem.** The set of bad starting vertices has cardinality at most two, and if there are two, they are adjacent in \(Q_5\). Consequently **at least 30 of the 32 starting vertices admit a one-change antipodal geodesic**. Both conclusions are sharp: for any chosen adjacent pair, some antipodal-reversal-odd coloring makes precisely those two vertices bad.

**Proof (upper bound).** Translating a coloring by any cube vertex preserves antipodal-reversal oddness. If two bad vertices existed at distance \(k\), translate the first to \(0^5\) and relabel the coordinate set as \(V=\{a,b,c,d,e\}\) so that the second has ones in the first \(k\) listed coordinates.

The classification of a coloring bad at \(0^5\) gives a function \(H(P,t)\) defined when \(t\in V\), \(P\subset V\setminus\{t\}\), \(|P|=2\), satisfying
\[
H((V\setminus\{t\})\setminus P,t)=1\oplus H(P,t),\tag{1}
\]
and, for an ordered face with free-coordinate order \((r,s,t)\) and exterior-one set \(S\),
\[
c(F,(r,s,t))=
\begin{cases}
H(\{r,s\},t),&|S|=0,\\
1\oplus H(S\cup\{r\},s),&|S|=1,\\
H(S,r),&|S|=2.
\end{cases}\tag{2}
\]
For completeness, all rooted words at \(0^5\) must alternate. Equality of first and last window colors, comparing first-two-coordinate transpositions, makes the rank-zero color symmetric in the first two free directions; call it \(H(\{r,s\},t)\). The middle and final windows of a rooted path then force (2) at ranks one and two, and antipodal reversal forces (1).

Write \(H(rs,t)=H(\{r,s\},t)\). For the purported second bad root \(y\), the first and third windows of any direction order have equal colors, whereas the first and second have different colors. Substituting (2) gives the following concise contradictions, where the listed direction orders are *complete* geodesics from \(y\):

- **\(k=2\), \(y_a=y_b=1\)**. The orders \(bdeac\), \(abdce\), and \(bedac\) yield, respectively,
\[
\begin{aligned}
H(bc,a)\oplus H(ab,d)&=1 &&(\text{windows }1,2),\\
H(ab,d)\oplus H(ab,e)&=1 &&(\text{windows }1,3),\\
H(ab,e)\oplus H(bc,a)&=1 &&(\text{windows }1,2).
\end{aligned}
\]
Adding over \(\mathbb F_2\) gives \(0=1\).

- **\(k=3\) or \(4\), \(y_a=y_b=y_c=1\)** (and also \(y_d=1\) when \(k=4\)). The orders \(adebc\) and \(badce\) yield
\[
H(bc,a)\oplus H(ab,e)=1 \quad(\text{windows }1,2),\qquad
H(ab,e)\oplus H(bc,a)=0 \quad(\text{windows }1,3).
\]
This is impossible.

- **\(k=5\), \(y=1^5\)**. The orders \(abcde\) and \(adebc\) yield
\[
H(bc,a)\oplus H(ad,c)=0 \quad(\text{windows }1,2),\qquad
H(ad,c)\oplus H(bc,a)=1 \quad(\text{windows }1,3).
\]
Again impossible.

Thus distinct bad starting vertices must have Hamming distance exactly one. Three distinct vertices of a hypercube cannot be pairwise adjacent, so there are at most two. This proves that at least 30 starting vertices are good.

**Sharpness.** Fix a distinguished direction \(a\). Define \(H(P,t)\), for \(t\ne a\), by
\[
H(P,t)=\mathbf1_{\{a\notin P\}},
\]
and, for \(t=a\), choose **any** function on the two-subsets of \(V\setminus\{a\}\) satisfying the complementary-pair condition (1). Define the full ordered-face coloring by (2). Its antipodal-reversal oddness and the badness of \(0^5\) follow from the classification.

To check that the adjacent vertex \(e_a\) is also bad, consider any direction order \(p=(p_1,\ldots,p_5)\), and let \(j\) be the position of \(a\) in this order. Along the geodesic starting at \(e_a\), the exterior-one set of the \(i\)-th window is the previously traversed directions other than \(a\), together with \(a\) if it is still untraversed and exterior to the window. Formula (2) gives the following complete three-window words:
\[
\begin{array}{c|c}
j&\text{window color word}\\\hline
1&010\\
2&010\\
3&H(\{p_1,p_2\},a),\;1\oplus H(\{p_1,p_2\},a),\;H(\{p_1,p_2\},a)\\
4&101\\
5&101
\end{array}
\]
Every case has exactly two changes. Hence both \(0^5\) and \(e_a\) are bad. The upper bound already proved implies every other starting vertex is good. Translating and permuting coordinates yields the example for any prescribed adjacent pair. \(\square\)

**Research use.** In dimension five the NORI conclusion is quantitatively strong: at least \(15/16\) of all starting vertices have a good coordinate order. Any induction that controls starting-vertex distributions, rather than choosing a single fixed root, may exploit this density. The theorem does not itself establish general \(n\ge7\) closure.
