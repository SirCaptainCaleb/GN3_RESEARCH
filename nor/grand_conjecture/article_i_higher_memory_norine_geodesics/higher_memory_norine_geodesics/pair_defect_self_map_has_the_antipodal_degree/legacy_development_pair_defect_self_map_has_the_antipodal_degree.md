# Pair-defect map deforms to the canonical endpoint carrier — preserved pre-item development

## Composition

(none yet)

## Development

## Pair-defect map deforms to the canonical endpoint carrier

Assume a minimum counterexample in the directed translation-invariant sector on a ground set \(V\), \(|V|=n\). Let
\[
D(\pi)=\sum_{\substack{i<j\\ d_i=d_j=1}}
(e_{v_i}-e_{v_{j+r}})
\in W_V
\]
be the canonical pair-defect, and let \(A_F\) denote its average over all chambers refining an ordered-partition face
\[
F=B_1|\cdots|B_s.
\]
The previous zero-free theorem gives a continuous odd face-average map
\[
\overline D:S^{n-2}\to W_V\setminus\{0\}.
\]

This note gives an explicit zero-free deformation of \(\overline D\) to the canonical endpoint carrier. It strengthens the carrier audit in the preceding subsection and fixes the sign convention in the first version of this note.

### Forward-cone lemma

For \(1\le t<s\), put
\[
U_t=B_1\cup\cdots\cup B_t
\]
and define
\[
\phi_t(z)=\sum_{v\in U_t} z_v.
\]
If \(\pi\) refines \(F\), every root
\[
e_{v_i}-e_{v_{j+r}}
\]
occurring in \(D(\pi)\) has its positive endpoint weakly earlier than its negative endpoint in the block order. Hence
\[
\phi_t(e_{v_i}-e_{v_{j+r}})\in\{0,1\},
\]
so
\[
\phi_t(A_F)\ge0.
\]

If \(F'\) refines \(F\), the same conclusion holds for \(A_{F'}\) at every cut of \(F\).

### Canonical endpoint carrier

For
\[
F=B_1|\cdots|B_s
\]
define
\[
u_F=
\frac1{|B_1|}\mathbf 1_{B_1}
-
\frac1{|B_s|}\mathbf 1_{B_s}
\in W_V.
\]
Then
\[
u_{F^{\rm rev}}=-u_F.
\]
If \(F'\) refines \(F\), the first block of \(F'\) lies inside \(B_1\) and the last block lies inside \(B_s\), so for every cut of \(F\),
\[
\phi_t(u_{F'})=1.
\]

Assign \(u_F\) to the barycenter of \(F\) and extend affinely on the barycentric subdivision. Call the resulting odd map
\[
G:S^{n-2}\to W_V.
\]

For a barycentric simplex corresponding to a chain
\[
F_0\subsetneq F_1\subsetneq\cdots\subsetneq F_m,
\]
use the first block \(B_1\) of \(F_0\) and
\[
\phi(z)=\sum_{v\in B_1}z_v.
\]
Then
\[
\phi(u_{F_i})=1
\]
for every \(i\), so every convex combination of the \(u_{F_i}\) is nonzero. Thus \(G\) is zero-free.

With the project’s standard Coxeter realization, the coordinate value is weakly decreasing from the first block of a face to the last. Hence the endpoint carrier points into the same face hemisphere as the radial barycentric direction. Equivalently, the normalized map \(G/\|G\|\) is carried with the identity by the standard Coxeter face carrier and is homotopic to the identity. Therefore
\[
\deg(G)=+1.
\]

### The pair-defect map is equivariantly homotopic to \(G\)

At every face barycenter set
\[
H_t(b_F)=(1-t)A_F+t\,u_F,
\qquad 0\le t\le1,
\]
and extend affinely on barycentric simplices.

Oddness is preserved because both \(A_F\) and \(u_F\) negate under face reversal.

At \(t=0\), the minimum-counterexample zero-free theorem gives
\[
H_0=\overline D\ne0.
\]
Fix \(t>0\) and a barycentric simplex with coarsest face
\[
F_0=B_1|\cdots|B_s.
\]
For
\[
\phi(z)=\sum_{v\in B_1}z_v
\]
the forward-cone lemma gives
\[
\phi(A_{F_i})\ge0,
\]
while
\[
\phi(u_{F_i})=1.
\]
Thus every vertex label of the simplex satisfies
\[
\phi(H_t(b_{F_i}))\ge t>0.
\]
Every affine combination in that simplex is therefore nonzero. Hence \(H_t\) is zero-free for all \(t>0\).

So \(\overline D\) and \(G\) are joined by an odd zero-free homotopy. With the standard realization,
\[
\deg\!\left(\frac{\overline D}{\|\overline D\|}\right)=+1.
\]

### Consequence for the closure strategy

The degree branch of the pair-defect route is closed off: forward-root carrier geometry deforms to the canonical endpoint carrier and supports degree \(+1\), rather than a contradiction.

Any successful topological closure must retain information discarded by this deformation, such as the coloring-dependent coefficients, transition-pair incidence, or a lower-dimensional chain-valued structure.
