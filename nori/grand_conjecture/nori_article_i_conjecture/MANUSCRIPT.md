# Article I — Antipodal-reversal-odd geodesic colorings of the cube

## Article setting and orientation

Let \(Q_n=\mathbb F_2^n\). An ordered three-face is a physical coordinate face \(F\) together with an ordering \(\pi=(a,b,c)\) of its three free directions. Its color is independent of the traversing corner within \(F\). The active NORI law is \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). A full antipodal geodesic crosses all \(n\) coordinates once and carries the \(n-2\) ordered-face colors of its consecutive three-move windows. It is *good* if this word has at most one change.

*Full Article composition: [source manuscript](../nori_article_i_conjecture.md).*

## Foundational closure theorems and rooted obstructions

Let \(Q_n=\mathbb F_2^n\). An ordered three-face is a physical coordinate face \(F\) together with an ordering \(\pi=(a,b,c)\) of its three free directions. Its color is independent of the traversing corner within \(F\). The active NORI law is \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). A full antipodal geodesic crosses all \(n\) coordinates once and carries the \(n-2\) ordered-face colors of its consecutive three-move windows. It is *good* if this word has at most one change.

*Full Section composition: [source manuscript](nori_foundations.md).*

### Dimension-five closure and cyclic windows

# Dimension five and the sharpness of unrestricted closure

An ordered three-face consists of a three-dimensional cube face and an ordering of its free coordinate directions. The color of this object may depend on all exterior fixed bits, but is independent of the traversal corner within the face. An antipodal geodesic in \(Q_n\) changes each coordinate exactly once, and its \(n-2\) consecutive ordered-three-face colors form its color word.

**Theorem 1 (unrestricted \(Q_5\)).** Every binary coloring of ordered three-faces of \(Q_5\) admits an antipodal geodesic whose three-window color word changes at most once.

**Proof.** If every five-direction geodesic failed, each color word would be \(010\) or \(101\), hence its first and third colors would agree. Fix a coordinate order \((a,b,c,d,e)\) and vary the starting bits. The first face color depends only on the fixed \(d,e\)-bits, while the last face color depends only on the independent \(a,b\)-bits, toggled before the third window. Equality for all four exterior bits forces both colors to be constant functions of their face positions. Since every ordered triple occurs as the first window of some full order, the entire coloring is position-independent, \(c(F,(a,b,c))=h(a,b,c)\). Failure in every order now gives \(h(a,b,c)\ne h(b,c,d)\) for every sequence of four distinct coordinates. Applied around the five cyclic rotations of \((a,b,c,d,e)\), this alternates five binary labels around an odd cycle, which is impossible. \(\square\)

**Theorem 2 (sharpness without antipodal oddness).** For every \(n\ge6\) there exists a face-independent binary coloring of ordered three-faces of \(Q_n\) such that *every* antipodal geodesic has at least two color changes.

**Proof.** Partition the coordinate directions as \(V=A\sqcup B\), with \(|B|=2\), and set
\[
h(a,b,c)=
\begin{cases}
1,&b\in A\ \text{and}\ (a\in B\text{ or }c\in B),\\
0,&\text{otherwise}.
\end{cases}
\]
Color \((F,(a,b,c))\) by \(h(a,b,c)\), independently of \(F\). Fix a full direction order \((p_1,\ldots,p_n)\). For \(2\le j\le n-1\), the window centered at \(p_j\) has color \(1\) precisely when \(p_j\in A\) and at least one of its immediate neighbors belongs to \(B\). Denote the resulting word indexed by centers \(j=2,\ldots,n-1\) by \(w\).

The word \(w\) contains a \(1\). Indeed, if the first \(B\)-position is \(i\ge3\), the preceding position \(i-1\) is an eligible interior \(A\)-center adjacent to \(B\). If \(i=2\), use center \(3\), unless the other \(B\) lies at \(3\), in which case use center \(4\). If \(i=1\), use center \(2\), unless the other \(B\) lies at \(2\), in which case use center \(3\). These positions exist and lie between \(2\) and \(n-1\) since \(n\ge6\).

We claim that if \(w\) begins with \(1\), it contains a later \(0\) and a still later \(1\). The position \(2\) is then an \(A\)-center, so one \(B\) occurs at position \(1\) or \(3\). If position \(3\) belongs to \(B\), its color is zero; center \(4\) has color one unless the other \(B\) is at position \(4\), in which case center \(5\) has color one. If position \(3\) belongs to \(A\), the \(B\)-positions are \(1\) and \(k\ge4\). For \(k=4\), the colors at centers \(3,4,5\) are \(1,0,1\). For \(k\ge5\), center \(3\) has color zero and center \(k-1\) has color one. This proves the claim. Reversing the direction order gives its mirror: if \(w\) ends with \(1\), it also has at least two changes. If \(w\) begins and ends with zero, its previously established occurrence of \(1\) produces at least two changes. Thus every order has at least two changes, independently of the starting vertex. \(\square\)

The construction in Theorem 2 satisfies \(h(c,b,a)=h(a,b,c)\), so it is **reversal-even**. It fails NORI's antipodal-reversal oddness, which for a position-independent coloring requires \(h(c,b,a)=1-h(a,b,c)\). Thus dimension five is the largest dimension in which the unrestricted one-change statement holds, while the NORI conjecture remains a distinct problem in dimension six and above.

## Further structural consequences

The unconditional dimension-five theorem combines an odd five-cycle of direction orders with independence of exterior root bits. Recent sharp counting arguments distinguish the unrestricted Q5 root-density guarantee from the stronger guarantee available under antipodal-reversal oddness.

Statement:
Let V=A⊔B and let c be a binary coloring of ordered three-faces of Q_V. Suppose changing the fixed bit of any a∈A complements c whenever a is outside the free triple. Then for any prescribed ordering σ of A, ordering τ of B, and initial bits on B, there is a choice of initial bits on A such that, along the full geodesic with coordinate order στ, every color change occurs between two consecutive triple windows lying entirely in B; their change sequence agrees exactly with that of the induced ordered-three-face coloring on Q_B at the prescribed B-start vertex. Consequently if |B|≤5, c admits an antipodal geodesic with at most one color change; if |B|≤3, it admits a monochromatic one. These conclusions hold without any antipodal symmetry hypothesis.

