# Genuine minimum pairs enter maximal support or are doubly endpoint-bad — preserved pre-item development

## Composition

(none yet)

## Development

## A genuine minimum pair either enters maximal-support normalization or is doubly endpoint-bad

Let
\[
X=\{x,y\}
\]
be a minimum two-cover deletion pair and fix
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t),
\]
with \(s,t\ge2\).

Define the two endpoint four-sets
\[
K_I=\{p_1,q_1,x,y\},\qquad
K_T=\{p_s,q_t,x,y\}.
\]

If \(K_I\) is Hamiltonian, then
\[
H-K_I
\]
is covered by the inherited tight paths
\[
(p_2,\ldots,p_s)\mid(q_2,\ldots,q_t).
\]
Thus \(K_I\) is a proper Hamiltonian support with two-coverable complement. The same statement holds for \(K_T\), whose complement is
\[
(p_1,\ldots,p_{s-1})\mid(q_1,\ldots,q_{t-1}).
\]

Hence if either endpoint four-set is Hamiltonian, the hypotheses of [[maximal_support_normalization_applies_directly_to_article_vii_bounded_outputs]] hold, and the genuine two-deletion state enters the maximal-support/sandwich normalization.

Suppose therefore that both
\[
H[K_I],\qquad H[K_T]
\]
are non-Hamiltonian.

For the initial pair \(\{p_1,q_1\}\), put
\[
\tau_I(z)=h(p_1,z,q_1),\qquad z\in\{x,y\}.
\]
If \(\tau_I(x)=\tau_I(y)\), the fixed-pair Hamiltonicity theorem makes \(K_I\) Hamiltonian, contradiction. Therefore
\[
\boxed{\tau_I(x)\ne\tau_I(y).}
\]

Likewise, with
\[
\tau_T(z)=h(p_s,z,q_t),
\]
non-Hamiltonicity of \(K_T\) forces
\[
\boxed{\tau_T(x)\ne\tau_T(y).}
\]

Thus:

> **Endpoint-four-set dichotomy.** Every genuine minimum deletion pair either has a Hamiltonian endpoint four-support with two-coverable complement and hence enters maximal-support normalization, or both endpoint four-sets are non-Hamiltonian and the two holes have complementary fixed-pair signatures at both opposite boundaries.

The second branch is the exact residue not covered by same-signature root advance. It is stronger than merely saying the signatures differ: the two corresponding cross-class four-extensions are themselves bad. Any future local closure theorem need only treat this **doubly endpoint-bad antipodal-signature pair**.

In particular, same-signature and accidentally-Hamiltonian opposite-signature pairs are no longer part of the genuine six-label routing frontier.
