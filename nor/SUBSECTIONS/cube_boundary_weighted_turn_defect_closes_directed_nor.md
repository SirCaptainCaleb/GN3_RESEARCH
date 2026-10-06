# Cube-boundary weighted turn defect closes directed NOR

## Metadata

- ID: cube_boundary_weighted_turn_defect_closes_directed_nor
- Parent Section: higher_memory_norine_geodesics
- Position: 34
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Cube-boundary lift closes the directed translation-invariant sector

### Theorem
Fix \(r\ge2\). Every reversal-antisymmetric binary coloring
\[
h(v_1,\ldots,v_r),\qquad
h(v_r,\ldots,v_1)=1-h(v_1,\ldots,v_r),
\]
on injective ordered \(r\)-tuples of a finite ground set \(V\) has a coordinate permutation whose sliding status word changes at most once.

### Proof by a minimum counterexample

Assume a counterexample exists and choose one with \(|V|=n\) minimum. Put
\[
M=n-r+1,\qquad
W_V=\{z\in\mathbb R^V:\sum_{v\in V}z_v=0\}.
\]
Every full permutation is bad, so its status word has at least two changes.

Triangulate the cube boundary \(\partial I^V\cong S^{n-1}\) by the standard Freudenthal triangulation on each facet. A top simplex in a zero-facet \(x=0\) is a maximal chain
\[
\varnothing\subset\cdots\subset V\setminus\{x\},
\]
hence an order \(\sigma\) of \(V\setminus\{x\}\); associate the full permutation
\[
\pi=(x,\sigma).
\]
A top simplex in the opposite facet \(x=1\) similarly gives a full permutation
\[
\pi=(\sigma,x).
\]

Choose arbitrary positive parameters
\[
a_x>0\quad(x\in V),\qquad
c_0,\ldots,c_r>0,
\qquad
C=\sum_{j=0}^r c_j.
\]

For a zero-facet simplex with full order \(\pi=(x,\sigma)\), let \(f(\pi)\) be the first transition index of its status word and define
\[
L(\pi)
=
a_x\left(
C e_x-\sum_{j=0}^r c_j e_{\pi_{f(\pi)+j}}
\right)\in W_V.
\tag{1}
\]
Thus the negative part is the positively weighted incidence vector of the ordered \((r+1)\)-coordinate witness of the first change.

For a one-facet simplex with full order \(\pi=(\sigma,x)\), let \(\ell(\pi)\) be the last transition index and define
\[
L(\pi)
=
a_x\left(
\sum_{j=0}^r c_{r-j}e_{\pi_{\ell(\pi)+j}}
-
C e_x
\right).
\tag{2}
\]

If a zero-facet simplex has full order \(\pi\), its antipodal one-facet simplex has full order \(\pi^{\rm rev}\). The first change of \(\pi\) becomes the last change of \(\pi^{\rm rev}\), and its ordered turn window is reversed. Hence
\[
L(\pi^{\rm rev})=-L(\pi).
\tag{3}
\]

Assign to the barycenter of every face of the boundary triangulation the average of \(L\) over the top simplices containing that face, and extend affinely over the barycentric subdivision. This gives a continuous odd map
\[
\Phi:\partial I^V\cong S^{n-1}\longrightarrow W_V\cong\mathbb R^{n-1}.
\]
By Borsuk--Ulam, \(\Phi\) has a zero.

### Non-pole zeros force descent

Take a zero and a smallest barycentric simplex containing it in its relative interior. Let \(F\) be the smallest ordinary Freudenthal face in that flag. Write its chain of cube vertices as
\[
A_0\subsetneq A_1\subsetneq\cdots\subsetneq A_t.
\]
Put
\[
O=A_0,\qquad Z=V\setminus A_t,
\]
and order the remaining coordinate blocks by the successive differences
\[
O\mid(A_1-A_0)\mid\cdots\mid(A_t-A_{t-1})\mid Z.
\]
At least one of \(O,Z\) is nonempty because \(F\) lies in the cube boundary.

Let \(\beta(v)\) be the index of the block containing \(v\).

