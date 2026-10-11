# Seven-dimensional flipper lift and rank-five root-density extensions

- Stable ID: note_q5_seven_flipper_and_root_density_extensions
- Author: unspecified; session provenance retained
- Primary home: subsection:dimension_five_closure_and_cyclic_windows
- Labels: obstruction, partial_argument
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:dimension_five_closure_and_cyclic_windows, exact version 3

## Research note

Editorial extraction: precise original proof retained below.

---

Source: dimension_five_closure_and_cyclic_windows prior composition v3

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
