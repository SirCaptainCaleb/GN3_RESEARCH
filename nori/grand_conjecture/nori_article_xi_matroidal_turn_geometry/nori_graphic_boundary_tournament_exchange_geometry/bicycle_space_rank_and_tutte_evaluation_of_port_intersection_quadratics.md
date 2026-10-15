# Bicycle-space rank and Tutte evaluation of port intersection quadratics

Let \(W\subseteq\mathbb F_2^E\) be any binary linear code containing a vector of odd Hamming weight, with standard overlap pairing
\[
\langle x,y\rangle=|x\cap y|\pmod2.
\]
Put
\[
\beta=\dim W,\quad R=W\cap W^\perp,\quad b=\dim R,\quad
K=\{x\in W:|x|\equiv0\pmod2\}.
\]
Since \(W\) has an odd-weight vector, \(K\) is a hyperplane in \(W\); on \(K\) the overlap pairing is alternating.

**Theorem 1 (bicycle-rank formula for binary codes).** The rank of the alternating pairing restricted to \(K\) is
\[
\boxed{\operatorname{rank}\bigl(\langle\cdot,\cdot\rangle|_K\bigr)
=2\left\lfloor\frac{\beta-b-1}{2}\right\rfloor.}\tag{1}
\]
In particular, no further invariant of the binary code is needed to determine this rank.

*Proof.* Every \(r\in R\) has even weight, since \(\langle r,r\rangle=0\), so \(R\subseteq K\). Pass to \(\overline W=W/R\), whose induced symmetric bilinear pairing is nondegenerate and whose dimension is \(d=\beta-b\). Its diagonal map
\[
\ell(x)=\langle x,x\rangle=|x|\pmod2
\]
is a nonzero linear functional, and \(\overline K=K/R=\ker\ell\) has dimension \(d-1\).

By nondegeneracy there is a unique characteristic vector \(h\in\overline W\) satisfying \(\langle h,x\rangle=\ell(x)\) for every \(x\). A symmetric bilinear form over \(\mathbb F_2\) decomposes orthogonally into one-dimensional odd lines and hyperbolic alternating planes. In such a decomposition, \(h\) is the sum of the unit generators of the odd lines. Therefore
\[
\langle h,h\rangle=\dim\overline W=d\pmod2.
\]
The orthogonal complement of \(\overline K\) in \(\overline W\) is \(\langle h\rangle\). Hence the radical of the restriction to \(\overline K\) is zero if \(d\) is odd, and is \(\langle h\rangle\) of dimension one if \(d\) is even. Its rank is consequently \(d-1\) when \(d\) is odd, or \(d-2\) when \(d\) is even; both equal \(2\lfloor(d-1)/2\rfloor\). Since \(R\) is the radical of the pairing on \(W\), restricting from \(K\) to \(K/R\) does not change rank. Substituting \(d=\beta-b\) proves (1). \(\square\)

The dimension \(b\) is the **bicycle dimension** of the code: it measures the overlap of its linear subspace with its orthogonal complement. Theorem 1 applies to arbitrary binary matroid cycle spaces and not merely to graph-cover representations.

## Application to the monochromatic-component quotient

Let \(H\) be the turn graph of a connected two-sheeted graph cover, and let \(d\) be an admissible deck-odd turn signature. As in the preceding Subsection, contract the zero-turn connected components of \(H\) to form the connected multigraph \(J=J_d\), whose edges are precisely the changed turns. Because its edge-count parity measures covering monodromy and the latter is nonzero, the graph \(J\) has an odd cycle. Put
\[
\beta(J)=|E(J)|-|V(J)|+1,\qquad
b(J)=\dim\bigl(Z(J)\cap Z(J)^\perp\bigr),
\]
where the orthogonal complement is the cut space of \(J\). Let \(r_d\) be half the polar rank of the quadratic half-intersection form on port-free cocycles of the pointed lift.

**Theorem 2 (Tutte–bicycle formula for port intersection).** With this notation,
\[
\boxed{
2r_d=2\left\lfloor\frac{\beta(J)-b(J)-1}{2}\right\rfloor.}\tag{2}
\]
Equivalently, the port-cocycle quadratic rank is determined by the graph cycle rank and the bicycle dimension of \(J\). By the Rosenstiehl–Read evaluation of the Tutte polynomial,
\[
\boxed{|T_J(-1,-1)|=2^{b(J)},}\tag{3}
\]
and therefore one can recover the polar rank from \(\beta(J)\) and \(T_J(-1,-1)\).

