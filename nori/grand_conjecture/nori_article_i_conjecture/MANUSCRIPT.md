# Article I — Antipodal-reversal-odd geodesic colorings of the cube

## Article setting and orientation

**Matching logarithmic path scale under fixed exterior support.** For any legal (indeed, arbitrary) physical ordered 3-face coloring whose ordinary triples depend only on a fixed t-coordinate exterior support, the longest monochromatic geodesic has length at least 1 + (1/2)log_2(n-t). The terminal ordered-pair label proof gives n-t <= binomial(2L-2,L-1). The Devine-Milans one-sentinel construction matches this within constant factors, so the extremal scale for every fixed t>=1 is Theta(log n). The unrestricted problem remains open because different windows may sample inconsistent ordinary exterior fibers. See the new Foundations Subsection.

**New sharp qualitative obstruction: logarithmic monochromatic NORI3 paths and near-linear switches.** Combining the explicit logarithmic-short-path \((3,3)\)-tournament from Devine–Milans' uploaded *Tight paths in fully directed hypergraphs* with its newly proved reverse-complement self-duality and one physical exterior sentinel yields legal NORI3 colorings in **every \(n\ge5\)** with no monochromatic geodesic longer than \(2\lceil\log_2(n-1)\rceil+6\) moves. Consequently
\[
 S_3(n)\ge\left\lceil\frac{n-2}{2\lceil\log_2(n-1)\rceil+4}\right\rceil-1
 =\Omega(n/\log n).
\]
This supersedes \(\Omega(\sqrt n)\) as a universal construction lower bound, and refutes the proposed universal \(\Omega(\sqrt n)\) monochromatic-geodesic guarantee. The fully rigorous physical-face proof is in the new Foundations Subsection *Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament*. The scrapbook's antisymmetric square-root bound is a distinct theorem for same-face reversal-odd boundary tournaments; unrestricted NORI3 permits same-face reversal-even pairs.

*Full Article composition: [source manuscript](../nori_article_i_conjecture.md).*

## Foundational closure theorems and rooted obstructions

**Sharp logarithmic lower bound with bounded exterior support.** If the colors of every ordered three-face avoiding a distinguished set S of t coordinates depend only on its ordered free directions and the fixed exterior S bits, there is a monochromatic coordinate geodesic of length at least 1+(1/2)log_2(n-t), without assuming legality. The proof uses ordered Ramsey terminal-pair path-length labels and pairwise distinct grid order ideals: n-t <= binomial(2L-2,L-1) <= 4^(L-1). The self-dual Devine-Milans single-sentinel construction attains O(log n) longest monochromatic geodesics. Hence, for every fixed t>=1, the minimum over legal NORI3 colorings of exterior-support at most t of the longest monochromatic geodesic is Theta(log n). This does not settle unrestricted exterior dependence; it identifies coherence between ordinary exterior fibers as the obstruction. See Subsection Sharp logarithmic monochromatic paths under bounded exterior support.

**Stronger NORI3 extremal theorem (2026-10-10).** Every \(n\ge5\) has a legal coloring of genuine physical ordered three-faces for which **every monochromatic geodesic has at most \(2\lceil\log_2(n-1)\rceil+6\) moves**. Hence \(S_3(n)\ge\lceil(n-2)/(2\lceil\log_2(n-1)\rceil+4)\rceil-1=\Omega(n/\log n)\), superseding the multilevel \(\Omega(\sqrt n)\) lower bound asymptotically. The self-contained Subsection *Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament* derives this by an exact one-sentinel physical lift of the explicit Devine-Milans logarithmic-short-path (3,3)-tournament from their attached publication. The new algebraic identity is \(h_t(\widehat c,\widehat b,\widehat a)=1-h_t(a,b,c)\), ensuring short tight paths in **both** colors. The lift satisfies actual antipodal-reversal oddness, while the \(0,\varepsilon,1\) sentinel windows force the sentinel to an end of any monochromatic path. The scrapbook's antisymmetric \(\Omega(\sqrt n)\) theorem remains correct for boundary tournaments but is inapplicable to general NORI3 because its same-triple reversal condition is stronger. The new construction refutes a universal \(\Omega(\sqrt n)\) monochromatic-geodesic lower bound.

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

# Known obstructions after the Q9 refutation

**Global status (October 10, 2026).** The original unrestricted physical ordered-three-face NORI conjecture is **false**. A fully legal, unrooted \(Q_9\) counterexample is proved in *Dimension-nine counterexample to the physical ordered-three-face NORI conjecture* (foundational Subsection 6). Therefore the universal conclusion of any proposed extraction argument from only antipodal-reversal oddness is false. The mechanism-level counterexamples below are independently useful because they distinguish which weakened, rooted, conditional, or related statements fail. In particular, the earlier statement that the listed *mechanism obstructions* are not themselves unrooted counterexamples remains correct, while an actual unrooted counterexample is now known.

**No fixed-switch correction survives.** The fully elementary *Unbounded mandatory color changes from multilevel local minima* construction proves that for each \(r\ge3\), in all dimensions \(n\ge2r^2+r+1\) a legal antipodal-reversal-odd physical coloring forces at least \(2r-4\) changes on every full geodesic. Thus there is **no universal constant \(K\)** for which every legal coloring admits a full geodesic with at most \(K\) switches. Quantitatively, the worst-case minimum is at least \(\sqrt{2n}-O(1)\). This is an obstruction to a family of weakened universal conjectures, and is stronger in scope than the two-switch Q9 refutation.


---

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

**Flat maximal-defect one-move plateaus exist in every dimension \(n\ge7\).** An explicit position-independent, reversal-odd ordered-three-face coloring makes the identity order and each of its \(n-1\) adjacent swaps have the maximum \(n-3\) window-color changes, while another order is entirely monochromatic. All roots have the same word for each order. Thus strict descent in the raw switch count by one adjacent swap, even supplemented with arbitrary root changes, is *false*. The proof is the all-dimensional flat exchange-trap theorem in *Maximal geodesic blockers and snake exchanges*. It leaves neutral sequences, larger exchanges, and other global potentials open.\n\n**Sharp quantitative NORI3 refutations.** An exact 18,840-case reduction upgrades the Q15 three-class counterexample to minimum three switches. A further boundary-parity argument improves one-sentinel switch loss from two to one; the multilevel NORI3 coloring has exact minimum 2r-3 in dimension n>=2r²+r+1 (for each fixed class partition with >=2r+1 directions per class). Thus Q22, Q37 and Q56 admit constructed colorings with exact minima 3, 5 and 7. For every odd k>=3, the insertion loss improves from k-1 to k-2 and the forced-switch lower bound improves to 2r-2k+3. These are counterexamples to universal k-1 switch guarantees; they preserve the physical-face antipodal-reversal law and allow every direction interleaving.

### A legal Q15 counterexample to unrooted NORI via a three-class reversal-even word obstruction

# A legal Q15 counterexample to the unrooted NORI grand conjecture

## Main theorem

**Theorem.** There exists a binary coloring of the physical ordered three-faces of \(Q_{15}\) satisfying
\[
c(\bar F,(w,v,u))=1-c(F,(u,v,w))
\]
for every ordered three-face, for which **every** full antipodal geodesic has at least two changes among its thirteen consecutive ordered-three-face colors. Consequently, the unrooted NORI grand conjecture, as stated for all dimensions, is false.

The construction is explicit except for an arbitrary fixed linear order on fourteen distinguished coordinates. Its only finite verification has 252,252 ternary words and also admits an exact 1,427-state dynamic-programming evaluation.

## 1. Reversal-even three-letter obstruction

Let \(\Sigma=\{0,1,2\}\), and set
\[
h(a,b,c)=\begin{cases}
1,& b>\min\{a,c\}\ \text{or }(a,b,c)=(0,0,0),\\
0,&\text{otherwise}.
\end{cases}
\tag{1}
\]
In particular, \(h(a,b,c)=h(c,b,a)\).

**Lemma (four-switch ternary obstruction).** Every word \(q=q_1\cdots q_{14}\) with precisely four zeros, five ones, and five twos has at least four switches in its consecutive-triple word
\[
H(q)=(h(q_1,q_2,q_3),\ldots,h(q_{12},q_{13},q_{14})).
\tag{2}
\]
The bound is attained.

**Proof (exhaustive finite recurrence with reproducible certificate).** For a partial word, retain its three letter counts, last two letters, and last defined triple color. Appending \(w\) incurs one switch exactly when the old and newly defined triple colors differ. Thus the minimum number of switches to complete a prefix obeys the following backward recurrence. The sentinel 3 denotes an absent letter and the sentinel 2 denotes an absent triple color; neither is a letter of the word's alphabet in these states. This self-contained Python 3 implementation evaluates that finite recurrence exactly:

