# Seam reseeding either preserves or splits the maximal support

## Composition

(none yet)

## Development

## A seam reseed either preserves the maximal support or splits its displayed order

Let
\[
S=(s_1,\ldots,s_k)
\]
be globally maximum among Hamiltonian supports with two-coverable complement in a no-two-cover boundary tournament \(H\). Let
\[
K\subseteq V(H)-S
\]
be a Hamiltonian four-support such that
\[
H-K=A\mid B
\]
is a two-cover.

By global maximality of \(S\),
\[
|A|,|B|\le k,
\]
because \(A\) and \(B\) are themselves admissible Hamiltonian supports in \(H\):
\[
H-A=B\mid K,\qquad H-B=A\mid K.
\]

Exactly one of the following structural alternatives occurs.

### 1. Support-preserving reseed

One of the two new cover components contains all of \(S\). Suppose
\[
S\subseteq A.
\]
Then
\[
|A|\ge|S|=k,
\]
while maximality gives \(|A|\le k\). Hence
\[
A=S.
\]
Thus the reseed cover has the exact form
\[
\boxed{H-K=S\mid R}
\]
for a Hamiltonian path \(R\) on the remaining vertices.

So whenever a reseed component contains the old maximal support, it contains nothing else: the old support survives as an entire cover component.

### 2. Support-splitting reseed

Neither \(A\) nor \(B\) contains all of \(S\). Since \(A\cup B=V(H)-K\) and \(K\cap S=\varnothing\), both \(A\cap S\) and \(B\cap S\) are nonempty.

Color each vertex \(s_i\) by whether it lies in \(A\) or \(B\). Since both colors occur, there is some
\[
1\le i<k
\]
for which
\[
s_i\in A,\qquad s_{i+1}\in B
\]
or vice versa. Therefore the displayed Hamilton path \(S\) has an ordinary edge
\[
\boxed{s_i s_{i+1}}
\]
whose endpoints lie in different components of the reseed two-cover.

Hence:

> **Reseed split theorem.** Every admissible seam four-support disjoint from a globally maximal support produces either
> \[
> H-K=S\mid R
> \]
> with \(R\) Hamiltonian, or a two-cover of \(H-K\) that splits an edge of the displayed maximal Hamilton path \(S\).

The second alternative is precisely a support-partition disturbance: the new two-cover cannot be compatible with the old support partition even at the level of displayed path edges.

For the explicit pure seam supports
\[
K_{PQ}=\{p_{m-1},p_m,q_1,q_2\},\qquad
K_{QP}=\{q_{t-1},q_t,p_1,p_2\},
\]
the theorem applies because each \(K\) is disjoint from \(S\).

Thus the vague "reseed" branch of the seam descent is reduced to a support-preserving \(4\mid k\mid(n-k-4)\) three-cover or an explicit split-edge comparison certificate on \(S\).
