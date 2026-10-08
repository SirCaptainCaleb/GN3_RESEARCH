# Uniform exterior sensitivity forces complementary face constants in reversal-even Q6

# Uniform exterior sensitivity collapses complementary faces in reversal-even Q6

Let \(B=\{a,b,c,d,e,f\}\), and let \(h\) be a binary coloring of ordered three-faces of \(Q_B\) satisfying reversal-even antipodality
\[
h(\bar F,\operatorname{rev}\pi)=h(F,\pi).
\]
Assume no full six-direction geodesic has fewer than two color changes. Say that the ordered triple \((a,b,c)\) is **uniformly sensitive** to its exterior coordinate \(d\) if toggling the fixed \(d\)-bit always complements its color, for every assignment of the other two exterior bits \(e,f\).

**Theorem (uniform complementary-face collapse).** Under these hypotheses, there exists \(K\in\mathbb F_2\) such that for *every* assignment of exterior face bits,
\[
\begin{array}{ll}
h(b,c,d)=h(b,a,d)=K,\\
h(c,d,e)=h(c,d,f)=h(a,d,e)=h(a,d,f)=1\oplus K,\\
h(d,e,f)=h(d,f,e)=h(f,e,d)=h(e,f,d)=K .
\end{array}\tag{1}
\]
In each formula \(h(r,s,t)\) denotes the color of the ordered face with those free directions; the equality holds identically over all its fixed exterior-bit assignments. Reversal-even antipodality supplies the corresponding reversed-order identities as well.

**Proof.** Fix any start \(x\in Q_B\). For the complete order \((a,b,c,d,e,f)\), denote the four window colors by \((w_1,w_2,w_3,w_4)\). Since \(d\) is exterior to the first face and free in the other three, toggling its starting bit complements \(w_1\) and leaves \(w_2,w_3,w_4\) unchanged. Uniform sensitivity implies that one of the two choices makes \(w_1=w_2\). If \((w_2,w_3,w_4)\) had at most one change, this choice would give a good complete geodesic. Hence global failure forces
\[
(w_2,w_3,w_4)=(K_x,1\oplus K_x,K_x)
\tag{2}
\]
for every starting vertex. The same holds for order \((a,b,c,d,f,e)\).

The face \((b,c,d)\) has exterior coordinates \(a,e,f\), while \((d,e,f)\) and \((d,f,e)\) have exterior coordinates \(a,b,c\). Equality of the first and third tail colors in (2) for **all** initial bits forces their common value to depend only on the shared exterior coordinate \(a\), evaluated after the \(a\)-move. Thus there is a function \(K(t)\), \(t=1\oplus x_a\), such that
\[
h(b,c,d)=h(d,e,f)=h(d,f,e)=K(t),\qquad
h(c,d,e)=h(c,d,f)=1\oplus K(t)
\tag{3}
\]
for all exterior assignments. This uses only the disjointness of the other exterior bit sets and the full quantifier over \(x\).

If \(K\) were nonconstant, the face \((d,e,f)\) would be uniformly sensitive to exterior coordinate \(a\). Reversal-even antipodality would make the reversed face \((f,e,d)\) uniformly sensitive to \(a\) as well. Consider the complete order
\[
(f,e,d,a,b,c).
\]
Its first-window face \((f,e,d)\) is uniformly sensitive to the initial \(a\)-bit; its last-window face \((a,b,c)\) is uniformly sensitive to the initial \(d\)-bit. Both middle windows \((e,d,a)\) and \((d,a,b)\) have \(a,d\) as free coordinates, so they are independent of both initial bits. Choose the initial \(a\)-bit to make the first color agree with the second and independently choose the initial \(d\)-bit to make the fourth color agree with the third. The resulting word has at most one change, contradiction. Thus \(K(t)\) is constant, proving the identities in (3) with a fixed bit \(K\); reversal-evenness gives the listed \((f,e,d)\) and \((e,f,d)\) constants.

Finally reversal-evenness also preserves uniform sensitivity under reversal of the *initial* free triple: \((c,b,a)\) is uniformly sensitive to \(d\). Repeat the preceding argument with complete orders \((c,b,a,d,e,f)\) and \((c,b,a,d,f,e)\). Their terminal \((d,e,f)\)-colors are already the constant \(K\), so the same alternating-tail reasoning forces \(h(b,a,d)=K\) and \(h(a,d,e)=h(a,d,f)=1\oplus K\), again at every exterior assignment. This establishes (1). \(\square\)

**Corollary (affine residual necessary condition).** If a globally bad reversal-even ordered-face coloring of \(Q_6\) is Boolean affine in the exterior bits on every ordered triple, then *every nonzero exterior derivative* triggers the entire constant block (1) after relabeling. Thus any counterexample of this affine type with genuine exterior dependence must contain uniform alternating blocks on many complementary triples. This is a stronger structural consequence than the bare rank-at-most-one criterion, but it does not establish that all exterior derivatives vanish.

**Scope.** Uniform sensitivity means Boolean derivative 1 for every outside-bit assignment. Mere sensitivity at one chosen face assignment does not imply the displayed universal constancies. The all-dimensional NORI conjecture and the arbitrary one-flipper seven-dimensional case remain open.
