# Minimum holes contain a dense family of four-support two-deletion cores — preserved pre-item development

## Development

## Fixed-pair elevation: every minimum hole has a dense family of four-support two-deletion cores

Let
\[
X\subseteq V(H),\qquad |X|=k=\kappa_2(H)\ge2,
\]
be a minimum two-cover deletion set and write
\[
H-X=P\mid Q,
\qquad
P=(p_1,p_2,\ldots),\quad Q=(q_1,q_2,\ldots),
\]
with the exposed hole-facing endpoints \(p_1,q_1\).

Partition the hole by the fixed-pair orientation through \(p_1,q_1\):
\[
X_+=\{x\in X:h(p_1,x,q_1)=1\},
\qquad
X_-=\{x\in X:h(q_1,x,p_1)=1\}.
\]
Boundary antisymmetry gives
\[
X=X_+\sqcup X_-.
\]

Apply the fixed-pair bad-extension theorem from [[extremal01]] with fixed pair
\[
\{p_1,q_1\}.
\]
Its bad-pair graph is bipartite between \(X_+\) and \(X_-\). Therefore if
\[
x,y\in X_+
\quad\text{or}\quad
x,y\in X_-,
\]
then
\[
K_{x,y}=\{p_1,q_1,x,y\}
\]
is Hamiltonian.

Now retain such a same-class pair and put
\[
G_{x,y}=H-(X-\{x,y\}).
\]
Minimality of \(X\) gives
\[
\boxed{\kappa_2(G_{x,y})=2},
\]
since deleting \(x,y\) leaves \(P\mid Q\), while a one-deletion two-cover of \(G_{x,y}\) would give a \((k-1)\)-deletion two-cover of \(H\).

At the same time
\[
K_{x,y}
\ \mid\
(p_2,p_3,\ldots)
\ \mid\
(q_2,q_3,\ldots)
\]
is a spanning three-cover of \(G_{x,y}\), omitting empty tails.

Hence:

> **Fixed-pair core theorem.** Every same-orientation pair of vertices in a minimum deletion hole produces an induced genuine \(\kappa_2=2\) core with a Hamiltonian four-component and the two inherited shortened tails.

If the original deletion cover is symmetric,
\[
|P|=|Q|=s+1,
\]
then every such core has the exact profile
\[
\boxed{4\mid s\mid s}.
\]

### Density

If
\[
a=|X_+|,\qquad b=|X_-|,\qquad a+b=k,
\]
the number of same-class pairs is
\[
\binom a2+\binom b2
=
\binom k2-ab
\ge
\binom k2-\left\lfloor\frac{k^2}{4}\right\rfloor.
\]
Thus a minimum hole of order \(k\) contains quadratically many pair cores of the \(4\mid s\mid s\) type; in particular one orientation class has size at least \(\lceil k/2\rceil\).

This is stronger and cleaner than choosing an arbitrary root-advance pair: the four-support uses only the two exposed path endpoints and two hole labels, and the two residual path components remain completely untouched except for removal of their first vertices.

### Strategic consequence

The high-hole zero-root branch now supplies two complementary canonical reductions:

1. every three hole labels give a \(\kappa_2=3,\operatorname{pc}=3\) core by finite root advance;
2. every same-orientation hole pair gives a \(\kappa_2=2\) core with profile \(4\mid s\mid s\).

The second form is especially well matched to the established “four-path beside a long path” descent/repartition lemmas. Thus a promising attack on a symmetric zero-root hole is to study the **family of overlapping \(4\mid s\mid s\) two-deletion cores indexed by the two orientation classes**, rather than one reflected-double packet at a time.
