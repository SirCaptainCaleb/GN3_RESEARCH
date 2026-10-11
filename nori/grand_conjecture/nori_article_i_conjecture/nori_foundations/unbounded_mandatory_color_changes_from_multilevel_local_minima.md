# Unbounded mandatory color changes from multilevel local minima

# Unbounded obligatory switches in legal ordered-three-face colorings

## Main theorem

**Theorem.** For every integer \(r\ge 3\) and every \(n\ge r(2r+1)+1\), there is a binary coloring of the *physical ordered three-faces* of \(Q_n\) satisfying
\[
c(\bar F,(w,v,u))=1-c(F,(u,v,w))
\]
such that **every** full antipodal geodesic has at least \(2r-4\) changes among its ordered-three-face colors. Consequently, no dimension-independent finite bound on the number of color changes can hold for all legal colorings. In particular, the worst-case minimum number of changes is at least
\[
2\left\lfloor\frac{\sqrt{8n-7}-1}{4}\right\rfloor-4
=\sqrt{2n}-O(1)
\qquad(n\ge 22).
\]
For example, the construction forces at least four changes in every dimension \(n\ge37\), and at least six in every dimension \(n\ge56\).

The proof uses an elementary run-count lemma, followed by a one-coordinate antipodal-odd lift. It has no computational premise.

## 1. A multilevel, reversal-even obstruction

Fix \(r\ge 2\) and a finite word \(q=(q_1,\ldots,q_m)\) on the linearly ordered alphabet \(\{0,\ldots,r-1\}\). Suppose **every** letter occurs at least \(2r+1\) times. Define the binary word indexed by interior positions \(2\le j\le m-1\) by
\[
H_j=\mathbf1_{\{q_j>\min(q_{j-1},q_{j+1})\}}.
\tag{1}
\]
For a binary word \(W\), write \(\sigma(W)\) for its number of adjacent changes.

**Lemma 1 (sharp run-count bound).** The word \(H\) has at least \(2r-2\) changes. The bound is sharp.

**Proof.** Suppose \(\sigma(H)\le2r-3\). Then \(H\) has at most \(r-1\) maximal runs of ones.

On any consecutive run of one-centers \(H_j=1\), set \(d_i=q_{i+1}-q_i\). The condition at center \(j\) says
\[
d_{j-1}>0\quad\hbox{or}\quad d_j<0.
\tag{2}
\]
In particular, whenever \(d_{j-1}\le0\), (2) forces \(d_j<0\). Along the centers of this one-run, the letter values consequently increase strictly and then decrease strictly, with at most a two-letter plateau at the peak. Thus **each particular letter occurs at most twice among the centers of a single one-run**. Across all the at most \(r-1\) one-runs, a given letter occupies at most \(2(r-1)\) interior positions having \(H_j=1\).

Every letter appears at least \(2r+1\) times in \(q\), and only the first and last positions are excluded from the interior-center sequence. Hence each letter occupies at least \(2r-1>2(r-1)\) interior centers, and so must occur at some center with \(H_j=0\).

If two consecutive centers both have color zero, (1) gives \(q_j\le q_{j+1}\) and \(q_{j+1}\le q_j\), hence \(q_j=q_{j+1}\). Therefore each maximal zero-run consists of centers carrying one and the same letter. Since all \(r\) distinct letters occur at zero-centers, there are at least \(r\) distinct zero-runs. Between any two successive zero-runs lies a nonempty one-run, creating a zero-to-one and a one-to-zero change. Thus \(\sigma(H)\ge 2(r-1)\), contradicting the assumption.

For sharpness, concatenate constant blocks of the letters in increasing order, each of length at least \(2r+1\). Each upward block boundary creates precisely one isolated one-center, and the other centers have color zero. There are \(r-1\) such isolated one-centers and exactly \(2r-2\) switches. \(\square\)

The triple rule
\[
h(a,b,c)=\mathbf1_{\{b>\min(a,c)\}}
\tag{3}
\]
is reversal-even: \(h(a,b,c)=h(c,b,a)\).

## 2. The distinguished-coordinate insertion bound

Adjoin one new letter \(s\) to \(q\), inserted at any of its \(m+1\) possible positions. Fix arbitrary \(z,\varepsilon\in\{0,1\}\). Color every consecutive triple avoiding \(s\) by its \(h\)-value XOR \(z\) if it occurs before \(s\), and XOR \(1-z\) if after \(s\). Color the triples with \(s\) at their final, middle, or initial position by \(0,\varepsilon,1\), respectively.

