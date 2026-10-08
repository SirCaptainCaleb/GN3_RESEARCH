# Exact flipper lifting and six-residual parity closure

# Exact universal-flipper lifting and parity-six closure

Let \(c\) be a binary coloring of ordered three-faces of \(Q_n\). A coordinate \(a\) is a universal exterior flipper if complementing its fixed exterior face bit complements every ordered face color not freeing \(a\). Let \(A\) be a set of such coordinates, \(B=V\setminus A\), \(r=|A|\), and \(m=|B|\ge3\).

**Exact lifting lemma.** There is an induced ordered-face coloring \(h\) of \(Q_m\) such that for every order \(\tau\) of \(B\), every starting vertex \(y\in Q_m\), and every order \(\sigma\) of \(A\), one may select the \(A\) starting bits \(z\) so that the full direction order \(\sigma\tau\) has change vector
\[
(\underbrace{0,\ldots,0}_{r},\ d_1^h(y,\tau),\ldots,d_{m-3}^h(y,\tau)).
\]
Consequently, if \(h\) has a full geodesic with at most \(k\) changes, so does \(c\).

**Proof.** Restrict to ordered faces whose free triple lies in \(B\). Define \(h\) by taking their \(A\)-exterior coordinates all zero. Independence of toggles of distinct \(A\)-bits gives
\[
c(F,\pi)=\bigoplus_{a\in A}x_a(F)\ \oplus h(F_B,\pi)
\quad(\pi\subseteq B).
\]
Consider the complete coordinate order \(\sigma=(a_1,\ldots,a_r)\), then \(\tau=(b_1,\ldots,b_m)\). For each \(1\le i\le r\), compare window \(i\) and window \(i+1\). Direction \(a_i\) exits the free triple and becomes a fixed exterior bit, flipped along the path, whereas directions \(a_j\) with \(j>i\) that remain outside the two windows have the same initial bit in each. Accordingly the change \(d_i\) has Boolean derivative exactly one in the initial bit \(z_i\), and is independent of \(z_1,\ldots,z_{i-1}\); this follows because these already traversed coordinates are exterior to both windows, so their equal contributions cancel when forming the XOR, and because every window containing \(a_j\) is independent of \(z_j\) when \(a_j\) is free. The dependence on later \(z_j\) may be arbitrary if \(a_j\) is free in one window, but \(d_i=z_i\oplus f_i(z_{i+1},\ldots,z_r,y)\). Choose \(z_r,z_{r-1},\ldots,z_1\) successively to make all \(d_i=0\). All subsequent windows have their three free directions inside \(B\), and each has the same exterior \(A\)-bits \(1\oplus z_a\), so their differences are exactly the differences from \(h\). This proves the claimed change vector. \(\square\)

**Symmetry transfer.** If \(c\) satisfies the NORI condition \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\), then for ordered faces within \(B\),
\[
h(\bar F_B,\operatorname{rev}\pi)
   =\bigl(1\oplus(r\bmod2)\bigr)\oplus h(F_B,\pi).
\]
Indeed, antipodality changes all \(r\) exterior \(A\)-bits, complementing the parity term exactly \(r\) times.

**Even-flipper, six-residual theorem.** If \(c\) is NORI, \(r\) is even, and \(3\le m\le6\), then \(c\) has a full geodesic with at most one color change. For \(m=6\), the induced \(h\) is itself NORI and the established \(Q_6\) closure theorem applies; for \(m\le5\), unrestricted \(Q_m\) closure applies. Then lift by the exact lemma. Cases \(n\le5\) are already covered directly.

**Implication.** A NORI counterexample with at most six nonflippers must have *exactly six* nonflippers and an *odd* number of universal exterior flippers. Hence such a counterexample, if any, has odd total dimension. This is a parity-sensitive strengthening of the existing five-nonflipper theorem. The remaining \(m=6,r\) odd residual is reversal-even and cannot be resolved merely by applying the known odd \(Q_6\) theorem.
