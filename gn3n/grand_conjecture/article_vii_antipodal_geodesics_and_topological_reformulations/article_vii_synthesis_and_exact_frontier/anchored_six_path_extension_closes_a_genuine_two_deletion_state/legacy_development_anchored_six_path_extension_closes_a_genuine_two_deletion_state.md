# Anchored six-path extension closes a genuine two-deletion state — preserved pre-item development

## Anchored six-path extension closes a genuine two-deletion state

Let \(H\) satisfy \(\kappa_2(H)=2\), let \(X=\{x,y\}\) be a minimum deletion pair, and fix
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_r),\quad Q=(q_1,\ldots,q_s),
\]
with \(r,s\ge3\). Put
\[
u=p_{r-2},\quad a=p_{r-1},\quad b=p_r,
\qquad
c=q_s,\quad d=q_{s-1},\quad v=q_{s-2},
\]
and let
\[
M=\{b,x,y,c\}.
\]

Suppose there is an ordering
\[
(z_1,z_2,z_3,z_4)
\]
of \(M\) such that
\[
(u,a,z_1,z_2,z_3,z_4)
\]
is a tight path. Then \(H\) has a spanning two-cover.

Indeed,
\[
(p_1,\ldots,p_{r-2},a,z_1,z_2,z_3,z_4)
\]
is a tight path: its inherited prefix ends in \((u,a)\), and the displayed six-path supplies every new junction triple. This path uses all vertices of \(P\), both hole labels, and the terminal vertex \(c=q_s\) of \(Q\). The remaining vertices
\[
(q_1,\ldots,q_{s-1})
\]
form the inherited tight path \(Q-c\). These two paths partition \(V(H)\).

Dually, if there is an ordering of \(M\) for which
\[
(v,d,z_4,z_3,z_2,z_1)
\]
is tight, then a spanning two-cover is obtained by absorbing \(b=p_r\) and the two hole labels into \(Q-c\)'s terminal side while leaving \(P-b\) as the second component.

Equivalently, in the four-label middle-face language of [[genuine_deletion_distance_two_forces_a_fully_protected_four_label_middle_face]], any chamber whose first four variable statuses are all \(1\), or whose last four variable statuses are all \(0\), is already a global two-cover chamber. In the left-anchored case the six variable statuses have form
\[
1111\alpha\beta,
\]
which avoids \(\mathcal W_+=\{001,011,0101\}\) for all \(\alpha,\beta\). The right-anchored case is the reverse-complement statement.

Therefore a genuine deletion-distance-two obstruction must satisfy the simultaneous failure condition:

> no Hamiltonian ordering of the four middle labels extends the inherited left anchor edge \((u,a)\) to a six-vertex tight path, and no Hamiltonian ordering extends the inherited right anchor edge \((v,d)\) through all four middle labels.

This converts the anchored \(S_4\) obstruction into a two-sided fixed-edge extension failure. The remaining local problem is to classify simultaneous failure of these two four-label extensions using the prescribed-endpoint and endpoint-pair Hamiltonicity calculus.
