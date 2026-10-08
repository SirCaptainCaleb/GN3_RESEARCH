# Nullity and terminal-pair complexity

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
