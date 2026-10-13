# Article XIII — Rainbow Paths with a Color-Preserving Involution

## Color-preserving involutions and one-switch rainbow paths

### The color-preserving involution conjecture

Let \(G=(V,E)\) be a finite connected simple undirected graph. Let
\[
\lambda:E\to\mathcal C
\]
be an arbitrary ordinary edge coloring, and let
\[
\chi:E\to\{0,1\}
\]
be an independent binary edge labeling.

Suppose \(\tau:V\to V\) is an involutive graph automorphism (\(\tau^2=\mathrm{id}\)) satisfying, for every undirected edge \(e=\{u,v\}\),
\[
\boxed{
\lambda(\{\tau u,\tau v\})=\lambda(\{u,v\}),\qquad
\chi(\{\tau u,\tau v\})=1-\chi(\{u,v\}).
}
\tag{1}
\]
Thus the vertex involution **preserves ordinary edge colors** and **reverses binary edge labels**. These are both mandatory hypotheses.

Write
\[
\hat\delta(G,\lambda)
=\min_{v\in V}|\{\lambda(e):e\ni v\}|.
\]

**Conjecture XIII.1 (color-preserving involutive rainbow path).**
Every such instance admits a vertex-simple path \(P\) of at least \(\hat\delta(G,\lambda)\) **edges**, whose ordinary edge colors are pairwise distinct, and whose sequence of binary edge labels changes value **at most once**.

Equivalently, if the consecutive edges of \(P\) are \(e_1,\ldots,e_m\), then
\[
\boxed{
m\ge\hat\delta(G,\lambda),\quad
\lambda(e_i)\ne\lambda(e_j)\ (i\ne j),\quad
\sum_{i=1}^{m-1}\mathbf1_{\{\chi(e_i)\ne\chi(e_{i+1})\}}\le1.
}
\tag{2}
\]

**Status: open for investigation.** No additional assumptions on the ordinary edge coloring are made (in particular, it need not be proper). The involution acts on vertices, not merely on abstract edge pairs. It need not be fixed-point-free on vertices, but (1) prevents any edge from being fixed. A result for an involution that fails to preserve \(\lambda\) does not refute this revised conjecture.

The research objective is to prove (2), construct counterexamples satisfying **both** identities in (1), or determine sharp bounds and mathematically natural additional hypotheses if (2) fails.
