# Unbounded compulsory switches for every even ordered-face dimension

# Unbounded compulsory switches for every even ordered-face dimension

## Theorem

**Theorem.** Fix an even face dimension \(k=2m\ge4\) and an integer \(r\ge3\). In every dimension
\[
 n\ge \max\{k,\;r(2r+1)+1\},
\]
there is a legal binary coloring of **physical ordered \(k\)-faces** of \(Q_n\), obeying
\[
 c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi),
\]
such that **every** full antipodal geodesic has at least
\[
 \boxed{2r-2(k-1)}
 \tag{T}
\]
changes in its consecutive ordered-\(k\)-face color word. Thus every fixed even \(k\ge4\) admits \(\Omega(\sqrt n)\) compulsory changes, and the proposed \(k-1\)-switch hierarchy fails.

For example, \(k=4,r=6,n=79\) forces at least six changes (against the proposed three); \(k=6,r=8,n=137\) forces at least six (against the proposed five).

This result complements the sibling Subsection *Unbounded compulsory switches for every odd ordered-face dimension*. The even case has two middle positions that reversal exchanges; crucially, **one exterior sentinel simultaneously supplies the sign flip and chooses which central triple to use**. A preliminary two-sentinel construction proved a weaker bound, but the single-sentinel rule below supersedes it.

## 1. A reversal-even local-minimum word with many switches

Partition the \(n-1\) ordinary directions into \(D_0,\dots,D_{r-1}\) with \(|D_i|\ge2r+1\), and let \(\tau(u)=i\) for \(u\in D_i\). For classes \(a,b,c\), define
\[
 h(a,b,c)=\mathbf1_{\{b>\min(a,c)\}}=h(c,b,a). \tag{1}
\]
For any word \(q=(q_1,\dots,q_N)\) on these classes, using every ordinary direction once, define \(H_j=h(q_j,q_{j+1},q_{j+2})\) for \(1\le j\le N-2\). Then
\[
 \sigma(H)\ge2r-2. \tag{2}
\]
This is the multilevel local-minimum run lemma of *Unbounded mandatory color changes from multilevel local minima*. Here \(\sigma\) is the number of adjacent binary differences.

For completeness, if \(\sigma(H)\le2r-3\), there are at most \(r-1\) runs of 1-centers. At each 1-center \(j\), either \(q_j>q_{j-1}\) or \(q_j>q_{j+1}\). Across a consecutive run of such centers, once a difference \(q_{i+1}-q_i\) is nonpositive, all subsequent differences in the run are strictly negative. Hence the center values first increase, then decrease, with at most a two-letter plateau at their peak; each class occurs at most twice in any one-run. A class occurs at least \(2r-1\) times among all interior centers, so it has at least one 0-center. Two consecutive 0-centers must have the same class, since their inequalities imply both \(q_j\le q_{j+1}\) and \(q_{j+1}\le q_j\). Therefore the \(r\) classes require at least \(r\) different zero-runs, and the binary word must have at least \(2r-2\) changes, a contradiction.

## 2. One-sentinel coloring of genuine physical even faces

Adjoin one distinguished direction \(s\) to the ordinary classes. Fix a physical \(k=2m\) face \(F\) with free-coordinate order \(\pi=(u_1,\dots,u_{2m})\).

If \(s\notin\pi\), let \(z_s(F)\) be its fixed exterior \(s\)-coordinate, and define the two neighboring central triple statistics
\[
 L(\pi)=h(\tau(u_{m-1}),\tau(u_m),\tau(u_{m+1})),\qquad
 R(\pi)=h(\tau(u_m),\tau(u_{m+1}),\tau(u_{m+2})). \tag{3}
\]
Set
\[
 c(F,\pi)=
 \begin{cases}
 L(\pi),&s\notin\pi,\ z_s(F)=0,\\
 1\oplus R(\pi),&s\notin\pi,\ z_s(F)=1,\\
 1,&s=u_j,\ 1\le j\le m,\\
 0,&s=u_j,\ m+1\le j\le 2m.
 \end{cases} \tag{4}
\]
The clauses use the actual **fixed exterior bit of the physical face** and the order of its varying coordinates; they are independent of the traversing corner. All cases are disjoint and exhaustive.

**Legality.** Reversal of a \(2m\)-tuple interchanges its left and right central triples, so by reversal-evenness of \(h\),
\[
 L(\operatorname{rev}\pi)=R(\pi),\qquad R(\operatorname{rev}\pi)=L(\pi). \tag{5}
\]
If \(s\) is exterior, antipodal complementation changes its fixed bit \(z\) to \(1-z\). The first clause of (4) becomes the second applied to the reversed tuple, and conversely; by (5) the selected \(h\)-value stays the same while the leading bit complements. Hence \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\). If \(s\) is free, reversal sends its position \(j\) to \(2m+1-j\), interchanging the two constant values 1 and 0. Legality holds for every ordered physical \(k\)-face.

