# Boundary-layer external reversals give a four-support or endpoint transfer

## Composition

(none yet)

## Development

## Boundary-layer external reversals give a four-support or a legal endpoint transfer

Let
\[
A=(a_1,\ldots,a_r),\qquad B=(b_1,\ldots,b_s)
\]
be vertex-disjoint tight paths, with \(r\ge2\) and \(s\ge2\). Consider an external reversal of the terminal edge of \(A\) carried from the initial boundary layer of \(B\).

### Endpoint carrier

Assume
\[
h(b_1,a_r,a_{r-1})=1.
\]
Test
\[
h(a_r,b_1,b_2).
\]

If this triple is tight, then
\[
A^-=(a_1,\ldots,a_{r-1}),
\qquad
(a_r,b_1,b_2,\ldots,b_s)
\]
are tight paths. Thus the endpoint \(a_r\) may be transferred legally from \(A\) to the front of \(B\).

If instead
\[
h(a_r,b_1,b_2)=0,
\]
boundary antisymmetry gives
\[
h(b_2,b_1,a_r)=1.
\]
Together with the standing reversal,
\[
h(b_1,a_r,a_{r-1})=1,
\]
this gives the Hamiltonian four-path
\[
\boxed{(b_2,b_1,a_r,a_{r-1})}.
\]

Hence an endpoint carrier gives either a legal one-vertex endpoint transfer or a Hamiltonian four-support.

### Second-layer carrier

Assume now
\[
h(b_2,a_r,a_{r-1})=1.
\]

First test
\[
h(b_1,b_2,a_r).
\]
If it is tight, then
\[
(b_1,b_2,a_r,a_{r-1})
\]
is a Hamiltonian four-path.

Assume therefore
\[
h(b_1,b_2,a_r)=0.
\]
Boundary antisymmetry gives
\[
h(a_r,b_2,b_1)=1.
\]

Now test the first legal transfer:
\[
h(a_r,b_1,b_2).
\]
If it is tight, move \(a_r\) from the terminal end of \(A\) to the initial end of \(B\):
\[
(a_1,\ldots,a_{r-1})
\mid
(a_r,b_1,\ldots,b_s).
\]

Assume this transfer fails. Then
\[
h(b_2,b_1,a_r)=1.
\]

Test the opposite legal transfer:
\[
h(a_{r-1},a_r,b_1).
\]
If it is tight, move \(b_1\) from the initial end of \(B\) to the terminal end of \(A\):
\[
(a_1,\ldots,a_r,b_1)
\mid
(b_2,\ldots,b_s).
\]

If this transfer also fails, boundary antisymmetry gives
\[
h(b_1,a_r,a_{r-1})=1.
\]
Together with
\[
h(b_2,b_1,a_r)=1
\]
we obtain the Hamiltonian four-path
\[
\boxed{(b_2,b_1,a_r,a_{r-1})}.
\]

Therefore:

> **Boundary-layer reversal conversion.** If an exterior vertex in the first two positions of one displayed path reverses the terminal edge of another displayed path, then either a Hamiltonian four-support occurs on the two boundary layers, or one endpoint can be transferred legally from one path to the other.

The three symmetric orientations satisfy the same conclusion.

Combined with [[oriented_reversal_carriers_of_arbitrary_displayed_edges_are_one_sided_boundary_layer_vertices]], every external displayed-edge reversal reduces to:
- a Hamiltonian four-support; or
- a legal endpoint transfer between the two displayed paths.

No cyclic permutation of a triple and no reversal of a tight path is used.

### Potential change

If the transfer moves one vertex from a path of order \(r\) to one of order \(s\), the affected quadratic potential changes by
\[
(r-1)^2+(s+1)^2-r^2-s^2
=
2(s-r+1).
\]
Thus a transfer from a path at least two vertices larger than the receiving path is a strict \(\Phi\)-decrease.
