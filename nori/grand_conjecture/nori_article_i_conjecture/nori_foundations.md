# Foundational closure theorems and rooted obstructions

# Foundational closure and rooted obstructions

Let \(Q_n=\mathbb F_2^n\). An ordered three-face is a physical coordinate face \(F\) together with an ordering \(\pi=(a,b,c)\) of its three free directions. Its color is independent of the traversing corner within \(F\). The active NORI law is \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). A full antipodal geodesic crosses all \(n\) coordinates once and carries the \(n-2\) ordered-face colors of its consecutive three-move windows. It is *good* if this word has at most one change.

**Theorem 1 (unconditional \(Q_5\) closure).** Every binary coloring of physical ordered three-faces of \(Q_5\), without any antipodal hypothesis, admits a good full geodesic.

**Proof.** Suppose every five-move geodesic is bad. Its three-window word must alternate, hence its first and last colors agree. For an arbitrary direction order \((a,b,c,d,e)\), the first color depends only on the fixed exterior bits in directions \(d,e\), whereas the last depends only on the bits in \(a,b\). These four bits can be independently chosen at the starting root; equality for all starts forces both colors to be constant over all exterior positions. Varying the order shows the coloring depends only on an ordered direction triple, say \(h(a,b,c)\). Every four consecutive distinct directions then satisfy \(h(a,b,c)\ne h(b,c,d)\), or else an order beginning with those directions gives a good path. Fix five distinct directions in a cycle; the five consecutive triple labels would alternate around an odd five-cycle, impossible. \(\square\)

The dimension-six closure also holds for *every* antipodal-reversal-odd coloring, including nonlinear dependence on exterior bits. The following six-path forcing certificate is the essential reason; it records literal physical-face identifications rather than assuming that a good geodesic in a facet can be lifted independently of the outside bits.

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

## Root mobility is essential

A prescribed-root version of the conjecture is false in every \(n\ge5\). For even \(n\ge6\), color a physical ordered three-face by the parity of its exterior-one bits. Because \(n-3\) is odd, antipodality complements the color; every full path from the all-zero root has successive exterior weights \(0,\ldots,n-3\) and therefore \(n-3\) switches. When \(n\ge7\) is odd, put \(n-3=2s\), use parity for exterior weights below \(s\), complemented parity above \(s\), and a reversal-odd ordered-triple bit at weight \(s\). The two wings alternate, and exactly one of the two central comparisons changes, forcing \(n-4\) switches. Translation moves the bad root to any prescribed vertex.

In \(Q_5\), the obstruction at one fixed root is completely classified. Let \(V\) be the five directions. Choose \(H(P,t)\in\mathbb F_2\) for each direction \(t\) and each two-set \(P\subset V\setminus\{t\}\), with
\[
H((V\setminus\{t\})\setminus P,t)=1+H(P,t).
\]
For a face with ordered free triple \((a,b,c)\) and exterior-one set \(S\), define its color as \(H(\{a,b\},c)\) when \(|S|=0\), as \(1+H(S\cup\{a\},b)\) when \(|S|=1\), and as \(H(S,a)\) when \(|S|=2\). Along any five-order \((a,b,c,d,e)\) from the all-zero root this gives \((h,1+h,h)\), \(h=H(\{a,b\},c)\), hence exactly two changes. Conversely alternating words force symmetry of the first-window color under exchanging \(a,b\), the middle and last layer formulas, and the complementary-pair relation from antipodal reversal. Each \(t\) has three free complementary-pair bits, giving exactly \(2^{15}\) such colorings.

**Theorem 3 (sharp \(Q_5\) good-root density).** At most two starting vertices of a legal \(Q_5\) coloring are bad, and if two are bad they are adjacent. Thus at least \(30\) of the \(32\) starting vertices admit a good full order; equality is attainable.

**Proof.** Translate a bad root to zero and write the coloring in the above \(H\)-form. If a second bad root has ones in \(k\ge2\) coordinates among \(a,b,c,d,e\), the required alternating words give contradictions. For \(k=2\), the full orders \(bdeac\), \(abdce\), and \(bedac\) imply, respectively, three equations \(A+B=B+C=C+A=1\) over \(\mathbb F_2\), whose sum is \(0=1\). For \(k=3,4\), the orders \(adebc,badce\) force the same \(H\)-difference to equal both \(0\) and \(1\); the orders \(abcde,adebc\) do likewise for \(k=5\). Hence bad roots are pairwise adjacent, and the triangle-free cube has at most two. For sharpness fix direction \(a\), set \(H(P,t)=1\) precisely when \(a\notin P\) for \(t\ne a\), and choose any complementary assignment when \(t=a\). Both \(0\) and \(e_a\) then have alternating rooted words for all orders, as is checked by placing \(a\) successively in positions \(1,\ldots,5\). \(\square\)

The two low-dimensional closure theorems establish the base cases of the active conjecture. The rooted theorem explains why subsequent proofs must allow physical root transport: an argument demanding a good order at a predetermined vertex cannot yield the unrestricted result.

## Complete finite-dimensional base and root mobility

The six-dimensional proof above is independent of any hypothetical induction. Its pointwise-exterior-sensitivity and fixed-order obstruction analyses are now grouped with that base theorem rather than with seven-dimensional wings. In dimension five, the unconditional odd five-cycle proof applies to *every* physical ordered-face coloring. Two separate root-density estimates must be distinguished: under arbitrary coloring a quantitative lower bound on good roots survives without any antipodal hypothesis, while antipodal-reversal oddness yields the sharp minimum of thirty good roots. Thus low-dimensional closure and the impossibility of prescribing a successful root are both structural inputs to any higher-dimensional argument.
