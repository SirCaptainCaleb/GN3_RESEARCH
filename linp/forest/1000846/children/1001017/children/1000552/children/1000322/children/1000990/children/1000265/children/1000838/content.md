# Exact density forces a potential-deficiency surplus of upward 0-1-1 transitions

## Statement

Let H be a \(P_\ell\)-free linear 3-graph with \(m=dn\), where \(d=\lfloor 2\ell/3\rfloor\). Choose maximum endpoint paths as in the contact-multiplicity snake wherever defined, let \(U\) be the number of unpaid 0-1-1 ascending edges, and define
\[
A_\phi=\sum_{v\in V(H)}((\ell-1)-\phi(v)),\qquad
N_i=|\{v\in V(H):\phi(v)=i\}|\quad(i=0,1).
\]
Then
\[
U\ge \gamma_\ell n+2A_\phi,
\qquad
\gamma_\ell=3d-(2\ell-3),
\]
where \(\gamma_\ell=3,1,2\) according as \(\ell\equiv0,1,2\pmod3\).

Orient every 0-1-1 edge from its unique entrance \(x\) to its two terminals \(y,z\). This produces an acyclic directed two-branch transition system because \(\phi(y),\phi(z)\ge\phi(x)+1\). If \(t_U(v)\) counts transitions for which \(v\) is a terminal, then
\[
t_U(v)\le\max\{0,2\phi(v)-3\},
\]
and hence
\[
2U\le (2\ell-5)n-2A_\phi+N_1+3N_0.
\]
In particular, if \(\phi(v)\ge1\) for every vertex, then
\[
2U\le (2\ell-5)n-2A_\phi+N_1,
\]
and if \(\phi(v)\ge2\) for every vertex, then
\[
2U\le (2\ell-5)n-2A_\phi.
\]

## Body

Let
\[
A_\phi=\sum_{v\in V(H)}((\ell-1)-\phi(v))
\]
and let \(N_i=|\{v:\phi(v)=i\}|\) for \(i=0,1\).

By the clean-minus-double identity and the certified 0-1-1 reduction,
\[
3m\le \sum_v(2\phi(v)-1)+U.
\]
Since \(H\) is \(P_\ell\)-free,
\[
\sum_v(2\phi(v)-1)
=(2\ell-3)n-2A_\phi.
\]
Using \(m=dn\), where \(d=\lfloor 2\ell/3\rfloor\), gives
\[
U\ge [3d-(2\ell-3)]n+2A_\phi
=\gamma_\ell n+2A_\phi.
\]
Thus \(\gamma_\ell\) equals \(3,1,2\) according as \(\ell\equiv0,1,2\pmod 3\).

Now let \(e=\{x,y,z\}\) be a 0-1-1 edge. It is ascending nonspecial, so if \(p=\phi(x)\), then \(\phi(e)=p+1\). Both \(y,z\) are terminal at \(e\), hence
\[
\phi(y),\phi(z)\ge \phi(e)=\phi(x)+1.
\]
Orient two arcs \(x\to y\) and \(x\to z\). Potential strictly increases along every arc, so this directed two-branch system is acyclic.

For a vertex \(v\), let \(t_U(v)\) be the number of 0-1-1 edges for which \(v\) is a terminal. The certified cumulative nonspecial-terminal bound gives
\[
t_U(v)\le \max\{0,2\phi(v)-3\}.
\]
Every 0-1-1 edge contributes exactly two terminal incidences, hence
\[
2U=\sum_v t_U(v)
\le \sum_v\max\{0,2\phi(v)-3\}.
\]
For every nonnegative integer \(r\),
\[
\max\{0,2r-3\}
=(2r-3)+\mathbf 1_{\{r=1\}}+3\mathbf 1_{\{r=0\}}.
\]
Therefore
\[
2U\le 2\sum_v\phi(v)-3n+N_1+3N_0
=(2\ell-5)n-2A_\phi+N_1+3N_0.
\]
If every vertex has positive vertex rank, then \(N_0=0\), giving
\[
2U\le (2\ell-5)n-2A_\phi+N_1.
\]
If every vertex has vertex rank at least two, then also \(N_1=0\), giving
\[
2U\le (2\ell-5)n-2A_\phi.
\]
