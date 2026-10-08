# One-flipper Q7 and all dimensions close when six-coordinate residual is coordinate-only

# One universal flipper with coordinate-only residual: full Q7 closure

Let \(V=B\sqcup\{g\}\), \(|B|=6\), and let \(c\) be an antipodal-reversal-odd binary coloring of ordered three-faces of \(Q_7\). Assume

1. \(g\) is a universal exterior flipper: complementing the fixed \(g\)-bit complements the color whenever the free triple avoids \(g\).
2. The induced six-coordinate residual on faces avoiding \(g\) is *position-independent*: for some ternary label \(H\),
\[
c(F,(a,b,d))=x_g(F)\oplus H(a,b,d)
\qquad(a,b,d\in B\text{ pairwise distinct}).
\]

There is **no restriction** on colors of ordered faces *containing* \(g\), beyond the global antipodal-reversal oddness condition. Those colors may be arbitrary functions of their four fixed exterior face bits.

**Theorem.** Every such \(c\) admits a full seven-coordinate antipodal geodesic with at most one color change.

**Proof.** For a free triple avoiding \(g\), antipodal complementation toggles \(x_g(F)\), and reversal of its ordered triple toggles the full \(c\)-color by oddness. Cancelling these two toggles gives
\[
H(d,b,a)=H(a,b,d),
\]
so the residual \(H\) is reversal-even.

If the six-direction residual \(H\) has a complete direction order with at most one color change, the exact universal-flipper lifting theorem applies: choose that \(B\)-order and place \(g\) first, selecting its starting bit so that the new first seam contributes zero changes. This yields a good full \(Q_7\) geodesic.

Otherwise *every* complete six-direction order of \(H\) has at least two changes. The exact finite classification in Item nori_reversal_even_coordinate_triple_q6_exact_classification_20261008 now forces
\[
H(a,b,d)=\varepsilon\oplus
\mathbf1_{\{b\notin M,\ \{a,d\}\cap M\ne\varnothing\}}
\]
for some marked two-set \(M\subset B\) and a global bit \(\varepsilon\). Complementing *all* colors of \(c\), if needed, removes \(\varepsilon\) without changing the NORI oddness axiom or the number of changes along any path.

Thus \(B\) splits into four unmarked and two marked directions, and the \(g\)-free face colors satisfy exactly the prescribed sparse two-mark template (AAA=0, AAM=MAA=1, AMM=MMA=0). The already proved *sparse-template seven-dimensional forcing theorem*, Item nori_sparse_two_mark_template_seven, applies even when all \(g\)-containing faces have arbitrary exterior dependence. It produces a good full seven-direction geodesic. Undo the global color complement if one was made. \(\square\)

**All-dimensional extension (six-coordinate residual).** Let \(c\) be an antipodal-reversal-odd coloring of \(Q_n\) with a set \(A\) of universal exterior flippers, leaving exactly six other directions \(B\). Suppose its induced ordered-three-face coloring on \(B\) is position-independent. Then \(c\) admits a one-change full antipodal geodesic in *every* dimension \(n\ge6\).

Indeed, write \(r=|A|\). If \(r\) is even, the symmetry-transfer theorem makes the six-coordinate residual antipodal-reversal odd, and the established full \(Q_6\) NORI closure lifts through the \(r\) flippers. If \(r\) is odd, choose a single flipper \(g\) and strip off the remaining \(r-1\) flippers, an even number; the seven-dimensional induced coloring is antipodal-reversal odd and has a universal \(g\)-flipper and the same position-independent six-coordinate residual. Apply the preceding \(Q_7\) theorem, then lift through the \(r-1\) stripped flippers by exact backward elimination.

**Research frontier.** The odd-flipper six-residual case has now been solved whenever the residual is position-independent. The remaining six-residual bottleneck is *genuine dependence on the fixed exterior face bits*. The finite classification explicitly isolates this distinction: reversal-even *coordinate-triple* obstructions are all two-mark, and every one of them lifts successfully. This does not prove arbitrary NORI in dimension seven or higher.