Proof:
Let T be the free triple of F. Repeatedly flipping fixed A coordinates gives c(F,π)=[⊕_{a∈A\T}x_a]⊕g(π,x_{B\T}), where g is independent of fixed A bits; each individual fixed A bit occurs with coefficient 1. Write |A|=r, order its coordinates first as a_1,…,a_r and then order B as b_1,…,b_m, and let w_t (1≤t≤n−2) be the color of the t-th consecutive triple window. Denote the initial a_i bit by z_i. Put G_t=g evaluated on the t-th window, a value independent of all z_i (since its fixed B bits are completely determined by the chosen B-start vertex and the B-coordinate order). The parity terms give, for 1≤t≤n−3, w_{t+1}⊕w_t=G_{t+1}⊕G_t⊕1_{t≤r}(z_t⊕1)⊕1_{t+3≤r}z_{t+3}. Fix arbitrarily every z_i with i>min(r,n−3). For t=min(r,n−3), min(r,n−3)−1,…,1 choose z_t to make the displayed difference zero. This is always possible since z_t occurs with coefficient 1 and z_{t+3}, if present, has already been fixed. Thus all differences with t≤r vanish. For t>r both windows are contained in the terminal B order, all A coordinates have already been traversed, and their parity contribution is the same constant. Hence w_{t+1}⊕w_t=G_{t+1}⊕G_t, exactly the adjacent color difference on the induced B-dimensional face coloring. This proves the exact reduction. For m≤3 there are no two consecutive B-only triple windows, so no differences remain. For m=4 there is at most one remaining difference. For m=5, every binary ordered-three-face coloring on Q_5 has a five-direction geodesic with at most one change: otherwise every order and start has word 010 or 101. For any order (a,b,c,d,e), its first and third window colors are equal. They vary independently with the two fixed exterior bits (d,e), respectively (a,b), forcing both functions to be constant. The coloring therefore depends only on the ordered triple, say h(a,b,c), and every order forces h(a,b,c)≠h(b,c,d). Applying these inequalities to the five cyclic rotations of (a,b,c,d,e) forces a binary label to alternate around an odd 5-cycle, impossible. Choose the resulting B-start bits and order and apply the exact reduction.

## Seven-dimensional closure for a universal flipper over the two-mark obstruction

Let \(Q_7\) have directions \(A\sqcup M\sqcup\{g\}\), where \(A=\{a,b,c,d\}\) has four unmarked directions and \(M=\{u,v\}\) has two marked directions. On ordered triples of the six directions \(B=A\sqcup M\), put
\[
 h(r,s,t)=
 \begin{cases}
 1,&s\in A\text{ and }(r\in M\text{ or }t\in M),\\
 0,&\text{otherwise}.
 \end{cases}
\]
This is reversal-even and gives the known sharp unrestricted \(Q_6\) obstruction: every full order of \(B\) has at least two changes.

**Theorem (face-dependent single-flipper lift is always good).** Suppose \(c\) colors ordered three-faces of \(Q_7\), satisfies \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\), and satisfies
\[
 c(F,\pi)=x_g(F)\oplus h(\pi)\qquad
 \text{whenever the free triple }\pi\text{ excludes }g.
\]
On triples containing \(g\), the coloring is completely arbitrary subject to antipodal-reversal oddness, and may depend on all four fixed exterior face bits. Then \(c\) has a full seven-edge antipodal geodesic with at most one color change.

**Proof.** Suppose for contradiction that every seven-edge geodesic is bad. Write \(m=(x_u,x_v)\in\mathbb F_2^2\) for the initial marked bits, and \(\bar m=(1\oplus x_u,1\oplus x_v)\). Denote the color of an ordered face whose free triple contains \(g\) by \(H\), retaining its dependence on the exterior face position.

*First forcing family.* Let \(a,b,c\) be distinct members of \(A\), \(d\) the fourth member, and consider the direction order
\[
 (a,g,b,c,u,v,d).
\]
Its final three windows, with free orders \((b,c,u),(c,u,v),(u,v,d)\), have \(h\)-colors \((1,0,0)\). Since \(g\) has already been flipped, their actual colors are \((x_g,x_g\oplus1,x_g\oplus1)\). The initial two window colors \(H(a,g,b)\) and \(H(g,b,c)\) are independent of \(x_g\). If they agreed, choosing \(x_g\) so the third window matched them would produce a good full geodesic. Hence
\[
 H(a,g,b)\ne H(g,b,c) \tag{1}
\]
for **every** assignment of the other six starting bits, with the appropriate face positions along this path.

For fixed \(a,b\), the face \((a,g,b)\) has the two other unmarked bits as exterior bits. In (1), \(x_c\) affects the first face but is free in the second face \((g,b,c)\), so the first color is independent of \(x_c\). We may choose \(c\) to be either member of \(A\setminus\{a,b\}\); thus the \((a,g,b)\)-face color is independent of both exterior unmarked bits. Write its value as \(F_{ab}(m)\). Similarly, in (1), \(x_a\) is free in the first face but (already toggled) is exterior to the second; varying \(a\) over \(A\setminus\{b,c\}\) shows that the \((g,b,c)\)-face color is independent of both exterior unmarked bits. Write it as \(G_{bc}(m)\). Therefore
\[
 F_{ab}(m)\ne G_{bc}(m)
 \quad\text{for every pairwise distinct }a,b,c\in A
 \text{ and every }m. \tag{2}
\]
For each fixed \(b,m\), the three values \(F_{ab}(m)\) with \(a\in A\setminus\{b\}\) are equal: given two choices \(a,a'\), use the remaining \(c\in A\setminus\{a,a',b\}\) in (2). Call their common value \(K_b(m)\). Equation (2) then gives \(G_{bc}(m)=1\oplus K_b(m)\) for every \(c\ne b\).

Apply the antipodal-reversal rule to the ordered face \((a,g,b)\), whose reversed triple is \((b,g,a)\). Reversal complements both marked exterior bits, and we have already proved independence of the other exterior bits. Hence
\[
 K_a(\bar m)=1\oplus K_b(m)
 \quad (a\ne b,\ a,b\in A). \tag{3}
\]
Fix one \(a\) and compare (3) for two other choices \(b,c\); then \(K_b(m)=K_c(m)\). Since \(|A|=4\), this forces a common function \(K(m)\) for all four subscripts. Equation (3) becomes
\[
 K(\bar m)=1\oplus K(m). \tag{4}
\]
We have proved, for any distinct unmarked \(r,s\in A\) and arbitrary exterior unmarked bits:
\[
 H(r,g,s)=K(m),\quad H(g,r,s)=1\oplus K(m).
\]
Antipodal reversal and (4) also give
\[
 H(r,s,g)=1\oplus K(m). \tag{5}
\]
Here \(m\) always means the marked exterior bits **at the window in question**.

