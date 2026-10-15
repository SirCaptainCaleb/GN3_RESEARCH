# Monochromatic-component quotients as canonical pointed cographic restriction minors

Let \(H\) be a finite connected graph, let \(B_H\) be its binary incidence matrix, and let \(a\in\mathbb F_2^{E(H)}\) represent a nonzero graph cohomology class. Form the pointed binary matroid
\[
D(H,a)=M\!\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*
\]
with port \(p\). For an admissible signature \(d=a+\delta f\), put
\[
S=\operatorname{supp}(d),
\]
and let \(J_d\) be the multigraph obtained by contracting every connected component of the spanning zero-signature subgraph \(H_0=(V(H),E(H)\setminus S)\). Its labeled edges are precisely the elements of \(S\), including possible loops. Write \(B_J\) for its binary incidence matrix and \(\mathbf1_S\) for the all-ones row on \(S\).

**Theorem 1 (canonical pointed cographic restriction minor).** There are canonical labeled binary-matroid isomorphisms
\[
\boxed{
D(H,a)|(S\cup\{p\})\cong
M\!\left(\begin{array}{c|c}B_J&0\\
\mathbf1_S&1\end{array}\right)^*,}
\tag{1}
\]
and
\[
\boxed{D(H,a)|S\cong M(J_d)^*.}\tag{2}
\]
The first restriction is a pointed parity coextension of the cographic matroid of \(J_d\). It depends only on the monochromatic-component quotient \(J_d\), not on the full turn graph or the chosen representative of the cohomology class.

*Proof.* The binary cocycle space of the dual \(D(H,a)\) is the kernel of its displayed primal representation:
\[
Z^*(D)=\left\{(z,t):B_Hz=0,\ 
t=\langle a,z\rangle\right\}.
\]
Since \(a=d+\delta f\) and every graph cycle is orthogonal to cuts, \(\langle a,z\rangle=\langle d,z\rangle=|z\cap S|\pmod2\). Thus
\[
Z^*(D)=\left\{\bigl(z,|z\cap S|\bmod2\bigr):
z\in Z(H)\right\}.\tag{3}
\]
Coordinate projection from \(Z(H)\) onto \(S\) is surjective onto \(Z(J_d)\), with kernel \(Z(H_0)\). For surjectivity, given an Eulerian set of changed edges of \(J_d\), pair its incident endpoints within each contracted zero-signature component and join each pair by zero-signature paths; the resulting mod-two union is Eulerian in \(H\). Consequently restriction of (3) to \(S\cup\{p\}\) gives
\[
\boxed{
Z^*(D|(S\cup\{p\}))
=\{(w,|w|\bmod2):w\in Z(J_d)\}.}\tag{4}
\]
The right-hand side of (4) is the kernel of the augmented matrix in (1), and hence is the binary cocycle space of its dual. A binary matroid is determined by its cocycle space, proving (1). Deleting the port coordinate from (4) gives \(Z(J_d)\), the cocycle space of the cographic matroid \(M(J_d)^*\), proving (2). \(\square\)

**Corollary 2 (port cocircuits are odd cycles of the quotient).** The cocircuits of \(D(H,a)|(S\cup\{p\})\) containing \(p\) are precisely the sets
\[
\boxed{C\cup\{p\},\quad
C\text{ a simple odd-length cycle of }J_d.}\tag{5}
\]
Loops count as odd cycles of length one. Therefore the shortest port-cocircuit size of the restriction minor is \(1+g_{\mathrm{odd}}(J_d)\).

*Proof.* An odd cycle \(C\) gives a cocycle \(C\cup\{p\}\) by (4). It is support-minimal because no nonzero Eulerian edge set lies in a proper subset of a simple graph cycle. Conversely, a cocycle containing \(p\) projects to an odd-cardinality Eulerian edge set of \(J_d\). Decompose it into edge-disjoint simple cycles. At least one constituent is odd, and the associated cocycle \(C\cup\{p\}\) lies inside the original cocycle. Support minimality therefore forces equality. \(\square\)

The theorem is valid for arbitrary binary graph-cover pointed lifts, including the folded cube and the boundary-tournament full-turn matroid. The restriction minor makes the quotient odd-cycle obstruction intrinsic to the matroid, but—because all unchanged turns have been deleted—it does not retain the length or resource-independence of a lift of an odd cycle to the original graph.
