# Lemma 3

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_path_relative_terminal_bounds_subsection_b
- Parent Section: snake_accounting_and_the_4348_equality_problem_path_relative_terminal_bounds
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

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