## 3. Arbitrary insertion and exact comparison survival

Fix **any** cube root \(x\) and **any** direction permutation \(p\) defining a full antipodal geodesic. Delete \(s\), leaving the ordinary class word \(q\), split at the deletion position into a prefix \(A\) of length \(a\) and suffix \(B\) of length \(b\), where \(a+b=N=n-1\).

Within each ordinary block the traversed \(s\)-coordinate is constant. Therefore consecutive \(k\)-windows avoiding \(s\) have colors given by consecutive triple statistics of \(H\), with one fixed index offset (left central triple if \(z_s=0\), right central triple if \(z_s=1\)) and a fixed XOR sign. Their **adjacent comparisons are precisely the corresponding adjacent comparisons of \(H\)**. The offset and possible complementation may differ between \(A\) and \(B\), but that affects only the missing seam comparisons.

A block of \(a\) ordinary directions contains \(\max(0,a-k)\) adjacent comparisons between two fully contained \(k\)-windows; similarly the suffix contributes \(\max(0,b-k)\). All these comparisons are witnessed by actual adjacent physical faces and remain unchanged relative to distinct comparisons of the original \(H\). Since \(H\) has \(N-3\) comparisons, at most
\[
 M=(N-3)-\max(0,a-k)-\max(0,b-k) \tag{6}
\]
original comparisons are unwitnessed.

If \(a,b\ge k\), then \(M=2k-3\). In that case all \(k\) windows involving \(s\) occur consecutively, with \(s\) occupying positions \(k,k-1,\dots,1\). By the last two clauses of (4), their color word is
\[
 \underbrace{00\cdots0}_{m}\underbrace{11\cdots1}_{m},
\]
and contributes **one additional genuine switch**, regardless of root, interleaving, and ordinary colors. The switch is distinct from all surviving ordinary-block comparisons.

If \(a<k\le b\), (6) gives \(M=a+k-3\le2k-4\). The symmetric case \(b<k\le a\) is identical. If both \(a,b<k\), then \(N\le2k-2\), and \(M=N-3\le2k-5\). Thus in **every** case the switches witnessed in the ordinary blocks, supplemented when necessary by the internal sentinel switch, give
\[
 \begin{aligned}
 \sigma(\text{full physical }k\text{-window colors})
 &\ge \sigma(H)-(2k-4)\\
 &\ge (2r-2)-(2k-4)=2r-2(k-1).
 \end{aligned} \tag{7}
\]
No changes from different components are added speculatively: every switch counted is an explicit comparison of adjacent physical windows. This proof works for every sentinel position and every ordering of the remaining coordinates, including arbitrary interleaving of all \(r\) classes. The starting root was arbitrary, establishing (T).

## 4. Scope and NORI1/NORI2 rotation

The odd-\(k\) theorem and (T) together give a **uniform unbounded-switch construction for all fixed \(k\ge3\)**, with the same lower bound \(2r-2(k-1)\) in dimension \(n\ge r(2r+1)+1\). For fixed \(k\), choosing \(r\) on the order of \(\sqrt{n/2}\) yields \(\sqrt{2n}-O(k)\) compulsory changes.

The construction genuinely needs at least three ordered free directions to define the local-minimum obstruction. The distinct case \(k=2\) has a symmetric **pair** statistic; the sibling result *NORI2 sentinel barrier and exact one-switch examples* proves that every one-sentinel symmetric-pair coloring of the analogous form admits a one-switch full geodesic. For \(k=1\), if an antipodally odd physical-edge geodesic has one switch, rotating its direction sequence at the switch and replacing the old prefix by its antipodal copy yields a monochromatic full geodesic. These lower-dimensional features explain why the present theorem does not settle NORI1 or unrestricted NORI2.

## 5. Independent stress tests

A separately written physical-mask evaluator checked 2,000 random physical ordered \(k\)-faces for legality and 300 sampled full rooted geodesics, including the sorted direction order, for each \((k,r)=(4,6),(6,8),(8,10),(10,13)\). Respectively, \((n,\text{proved minimum},\text{sampled minimum})\) was \((79,6,10),(137,6,15),(211,6,19),(352,8,24)\). These tests additionally derive each ordinary \(k\)-face's exterior \(s\)-bit from the path's actual traversed vertex. The proof (1)–(7) is unconditional and independent of testing.
