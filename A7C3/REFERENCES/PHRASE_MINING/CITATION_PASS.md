# A7C3 citation-graph reuse pass

Phrase frequency finds recurring language. Source scoring finds theorem statements that explain several recurring phrases. A third signal is already latent in the corpus: **how many distinct source files actually cite each accepted result**.

The companion script `citation_reuse_ranker.py` parses the `R<number>` references in `SEARCH_CORPUS.md`, counts distinct-file inbound references to every `USABLE/ACTIVE` result, and records simple portability metadata. The count is a discovery signal only. It does not certify current validity, independence, or Spare-Part suitability.

## Highest-reuse active results

| Result | Distinct citing files | Curation disposition |
|---|---:|---|
| R3 | 521 | Foundational boundary-antisymmetry axiom; reference primitive, not a Spare Part. |
| R435 | 212 | Already rescued as `S9001` Reverse-Ear Lemma. |
| R4 | 153 | Foundational smallest-counterexample minimality; better treated as project foundation than orphan theorem. |
| R436 | 136 | Rescued as `S9010` Signed-Path Contact and Historical Anchor Protection. |
| R176 | 104 | Cross-state upgrade already inlined into `S9002`. |
| R542 | 103 | Highly reused, but still short-carrier capture/payment machinery tied to the signed-payment lineage; defer. |
| R621 | 98 | Crossed-middle-gate structural machinery; branch-specific, not a Spare Part. |
| R523 | 89 | Same-support sign interaction; essentially convention unpacking, better suited to a conventions/reference layer. |
| R159 | 88 | Rescued with R176 as `S9002` Punctured Component-Drop Pair Theorem. |
| R508 | 83 | Rescued as `S9003` Absorbable-Deletion Crossing Lemma. |
| R561 | 68 | Rescued as `S9005` Boundary-Reversed Hamilton Dimer Absorber. |
| R594 | 59 | R24-failure reduction machinery; historically central but branch-specific. |
| R927 | 55 | Specialized source-crossing saturation theorem; retain in archaeology/Engine context. |
| R527 | 48 | Same-frame crossing/capture/refund package; highly useful inside signed-payment machinery but not a clean independent primitive. |
| R518 | 47 | Universal-looking four-cell theorem, but it depends on the exact signature package and accepted/provisional historical ingredients; do not rescue without a fresh dependency audit. |
| R887 | 43 | Rescued as `S9011` Line-Graph Comparison Representation Theorem. |
| R428 | 42 | Smallest-counterexample singleton-payment descent; lineage-dependent, defer. |
| R434 | 42 | Fixed-turn endpoint-budget package; depends on several ancestry/protection mechanisms, not portable enough. |
| R432 | 41 | Target steering for ancestry-bearing singleton floors; useful but payment-lineage specific. |
| R902 | 41 | **Not promotable:** its own record says the computer-assisted proof remains pending independent review. |

## Additional citation-mined rescues

### S9010 — Signed-Path Contact and Historical Anchor Protection

Historical source: `R436`, cited by 136 distinct corpus files.

The theorem is a genuine parent: contact away from the signed anchor strictly shortens the old support while preserving the anchor; contact at the anchor must expose path growth, Reverse-Ear geometry, or a proper cycle. Its only real external mathematical ingredient is Reverse-Ear plus boundary antisymmetry.

### S9011 — Line-Graph Comparison Representation Theorem

Historical source: `R887`, cited by 43 distinct corpus files.

This result supplies a conceptual representation of the whole tight-turn relation as an orientation of `L(K_V)`, proves that global edge-orderability is exactly acyclicity of this comparison orientation, and gives a shortest-cycle holonomy certificate when integrability fails. Phrase mining underweighted it because descendants use several different vocabularies for the same representation.

### S9012 — Two-Ended Endpoint Replacement Lemma

Historical source: `R966`, cited by 24 distinct corpus files.

Although not among the very highest citation counts, it is unusually portable: one exterior vertex cannot Hamilton-replace both endpoints of a Hamilton path while the full extension remains non-Hamiltonian unless a Reverse-Ear comparison fires. No smallest-counterexample or cover machinery is used.

### S9013 — Partition-Cover Deficit Identity

Historical source: `R7`.

This small counting identity is reusable enough to preserve even without extreme citation count. Relative to a fixed partition, cross-class transitions equal intrinsic class path-cover complexity minus current component count plus a nonnegative representative-relative excess. The proof is a one-line block count and has no A7C3-specific dependency.

## Refinement rather than duplication

Citation mining also identified `R579`, the exact four-way wrap classification, as a refinement of `R548`. Rather than create another Spare Part, its double-wrap / single-wrap / double-fail classification was incorporated into `S9004`.

Likewise `R471` remains intentionally unpromoted: its useful content largely decomposes into `S9001` Reverse-Ear and `S9002` same-residue cross-state/component-drop comparison.

## Current cutoff philosophy

A result is a strong Spare-Part candidate when several signals agree:

1. recurring phrase/mechanism vocabulary;
2. substantial inbound reuse from distinct documents;
3. order-free or clearly bounded general hypotheses;
4. a short standalone proof or a dependency chain that can be cleanly inlined/replaced by existing Spare Parts;
5. mathematical content not already subsumed by another rescued primitive.

High citation count alone is not enough. In particular, branch-local payment/gate machinery can be cited very heavily while still belonging inside its coherent Engine/history rather than in the generic library.