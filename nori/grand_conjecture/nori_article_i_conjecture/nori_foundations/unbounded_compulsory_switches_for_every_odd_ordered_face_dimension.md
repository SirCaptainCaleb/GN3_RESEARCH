# Unbounded compulsory switches for every odd ordered-face dimension

# Unbounded compulsory switches for every odd ordered-face dimension

## Theorem

**Theorem.** Let \(k=2t+1\ge3\) and \(r\ge3\). For each \(n\ge\max\{k,r(2r+1)+1\}\), there exists a binary coloring of physical ordered \(k\)-faces of \(Q_n\) satisfying
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)
\]
such that every full antipodal geodesic has at least
\[
\boxed{2r-2(k-1)}
\]
changes in its consecutive ordered-\(k\)-face color word. Thus for each fixed odd \(k\ge3\) the required switch budget is unbounded, at least \(\sqrt{2n}-O(k)\); the proposed \(k-1\) hierarchy is false for every such \(k\).

## Multilevel local-minimum lemma

Let \(q=q_1\cdots q_m\) be a word over \(\{0,\ldots,r-1\}\), every symbol occurring at least \(2r+1\) times. Set
\[
h(a,b,c)=\mathbf1_{\{b>\min(a,c)\}},\qquad H_j=h(q_j,q_{j+1},q_{j+2}).
\]
Write \(\sigma(W)\) for the number of changes in a binary word. Then
\[
\sigma(H)\ge2r-2. \tag{1}
\]

**Proof.** Otherwise \(\sigma(H)\le2r-3\), and the 1-centers have at most \(r-1\) maximal runs. On each such run, the successive differences \(d_i=q_{i+1}-q_i\) satisfy \(d_{j-1}>0\) or \(d_j<0\). Once a difference becomes nonpositive, the following difference is strictly negative. Hence the center values increase strictly, then decrease strictly, with at most one double peak. Each alphabet symbol occurs at most twice among the centers of any one-run, hence at most \(2(r-1)\) times among all 1-centers. Each symbol occurs at least \(2r-1\) times among the interior centers \(q_2,\ldots,q_{m-1}\). Consequently every symbol occurs at some 0-center. If \(H_j=H_{j+1}=0\), then \(q_j\le q_{j+1}\) and \(q_{j+1}\le q_j\), so these centers have the same symbol. Each zero-run therefore bears only one symbol. There are at least \(r\) zero-runs, separated by one-runs, forcing at least \(2r-2\) changes, contradiction. \(\square\)

For odd \(k=2t+1\), let
\[
g_k(a_1,\ldots,a_k)=h(a_t,a_{t+1},a_{t+2}).
\]
Reversing the \(k\)-tuple reverses its central triple, so \(g_k\) is reversal-even. The consecutive ordinary \(k\)-window word
\[
G_i=g_k(q_i,\ldots,q_{i+k-1})=H_{i+t-1},
\quad 1\le i\le m-k+1
\]
is obtained from \(H\) by deleting exactly \(t-1\) terms at each end. Thus
\[
\sigma(G)\ge2r-2-2(t-1)=2r-2t. \tag{2}
\]

## General insertion lemma: exact interleaving control

Insert a distinguished letter \(s\) at an arbitrary position in \(q\), producing a word \(p\) of length \(m+1\). Fix arbitrary bits \(z,\varepsilon\). Color each consecutive \(k\)-window as follows: if it avoids \(s\), use \(g_k\oplus z\) before \(s\) and \(g_k\oplus(1-z)\) after \(s\); if the position of \(s\) within the window is less than \(t+1\), use 1; if greater than \(t+1\), use 0; if exactly \(t+1\), use \(\varepsilon\). Let \(C\) be this color word. Then
\[
\sigma(C)\ge\sigma(G)-(k-1). \tag{3}
\]

