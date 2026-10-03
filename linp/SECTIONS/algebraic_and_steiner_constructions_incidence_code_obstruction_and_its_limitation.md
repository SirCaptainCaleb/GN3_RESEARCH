# Incidence-code obstruction and its limitation

## Body

Let \(M_H\) be the vertex-edge incidence matrix of a linear \(3\)-graph over \(\mathbb F_2\).

## Lemma 7

If \(H\) contains a linear path with \(\ell\) edges, then the binary column span of \(M_H\) contains a vector of Hamming weight \(\ell+2\).

#### Proof
Sum the incidence vectors of the \(\ell\) path edges. Every joint occurs twice and cancels. The remaining vertices are the two endpoints and the \(\ell\) private vertices, altogether \(\ell+2\) coordinates. ∎

Thus absence of weight \(\ell+2\) is a sufficient condition for \(P_\ell^{(3)}\)-freeness. It cannot, however, prove a density above \(\ell/3\).

## Theorem 8

If
\[
\frac{|E(H)|}{|V(H)|}>\frac{\ell}{3},
\]
then the binary incidence code of \(H\) contains a word of weight \(\ell+2\).

#### Proof
Pass to the \(>\ell/3\)-core. It is nonempty, has the same or larger density, and has minimum degree greater than \(\ell/3\). Its average degree exceeds \(\ell\), so some vertex \(v\) has degree at least \(\ell+1\). The edges through \(v\) form a linear star, whose \(2d\) vertices outside \(v\) are all distinct.

The sum of \(k\) star edges has weight \(2k\) when \(k\) is even and \(2k+1\) when \(k\) is odd.

If \(\ell\equiv2\pmod4\), take \(k=(\ell+2)/2\). If \(\ell\equiv1\pmod4\), take \(k=(\ell+1)/2\). These give the required weight directly.

If \(\ell\equiv0\pmod4\), choose an edge \(f\) not containing \(v\). It meets at most three star edges. Choose
\[
k=\frac{\ell-2}{2}
\]
star edges disjoint from \(f\); their sum has weight \(\ell-1\), and adding \(f\) gives weight \(\ell+2\).

If \(\ell\equiv3\pmod4\), choose a star edge \(e=\{v,a,b\}\) and another edge \(f\ne e\) through \(a\). Choose
\[
k-1=\frac{\ell-1}{2}
\]
further star edges disjoint from \(f\). The sum of these \(k\) star edges has weight \(\ell+1\), and adding \(f\), which meets the support exactly in \(a\), changes the weight to \(\ell+2\). ∎

Therefore a code construction must use more information than the absence of one support size.

## Metadata

- ID: algebraic_and_steiner_constructions_incidence_code_obstruction_and_its_limitation
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 1: (untitled)
- Subsection 2 — crystallized, version 1: Lemma 7
- Subsection 3 — HOT, version 1: Theorem 8
