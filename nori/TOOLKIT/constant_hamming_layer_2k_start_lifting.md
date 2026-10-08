# Constant exterior Hamming layers for ordered k-face windows

**Summary:** A k-step antiperiodic starting bit pattern keeps the number of exterior ones constant, so nonlinear Hamming-weight twists cannot create additional color changes.

## Statement

For every k-window direction order exactly 2^k starting vertices maintain constant exterior Hamming weight, via x_{i+k}=1-x_i. Consequently arbitrary nonlinear exterior-weight perturbations preserve the complete coordinate-only color-change vector on these starts.

## Body

Let \(1\le k\le n\) and fix a direction order \(p=(p_1,\ldots,p_n)\) in the Boolean cube. A starting vertex has bits \(x_1,\ldots,x_n\) in that order. Let \(K_i\) be the number of fixed exterior 1-bits of the consecutive ordered \(k\)-face on directions \(p_i,\ldots,p_{i+k-1}\), after the first \(i-1\) moves.

**Constant exterior Hamming-layer theorem.** Precisely \(2^k\) starting vertices make all \(K_i\), \(1\le i\le n-k+1\), equal. They are the solutions of
\[
x_{i+k}=1-x_i\qquad(1\le i\le n-k),
\]
with \(x_1,\ldots,x_k\) arbitrary.

**Proof.** The exterior 1-count is
\[
K_i=\sum_{j<i}(1-x_j)+\sum_{j>i+k-1}x_j.
\]
On moving the window from \(i\) to \(i+1\), the departing direction joins the fixed exterior at bit \(1-x_i\) and the arriving direction leaves the exterior, removing bit \(x_{i+k}\). Hence
\[
K_{i+1}-K_i=1-x_i-x_{i+k}.
\]
All counts are constant exactly when the displayed recurrence holds. Every choice of its first \(k\) bits determines a unique solution, giving \(2^k\) solutions. \(\square\)

**Nonlinear weight-lifting corollary.** Let \(h\) be any binary label on ordered \(k\)-tuples, and \(f:\{0,\ldots,n-k\}\to\{0,1\}\) any function. Color ordered \(k\)-faces by
\[
c(F,\pi)=h(\pi)\oplus f(K(F)),
\]
where \(K(F)\) is the number of fixed exterior 1-bits. On each of the \(2^k\) constant-layer starting vertices, the entire adjacent change vector of the based geodesic equals the change vector of the coordinate-only word
\[
h(p_1,\ldots,p_k),h(p_2,\ldots,p_{k+1}),\ldots,h(p_{n-k+1},\ldots,p_n).
\]
Thus a coordinate-only order with at most \(q\) changes always lifts to at least \(2^k\) full-cube geodesics with at most \(q\) changes, for arbitrary nonlinear \(f\). When \(h\) is constant, every direction order has at least \(2^k\) monochromatic geodesics, independent of \(f\). The statement requires no antipodal symmetry.

The assertion counts starts making the *exterior Hamming weight* constant. Other starts may also yield monochromatic color sequences when \(f\) has coincidences.

## Metadata

- ID: constant_hamming_layer_2k_start_lifting
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
