# Open problem

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_the_remaining_implication_subsection_b
- Parent Section: snake_accounting_and_the_4348_equality_problem_the_remaining_implication
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

For one of the three families in Theorem 10, prove that \(\Omega(S)\) vertex-indexed occurrences cannot be supported by \(o(S)\) distinct global objects with unbounded multiplicity.

A sufficient statement is the following. Assign every selected edge to one of its terminal vertices, and let \(d(w)\) be the number assigned to \(w\). Prove
\[
d(w)\le g(\phi(w))
\qquad\text{with}\qquad
g(p)=o(p). \tag{40}
\]
Then
\[
|E'|\le\sum_wg(\phi(w))=o(S),
\]
because for every \(\varepsilon>0\),
\[
\sum_wg(\phi(w))
\le
\varepsilon S+O_\varepsilon(n_+)
=
\varepsilon S+o(S).
\]
This contradicts (37).

The remaining difficulty is therefore global reuse of the maximum paths, terminal vertices, fundamental-cycle edges, local \(3\)-cycles, and rank-superlevel edges produced above.
