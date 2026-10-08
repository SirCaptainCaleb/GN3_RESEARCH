# Canonical uncentered pair-defect and face-localization descent — preserved pre-item development

## Composition

(none yet)

## Development

## Canonical uncentered pair-defect for directed NOR

Fix coordinate-label arity \(r\ge 2\), a ground set \(V\) of size \(n\), and a reversal-antisymmetric coloring
\[
h(v_1,\ldots,v_r)\in\{0,1\},
\qquad
h(v_r,\ldots,v_1)=1-h(v_1,\ldots,v_r).
\]
For a coordinate order
\[
\pi=(v_1,\ldots,v_n),
\]
write
\[
c_i=h(v_i,\ldots,v_{i+r-1}),
\qquad
1\le i\le n-r+1,
\]
and
\[
d_i=c_i\oplus c_{i+1},
\qquad
1\le i\le m:=n-r.
\]

Define the pair-defect
\[
D(\pi)
=
\sum_{\substack{1\le i<j\le m\\ d_i=d_j=1}}
\bigl(e_{v_i}-e_{v_{j+r}}\bigr)
\in
W_V:=\Bigl\{x\in\mathbb R^V:\sum_{v\in V}x_v=0\Bigr\}.
\]

### Lemma 1: chamber zeros are exactly one-change orders

\[
D(\pi)=0
\quad\Longleftrightarrow\quad
\sum_{i=1}^m d_i\le 1.
\]

#### Proof

If the word has at most one change, there is no pair \(i<j\) with \(d_i=d_j=1\), so the sum is empty.

Conversely suppose there are at least two changes. Let \(\lambda_\pi\) be the linear functional determined by
\[
\lambda_\pi(e_{v_t})=t.
\]
Every summand satisfies
\[
\lambda_\pi(e_{v_i}-e_{v_{j+r}})
=
i-(j+r)<0.
\]
Hence \(\lambda_\pi(D(\pi))<0\), so \(D(\pi)\ne0\). \(\square\)

Thus \(D\) is an uncentered defect vector whose chamber-level zero set is exactly the directed NOR target. No pivot, chosen transition, or auxiliary gauge is required.

### Lemma 2: reversal oddness

If
\[
\pi^{\rm rev}=(v_n,\ldots,v_1),
\]
then
\[
D(\pi^{\rm rev})=-D(\pi).
\]

#### Proof

Reversal antisymmetry gives
\[
c_i(\pi^{\rm rev})
=
1-c_{n-r+2-i}(\pi),
\]
hence
\[
d_i(\pi^{\rm rev})
=
d_{m+1-i}(\pi).
\]
A pair \(i<j\) of changes in \(\pi\) corresponds in the reversed order to
\[
i'=m+1-j<j'=m+1-i.
\]
The associated reversed root is
\[
e_{v^{\rm rev}_{i'}}-e_{v^{\rm rev}_{j'+r}}
=
e_{v_{j+r}}-e_{v_i},
\]
the negative of the original root. Summing over all change pairs proves the claim. \(\square\)

### Lemma 3: positive balance on a permutahedral face localizes every change to one block

Let
\[
\mathcal F=B_1|\cdots|B_t
\]
be an ordered-partition face of the permutahedron, and let \(\pi\) range over chamber refinements of \(\mathcal F\). Suppose
\[
\sum_\pi \alpha_\pi D(\pi)=0,
\qquad
\alpha_\pi\ge0.
\]
For every \(\pi\) with \(\alpha_\pi>0\), every pair of change positions \(i<j\) of \(\pi\) satisfies
\[
v_i,\ v_{j+r}\in B_s
\]
for one common face block \(B_s\). In particular, if \(\pi\) is bad, all of its changes and all coordinate positions from its first change through \(r\) positions beyond its last change lie inside a single face block.

#### Proof

Let \(\beta(v)=s\) for \(v\in B_s\), extended linearly by \(\beta(e_v)=s\). Every chamber refining \(\mathcal F\) lists the blocks in the displayed order. Therefore for every root occurring in \(D(\pi)\),
\[
\beta(e_{v_i}-e_{v_{j+r}})
=
\beta(v_i)-\beta(v_{j+r})
\le0.
\]
Applying \(\beta\) to the positive balance gives zero as a sum of nonpositive terms. Hence every occurring term with positive coefficient has value zero, so its endpoints lie in the same block.

For a bad chamber choose its first and last changes \(f<\ell\). The root
\[
e_{v_f}-e_{v_{\ell+r}}
\]
occurs in \(D(\pi)\), so these endpoints lie in one block. Since face blocks are contiguous in every refinement, every coordinate position from \(f\) through \(\ell+r\) lies in that block. This contains every transition and every \(r\)-window participating in those transitions. \(\square\)

### Minimum-counterexample descent consequence

Assume \(V\) is a minimum directed-sector counterexample. If a positive zero relation involves all chamber refinements of a proper face \(\mathcal F\) with positive weight, then Lemma 3 forces a smaller counterexample.

Indeed every refinement is bad and has all changes internal to one face block. The host block is constant across refinements: adjacent swaps inside any other block leave the two or more internal changes of the host block untouched, while swaps inside the host block cannot create two internal changes in a different block whose internal order is unchanged. Since the product of the symmetric groups on the face blocks is connected by adjacent swaps, one fixed block \(B\) hosts all changes for every refinement.

Fix the orders of all other blocks and vary the order of \(B\). Every permutation of \(B\) then has at least two changes in its restricted \(r\)-window word. Thus \(h|_B\) is a counterexample on the proper subset \(B\), contrary to minimality.

### Topological status and remaining gap

The defect \(D\) takes values in the type-\(A\) root space \(W_V\), which has dimension \(n-1\), whereas the permutation Coxeter sphere has dimension \(n-2\). Hence ordinary Borsuk--Ulam does not by itself force a zero of the canonical cellular extension.

This isolates a one-dimension gap. Any mechanism that either

1. compresses \(D\) equivariantly by one dimension without destroying the face-localization descent, or
2. proves that the normalized odd self-map of the Coxeter sphere induced by \(D\) has impossible degree/carrier behavior,

would close the directed sector.

The gain over the earlier centered violation vector is that the chamber zero condition is already exactly the unrestricted one-change target, and any balanced face relation comes with an automatic minimum-counterexample descent.