*Proof.* The preceding monochromatic-component quotient theorem identifies the port-free cocycle space, modulo cycles of zero-turn edges, with the even-cardinality subspace \(K\) of \(Z(J)\). Its polar form is precisely the standard binary edge-overlap pairing on \(K\), and the quotient kernel has zero polar pairing against the entire port-free space. Consequently the two polar ranks agree. Apply Theorem 1 to \(W=Z(J)\), which contains odd-weight vectors, with radical dimension \(b(J)\). Equation (3) is the classical Rosenstiehl–Read identity. \(\square\)

**Corollary 3 (three-value modular distribution).** Set
\[
r=\left\lfloor\frac{\beta(J)-b(J)-1}{2}\right\rfloor.
\]
For a uniformly sampled port-containing binary cocycle \(Y\), the probability that
\(|X_d\cap Y|\equiv2\pmod4\) belongs to the three-element set
\[
\boxed{
\left\{\frac12,\quad
\frac12-2^{-r-1},\quad
\frac12+2^{-r-1}\right\}.}\tag{4}
\]
It is not merely bounded by this interval.

*Proof.* In the affine coset of port-containing cocycles, the half-intersection function is quadratic with polar rank \(2r\). Its sign sum is zero when its affine-linear restriction to the radical is nontrivial; otherwise it has absolute value \(2^{-r}\) times the size of the affine coset. This is the standard quadratic Gauss-sum calculation, also proved by squaring the sign sum in the previous Subsection. Dividing by the coset size yields (4). \(\square\)

For a connected graph, the bicycle dimension can also be determined by the nullity of the binary graph Laplacian: \(b(J)=\dim\ker L_J-1\). Consequently the complete modular-distribution bound is computable by binary Gaussian elimination on the monochromatic-component quotient, without enumerating cocircuits or colorings.

## Intrinsic pointed-matroid restriction theorem

Let \(M\) be a finite binary matroid, let \(p\) be a nonloop element, and let \(X\in Z(M)\) be a binary cycle containing \(p\). Put \(S=X\setminus\{p\}\) and let
\[
N=M|S
\]
be the restriction minor of \(M\) to \(S\). Define the binary bicycle dimension of \(N\) by
\[
b(N)=\dim\bigl(Z(N)\cap Z^*(N)\bigr),
\]
and write \(r(N)\) for the rank of \(N\).

**Theorem 4 (universal pointed intersection-rank formula).** On the port-free cocycle space
\[
K_p=\{Y\in Z^*(M):p\notin Y\},
\]
let
\[
B_X(Y,Z)=|X\cap Y\cap Z|\pmod2.
\]
Then
\[
\boxed{
\operatorname{rank}(B_X|_{K_p})
=2\left\lfloor\frac{r(N)-b(N)-1}{2}\right\rfloor.
}\tag{5}
\]
By the bicycle-space evaluation (Rosenstiehl–Read for graphs, extended to binary matroids by Jaeger, European J. Combin. 10 (1989), 247–255),
\[
\boxed{|T_N(-1,-1)|=2^{b(N)},}\tag{6}
\]
so the polar rank is determined solely by the rank and Tutte polynomial of the restriction minor \(N\). In particular, this quadratic invariant does not require a graph, a line-graph cover, a distinguished cocircuit length, or an admissible resource-path language.

*Proof.* Represent \(M\) over \(\mathbb F_2\) by a matrix \(A\). The binary cocycle space is the row space of \(A\), and coordinate restriction to \(S\) maps it surjectively onto the row space of \(A|S\), which is precisely \(Z^*(N)\). Denote this surjection by \(\rho\).