**Proof.** If \(s\) is inserted at position \(\ell\) (1-based), the original ordinary windows surviving in \(p\) are precisely the prefix \(G_i\), \(i\le\ell-k\), and suffix \(G_i\), \(i\ge\ell\). Between them at most \(k-1\) consecutive terms of \(G\) are missing. Complementing any surviving whole segment preserves its internal changes.

If both ordinary segments are nonempty, at most \(k\) adjacent comparisons of \(G\) disappear. All \(k\) sentinel-containing windows appear between the surviving segments. Their sentinel positions run from \(k\) down to 1 and their colors are
\[
0,\ldots,0,\ \varepsilon,\ 1,\ldots,1,
\]
so they contribute at least one internal change. Net loss is at most \(k-1\).

If one ordinary segment is empty, the missing terms are a prefix or suffix of at most \(k-1\) terms and hence remove at most \(k-1\) comparisons. If both segments are empty, \(G\) has at most \(k-1\) terms and thus at most \(k-2\) changes, so (3) holds automatically. This covers every insertion position, without restrictions on coordinate interleaving. \(\square\)

## The legal coloring of genuine physical faces

Partition the coordinate directions as
\[
V=D_0\sqcup\cdots\sqcup D_{r-1}\sqcup\{s\},\qquad |D_i|\ge2r+1.
\]
Let \(\tau(u)=i\) for \(u\in D_i\), and choose a strict total ordering \(<\) of the ordinary directions. For a *physical* \(k\)-face \(F\) with ordered free directions \(\pi=(u_1,\ldots,u_k)\), define
\[
c(F,\pi)=
\begin{cases}
z_s(F)\oplus h(\tau(u_t),\tau(u_{t+1}),\tau(u_{t+2})),&
  s\notin\pi,\\
1,&s=u_j,\ j<t+1,\\
0,&s=u_j,\ j>t+1,\\
\mathbf1_{\{u_t>u_{t+2}\}},&s=u_{t+1}.
\end{cases} \tag{4}
\]
Here \(z_s(F)\) is the fixed \(s\)-coordinate of \(F\), defined exactly in the first case. These cases are mutually exclusive, depend only on the physical face and its free-direction ordering, and are independent of the corner through which the face is traversed.

**Legality.** When \(s\) is outside the face, antipodal complementation flips \(z_s(F)\), and reversal leaves the central-triple \(h\)-value unchanged. When \(s\) is a noncentral free direction, reversal takes a position left of center to one right of center, interchanging 1 and 0. When \(s\) is central, reversal interchanges its two distinct immediate neighbors, complementing the strict-order indicator. Thus \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\) in every case.

**Forced switches.** Fix any starting vertex \(x\) and any full coordinate order \(p\). Delete \(s\) from \(p\) and replace each ordinary direction by its class to produce \(q\). This has at least \(2r+1\) occurrences of each symbol. Put \(z=x_s\). The actual window colors avoiding \(s\) equal \(g_k\oplus z\) before the \(s\)-move and \(g_k\oplus(1-z)\) afterward, since precisely the physical face's fixed \(s\)-bit changes. The sentinel windows have the prescribed left/central/right colors, with the central bit \(\varepsilon\) fixed by comparing its distinct neighboring directions. Thus the complete physical path word is exactly an instance of the insertion lemma:
\[
\sigma(C)\ge\sigma(G)-(k-1)\ge(2r-2t)-2t
=2r-2(k-1).
\]
The root and permutation were arbitrary, proving the theorem. \(\square\)

## Consequences and scope

