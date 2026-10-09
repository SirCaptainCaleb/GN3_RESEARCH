# Uniform five-coordinate good tails force one-flipper Q7 closure

# Uniform good-tail completions force one-flipper Q7 closure

Let \(V=B\sqcup\{g\}\), \(|B|=6\). Let \(c\) color ordered three-faces of \(Q_7\) with antipodal-reversal oddness. Suppose \(g\) is a *universal exterior flipper*: complementing its fixed face bit complements the color of every ordered face whose free triple avoids \(g\).

Let \(h\) be the induced coloring on ordered three-faces of the \(B\)-cube with \(x_g=0\), so \(c(F,\pi)=x_g(F)\oplus h(F_B,\pi)\) for every ordered face avoiding \(g\). An assignment of the six starting bits on \(B\) is denoted \(x\).

**Theorem (uniform good-tail completion).** Assume the following property of \(h\):

For every ordered triple \((a,b,c)\) of distinct coordinates of \(B\), and every \(x\in Q_B\), there is a permutation \((d,e,f)\) of the remaining three coordinates such that the last three ordered-three-face windows of the complete \(B\)-direction order
\[
(a,b,c,d,e,f),
\]
starting from \(x\), have *at most one color change* in the induced coloring \(h\). Equivalently, the five-coordinate tail \((b,c,d,e,f)\), entered after the move \(a\), has at most one change.

Then **the full coloring \(c\) admits an antipodal seven-geodesic with at most one color change**. The colors of all faces *containing* \(g\) are unrestricted except for antipodal-reversal oddness.

**Proof.** Suppose every full geodesic in \(Q_7\) is bad. Fix any distinct \(a,b,c\in B\), any six starting bits \(x\) on \(B\), and choose a completion \(d,e,f\) from the hypothesis. Use the seven-direction order
\[
(a,g,b,c,d,e,f).
\]
Its first two window colors are \(U=c(a,g,b)\) and \(W=c(g,b,c)\), in the face positions reached along this order. Both are independent of the initial \(g\)-bit. The last three window colors are on \(g\)-free faces, so are either the three \(h\)-tail colors or their bitwise complement, according to the initial \(g\)-bit. They have at most one internal change. By selecting the initial \(g\)-bit, we can make the first of these last three colors equal to \(W\). If \(U=W\), this produces a full seven-geodesic with at most one change. Our assumption of global failure consequently forces
\[
c(a,g,b)\ne c(g,b,c)
\tag{1}
\]
for every \(x\in Q_B\) and every pairwise distinct \(a,b,c\in B\), using the corresponding early-window face positions. The values in (1) are independent of the chosen completion \(d,e,f\).

Fix \(a,b\). In the face \((a,g,b)\), the starting bit \(x_c\) is exterior; in \((g,b,c)\) it is free. Since (1) holds for both values of \(x_c\), the first color is independent of \(x_c\). Vary \(c\) through the four elements of \(B\setminus\{a,b\}\). Thus every exterior bit is irrelevant to \(c(a,g,b)\); it has a constant value \(F_{ab}\), depending only on the *ordered* pair \((a,b)\).

Similarly, for fixed \(b,c\), the starting bit \(x_a\) is free in \((a,g,b)\) but exterior (already traversed) in \((g,b,c)\). Varying \(x_a\) in (1) proves independence of the second color from \(x_a\). As \(a\) ranges through the four elements of \(B\setminus\{b,c\}\), this shows that \(c(g,b,c)\) has a constant value \(G_{bc}\), depending only on \((b,c)\).

Equation (1) becomes
\[
F_{ab}=1\oplus G_{bc}\qquad(a,b,c\ \text{pairwise distinct}).
\tag{2}
\]
For a fixed \(b\) and any distinct \(a,a'\ne b\), choose \(c\) different from \(a,a',b\). Then (2) gives \(F_{ab}=F_{a'b}\). Hence \(F_{ab}=K_b\), independent of \(a\), for some bits \(K_b\).

Finally antipodal-reversal oddness applied to the \(g\)-containing ordered face \((a,g,b)\) gives \(F_{ba}=1\oplus F_{ab}\), because both values have already been shown independent of exterior face bits. Thus
\[
K_a=1\oplus K_b\qquad\text{for every }a\ne b\text{ in }B.
\]
Taking three distinct coordinates \(a,b,c\) yields \(K_a=K_c\) from the first two equalities and \(K_a\ne K_c\) from the third, contradiction. Therefore a good seven-geodesic exists. \(\square\)

**Corollary (coordinate-only residual).** Suppose the residual \(h\) depends only on the ordered free triple: \(h(F_B,(a,b,c))=H(a,b,c)\). If, for every ordered distinct \(a,b,c\in B\), at least one permutation \(d,e,f\) of the other three directions makes
\[
\big(H(b,c,d),H(c,d,e),H(d,e,f)\big)
\]
have at most one change, then the full \(Q_7\) coloring has a one-change antipodal geodesic, irrespective of all \(g\)-containing face colors.

**Necessary frontier condition.** A seven-dimensional NORI counterexample with one universal exterior flipper must have at least one ordered triple \((a,b,c)\) and one residual starting vertex \(x\) for which *every* completion \(d,e,f\) of the remaining three directions produces a last-three-window word with exactly two changes, namely \(010\) or \(101\). In the coordinate-only subclass this bad-tail triple must occur for the label function \(H\) independently of \(x\). This sharply localizes a necessary obstruction in the six-coordinate residual.
