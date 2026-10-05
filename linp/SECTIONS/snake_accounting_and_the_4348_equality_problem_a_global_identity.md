# A global identity

## Composition

Define
\[
\beta(1)=0,\quad
\beta(2)=1,\quad
\beta(3)=2,\quad
\beta(4)=2,\quad
\beta(5)=3,\quad
\beta(6)=5,
\]
and
\[
\beta(p)=\left\lfloor\frac{11p-16}{8}\right\rfloor
\qquad(p\ge7). \tag{5}
\]

For each nonisolated \(v\), put \(p_v=\phi(v)\), choose a maximum \(p_v\)-edge path \(P_v\) ending at \(v\), and let \(D_v\) be the number of incident edges with \(\mu_{P_v}(e)=2\). If \(T(v)\ne\varnothing\), let
\[
q(v)=\max\{\phi(e):e\in T(v)\}.
\]

## Lemma 4

For every nonisolated \(v\),
\[
t(v)-D_v\le \beta(p_v). \tag{6}
\]

#### Proof
If \(T(v)=\varnothing\), the assertion is immediate.

Suppose first that \(q(v)=p_v\). Choose \(P_v\) with last edge an ascending edge of rank \(p_v\). Lemma 1, with the double intersections removed, gives
\[
t(v)-D_v
\le
1+\left\lceil\frac{3p_v-8}{4}\right\rceil
=
\left\lceil\frac{3p_v-4}{4}\right\rceil . \tag{7}
\]

Now suppose \(q(v)<p_v\). Corollary 2 gives
\[
t(v)\le \gamma(q(v))\le \gamma(p_v-1). \tag{8}
\]
After the \(D_v\) double intersections are removed, every remaining member of \(T(v)\) has one off-\(v\) intersection with \(P_v\). Lemma 3 gives
\[
t(v)-D_v
\le
\max(0,4q(v)-2p_v-3)
\le
\max(0,2p_v-7). \tag{9}
\]
Thus
\[
t(v)-D_v
\le
\min\{\gamma(p_v-1),\max(0,2p_v-7)\}. \tag{10}
\]
Comparing (7) and (10) with (5), directly for \(p_v\le7\) and by the floor formula for \(p_v\ge8\), gives (6). ∎

Define the local nonnegative quantity
\[
\eta_v=\beta(p_v)-t(v)+D_v. \tag{11}
\]
Let
\[
D=\sum_vD_v,\qquad \eta=\sum_v\eta_v.
\]
Let \(C\) be the number of incidences \((v,e)\) for which \(\mu_{P_v}(e)=0\), and let
\[
R=\sum_v\left(2p_v-1-\sum_{e\ni v}\mu_{P_v}(e)\right). \tag{12}
\]
Linearity gives \(R\ge0\).

Let \(A\) be the number of ascending edges.

## Theorem 5

\[
6|E(H)|
=
\sum_v\bigl(4p_v-2+\beta(p_v)\bigr)
-D-\eta-2(A-C)-2R. \tag{13}
\]

#### Proof
For a fixed \(v\), the path \(P_v\) has \(2p_v-2\) vertices outside its last edge. Distinct incident edges can use each such vertex at most once, so (12) is nonnegative.

Summing the multiplicities \(\mu_{P_v}(e)\) over all incidences, an ordinary incidence contributes \(1\), a zero-intersection incidence contributes \(0\), and a double-intersection incidence contributes \(2\). Hence
\[
3m-C+D=2S-n_+-R. \tag{14}
\]

A zero-intersection incidence can occur only at the unique entrance of an ascending edge; otherwise the incident edge could be appended to the chosen maximum path. Therefore
\[
C\le A. \tag{15}
\]
Every ascending edge has two terminal vertices, so
\[
\sum_v t(v)=2A. \tag{16}
\]
By (11),
\[
\sum_v\beta(p_v)=2A-D+\eta. \tag{17}
\]
Substituting (17) into twice (14) gives (13). ∎

## Corollary 6

If \(H\) is \(P_\ell^{(3)}\)-free and \(\ell\ge8\), then
\[
|E(H)|
\le
\frac{43\ell-75-\rho_\ell}{48}\,n
\le
\frac{43\ell-75}{48}\,n, \tag{18}
\]
where \(0\le\rho_\ell\le7\) is determined by
\[
\left\lfloor\frac{11\ell-27}{8}\right\rfloor
=
\frac{11\ell-27-\rho_\ell}{8}.
\]

#### Proof
If \(H\) is \(P_\ell^{(3)}\)-free, then \(p_v\le\ell-1\). The function
\[
4p-2+\beta(p)
\]
is increasing. Discard the four nonnegative terms subtracted in (13) and substitute \(p_v\le\ell-1\). ∎

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_a_global_identity
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_a.md) (`snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 4](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_b.md) (`snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_b`; development v1; composition v1; stale=False)
- [Subsection 3 — Theorem 5](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_c.md) (`snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_c`; development v1; composition v1; stale=False)
- [Subsection 4 — Corollary 6](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_d.md) (`snake_accounting_and_the_4348_equality_problem_a_global_identity_subsection_d`; development v1; composition vNone; stale=False)
