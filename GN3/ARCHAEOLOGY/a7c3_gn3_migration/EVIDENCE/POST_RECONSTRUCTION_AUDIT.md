# Post-reconstruction GN3 audit

Status: migration evidence for checklist items 29–46. This document is not mathematical exposition.

Audit coordinate:

- proof spine blob: `b5a3febaaac576946f8a919fd1046e2af69c5059`;
- architecture after synchronization: commit `416000a514c3a16d2c070f148f760de02d74fe2f`;
- canonical status: `GN3/STATUS.md`;
- big-picture research entry point: `GN3/RESEARCH_STATE.md`;
- research protocol: `GN3/RESEARCH_PROTOCOL.md`;
- reusable shelf: `GN3/TOOLKIT/README.md`.

## Factorization audit

The single proof spine, rather than the A7C3 result graph, determines theorem boundaries.

The selected reusable shelf contains only five broad items: comparison representation, fixed three-vertex path extension, the Johnson cut bound, the path-forest deletion formula, and the ordered-path intersection lemmas. Their proofs remain at their canonical locations in the spine. All other numbered statements remain proof-local.

Several Section 4 lemmas are narrow, but they are intentionally retained because they make lawful reachability checkable. In particular, the definitions and proofs of endpoint reduction, one-vertex shortening, prescribed singleton replacement, and their composition prevent the exact historical error in which restriction/deletion was treated as a reached descendant. Their independent presentation improves verification rather than transporting an old Engine frame.

There is no canonical GN3 Engine dependency graph. Engine-like labels are optional research organization only; canonical mathematics is the sequential proof.

## Human-style readability audit

An unrelated graph theorist can begin at Section 1 and read the argument without A7C3 archaeology. The proof defines boundary tournaments, tight paths, path covers, comparison digraphs, endpoint transfers, fixed-pair orientation classes, extended paths, oppositely extended pairs, every continuation move, deletion notation, and lexicographic maximality before relying on them.

Legacy audit/workflow vocabulary is not required to interpret the proof. The dense point is Section 4, but its nonstandard nouns are mathematical rather than historical: each denotes a structurally defined object or relation with explicit domain and hypotheses. The section expressly distinguishes inherited restrictions from actual continuation reachability.

The proof visibly stops at the augmentation statement after Proposition 6.2. It does not disguise that bridge as an established continuation or imported Engine interface. `STATUS.md` separately records that the proved text is audited while the augmentation remains open.

No load-bearing finite check is hidden behind “one checks”: the five-vertex arguments give explicit forcing tables, and the order-ten argument states its counting inequalities.

## Cargo-cult and alternatives audit

The migrated state does not reproduce the old channel taxonomy, Engine sequence, payment ontology, remint ontology, signed-credit vocabulary, or result-number graph. The three GN3 Slack channels have distinct operational purposes rather than historical one-to-one A7C3 analogues.

The fixed-pair continuation formalism survives because the mathematics genuinely needs a reachability relation; it has been rebuilt intrinsically instead of preserved because A7C3 had a state machine. The comparison-digraph and edge-order machinery survives because it materially shortens and internalizes the small-order proof. The lexicographic extremal cover is a new global organization of the active proof rather than an Engine wrapper.

Known alternative inputs are preserved without controlling topology: the longest-path route, fixed-pair route, deletion/crossing route, same-orientation five-path, and ordered-path intersection tools all appear where their actual mathematical content is used. The open augmentation frontier explicitly notes that these local facts still need a literal spanning replacement construction.

## Negative knowledge retained

The migration keeps only negative knowledge that prevents expensive regression: the invalid legacy payment reconstructions and the restriction-versus-reachability fence remain in provenance/evidence; the current augmentation note records why existing local contact facts do not yet imply a spanning replacement. Failed historical ontology is not imported into theorem language.

## Failure-honesty audit

`RESEARCH_PROTOCOL.md` explicitly allows null returns, separates “no proof found” from counterexample/missing hypothesis/structural obstruction, and distinguishes search progress from theorem progress. Neither the architecture nor the GN3 Slack design imposes quotas for named results, Engines, or nonempty returns.

## Result

The reconstructed GN3 state passes the factorization, readability, cargo-cult, and failure-honesty audits required before final architecture/startup testing and post-baseline reconciliation. No mathematical rewrite is required by this audit.
