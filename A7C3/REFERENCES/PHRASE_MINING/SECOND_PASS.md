# A7C3 phrase mining: second-pass theorem-source triage

This pass adds a second stage to the phrase miner. Instead of asking only which phrases are ubiquitous, it asks which **accepted active archaeology results concentrate several recurring mechanism phrases**, then applies a portability heuristic favoring order-free scope, short dependency chains, and absence of a smallest-counterexample hypothesis.

The companion script is `source_candidate_ranker.py`.

The score is a discovery aid only. It is not an audit status, proof certificate, or automatic promotion rule.

## New Spare Parts promoted in this pass

### S9003 — Absorbable-Deletion Crossing Lemma

Historical source: `R508`.

Why it survived curation: it is an order-free combinatorial parent with a one-paragraph proof. If `D∪S` already forms one certified tight path and `pc(H)>2`, then every two-cover of `H-D` must physically cross `S | (W\S)`. Several later crossing arguments are specializations of this principle.

### S9004 — Wrap Selection-or-Reversal Lemma

Historical source: `R548`.

Why it survived curation: it is a universal path-cover theorem using only boundary antisymmetry. Rotating one rail either selects its tail-to-head wrap or produces the exact reverse seam packet, and for a long enough rail a reverse `P4`.

### S9005 — Boundary-Reversed Hamilton Dimer Absorber

Historical source: `R561`.

Why it survived curation: two Hamilton representatives exposing one boundary dimer in opposite orientations at opposite ends make the whole support universally one-vertex Hamilton-extendable. The proof is one direct antisymmetry split and is independent of smallest-counterexample machinery.

### S9006 — Cycle-Opening Gain Identity

Historical source: `R17`.

Why it survived curation: `cycle debt` appears throughout the corpus, but the reusable invariant is the exact identity `actual improvement = raw exchange gain - number of cycles opened`. It is generic bookkeeping rather than branch-local geometry.

### S9007 — Both-Singleton Sign Degeneracy Guardrail

Historical source: `R444`.

Why it survived curation: `both-singleton floor` occurs in 58 source files and `ancestry-bearing both-singleton floor` in 40. The theorem explains the distinction: bare opposite singleton signs are automatically realizable from a two-vertex path and therefore carry no triple-turn information. Productive mass-two use must consume ancestry, not merely the labels.

## Strong candidates deliberately not promoted yet

- **R523, Same-support sign interaction.** Extremely reusable and very portable, but close to a direct unpacking of the signed-dimer convention. It may belong in a durable conventions/reference layer rather than as another theorem Spare Part.
- **R471, Two-cover partition rigidity modulo balanced-pair birth.** Mathematically useful, but much of its reusable content decomposes into S9001 Reverse-Ear plus S9002 component/cross-state comparison. Prefer adding concise corollaries to those parts over duplicating a wrapper theorem.
- **R509, cut-indexed outward-transition recompletion exchange.** Scores at the top of the portability heuristic, but its input packet and two-block coordinates are still specialized enough that it is better treated as a candidate than promoted automatically.
- **R915 and nearby reverse-seam packages.** High source scores reflect heavy reuse inside one signed middle-gate technology. They remain branch machinery rather than obvious independent Spare Parts.
- **R195, Four-of-six Hamilton-five density.** A genuinely order-free local theorem and an attractive future candidate, but its proof currently depends on the computational six-vertex theorem R146. A durable rescue should either package that computation cleanly or provide a new conceptual proof.
- **R4, smallest-counterexample minimality.** Ubiquitous and fundamental, but conceptually closer to project foundations than an orphan Spare Part. It may deserve a compact foundational-reference file instead.

## Interpretation of the source ranking

The first source-ranking pass correctly surfaced important central results, but centrality alone over-rewards sophisticated branch machinery. The portability layer therefore records separately:

- mechanism concentration from recurring phrases;
- number of explicit archaeology dependencies;
- whether the theorem assumes a smallest counterexample;
- whether its declared scope is order-free;
- proof size.

Human curation still makes the final decision. In particular, a short theorem with modest phrase frequency can be a better Spare Part than a highly central theorem embedded in one historical branch.

## Current reusable spine discovered by corpus mining

The strongest rescued primitives now form a coherent small library:

`S9001` reverse-order contact geometry;
`S9002` component-drop / cross-state pair birth;
`S9003` absorbable-deletion crossing;
`S9004` wrap selection or reversed endpoint geometry;
`S9005` boundary-reversed Hamilton one-vertex absorption;
`S9006` exchange gain minus cycle debt;
`S9007` singleton-sign degeneracy guardrail.

This is intentionally still sparse relative to the 1,276-document corpus. The miner is being used to collapse repeated mechanisms into a few durable parents, not to mirror archaeology into a second theorem shelf.