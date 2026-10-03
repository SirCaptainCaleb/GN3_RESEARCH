# Nullity and terminal-pair complexity

## Body

The rank problem also receives information from the terminal-pair graph of nonspecial edges.

Let \(T\) be that graph, let \(h\) be the number of distinct unique entrances of nonspecial edges, and let \(s\) be the number of special edges.

## Proposition 6

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

## Metadata

- ID: incidence_rank_and_induced_paths_in_the_intersection_graph_nullity_and_terminal_pair_complexity
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 1: (untitled)
- Subsection 2 — HOT, version 1: Proposition 6