**Lemma 2 (two-switch loss).** If the original \(H\) has \(T\) changes, every resulting \((m-1)\)-term triple-color word has at least \(T-2\) changes, independently of the insertion position and of \(z,\varepsilon\).

**Proof.** The ordinary triples surviving the insertion form a prefix and a suffix of the original \(H\); at most two *consecutive* terms of \(H\) are omitted. Within either surviving segment, XOR by a constant preserves all adjacent changes. Removing two consecutive terms deletes at most three adjacent comparisons. If all three \(s\)-containing triples occur, they appear in the order \((u,v,s),(u,s,v),(s,u,v)\) and have color word \((0,\varepsilon,1)\), which contributes at least one further change. Therefore the total is at least \(T-3+1=T-2\). If fewer than three \(s\)-containing triples occur, \(s\) occupies one of the first two or last two positions. In that case at most one ordinary \(H\)-term is omitted, and it is an endpoint; at most one original comparison is lost. The surviving changes alone are therefore at least \(T-1\). \(\square\)

## 3. A legal physical coloring with unbounded defect

Choose a partition
\[
V=D_0\sqcup\cdots\sqcup D_{r-1}\sqcup\{s\},
\qquad |D_i|\ge2r+1,
\tag{4}
\]
of the \(n\) coordinate directions. Write \(\tau(u)=i\) for \(u\in D_i\), and fix any strict total ordering \(<\) of the ordinary directions \(V\setminus\{s\}\).

For each **physical** three-face \(F\) with ordered free directions \((u,v,w)\), set
\[
c(F,(u,v,w))=
\begin{cases}
z_s(F)\oplus h(\tau(u),\tau(v),\tau(w)),&s\notin\{u,v,w\},\\
1,&u=s,\\
0,&w=s,\\
\mathbf1_{\{u>w\}},&v=s.
\end{cases}
\tag{5}
\]
Here \(z_s(F)\) is the fixed \(s\)-coordinate of \(F\) in the first case. The four cases are mutually exclusive, depend only on the physical face and its ordered free directions, and are independent of the traversing corner.

The coloring is antipodal-reversal-odd. On a triple avoiding \(s\), complementation flips the fixed \(s\)-bit and reversal leaves \(h\) invariant. For a triple with \(s\) at an endpoint, reversal interchanges the complementary constants 1 and 0. For \(s\) in the middle, reversal exchanges two distinct outside directions and therefore flips the strict-order indicator.

Now fix **any** root and **any** full direction order. Delete the one occurrence of \(s\) and replace every other direction by its class \(\tau\). By (4), the resulting word satisfies Lemma 1, so its ordinary triple-color word has at least \(T=2r-2\) changes. The actual physical three-face colors along the original full path are precisely those prescribed in Lemma 2: the fixed \(s\)-bit before the \(s\)-move is its starting bit \(z\), and after the move it is \(1-z\); the middle-\(s\) bit is one definite \(\varepsilon\in\{0,1\}\) selected by the two neighboring directions. Lemma 2 therefore gives at least
\[
T-2\ge2r-4
\]
changes along **every** full antipodal geodesic. This proves the theorem. \(\square\)

## Consequence and scope

The previously published binary-class sentinel coloring disproves one-change NORI for every \(n\ge9\), but gives a dimension-independent lower bound of two changes. The multilevel construction (5) proves a qualitatively different statement: **every proposed universal bounded-switch replacement is also false**, with a quantitative \(\Omega(\sqrt n)\) lower bound. The positive \(Q_5\) and \(Q_6\) results and the undecided \(Q_7,Q_8\) cases are unaffected. The ordinary-word lemma is sharp; no sharpness for the final geodesic bound is asserted.

## Sharp improvement: a one-switch insertion loss and exact extremal value

**Lemma (sharp ternary sentinel insertion).** In the insertion construction of Lemma 2, for *every* ordinary class word \(q\), every sentinel position and both independent bits \(z,\varepsilon\), the full color word \(C\) satisfies
\[
\boxed{\sigma(C)\ge \sigma(H(q))-1.}\tag{6}
\]
In particular, the earlier two-switch insertion-loss estimate is valid but suboptimal.

**Proof.** If the insertion has two nonempty surviving ordinary-window segments, it deletes two adjacent letters of \(H\), eliminating at most three adjacent comparisons. Between the surviving physical segments there are three sentinel-containing windows, whose colors are \(0,\varepsilon,1\); their internal switch count is exactly one. If fewer than three of the removed comparisons change color, the claimed loss of at most one follows immediately.

