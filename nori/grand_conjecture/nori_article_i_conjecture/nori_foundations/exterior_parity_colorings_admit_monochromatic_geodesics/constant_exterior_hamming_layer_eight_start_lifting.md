# Eight constant exterior-Hamming-layer starts and nonlinear weight lifting

## Development

Fix any dimension \(n\ge3\) and any order \(p=(p_1,\ldots,p_n)\) of the coordinates. If the starting bits in this order are \(x_1,\ldots,x_n\), let \(K_i\) be the number of 1-bits fixed outside the consecutive three-face with free directions \(p_i,p_{i+1},p_{i+2}\), after the first \(i-1\) directions have been traversed. Then
\[
K_i=\sum_{j<i}(1-x_j)+\sum_{j>i+2}x_j,\qquad
K_{i+1}-K_i=1-x_i-x_{i+3}.
\]

**Theorem (eight constant-layer starts).** For every fixed direction order \(p\), precisely eight starting vertices make the entire sequence \(K_1,\ldots,K_{n-2}\) constant: freely choose \(x_1,x_2,x_3\), and recursively set
\[
x_{i+3}=1-x_i \quad(1\le i\le n-3).
\]
The successive exterior fixed-bit configurations may differ, but their Hamming weights are identical. This holds independently of any coloring.

**Corollary (arbitrary nonlinear exterior-weight colorings).** Let \(f:\{0,1,\ldots,n-3\}\to\{0,1\}\) be arbitrary, and color every ordered three-face by \(c(F,\pi)=f(K(F))\), where \(K(F)\) is the number of exterior coordinates fixed at 1. Every direction order has at least eight monochromatic antipodal geodesics, namely the starting vertices from the theorem. No antipodal-oddness or linearity of \(f\) is needed.

**Transference corollary.** More generally, let \(h\) be any binary function of ordered triples of distinct coordinates and define
\[
c(F,\pi)=h(\pi)\oplus f(K(F)).
\]
For the eight starts above, the entire sequence of window-color differences is **exactly** the change sequence of \(h(p_i,p_{i+1},p_{i+2})\): the \(f(K_i)\)-term is constant. Thus every one-change direction order for the coordinate-only coloring \(h\) yields at least eight one-change based antipodal geodesics for \(c\). This transfer holds for any \(f\), even when \(c\) does not satisfy antipodal oddness.

**Antipodal compatibility.** Setting \(m=n-3\), this class satisfies \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\) precisely when
\[
h(\operatorname{rev}\pi)\oplus h(\pi)
 \oplus f(m-k)\oplus f(k)=1
\]
for every ordered triple \(\pi\) and all \(0\le k\le m\). For example, reversal-odd \(h\) with any complement-symmetric weight function \(f(m-k)=f(k)\) is a valid NORI coloring, and the transference result applies. Exterior-weight-only colorings with reversal-even \(h\) are antipodally odd exactly when \(f(m-k)=1\oplus f(k)\), possible for odd \(m\).

*Proof.* When the window shifts right by one direction, the departing coordinate \(p_i\) enters the fixed exterior at its toggled bit \(1-x_i\), and the arriving direction \(p_{i+3}\) leaves the fixed exterior, removing \(x_{i+3}\). This proves the difference formula. Its vanishing for every \(i\) is equivalent to the displayed recurrence. Three freely chosen initial bits determine all later bits uniquely, giving exactly eight starts. Under these starts \(f(K_i)\) is constant, so it changes no adjacent color differences. The antipodal condition follows because complementation sends \(K\) to \(m-K\) and reverses the ordered free directions. \(\square\)

**Scope.** This proves a genuinely nonlinear face-dependent subclass of NORI but does not resolve arbitrary face-position dependence or arbitrary reversal-odd coordinate-only \(h\).
