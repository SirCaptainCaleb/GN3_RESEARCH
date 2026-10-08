# Imbalanced minimum holes descend to four-component one-hole cores

## Composition

(none yet)

## Development

## Imbalance descends either to an all-old four-support or to deletion-distance one

Retain the setup of [[imbalanced_minimum_hole_complements_force_dense_endpoint_spanning_four_supports]].

Let
\[
X
\]
be a minimum deletion hole, and choose a \(\Psi\)-minimal two-cover
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t),
\]
with
\[
t\ge s+2.
\]
Use the fixed pair
\[
\{p_1,p_s\}
\]
and its two orientation classes on
\[
R=X\cup\{q_1,q_t\}.
\]

There are two cases.

### Case 1: \(q_1,q_t\) lie in the same class

Then the fixed-pair theorem gives
\[
K_0=\{p_1,p_s,q_1,q_t\}
\]
Hamiltonian.

Removing the four endpoint vertices leaves the two inherited contiguous tight paths
\[
P^\circ=(p_2,\ldots,p_{s-1}),
\qquad
Q^\circ=(q_2,\ldots,q_{t-1}),
\]
with the usual convention for paths of order at most two.

Hence
\[
\boxed{K_0\mid P^\circ\mid Q^\circ}
\]
is a spanning three-cover of \(H-X\) with a distinguished Hamiltonian four-component entirely on old, non-hole vertices.

### Case 2: \(q_1,q_t\) lie in opposite classes

Every hole label \(x\in X\) belongs to exactly one of the two classes, so it agrees with exactly one endpoint
\[
q(x)\in\{q_1,q_t\}.
\]
Therefore
\[
K_x=\{p_1,p_s,q(x),x\}
\]
is Hamiltonian for every \(x\in X\).

Now put
\[
G_x=H-(X-\{x\}).
\]
Hereditary exactness of a minimum deletion hole gives
\[
\boxed{\kappa_2(G_x)=1.}
\]

If \(q(x)=q_1\), then
\[
K_x
\mid
(p_2,\ldots,p_{s-1})
\mid
(q_2,\ldots,q_t)
\]
is a spanning three-cover of \(G_x\).

If \(q(x)=q_t\), use instead
\[
K_x
\mid
(p_2,\ldots,p_{s-1})
\mid
(q_1,\ldots,q_{t-1}).
\]

Thus:

> **Imbalance-to-one-hole theorem.** A \(\Psi\)-minimal imbalanced two-cover of a minimum-hole complement has one of two outputs:
> 1. an all-old spanning three-cover with a Hamiltonian four-component; or
> 2. for every hole label \(x\), a canonical induced \(\kappa_2=1\) core \(G_x\) having a spanning three-cover with a Hamiltonian four-component containing \(x\).

### Elevation consequence

This connects the \(k\ge2\) zero-root/minimum-hole branch directly to the mature deletion-distance-one theory [[kappa_one_role_balance_and_ky_fan]].

In the opposite-endpoint-signature case, there is no need to analyze the entire large hole simultaneously: **every individual hole label already carries a rooted four-component state at deletion distance one**.

In the same-signature case, the large-hole complement itself has a four-component three-cover with both long-path endpoint pairs shortened simultaneously.

Therefore any proof that controls four-component three-covers at \(\kappa_2=1\), together with their all-old analogue, immediately constrains imbalance in every minimum deletion complement.
