# Protected rank-three coherence from terminal block compression

## Composition

(none yet)

## Development

## Protected rank-three coherence closes once the terminal block bound is used

The audit gap between existential and protected carriers can be reduced further. The key point is that the protected terminal classification already claims that the unique face block coupling the two reflected determining windows has order at most four. Hence, after factoring off disjoint exterior face blocks, the only genuinely non-product Coxeter residue that can contain terminal sign-flip surgery has rank at most three.

The rank-three residue is also controllable.

Let the terminal determining span be the contiguous positional interval \(I\), with \(|I|\le 10\), and let \(R\) be an irreducible rank-three type-\(A_3\) residue meeting one endpoint of \(I\). Normalize surgery inside a contiguous ten-position interval \(J\supseteq I\).

### Case 1: \(|I|\le 8\)

There are at least two slack positions in \(J\). Put both slack positions at the endpoint meeting \(R\). Then all three adjacent generators of \(R\) lie inside \(J\). Terminal surgery may therefore use one repaired chamber for the whole residue and collapse the complete \(A_3\) factor to a point. The image point is outward, hence lies in the protected next-depth complex \(X_{r+1}\).

### Case 2: \(|I|=9\)

Only reflected alternating terminal support can have order nine; the span-two reflected type has order at most eight.

Write the two alternating status windows at starts \(1\) and \(4\). Their four-bit words are in \(\{0101,1010\}\). If both reflected orientations occur in one chamber, overlap consistency forces exactly
\[
0101010\qquad\text{or}\qquad1010101
\]
on the seven status positions of the union. In either case there is an alternating forbidden word at an intermediate start (indeed at starts \(2\) and \(3\)), hence a witness edge strictly closer to the center. A protected chamber therefore cannot contain both reflected order-nine alternating occurrences.

Consequently the endpoint-exclusion argument used for order ten applies verbatim: on a terminal sign-flip Coxeter edge, if the generator is disjoint from one of the two six-vertex determining windows, that occurrence has the same truth value at both endpoints; opposite labels then force one endpoint to contain both reflected occurrences, impossible by the preceding paragraph.

For an endpoint \(A_3\) residue on an order-nine span, every generator supported at the endpoint is disjoint from the far six-vertex determining window. Hence no such generator can be a terminal sign-flip edge. The endpoint rank-three residue therefore contains no terminal surgery site and imposes no compatibility condition.

### Case 3: \(|I|=10\)

This is exactly the already proved maximal endpoint-exclusion lemma in [[maximal_ten_support_endpoint_braids_are_impossible]]. Again an endpoint rank-three residue contains no terminal sign-flip edge.

Thus every irreducible rank-three residue meeting a terminal interaction is either collapsed to one protected outward chamber or contains no terminal sign-flip site. Reducible rank-three residues \(A_2\times A_1\) and \(A_1^3\) are products of the already closed protected square/hexagon transport with disjoint safe directions; every chamber of the product remains outward.

### Consequence for the higher-carrier audit

Assuming the terminal block-compression claim \(|B|\le4\) from [[local_witness_topology_and_the_finite_terminal_theorem]], all non-product terminal interaction lives in Coxeter rank at most three. Exterior blocks are disjoint permutahedron factors and safe transport preserves outwardness on every chamber of those factors. Hence the previous audit concern about arbitrary unbounded higher-dimensional terminal cells reduces completely to the already closed rank-two residues plus the rank-three statement above.

This does **not** yet repair the Article VII proof by itself, because the independent audit also found that the terminal block-compression lemmas (including \(|B|\le4\)) are not presently written with enough proof detail to certify. But conditional on those finite-terminal compression lemmas, the higher-dimensional acyclic-carrier objection is removed: the only local carrier factors are protected points/edges/squares/hexagons/rank-three collapses, times safe exterior permutahedron factors, all contractible and wholly contained in \(X_{r+1}\).