\`\`\`python
from functools import lru_cache

target = (4, 5, 5)

def h(a, b, c):
    return int(b > min(a, c) or (a == b == c == 0))

@lru_cache(None)
def minimum(counts, a, b, last):
    if counts == target:
        return 0
    candidates = []
    for c in range(3):
        if counts[c] == target[c]:
            continue
        current = h(a, b, c) if a != 3 else 2
        increment = int(last != 2 and current != 2 and last != current)
        updated = list(counts)
        updated[c] += 1
        candidates.append(
            increment + minimum(tuple(updated), b, c, current)
        )
    return min(candidates)

assert minimum((0, 0, 0), 3, 3, 2) == 4
\`\`\`

All legal completions are considered, because at each state the recurrence branches on each symbol whose multiplicity has not been exhausted. The terminal value is zero and the recursion strictly increases total multiplicity; induction on the number of letters remaining proves exactness. An independent direct enumeration of all \(14!/(4!5!5!)=252252\) words gives the histogram of switch counts
\[
\begin{array}{c|rrrrrrrr}
\text{switches}&4&5&6&7&8&9&10&11\\
\hline
\text{number of words}&314&3724&19802&51232&76938&64924&29730&5588
\end{array}
\]
with zero words of 0, 1, 2, or 3 switches. As one explicit equality witness, the word
\(00122001221112\) has triple-color word \(011100111000\), containing exactly four switches. \(\square\)

## 2. Explicit physical-face coloring

Partition a set \(D\) of fourteen distinct coordinate directions as
\[
D=D_0\sqcup D_1\sqcup D_2,\qquad
(|D_0|,|D_1|,|D_2|)=(4,5,5),
\]
and let \(\tau(d)=i\) for \(d\in D_i\). Adjoin a fifteenth direction, denoted \(s\), and fix any total ordering \(<\) of the fourteen directions in \(D\).

For a physical three-face \(F\), let \(z_s(F)\) be its fixed \(s\)-coordinate whenever \(s\) is not one of its three varying directions. Define the bit \(c(F,(u,v,w))\) as follows.

1. If \(u,v,w\in D\), put
\[
c(F,(u,v,w))=
z_s(F)\ \oplus\ h(\tau(u),\tau(v),\tau(w)).
\tag{3}
\]
2. If \(s\) is in the ordered triple, put
\[
c(F,(s,u,v))=1,\quad
c(F,(u,v,s))=0,\quad
c(F,(u,s,v))=\mathbf 1_{\{u>v\}} .
\tag{4}
\]
Here \(u,v\in D\) are distinct and the inequality is in the fixed total ordering.

These definitions depend only on the physical face and its ordered varying directions; in particular, they are independent of the traversing corner.

**Lemma (legality).** The coloring (3)--(4) is antipodal-reversal-odd.

**Proof.** If \(s\) is outside the ordered triple, the fixed \(s\)-coordinate flips when \(F\) is replaced by \(\bar F\), while \(h\) is reversal-even by (1); thus (3) complements. If \(s\) is first or last, reversal interchanges the first two cases of (4), whose values are 1 and 0. If \(s\) is middle, reversal interchanges the two distinct outside directions, so \(\mathbf1_{\{u>v\}}+\mathbf1_{\{v>u\}}=1\). These exhaust all ordered faces. \(\square\)

## 3. Every full antipodal geodesic has at least two changes

Fix an arbitrary root \(x\in\{0,1\}^{15}\) and any permutation \(p\) of the fifteen directions; it specifies an antipodal geodesic. Let \(k\in\{1,\ldots,15\}\) be the position of \(s\) in \(p\), and let \(q=(q_1,\ldots,q_{14})\) be the ordered list obtained by deleting \(s\) from \(p\).

Define \(H_i=h(\tau(q_i),\tau(q_{i+1}),\tau(q_{i+2}))\) for \(1\le i\le12\). By the four-switch lemma, \(H_1,\ldots,H_{12}\) has at least four switches.

Of the thirteen length-three windows in \(p\), the windows avoiding \(s\) appear in two contiguous segments. The first segment corresponds, in order, to
\[
H_1,\ldots,H_{k-3},
\]
and the second to
\[
H_k,\ldots,H_{12},
\]
where out-of-range intervals are empty. In the first segment, all the physical colors are \(H_i\oplus x_s\); in the second, they are \(H_i\oplus (1-x_s)\), because the \(s\)-coordinate flips once along the geodesic, when the direction \(s\) is traversed. Thus **every switch strictly inside either surviving segment is retained**.

Passing from the original twelve-term word \(H\) to those two segments deletes at most the two terms \(H_{k-2},H_{k-1}\), and therefore removes at most three of its adjacent comparisons. Consequently, for \(4\le k\le12\) the two surviving segments together retain at least \(4-3=1\) switch. In this range all three \(s\)-containing windows occur; by (4), their color word is
\[
0,\quad \varepsilon,\quad1,\qquad \varepsilon\in\{0,1\},
\]
which has an additional switch. The full geodesic therefore has at least two switches.

If \(k\notin\{4,\ldots,12\}\), then deleting the terms at positions \(k-2,k-1\) removes at most two actual comparisons of \(H\): the two deleted entries touch an end or are partly out of range. Hence the surviving segments already retain at least \(4-2=2\) switches, independently of the colors of any \(s\)-containing windows.

In every case, the full antipodal geodesic has at least two changes. The root and permutation were arbitrary, establishing the theorem. \(\square\)

## 4. Independent checks, scope, and consequence

A separate direct enumeration evaluates all \(252252\) three-class direction words, fifteen insertion positions for \(s\), both possible initial \(s\)-coordinate bits, and **both** possible middle-\(s\) window colors. Across \(252252\cdot15\cdot2\cdot2=15135120\) resulting color words there are zero with zero or one switch (indeed, the minimum is three in this finite enumeration). This second check allows an adversarial choice of the middle-\(s\) bit and so is stronger than the face rule (4) on the tested class words. A further independent direct physical-face implementation checked random antipodal ordered-face pairings and randomly rooted full geodesics. All agree with the mathematical proof above.

The construction refutes the **unrooted, unrestricted, antipodal-reversal-odd, physical ordered-three-face** grand conjecture already in dimension fifteen. It preserves the established Q5 and Q6 positive theorems; it does not claim dimension fifteen is minimal. The ternary finite lemma is the sole computer-assisted step, with complete recursion and direct enumeration cross-check given above.

The main conceptual point is that a reversal-even local triple word obstructed by four switches can be inserted across one distinguished exterior coordinate: at most three of its switches are lost, while the distinguished triple windows contribute the final forcing switch. This yields an actual physical-face counterexample rather than a prescribed-root obstruction.

## Sharpening: the exact minimum is three switches in Q15

**Theorem (sharp switch certificate).** For the physical coloring (3)--(4), *every* full antipodal geodesic has **at least three**, and some full antipodal geodesic has **exactly three**, consecutive ordered-three-face color changes. Thus this construction already refutes the proposed universal two-switch NORI3 bound in ambient dimension fifteen. The original two-switch lower bound above remains valid but is superseded by this strengthening.

**Proof and smaller complete certificate.** Write \(\sigma\) for the change count. The proved four-switch ordinary-word lemma gives \(\sigma(H)\ge4\), and the sentinel insertion inequality gives \(\sigma(C)\ge\sigma(H)-2\) for every sentinel position, initial sentinel bit \(z\), and arbitrary middle-sentinel bit \(\varepsilon\). Consequently, **only** ordinary class words with \(\sigma(H)=4\) could possibly produce \(\sigma(C)\le2\). There are exactly 314 such words among the \(14!/(4!5!5!)=252252\) ordinary class words, by the independently recorded histogram in Section 1.

The following standalone Python 3 certificate enumerates these 314 critical words, all fifteen sentinel slots and both choices each of \(z,\varepsilon\). It checks the stronger bound \(\sigma(C)\ge3\) for all \(314\cdot15\cdot4=18840\) cases:

~~~python
from itertools import combinations

def h(a,b,c):
    return int((a==b==c==0) or b>min(a,c))

def sw(bits):
    return sum(x != y for x,y in zip(bits,bits[1:]))

critical=0
checked=0
hist={}
for zeros in combinations(range(14),4):
    remain=[i for i in range(14) if i not in zeros]
    for ones in combinations(remain,5):
        q=[2]*14
        for i in zeros: q[i]=0
        for i in ones: q[i]=1
        H=[h(*q[i:i+3]) for i in range(12)]
        assert sw(H)>=4
        if sw(H)!=4: continue
        critical+=1
        for k in range(15):
            p=q[:k]+[3]+q[k:]
            for z in (0,1):
                for eps in (0,1):
                    C=[]
                    for j in range(13):
                        a,b,c=p[j:j+3]
                        if a==3: v=1
                        elif c==3: v=0
                        elif b==3: v=eps
                        else: v=z^(j>k)^h(a,b,c)
                        C.append(v)
                    t=sw(C)
                    assert t>=3
                    hist[t]=hist.get(t,0)+1
                    checked+=1

assert (critical,checked)==(314,18840)
assert hist=={3:1592,4:2632,5:13024,6:1136,7:456}
~~~

The bit \(\varepsilon\) is allowed adversarially, so this covers every actual choice induced by the strict order of the two ordinary directions adjacent to \(s\). In fact, equality is realized: an abstract direction-class order
\[
(0,s,0,1,2,2,0,0,1,2,2,1,1,1,2)
\]
with starting sentinel bit \(z=1\) and middle-sentinel bit \(\varepsilon=1\) has physical color word
\[
1111100111000
\]
and exactly three changes. Choose the first of the two adjacent class-0 directions greater than the second in the prescribed strict direction order to realize \(\varepsilon=1\); all directions are distinct and all classes retain their prescribed multiplicities. Other initial vertex bits are arbitrary. Therefore the actual physical minimum is **exactly three**. \(\square\)

**Relation to amplification.** The later multilevel construction forces four changes already on \(Q_{37}\) and unboundedly many as \(n\) grows. The present sharp \(Q_{15}\) result supplies a substantially smaller explicit violation of the conjectural NORI3 two-switch budget. No dimension-minimality claim is made.


### Dimension-nine counterexample to the physical ordered-three-face NORI conjecture

# A dimension-nine counterexample to the physical NORI conjecture

## Theorem

There exists a binary coloring of **physical ordered three-faces** of \(Q_9\) obeying
\[
c(\bar F,(w,v,u))=1-c(F,(u,v,w))
\]
for which **every** full antipodal geodesic has at least two color changes in its seven ordered-three-face windows. Thus the unrestricted, unrooted NORI grand conjecture is false already in dimension nine.

The proof is an explicit construction with a finite certificate of only 2,016 cases (56 binary class words, nine sentinel positions, two sentinel start bits, and two possible middle-sentinel colors). The enumeration below checks both middle-sentinel colors adversarially, making its conclusion independent of the chosen tie-break ordering.

## The coloring

Partition the nine coordinate directions as \(V=A\sqcup B\sqcup\{s\}\), where \(|A|=3\), \(|B|=5\), and \(s\) is a distinguished sentinel direction. Fix an arbitrary strict total order \(<\) on the eight directions in \(D=A\sqcup B\). Give directions in \(A\) type \(0\) and directions in \(B\) type \(1\), and write \(\tau:D\to\{0,1\}\).

Define the reversal-even ternary rule
\[
h(a,b,c)=\mathbf1_{\{(a,b,c)=(0,0,0)\ \text{or}\ [b=1\ \text{and}\ (a=0\text{ or }c=0)]\}},
\qquad h(a,b,c)=h(c,b,a).
\tag{1}
\]
For each physical ordered three-face \((F,(u,v,w))\), set
\[
c(F,(u,v,w))=
\begin{cases}
z_s(F)\oplus h(\tau(u),\tau(v),\tau(w)),& u,v,w\in D,\\
1,&u=s,\\
0,&w=s,\\
\mathbf1_{\{u>w\}},&v=s.
\end{cases}
\tag{2}
\]
Here \(z_s(F)\) is the fixed \(s\)-coordinate when \(s\notin\{u,v,w\}\). In the last three cases \(s\) is one of the varying directions, so no \(s\)-bit is needed. These cases are mutually exclusive. The rule is independent of any traversal corner within \(F\).

**Lemma 1 (legality).** The coloring in (2) satisfies the physical ordered-face antipodal-reversal law.

*Proof.* For triples avoiding \(s\), complementation flips the fixed bit \(z_s(F)\), and reversal leaves \(h\) unchanged. For triples containing \(s\) at an endpoint, reversal interchanges the constant values \(1\) and \(0\). For triples containing \(s\) in the middle, reversal interchanges distinct outside directions \(u,w\), and \(\mathbf1_{\{u>w\}}\oplus\mathbf1_{\{w>u\}}=1\). These cases exhaust all faces. \(\square\)

## Finite forcing lemma

For a word \(q=(q_1,\ldots,q_8)\in\{0,1\}^8\) with exactly three zeros and five ones, insert the sentinel symbol \(s\) at any position \(k\in\{1,\ldots,9\}\). Regard the resulting nine-letter word as a direction order. Choose a starting \(s\)-bit \(z\in\{0,1\}\), and an arbitrary \(\varepsilon\in\{0,1\}\) for the unique length-three window in which \(s\) is middle (if that window exists).

Give a length-three window avoiding \(s\) color \(h\) of its three letters, XOR \(z\) before the \(s\)-step, and XOR \(1-z\) after the \(s\)-step. Give windows containing \(s\) color \(1\) if \(s\) is first, \(0\) if \(s\) is last, and \(\varepsilon\) if \(s\) is middle.

**Lemma 2 (2,016-case certificate).** Every such seven-bit window-color word has at least two changes. More precisely, taking the minimum over all 56 words \(q\), both \(z\), and both \(\varepsilon\), the minima by sentinel position \(k=1,\ldots,9\) are
\[
(3,2,2,2,2,2,2,2,3).
\tag{3}
\]

*Proof.* The following self-contained Python 3 program exhausts all \(\binom83=56\) possible class words and all \(9\cdot2\cdot2\) insertion parameters. The first loop visits every possible triple of zero positions, the second loop every sentinel position, and the last two loops both binary choices. The window clauses implement exactly (1)--(2), so every relevant color comparison is evaluated. It computes the minima (3).

```python
from itertools import combinations

