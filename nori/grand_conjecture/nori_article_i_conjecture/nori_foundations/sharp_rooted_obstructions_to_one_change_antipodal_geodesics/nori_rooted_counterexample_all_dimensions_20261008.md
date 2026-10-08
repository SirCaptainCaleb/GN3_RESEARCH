# Rooted one-change strengthening fails for every n ≥ 5

# Sharp failure of the rooted NORI strengthening

Write \(V=[n]\), \(Q_n=\{0,1\}^V\), and let \(F\) be a three-dimensional coordinate face with ordered free directions \(\pi=(a,b,c)\). Let \(E(F)=V\setminus\{a,b,c\}\) and let \(S(F)\subseteq E(F)\) consist of its exterior directions fixed to \(1\). An *antipodal geodesic starting at \(z\)* crosses every coordinate exactly once, starting from \(z\).

**Theorem (rooted obstruction in every dimension \(n\ge5\)).** For every \(n\ge5\) and every prescribed vertex \(z\in Q_n\), there is an antipodal-reversal-odd binary coloring of ordered three-faces,
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi),
\]
for which **every** antipodal geodesic starting at \(z\) has at least two changes among its consecutive ordered-three-face colors. More precisely, for \(z=0^n\), we can arrange the exact number of changes to be
\[
\begin{cases}
2,&n=5,\\
n-3,&n\ge6\text{ even},\\
n-4,&n\ge7\text{ odd}.
\end{cases}
\]
The dimensions \(n\le4\) admit no such rooted obstruction because their geodesics have at most two ordered-three-face windows.

**Proof.** Translation of cube coordinates commutes with antipodality and preserves ordered free directions. Thus it suffices to construct the coloring for \(z=0^n\). Put \(q=n-3=|E(F)|\).

*Even \(n\ge6\).* Here \(q\) is odd. Define
\[
c(F,\pi)=|S(F)|\pmod2.
\]
Under cube antipodality the exterior weight \(k\) becomes \(q-k\), whose parity is opposite to that of \(k\). Reversal of \(\pi\) has no effect. Along any full geodesic from \(0^n\), window \(i\) has exactly \(i-1\) previously crossed exterior directions, hence color \(i-1\bmod2\). Its \(n-2\) window colors alternate, with exactly \(n-3\) changes.

*Odd \(n\ge7\).* Here \(q=2s\) with \(s\ge2\). Fix a linear ordering of \(V\), and choose a binary function \(h\) of ordered triples such that \(h(c,b,a)=1-h(a,b,c)\); for example, take \(h(a,b,c)=[a>c]\). For \(k=|S(F)|\) set
\[
c(F,\pi)=
\begin{cases}
k\bmod2,&k<s,\\
h(\pi),&k=s,\\
1\oplus(k\bmod2),&k>s.
\end{cases}
\]
Because \(|S(\bar F)|=2s-k\), the two outer branches are complementary under antipodality. At \(k=s\), reversing \(\pi\) complements \(h\), so the oddness identity holds on every ordered face. A full geodesic from \(0^n\) visits exterior weights \(k=0,1,\ldots,2s\) in order. Its first \(s\) colors alternate, and so do its last \(s\) colors, contributing \(2(s-1)\) changes. The colors immediately to the left and right of the single central window are
\[
(s-1)\bmod2
\quad\text{and}\quad
1\oplus((s+1)\bmod2),
\]
which are complementary. Whatever the central value \(h(\pi)\), exactly one of its two adjacent comparisons changes. Thus every such geodesic has \(2(s-1)+1=2s-1=n-4\) changes.

*The exceptional odd dimension \(n=5\).* Fix a linear ordering of the five directions. For \(t\in V\) and any two-element subset \(P\subseteq V\setminus\{t\}\), choose a binary function \(H(P,t)\) satisfying
\[
H((V\setminus\{t\})\setminus P,t)=1-H(P,t).
\]
For example, set \(H(P,t)=0\) when the least member of \(P\) precedes the least member of its complementary pair, and \(H(P,t)=1\) otherwise. For a face with ordered free directions \(\pi=(a,b,c)\), and with \(S=S(F)\) its set of exterior ones, define
\[
c(F,(a,b,c))=
\begin{cases}
H(\{a,b\},c),&|S|=0,\\
1-H(S\cup\{a\},b),&|S|=1,\\
H(S,a),&|S|=2.
\end{cases}\tag{*}
\]
Each argument of \(H\) is a two-element subset of the four directions other than its displayed second argument. Under antipodality and reversal, the \(|S|=0\) and \(|S|=2\) branches pair as complementary pairs in \(V\setminus\{c\}\). For \(|S|=1\), write \(S=\{u\}\) and let the remaining exterior direction be \(v\). The reversed antipodal face has free order \((c,b,a)\), exterior-one set \(\{v\}\), and color \(1-H(\{v,c\},b)=H(\{u,a\},b)\), complementary to the original \(1-H(\{u,a\},b)\). Hence (*) is antipodal-reversal odd.

Finally consider any geodesic from \(0^5\) with direction order \((a,b,c,d,e)\). Its three windows have free orders \((a,b,c)\), \((b,c,d)\), \((c,d,e)\), and exterior-one sets \(\varnothing\), \(\{a\}\), and \(\{a,b\}\). By (*), its color word is
\[
\bigl(H(\{a,b\},c),\;1-H(\{a,b\},c),\;H(\{a,b\},c)\bigr),
\]
so it has exactly two changes.

The constructions have now been proved for all \(n\ge5\). Translate them by \(z\) to prescribe any starting vertex. \(\square\)

**Interpretation.** The unrestricted NORI conjecture seeks *some* starting vertex and direction order. The theorem demonstrates that its rooted strengthening fails sharply already in dimension five, despite the full ordered-face antipodal-reversal symmetry. Consequently a dimension-raising or topological argument that fixes the initial cube vertex and seeks a one-change order for that vertex cannot prove the grand conjecture without additional structural hypotheses. This theorem supplies no counterexample to the unrooted conjecture.