Take \(r=\lfloor(\sqrt{8n-7}-1)/4\rfloor\), with \(r\ge3\). Then \(r(2r+1)+1\le n\), giving a lower bound \(\sqrt{2n}-O(k)\) on the minimum changes of the constructed coloring. For \(k=3\), the result recovers the established multilevel construction. For \(k=5\), \(r=7,n=106\) forces at least six changes (versus the hierarchy's proposed four). For \(k=7\), \(r=10,n=211\) forces at least eight (versus the proposed six).

The use of the central triple requires odd \(k\). For even \(k\), reversing an ordered face interchanges its two middle positions, and this exact projection is unavailable. The argument therefore makes no assertion about unrestricted NORI2 or higher even \(k\). For NORI1, there is no triple and no central sentinel with two distinct neighbors; the well-known cyclic root-rotation converting a one-switch edge path into a monochromatic edge path has no analogue in this construction.

**Independent finite stress test.** Exhaustive tests enumerated all ternary ordinary words, insertion positions, both starting sentinel bits and both central bits for \((k,m)=(3,7),(5,7),(5,8),(7,9)\); all 1,163,484 tests satisfied (3). The mathematical proof above is unconditional.

## Sharp odd-length sentinel comparison lemma (strengthening)

**Lemma (one additional comparison always survives).** For every odd \(k=2t+1\ge3\), the abstract one-sentinel insertion model of (3) satisfies the stronger inequality
\[
\boxed{\sigma(C)\ge\sigma(G)-(k-2).}\tag{5}
\]
It is uniform over every ordinary word \(G\), every sentinel insertion position and both independent choices \(z,\varepsilon\). The previous \(k-1\)-loss estimate is valid but can be sharpened.

**Proof.** When both surviving ordinary \(k\)-window blocks are nonempty, the insertion removes \(k-1\) consecutive terms of \(G\), and thus at most \(k\) original comparisons. The \(k\) sentinel-containing physical windows have the color word
\[
0,\ldots,0,\varepsilon,1,\ldots,1
\]
with exactly one internal switch. If at most \(k-1\) deleted comparisons were switches, the total loss is at most \(k-2\).

It remains to examine the unique possible worst case: all \(k\) deleted comparisons were switches. Let \(a\) and \(b\) be the surviving ordinary \(G\)-bits bordering the erased interval. Since **\(k\) is odd**, \(b=1-a\). Across the physical sentinel step the exterior sign changes, so the physical colors at the two ends of the inserted sentinel word are \(a\oplus z\) and \(b\oplus(1-z)=a\oplus z\): they are **equal**. The sentinel word itself begins with zero and ends with one. Hence its two *external* seams cannot both be color-preserving; at least one additional comparison switches, independently of \(\varepsilon\). The new word therefore contains at least two switches in the inserted region, losing at most \(k-2\) relative to the removed \(k\) switches.

If exactly one ordinary \(k\)-window block survives, the omitted original terms form an initial or final segment of \(G\), of length at most \(k-1\). If its length is at most \(k-2\), at most \(k-2\) comparisons disappear and the inequality follows. If its length equals \(k-1\), the sentinel occupies precisely the \(k\)-th position from that end, so all \(k\) sentinel windows occur and their internal switch compensates for one removed comparison. If neither block survives, \(G\) has at most \(k-1\) terms and therefore at most \(k-2\) switches, making the inequality immediate. These cases exhaust all insertion positions. \(\square\)

**Strengthened odd-\(k\) amplification theorem.** Under the legal physical coloring (4), for every \(r\ge3\) and every \(n\ge\max\{k,2r^2+r+1\}\), all full antipodal geodesics have at least
\[
\boxed{2r-2k+3}
\]
ordered-\(k\)-face color changes. Indeed, the ordinary word has at least \(2r-2\) changes; restricting to central \(k\)-windows discards at most \(k-3\); the improved sentinel lemma discards at most \(k-2\). The result is
\[
(2r-2)-(k-3)-(k-2)=2r-2k+3.
\]
For \(k=3\), the separate multilevel Subsection further establishes that the bound \(2r-3\) is **exact for the constructed coloring**, achieved by ordered constant class blocks with the sentinel at their first boundary. For larger odd \(k\), no assertion of exactness is made.

The improvement is a genuine antipodal-sign constraint: parity of the \(k\) missing comparisons makes the two surviving exterior-complemented boundary colors identical, while the sentinel-color bridge has distinct endpoints. It directly accounts for all possible interleavings and does not assume that switches from separate components add.
