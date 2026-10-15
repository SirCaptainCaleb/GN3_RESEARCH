# Cube antipodal-edge stabilizers and symmetric middle-layer paths

### Stabilizer cycle criterion for cube edges and the balanced-layer geodesic

Let \(n\ge2\), let \(E_n\) be the set of undirected edges of the binary cube \(Q_n\), and let \(R\) complement both endpoints of an edge. The permutation group \(S_n\) acts on \(E_n\) by permuting directions and vertex entries, commuting with \(R\).

**Theorem 1 (antipodal-edge cycle criterion).** For a permutation \(g\in S_n\), there exists an edge \(e\in E_n\) with \(ge=Re\) if and only if \(g\) has precisely one fixed symbol \(i\), and every other cycle of \(g\) has even length. Furthermore \(g\) fixes some edge of \(Q_n\) if and only if it fixes at least one direction.

*Proof.* Represent an undirected edge by its direction \(i\) and a bit assignment to the \(n-1\) other directions. If \(ge=Re\), the direction is unchanged, so \(g(i)=i\). On every other direction \(j\), the bit assignment must satisfy
\[
x_{g^{-1}j}=1-x_j.
\tag{1}
\]
Going once around a cycle of \(g\) shows its length must be even. Conversely, on every even cycle, alternating zeros and ones satisfies (1), yielding such an edge. Every other fixed direction would be an odd length-one cycle, so \(i\) is unique. For the second assertion, an edge fixed by \(g\) must have its direction fixed; conversely the edge from \(0^n\) in any fixed direction is fixed. QED.

**Theorem 2 (complete permutation-equivariance test).** Let \(G\le S_n\) and \(\chi:G\to\mathbb F_2\) be a homomorphism. There is an antipodally odd edge coloring \(c:E_n\to\mathbb F_2\) satisfying \(c(ge)=c(e)+\chi(g)\) for all \(g,e\) if and only if:
(i) \(\chi(g)=0\) for every \(g\in G\) fixing any direction; and
(ii) \(G\) contains no permutation having a unique fixed direction and only even cycles otherwise.

*Proof.* By Theorem 1, condition (i) is precisely the fixed-edge constraint of the universal twisted-color stabilizer criterion in the preceding Subsection. Condition (ii) rules out a permutation carrying some edge to its antipodal edge, because (i) would force its twist to be zero while reversal oddness would force its twist to be one. The universal criterion gives sufficiency as well. QED.

**Corollary 3 (fully symmetric cube colorings).** A color-preserving antipodally odd cube-edge coloring invariant under all direction permutations \(S_n\) exists if and only if \(n\) is even.

*Proof.* When \(n\) is even, the set of \(n-1\) directions outside a fixed direction has odd cardinality; it cannot be partitioned into exclusively even cycles. Theorem 2 applies to \(G=S_n,\chi=0\). Explicitly, for an edge in direction \(i\), let \(k\) be the number of ones on the other \(n-1\) directions and put \(c(e)=h(k)\), where the arbitrary function \(h:\{0,\ldots,n-1\}\to\mathbb F_2\) satisfies \(h(n-1-k)=1-h(k)\). Such an \(h\) exists because \(n-1\) is odd. If \(n\) is odd, a permutation fixing one direction and exchanging all other directions in pairs violates Theorem 2. QED.

**Theorem 4 (dimension-simple monochromatic geodesic in every fully symmetric odd coloring).** Suppose \(n=2m\) and \(c\) is any \(S_n\)-invariant antipodally odd cube-edge coloring. Then it admits an antipodal geodesic using every direction once whose \(n\) edges all have the same color.

*Proof.* By symmetry the color of an edge joining vertices of Hamming weights \(k\) and \(k+1\) depends only on \(k\); call it \(h(k)\). Choose a root vertex with precisely \(m\) ones. Alternate toggling a previously unused one-direction and a previously unused zero-direction, until all \(2m\) directions have been used. Each pair of steps changes the Hamming weight from \(m\) to \(m-1\) and back to \(m\), so *every edge lies between the same two middle weight levels*. Every edge therefore has color \(h(m-1)\). All directions are distinct, and the last vertex is the complement of the root. QED.

**Comparison with reversal-odd boundary triples.** Every transposition of two symbols fixes a third when \(n\ge3\) and consequently sends a suitable triple to its reversal, so no \(S_n\)-invariant reversal-odd triple coloring exists. In even dimension the cube permits the full \(S_n\) symmetry and its full-dimensional monochromatic geodesic follows from the middle-layer alternation. Thus the stabilizer condition supplies a sharp common framework for the two coloring classes while exposing a structural difference between their permissible symmetries.
