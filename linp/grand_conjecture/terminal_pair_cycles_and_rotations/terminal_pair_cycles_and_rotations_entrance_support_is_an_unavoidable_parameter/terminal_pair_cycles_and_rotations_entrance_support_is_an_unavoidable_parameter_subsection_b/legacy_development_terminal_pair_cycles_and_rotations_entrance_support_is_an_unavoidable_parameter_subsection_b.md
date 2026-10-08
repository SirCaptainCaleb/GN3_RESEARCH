# Proposition 7 — preserved pre-item development

## Composition

(none yet)

## Development

\[
\operatorname{nullity}(N_{\mathrm{ns}})\le \beta(T)+h. \tag{5}
\]
For the full incidence matrix \(N\),
\[
\operatorname{nullity}(N)\le \beta(T)+h+s. \tag{6}
\]

#### Proof
For a nonspecial edge \(e\) with unique entrance \(x_e\) and terminal pair \(u_ev_e\), write its incidence column as
\[
\mathbf 1_{u_e}+\mathbf 1_{v_e}+\mathbf 1_{x_e}.
\]
Let \(B\) be the ordinary \(0/1\) vertex-edge incidence matrix of \(T\), with zero rows added for vertices outside \(V(T)\), and let \(R\) be the matrix whose \(e\)-column is \(\mathbf 1_{x_e}\). Then
\[
N_{\mathrm{ns}}=B+R.
\]
Since \(R\) is supported on \(h\) rows,
\[
\operatorname{rank}(R)\le h.
\]
The inequality
\[
\operatorname{rank}(B+R)\ge\operatorname{rank}(B)-\operatorname{rank}(R)
\]
gives
\[
\operatorname{nullity}(N_{\mathrm{ns}})
\le |E(T)|-\operatorname{rank}(B)+h.
\]

For a graph with \(v\) vertices, \(b\) edges, and \(c_{\mathrm{bip}}\) bipartite components, the real \(0/1\) incidence matrix has rank \(v-c_{\mathrm{bip}}\). Hence
\[
b-\operatorname{rank}(B)
=
b-v+c_{\mathrm{bip}}
\le
b-v+\kappa(T)
=
\beta(T).
\]
This proves (5). Adding \(s\) special columns can increase nullity by at most \(s\), proving (6). ∎

Thus the natural global quantity is \(\beta(T)+h\), not \(\beta(T)\) alone.
