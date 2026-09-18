# Reusable mathematics

This README is the startup-facing **statement index** for the toolkit. It should represent every retained toolkit theorem or lemma at statement-level detail sufficient to recover its hypotheses and conclusion. The linked toolkit modules are primarily the proof and exposition surface and are opened when a proof or exact local detail is needed.

The toolkit is the preferred home for general-purpose lemmas that can be used independently of the main proof architecture. In particular, reusable mathematics extracted from the proof spine should be cited here rather than recovered from the sequential proof.

Proof-specific minimal-counterexample reductions, extremal-cover statements, and the fixed-pair continuation machinery remain in `PROOF_SPINE/TWO_TIGHT_PATHS.md`; their hypotheses are specialized to the main argument rather than general utilities.

## Foundational boundary-tournament utilities

### [Small-order Hamiltonicity and edge-order representation](SMALL_ORDER_HAMILTONICITY.md)

The universal small-order results formerly available only inside the proof spine:

- comparison-digraph representation of boundary tournaments and characterization of edge-order representability by acyclicity;
- three common-endpoint tight triples force a Hamilton five-path;
- **every non-Hamiltonian five-vertex boundary tournament is represented by a strict edge order**;
- the matching-block classification of a non-Hamiltonian edge-ordered `K_4`;
- two non-Hamiltonian edge-ordered four-sets with a common triple force an increasing Hamilton path on their five-vertex union;
- extension of a fixed tight three-vertex path by at least one of three exterior pairs;
- every six-set has at least four Hamiltonian five-subsets;
- the sharp local restrictions on non-Hamiltonian four-subsets of a five-set.

These statements are universal; no smallest-counterexample hypothesis is used.

### [Path restriction, forest deletion, and ordered-path intersections](PATH_FORESTS_AND_INTERSECTIONS.md)

General path utilities extracted from the proof spine:

- restriction of a left- or right-extended path at its first/last intersection;
- inheritance of an extension by the first or last surviving interval after deletion;
- the ordinary path-forest deletion formula
  `comp(F-S)=comp(F)+sum_{v in S}(deg_F(v)-1)-e_F(S)`;
- disagreement in the relative order of common vertices of two tight paths forces a reversed common edge, a reversed-edge tight triple, or a vertex-simple tight cycle;
- the corresponding four-way alternative when another path meets an extended end.

## Hamilton-extension and local-structure tools

### [Local Hamilton extension lemmas](LOCAL_HAMILTON_EXTENSIONS.md)

Bad exterior pairs around a fixed tight three-path form a triangle-free graph; Hamilton five-sets through a prescribed subset of order at most three satisfy the stated density bounds; two parallel middle vertices force a Hamilton four-path. Its small-order inputs are now taken from `SMALL_ORDER_HAMILTONICITY.md`.

### [Parallel middle vertices and match sets relative to a fixed three-set](PARALLEL_TURNS.md)

Exterior vertices relative to a fixed three-vertex set admit the stated match-set classification; three parallel middle vertices admit a Hamilton five-path with at least one of those middle vertices as an endpoint, and no fixed middle vertex can always be prescribed; four parallel middle vertices force a five-path of the form `(x,a,y,c,z)`.

### [Four-vertex structure and fifth-vertex extensions](FOUR_VERTEX_STRUCTURE.md)

Two tight triples with a common first ordered pair on a non-Hamiltonian four-set force one of two matching-block edge orders; the cyclic non-Hamiltonian four-vertex configuration is extended by every fifth vertex; non-Hamiltonian fifth-vertex extensions of an edge-ordered non-Hamiltonian four-set satisfy the stated extreme- and middle-matching restrictions; the ordered two-vertex extension consequence and the `3/5` four-subset density bound hold. The matching-block classification is sourced from `SMALL_ORDER_HAMILTONICITY.md`.

## Path-cover manipulation

### [Path-cover modification lemmas](PATH_COVER_SURGERY.md)

Crossing under absorbable deletion; cyclic rotations of a tight path; one-vertex absorption from opposite end-edge orientations; the path/cycle edge-exchange component formula; joining two path-cover components through a Hamilton path; transitions across a vertex partition; deletion block count and unique-crossing consequences.

### [Cover-comparison and matching lemmas](COVER_COMPARISON.md)

A drop in the number of path-cover components forces an ordinary crossing edge; the Cartesian clause lemma has the stated boundary-tournament specialization; the weighted symmetric difference of two matchings satisfies the stated dichotomy when the total `F`-weight is positive.

### [Cover augmentation lemmas](COVER_AUGMENTATION.md)

Failed concatenations force reversed joining triples; the stated one-cut/two-join and two-cut singleton moves reduce component count; repeated singleton transfers force an extreme triangle edge; globally extreme two-vertex components impose the stated barriers; the three-vertex-component cut and fixed-two-cover concatenation lemmas hold.

### [Path insertion and endpoint replacement lemmas](PATH_INSERTION.md)

Two-sided endpoint replacement forces a reversal in common-vertex order; noninsertability in an edge-ordered complete graph yields the stated barrier gap; complete insertion failure in a boundary tournament yields one of the stated bounded comparison-digraph obstructions; opposite extensions of one ordered pair concatenate. Ordered-path intersection consequences are sourced from `PATH_FORESTS_AND_INTERSECTIONS.md`.

## Johnson-graph and set-family bounds

### [Johnson-graph density bounds](JOHNSON_DENSITY.md)

Local occupancy bounds on `(k+1)`-sets imply the stated quadratic and stronger local-degree bounds for a family of `k`-sets in `J(r,k)`, together with their equality conditions. The boundary-tournament specialization gives the stronger fixed-subset Hamilton-five density hierarchy: for `|S|=s<=3`, the non-Hamiltonian fraction among five-sets containing `S` is at most `(r-s)/[(5-s)(r-4)]`, strictly improving the elementary double-counting hierarchy for `r>10`. This file also retains the extracted `J(10,5)` complement-pair cut bound as a separate reusable set-family lemma.

### [Complement-free Johnson bounds](JOHNSON_COMPLEMENT_BOUNDS.md)

For a complement-free family `F` of `m` five-subsets of a ten-element set, the graph joining pairs with intersection one has average degree at most

`7+18m/252 <= 16`.

## Abstract path systems

### [Ternary path-system insertion theorem](TERNARY_PATH_SYSTEMS.md)

In a reversal-symmetric ternary path system satisfying the stated three-vertex completeness axiom, every exterior vertex has at least two insertion positions in a tight path. Every `n`-vertex system therefore has at least `2^(n-1)` Hamilton tight paths, and the bound is sharp.
