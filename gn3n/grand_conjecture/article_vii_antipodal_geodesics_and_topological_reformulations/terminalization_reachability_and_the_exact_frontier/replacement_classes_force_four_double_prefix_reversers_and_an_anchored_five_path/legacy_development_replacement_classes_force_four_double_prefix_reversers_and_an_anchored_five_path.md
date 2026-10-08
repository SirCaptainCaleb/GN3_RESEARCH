# Replacement classes force four double-prefix reversers and an anchored five-path — preserved pre-item development

## Composition

(none yet)

## Development

## Replacement classes for a longest reversed-pair path

Assume the odd uniform residue on \(n=2r+1\) vertices, \(r\ge3\): every \(r\)-set is Hamiltonian and every \((r+1)\)-set is non-Hamiltonian. Retain a maximum path beginning in an ordered pair \((a,b)\), and let
\[
R=(c_1,c_2,\ldots,b,a)
\]
be a longest tight path ending in the reversed pair \((b,a)\). By the reversed-endpoint-pair augmentation theorem, \(R\) has order
\[
3\le t\le r-1.
\]
Put \(E=V(H)-V(R)\).

Define the first-position replacement set
\[
A^\ast=\{z\in E:(z,c_2,c_3,\ldots,b,a)\text{ is tight}\},
\qquad A=\{c_1\}\cup A^\ast.
\]

### Uniform transition relation on the replacement class

For every \(z\in A\) and every
\[
y\in(\{c_1\}\cup E)-\{z\},
\]
one has
\[
(c_2,z,y)\text{ tight}.
\]

For \(z=c_1\), this is the universal prepend reversal already forced by maximality of \(R\): if \((y,c_1,c_2)\) were tight, then \((y,R)\) would be a longer path with terminal pair \((b,a)\).

For \(z\in A^\ast\), the replacement word
\[
R_z=(z,c_2,c_3,\ldots,b,a)
\]
is another longest path with the same terminal pair. The vertex \(y\) is exterior to \(R_z\). Hence \((y,z,c_2)\) cannot be tight, else \((y,R_z)\) would be longer. Boundary antisymmetry gives \((c_2,z,y)\) tight.

### The replacement class has order at most \(r-1\)

If \(|A|\ge r\), choose an \(r\)-subset \(S\subseteq A\). By the odd uniform hypothesis \(S\) has a Hamilton order
\[
(z_1,\ldots,z_r).
\]
Since \(z_1,z_2\in A\), the uniform transition relation gives
\[
(c_2,z_1,z_2)
\]
tight. Therefore
\[
(c_2,z_1,\ldots,z_r)
\]
is a tight \((r+1)\)-path, contradiction. Thus
\[
\boxed{|A|\le r-1,\qquad |A^\ast|\le r-2.}
\]

Consequently the nonreplacement set
\[
N=E-A^\ast
\]
has
\[
|N|\ge |E|-(r-2)=r+3-t\ge4.
\]

### Every nonreplacement root reverses two adjacent prefix edges

For \(x\in N\), failure of the replacement word gives
\[
(x,c_2,c_3)\text{ non-tight},
\]
hence
\[
(c_3,c_2,x)\text{ tight}.
\]
The universal prepend reversal for \(R\) also gives
\[
(c_2,c_1,x)\text{ tight}.
\]
Thus every \(x\in N\) simultaneously reverses the two adjacent prefix edges
\[
c_1c_2,\qquad c_2c_3
\]
in the literal orientations
\[
(c_2,c_1,x),\qquad(c_3,c_2,x).
\]

This is a scale-independent alternative: the first-position rotation class cannot become large, so at least four exterior labels fall into one common double-reversal class.

## Local lemma: three common double-prefix reversers force an anchored five-path

Let \((a,b,c)\) be a tight three-path and let \(x,y,z\) be three distinct exterior vertices satisfying
\[
(b,a,u),\qquad(c,b,u)
\]
tight for every \(u\in\{x,y,z\}\).

For each root put
\[
\theta(u)=h(a,u,c)\in\{0,1\}.
\]
Two roots, say \(x,y\), have the same \(\theta\)-value.

If \(\theta(x)=\theta(y)=1\), then
\[
(a,x,c),\qquad(a,y,c)
\]
are tight. Exactly one of \((x,c,y)\), \((y,c,x)\) is tight. In the first case
\[
(b,a,x,c,y)
\]
is a tight five-path; in the second case
\[
(b,a,y,c,x)
\]
is.

Now suppose \(\theta(x)=\theta(y)=0\). Boundary antisymmetry gives
\[
(c,x,a),\qquad(c,y,a)
\]
tight. Relabel \(x,y\) if necessary so that
\[
(x,a,y)
\]
is tight. If \((b,c,x)\) is tight, then
\[
(b,c,x,a,y)
\]
is a tight five-path. Otherwise \((x,c,b)\) is tight. If \((b,y,a)\) is tight, then
\[
(x,c,b,y,a)
\]
is a tight five-path, using the standing relation \((c,b,y)\). If \((b,y,a)\) is non-tight, boundary antisymmetry gives \((a,y,b)\) tight, and
\[
(c,x,a,y,b)
\]
is a tight five-path.

Hence in all cases some pair among three common double-prefix reversers forms a Hamiltonian five-set together with \(a,b,c\).

Applying this with
\[
(a,b,c)=(c_1,c_2,c_3)
\]
and any three vertices of \(N\) yields a Hamiltonian five-support
\[
\boxed{\{c_1,c_2,c_3,x,y\}}
\]
with an explicit Hamilton order and with \(x,y\) drawn from the common double-reversal class.

### Audit boundary

The Hamiltonian five-support is not by itself a terminal outcome in a minimum counterexample; bare bounded support is automatic once its complement is proper. The retained information is stronger: the support contains the first three vertices of a longest path with the prescribed terminal pair \((b,a)\), while its two added roots belong to a common exterior class reversing both adjacent prefix edges.

The closure target is to use this anchored five-support to obtain inherited rail shortening, a compatible endpoint transfer, or a longer path preserving enough of the fixed-terminal geometry. No spanning two-cover is claimed here.