*Second forcing family.* Fix an ordering \((a,b,c,d)\) of \(A\) and the full direction order
\[
 (a,b,c,g,d,u,v).
\]
By the forced identities and the definition of \(h\), its complete five-window color word is
\[
 \bigl(x_g,\;1\oplus K(m),\;K(m),\;T_u,\;x_g\oplus1\bigr), \tag{6}
\]
where \(T_u\) is the color of the ordered face \((g,d,u)\) reached in the fourth window. None of \(u,v\) has yet been traversed when the second and third windows occur, so both use the same \(m\). Choose \(x_g=1\oplus K(m)\). Then (6) becomes
\[
 (1\oplus K,\;1\oplus K,\;K,\;T_u,\;K).
\]
If \(T_u=K(m)\), this word has exactly one change. Thus the assumed universal failure forces
\[
 T_u=1\oplus K(m) \tag{7}
\]
for every choice of starting bits. Yet the direction \(u\) is free in the face \((g,d,u)\), so \(T_u\) is independent of the starting bit \(x_u\), whereas all its other exterior face bits are unchanged when \(x_u\) varies. It follows from (7) that \(K(x_u,x_v)\) is independent of \(x_u\).

Now interchange \(u,v\) in the last two positions, using the order \((a,b,c,g,d,v,u)\). Exactly the same argument, with the face \((g,d,v)\) in the fourth window and with \(h(d,v,u)=0\), shows that \(K\) is independent of \(x_v\). Therefore \(K\) is constant, contradicting (4). This establishes the theorem. \(\square\)

**Corollary.** The sharp reversal-even two-mark counterexample in six dimensions cannot be converted into a seven-dimensional NORI counterexample by adding a universal-flipper coordinate, **even when every ordered three-face containing that coordinate is allowed arbitrary dependence on its four fixed exterior bits**.

**Proof status and frontier.** This is a complete, local proof for the specified, highly structured class of seven-dimensional odd colorings. It is strictly stronger than the coordinate-only-on-\(g\)-faces suffix-rich theorem: the latter's pointwise triple-label contradiction does not survive arbitrary exterior dependence, while the two forcing families above use the available marked-bit freedom to recover a contradiction. No statement of general \(Q_7\) closure or all-dimensional NORI closure follows.

## An unconditional 7/8 good-root theorem in every physical five-face, and simultaneous NORI root transports

A physical ordered-three-face coloring on a selected Q5 face of a larger NORI cube need not satisfy a Q5 antipodal-reversal axiom. We therefore work first with an ARBITRARY binary coloring of actual ordered three-faces of Q5, imposing NO oddness.

A rooted full five-edge geodesic has THREE ordered-three-face windows. Call its root good if some direction permutation has a color word with at most one change; call the root bad if EVERY permutation has color word 010 or 101. Let D be the set of bad roots.

**THEOREM A (unconditional rank-five ROOT DENSITY).** For EVERY binary coloring of physical ordered three-faces of Q5,
  |D|<=4, hence at least 28 of the 32 physical starting vertices are GOOD.
Moreover, if |D|=4, the four bad roots are the vertices of ONE ordinary coordinate square of Q5. This theorem assumes no antipodal symmetry.

**Notation for the explicit odd-cycle proof.** Number the five coordinates 0,1,2,3,4. Encode a root x by its ordinary five-bit integer mask. Write [abc:t] for the ACTUAL ordered physical face with free ordered directions (a,b,c) and exterior-one-bit integer mask t, necessarily supported outside {a,b,c}. For a rooted permutation p=p0p1p2p3p4 at root x, the rank-j (j=0,1,2) physical window is
 [p_j p_(j+1) p_(j+2) : (x xor {p0,...,p_(j-1)}) outside its free triple].
If x is BAD, the colors of the rank-0 and rank-1 windows differ, as do the colors of the rank-1 and rank-2 windows. Therefore any sequence of an ODD number of physical window variables whose consecutive pairs are such forced comparisons gives an immediate contradiction. The following explicit finite certificates use SEVEN forced inequalities each; no machine-verification premise is needed, since every entry is a literal actual ordered face.

**Certificate table.** In every row, the seven displayed windows V0,...,V6 occur cyclically. The jth displayed 'r/p/12' or 'r/p/23' says that Vj and V_(j+1 modulo7) are exactly the first-two or last-two ordered-three-face windows, respectively, of the rooted 5-edge direction permutation p from root r. Thus if all listed roots were bad, every one of the SEVEN consecutive window-color inequalities would hold, impossible for binary colors.

1. TWO bad roots at Hamming distance THREE. By translation and coordinate relabeling reduce to roots {0,7}.
   Windows:
     412:9 | 341:1 | 234:3 | 123:1 | 230:0 | 304:0 | 041:8
   Edge certificates in the same cyclic order:
     0/03412/23 | 7/23410/12 | 0/01234/23 | 7/12304/12 | 7/12304/23 | 0/30412/12 | 0/30412/23.

2. TWO bad roots at Hamming distance FOUR. Reduce to {0,15}.
   Windows:
     340:2 | 234:3 | 123:1 | 012:0 | 124:0 | 240:2 | 401:0
   Edge certificates:
     15/23401/12 | 0/01234/23 | 0/01234/12 | 15/30124/23 | 0/12403/12 | 15/32401/23 | 15/23401/23.

3. FOUR bad roots of THREE-SPOKE-STAR type (one root and three distinct adjacent roots). Reduce to {0,1,2,4}.
   Windows:
     412:9 | 341:5 | 234:3 | 123:1 | 230:2 | 304:2 | 041:8
   Edge certificates:
     4/03412/23 | 2/02341/23 | 0/01234/23 | 1/12304/12 | 4/12304/23 | 2/30412/12 | 0/30412/23.

4. FOUR pairwise distance-two roots of TRIANGLE-SPAN type. Reduce to {0,3,5,6}.
   Windows:
     412:9 | 341:5 | 234:3 | 123:1 | 230:0 | 304:0 | 041:8
   Edge certificates:
     5/34120/12 | 3/23410/12 | 0/01234/23 | 3/12304/12 | 5/23041/12 | 0/30412/12 | 0/30412/23.

5. FOUR pairwise distance-two roots of THREE-INDEPENDENT-SPOKE type. Reduce to {0,3,5,9}.
   Windows:
     340:4 | 234:1 | 123:1 | 012:0 | 124:1 | 240:0 | 401:4
   Edge certificates:
     3/12340/23 | 3/12340/12 | 0/01234/12 | 0/01243/12 | 3/12403/12 | 0/24013/12 | 9/23401/23.

All five sequences close from their seventh to their first window with the seventh displayed certificate. Each row is independently checkable by the single physical-window formula above, using only the stated root masks and full coordinate permutations.

**Combinatorial classification and proof of Theorem A.** The first two certificates show that no pair of bad roots is at Hamming distance 3 or 4. If a bad antipodal pair has distance 5, no THIRD bad root can exist: a third vertex at distance k from the first is at distance 5-k from the second, and for k in {1,2,3,4} one distance belongs to {3,4}. Thus a bad set with at least three roots has pairwise distances only 1 or 2.

