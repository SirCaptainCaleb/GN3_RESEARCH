# GN3 reusable toolkit

The toolkit contains selected mathematics that a future researcher could reasonably want independently of the route that first produced it. It is not a second proof graph, discovery log, or archive of every correct lemma.

Most proof-local facts remain in the canonical proof spine. Standalone toolkit files are used when extraction materially improves retrieval, reuse, or verification. Migration does not transfer certification: each standalone file states the audit status of its exact current mathematical text.

## Indexed from the proof spine

### Comparison representation — Lemma 2.1

For a boundary tournament `G`, orient the line graph of the ordinary complete graph by the tight-triple comparisons. Tight paths are exactly directed chains of consecutive ordinary edges; an edge order realizing all tight triples exists exactly when this comparison digraph is acyclic. A shortest comparison cycle has a sharply constrained chordless ordinary-edge shape.

**Why retained:** this is a general representation theorem for boundary tournaments, independent of the minimal-counterexample route.

### Fixed three-vertex path extension — Lemma 2.5

Given a tight three-vertex path `P` and three distinct vertices outside it, at least one five-set obtained from `P` by adding two of the three outside vertices has a Hamilton tight path.

**Why retained:** this is a compact local extension principle reused in the small-order argument and potentially useful in future local constructions.

### Johnson cut bound — Lemma 2.8

If `F` is a family of five-subsets of a ten-element set containing no complementary pair, the number of `J(10,5)` edges between `F` and its complement family is at most `15|F|`.

**Why retained:** this is a clean standalone extremal-set statement with no proof-specific ontology.

### Path-forest deletion formula — Lemma 5.1

For an ordinary path forest `F` with `k` components and `S subseteq V(F)`,

`comp(F-S)=k+sum_{v in S}(deg_F(v)-1)-e_F(S)`.

When `F` comes from a tight-path cover, every surviving component inherits a tight order.

**Why retained:** this is a general bookkeeping identity for literal path-cover surgery and is useful for checking proposed spanning replacements.

### Ordered-path intersection lemmas — Appendix A

Lemma A.1 converts disagreement in the relative order of common vertices of two tight paths into a reversed common edge, a tight reversed-edge triple, or a tight cycle. Lemma A.2 gives the corresponding four-way alternative when another path meets an extended end.

**Why retained:** these are general path-intersection principles and isolate order-sensitive reasoning that would otherwise be repeatedly rederived.

## Standalone modules with GN3 audit PASS

### [Path-cover surgery lemmas](PATH_COVER_SURGERY.md)

Seven general tools for cut-and-join work: a crossing forced by an absorbable deletion, cyclic path rotations, a one-vertex Hamilton absorber, the path/cycle edge-exchange component formula, a two-ended Hamilton splice, the partition-transition identity, and the deletion block-count/unique-crossing lemma.

### [Local Hamilton extension lemmas](LOCAL_HAMILTON_EXTENSIONS.md)

Three local extension results: the triangle-free graph of bad exterior pairs around a fixed tight three-path, density of Hamilton five-sets through a prescribed set of at most three vertices, and a four-vertex extension from two parallel middle vertices.

### [Johnson-graph density bounds](JOHNSON_DENSITY.md)

Two general extremal-set inequalities converting a local cap on the number of selected `k`-sets inside each `(k+1)`-set into global density bounds in `J(r,k)`, together with equality constraints.

### [Parallel turns and three-vertex core signatures](PARALLEL_TURNS.md)

A three-coordinate signature compression for exterior vertices around a fixed core, and the strengthening of Lemma 2.2 that three parallel middle vertices admit a Hamilton five-path with at least one of those middle vertices as an endpoint.

### [Complement-free Johnson bounds](JOHNSON_COMPLEMENT_BOUNDS.md)

The intersection-one spectral bound for complement-free families of five-subsets of a ten-set. The companion four-overlap cut bound is already Lemma 2.8 of the proof spine and is not duplicated here.

### [Ternary path-system insertion theorem](TERNARY_PATH_SYSTEMS.md)

For a reversal-symmetric ternary path system satisfying the stated three-vertex completeness axiom, every exterior vertex has at least two insertion positions in a tight path, yielding a sharp `2^(n-1)` lower bound on Hamilton tight paths.

## Standalone modules revised after audit and pending re-audit

### [Cover-comparison and matching lemmas](COVER_COMPARISON.md)

A component-drop crossing lemma stated without signed-support language, the direct observation that two singleton components impose no three-vertex tightness condition, an intrinsic Cartesian clause lemma for families of spanning vertex sequences, and a weighted symmetric-difference lemma for two matchings. The matching lemma includes the positive-total-weight hypothesis needed by its intrinsic formulation.

### [Cover augmentation lemmas](COVER_AUGMENTATION.md)

Explicit spanning-cover surgery: reversed joining triples forced by failed component concatenation, one-cut/two-join augmentation in edge-ordered complete graphs, a two-cut singleton cross-swap, inequalities forced by repeated singleton transfers, barriers forced by a globally extreme two-vertex component, a cut-and-join obstruction around a three-vertex component, and comparison of concatenations of a three-cover with a fixed two-cover.

### [Path insertion and endpoint replacement lemmas](PATH_INSERTION.md)

Two-sided endpoint replacement forces a reversal in common-vertex order; failed insertion in an edge-ordered complete graph has a canonical barrier gap; complete insertion failure in an arbitrary boundary tournament has a bounded comparison-digraph obstruction supported on the inserted vertex and at most four consecutive path vertices; opposite extensions of one ordered pair concatenate immediately.

### [Four-vertex structure and fifth-vertex extensions](FOUR_VERTEX_STRUCTURE.md)

The two edge-orderable normal forms forced by two parallel turns on a non-Hamiltonian four-set, universal fifth-vertex extension of the cyclic non-Hamiltonian four-set, explicit extreme- and middle-matching structure for a non-Hamiltonian fifth-vertex extension of an edge-ordered four-set, a two-vertex extension consequence, and the `3/5` density bound for Hamiltonian four-subsets of an edge-ordered complete graph.

## Deliberately proof-local

The minimal-counterexample consequences, endpoint-transfer propositions, fixed-pair continuation machinery, internal-deletion crossing proposition, same-orientation selection, eight induced subgraphs, and lexicographic extremal-cover propositions remain in `PROOF_SPINE/TWO_TIGHT_PATHS.md`. They are important, but their present value is primarily inside this proof. Keeping them in place makes the sequential argument easier to read and avoids a second dependency ontology.

Legacy phase-descent, packet, payment, source-routing, and Engine terminology has not been migrated as terminology. Where an old spare part contained reusable mathematics, only its intrinsic graph-theoretic, edge-ordered, set-theoretic, or matching-theoretic core was retained in the modules above.