# Unbounded switches under reversal coherence in arities congruent to one modulo four

# Unbounded switches under reversal coherence in arities \(k\equiv1\pmod4\)

Let \(k\ge5\) satisfy \(k\equiv1\pmod4\). For an ordered \(k\)-face \((F,\pi)\) of \(Q_n\), let \(\bar F\) complement all its fixed coordinates.

**Theorem.** For every \(r\ge3\) and \(n\ge\max\{k+1,r(2r+1)+1\}\), there exists a binary coloring of ordered \(k\)-faces satisfying
\[
 c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi),
 \qquad c(F,\operatorname{rev}\pi)=c(F,\pi),                    \tag{1}
\]
for which every full antipodal geodesic has at least \(2r-2k+1\) changes in its ordered-face color word. In particular, for \(k=5\), \(r=6\), \(n=79\), no full antipodal geodesic is \(2\)-splice. For every fixed \(k\equiv1\pmod4\), \(k\ge5\), the minimum switch count can grow without bound as \(n\) increases.

**Proof.** Put \(m=n-1\), distinguish one direction \(s\), and partition the other \(m\) directions into \(r\) classes \(D_0,\ldots,D_{r-1}\), each containing at least \(2r+1\) directions. Write \(\tau(u)\) for the class of \(u\ne s\). Define the reversal-even triple function
\[
 h(a,b,c)=\mathbf1_{\{b>\min(a,c)\}},
 \qquad a,b,c\in\{0,\ldots,r-1\}.                            \tag{2}
\]

We first prove a word bound. If a word \(q=q_1\cdots q_m\) uses every class symbol at least \(2r+1\) times, its triple word
\[
 H_j=h(q_j,q_{j+1},q_{j+2}),\qquad 1\le j\le m-2,
\]
has \(\sigma(H)\ge2r-2\) changes. Otherwise its \(1\)'s form at most \(r-1\) runs. Within a run of \(1\)-centers, a nonincreasing step must be followed by a strictly decreasing step, by (2). Therefore the center values first increase strictly and then decrease strictly, with at most one repeated value at the peak. Each class symbol consequently occurs at most twice within each \(1\)-run and at most \(2r-2\) times among all \(1\)-centers. Yet each symbol occurs at least \(2r-1\) times among the interior positions \(q_2,\ldots,q_{m-1}\), so each must occur at a \(0\)-center. Two consecutive \(0\)-centers have equal symbols, since (2) then gives both \(q_{j+1}\le q_{j+2}\) and \(q_{j+2}\le q_{j+1}\). At least \(r\) different \(0\)-runs are therefore necessary, forcing at least \(2r-2\) changes. This contradiction proves the bound.

Write \(k=2t+1\). For an ordered \(k\)-tuple of distinct directions \(\pi=(u_1,\ldots,u_k)\), put
\[
 g(\pi)=
 \begin{cases}
 h(\tau(u_t),\tau(u_{t+1}),\tau(u_{t+2})),&s\notin\pi,\\
 0,&s\in\pi .
 \end{cases}                                                 \tag{3}
\]
The central triple reverses under reversal of \(\pi\), and \(h(a,b,c)=h(c,b,a)\). Thus \(g(\operatorname{rev}\pi)=g(\pi)\).

For each \(k\)-face \(F\), select one exterior direction \(e(F)\): take \(e(F)=s\) if \(s\) is exterior; otherwise take the least exterior direction in a fixed total order. Such a direction exists because \(n>k\), and its choice depends only on the set of free directions. Let \(z_{e(F)}(F)\) denote the bit fixed on \(F\) in that direction, and define
\[
 c(F,\pi)=z_{e(F)}(F)\oplus g(\pi).                             \tag{4}
\]
Reversing \(\pi\) preserves both summands; antipodal complementation toggles the selected exterior bit. Hence (1) holds.

Fix any full antipodal geodesic with root \(x\) and coordinate order \(p\), and delete \(s\) from \(p\), obtaining a permutation of the remaining directions. Replacing these by their class symbols gives a word \(q\) as above. Consider the consecutive ordinary \(k\)-window colors
\[
 G_i=h(q_{i+t-1},q_{i+t},q_{i+t+1}),
 \qquad 1\le i\le m-k+1.
\]
This word is obtained from \(H\) by removing \(t-1\) entries at each end, whence
\[
 \sigma(G)\ge (2r-2)-2(t-1)=2r-2t.                            \tag{5}
\]

Inserting \(s\) into the direction order removes at most \(k-1\) consecutive entries of \(G\), losing at most \(k\) adjacent comparisons. Every surviving ordered \(k\)-face omits \(s\), so its selected exterior direction is \(s\). Before the \(s\)-move its color is \(G_i\oplus x_s\); after that move its color is \(G_i\oplus(1-x_s)\). Complementing either surviving contiguous block preserves all its internal changes. Windows containing \(s\) can only increase the total count beyond these surviving comparisons. Thus
\[
 \sigma(c(P))\ge\sigma(G)-k
 \ge 2r-2t-k=2r-2k+1.
\]
The bound is independent of root and direction order. Taking \(k=5,r=6\) gives three compulsory changes with \(6(13)+1=79\) directions. \(\square\)

**Corollary.** The graded reversal-coherent proposal asserting that every odd-\(k\) ordered-face coloring satisfying \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\) and \(c(F,\operatorname{rev}\pi)=c(F,\pi)+\binom{k}{2}\pmod2\) admits a \((k-1)/2\)-splice full geodesic is false at \(k=5\). The arities \(k=1\) and \(k=3\) are unaffected by this construction.