Classify any FOUR cube vertices of pairwise distances at most two. Translate one to the origin. The other three have supports of size 1 or 2. If at least two singleton supports occur, the set is either a coordinate square or a three-spoke star. If exactly one singleton occurs, all other two-element supports must contain that coordinate, again giving a three-spoke star (after translating its central vertex). If none occurs, the other three two-element supports pairwise intersect, hence either form the three edges of a triangle (the triangle-span equidistant-four class) or have a common element (the independent-spoke equidistant-four class). These are precisely the four types in Cases 3-5 plus the ordinary square. The three certificates exclude every nonsquare type. Hence EVERY set of four bad roots must be a coordinate square.

A coordinate square has no fifth vertex within Hamming distance at most two of ALL four corners: to be within distance at most two of opposite corners forces every outside-square bit zero, and then the vertex is one of its four corners. Consequently five bad vertices are impossible. Thus |D|<=4, and equality requires a square. QED.

**THEOREM B (unconditional same-root multi-support density in NORI).** Let n>=5 carry an arbitrary binary coloring of physical ordered three-faces. For each five-coordinate support B define G_B(x) as existence of a genuine <=1-switch geodesic rooted at x that uses EXACTLY the five directions of B. Then
  |Q_n\G_B|<=2^(n-3), i.e. |G_B|>= (7/8)*2^n.
For any m prescribed five-supports B1,...,Bm,
  |G_B1 intersect ... intersect G_Bm| >= (1-m/8)*2^n.
In particular ANY collection of at most SEVEN five-supports admits a SINGLE common physical root supporting real one-switch rank-five geodesics on every support simultaneously; at least 1/8 of all roots work when m=7.

**Proof.** Fix B and the n-5 exterior coordinate bits. Within that actual five-face, the induced coloring is arbitrary, so Theorem A supplies at least28 good starting vertices of32. Summing over all 2^(n-5) fibers yields the 7/8 density. The intersection estimate is the elementary union bound on the bad-root sets, requiring no independence and no antipodal symmetry. QED.

**THEOREM C (genuine antipodal root-orbit synchronization under active NORI).** Now assume the FULL active NORI axiom c(bar F,rev pi)=1-c(F,pi), and n>=6. Put sigma_B=[n]\B. Then
  G_B + sigma_B=G_B,
since the antipodal reversal of a B-geodesic from x has root bar(x xor B)=x xor sigma_B and has the same number of switches.

Given m prescribed five-supports B_j, let H=span_F2{sigma_Bj} of size 2^r. If p_j=|Q_n\G_Bj|/2^n <=1/8, then the fraction of roots x for which EVERY root in the full affine orbit x+H belongs to ALL of the G_Bj is at least
  1 - (|H|/2)*sum_j p_j
  >= 1 - m|H|/16.
Indeed for each j, the failure event at x+h is identical to that at x+h+sigma_Bj, so there are only |H|/2 distinct translates. Sum their probabilities, then sum over j.

In particular for TWO distinct five-supports B,C, H=<sigma_B,sigma_C> has four elements and
  at least ONE HALF of all physical roots x have the property that all FOUR roots in x+H support genuine one-switch rank-five geodesics on BOTH B and C.
For THREE supports with dependent, nonzero complement vectors spanning a 2-dimensional H, at least 1/4 of roots support analogous entire four-root simultaneous witness orbits (m=3, |H|=4).

**Connection to exact grand extraction and unresolved step.** A rank-five <=1-switch path gives two genuine constant-color BLOCKS of its three-window word. Under FULL NORI reversal, the complementary-colored reversed suffix starts at an exterior-shifted root, since bar(x xor B)=x xor sigma_B. Thus the exact SAME-ROOT reversed-two-tail equivalence for a FULL n-direction path CANNOT be applied directly to a proper five-face: the induced face coloring need not be reversal-odd. Theorem B forces compatible COMMON ROOTS for up to seven arbitrarily prescribed five-support one-switch certificates. Theorem C forces honest multi-root affine transport orbits with paired physical reverse witnesses. The missing step is a theorem transporting and aligning the variable terminal ordered pairs, exterior root shifts, and monochromatic branch supports across these actual witnesses to obtain a full n-direction complementary reversed-two-tail pair at ONE root. Root synchronization alone does not imply such memory alignment, and grand NORI remains open.

### Complete dimension-six closure by six coupled antipodal geodesics

Let \(Q_6=\{0,1\}^{\{a,b,c,d,e,f\}}\), and let \(c(F,\pi)\in\mathbb F_2\) color each three-dimensional face \(F\) with ordered free directions \(\pi\), subject to
\[
 c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi).
\]
For a starting vertex \(y\) and a permutation \(p\) of the six coordinates, write \(W(y,p)\in\mathbb F_2^4\) for its four consecutive ordered-three-face colors. In the window beginning at position \(i\), the free directions are \((p_i,p_{i+1},p_{i+2})\); the fixed bit at an outside coordinate \(t\) equals \(y_t\oplus\mathbf1_{t\in\{p_1,\ldots,p_{i-1}\}}\). This formula permits direct comparison of any two window faces.

**Lemma (six-geodesic forcing certificate).** Suppose there is a four-edge path through distinct directions \(a,b,c,d\), starting at a vertex \(x=(A,B,C,D,E,F)\), whose two length-three ordered-face windows have the same color. Then at least one of the six antipodal geodesics in the following table has at most one change. Here \(\bar A=1\oplus A\), etc., and the starting vertices are listed in \((a,b,c,d,e,f)\)-coordinate order.

| index | direction order | starting vertex |
|---|---|---|
| 1 | \(a b c d e f\) | \((A,B,C,D,E,F)\) |
| 2 | \(d c b a e f\) | \((A,B,C,D,\bar E,\bar F)\) |
| 3 | \(d c b a f e\) | \((A,\bar B,\bar C,D,\bar E,\bar F)\) |
| 4 | \(d c b f e a\) | \((A,\bar B,\bar C,\bar D,\bar E,\bar F)\) |
| 5 | \(d e f a c b\) | \((\bar A,\bar B,\bar C,\bar D,E,F)\) |
| 6 | \(d e f b c a\) | \((\bar A,\bar B,\bar C,D,\bar E,\bar F)\) |

**Proof.** A global complement of the coloring preserves antipodal-reversal oddness and the number of color changes. Thus assume the initial path's two window colors are both 0. Suppose for contradiction that all six displayed antipodal geodesics have at least two changes. A four-bit word beginning \(00\) is bad precisely when it is \(0010\), and a word beginning \(11\) is bad precisely when it is \(1101\). A four-bit word beginning with \(1\) and ending with \(0\) is bad precisely when it equals \(1010\). (Here 'bad' means at least two changes.)