Because \(X\) is a binary cycle, cycle–cocycle orthogonality gives
\[
\mathbf1_Y(p)=|Y\cap S|\pmod2
\quad\text{for all }Y\in Z^*(M).
\tag{7}
\]
Thus \(\rho(K_p)\) equals the even-cardinality subspace
\[
K=\{z\in Z^*(N):|z|\equiv0\pmod2\}.
\]
Since \(p\) is a nonloop, some cocycle contains \(p\); by (7), \(Z^*(N)\) contains an odd-weight vector, and \(K\) is a hyperplane. The map \(\rho|_{K_p}\) is surjective onto \(K\), and its kernel has zero overlap pairing against every cocycle because all of its coordinates on \(S\) vanish. Therefore the polar rank on \(K_p\) equals the rank of the standard binary overlap form restricted to \(K\).

The full code \(W=Z^*(N)\) has dimension \(\beta=r(N)\), and its orthogonal complement is \(Z(N)\). Its radical hence has dimension \(b(N)\). Apply Theorem 1 to \(W\), giving precisely (5). The identity (6) is the classical bicycle-space evaluation of the Tutte polynomial, which holds for binary matroids. \(\square\)

**Corollary 5 (universal modular spectrum from a restriction minor).** Let
\[
r=\left\lfloor\frac{r(N)-b(N)-1}{2}\right\rfloor.
\]
Among all binary cocycles of \(M\) containing \(p\), the proportion meeting \(X\) in cardinality congruent to two modulo four belongs to
\[
\boxed{\left\{\frac12,\ \frac12-2^{-r-1},\
\frac12+2^{-r-1}\right\}.}\tag{8}
\]

*Proof.* The half-intersection quadratic function on the affine port-containing cocycles factors through the odd-weight coset of \(Z^*(N)\), by (7). Its polarization has rank \(2r\) by Theorem 4; the quadratic Gauss-sum dichotomy from Corollary 3 gives the stated three-value spectrum. \(\square\)

The theorem is a purely pointed-binary-matroid statement and is thus directly suitable for testing candidate intrinsic generalization classes. It also identifies a sharp limitation: modular intersection balance of *all* port-containing cocycles is governed by a restriction minor and need not impose any condition on minimum-size cocircuits or on the resource simplicity of their graph-cover witnesses.

**Corollary 6 (bicycle-corrected cycle-rank inequality).** In any signed line-graph cover with admissible turn cochain \(d\), put \(S=\operatorname{supp}(d)\), let \(r_0\) be the number of zero-turn connected components, and let \(J_d\) be the resulting connected multigraph on those components. If \(R(d)\) denotes the sum of the local star-cut polar ranks from the preceding Subsection, then
\[
\boxed{|S|-r_0\ge b(J_d)+R(d).}\tag{9}
\]
Thus the local quadratic mixing requires not merely global cycle rank but cycle rank *beyond the graph's bicycle space*.

*Proof.* The preceding local star theorem gives a lower bound \(R(d)\) for the polar rank of the port-free cocycle quadratic. By Theorem 2 this rank equals \(2\lfloor(\beta-b-1)/2\rfloor\), where \(\beta=|S|-r_0+1\) and \(b=b(J_d)\). Therefore
\[
R(d)\le 2\left\lfloor\frac{|S|-r_0-b}{2}\right\rfloor
\le |S|-r_0-b,
\]
which is (9). \(\square\)

**Corollary 7 (Laplace–Tutte computational interpretation).** For connected \(J_d\), its binary Laplacian satisfies
\[
b(J_d)=\dim\ker_{\mathbb F_2} L_{J_d}-1.
\]
Hence the quantity on the right side of (9) and the complete three-value modular spectrum can be computed by binary matrix rank calculations on the monochromatic-component quotient. When the number of spanning trees of \(J_d\) is odd, the bicycle dimension is zero; equivalently \(|T_{J_d}(-1,-1)|=1\).

*Proof.* A bicycle is a cut vector \(\partial^Tf\) that also lies in \(\ker\partial\); this is equivalent to \(L_{J_d}f=\partial\partial^Tf=0\). The map \(f\mapsto\partial^Tf\) has one-dimensional kernel for connected \(J_d\), yielding the displayed dimension identity. The matrix-tree theorem over \(\mathbb F_2\) identifies odd spanning-tree count with invertibility of a reduced Laplacian, which is equivalent to one-dimensional kernel of the full Laplacian and thus to \(b(J_d)=0\). \(\square\)
