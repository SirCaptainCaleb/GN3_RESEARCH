# Correction: minimum holes have four-end synchronization and bidirectional root-advance certificates

## Composition

### Four-end synchronization and bidirectional one-step root advance

Let \(X\) be a minimum deletion set and \(H-X=P\mid Q\). Every \(x\in X\) reverses all four exposed end edges of the displayed two-cover. For every three-subset \(U\subseteq X\), hereditary exactness gives
\[
\kappa_2\!\left(H-(X\setminus U)\right)=3.
\]
The three restored labels are common reversers at either boundary, so the one-step root-advance lemma applies from both ends of the same base cover. Hence every three-hole core carries bounded root-advance five-path certificates from both boundaries. No spanning three-cover is inferred by recursive lifting.

## Development

## Correction: minimum holes are four-end synchronized and three-hole cores have bidirectional one-step root advance

Let
\[
X\subseteq V(H),\qquad |X|=\kappa_2(H),
\]
be a minimum two-cover deletion set, and fix
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t).
\]

For every \(x\in X\), absolute nonaugmentability gives
\[
\boxed{
\begin{aligned}
h(p_2,p_1,x)&=1,\\
h(x,p_s,p_{s-1})&=1,\\
h(q_2,q_1,x)&=1,\\
h(x,q_t,q_{t-1})&=1.
\end{aligned}}
\]
Thus every minimum-hole vertex reverses all four exposed end edges of the displayed two-cover.

Choose any three-subset
\[
U=\{u,v,w\}\subseteq X
\]
and form
\[
G_U=H-(X-U).
\]
By hereditary exactness,
\[
\kappa_2(G_U)=3.
\]

At the initial ends of \(P,Q\), the labels \(u,v,w\) are three common reversers, so [[three_common_initial_reversers_force_a_root_advancing_five_path]] gives a one-step root-advancing five-path.

At the opposite ends, use the displayed terminal reversal relations as the symmetric local input; equivalently reindex the two exposed terminal edges as the new rooted edges. The same three-label pigeonhole argument gives a second one-step root-advance certificate from the opposite boundary.

Hence every exact three-hole core is **bidirectionally rooted**: it carries bounded root-advance five-path certificates from both ends of the same underlying deleted two-cover.

The earlier version of this addendum claimed spanning three-covers from both ends by invoking [[three_common_reversers_force_a_three_cover_by_finite_root_advance]]. That recursive lift is not established, so those path-cover assertions are withdrawn.

### Valid strategic consequence

The natural fixed-layer obstruction is not an arbitrary \(\kappa_2=3\) boundary tournament. It is a synchronized three-hole core whose three deleted labels reverse all four exposed ends and admit one-step root advance from both boundaries.

This two-sided bounded structure remains available for endpoint transport, six-set deletion graphs, and pairwise repartition arguments without relying on the invalid recursive covering lift.
