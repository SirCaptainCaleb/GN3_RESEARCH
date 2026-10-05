# Proposition 6

## Metadata

- ID: incidence_rank_and_induced_paths_in_the_intersection_graph_nullity_and_terminal_pair_complexity_subsection_b
- Parent Section: incidence_rank_and_induced_paths_in_the_intersection_graph_nullity_and_terminal_pair_complexity
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: True

## Cold composition

(none yet)

## Development

\[
\operatorname{nullity}(N)\le \beta(T)+h+s. \tag{11}
\]

#### Proof
For the nonspecial columns, write
\[
N_{\mathrm{ns}}=B+R
\]
as follows: \(B\) is the ordinary \(0/1\) incidence matrix of \(T\), and the column of \(R\) corresponding to a nonspecial edge is the standard basis vector indexed by its unique entrance. Since \(R\) is supported on \(h\) rows,
\[
\operatorname{rank}R\le h.
\]
Hence
\[
\operatorname{rank}N_{\mathrm{ns}}
\ge
\operatorname{rank}B-h.
\]
The real \(0/1\) incidence matrix of a graph has nullity at most its cycle rank, so
\[
\operatorname{nullity}(N_{\mathrm{ns}})\le \beta(T)+h.
\]
Adding the \(s\) special columns can increase nullity by at most \(s\). ∎

Thus a bound on \(\beta(T)+h\) would also yield a rank theorem.