Write \(W_i\) for the window-color word of displayed path \(i\). The face-address formula and the oddness hypothesis yield the following chain.

1. \(W_1\) begins \(00\), so \(W_1=0010\), and its final \((d,e,f)\) window has color 0.
2. The first two windows of path 2, ordered \((d,c,b)\) and \((c,b,a)\), are the antipodal reversals respectively of path 1's second and first windows, hence both color 1. Thus \(W_2=1101\), forcing its final \((a,e,f)\) window to color 1.
3. The corresponding first two windows of path 3 are the same antipodal reversals, and again \(W_3=1101\). Its final \((a,f,e)\) window therefore colors 1.
4. The first window of path 4 is the antipodal reversal of path 1's second window, giving color 1. Path 4's final \((f,e,a)\) window is the antipodal reversal of path 2's final \((a,e,f)\) window, giving color 0. Therefore \(W_4=1010\), so its third \((b,f,e)\) window colors 1.
5. Path 5 begins with exactly the same ordered \((d,e,f)\) face as path 1's final window, giving color 0. Its second \((e,f,a)\) window is the antipodal reversal of path 3's final \((a,f,e)\) window, giving color 0. Thus \(W_5=0010\), forcing its final \((a,c,b)\) window to color 0.
6. Path 6 begins with the same \((d,e,f)\) face as path 1's final window, giving color 0. Its second \((e,f,b)\) window is the antipodal reversal of path 4's third \((b,f,e)\) window, giving color 0. Its final \((b,c,a)\) window is the antipodal reversal of path 5's final \((a,c,b)\) window, giving color 1. Hence \(W_6=(0,0,*,1)\), which has at most one change.

This contradicts the assumed failure of all six paths. Each claim that two windows are identical or antipodal reversals follows directly from the six starting-vertex vectors and the face-address formula; the proof uses the actual fixed exterior face bits throughout. \(\square\)

**Theorem (complete dimension-six NORI).** Every antipodal-reversal-odd coloring \(c\) of ordered three-faces of \(Q_6\) admits an antipodal geodesic with at most one color change.

**Proof.** Let \(H\) be any five-dimensional subcube of \(Q_6\), obtained by fixing one coordinate. Its induced ordered-face coloring is arbitrary, with no oddness assumption. The unconditional five-dimensional theorem states that some five-direction antipodal geodesic in \(H\) has at most one color change. For completeness, its proof is as follows. If every five-direction geodesic had two changes, every three-window color word would alternate, making its first and third colors equal. For a fixed order \((a,b,c,d,e)\), the first color depends only on the two fixed exterior bits \(d,e\), while the third depends only on the two independent exterior bits \(a,b\). Varying all starting bits forces both functions to be constant. Since every ordered triple can occur first in some ordering, the color is independent of the choice of three-face and has the form \(h(a,b,c)\). Universal alternation forces \(h(a,b,c)\ne h(b,c,d)\) in every order. Applying this to the five cyclic rotations of five distinct coordinates would alternate a binary labeling around a 5-cycle, impossible.

Select that good five-direction path in \(H\). Of its three consecutive window colors, two adjacent colors agree. The corresponding contiguous four-edge subpath therefore has equal ordered-three-face colors. Name its four directions \((a,b,c,d)\), and call the remaining two cube directions \(e,f\). Apply the six-geodesic forcing certificate to this four-edge subpath. At least one of the six explicit antipodal geodesics has at most one color change, as claimed. \(\square\)

**Scope and extension obligation.** This theorem proves the full face-dependent antipodal-reversal-odd conjecture in dimension six; dimension five needs no oddness. In dimensions \(n>6\), the six-path forcing certificate can be applied to six-coordinate restrictions only if the exterior fixed-bit assignments needed by the antipodal-reversal comparisons are compatible. A general restriction has extra fixed exterior bits, and the six-route gadget uses both equality and antipodal complement of faces. Establishing a compatible embedding or a full-dimensional forcing cycle is the remaining extension problem.

## Further structural consequences

The six-path physical-face certificate proves the legal dimension-six theorem. Complementary structural classifications reveal how uniform and pointwise exterior sensitivities would constrain a hypothetical reversal-even Q6 obstruction; their proofs must retain the actual antipodal face comparisons, not just a four-bit word template.

## Alternating-tail rigidity in a reversal-even six-coordinate residual

Let \(B\) be a six-element coordinate set and let \(H(a,b,c)\in\mathbb F_2\) be a position-independent coloring of ordered *distinct* triples satisfying reversal-evenness
\[
H(a,b,c)=H(c,b,a).
\]
Call an ordered triple \((a,b,c)\) a **dead prefix** if, for every permutation \((d,e,f)\) of \(D=B\setminus\{a,b,c\}\), the three-color tail
\[
\bigl(H(b,c,d),\,H(c,d,e),\,H(d,e,f)\bigr)
\]
has two changes, equivalently it alternates.

**Lemma (rigid alternating-tail seed).** For a fixed ordered triple \((a,b,c)\) and \(D=B\setminus\{a,b,c\}\), the dead-prefix condition holds **if and only if** there is a bit \(K\) such that
\[
\begin{aligned}
H(b,c,d)&=K &&(d\in D),\\
H(c,d,e)&=1\oplus K &&(d,e\in D,\ d\ne e),\\
H(d,e,f)&=K &&((d,e,f)\text{ any permutation of }D).
\end{aligned}\tag{1}
\]
Thus a single dead prefix forces the colors of all six permutations on \(D\), all six \(c\)-to-\(D\)-to-\(D\) triples, and all three \(b,c,D\) triples from one bit.

**Proof.** Assume every tail alternates. Fix an element \(d\in D\) and write \(e,f\) for the other two. Reversal-evenness implies that \(H(d,e,f)=H(f,e,d)\), so the color of a triple whose three coordinates are exactly \(D\) depends only on its middle coordinate; call it \(W_e\). Put \(U_d=H(b,c,d)\). Alternation for the permutation \((d,e,f)\) says
\[
U_d=W_e,\qquad H(c,d,e)=1\oplus W_e\qquad(d,e\in D,\ d\ne e).\tag{2}
\]
For any distinct \(e,e'\in D\), take the remaining \(d\in D\). Then \(W_e=U_d=W_{e'}\). Therefore all \(W_e\) equal some \(K\); (2) gives all \(U_d=K\) and \(H(c,d,e)=1\oplus K\), proving (1). Conversely, (1) makes every tail word \((K,1\oplus K,K)\), so the prefix is dead. \(\square\)