def h(a, b, c):
    return int((a == b == c == 0)
               or (b == 1 and (a == 0 or c == 0)))

minimum = [7] * 9
histogram = [0] * 7

for zeros in combinations(range(8), 3):
    q = [1] * 8
    for i in zeros:
        q[i] = 0
    for k in range(9):
        p = q[:k] + [2] + q[k:]   # sentinel = 2
        for z in (0, 1):
            for eps in (0, 1):
                colors = []
                for j in range(7):
                    a, b, c = p[j:j + 3]
                    if 2 not in (a, b, c):
                        colors.append(z ^ int(k < j) ^ h(a, b, c))
                    elif a == 2:
                        colors.append(1)
                    elif c == 2:
                        colors.append(0)
                    else:
                        colors.append(eps)
                switches = sum(colors[j] != colors[j + 1]
                               for j in range(6))
                minimum[k] = min(minimum[k], switches)
                histogram[switches] += 1

assert minimum == [3, 2, 2, 2, 2, 2, 2, 2, 3]
assert histogram == [0, 0, 112, 524, 812, 484, 84]
```

In particular no word with at most one switch occurs. The reported histogram independently specifies the entire 2,016-case distribution and provides an additional arithmetic check. \(\square\)

## From the finite lemma to every physical geodesic

Fix any starting vertex \(x\in Q_9\) and any ordering \(p\) of the nine distinct coordinate directions. Delete \(s\) from \(p\) and replace the eight remaining directions by their types; this gives a word \(q\) with three zeros and five ones. The position of \(s\) in \(p\) is \(k\), and its initial bit is \(z=x_s\).

For a window avoiding \(s\), its physical face has \(s\)-coordinate fixed at \(z\) before the \(s\)-move and \(1-z\) after that move. Therefore its color in (2) is precisely the color specified in Lemma 2. For a window containing \(s\), the first/last sentinel clauses of (2) likewise agree with Lemma 2. If \(s\) is middle, (2) selects one definite value \(\varepsilon\in\{0,1\}\) by comparing the two adjacent, distinct directions. Lemma 2 allows *either* value.

Consequently the actual seven-window color word of **every** rooted full antipodal geodesic appears among the finite words of Lemma 2 and has at least two changes. The starting vertex and full direction order were arbitrary, proving the theorem. \(\square\)

## Scope and relation to earlier constructions

This is an **unrooted counterexample in the exact active physical ordered-three-face model**. Its face color does not depend on traversal corner, and its legality uses antipodal reversal rather than ordinary reversal. The earlier \(Q_{15}\) three-class construction also provides a correct, independent finite certificate but is superseded as a dimension bound. Unconditional positive results in dimensions five and six remain true. This proof makes no minimal-dimension claim, and leaves dimensions seven and eight for separate consideration.

The structural obstruction is a reversal-even local direction-word rule shielded by one exterior sentinel bit; the sentinel-containing triples satisfy global oddness via order reversal, while the class-word switch constraints survive every possible sentinel insertion. This is a globally physical counterexample and removes the extraction premise of the proposed universal NORI theorem.

## Independent exhaustive physical-cube verification

Composition version 1 was independently audited in session session_nori_r4584_4. A separately written C++ implementation uses the literal triple truth table (1,0,1,1,0,0,1,0), labels A={0,1,2}, B={3,4,5,6,7}, s=8, and compares ordinary coordinate labels for the middle-sentinel clause. It checks all 32,256 ordered physical faces for antipodal-reversal oddness and all 258,048 choices of a face and traversal corner for corner independence. It then constructs the actual ten cube vertices of each of the 512 * 9! = 185,794,560 rooted full geodesics, derives each window's fixed-one mask by intersecting its four vertices, and evaluates its color directly. This enumeration uses no reduction to class words and no SAT solver.

The exact numbers of full rooted geodesics with 0 through 6 switches are respectively (0, 0, 10137600, 48476160, 75018240, 44421120, 7741440). The minima by sentinel position are (3,2,2,2,2,2,2,2,3). A minimum witness starts at the all-zero vertex with order (0,1,2,3,8,4,5,6,7) and color word 1000111. Independently reimplementing the reduced class-word check also reproduced the stated 2,016-case histogram. Thus the construction satisfies the exact physical-face hypotheses and excludes good full paths at every root.

Reproducible independent verifier (C++17; compile with optimization):

```cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
using namespace std;
// Physical face is encoded by its free-coordinate mask and fixed-one mask.
int color(int a,int b,int c,int fixed){
 if(a==8) return 1;
 if(c==8) return 0;
 if(b==8) return a>c;
 int A=a<3?0:1,B=b<3?0:1,C=c<3?0:1;
 // Explicit truth table indexed by the three class bits.
 const int table[8]={1,0,1,1,0,0,1,0};
 return ((fixed>>8)&1)^table[4*A+2*B+C];
}
int main(){
 long long faces=0,corners=0;
 for(int a=0;a<9;a++)for(int b=0;b<9;b++)for(int c=0;c<9;c++){
  if(a==b||a==c||b==c) continue;
  int free=(1<<a)|(1<<b)|(1<<c),outside=511^free;
  for(int fixed=0;fixed<512;fixed++)if((fixed&free)==0){
   int value=color(a,b,c,fixed);
   assert(value==0||value==1);
   assert(color(c,b,a,fixed^outside)==1-value);
   faces++;
   for(int bits=free;;bits=(bits-1)&free){
    int root=fixed|bits;
    assert(color(a,b,c,root&outside)==value);corners++;
    if(bits==0)break;
   }
  }
 }
 array<int,9> p={0,1,2,3,4,5,6,7,8};
 array<long long,7> hist={};array<int,9> mins;mins.fill(7);
 long long paths=0;int witnessRoot=-1;array<int,9>witness;array<int,7>wcolors;
 do{
  int slot=find(p.begin(),p.end(),8)-p.begin();
  for(int root=0;root<512;root++){
   // Traverse actual cube vertices. Derive each face from its four vertices.
   array<int,10> v;v[0]=root;
   for(int j=0;j<9;j++)v[j+1]=v[j]^(1<<p[j]);
   assert(v[9]==(root^511));
   array<int,7> colors;
   for(int j=0;j<7;j++){
    int free=v[j]^v[j+3];
    int fixed=v[j]&v[j+1]&v[j+2]&v[j+3];
    assert((fixed&free)==0);
    colors[j]=color(p[j],p[j+1],p[j+2],fixed);
   }
   int changes=0;for(int j=1;j<7;j++)changes+=(colors[j]!=colors[j-1]);
   assert(changes>=2);hist[changes]++;paths++;mins[slot]=min(mins[slot],changes);
   if(changes==2&&witnessRoot<0){witnessRoot=root;witness=p;wcolors=colors;}
  }
 }while(next_permutation(p.begin(),p.end()));
 cout<<"ordered physical faces "<<faces<<"; corner checks "<<corners<<"; full rooted paths "<<paths<<"\n";
 cout<<"histogram ";for(auto x:hist)cout<<x<<' ';cout<<"\nminima ";for(auto x:mins)cout<<x<<' ';
 cout<<"\nwitness root "<<witnessRoot<<" order ";for(auto x:witness)cout<<x<<' ';cout<<" colors ";for(auto x:wcolors)cout<<x;cout<<'\n';
}

