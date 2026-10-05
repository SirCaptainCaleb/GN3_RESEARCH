# Corollary 2

## Metadata

- ID: terminal_pair_cycles_and_rotations_the_special_edge_inequality_subsection_c
- Parent Section: terminal_pair_cycles_and_rotations_the_special_edge_inequality
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

\[
2m+s\le \sum_v(2\phi(v)-1)\le (2\ell-3)n. \tag{2}
\]

#### Proof
Summing (1), every special edge contributes \(3\) and every nonspecial edge contributes \(2\). Since there are \(s\) special edges,
\[
\sum_v d^-_{\mathrm{snake}}(v)=3s+2(m-s)=2m+s.
\]
The second inequality follows from \(\phi(v)\le\ell-1\). ∎

Thus any lower bound on \(s\) immediately improves the general coefficient.
