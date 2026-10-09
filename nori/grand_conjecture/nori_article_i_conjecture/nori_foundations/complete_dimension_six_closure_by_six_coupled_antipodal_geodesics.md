# Complete dimension-six closure by six coupled antipodal geodesics

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