Suppose all three removed comparisons do change color. Let \(a\) and \(b\) be the surviving \(H\)-bits immediately before and after the deleted pair. Three successive differences give \(b=1-a\). The actual physical color immediately before the sentinel windows is \(a\oplus z\), while the physical color immediately afterward is \(b\oplus(1-z)=a\oplus z\). These two boundary colors are *equal*. The sentinel windows start at color zero and end at color one. Therefore at least one of their **two external boundary comparisons** must also change, irrespective of \(\varepsilon\). At least two new comparisons change (one inside and one outside the sentinel run), compensating for three removed changes. Thus (6) holds.

If one ordinary segment is empty, the sentinel occupies one of the first three or final three direction slots. In the first or last two slots, at most one original comparison is removed. In the third or third-last slot, at most two original comparisons are removed, while all three sentinel windows occur and contribute one switch. In each case the net loss is at most one. These possibilities exhaust all positions. \(\square\)

**Theorem (exact compulsory defect of the multilevel family).** For every \(r\ge3\) and every partition of the ordinary directions into \(r\) nonempty ordered classes with \(|D_i|\ge2r+1\), the legal physical coloring (5) has
\[
\boxed{\min_{x,p}\sigma(C(x,p))=2r-3.}\tag{7}
\]
Consequently, for every \(n\ge 2r^2+r+1\) a legal NORI3 coloring exists forcing at least \(2r-3\) switches on *every* full antipodal geodesic. The dimension-uniform lower bound improves to
\[
2\left\lfloor\frac{\sqrt{8n-7}-1}{4}\right\rfloor-3
=\sqrt{2n}-O(1).
\]
In particular, this family has exact minimum three in \(Q_{22}\), five in \(Q_{37}\), and seven in \(Q_{56}\).

**Proof.** Lemma 1 proves \(\sigma(H(q))\ge2r-2\) for every coordinate-class permutation. The sharp insertion lemma now gives \(\sigma(C)\ge2r-3\), uniformly in starting root and full coordinate order.

For equality, choose the full coordinate direction order
\[
(D_0\text{ in any order}),\ s,\ (D_1\text{ in any order}),\ldots,(D_{r-1}\text{ in any order}),
\]
and take initial sentinel bit \(z=0\). The ordinary \(h\)-word is zero inside each constant class block and has exactly one isolated 1 at each ascending class boundary. The insertion of \(s\) removes the first such boundary: the surviving windows before \(s\) are all zero, the three \(s\)-containing windows are \(0,\varepsilon,1\), and the surviving ordinary windows after \(s\) start at one and have two changes at each of the remaining \(r-2\) class boundaries. The total is \(1+2(r-2)=2r-3\), for either value of \(\varepsilon\). This is an actual full antipodal geodesic from any root with \(x_s=0\). Thus equality holds for the physical coloring. \(\square\)

**Scope.** The improvement exploits a physical sign flip *across* the sentinel together with the forced opposite endpoint colors of the sentinel windows. Counting deleted switches without these two features loses one unit of sharpness. No cancellation or noninterleaving assumption is made.


## Consolidated independent proof: two-sentinel antichain

Previous Subsection `logarithmic_monochromatic_path_obstruction_and_near_linear_switch_amplification`, exact original composition version 1.

# Logarithmic monochromatic geodesics and near-linear compulsory switches

**Theorem (two-sentinel antichain construction).** Fix \(k\ge3\) and \(n\ge k+2\). Put \(N=n-2\) and
\[
m=\min\{d\ge2:\binom d{\lfloor d/2\rfloor}\ge N\}.
\]
There is a legal binary coloring of ordered PHYSICAL \(k\)-faces of \(Q_n\) such that every monochromatic coordinate-distinct geodesic has at most \(3m+3k-4\) edges, while every full antipodal geodesic has at least
\[
\boxed{\max\{0,\lceil(n-3k+1)/(m-1)\rceil-3\}}
\]
switches. In particular, for each fixed \(k\ge3\), the longest monochromatic geodesic can be \(O(\log n)\), and the compulsory switch count can be \((1-o(1))n/\log_2n\).

