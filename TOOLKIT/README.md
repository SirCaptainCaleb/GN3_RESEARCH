# Reusable mathematics

## Proof-spine lemmas

### Comparison representation — Lemma 2.1

For a boundary tournament `G`, orient the line graph of the ordinary complete graph by the tight-triple comparisons. Tight paths are exactly directed chains of consecutive ordinary edges; an edge order realizing all tight triples exists exactly when this comparison digraph is acyclic. A shortest comparison cycle has the chordless ordinary-edge form stated in the proof spine.

### Fixed three-vertex path extension — Lemma 2.5

Given a tight three-vertex path `P` and three distinct vertices outside it, at least one five-set obtained from `P` by adding two of the three outside vertices has a Hamilton tight path.

### Johnson cut bound — Lemma 2.8

If `F` is a family of five-subsets of a ten-element set containing no complementary pair, the number of `J(10,5)` edges between `F` and its complement family is at most `15|F|`.

### Path-forest deletion formula — Lemma 5.1

For an ordinary path forest `F` with `k` components and `S subseteq V(F)`,

`comp(F-S)=k+sum_{v in S}(deg_F(v)-1)-e_F(S)`.

When `F` comes from a tight-path cover, every surviving component inherits a tight order.

### Ordered-path intersection lemmas — Appendix A

Lemma A.1 converts disagreement in the relative order of common vertices of two tight paths into a reversed common edge, a tight reversed-edge triple, or a tight cycle. Lemma A.2 gives the corresponding four-way alternative when another path meets an extended end.

## Standalone lemmas and theorems

### [Path-cover surgery lemmas](PATH_COVER_SURGERY.md)

Crossing under absorbable deletion; cyclic rotations of a tight path; one-vertex absorption from opposite end-edge orientations; the path/cycle edge-exchange component formula; a two-ended Hamilton splice; transitions across a vertex partition; deletion block count and unique-crossing consequences.

### [Local Hamilton extension lemmas](LOCAL_HAMILTON_EXTENSIONS.md)

Bad exterior pairs around a fixed tight three-path form a triangle-free graph; Hamilton five-sets through a prescribed subset of order at most three satisfy the stated density bounds; two parallel middle vertices force a Hamilton four-path.

### [Johnson-graph density bounds](JOHNSON_DENSITY.md)

Local occupancy bounds on `(k+1)`-sets imply the stated quadratic and degree bounds for a family of `k`-sets in `J(r,k)`, together with their equality conditions.

### [Parallel turns and three-vertex core signatures](PARALLEL_TURNS.md)

Exterior vertices around a fixed three-vertex core admit the stated signature compression; three parallel middle vertices admit a Hamilton five-path with at least one of those middle vertices as an endpoint, and no fixed middle vertex can always be prescribed.

### [Complement-free Johnson bounds](JOHNSON_COMPLEMENT_BOUNDS.md)

For a complement-free family `F` of `m` five-subsets of a ten-element set, the graph joining pairs with intersection one has average degree at most

`7+18m/252 <= 16`.

### [Ternary path-system insertion theorem](TERNARY_PATH_SYSTEMS.md)

In a reversal-symmetric ternary path system satisfying the stated three-vertex completeness axiom, every exterior vertex has at least two insertion positions in a tight path. Every `n`-vertex system therefore has at least `2^(n-1)` Hamilton tight paths, and the bound is sharp.

### [Cover-comparison and matching lemmas](COVER_COMPARISON.md)

A drop in the number of path-cover components forces an ordinary crossing edge; the Cartesian clause lemma has the stated boundary-tournament specialization; the weighted symmetric difference of two matchings satisfies the stated dichotomy when the total `F`-weight is positive.

### [Cover augmentation lemmas](COVER_AUGMENTATION.md)

Failed concatenations force reversed joining triples; the stated one-cut/two-join and two-cut singleton moves reduce component count; repeated singleton transfers force an extreme triangle edge; globally extreme two-vertex components impose the stated barriers; the three-vertex-component cut and fixed-two-cover concatenation lemmas hold.

### [Path insertion and endpoint replacement lemmas](PATH_INSERTION.md)

Two-sided endpoint replacement forces a reversal in common-vertex order; noninsertability in an edge-ordered complete graph yields the stated barrier gap; complete insertion failure in a boundary tournament yields one of the stated bounded comparison-digraph obstructions; opposite extensions of one ordered pair concatenate.

### [Four-vertex structure and fifth-vertex extensions](FOUR_VERTEX_STRUCTURE.md)

Two parallel turns on a non-Hamiltonian four-set force one of two matching-block edge orders; the cyclic non-Hamiltonian four-vertex configuration is extended by every fifth vertex; non-Hamiltonian fifth-vertex extensions of an edge-ordered non-Hamiltonian four-set satisfy the stated extreme- and middle-matching restrictions; the ordered two-vertex extension consequence and the `3/5` four-subset density bound hold.
