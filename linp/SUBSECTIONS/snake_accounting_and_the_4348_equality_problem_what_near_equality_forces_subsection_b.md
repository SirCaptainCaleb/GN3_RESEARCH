# Lemma 7

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_what_near_equality_forces_subsection_b
- Parent Section: snake_accounting_and_the_4348_equality_problem_what_near_equality_forces
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

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
