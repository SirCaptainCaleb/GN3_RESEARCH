# Imbalanced minimum-hole complements force dense endpoint-spanning four-supports — preserved pre-item development

## Development

## Imbalanced minimum-hole complements force dense endpoint-spanning four-supports

Let
\[
X\subseteq V(H),\qquad |X|=\kappa_2(H),
\]
be a minimum two-cover deletion set. Among all two-covers of \(H-X\), choose
\[
P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t),
\]
minimizing
\[
\Psi=s^2+t^2,
\]
and assume
\[
2\le s\le t,\qquad t\ge s+2.
\]

### Imbalance forces endpoint reversers

Fix \(q\in\{q_1,q_t\}\). If \(P\cup\{q\}\) were Hamiltonian, deleting the corresponding endpoint from the displayed path \(Q\) would leave a tight path, and we would obtain a two-cover of \(H-X\) with component orders
\[
s+1,\qquad t-1.
\]
Its potential changes by
\[
(s+1)^2+(t-1)^2-(s^2+t^2)
=2(s-t+1)\le-2,
\]
contradicting the choice of \(P\mid Q\).

Thus neither endpoint of \(Q\) can be attached to either displayed end of \(P\). Boundary antisymmetry gives
\[
h(p_2,p_1,q)=1,
\qquad
h(q,p_s,p_{s-1})=1
\qquad(q\in\{q_1,q_t\}).
\]

Every hole vertex \(x\in X\) satisfies the same two relations by minimum-hole four-end synchronization. Hence
\[
R:=X\cup\{q_1,q_t\}
\]
is a common two-ended reverser reservoir for \(P\):
\[
h(p_2,p_1,r)=h(r,p_s,p_{s-1})=1
\qquad(r\in R).
\]

This generalizes the frozen-complement imbalance lemma from marked three-covers: no minimum-counterexample assumption is needed here, only \(\Psi\)-minimality of the two-cover of \(H-X\).

### Fixed-pair elevation across the short path

Now use the opposite endpoints
\[
\{p_1,p_s\}
\]
as the fixed pair. Partition \(R\) by
\[
R_+=\{r:h(p_1,r,p_s)=1\},
\qquad
R_-=\{r:h(p_s,r,p_1)=1\}.
\]

By the fixed-pair bad-extension theorem in [[extremal01]], any two labels \(u,v\) in the same class give a Hamiltonian four-set
\[
\boxed{\{p_1,p_s,u,v\}\text{ is Hamiltonian}.}
\]

Therefore one of \(R_+,R_-\) has order at least
\[
\left\lceil\frac{|X|+2}{2}\right\rceil,
\]
and the imbalanced minimum-hole cover carries at least
\[
\binom{|R_+|}{2}+\binom{|R_-|}{2}
\]
Hamiltonian four-supports containing **both endpoints of the short component**.

### Strategic consequence

A minimum deletion hole therefore has a sharp dichotomy after minimizing the imbalance of its surviving two-cover:

1. the two surviving path orders differ by at most one; or
2. the shorter path has a reservoir of \(|X|+2\) labels reversing both of its displayed ends, and a quadratic-density family of Hamiltonian four-supports spanning its two endpoints.

In particular, an attempt to force a balanced minimum hole need not attack arbitrary imbalance. Large imbalance automatically creates the exact bounded endpoint structures used by the Article III–V transport and disagreement machinery.

This suggests an earlier replacement for part of the exact-root zero-hole problem: minimize \(\Psi\) inside a minimum deletion complement first, then either obtain near-balance immediately or enter a dense bounded-support regime around the shorter path.
