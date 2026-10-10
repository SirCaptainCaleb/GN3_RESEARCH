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