**Rank-map proof.** Choose \(N\) distinct equal-size subsets \(A_u\subseteq[m]\), indexed by ordinary directions. Define \(\lambda(u,v)=\min(A_u\setminus A_v)\) for \(u\ne v\). For distinct \(u,v,w\), the label \(\lambda(u,v)\notin A_v\), whereas \(\lambda(v,w)\in A_v\), so these two labels are distinct. Put
\[
h(u,v,w)=\mathbf1_{\{\lambda(u,v)<\lambda(v,w)\}}.
\]
A monochromatic run of consecutive \(h\)-triples forces all successive directed-pair labels to strictly increase (color 1) or decrease (color 0). There are only \(m\) possible labels, so such a run contains at most \(m-1\) triple windows. The same statement holds for the reverse rule \(h(w,v,u)\), by reading the word backward.

**Physical coloring and legality.** Adjoin distinct sign and selector directions \(s,t\). For an ordered physical \(k\)-face \((F,\pi)\) with neither sentinel free, let \(g(\pi)=h(\pi_1,\pi_2,\pi_3)\). Assign color \(z_s(F)\oplus g(\pi)\) if \(z_t(F)=0\), or \(z_s(F)\oplus g(\operatorname{rev}\pi)\) if \(z_t(F)=1\). If at least one sentinel is free, assign \(\mathbf1_{\{\pi_1>\pi_k\}}\) using an arbitrary fixed strict order of all coordinate directions. The rule depends only on the genuine physical face and its free-direction order; it never depends on the traversing corner.

Under antipodal reversal both exterior sentinel bits flip, and reversal swaps the two selector alternatives. Thus the chosen \(g\)-term remains unchanged and the XOR sign flips. If a sentinel is free, the distinct first and last ordered free directions exchange, complementing their strict-order comparison. Hence for EVERY physical ordered face,
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi).
\]

**Monochromatic length.** Delete the at most two sentinel steps from any direction-distinct monochromatic geodesic, splitting ordinary directions into at most three contiguous blocks. Within each block both sentinel bits are fixed. The colors of consecutive ordinary \(k\)-windows therefore reproduce, up to one constant XOR, consecutive \(h\)-triples on either the first three or reversed last three directions of each window. A block of \(b\ge k\) ordinary directions contains \(b-k+1\) such windows, so \(b-k+1\le m-1\), or \(b\le m+k-2\). A shorter block obeys this bound trivially. Adding at most three blocks and two sentinels yields length at most \(3(m+k-2)+2=3m+3k-4\).

**Compulsory switches, with arbitrary interleaving.** In a full \(n\)-direction geodesic, let the at most three ordinary blocks have lengths \(b_i\), with \(\sum_i b_i=n-2\). Block \(i\) contains \(w_i=\max(0,b_i-k+1)\) actual consecutive ordinary physical \(k\)-window colors. Each monochromatic run among those \(w_i\) colors has at most \(m-1\) terms, so its INTERNAL physically adjacent comparisons force at least \(w_i/(m-1)-1\) switches. Those internal comparisons from distinct blocks are disjoint genuine comparisons of the full geodesic's color word; NO addition or noncancellation assumption is made about intervening sentinel windows. Summing gives
\[
\sigma(P)\ge\frac{\sum_i w_i}{m-1}-3
\ge\frac{n-2-3(k-1)}{m-1}-3.
\]
Take a ceiling and the trivial nonnegative bound. Stirling gives \(m=\log_2n+O(\log\log n)\), completing the theorem.

**Relation to the scrapbook snake bound.** The boundary 3-tournament \(\sqrt n\) proof uses reversal antisymmetry at the SAME triple to orient a tournament of terminal-pair competitors. The active NORI axiom relates different ANTIPODAL physical faces instead. Two exterior coordinates legally encode the arbitrary rank-comparison \(h\) and its reverse in complementary charts, refuting a universal \(\Omega(\sqrt n)\) monochromatic-geodesic claim already for NORI3. The universal positive longest-path lower bound and matching extremal switch upper bound are still open; NORI1 and NORI2 are not addressed.

**Verification.** Independently coded tests checked antipodal-reversal legality on every ordered physical \(k\)-face in dimensions \(5\) through \(8\), \(3\le k\le5\) where applicable, using actual exterior bitmasks. Further checks covered randomly rooted coordinate-distinct paths and verified \(\lambda(u,v)\ne\lambda(v,w)\) for ordinary-set sizes \(3\) through \(119\). The proof above is independent of these tests.

## Consolidated independent proof: even-face theorem

Previous Subsection `unbounded_compulsory_switches_for_every_even_ordered_face_dimension`, exact original composition version 2.

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

## Consolidated independent proof: odd-face theorem

Previous Subsection `unbounded_compulsory_switches_for_every_odd_ordered_face_dimension`, exact original composition version 2.

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