**Necessary structural consequence for one-flipper Q7.** Let \(c\) be a hypothetical NORI counterexample on \(Q_7\) with a universal exterior flipper \(g\), whose induced reversal-even six-coordinate coloring is position-independent, \(h(F,\pi)=H(\pi)\). The uniform good-tail theorem implies that *some* ordered triple \((a,b,c)\) is a dead prefix. Consequently the induced \(H\) contains an alternating-tail seed of the exact form (1), up to coordinate relabeling and global color complementation.

The known reversal-even two-mark obstruction realizes such a seed by taking \(b,c\) to be its marked directions, \(a\) an unmarked direction, and the three elements of \(D\) unmarked. Formula (1) is a necessary seed for every possible coordinate-only residual obstruction to one-flipper closure, without assuming the entire two-mark template. It is a rigidity mechanism, not by itself closure.

## Two uniform exterior sensitivities force a good Q6 geodesic

Let \(B=\{a,b,c,d,e,f\}\), and let \(h\) be a binary ordered-three-face coloring on \(Q_B\) satisfying reversal-even antipodality
\[
h(\bar F,\operatorname{rev}\pi)=h(F,\pi).
\]
An ordered triple \((a,b,c)\) is **uniformly sensitive** in an exterior direction \(t\in B\setminus\{a,b,c\}\) if toggling the fixed \(t\)-bit always complements its color, independently of the other exterior bits.

**Theorem (two-flipper sensitivity closure).** If some ordered triple \((a,b,c)\) is uniformly sensitive in two distinct exterior directions \(d,e\), then \(h\) has a full six-coordinate antipodal geodesic with at most one color change.

**Proof.** Suppose instead that *every* complete six-direction geodesic is bad. Let \(f\) be the remaining exterior direction. Apply the previously established uniform complementary-face collapse lemma first with the distinguished exterior direction \(d\), then with \(e\).

The \(d\)-collapse supplies a constant \(K_d\) and, for every exterior assignment,
\[
h(d,a,b)=K_d,\qquad h(d,f,e)=K_d.
\tag{1}
\]
The first equality uses reversal-evenness to reverse the forced triple \((b,a,d)\).

The \(e\)-collapse supplies a constant \(K_e\) and the universal identities
\[
h(d,f,e)=K_e,\qquad
h(b,c,e)=K_e,\qquad
h(c,e,f)=1\oplus K_e.
\tag{2}
\]
Here \((d,f,e)\) is one of the four complementary-triple orientations forced by sensitivity in \(e\). Comparing (1) and (2) gives \(K_d=K_e=:K\).

Now take the complete direction order
\[
(d,a,b,c,e,f).
\tag{3}
\]
Its four window colors, at their actual face positions, are
\[
\big(K,\ h(a,b,c),\ K,\ 1\oplus K\big),
\tag{4}
\]
by (1) and (2), with the displayed constant entries valid for **all** initial bits. The second window has the free directions \(a,b,c\); the previously crossed direction \(d\) is fixed outside it. By uniform \(d\)-sensitivity, toggling the initial \(d\)-bit complements only its second-window color among the four entries in (4), because the other three entries are constants. Choose that bit so the second color equals \(K\). We obtain
\[
(K,K,K,1\oplus K),
\]
with exactly one change, a contradiction. \(\square\)

**Corollary (one-junta rigidity of affine residuals).** Let \(h\) be a reversal-even ordered-three-face coloring of \(Q_6\) such that the color of each ordered face is an affine Boolean function of its three exterior bits. If every six-direction geodesic has at least two color changes, then for each ordered triple \(\pi\), the exterior-bit function \(h(F,\pi)\) depends on **at most one** of its three exterior coordinates.

**Proof.** Every nonzero Boolean derivative of an affine function equals 1 everywhere. Two distinct nonzero exterior coefficients would therefore give two uniform sensitivities, contradicting the theorem. \(\square\)

**Impact on NORI.** A one-universal-flipper NORI coloring of \(Q_7\) has a reversal-even six-dimensional residual. If that residual is affine and no six-direction residual path is good, the residual is necessarily a collection of Boolean one-juntas (one exterior input per oriented triple). Each nonconstant one-junta additionally forces the universal face-constant blocks of the complementary-face collapse lemma. This reduces the affine six-residual frontier to a much more rigid, explicitly finite class. It does not yet prove that all one-junta residuals are coordinate-only or that the general seven-dimensional NORI conjecture holds.

## Alternating-pole restriction fails in dimension six

Partition six directions into four unmarked directions A and two marked directions M. Define
\[
h(a,b,c)=1 \quad\Longleftrightarrow\quad b\in A\text{ and }\{a,c\}\cap M\ne\varnothing.
\]
This triple label is invariant under reversal. For an ordered three-face F with k exterior coordinates fixed to one, define
\[
\chi(F,\pi)=\begin{cases}
0&k=0,\\
1\oplus h(\pi)&k=1,\\
h(\pi)&k=2,\\
1&k=3.
\end{cases}
\]
Since antipodality sends k to 3-k, reversal leaves h unchanged, and the corresponding displayed values are complementary, this is an antipodal-reversal-odd ordered-face coloring on Q6.

**Theorem.** Every full six-coordinate geodesic whose starting bits alternate in the traversal order has at least two color changes.

**Proof.** Let p=(p1,...,p6) be the traversal order. For starts 010101 and 101010 (in p order), all four windows have exterior-one weights 2 and 1, respectively: between windows the exiting direction pi enters the exterior in flipped state, the entering direction p(i+3) leaves it with the same state. Hence the color word is the h-word of p or its complement. The four-window h-word depends only on the positions occupied by the two M directions. The 15 cases, in increasing marked-position order, are

12:0100, 13:1010, 14:1101, 15:1010, 16:1001;
23:0010, 24:0101, 25:0110, 26:0101;
34:1001, 35:1010, 36:1011;
45:0100, 46:0101, 56:0010.

Each word has two or three color changes. Complementation preserves change count. Thus all alternating-pole geodesics fail. QED.

**Significance.** The established unrestricted Q6 NORI theorem nevertheless guarantees a good geodesic in this coloring. Thus every good full geodesic must visit at least two exterior Hamming-weight layers. The preceding all-dimensional central-layer tournament theorem is strictly conditional; no general argument can restrict to constant-central-weight paths.

### Sharp rooted obstructions to one-change antipodal geodesics

# Rooted obstructions and sharp dimension-five root density

A root \(x\in Q_n\) is called *bad* when every full geodesic beginning at \(x\) has at least two changes among its consecutive ordered-three-face colors. We assume the NORI reversal law \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\).

