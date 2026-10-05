# Minimum holes contain bidirectionally compatible four-support pair cores

## Metadata

- ID: minimum_holes_contain_bidirectionally_compatible_four_support_pair_cores
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 20
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

### Bidirectional four-support pair cores

For a minimum deletion set \(X\) and \(H-X=P\mid Q\), assign to each \(x\in X\) the two orientation bits
\[
\theta_L(x)=h(p_1,x,q_1),\qquad
\theta_R(x)=h(p_s,x,q_t).
\]
Two vertices \(x,y\) with the same signature give Hamiltonian four-supports
\[
\{p_1,q_1,x,y\}
\quad\text{and}\quad
\{p_s,q_t,x,y\}.
\]
For
\[
G_{x,y}=H-(X\setminus\{x,y\}),
\]
minimum-hole heredity gives \(\kappa_2(G_{x,y})=2\), and the two four-supports yield spanning three-covers rooted at opposite boundaries. Since there are at most four signatures, a minimum hole contains a quadratically dense family of such bidirectionally compatible two-deletion pair cores.

## Development

## Two-end fixed-pair elevation: many hole pairs are simultaneously compatible at both boundaries

Let
\[
X\subseteq V(H)
\]
be a minimum two-cover deletion hole and
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t).
\]

For each \(x\in X\), record two fixed-pair orientation bits:
\[
\theta_L(x)=h(p_1,x,q_1),
\qquad
\theta_R(x)=h(p_s,x,q_t).
\]
Boundary antisymmetry makes each bit binary.

Thus \(X\) is partitioned into at most four signature classes
\[
X_{\alpha,\beta}
=
\{x\in X:\theta_L(x)=\alpha,\ \theta_R(x)=\beta\},
\qquad
(\alpha,\beta)\in\{0,1\}^2.
\]

Take two distinct vertices \(x,y\) in the same signature class. Apply the fixed-pair bad-extension theorem from [[extremal01]] first to the pair \(\{p_1,q_1\}\). Since \(x,y\) have the same orientation through that pair,
\[
\{p_1,q_1,x,y\}
\]
is Hamiltonian.

Apply the same theorem to the terminal pair \(\{p_s,q_t\}\). Since \(x,y\) also have the same terminal signature,
\[
\{p_s,q_t,x,y\}
\]
is Hamiltonian.

Therefore every same-signature pair produces **two compatible Hamiltonian four-supports**, one at each end of the same base two-cover.

If
\[
G_{x,y}=H-(X-\{x,y\}),
\]
then minimality of \(X\) gives
\[
\kappa_2(G_{x,y})=2.
\]
Moreover \(G_{x,y}\) has both spanning three-covers
\[
\{p_1,q_1,x,y\}
\mid
(p_2,\ldots,p_s)
\mid
(q_2,\ldots,q_t)
\]
and
\[
\{p_s,q_t,x,y\}
\mid
(p_1,\ldots,p_{s-1})
\mid
(q_1,\ldots,q_{t-1}).
\]

Hence:

> **Bidirectional four-support core theorem.** Every pair of hole vertices with the same two-end signature yields a genuine \(\kappa_2=2\) induced core carrying Hamiltonian four-support three-covers at both opposite boundaries.

### Density

There are at most four signatures, so one class has order at least
\[
\left\lceil |X|/4\right\rceil.
\]
Consequently the hole contains at least
\[
\sum_{\alpha,\beta}\binom{|X_{\alpha,\beta}|}{2}
\ge
4\binom{\lfloor |X|/4\rfloor}{2}
\]
up to the usual balancing remainder, and in particular quadratically many, bidirectionally compatible pair cores.

In the symmetric zero-root case
\[
|P|=|Q|=s+1,
\]
both three-covers have profile
\[
\boxed{4\mid s\mid s}.
\]

### Further elevation

One may record orientations through more endpoint pairs. For the four exposed endpoints
\[
E=\{p_1,p_s,q_1,q_t\},
\]
there are six fixed unordered pairs. Assigning all six orientation bits partitions \(X\) into at most \(2^6=64\) full endpoint-signature classes. Any two vertices in one full class make
\[
\{a,b,x,y\}
\]
Hamiltonian for **every** pair \(\{a,b\}\subseteq E\).

Thus sufficiently large minimum holes contain pairs which are simultaneously compatible with every two-end interface of the displayed cover. This stronger 64-class form is available when a later gluing argument needs mixed or same-path endpoint pairs.
