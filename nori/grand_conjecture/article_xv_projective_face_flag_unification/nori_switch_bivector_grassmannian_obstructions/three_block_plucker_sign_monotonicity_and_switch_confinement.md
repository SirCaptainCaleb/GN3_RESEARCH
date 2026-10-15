# Three-block Plucker sign monotonicity and switch confinement

### Three-block Pluecker monotonicity and switch-confinement criterion

Let \(V=A\sqcup B\sqcup C\) be an ordered partition with positive block sizes \(a,b,c\), \(n=a+b+c\). Let \(\pi\) be any complete order refining \(A|B|C\). Put \(Z_p(\pi)=\sum_{i\le p}e_{\pi_i}-(p/n)\mathbf1\) for \(1\le p<n\), and \(\lambda_{A,C}=\mathbf1_A^*\wedge\mathbf1_C^*\) on \(W=\{\sum z_i=0\}\).

**Theorem 1 (universal Pluecker sign).** For every \(1\le p<q<n\),
\[
D_{p,q}:=\lambda_{A,C}(Z_p\wedge Z_q)\le0,
\]
independently of the internal block orders. Furthermore,
\[
\boxed{D_{p,q}=0\iff q\le a\ \text{or}\ p\ge a+b.}\tag{1}
\]

*Proof.* Let \(X_p=\mathbf1_A\cdot Z_p=\min(p,a)-ap/n\) and \(Y_p=\mathbf1_C\cdot Z_p=\max(0,p-a-b)-cp/n\). Then \(D_{p,q}=X_pY_q-X_qY_p\). The planar path \((X_p,Y_p)\) has three linear segments:
\[
p\le a:\ ((b+c)p/n,-cp/n);\quad
a\le p\le a+b:\ (a(n-p)/n,-cp/n);\quad
a+b\le p:\ (a(n-p)/n,-(a+b)(n-p)/n).
\]
The determinant for ranks in the six segment pairs \(AA,AB,AC,BB,BC,CC\) is respectively
\[
0,\quad cp(a-q)/n,\quad-bp(n-q)/n,\quad
-ac(q-p)/n,\quad a(n-q)(p-a-b)/n,\quad0.
\]
All mixed entries are negative away from the stated degenerate rank regions. This proves (1). QED.

**Theorem 2 (complete switch-bivector characterization).** Let \(S(\pi)\subseteq\{1,\ldots,n-1\}\) contain at least two switch-prefix ranks, and put
\[
\mathcal B(\pi)=\sum_{p<q,\ p,q\in S(\pi)}Z_p\wedge Z_q,\qquad
E(\pi)=Z_{\min S(\pi)}\wedge Z_{\max S(\pi)}.
\]
Then \(\lambda_{A,C}(\mathcal B)\le0\), and
\[
\boxed{\lambda_{A,C}(\mathcal B)<0
\iff S(\pi)\not\subseteq[1,a]\ \text{and}\
S(\pi)\not\subseteq[a+b,n-1].}\tag{2}
\]
The same condition characterizes strict negativity of \(\lambda_{A,C}(E)\).

*Proof.* Every switch-pair summand is nonpositive by Theorem 1. If all selected ranks lie in either extremal interval, each pair vanishes. Otherwise the smallest and largest ranks form a pair outside both intervals, so its determinant is strictly negative. No other term can cancel it. QED.

**Corollary 3 (coherent parabolic carriers).** Suppose every Hamilton flag in the three-block Coxeter residue \(A|B|C\) has at least two switches, with no flag having all switch ranks contained in either extremal interval of (2). Then all full quadratic bivectors belong to the common strict convex halfspace \(\lambda_{A,C}<0\), so their piecewise-affine interpolation is zero-free on the cell. All extreme-switch oriented planes belong to one contractible Pluecker chart. When a coherent triangulation of the whole Coxeter complex is used, the affine fillings agree on shared faces.

**Corollary 4 (monochromatic-tail localization).** For boundary 3-tournaments the legal switch ranks are \(2,\ldots,n-2\). A flag can prevent this strict three-block chart only if \(a\ge3\) and all its switches are in \(\{2,\ldots,a\}\), or if \(c\ge3\) and all its switches are in \(\{a+b,\ldots,n-2\}\). The former gives a long monochromatic suffix of the triple-color word, and the latter a long monochromatic prefix. The same theorem applies to cube-edge words with their full switch-rank range.

This strengthens the prior universal endpoint-block convex-carrier criterion by allowing arbitrarily large endpoint blocks whenever coloring constraints exclude the two explicitly characterized kinds of switch confinement. It does not show that such exceptional flags are impossible for unrestricted colorings.