**Theorem 1 (failure of rooted strengthening).** For each \(n\ge5\) and prescribed root \(x\), there is a legal NORI coloring making \(x\) bad. The number of changes along every full \(x\)-rooted geodesic may be made equal to \(2\) for \(n=5\), to \(n-3\) for even \(n\ge6\), and to \(n-4\) for odd \(n\ge7\).

**Proof.** Translate \(x\) to \(0^n\). Let \(k\) be the number of exterior coordinates fixed to 1 on a physical ordered three-face. For even \(n\), color by \(k\bmod2\). Since \(n-3\) is odd, antipodal complementation reverses the bit. Every rooted order visits the successive exterior weights \(0,\ldots,n-3\), yielding complete alternation.

For odd \(n\ge7\), write \(n-3=2s\) and fix a reversal-odd ordered-triple bit \(h(a,b,c)=1-h(c,b,a)\). Color faces of exterior weight \(k<s\) by \(k\bmod2\), of weight \(k=s\) by \(h\), and of weight \(k>s\) by \(1+(k\bmod2)\). Exterior weights are paired by \(k\mapsto2s-k\), so this is NORI-odd. The left and right window strings alternate, with opposite values directly adjacent to the central window. Exactly one central comparison changes, giving \(2(s-1)+1=n-4\) changes. The \(n=5\) construction is furnished by Theorem 2. \(\square\)

**Theorem 2 (exact rooted \(Q_5\) classification).** Put \(V=[5]\). For each \(t\in V\) and \(P\subset V\setminus\{t\}\) of size two, choose a bit \(H(P,t)\) satisfying
\[
H((V\setminus\{t\})\setminus P,t)=1+H(P,t).
\tag{1}
\]
For a physical ordered face with directions \((a,b,c)\) and exterior-one set \(S\), define
\[
c(F,(a,b,c))=
\begin{cases}
H(\{a,b\},c)&|S|=0,\\
1+H(S\cup\{a\},b)&|S|=1,\\
H(S,a)&|S|=2.
\end{cases}
\tag{2}
\]
Precisely these \(2^{15}\) legal NORI colorings make \(0^5\) bad.

**Proof.** At a bad root every three-window word is \(010\) or \(101\). The first and last windows consequently agree. Exchanging the first two directions fixes the physical last window, so the first-window color has the form \(H(\{a,b\},c)\). Forced alternation then determines the middle and last window values as (2). Every ordered face occurs in some \(0^5\)-rooted full path, so these formulas exhaust the coloring. Antipodal reversal of the rank-zero and rank-two faces gives (1), which also enforces reversal oddness at rank one. Conversely (1)–(2) produce the word \((H(\{a,b\},c),1+H(\{a,b\},c),H(\{a,b\},c))\) for every rooted order \((a,b,c,d,e)\). For each \(t\), the six possible \(P\)'s form three complementary pairs; one free bit per pair gives \(3\cdot5=15\) independent choices. \(\square\)

**Theorem 3 (sharp good-root density).** Every legal NORI coloring of \(Q_5\) has at most two bad roots, and any two bad roots are adjacent. Consequently at least \(30\) of its \(32\) vertices admit good full geodesics. The bound is attained with any prescribed adjacent pair as the exact bad set.

**Proof.** Translate one bad root to \(0^5\) and use the classification (1)–(2). Suppose a second bad root is at Hamming distance \(k\ge2\), with first \(k\) of the coordinates \(a,b,c,d,e\) equal to 1. A bad three-window word at that root has its first and last bits equal, distinct from its middle bit. Substituting (2) gives the following contradictions (all equations in \(\mathbb F_2\)):

For \(k=2\), orders \(bdeac,abdce,bedac\) yield
\[
H(bc,a)+H(ab,d)=1,\quad H(ab,d)+H(ab,e)=1,\quad
H(ab,e)+H(bc,a)=1,
\]
whose sum is \(0=1\). For \(k=3,4\), orders \(adebc,badce\) demand simultaneously \(H(bc,a)+H(ab,e)=1\) and \(=0\). For \(k=5\), orders \(abcde,adebc\) demand simultaneously \(H(bc,a)+H(ad,c)=0\) and \(=1\). Hence two distinct bad roots are adjacent; three pairwise adjacent vertices cannot exist in a hypercube.

For sharpness fix coordinate \(a\), and in (1) set \(H(P,t)=\mathbf1_{\{a\notin P\}}\) for \(t\ne a\), choosing any complementary-pair assignment for \(t=a\). Formula (2) makes \(0^5\) bad. For a path rooted at \(e_a\), place \(a\) at position \(j\) in its direction order. Its full color word is \(010\) for \(j=1,2\), \(101\) for \(j=4,5\), and \((h,1+h,h)\) for \(j=3\), with \(h=H(\{p_1,p_2\},a)\). Thus \(e_a\) is bad too; the upper bound makes every other vertex good. \(\square\)

The rooted strengthening therefore fails for every \(n\ge5\), whereas the unrooted five-dimensional theorem has the stronger conclusion that at least \(15/16\) of the roots succeed. This makes root mobility an essential part of any global topological or inductive extraction.

## Exact thin-shell theorem for good roots of exterior parity

The sharp five-dimensional lower bound on the proportion of good roots has no dimension-independent analogue. For even \(n\ge6\), consider the legal coloring
\[
c(F,\pi)=\bigoplus_{t\notin\mathrm{free}(F)}b_t(F).
\]
Write \(G_n\subseteq Q_n\) for its roots admitting a full geodesic with at most one color change, and put
\[
\rho_n=\begin{cases}1&n\equiv0\pmod6,\\2&n\equiv2,4\pmod6.\end{cases}
\]

**Theorem 4 (exact good-root shell).** For this NORI coloring,
\[
G_n=\{x\in Q_n:|\operatorname{wt}(x)-n/2|\le\rho_n\}.
\tag{3}
\]
Consequently
\[
\frac{|G_n|}{2^n}
=2^{-n}\sum_{j=-\rho_n}^{\rho_n}\binom n{n/2+j}
=(2\rho_n+1)\sqrt{\frac{2}{\pi n}}\,(1+O(n^{-1})).
\tag{4}
\]
In particular, the good-root density tends to zero along even dimensions, and every good root has Hamming distance at least \(n/2-\rho_n\) from \(0^n\). Translating the coloring places such a bad-root ball around any prescribed vertex.

**Proof.** The coloring is legal because antipodal complementation toggles all \(n-3\) exterior bits and \(n-3\) is odd. Fix a root \(x\) and a full coordinate order \(p=(p_1,\ldots,p_n)\). Write \(a_i=x_{p_i}\). If \(K_i\) is the exterior-one count of the \(i\)-th physical three-face, then
\[
K_{i+1}-K_i=1-a_i-a_{i+3}\quad(1\le i\le n-3).
\]
The two consecutive colors differ precisely when \(a_i=a_{i+3}\). Hence a full order is good exactly when the three disjoint position chains
\[
(a_r,a_{r+3},a_{r+6},\ldots),\qquad r=1,2,3,
\tag{5}
\]
have **at most one adjacent equal pair in total**.

