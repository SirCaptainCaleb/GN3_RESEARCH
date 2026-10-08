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
