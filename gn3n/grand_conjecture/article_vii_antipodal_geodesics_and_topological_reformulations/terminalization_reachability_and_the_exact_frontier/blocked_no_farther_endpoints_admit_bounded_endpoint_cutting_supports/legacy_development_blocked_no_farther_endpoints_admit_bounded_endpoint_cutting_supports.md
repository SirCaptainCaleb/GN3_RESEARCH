# Blocked no-farther endpoints admit bounded endpoint-cutting supports — preserved pre-item development

## Development

## A blocked/no-farther endpoint has a bounded endpoint-cutting Hamiltonian support

Retain a genuine mixed reflected-double chamber
\[
J=(x,c_1,\ldots,c_N,y)
\]
and suppose there is no strictly farther positive witness on the left. Let \(z_1,z_2\) be the first two ambient vertices immediately to the left of \(x\), when they exist.

By [[no_farther_positive_witness_forces_monochromatic_outward_status_rays]], the outward prefix is a tight path. In particular
\[
(z_2,z_1,x,c_1)
\]
is tight, so
\[
(z_2,z_1,x)
\]
is a tight three-vertex path.

Apply the local prescribed-exterior-endpoint theorem in [[localextend01]] to
\[
(a,b,c)=(z_2,z_1,x),
\qquad d=c_2,
\qquad y=c_1.
\]
It gives a set
\[
K\subseteq\{z_2,z_1,x,c_1,c_2\},
\qquad 4\le |K|\le5,
\qquad c_1\in K,
\]
having a Hamiltonian tight path in which \(c_1\) is an endpoint.

This statement is completely local and uses no minimum-counterexample consequence of the prescribed-endpoint theorem.

Now let
\[
P=(c_1,c_2,c_3,\ldots)
\]
be the corridor path containing the left endpoint. Since the only vertices of \(P\) available to \(K\) are \(c_1,c_2\), exactly one of the following holds:

1. \(K\cap V(P)=\{c_1\}\), and the untouched remainder
   \[
   P'=(c_2,c_3,\ldots)
   \]
   is a tight path; or
2. \(K\cap V(P)=\{c_1,c_2\}\), and the untouched remainder
   \[
   P''=(c_3,c_4,\ldots)
   \]
   is a tight path.

Thus a two-layer outward guard always supplies a bounded Hamiltonian support that **cuts off the corridor endpoint while leaving a contiguous tight tail**. The right-hand mirror is identical.

### Why this is the correct rooted primitive

In a uniformly blocked sector one has
\[
h(z,c_1,c_2)=0
\]
for every available outer label \(z\). Consequently no Hamilton path supported only on the blocked outer labels together with \(c_1,c_2\) can have terminal segment
\[
(z,c_1,c_2),
\]
so a theorem demanding preservation of the old ordered corridor endpoint \(c_1,c_2\) is structurally mis-aimed.

The endpoint-cutting support above avoids that impossible requirement. It replaces the old boundary by a Hamiltonian packet having \(c_1\) itself as an endpoint and shortens the untouched corridor by one or two vertices. Hence the remaining gluing problem should be formulated as a **boundary repartition / endpoint transport** theorem:

> combine the endpoint-cutting Hamiltonian support with the surviving contiguous corridor tail and the opposite corridor component, rather than trying to attach a blocked vertex to the original pair \(c_1,c_2\).

This does not yet yield a spanning two-cover: the complement of \(K\) need not be Hamiltonian, and the Hamilton order on \(K\) need not be oriented compatibly with a prescribed outside tail. What it does prove is that the blocked/no-farther branch admits a bounded repartition which preserves the long corridor only as an untouched suffix, eliminating the false fixed-root requirement that caused earlier repair attempts to fail.