```


### Hereditary sentinel-word contraction and NORI counterexamples in every dimension at least nine

# Hereditary sentinel-word contraction and counterexamples in all dimensions \(n\ge9\)

## Theorem

**Theorem.** For every integer \(n\ge9\), there is a legal antipodal-reversal-odd coloring of the physical ordered three-faces of \(Q_n\) for which **every** full antipodal geodesic has at least two ordered-three-face color changes. Consequently the unrooted NORI grand conjecture fails in *each* dimension \(n\ge9\).

This strengthens the explicit \(Q_9\) counterexample in *A dimension-nine counterexample to the physical NORI conjecture* by a dimension-free contraction principle. The finite \(Q_9\) obstruction requires only 2,016 comparisons; the new hereditary lemma is certified by 22,272 local comparisons of length at most seven, independently of \(n\).

## 1. The abstract sentinel word

Use symbols \(0,1,s\), with exactly one \(s\) in each word. Define the reversal-even triple rule on ordinary symbols by
\[
h(a,b,c)=\mathbf1_{\{(a,b,c)=(0,0,0)\ \mathrm{or}\ [b=1\ \mathrm{and}\ (a=0\ \mathrm{or}\ c=0)]\}}.
\]
Fix two bits \(z,\varepsilon\). For any word \(w=(w_1,\ldots,w_m)\) containing exactly one \(s\), define its \((m-2)\)-term color word \(C_{z,\varepsilon}(w)\) as follows. For each ordered triple \((w_j,w_{j+1},w_{j+2})\),

* if it avoids \(s\), its color is \(h(w_j,w_{j+1},w_{j+2})\oplus z\oplus\mathbf1_{\{s\text{ precedes the triple}\}}\);
* if \(s\) is first, its color is \(1\);
* if \(s\) is last, its color is \(0\);
* if \(s\) is middle, its color is \(\varepsilon\).

When no sentinel appears in a local subword, use \(h\oplus z\) for every triple there. Let \(V_{z,\varepsilon}(w)\) be the number of adjacent color differences in this word (zero when it has fewer than two colors).

**Deletion lemma.** If \(d\ne s\) is any occurrence of an ordinary letter in \(w\), and \(w\setminus d\) is the word obtained by deleting that occurrence, then
\[
V_{z,\varepsilon}(w\setminus d)\le V_{z,\varepsilon}(w).
\tag{1}
\]

**Proof.** A color difference between two adjacent triple windows is determined by their four consecutive letters, the position of the unique sentinel relative to them, and the fixed bits \(z,\varepsilon\). Deleting a letter at position \(k\) leaves every four-letter comparison unaffected except those whose original four-letter window contains position \(k\), or whose new window joins the two sides of that position. All affected letters lie in the at-most-seven-letter interval from \(k-3\) through \(k+3\). Comparisons outside this interval correspond one-to-one with identical old and new comparisons.

If \(s\) lies outside the interval, every affected ordinary triple has the same exterior-\(s\) parity, before and after deletion. The resulting comparisons are therefore identical to the no-sentinel local model, up to a common bit complement that preserves changes. If \(s\) lies inside the interval, its local position and the two bits \(z,\varepsilon\) determine the affected comparisons exactly as in the abstract model. Thus it is sufficient to verify (1) for all words of lengths four through seven over \(\{0,1\}\), with either no sentinel or one sentinel, for all sentinel positions, both \(z\), both \(\varepsilon\), and every ordinary deletion position. Lengths at most three are immediate.

Here is a complete, executable finite certificate, with no external library or solver. The four sizes require respectively \(640,1920,5376,14336\) checks; their sum is \(22272\).

~~~python
from itertools import product

def h(a, b, c):
    return int((a == b == c == 0) or
               (b == 1 and (a == 0 or c == 0)))

def changes(w, z, eps):
    s = w.index(2) if 2 in w else -1
    colors = []
    for j in range(len(w) - 2):
        a, b, c = w[j:j + 3]
        if a == 2:
            colors.append(1)
        elif c == 2:
            colors.append(0)
        elif b == 2:
            colors.append(eps)
        else:
            colors.append(h(a, b, c) ^ z ^
                          int(s >= 0 and j > s))
    return sum(a != b for a, b in
               zip(colors, colors[1:]))

checks = 0
for n in range(4, 8):
    for slot in [-1] + list(range(n)):
        for q in product((0, 1),
                         repeat=n - int(slot >= 0)):
            w = (list(q) if slot == -1 else
                 list(q[:slot]) + [2] + list(q[slot:]))
            for z in (0, 1):
                for eps in (0, 1):
                    before = changes(w, z, eps)
                    for k in range(n):
                        if w[k] == 2:
                            continue
                        after = changes(w[:k] + w[k + 1:],
                                        z, eps)
                        assert after <= before
                        checks += 1
assert checks == 22272
~~~

This exhausts the local cases and proves the deletion lemma for arbitrary word length. \(\square\)

## 2. All-dimensional legal physical-face coloring

Let \(n\ge9\), partition the coordinate directions into
\[
V=A\sqcup B\sqcup\{s\},\qquad |A|=3,\quad |B|=n-4\ge5,
\]
and assign types \(0\) to \(A\) and \(1\) to \(B\). Fix any strict total order on \(A\sqcup B\).

For a physical ordered three-face \((F,(u,v,w))\), define
\[
c(F,(u,v,w))=
\begin{cases}
z_s(F)\oplus h(\tau(u),\tau(v),\tau(w)),&s\notin\{u,v,w\},\\
1,&u=s,\\
0,&w=s,\\
\mathbf1_{\{u>w\}},&v=s .
\end{cases}
\tag{2}
\]
The first case uses the fixed \(s\)-bit of the face. Each case depends solely on the physical face and free-coordinate order, never on the traversal corner.

**Legality.** For triples avoiding \(s\), antipodal complementation flips \(z_s(F)\), while reversal preserves \(h\). For triples with \(s\) first or last, reversal interchanges the complementary constants \(1,0\). For triples with \(s\) middle, reversal interchanges two distinct ordinary directions, complementing the strict-order indicator. Thus \(c(\bar F,(w,v,u))=1-c(F,(u,v,w))\) for every face.

**No good geodesic.** Fix any root and any full direction order. Replace the ordinary directions by their types, leaving the sentinel in place. The actual physical window-color word is precisely \(C_{z,\varepsilon}(w)\) for \(z\) equal to the root's \(s\)-bit and \(\varepsilon\) equal to the order comparison between the two directions adjacent to \(s\) (when this middle window exists). Delete \(n-9\) occurrences of type \(1\), leaving a nine-letter abstract word with three zeros, five ones, and one sentinel, while retaining the same formal \(z,\varepsilon\). Repeated application of (1) gives
\[
V_{z,\varepsilon}(w)\ \ge\
V_{z,\varepsilon}(w_{\mathrm{reduced}}).
\]
The exact \(Q_9\) finite certificate (*A dimension-nine counterexample to the physical NORI conjecture*) checks all \(\binom83\cdot9\cdot2\cdot2=2016\) possible reduced words and parameters and proves that the right side is at least two. Hence every rooted full geodesic for (2) has at least two changes. \(\square\)

## 3. Significance

The hereditary lemma identifies the missing dimension-lifting mechanism for the explicit sentinel construction. Rather than embedding a finite forcing *proof* with inconsistent exterior-bit holonomy, it enlarges a globally legal counterexample while retaining a monotone obstruction under deletion of ordinary direction occurrences. The chosen total order on distinct directions realizes one value of \(\varepsilon\); allowing both values in the reduced certificate makes the proof independent of the changing identities adjacent to the sentinel.

The original \(Q_9\) physical-face proof remains the base case. The \(Q_{15}\) three-class construction and its independent verification remain valid historical certificates but are dimensionally superseded. This argument establishes failure for every \(n\ge9\); dimensions \(7\) and \(8\) are not decided by it.

### Scope of distinguished-coordinate counterexamples and edge-order realizability

# Scope of the distinguished-coordinate construction and edge-order realizability

The dimension-nine NORI counterexample separates physical ordered-three-face colorings from two more constrained structures: lower-arity distinguished-coordinate colorings and boundary 3-tournaments. This subsection proves the relevant distinctions. It establishes no counterexample to general NORI1 or NORI2.

## The one-face distinguished-coordinate family always has a monochromatic antipodal geodesic

Let the cube directions be D together with s. For every ordinary direction d in D choose a bit a_d, and color its physical edges by c_d(x)=x_s XOR a_d. Color each s-edge by g(x_D), where g(complement y)=1-g(y). These are legal undirected antipodally odd edge colors.

**Proposition.** Every such coloring admits a monochromatic full antipodal geodesic.

**Proof.** Let D_0 and D_1 be the directions with a_d=0 and a_d=1. Choose z in {0,1} and y with g(y)=z; antipodal oddness guarantees such y. Set x_s=z and x_D=y XOR D_0. Traverse all directions in D_0, then s, then all directions in D_1. Before s, each ordinary edge has color z. The s-edge is traversed at ordinary-coordinate vector y and also has color z. After s, each ordinary edge has color (1-z) XOR 1=z. Every direction occurs once. This covers empty D_0 or D_1 as well. QED.

## The two-face distinguished-coordinate family always has a one-switch antipodal geodesic

Here NORI2 means binary colors of ordered physical squares satisfying c(complement F,(b,a))=1-c(F,(a,b)).

**Lemma.** Every binary coloring of the edges of a complete graph has a Hamilton vertex order whose consecutive edge colors change at most once.

**Proof.** Maintain vertex-disjoint paths R and B covering the vertices already inserted, with all R-edges color 0 and all B-edges color 1; either path may be empty. To insert x with both paths nonempty, write r,b for their final vertices. If rx has color 0, append x to R. If bx has color 1, append x to B. In the remaining case rx has color 1 and bx color 0. If rb has color 0, remove b from B and append b,x to R. If rb has color 1, remove r from R and append r,x to B. Every operation preserves the path colors and disjoint coverage. With one path empty, append x to the other if its endpoint edge has the required color, and otherwise put x alone in the empty path. Begin with one singleton path. Finally concatenate R and B. The connecting edge has one of the two colors, so the resulting edge word has at most one change. QED.

Let h(a,b)=h(b,a) be any binary edge coloring on D. Define ordered-square colors by
- c(F,(a,b))=z_s(F) XOR h(a,b) for a,b in D;
- c(F,(s,a))=1;
- c(F,(a,s))=0.

**Proposition.** Every such legal NORI2 coloring has a good full antipodal geodesic.

**Proof.** Symmetry of h and the complementary endpoint constants verify the combined antipodal-reversal law. Choose a Hamilton order d_1,...,d_m of D supplied by the lemma. Traverse (s,d_1,...,d_m). Its square colors are 1 followed by (1-z) XOR h(d_i,d_{i+1}), where z is the initial s-bit. For m>=2 choose z=h(d_1,d_2). Then the initial 1 agrees with the first ordinary square color, and the remainder has at most one change. The cases m<=1 are immediate. QED.

These propositions rule out the direct lower-arity versions of this construction in every dimension. They leave more general reductions and colorings open.

## Boundary 3-tournaments are orientations of a line graph

A boundary 3-tournament on V chooses exactly one of (a,b,c) and (c,b,a) for every triple of distinct vertices with specified middle vertex b. Call the chosen triples right.

**Proposition.** Boundary 3-tournaments on V correspond bijectively to orientations of the line graph L(K_V).

**Proof.** Vertices of L(K_V) are unordered pairs ab. Its adjacent vertices ab and bc share a unique vertex b. Orient ab -> bc exactly when (a,b,c) is right. Reversal of the triple reverses this one line-graph edge. Every adjacency corresponds to exactly one such reversal pair, proving the bijection. QED.

**Corollary (exact edge-order realizability).** A boundary 3-tournament arises from one strict ordering of the edges of K_V, with (a,b,c) right precisely when ab < bc, if and only if the corresponding orientation of L(K_V) is acyclic.

**Proof.** An edge ordering is a strictly increasing potential on every directed line-graph edge, which forbids directed cycles. Conversely a topological ordering of any finite acyclic orientation orders the vertices of the line graph, hence the original graph edges, and realizes every specified comparison. QED.

For a noncomplete graph G the same statement holds for the partial triple system on actual two-edge paths. An increasing vertex-simple path in G is exactly a sequence of distinct original vertices whose successive original edges form a directed line-graph path. Arbitrary directed paths in the line graph need not have this property: they may repeatedly pass through the same original vertex. Thus the original path-incidence and vertex-distinctness constraints remain essential.

Transitivity of the comparison tournament at each individual middle vertex is necessary but insufficient for global realizability. Already on three vertices the comparisons ab<bc, bc<ca, ca<ab give a cycle while each individual vertex has only two incident edges and hence a transitive local comparison.

## Why the NORI3 example gives no immediate boundary-tournament or increasing-path bound

In the distinguished-coordinate NORI3 construction, for every ordered face avoiding s,
c(F,(a,b,c))=z_s(F) XOR h(a,b,c),
where h(a,b,c)=h(c,b,a).
Thus a triple and its reverse have the same color at that face. A boundary 3-tournament requires opposite memberships. The three-class auxiliary rule of the Q15 example also has this reversal-even property.

Consequently the construction supplies no boundary 3-tournament under the direction-triple identification, and supplies no edge ordering through the comparison representation above. Any further transfer would have to prove its own preservation of admissible paths and quantify the relation between path lengths or covering numbers. No new extremal bound for those classes follows here.

## A candidate additional symmetry

One possible class for future investigation imposes, besides the combined NORI k-face law,
c(F,reverse pi)=c(F,pi) XOR rho_k, where rho_k=binom(k,2) mod 2.
The combined law then gives c(complement F,pi)=c(F,pi) XOR (1 XOR rho_k).

For k=1 the added reversal identity is automatic and retains every NORI1 coloring. For k=3 it retains all direction-only boundary 3-tournaments and requires antipodal invariance with the order fixed. It excludes the present distinguished-coordinate counterexamples. Only reversal is prescribed; other permutations of directions remain free. This is a candidate class, with no general existence theorem asserted.


### Unbounded mandatory color changes from multilevel local minima

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


### Unbounded compulsory switches for every odd ordered-face dimension

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


### Unbounded compulsory switches for every even ordered-face dimension

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

### NORI2 sentinel barrier and exact one-switch examples

# NORI2 sentinel barrier: one-switch closure for all symmetric direction-pair rules

## Main theorem

**Theorem A (complete one-sentinel family).** Let \(n\ge3\). Fix one distinguished coordinate \(s\), and let \(D=V(Q_n)\setminus\{s\}\) denote the set of the other **coordinate directions**. Let \(h:D^{(2)}\to\{0,1\}\) be any symmetric binary function of two distinct ordinary directions:
\[
h(u,v)=h(v,u).
\]
For an ordered physical two-face \(F\) with ordered free directions \((u,v)\), define
\[
c(F,(u,v))=
\begin{cases}
z_s(F)\oplus h(u,v),&s\notin\{u,v\},\\
1,&u=s,\\
0,&v=s.
\end{cases} \tag{1}
\]
Then (1) satisfies the antipodal-reversal law, and there is a full antipodal geodesic whose consecutive two-face colors change at most **once**.

This applies to arbitrary symmetric direction-pair rules, arbitrary direction multiplicities/classes, and any ambient dimension. Thus the direct one-sentinel mechanism that gives unbounded obligatory changes for NORI3 **cannot disprove the proposed one-switch NORI2 bound**.

**Proof of legality.** For a square avoiding \(s\), its antipodal square has the opposite fixed \(s\)-bit; reversing the ordered pair preserves \(h\). For squares containing \(s\), reversal exchanges the two clauses 1 and 0. The color is independent of traversal corner in all cases. \(\square\)

## Two-color complete-graph path lemma

**Lemma (Gerencsér–Gyárfás, with elementary proof).** Every red/blue coloring of the edges of a finite complete graph admits a Hamiltonian path whose edge-color word changes at most once.

**Proof.** Maintain disjoint red and blue paths \(R\) and \(B\) covering the vertices handled so far; a path of one vertex is permitted, and either path may be empty. The invariant is initially trivial. Let \(v\) be the next vertex. If one path is empty, append \(v\) to the nonempty path when their joining edge has its designated color, otherwise create the other path as singleton \(v\). If both are nonempty, let \(r,b\) be their final vertices. If \(vr\) is red, append \(v\) to \(R\). If \(vb\) is blue, append \(v\) to \(B\). Otherwise \(vr\) is blue and \(vb\) red. If \(rb\) is red, remove \(b\) from the blue path \(B\) and extend \(R\) by the consecutive edges \(rb,bv\), both red. If \(rb\) is blue, remove \(r\) from \(R\) and extend \(B\) by \(br,rv\), both blue. In all cases the paths remain disjoint, monochromatic in their respective colors, and now cover one more vertex. By induction they partition the complete vertex set.

If both paths are nonempty, concatenate \(R\) and \(B\) using their one joining edge. Its color is necessarily red or blue, so the concatenated Hamiltonian path has a red segment followed by a blue segment, with at most one change. If one path is empty, the other is already a monochromatic Hamiltonian path. \(\square\)

This lemma is the classical 1967 Gerencsér–Gyárfás path-partition theorem; the constructive proof above is included to make the NORI consequence self-contained.

**Proof of Theorem A.** Apply the lemma to the complete graph on the ordinary directions \(D\), coloring each edge \(\{u,v\}\) by \(h(u,v)\). Choose an ordering \(q=(q_1,\ldots,q_{n-1})\) whose pair-color word
\[
H=(h(q_1,q_2),\ldots,h(q_{n-2},q_{n-1}))
\]
has at most one change. Traverse the \(n\) coordinates in the order \((s,q_1,\ldots,q_{n-1})\). The first ordered square has free directions \((s,q_1)\) and color 1. After the first step, the fixed \(s\)-bit is \(1-z\), where \(z\) is the root's initial \(s\)-bit. All later square-window colors equal
\[
1\oplus z\oplus H_1,\;\ldots,\;1\oplus z\oplus H_{n-2}.
\]
Choose the starting vertex with \(z=H_1\) (all other root bits arbitrary). The initial two square colors are then both 1, and the remainder has exactly the color changes of \(H\). Hence the full square-color word has at most one change. \(\square\)

## Sharpness inside the one-sentinel family

**Theorem B.** For every \(n\ge5\), there is a coloring of the form (1) for which every full antipodal geodesic has at least one change. Thus the universal bound of Theorem A is exact for this family.

**Proof.** Partition the \(n-1\) ordinary directions into \(A\sqcup\{b\}\) with \(|A|=n-2\ge3\), and set \(h(u,v)=0\) for \(u,v\in A\), and \(h(u,b)=h(b,u)=1\) for \(u\in A\). The color-0 complete-graph edges form a clique on \(A\) and isolate \(b\). The color-1 graph is a star centered at \(b\), with at least three leaves. Neither graph contains a Hamiltonian path, so for **every** order \(q\) of the ordinary directions, its adjacent-pair color word \(H\) has at least one change.

For a full cube geodesic with \(s\) in the first position, its later ordinary pair windows give \(H\) up to uniform complementation, and therefore at least one change. The same holds if \(s\) is last. If \(s\) is at an interior position, the two successive square windows containing \(s\) have free-direction orders \((u,s)\) and \((s,v)\) and colors \(0,1\), giving an unavoidable change. Thus every root and every full direction order has at least one switch. By Theorem A, some full path has exactly one. \(\square\)

## Further comparison: direction-only legal NORI2 colorings

**Theorem C.** Suppose a legal physical ordered-two-face coloring is independent of all fixed exterior face bits, so \(c(F,(u,v))=g(u,v)\) depends only on the ordered free directions. Then there is a **monochromatic** full antipodal geodesic.

**Proof.** Legality gives \(g(v,u)=1-g(u,v)\); hence \(u\to v\) whenever \(g(u,v)=1\) defines a tournament on the coordinate directions. Every tournament has a directed Hamiltonian path (Rédei's theorem). For completeness, the elementary insertion proof starts with one directed path; a new vertex can be inserted at its beginning if it dominates the first vertex, at its end if dominated by the last, or between two successive vertices where the preceding vertex dominates it and it dominates the following vertex. Inserting vertices successively yields a directed Hamiltonian path. Traversing its direction order gives color 1 in every consecutive square, at any root. \(\square\)

## Scope and implications for the proposed switch hierarchy

Theorem B realizes the predicted NORI2 budget of one exactly; Theorem A shows that any attempted amplification based solely on a reversal-even pair rule and a single exterior sentinel bit necessarily collapses to that budget. In contrast, the higher odd-\(k\) construction uses a central triple with a local-minimum run-count obstruction. The obstruction has no analog for a symmetric *pair* rule because the two-colored complete graph admits a Hamiltonian order with at most one color change.

These are exact statements for two explicitly defined subfamilies of legal colorings. They do **not** establish the unrestricted NORI2 conjecture: arbitrary physical two-face colors may depend on many exterior coordinates, and no direction-only complete-graph reduction then applies. Likewise they do not settle unrestricted NORI1; the NORI1 path-rotation mechanism concerns antipodally odd physical edges rather than ordered squares.

Literature: L. Gerencsér and A. Gyárfás (1967), the red/blue vertex-disjoint path-partition theorem; L. Rédei (1934), the tournament Hamiltonian-path theorem.

### Bounded NORI2 switches from finite exterior-coordinate support

# Bounded NORI2 switches from finite exterior-coordinate support

## Theorem

Let \(V\) be the \(n\) coordinate directions of \(Q_n\), let \(S\subseteq V\) have \(t\) elements, and put \(D=V\setminus S\). Suppose a binary coloring \(c(F,(u,v))\) is defined on **physical ordered squares** and has the following exterior-support property:

**(ES)** For every two ordered distinct directions \(u,v\in D\), the value \(c(F,(u,v))\) depends only on the ordered pair \((u,v)\) and on the \(t\) fixed bits \(z_S(F)\) of \(F\) in directions in \(S\). In particular it is independent of all other exterior fixed bits. There is no condition whatsoever on colors of squares meeting \(S\).

**Theorem (finite-support NORI2 bound).** Under (ES), there exists a full antipodal geodesic whose ordered-square color word has at most
\[
\boxed{t+1}
\]
switches. This holds for every \(n\) and every such physical coloring, with **no antipodal-reversal hypothesis needed**. Consequently it holds for legal NORI2 colorings satisfying (ES).

In particular:
- One distinguished exterior direction, allowing *arbitrary directed* pair rules and arbitrary colors of squares containing that direction, guarantees at most two changes.
- Two distinguished exterior directions, allowing arbitrary nonlinear interactions of their exterior bits and arbitrary square colors meeting either direction, guarantee at most three changes.
- Every family with an exterior dependence support of fixed size \(t\) has a switch budget bounded independently of ambient dimension.

The sharp previously established one-switch theorem for a **symmetric pair rule with one sentinel** is stronger under its additional hypotheses. The present bound is intentionally independent of reversal symmetry of the ordinary pair function.

## Raynaud's directed two-color Hamiltonian path theorem

**Lemma (Raynaud, 1973; Hamilton path consequence).** Let \(D\) be a finite set, and arbitrarily color each **ordered pair** \((u,v)\), \(u\ne v\), red or blue. There is a Hamiltonian vertex order \((q_1,\dots,q_m)\) in which the consecutive arc-color word
\[
h(q_1,q_2),\dots,h(q_{m-1},q_m)
\]
has at most one change.

**Proof from Raynaud's theorem.** Raynaud's directed result says that every red/blue arc coloring of a complete symmetric digraph has a directed Hamiltonian cycle expressible as one red directed path and one blue directed path (monochromatic cases permitted). The edge colors therefore form at most two monochromatic runs cyclically. Delete one arc at a transition between those runs. The remaining directed Hamiltonian path has at most one switch. If the cycle is monochromatic, delete any arc. For \(m\le2\), the claim is immediate.

This directed lemma allows \(h(u,v)\) and \(h(v,u)\) to be completely unrelated; the undirected Gerencsér–Gyárfás path-partition lemma only covers symmetric \(h\). Raynaud's theorem is a published external input. One source explicitly stating it is A. Gyárfás, *Vertex covers by monochromatic pieces — a survey*, Theorem 2, which attributes the directed Hamiltonian-cycle result to Raynaud (1973). The same result appears as Theorem 2.1 in Ben-Eliezer et al., *The size Ramsey number of a directed path*, Journal of Combinatorial Theory, Series B **102** (2012).

## Proof of the NORI2 theorem

Let \(S=(s_1,\dots,s_t)\) be any order of the special directions. Fix any initial cube vertex \(x\). After traversing each member of \(S\) once, the fixed \(S\)-bit vector on subsequent ordinary squares is
\[
 \beta = \bigl(1-x_{s_1},\dots,1-x_{s_t}\bigr).
\]
By (ES), for each ordered pair \(u,v\in D\) the color of **every physical square** with ordered free directions \((u,v)\) and fixed \(S\)-bits \(\beta\) is a well-defined bit
\[
 h_\beta(u,v)\in\{0,1\}. \tag{1}
\]
No symmetry is assumed between \(h_\beta(u,v)\) and \(h_\beta(v,u)\).

Apply Raynaud's lemma to this 2-coloring of all directed arcs on \(D\). Obtain an order \(q=(q_1,\dots,q_m)\) of the \(m=n-t\) ordinary coordinates for which the adjacent-pair color word
\[
 H=(h_\beta(q_1,q_2),\dots,h_\beta(q_{m-1},q_m))
 \tag{2}
\]
has at most one change.

Traverse the complete direction permutation
\[
 p=(s_1,\dots,s_t,q_1,\dots,q_m)
 \tag{3}
\]
from the chosen cube root \(x\). For every consecutive ordered-square window entirely inside the ordinary \(q\)-block, its physical fixed \(S\)-bits are exactly \(\beta\); therefore its color equals the corresponding entry of \(H\) in (2), regardless of exterior bits on the other ordinary directions, by (ES). The suffix of the actual full square-color word thus contributes at most one internal switch.

When \(t\ge1\), precisely the first \(t\) consecutive ordered-square windows in (3) meet \(S\): their free direction pairs are
\[
 (s_1,s_2),\dots,(s_{t-1},s_t),(s_t,q_1).
 \tag{4}
\]
For \(t=1\), only \((s_1,q_1)\) occurs. The colors of these \(t\) windows can be *arbitrary*, contributing at most \(t-1\) internal switches. The transition from the last window in (4) to the first ordinary window contributes at most one further switch. Therefore
\[
 \sigma(c(P)) \le (t-1)+1+1=t+1. \tag{5}
\]
For \(t=0\), the complete word is \(H\) and has at most one switch. If \(D\) has zero or one coordinate, the full word is too short to violate the claimed bound. This covers all cases.

Crucially, the argument evaluates each window as an actual **physical square with its correct fixed exterior bits**; the prefix of special directions is a genuine cube geodesic, and the ordinary suffix is a genuine simple Hamilton order of distinct directions. There is no root or coordinate-interleaving assumption. \(\square\)

## Implications for the NORI hierarchy

The multilevel NORI3 amplification uses a constant number of sentinel directions but a *ternary* local-minimum statistic, whose mandatory changes grow unboundedly with the number of direction classes. The present theorem proves a qualitatively different phenomenon for **square** colorings: the same finite-support architecture has a uniform switch bound, even if the ordinary ordered-pair rule is asymmetric and the colors of special-direction squares are otherwise unconstrained.

Therefore a putative NORI2 coloring forcing an **unbounded** number of switches must have unbounded minimal exterior-coordinate support (in the precise sense (ES)) as \(n\to\infty\). A coloring forcing **two** switches might already exist with one or two exterior directions; (5) does not decide this. The sharp symmetric-pair one-sentinel result rules out a two-switch obstruction in that restricted subfamily. Nor does (5) settle unrestricted NORI2, where ordinary squares can depend on arbitrarily many exterior coordinate bits.

## References

A. Gyárfás, *Vertex covers by monochromatic pieces — a survey*, Theorem 2 (Raynaud's 1973 directed two-color Hamiltonian-cycle theorem), accessible at https://www.renyi.hu/~gyarfas/Cikkek/172_krakowrev3.pdf.

The directed statement is also quoted as Theorem 2.1 in *The size Ramsey number of a directed path*, Journal of Combinatorial Theory, Series B **102** (2012), 743–755.

### Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament

# Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament

## Theorem: near-linear compulsory switches

**Theorem.** For every \(n\ge5\) there exists a legal coloring of genuine **physical ordered three-faces** of \(Q_n\), with
\[
c(\bar F,(w,v,u))=1-c(F,(u,v,w)),
\tag{1}
\]
such that every monochromatic coordinate-geodesic uses at most
\[
L(n)=2\lceil\log_2(n-1)\rceil+6
\tag{2}
\]
coordinate moves. Consequently every full antipodal geodesic has at least
\[
\boxed{\left\lceil\frac{n-2}{2\lceil\log_2(n-1)\rceil+4}\right\rceil-1}
\tag{3}
\]
color changes. In particular, \(S_3(n)=\Omega(n/\log n)\). This disproves the conjecture that every legal NORI3 coloring possesses a monochromatic geodesic of length \(\Omega(\sqrt n)\).

The source input is the explicit \((3,3)\)-tournament in R. C. Devine and K. G. Milans, *Tight paths in fully directed hypergraphs*, uploaded main-appendix manuscript, Theorem (33)-upper. That theorem constructs a tournament on \(\mathbb F_2^t\) with all directed tight paths of order at most \(2t+4\). The new steps are a **complement-reversal self-duality** of that tournament and a legal one-sentinel physical NORI3 lift preserving both colors' short-path bounds.

## The source (3,3)-tournament

Fix \(t\ge2\). For three distinct binary strings \(a,b,c\in B_t=\{0,1\}^t\), let \(\alpha(a,b,c)\) be the first coordinate where the three strings are not all equal; two strings agree at \(\alpha\). Let \(\beta>\alpha\) be the first coordinate where those two agreeing strings disagree. Such a coordinate exists.

Define \(h_t(a,b,c)=1\) precisely when the ordered strings' bit-matrix rows satisfy one of:
\[
\begin{array}{ll}
P_1:&\alpha\text{-row }010,\\
P_2:&\alpha\text{-row }001,\quad
 (\beta\text{-bits of }a,b)=01,\\
P_3:&\alpha\text{-row }011,\quad
 (\beta\text{-bits of }b,c)=10,\\
P_4:&\alpha\text{-row }110.
\end{array}
\tag{4}
\]
The remaining beta bits are unrestricted. Every unordered triple has exactly three positive permutations, as in the source manuscript. Its proved upper-bound theorem is:
\[
\text{Every vertex-simple all-positive tight path in }h_t
\text{ has order at most }M_t=2t+4.
\tag{5}
\]

## The self-duality lemma

Write \(\widehat a\) for bitwise complement of \(a\). Then
\[
\boxed{h_t(\widehat c,\widehat b,\widehat a)=1-h_t(a,b,c)}
\tag{6}
\]
for all distinct \(a,b,c\).

**Proof.** Both \(\alpha\) and \(\beta\) are preserved by simultaneously reversing the ordered three strings and complementing all their bits. The first-disagreement row undergoes reverse-complement, interchanging \(010\leftrightarrow101\), \(110\leftrightarrow100\), and \(001\leftrightarrow011\). The first two exchanges change automatic acceptance (patterns \(P_1,P_4\)) into automatic rejection. For row \(001\), acceptance is \((a_\beta,b_\beta)=(0,1)\); after reverse-complement the transformed row is \(011\), whose acceptance under \(P_3\) means \((1-b_\beta,1-a_\beta)=(1,0)\), equivalently \((a_\beta,b_\beta)=(1,0)\). Since the two agreeing-at-alpha strings differ at beta, these are complementary conditions. The argument reverses for row \(011\). These exhaust all six possible first-disagreement rows. \(\square\)

**Corollary.** Every vertex-simple ordered sequence whose consecutive \(h_t\)-triples are monochromatic in **either** color has at most \(M_t\) vertices.

**Proof.** The positive case is (5). For any all-zero tight path \(a_1,\dots,a_m\), reverse the entire list and complement each binary vertex, obtaining \(\widehat a_m,\dots,\widehat a_1\). The consecutive triples in this new path are reverse-complements of the original triples, hence all positive by (6); their vertices remain distinct. Apply (5). \(\square\)

This is not a boundary 3-tournament: generally \(h_t(a,b,c)\) and \(h_t(c,b,a)\) need not be opposite. **Bitwise complementing the underlying labels is essential** to the new duality.

## Physical NORI3 lift with one sentinel

Choose \(t=\lceil\log_2(n-1)\rceil\), and injectively label the \(n-1\) ordinary cube directions by distinct strings from \(B_t\). Write \(D\subseteq B_t\) for these labels. Add one sentinel cube direction \(s\) and fix any total order \(<\) on \(D\).

For a physical ordered three-face \(F\) with ordered free directions \((u,v,w)\), define
\[
c(F,(u,v,w))=
\begin{cases}
h_t(u,v,w),&u,v,w\in D,\ z_s(F)=0,\\
h_t(\widehat u,\widehat v,\widehat w),
 &u,v,w\in D,\ z_s(F)=1,\\
1,&u=s,\\
0,&w=s,\\
\mathbf1_{\{u>w\}},&v=s.
\end{cases}
\tag{7}
\]
In the first two cases, \(z_s(F)\) is the actual fixed exterior \(s\)-bit of the **physical face**. All cases depend only on the ordered free directions and a genuine fixed exterior coordinate, independently of the traversal corner.

**Legality.** When \(s\) is exterior, the antipodal face has fixed \(s\)-bit \(1-z_s(F)\), and reversing the order changes \(h_t(u,v,w)\) to \(h_t(\widehat w,\widehat v,\widehat u)\) (or conversely), which is its complement by (6). When \(s\) is free at an endpoint, reversal interchanges the constant values 1 and 0. With \(s\) in the middle, reversal interchanges its distinct ordinary neighbors and complements their strict-order indicator. Thus (1) holds for every genuine physical ordered face. \(\square\)

## Every monochromatic geodesic is short

Fix any starting vertex and any geodesic with \(m\) distinct coordinate moves \(p_1,\dots,p_m\).

If \(s\) is absent, its bit \(z\) remains fixed along the path. All physical face colors are successive \(h_t\)-triple values on the distinct label list \(p_1,\dots,p_m\) (for \(z=0\)), or on the uniformly complemented list \(\widehat p_1,\dots,\widehat p_m\) (for \(z=1\)). If the path is monochromatic, the corollary gives \(m\le M_t\).

If \(s\) occurs at position \(j\) with \(3\le j\le m-2\), the three consecutive windows in which \(s\) is respectively last, middle, and first have colors
\[
(0,\varepsilon,1),\qquad\varepsilon\in\{0,1\}.
\tag{8}
\]
Thus a monochromatic geodesic containing \(s\) must have \(j\le2\) or \(j\ge m-1\). Removing \(s\) leaves, on one side, a contiguous ordinary segment with at least \(m-2\) moves. Its actual physical windows are monochromatic and have a constant \(s\)-bit, so the corollary applies to that segment: \(m-2\le M_t\). This proves (2) for every root and every coordinate ordering.

## Full antipodal paths and the switch count

A full \(n\)-move antipodal geodesic has \(n-2\) ordered-three-face colors. If a maximal monochromatic run contains \(a\) consecutive colors, its corresponding contiguous geodesic uses exactly \(a+2\) coordinate moves. From (2), \(a+2\le M_t+2\), hence \(a\le M_t\).

If there are \(R\) runs, \(n-2\le RM_t\), so the number of switches is
\[
R-1\ge \left\lceil\frac{n-2}{M_t}\right\rceil-1
=\left\lceil\frac{n-2}{2\lceil\log_2(n-1)\rceil+4}\right\rceil-1,
\]
as claimed. The entire argument counts **actual adjacent physical face colors along one full geodesic**, and requires no blockwise concatenation or anti-cancellation hypothesis.

## Independent checks

An independent implementation exhaustively verified both the \((3,3)\)-property and duality (6) on all \(24,336,3360\) ordered triples for \(t=2,3,4\), respectively. Exact maximum-path dynamic programming found maxima \(4,7,9\) for both colors at \(t=2,3,4\), consistent with (5). An independent physical face evaluator checked 100,000 random antipodal-reversal face pairings for \(Q_{17}\), and 10,000 randomly rooted full geodesics for the claimed monochromatic-run bound. All tests passed. The stated theorem follows from the supplied publication's proved (5) and the fully written algebraic argument above.

## Interpretation of the scrapbook antisymmetry proof

The scrapbook's terminal-pair tournament argument proves \(g(n,3)\ge1+\sqrt{(n-1)/2}\) for **boundary/antisymmetric 3-tournaments**. Its crucial step compares \(uvw\) and \(wvu\) **at the same combinatorial triple**, ensuring an orientation of the auxiliary tournament on competing terminal directions.

The physical NORI3 axiom (1) compares two **antipodal physical faces**, not the two reversals on one face. The lifted coloring (7) exhibits this distinction exactly: both same-face reversals may have equal color, while antipodal reversal always complements it. The scrapbook's square-root conclusion therefore does not apply to general NORI3. It remains applicable to direction-only boundary-compatible colorings; under exterior-dependent same-face reversal oddness, any extension must also control transport between distinct physical face fibers.

This settles the proposed extension to unrestricted NORI3 in the strongest negative sense: the broader law allows monochromatic paths of logarithmic maximum length and hence near-linear compulsory switches.

## Source attribution

R. C. Devine and K. G. Milans, *Tight paths in fully directed hypergraphs*, user-supplied main-appendix manuscript, Subsection “Paths in (3,3)-tournaments,” Theorem (33)-upper, for the explicit \(h_t\) and its \(2t+4\) positive tight-path upper bound.

R. C. Devine and K. G. Milans, user-supplied scrapbook manuscript, Sections “Antisymmetric Tournaments” and “Boundary Tournaments,” for the square-root terminal-pair proof and the boundary/generalization discussion.

## Additional structural proposition: maximally non-boundary on every triple

The published \(h_t\) has a stronger local obstruction to boundary-tournament or edge-ordered realization than mere failure of reversal-oddness.

**Proposition (exact reversal-defect distance).** For **every** unordered triple \(T=\{u,v,w\}\subseteq B_t\), the three reversal pairs \((uvw,wvu)\), \((uwv,vwu)\), and \((vuw,wuv)\) include exactly **one** equal-zero pair \((0,0)\), exactly **one** equal-one pair \((1,1)\), and exactly **one** opposite-color pair. Consequently the minimum Hamming distance between the ordered-triple indicator \(h_t\) and **any** direction-only boundary 3-tournament is
\[
2\binom{2^t}{3},
\tag{12}
\]
exactly **one third of all** \(6\binom{2^t}{3}\) ordered-triple values. In particular \(h_t\) is not the comparison tournament of *any* global edge ordering on \(K_{2^t}\), and cannot even be made boundary-compatible by changing fewer than one third of its values.

**Proof.** On any unordered triple choose labels so that \(u,v\) agree in the first distinguishing coordinate \(\alpha\), their bits at the subsequent disagreement coordinate \(\beta\) are \(u_\beta=0,v_\beta=1\), and \(w_\alpha\ne u_\alpha=v_\alpha\). When \(u_\alpha=v_\alpha=0\), the four patterns (4) accept exactly \(uvw,uwv,vwu\), while rejecting \(wvu,vuw,wuv\). Thus the three reversal pairs are respectively \((1,0),(1,1),(0,0)\). When \(u_\alpha=v_\alpha=1\), the four patterns accept exactly \(uvw,vuw,wvu\), while rejecting \(uwv,wuv,vwu\). Thus the reversal pairs are \((1,1),(0,0),(1,0)\), up to which pair is listed first. These are the only two cases.

A boundary 3-tournament must make the two members of *every* reversal pair opposite. Therefore it needs at least one flip in each of the two equal pairs on every unordered triple, or two flips per triple. Conversely such two flips suffice to make each triple separately boundary-compatible; the choices are independent across unordered triples. Summation gives (12). A global edge ordering is an even smaller subclass of boundary 3-tournaments, so it is also impossible. \(\square\)

This pinpoints the **very first** failure of edge-order realizability: the logarithmic obstruction does not even define an orientation of \(L(K_n)\), so acyclicity is not yet an applicable test. For genuine boundary tournaments, the orientation exists, and *then* directed cycles are the exact obstruction to one global edge ordering.

## Why the published (3,3)-tournament lower bound does not automatically transfer

The source paper also proves \(f(n,3,3)\ge \Omega((\ln n/\ln\ln n)^{1/2})\). Its proof begins with a uniform tournament on the same \(n\) vertices, first extracts an induced subgraph with no long directed walks, and then labels pairs by longest directed-walk lengths. It uses **exactly three accepted permutations on each unordered triple** to rule out monochromatic triangles in an auxiliary edge coloring. (See the uploaded main-appendix manuscript, Theorem (33)-lower.)

None of those hypotheses is supplied by arbitrary legal physical NORI3, even after fixing a reference cube vertex. For example, for any \(n\ge4\), any free triple \(T\), and any ordered physical face \(F\) with those free directions, let \(j(T)\) be the smallest direction outside \(T\), and set
\[
 c(F,\pi):=z_{j(T)}(F),\quad \pi\text{ any ordering of }T.
 \tag{13}
\]
The antipodal face flips this exterior bit, so \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\): (13) is perfectly legal. Yet in the fiber obtained by fixing all exterior bits from the zero vertex, **all six permutations of every triple have color zero**, not three. Thus the initial \((3,3)\)-tournament premise fails completely.

Moreover even if some reference fiber happened to satisfy the three-of-six balance, its direction-only tight path would not automatically be a physical geodesic of matching colors: the \(i\)-th physical window of a geodesic starting at \(x\) sees outside bits from \(x\oplus e_{p_1}\oplus\cdots\oplus e_{p_{i-1}}\), not generally the initial fiber \(x\). This is the **root-consistency** obstruction. The source Ramsey labeling proof does not furnish a way to maintain a common exterior-bit assignment as distinct directions are traversed.

Therefore the published \(\Omega(\sqrt{\log n/\log\log n})\) lower bound is **not** an established NORI3 universal lower bound. Any transfer must supply both a balanced (3,3)-tournament reduction and a face-consistent lift of its vertex-simple tight path. Obtaining such a reduction remains a separate substantive problem.

### Logarithmic monochromatic-path obstruction and near-linear switch amplification

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

### Sharp logarithmic monochromatic paths under bounded exterior support

# Sharp logarithmic monochromatic geodesics under bounded exterior support

## Main theorem and its sharpness

Let \(V\) be the \(n\) coordinate directions of \(Q_n\), let \(S\subseteq V\) be a distinguished set of size \(t\), and put \(D=V\setminus S\), of size \(m=n-t\). Consider **any** binary coloring \(c(F,(a,b,d))\) of genuine physical ordered three-faces satisfying:

**Exterior-support hypothesis ES3(S):** If the three free directions belong to \(D\), the color of their ordered physical face depends only on their ordered directions and on the fixed exterior coordinate bits in \(S\), with no dependence on any other fixed exterior bits. Colors of ordered faces meeting \(S\) are completely unrestricted.

**Theorem 1 (uniform logarithmic lower bound).** If \(m\ge3\), some monochromatic coordinate geodesic, traversing only directions from \(D\), has at least
\[
\boxed{L\ \ge\ 1+\tfrac12\log_2 m}
\tag{1}
\]
coordinate moves. More precisely, if \(L\) denotes the longest monochromatic *increasing-direction* geodesic length after fixing any total order of \(D\), and any fixed \(S\)-bit vector, then
\[
m\ \le\ \binom{2L-2}{L-1}.
\tag{2}
\]
The proof assumes **neither** antipodal-reversal oddness nor reversal symmetry; it is a self-contained ordered-Ramsey argument for colored consecutive triples.

**Corollary 2 (sharp order for one or finitely many sentinels).** Let \(\mathcal C_t(n)\) consist of all legal antipodal-reversal-odd physical ordered-three-face colorings admitting some support \(S\) of size at most \(t\) satisfying ES3(S), and define
\[
\Lambda_t(n)=\min_{c\in\mathcal C_t(n)}
\max_{\text{monochromatic coordinate geodesics }P}|E(P)|.
\]
For every fixed \(t\ge1\),
\[
\boxed{\Lambda_t(n)=\Theta_t(\log n)}\qquad(n\to\infty).
\tag{3}
\]
The lower bound follows from Theorem 1 using \(m\ge n-t\). For the upper bound, the established self-dual Devine--Milans \((3,3)\)-tournament physical one-sentinel lift belongs to \(\mathcal C_1(n)\subseteq\mathcal C_t(n)\) and forces
\[
\max_P|E(P)|\le2\lceil\log_2(n-1)\rceil+6
\tag{4}
\]
for every monochromatic coordinate geodesic, including arbitrary roots and orders. Thus the logarithmic obstruction and lower bound **match in this substantial face-dependent subclass**. This does *not* establish a universal logarithmic lower bound for unrestricted NORI3.

## 1. Ordered-triple Ramsey lemma with explicit counting

Let \(W=\{1,\ldots,m\}\) be linearly ordered, and assign an arbitrary binary color \(h(i,j,k)\) to every increasing triple \(1\le i<j<k\le m\). An *increasing monochromatic tight path* is a sequence \(v_1<\cdots<v_\ell\) such that the consecutive triple colors \(h(v_i,v_{i+1},v_{i+2})\) are all equal. As customary, a sequence of two vertices is vacuously a monochromatic tight path.

**Lemma 3 (two-color ordered tight-path bound).** Let \(L\ge2\) be the maximum number of vertices in such a path. Then
\[
m\le\binom{2L-2}{L-1}\le4^{L-1}.
\tag{5}
\]

**Proof.** For each ordered pair \(i<j\), let \(A(i,j)\) be the maximum order of a color-0 increasing tight path ending with \(i,j\), and \(B(i,j)\) the analogous maximum for color 1. Both lie in \(\{2,\ldots,L\}\).

If \(i<j<k\) and \(h(i,j,k)=0\), appending \(k\) to any longest 0-path ending in \(i,j\) preserves strict increase and distinctness, so
\[
A(j,k)\ge A(i,j)+1.
\tag{6}
\]
For color 1, correspondingly \(B(j,k)\ge B(i,j)+1\). At least one of these two inequalities applies to **every** \(i<j<k\).

Define, for each vertex \(j\), the downset
\[
I_j=\bigcup_{i<j}
\bigl\{(a,b)\in\{2,\ldots,L\}^2:
a\le A(i,j),\ b\le B(i,j)\bigr\}.
\tag{7}
\]
This is an order ideal of the square grid poset \(\{2,\ldots,L\}^2\). We claim the \(m\) ideals \(I_j\) are **pairwise distinct**. Fix \(i<j\), and set \(q=(A(i,j),B(i,j))\). By definition \(q\in I_j\). If \(q\in I_i\), some \(h<i\) would satisfy
\[
A(h,i)\ge A(i,j),\quad B(h,i)\ge B(i,j).
\]
But the color of the increasing triple \((h,i,j)\), by (6) applied either to \(A\) or to \(B\), forces its corresponding coordinate at \((i,j)\) to be **strictly greater** than that at \((h,i)\), contradiction. Thus \(q\notin I_i\), and \(I_i\ne I_j\).

The number of order ideals in a product of two chains of length \(L-1\) is exactly \(\binom{2L-2}{L-1}\), obtained by identifying the staircase boundary of an ideal with a monotone lattice path having \(L-1\) horizontal and \(L-1\) vertical steps. We have \(m\) distinct ideals, yielding the first inequality in (5). The elementary bound \(\binom{2d}{d}\le2^{2d}=4^d\) gives the second. Taking base-two logarithms proves \(L\ge1+\tfrac12\log_2m\). \(\square\)

**Remark.** This is the exact terminal-*ordered*-pair/ideal-counting mechanism behind the classical ordered Ramsey bound for two-colored 3-uniform monotone tight paths. Unlike the scrapbook's boundary-tournament \(\sqrt n\) theorem, it assumes neither antisymmetry nor a tournament condition. Its price is the weaker logarithmic conclusion.

## 2. Transfer to physical cube geodesics

**Proof of Theorem 1.** Fix any cube vertex \(x\) and any strict total ordering of the ordinary directions \(D\). Put \(\beta=x|_S\). For every ordered triple \(a<b<d\) of *ordinary directions*, exterior support ES3(S) makes
\[
h_\beta(a,b,d)=c(F,(a,b,d))
\tag{8}
\]
well defined for **every** physical face \(F\) whose free directions are \(a,b,d\) and whose fixed \(S\)-coordinates equal \(\beta\). The bits of \(F\) outside \(S\cup\{a,b,d\}\) are immaterial, by the hypothesis.

Apply Lemma 3 to \(h_\beta\), obtaining a strictly increasing list of \(L\) distinct ordinary coordinate directions \(p_1<\cdots<p_L\) with all its consecutive \(h_\beta\)-triples colored by one bit.

Starting at the chosen cube vertex \(x\), traverse the \(L\) directions \(p_1,\ldots,p_L\) exactly once each. This is a genuine coordinate geodesic with \(L\) edges. Every ordered-three-face window along it is a genuine physical face, and since no direction in \(S\) is ever traversed, its fixed \(S\)-bit vector is still \(\beta\). By (8), the actual physical colors of the consecutive windows equal
\[
h_\beta(p_i,p_{i+1},p_{i+2})
\]
and are monochromatic. This proves both the path assertion and the explicit bound (2), with no root changes during the argument. The directions are distinct because they are strictly increasing, and physical face consistency is ensured by ES3(S). \(\square\)

## 3. Matching construction, scope, and failure of unrestricted transfer

The Devine--Milans one-sentinel lift is legal and has \(S=\{s\}\). For every face avoiding \(s\), its color depends solely on ordered free directions and the fixed exterior bit \(z_s(F)\); all other exterior bits are ignored. It therefore satisfies ES3(S) and has logarithmically bounded longest monochromatic geodesics in *both* colors, by complement-reversal self-duality. Combining with Theorem 1 proves (3) even though the lift also colors arbitrary faces meeting \(s\).

For **unrestricted** legal NORI3 colorings the reduction (8) generally fails: at different windows of the same cube geodesic, the exterior ordinary bits reflect different previously traversed directions. A single ordered triple may consequently be assigned different colors on different physical faces with the same ordered free directions and the same \(\beta\). No fixed \(h_\beta\) can represent all those windows. In particular **neither** the \((3,3)\)-tournament lower-bound mechanism nor the ordered-Ramsey proof above transfers without an additional coherence/transport hypothesis. The theorem is exactly sharp as a conclusion for fixed-size exterior support; it is deliberately not promoted to a universal bound.

**Further scope.** The same argument applies if one can find a subset \(D\) of \(m\) directions and a fixed exterior fiber for which all ordered physical three-faces on \(D\) are independent of the other \(D\)-exterior bits (regardless of how the coloring behaves elsewhere). It also applies to *nonlegal* binary ordered physical-face colorings: the lower bound is a purely combinatorial consequence of exterior-bit flatness.

## Consequential research implication

The logarithmic extremal scale is settled **within the bounded-exterior-support class**. An unrestricted counterexample to \(\Omega(\log n)\) cannot have bounded exterior-coordinate support, and any successful universal theorem must handle changes of the induced ordered-triple coloring as ordinary coordinates are traversed. Thus the remaining problem is fundamentally an *exterior-fiber coherence problem*, not merely a better path theorem for fixed \((3,3)\)-tournaments.

**Cross-reference.** The established manuscript *Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament* supplies (4). The present proof of Lemma 3 is independent of published literature and can be checked directly.
