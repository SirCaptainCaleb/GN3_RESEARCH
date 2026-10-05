# What near equality forces

## Cold composition

Assume now that
\[
|E(H)|=\left(\frac{43}{48}-o(1)\right)S,
\qquad
\frac{S}{n_+}\to\infty. \tag{19}
\]
Since
\[
\sum_v(4p_v-2+\beta(p_v))
\le
\frac{43}{8}S+O(n_+),
\]
Theorem 5 implies
\[
D=o(S),\qquad
\eta=o(S),\qquad
A-C=o(S),\qquad
R=o(S). \tag{20}
\]

If \(q(v)=p_v=p\ge8\), then (7) gives
\[
\eta_v
\ge
\beta(p)-\left\lceil\frac{3p-4}{4}\right\rceil
\ge
\frac{5p-24}{8}. \tag{21}
\]
Thus the vertices satisfying \(q(v)=p_v\) have total vertex rank \(o(S)\).

The remaining high-rank vertices have \(q(v)<p_v\). Fix one, write
\[
p=p_v,\qquad q=q(v),
\]
choose \(e_0\in T(v)\) of edge rank \(q\), choose a maximum \(q\)-edge path \(Q\) ending in \(e_0\) at \(v\), and retain the chosen maximum \(p\)-edge path \(P=P_v\).

## Lemma 7

There is a family \(F_v\subseteq T(v)\) of edges that meet \(Q\) in both vertices outside \(v\) and meet \(P\) in exactly one vertex outside \(v\), with
\[
|F_v|
\ge
\beta(p)-\eta_v
-\left\lceil\frac{3q-4}{4}\right\rceil. \tag{22}
\]
In particular,
\[
|F_v|\ge \frac58p-\eta_v-O(1). \tag{23}
\]

#### Proof
Applied to the \(q\)-edge path \(Q\), the singleton part of Lemma 1 shows that at most
\[
\left\lceil\frac{3q-4}{4}\right\rceil
\]
members of \(T(v)\) fail to have both off-\(v\) vertices on \(Q\). Hence at least
\[
t(v)-\left\lceil\frac{3q-4}{4}\right\rceil
\]
have both.

Among these, at most \(D_v\) have two off-\(v\) vertices on \(P\). Removing them leaves at least
\[
t(v)-D_v-\left\lceil\frac{3q-4}{4}\right\rceil
=
\beta(p)-\eta_v-\left\lceil\frac{3q-4}{4}\right\rceil,
\]
which proves (22). Since \(q\le p-1\), (5) gives (23). ∎

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_what_near_equality_forces
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_what_near_equality_forces_subsection_a.md) (\`snake_accounting_and_the_4348_equality_problem_what_near_equality_forces_subsection_a\`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 7](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_what_near_equality_forces_subsection_b.md) (\`snake_accounting_and_the_4348_equality_problem_what_near_equality_forces_subsection_b\`; development v1; composition vNone; stale=True)