Every zero-facet top simplex containing \(F\) has normal \(x\in Z\); its associated full permutation places \(x\) first, then refines the displayed block order, with \(Z\setminus\{x\}\) last. Therefore (1) gives
\[
\beta(L(\pi))
=
a_x\sum_{j=0}^r c_j
\bigl(\beta(x)-\beta(\pi_{f+j})\bigr)
\ge0,
\]
with equality precisely when the entire first-change turn window lies in \(Z\).

Similarly every one-facet top simplex containing \(F\) has normal \(x\in O\), places \(x\) last, and (2) gives
\[
\beta(L(\pi))\ge0,
\]
with equality precisely when the entire last-change turn window lies in \(O\).

Expanding the zero of \(\Phi\) gives a positive combination of top-simplex labels, and because the barycenter of \(F\) occurs with positive coefficient, every top simplex containing \(F\) occurs with positive coefficient. Applying \(\beta\) forces equality term by term. Hence:

- every zero-facet refinement of \(F\) has its first-change turn window wholly inside \(Z\);
- every one-facet refinement has its last-change turn window wholly inside \(O\).

Suppose \(Z\) is nonempty and proper. Choose \(x\in Z\). By minimality, \(h\) restricted to \(Z\setminus\{x\}\) has a one-change order \(\tau\). Choose a zero-facet top refinement of \(F\) whose final \(Z\setminus\{x\}\)-block is ordered as \(\tau\). Its full order has the form
\[
(x,\omega,\tau),
\]
where \(\omega\) uses the nonempty set \(V\setminus Z\).

Its first-change turn window lies wholly in \(Z\). Since \(x\) is separated from the terminal \(Z\setminus\{x\}\)-block by \(\omega\), that turn window lies wholly inside \(\tau\). Therefore no status change occurs before the status word induced by \(\tau\), and thereafter the changes are exactly those of \(\tau\). The full order consequently changes at most once, contradiction.

The case that \(O\) is nonempty and proper is symmetric, using a one-change order of \(O\setminus\{x\}\) and a one-facet refinement.

Thus a zero of \(\Phi\) can lie only over the two cube vertices
\[
\varnothing,\qquad V.
\tag{4}
\]

### Varying the positive weights makes the pole zero impossible

Borsuk--Ulam supplies a zero for every choice of the positive parameters \(a_x,c_j\). By (4) it must be a pole. Oddness exchanges the two poles, so both pole values are zero.

At the bottom pole \(\varnothing\), the containing top simplices are in bijection with all full permutations: \(\pi_1=x\) specifies the zero-facet normal. Hence
\[
0=
\sum_{\pi\in S_V}
a_{\pi_1}
\left(
C e_{\pi_1}
-
\sum_{j=0}^r c_j e_{\pi_{f(\pi)+j}}
\right).
\tag{5}
\]

The positive numbers \(a_x\) are arbitrary. Therefore, for each fixed \(x\),
\[
0=
\sum_{\pi:\pi_1=x}
\left(
C e_x
-
\sum_{j=0}^r c_j e_{\pi_{f(\pi)+j}}
\right).
\tag{6}
\]
There are \((n-1)!\) such permutations. Since the positive \(c_j\) are also arbitrary, (6) implies separately for every \(j\),
\[
\sum_{\pi:\pi_1=x} e_{\pi_{f(\pi)+j}}
=
(n-1)!\,e_x.
\tag{7}
\]

Take \(j=r\). Since every first transition index satisfies \(f(\pi)\ge1\),
\[
f(\pi)+r>1.
\]
Thus
\[
\pi_{f(\pi)+r}\ne \pi_1=x
\]
for every permutation in the sum. The \(x\)-coordinate of the left side of (7) is therefore \(0\), while the right side has \(x\)-coordinate \((n-1)!\), contradiction.

Hence no minimum counterexample exists. \(\square\)

### Remarks

1. The extra dimension absent from the permutation-sphere defect is supplied by the cube boundary: the source is \(S^{n-1}\), while the coordinate root space has dimension \(n-1\).
2. Positive weights are essential. They preserve face-localization while allowing independent variation at the pole, where the final contradiction occurs.
3. No computation is used. The only topological input is Borsuk--Ulam in equal source-sphere/target-vector dimension.

## Frontier

- Development version when composed: None
- Development version now: 1
