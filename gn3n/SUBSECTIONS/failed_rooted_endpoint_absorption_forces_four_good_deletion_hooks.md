# Failed rooted endpoint absorption forces four good-deletion hooks

## Metadata

- ID: failed_rooted_endpoint_absorption_forces_four_good_deletion_hooks
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 168
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Failed rooted endpoint absorption forces at least four good-deletion wrong-way hooks

Let
\[
T=(x,y,z,\ldots)
\]
be the frozen tight corridor at one endpoint, and let \(A\) be the disjoint six-vertex endpoint packet.

Define the good-deletion set
\[
G(A)=\{v\in A:H[A-v]\text{ is Hamiltonian}\}.
\]
By the four-of-six theorem,
\[
|G(A)|\ge4.
\]

Suppose \(v\in G(A)\) satisfies
\[
h(v,x,y)=1.
\]
Since \(T\) is tight,
\[
h(x,y,z)=1
\]
and all later corridor triples are tight. Hence
\[
(v,x,y,z,\ldots)
\]
is a tight path. Its complement in
\[
A\cup V(T)
\]
is exactly \(A-v\), which is Hamiltonian by the choice of \(v\). Therefore
\[
(A-v)\mid(v,x,y,z,\ldots)
\]
is a two-cover of the endpoint packet together with the entire frozen corridor.

Consequently, if direct rooted endpoint absorption fails, then
\[
h(v,x,y)=0
\qquad(v\in G(A)).
\]
Boundary antisymmetry gives
\[
\boxed{h(y,x,v)=1\qquad(v\in G(A)).}
\]

Thus:

> **Four-good-hook theorem.** Failure of rooted endpoint absorption forces at least four distinct wrong-way hooks through the same ordered interface pair \((y,x)\), and every label not carrying such a forced hook lies in the bad-deletion set
> \[
> B(A)=A-G(A),
> \qquad |B(A)|\le2.
> \]

Equivalently, all possible one-label forward connectors across the corridor edge \(x,y\) are confined to at most two packet labels, and each such label has non-Hamiltonian five-vertex complement inside \(A\).

This strengthens [[rooted_corridor_absorption_reduces_to_a_bounded_three_hook_residue]] for the direct one-label attachment problem: the obstruction supplies at least four hooks, not merely three predecessor hooks, and those hooks are exactly the good-deletion labels of the six-packet.

No prescribed-endpoint theorem, cyclic rotation, or minimum-counterexample hypothesis is used.