A fully alternating chain of length \(2m\) has exactly \(m\) ones, and one of length \(2m+1\) has \(m\) or \(m+1\) ones. Allowing a single adjacent equal pair changes an even-length chain's possible one-count to \(m-1,m,m+1\), while an odd-length chain still has \(m\) or \(m+1\) ones. These claims follow by splitting at the exceptional pair into two alternating segments; both extreme even-chain counts are obtained, for example, by beginning \(00,10,10,\ldots\) or its complement.

For \(n=6m\), the three chain lengths are \(2m,2m,2m\). Without an exceptional pair the total is \(3m\), and one exception permits \(3m\pm1\). For \(n=6m+2\), the lengths are \(2m+1,2m+1,2m\): alternating chains give totals \(3m,3m+1,3m+2\), and one exception in the even chain additionally realizes \(3m-1\) and \(3m+3\). For \(n=6m+4\), the lengths are \(2m+2,2m+1,2m+1\): alternating chains give \(3m+1,3m+2,3m+3\), and one exception in the even chain additionally realizes \(3m\) and \(3m+4\). Thus the possible total number of ones in a good order is exactly the interval in (3).

Because the coloring is invariant under permutations of coordinate names, every root of a feasible Hamming weight admits an order placing its one-bits into a suitable chain pattern. This proves (3). Summing the binomial layers gives the exact formula (4), and the displayed asymptotic follows from the central binomial estimate for fixed offsets \(j\). The distance and translation assertions follow immediately. \(\square\)

**Implication for a general proof.** A universal argument cannot assume a fixed positive fraction of good starting roots, or guarantee a good root within \(o(n)\) bit flips of an arbitrary prescribed root. This obstruction arises in the same exterior-parity class for which every *fixed order* has eight monochromatic starts; abundance over orders can coexist with severe geometric concentration of successful roots. The theorem concerns a structured legal coloring and does not weaken the unrooted NORI conjecture.


### Appendix — Known obstructions to proposed NORI mechanisms

# Appendix — Known obstructions

These are **proved limitations of specific proposed implications**, not counterexamples to the unrooted grand NORI conjecture. Proofs and finite certificates are in the indicated Subsections; historical identifiers resolve through the legacy-reference lookup.

## Prescribed roots and unsupported support lifting

**A prescribed root need not support any full good geodesic.** In dimensions \(n\geq 6\) the exterior-weight parity construction (with the central reversal-odd correction in odd \(n\)) is legal and forces multiple color changes for every full order from a chosen root. Root motion remains permissible and necessary; see *Sharp rooted obstructions to one-change antipodal geodesics*.

**No dimension-independent positive density or sublinear root-localization bound.** For even \(n\ge6\), the legal exterior-parity coloring has good roots *exactly* at Hamming weights \(n/2-\rho_n,\ldots,n/2+\rho_n\), with \(\rho_n=1\) if \(6\mid n\) and \(\rho_n=2\) otherwise. Their density is \(\Theta(n^{-1/2})\), and the nearest good root to \(0^n\) is at distance \(n/2-\rho_n\). Thus neither a uniform positive fraction of successful roots nor a universal \(o(n)\)-radius search around a prescribed root can be assumed. See the exact thin-shell theorem in *Sharp rooted obstructions to one-change antipodal geodesics*.

**Good paths on every proper support do not imply a full good path at that root.** A verified legal \(Q_7\) coloring has an ordering with at most one switch on *every* proper support of size 3–6, yet every full seven-order from the same root has at least two switches. The full 1680-bit face-color certificate and exhaustive verifier are retained in *Maximal geodesic blockers and snake exchanges*. A more general exterior-weight construction gives all-dimensional short-path coverage without rooted full closure. These refute **coverage-only rooted implications**, not same-root *complementary reversed-terminal* intersections with their correct ordered memory, nor an unrooted conclusion.

## Exterior-bit consistency and restricted positional claims

**Naively embedding the six-path forcing certificate is unsound.** Each added exterior coordinate must meet actual equality and complemented-face constraints. A signed cycle with an odd number of complementation edges yields \(z=z\oplus1\), so the six-row pattern can have no consistent higher-dimensional physical realization. The \(Q_6\) theorem and six-path implication proof remain correct. An entirely new globally compatible forcing network or a different inductive invariant remains possible. See *Exterior-bit holonomy and the six-path extension obstruction*.

**Prescribing a sentinel slot is too strong even when a restricted family closes.** Legal face-dependent \(Q_7\) colorings can forbid every full good path with a designated direction third or fifth (exact finite coloring/certificate; historical ID \(nori_q7_fixed_sentinel_third_and_fifth_slot_2sat_counterexample_20261009\)). This does **not** refute ordinary \(Q_7\) closure with a free order. Positive one-sentinel \(Q_7\) and \(Q_8\) computer-assisted results retain their explicitly restricted exterior-dependence hypotheses; see *Seven-coordinate wing factorization and exact obstruction* and *Exterior face charts and Fourier transport*.

## Physical witness geometry versus abstract carriers

**Formal equal-support diagonals need not be actual path transitions.** The physical window-shift graph contains squares whose abstract diagonals do not correspond to any four-edge ordered-window shift. Topological or parity arguments using them as actual incidence require correction. The proven optimal physical transport and connector counts survive; extracting one full compatible path remains open. See the Article IV window-transport Subsections.

**Index in an ambient uncolored carrier is insufficient.** Actual good-path cells require joint witnessing, not pairwise label compatibility. For contiguous extension-flag models, the established equivariant collapse to the window-level graph limits the index information such a model retains. This does not rule out a different, more informative jointly witnessed carrier. See the Article II topological-carrier Subsections.

## Exchange and representation limitations

**Every adjacent exchange is local, but need not improve a defect.** A swap changes at most four consecutive physical windows; local caps and opposite-color extremal walls can coexist with insertion/swap obstructions. A strict globally terminating potential remains unproved. See *Maximal geodesic blockers and snake exchanges* and Article V.

**Edge-coloring results do not automatically transfer.** A path's physical edge-color word does not determine the ordered colors of its overlapping three-faces. Affine and central-Johnson edge theorems remain valid for the edge problem, but a NORI transfer must preserve actual exterior bits, terminal order and seam colors. See Article VIII.

These entries are curated by *mechanism*, not by the history of unsuccessful searches. A new exact proof may supersede an entry; its mathematical statement and surviving scope should then be revised.
