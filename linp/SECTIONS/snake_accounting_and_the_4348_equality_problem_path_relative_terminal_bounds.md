# Path-relative terminal bounds

## Composition

For a maximum \(p\)-edge path \(P\) ending at \(v\), and an incident edge \(f\ne g_p\), let
\[
\mu_P(f)=|(f\setminus\{v\})\cap(V(P)\setminus g_p)|.
\]
Assign \(\mu_P(g_p)=1\).

The following path-local estimate will be used in the count.

## Lemma 3

Let \(P\) be a \(p\)-edge path ending at \(v\), and let \(F_Q\) be a family of ascending edges \(e=\{x,u,v\}\) at which \(v\) is terminal and
\[
\phi(e)\le Q,\qquad
\left\lceil\frac{p+2}{2}\right\rceil\le Q\le p.
\]
If every member of \(F_Q\) has \(\mu_P(e)=1\), then
\[
|F_Q|\le 4Q-2p-3. \tag{4}
\]

The proof is a path-splice count. For \(e=\{x,u,v\}\), both \(x\) and \(u\) must occur in the final \(Q-1\) edges of any maximum \(p\)-edge path ending at \(v\), unless the edge has a second intersection with the path. Under \(\mu_P(e)=1\), the unique intersection therefore lies in the overlap of the two terminal intervals obtained from the entrance side and the opposite-terminal side. This overlap contains \(4Q-2p-3\) admissible vertices. Distinct members of \(F_Q\) use distinct admissible vertices by linearity, proving (4).

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_path_relative_terminal_bounds
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False
- Subsections existing when composed: 2
- Subsections now: 2

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_path_relative_terminal_bounds_subsection_a.md) (`snake_accounting_and_the_4348_equality_problem_path_relative_terminal_bounds_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 3](../SUBSECTIONS/snake_accounting_and_the_4348_equality_problem_path_relative_terminal_bounds_subsection_b.md) (`snake_accounting_and_the_4348_equality_problem_path_relative_terminal_bounds_subsection_b`; development v1; composition vNone; stale=False)
