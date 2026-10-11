# Rooted one-switch failures and exact good-root localization obstructions

- Stable ID: note_rooted_restriction_and_good_root_density_limitations
- Author: NORI manuscript editorial migration; mathematical origins recorded in original compositions
- Primary home: section:nori_foundations
- Labels: obstruction, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:sharp_rooted_obstructions_to_one_change_antipodal_geodesics, exact version 3
- subsection:exact_change_vector_fibers_and_affine_obstruction_certificates, exact version 2

## Research note

# Editorial scope and mathematical status

Exact results for prescribed-root strengthenings and thin good-root regions; these constrain rooted proof strategies, not the already-refuted unrestricted three-face conjecture.

The exact compositions below are copied verbatim from the previous manuscript hierarchy for reproducibility. Editorial transfer is not a refutation or a new mathematical proof. Manuscript historical versions and provenance remain accessible through nori.read_manuscript.


---

## Retired Subsection: Sharp rooted obstructions to one-change antipodal geodesics

Source ID: `sharp_rooted_obstructions_to_one_change_antipodal_geodesics`
Source Section: `nori_foundations`
Exact original Subsection composition: v3.

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


Source: exact_change_vector_fibers_and_affine_obstruction_certificates composition v2

For every n>=7 there is a NORI antipodal-reversal-odd ordered-three-face coloring with pointwise reversal-evenness, affine single-exterior-bit color on each face, and a coordinate order for which EVERY starting vertex produces at least two color changes.

Construction: On ordered free triples (1,2,3), (2,3,4), (3,4,5), (4,5,6), and (i,i+1,i+2) for i>=5, assign face colors respectively y_n, 1+y_1, y_1, y_n, y_1 (sum mod 2; y is the physical exterior-bit assignment). Along order (1,...,n) from x, the color word is (x_n,x_1,1+x_1,x_n,1+x_1,...,1+x_1). Its first five bits are 00101, 01000, 10111, or 11010 according to (x_1,x_n)=(0,0),(1,0),(0,1),(1,1); each has at least two switches, and the remaining bits repeat its fifth bit. Give reversed ordered triples the same function on their common face. Fill all other reversal-pairs using an arbitrary single exterior bit y_r (possible since n>=7). Each function changes under exterior-bit complement, so c(bar F,rev pi)=1+c(F,pi) globally. This proves the claim.

Research consequence: oddness plus exact face-locality does not force a good root for any fixed coordinate order. A grand-closure argument must exchange direction orders as well as roots. This is a proof obstruction to root-only Hamming-layer or fixed-permutation surjectivity arguments, not a counterexample to the grand conjecture.
