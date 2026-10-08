# Basic properties of the full shadow

## Lemma 1

The coloring (1) is proper. Moreover,
\[
e(G)=3|E(H)| \tag{2}
\]
and, for every vertex \(v\),
\[
d_G(v)=2d_H(v). \tag{3}
\]

#### Proof
If two shadow edges \(xy\) and \(xw\) had the same color \(z\), then the corresponding hyperedges
\[
\{x,y,z\},\qquad \{x,w,z\}
\]
would share the two vertices \(x,z\), contrary to linearity. Thus the coloring is proper.

Every hyperedge contributes its three distinct pairs, and distinct hyperedges share no pair, proving (2).

Every hyperedge through \(v\) contributes exactly the two shadow edges joining \(v\) to its other two vertices. Distinct hyperedges through \(v\) cannot reuse a shadow neighbor, so these \(2d_H(v)\) graph edges are distinct. This proves (3). ∎

The coloring has additional symmetry: if \(c(xy)=z\), then
\[
c(xz)=y,\qquad c(yz)=x. \tag{4}
\]
Thus every hyperedge appears as a triangle whose edge colors are the opposite vertices.
