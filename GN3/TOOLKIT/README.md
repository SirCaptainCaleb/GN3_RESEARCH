# GN3 reusable toolkit

The toolkit is intentionally small. It indexes broad results already proved in the canonical proof spine rather than copying their proofs or recreating an Engine graph. A result belongs here only when it is natural enough to be useful outside the paragraph that first needed it.

## Selected results

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

## Deliberately proof-local

The minimal-counterexample consequences, endpoint-transfer propositions, fixed-pair continuation machinery, internal-deletion crossing proposition, same-orientation selection, eight induced subgraphs, and lexicographic extremal-cover propositions remain in `PROOF_SPINE/TWO_TIGHT_PATHS.md`. They are important, but their present value is primarily inside this proof. Keeping them in place makes the sequential argument easier to read and avoids a second dependency ontology.

The toolkit should grow only when a result is repeatedly reused or is independently natural enough that extracting it improves retrieval or verification.
