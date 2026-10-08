# Minimum-hole singleton restorations have opposite-boundary four-supports — preserved pre-item development

## Development

## Singleton restorations have opposite-boundary four-supports

Let \(X\) be a minimum two-cover deletion set and fix
\[
H-X=P\mid Q,\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t),
\]
with \(s,t\ge2\). For \(x\in X\), minimum-hole synchronization gives
\[
h(x,p_s,p_{s-1})=h(x,q_t,q_{t-1})=1
\]
and
\[
h(p_2,p_1,x)=h(q_2,q_1,x)=1.
\]

At the terminal boundary, boundary antisymmetry makes exactly one of
\[
h(p_s,x,q_t),\qquad h(q_t,x,p_s)
\]
equal to one. In the first case
\[
(p_s,x,q_t,q_{t-1})
\]
is a tight four-path; in the second case
\[
(q_t,x,p_s,p_{s-1})
\]
is a tight four-path. Hence the singleton restoration
\[
G_x=H-(X\setminus\{x\})
\]
has a spanning three-cover of one of the forms
\[
(p_s,x,q_t,q_{t-1})\mid(p_1,\ldots,p_{s-1})\mid(q_1,\ldots,q_{t-2})
\]
or
\[
(q_t,x,p_s,p_{s-1})\mid(q_1,\ldots,q_{t-1})\mid(p_1,\ldots,p_{s-2}).
\]

The initial boundary is symmetric. Exactly one of
\[
h(p_1,x,q_1),\qquad h(q_1,x,p_1)
\]
equals one, giving respectively the tight four-path
\[
(p_2,p_1,x,q_1)
\]
or
\[
(q_2,q_1,x,p_1),
\]
and therefore a second spanning three-cover of \(G_x\), now rooted at the opposite boundary.

By minimum-hole heredity, \(\kappa_2(G_x)=1\). Thus every one-label restoration of a minimum hole carries explicit Hamiltonian four-supports at both opposite boundaries, with the restored label on both supports.

For a two-element residual hole \(\{x,y\}\), define
\[
\tau_I(z)=h(p_1,z,q_1),\qquad
\tau_T(z)=h(p_s,z,q_t).
\]
The rooted four-support behavior of \(x,y\) at the two corresponding endpoint pairs has only four relative types
\[
(\tau_I(x)\oplus\tau_I(y),\,\tau_T(x)\oplus\tau_T(y))\in\{0,1\}^2.
\]
When the corresponding bit is zero, the fixed-pair theorem gives a Hamiltonian four-support on that endpoint pair together with \(x,y\). When it is one, the two singleton four-supports cross that boundary in opposite orientations. This reduces the exposed endpoint part of every genuine two-deletion state to a four-type interface; no path reversal is used.
