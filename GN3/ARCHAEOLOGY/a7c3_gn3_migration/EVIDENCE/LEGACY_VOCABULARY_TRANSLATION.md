# Legacy A7C3 vocabulary translation aid

Status: **temporary migration archaeology; not canonical theorem language**.

This note exists only so a migration worker reading A7C3 material can recognize the ordinary mathematics now used in GN3. It is deliberately not a word-for-word dictionary. Several A7C3 terms bundled a mathematical object together with proof history, audit history, or an intended future use; GN3 splits those apart and states only the mathematical structure actually needed.

The canonical language is the language of `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`. In particular, legacy vocabulary must not be copied from this note back into canonical proofs.

## Reading guide

| Legacy expression | GN3 mathematical content to recover |
| --- | --- |
| `TWO-COVER`, two-cover | a spanning two-path cover by tight paths |
| physical pair / literal pair `E={a,c}` | two fixed distinct vertices `a,c`; no extra status is carried by the adjective “physical” |
| source orientation at `s` | membership of `s` in the fixed-pair class `X` or `Y`, according as `(a,s,c)` or `(c,s,a)` is tight |
| source path / source-boundary dimer | one of the explicitly defined two-vertex paths `L_s,R_s` through the fixed pair and `s` |
| dimer | a two-vertex tight path; when legacy text attached signs, anchors, or ancestry, recover those separately as endpoint choice, extension direction, and/or membership in an explicitly defined continuation sequence |
| opposite polarity | opposite extension roles: one support is left-extended and the other right-extended. GN3 represents this by an **oppositely extended pair** rather than by a sign label |
| `2+2` birth / balanced pair | where the old argument genuinely needs both two-vertex supports at once, an oppositely extended pair whose two supports both have order two |
| `1+1` floor | an oppositely extended pair whose two supports are singletons |
| anchor / nonanchor | a specifically chosen endpoint of a two-vertex support and the other endpoint. GN3 names the actual endpoint instead of assigning a persistent role label unless that choice is part of a defined move |
| payment / payment continuation | no single GN3 operation. Recover the exact lawful sequence needed: endpoint reduction, one-vertex shortening, prescribed singleton replacement, or a finite continuation sequence composed from those moves |
| refund marker / certificate | the explicit tight triple, path-cover component, ordered edge, or other witness required by the definition of the relevant move. The witness proves that move; it is not stored as abstract “credit” |
| cut memory / retained interval | a true inherited property of a specified subpath after deletion, such as Lemma 4.1 or Lemma 4.3. This does **not** by itself create a later support or continuation step |
| ancestry / lineage | when temporal dependence is mathematically needed, membership and order inside one explicitly fixed continuation sequence. Static facts about an earlier path remain static facts unless a defined transition produces a later pair |
| strict return / later return | a later support in the **same** continuation sequence whose vertex set is a previously named source support; Theorem 4.9 states the limited ordering conclusion that is actually proved |
| remint | removed as ontology. Ask instead whether a specified later two-vertex support occurs in a defined continuation sequence and whether its other endpoint is one of the fixed-pair vertices or a genuinely different vertex |
| replay | removed as ontology. The relevant mathematical residue is exact reuse of an old support such as `{a,s}` or `{s,c}`; new-endpoint geometry is handled explicitly by Proposition 4.8 / Theorem 4.9 |
| harvested / spent history | removed as persistent status. Recover the exact fixed-pair restrictions, continuation reductions, or previously quantified paths actually used by the argument |
| SPECIAL P5 | the explicit tight five-vertex path `(x,a,y,c,z)` (or the version with `a,c` interchanged) |
| crossing | the concrete structure of Proposition 5.2: an ordinary edge `{h,x}` from one path cover, an ordinary edge `{x,y}` from another, and exactly one tight triple from `(h,x,y),(y,x,h)` |
| frame / portal / compiler / state machine / state coordinate | no canonical mathematical object. Recover the underlying fixed vertices, paths, covers, extensions, transitions, or inequalities individually |
| Engine / R-number / S-number | provenance or research organization only. In GN3 a mathematical statement stands as a theorem/lemma/proposition in the sequential proof when it earns that role; historical identifiers belong only in provenance/evidence |

## Important non-translations

Three legacy habits must not be translated mechanically.

1. **Restriction is not reachability.** A singleton or subpath obtained from a path remains a mathematically valid path and may inherit an extension, but it is not thereby a later support in a continuation sequence. GN3 requires one of the intrinsically defined transition relations.
2. **A witness is not currency.** A tight triple or path-cover witness justifies the exact operation whose hypotheses it satisfies. It does not create an abstract balance that can silently be spent later.
3. **Historical occurrence is not mathematical status.** If an argument needs an earlier path, pair, endpoint, orientation, or witness, it fixes that object and the required property explicitly. Words such as “current”, “physical”, “retained”, or “spent” do not add semantics.

This translation aid may be deleted or archived with the rest of `GN3/MIGRATION/` after cutover. Ordinary GN3 work should learn the mathematics from the proof spine, not from this file.
