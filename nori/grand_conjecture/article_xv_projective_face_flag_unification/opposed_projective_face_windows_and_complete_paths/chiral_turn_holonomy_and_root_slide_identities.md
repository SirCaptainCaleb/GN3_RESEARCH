# Chiral turn holonomy and root slide identities

# Root-slide holonomy for reversal-odd cube turns

Fix \(n\ge3\), an antipodally odd undirected cube-edge coloring \(c(\bar e)=1-c(e)\), and a chirality \(\chi(i,j)\in\mathbb F_2\) on pairs of distinct dimensions with \(\chi(j,i)=1+\chi(i,j)\). For a full cube geodesic from \(x\) with dimension order \(\pi=(\pi_1,\ldots,\pi_n)\), write its edge colors \(w_1,\ldots,w_n\) and define
\[
b_j=w_j+w_{j+1}+\chi(\pi_j,\pi_{j+1})\quad(1\le j<n).
\]
The \(b_j\) are locally reversal-odd turn labels: reversing an ordered turn exchanges its two dimensions and complements \(\chi\), while its edge-color XOR is unchanged. Antipodal translation complements both edge colors and hence preserves \(b_j\).

Let \(\pi_{n+1}=\pi_1\). Define the cyclic chirality
\[
K(\pi)=\sum_{j=1}^n\chi(\pi_j,\pi_{j+1})
\]
and append the closing bit
\[
\boxed{b_n=1+K(\pi)+\sum_{j=1}^{n-1}b_j.}
\]

**Theorem 1 (cyclic chiral root-slide theorem).** The canonical flag shift
\[
T(x;\pi_1,\ldots,\pi_n)=(x+e_{\pi_1};\pi_2,\ldots,\pi_n,\pi_1)
\]
rotates the augmented turn word \((b_1,\ldots,b_n)\) cyclically. Every such augmented turn word obeys
\[
\boxed{\sum_{j=1}^n b_j=1+K(\pi).}
\]
After \(n\) slides the root is antipodal, and the entire turn word returns.

*Proof.* Under \(T\) the undirected edge-color word changes from \((w_1,\ldots,w_n)\) to \((w_2,\ldots,w_n,1+w_1)\). The first \(n-2\) new turns are \(b_2,\ldots,b_{n-1}\), while the last is
\[
w_n+(1+w_1)+\chi(\pi_n,\pi_1)
=1+\sum_{j=1}^{n-1}b_j+K(\pi)=b_n.
\]
Since \(K\) is invariant under cyclic permutation of \(\pi\), the closing-bit rule gives the next rotation too. After \(n\) slides, each dimension has been toggled once; the antipodal edge-color complementation cancels in every turn XOR. \(\square\)

**Corollary 2 (quantitative switch-defect criterion).** Put
\[
\delta_j=b_j+\chi(\pi_j,\pi_{j+1}) \quad(1\le j\le n),
\]
interpreting the last pair cyclically, and let \(D\) be the integer number of ones in this cyclic defect vector. Then
\[
\boxed{\sum_j\delta_j=1,\qquad
\min_{0\le k<n}\operatorname{sw}(P(T^k(x;\pi)))=D-1.}
\]
In particular \(D\) is odd, and the orbit contains a monochromatic full geodesic if and only if \(D=1\). One-switch and zero-switch existence are equivalent on each root-slide orbit.

*Proof.* For \(j<n\), \(\delta_j=w_j+w_{j+1}\); the closing defect is \(\delta_n=1+w_n+w_1\). Their binary sum is one. Sliding rotates these defects and places any selected defect at the omitted seam. Thus the least internal switch count is \(D-\max_j\delta_j=D-1\). \(\square\)

**Theorem 3 (fixed-root type-A opposition).** For each fixed cube root \(x\), all dimension orders form the chambers of a type-\(A_{n-1}\) Coxeter sphere. The order-reversal involution \(\pi\mapsto\pi^{\mathrm{rev}}\) is its antipode, and
\[
\boxed{b(x;\pi^{\mathrm{rev}})=\mathbf1-\operatorname{rev} b(x;\pi).}
\]
This is the same complemented-reversal law obeyed by the triple-color words of ordinary reversal-odd boundary tournaments on Hamilton paths.

*Proof.* Reversing a complete geodesic and applying cube antipodality gives the same root and reversed dimension order; its edge-color word is complemented reversal of the original. Adjacent edge-color changes are therefore reversed without complementation. The antisymmetry of \(\chi\) adds the one-bit complement at each reversed turn, yielding the displayed identity. Order reversal is the longest-element opposition of the type-A Coxeter complex. \(\square\)

**Scope.** This is a faithful local-reversal-odd encoding of unrestricted NORI1, not a proof that an orbit with \(D=1\) exists. The cube also has gluing edges between these fixed-root type-A spheres, and the reversal involution does not preserve that gluing in the standard type-B complex. Root selection remains the outstanding compatibility problem.
