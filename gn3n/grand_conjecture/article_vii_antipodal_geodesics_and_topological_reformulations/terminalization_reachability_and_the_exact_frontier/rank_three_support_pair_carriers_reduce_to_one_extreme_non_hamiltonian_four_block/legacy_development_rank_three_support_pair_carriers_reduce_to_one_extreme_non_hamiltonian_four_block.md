# Rank-three support-pair carriers reduce to one extreme non-Hamiltonian four-block — preserved pre-item development

## Composition

(none yet)

## Development

## Rank-three support-pair carriers reduce to one extreme non-Hamiltonian four-block

Work with the singleton-allowed support-pair target
\[
\widehat{\mathcal P}(H)
=
\{(A,B): A,B\neq\varnothing,\ A\cap B=\varnothing,\ H[A],H[B]\text{ Hamiltonian}\}.
\]

Let \(F\) be a rank-three face of the permutahedron, written as an ordered partition into face blocks. Thus
\[
\sum_{W\in F}(|W|-1)=3,
\]
so the non-singleton block sizes have one of the types
\[
4,\qquad 3+2,\qquad 2+2+2.
\]

For each chamber \(\pi\in F\), let
\[
C(\pi)=(P_\pi,Q_\pi)
\]
be its canonical nonempty partial two-cover. Put
\[
A_F=\bigcap_{\pi\in F}P_\pi,\qquad
B_F=\bigcap_{\pi\in F}Q_\pi.
\]

As in the rank-two analysis, whenever nonempty \(A_F\) is an inherited common prefix and \(B_F\) an inherited common suffix, hence Hamiltonian.

Consider the natural face carrier generated downward by the chamber states and by their common-lower support-pair intersections. The following alternatives hold.

### 1. Both common sides survive

If
\[
A_F\neq\varnothing,\qquad B_F\neq\varnothing,
\]
then
\[
Z=(A_F,B_F)\in\widehat{\mathcal P}(H)
\]
lies below every chamber state. Every common-lower state obtained from intersections of chamber supports also contains \(A_F\) and \(B_F\). Hence the natural face carrier is coned by \(Z\).

### 2. Exactly one common side disappears

Assume
\[
A_F=\varnothing,\qquad B_F\neq\varnothing.
\]
Then the first face block \(W\) is non-singleton; otherwise its fixed first singleton would belong to every \(P_\pi\).

If
\[
|W|\le3,
\]
every nonempty subset of \(W\) is Hamiltonian. Intersecting the left support of every carrier state with \(W\), while replacing its right support by \(B_F\), gives an order-preserving downward deformation into the cone under
\[
(W,B_F).
\]
Thus the carrier is contractible.

The same conclusion holds when \(|W|=4\) and \(H[W]\) is Hamiltonian.

Therefore the only unresolved subcase with exactly one vanished common side is
\[
\boxed{|W|=4,\quad H[W]\text{ non-Hamiltonian}.}
\]
Because \(|W|-1=3\), this is necessarily the unique non-singleton block of \(F\). The symmetric statement holds when \(B_F=\varnothing\): the only unresolved case is a non-Hamiltonian final block of order four.

### 3. Both common sides disappear

Assume
\[
A_F=B_F=\varnothing.
\]
Then both the first and last face blocks are non-singleton. Since each contributes at least one to the rank and the total rank is three, both extreme blocks have order at most three. In particular both are Hamiltonian.

Let \(W_L\) and \(W_R\) be the first and last blocks. Every natural carrier state has nonempty intersection of its left support with \(W_L\) and of its right support with \(W_R\). The map
\[
(A,B)\longmapsto(A\cap W_L,\;B\cap W_R)
\]
is an order-preserving downward deformation into the cone under
\[
(W_L,W_R).
\]
Hence the carrier is contractible.

### Conclusion

Every rank-three face has a contractible natural singleton-support carrier except possibly when one extreme block is a non-Hamiltonian four-set and the opposite common side survives.

Thus the first local obstruction after the automatically fillable two-skeleton is exactly the first place where Hamiltonicity itself ceases to be universal:
\[
\boxed{\text{nonempty sets of size }\le3\text{ are harmless; a non-Hamiltonian }K_4\text{ is first.}}
\]

This makes the later four-/five-set extension theory relevant at the correct earlier stage. If the exceptional four-block \(W\) has an exterior label \(z\) such that \(H[W\cup\{z\}]\) is Hamiltonian and \(z\) is disjoint from the surviving opposite common support, then
\[
(W\cup\{z\},B_F)
\]
cones the exceptional carrier as well. Hence a genuine rank-three obstruction requires a relative four-set extension desert: no usable exterior vertex may Hamiltonian-extend the extreme block while remaining disjoint from the opposite common support.

This is a carrier reduction, not yet a globally coherent rank-three extension theorem. It deliberately avoids assuming that independently chosen two-face fillings agree across adjacent rank-three faces.
