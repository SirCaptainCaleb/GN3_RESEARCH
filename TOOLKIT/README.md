# GN3 reusable toolkit

The toolkit is intentionally small. Most entries index broad results already proved in the canonical proof spine rather than copying their proofs. A small number of independently natural results that do not belong in the proof spine may live here as standalone theorem files. Migration does not transfer certification: every standalone rewrite carries its own GN3 audit status.

A result belongs here only when a future researcher could reasonably want the mathematics independently of the route that first produced it. The toolkit is not a second proof graph, discovery log, or archive of every passed lemma.

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

For an ordinary path forest `F` with `k` components and `S⊆V(F)`,

`comp(F-S)=k+sum_{v in S}(deg_F(v)-1)-e_F(S)`.

When `F` comes from a tight-path cover, every surviving component inherits a tight order.

**Why retained:** this is a general bookkeeping identity for literal path-cover surgery and is useful for checking proposed spanning replacements.

### Ordered-path intersection lemmas — Appendix A

Lemma A.1 converts disagreement in the relative order of common vertices of two tight paths into a reversed common edge, a tight reversed-edge triple, or a tight cycle. Lemma A.2 gives the corresponding four-way alternative when another path meets an extended end.

**Why retained:** these are general path-intersection principles and isolate order-sensitive reasoning that would otherwise be repeatedly rederived.

## Standalone migrated modules

The following files preserve selected reusable mathematics from the A7C3 spare-parts shelf in ordinary GN3 language. The exact current text of all three standalone modules has passed independent GN3 audit.

### [Path-cover surgery lemmas](PATH_COVER_SURGERY.md)

Seven general tools for cut-and-join work: a crossing forced by an absorbable deletion, cyclic path rotations, a one-vertex Hamilton absorber, the path/cycle edge-exchange component formula, a two-ended Hamilton splice, the partition-transition identity, and the deletion block-count/unique-crossing lemma.

**Why retained:** these are direct tools for literal spanning replacements and path-cover surgery, including several mechanisms especially relevant to the present augmentation frontier.

### [Local Hamilton extension lemmas](LOCAL_HAMILTON_EXTENSIONS.md)

Three local extension results: the triangle-free graph of bad exterior pairs around a fixed tight three-path, density of Hamilton five-sets through a prescribed set of at most three vertices, and a four-vertex extension from two parallel middle vertices.

**Why retained:** these turn the five- and six-vertex theory into reusable extension and density principles without carrying the old research vocabulary.

### [Johnson-graph density bounds](JOHNSON_DENSITY.md)

Two general extremal-set inequalities converting a local cap on the number of selected `k`-sets inside each `(k+1)`-set into global density bounds in `J(r,k)`, together with equality constraints.

**Why retained:** these are clean standalone combinatorial results, broader than the parameter-specific Johnson argument used in the proof spine.

## Deliberately proof-local

The minimal-counterexample consequences, endpoint-transfer propositions, fixed-pair continuation machinery, internal-deletion crossing proposition, same-orientation selection, eight induced subgraphs, and lexicographic extremal-cover propositions remain in `PROOF_SPINE/TWO_TIGHT_PATHS.md`. They are important, but their present value is primarily inside this proof. Keeping them in place makes the sequential argument easier to read and avoids a second dependency ontology.

The toolkit should grow only when a result is repeatedly reused or is independently natural enough that extracting it improves retrieval or verification.