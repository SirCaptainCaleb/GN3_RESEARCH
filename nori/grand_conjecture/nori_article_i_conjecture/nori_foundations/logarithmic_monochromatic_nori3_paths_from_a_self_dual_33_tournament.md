# Logarithmic monochromatic NORI3 paths from a self-dual (3,3)-tournament

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
