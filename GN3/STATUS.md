# GN3 mathematical status

This file records status only. Mathematical exposition is in `PROOF_SPINE/TWO_TIGHT_PATHS.md`; provenance is in `PROVENANCE.md` and `MIGRATION/EVIDENCE/`.

## Canonical proof spine

Canonical document: `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`

Audited blob: `b5a3febaaac576946f8a919fd1046e2af69c5059`

Migration record: on 2026-09-17 the user confirmed that this exact language-reduced document had completed audit. Its proved statements are therefore treated as the audited GN3 proof spine at this migration coordinate.

Audit of the document does **not** assert the conjecture itself: the document explicitly stops after Proposition 6.2 and states an unproved augmentation statement.

## Open mathematical frontier

For a smallest counterexample, choose a spanning three-path cover `F` with lexicographically maximal sorted component-order triple `lambda(F)`. The proved spine supplies the extremal-cover restrictions, fixed-pair end information, lawful continuation reductions, deletion/crossing facts, and the other statements through Proposition 6.2.

The remaining bridge is to prove that a spanning three-path cover with no endpoint transfer into a component of at least equal order either yields a spanning two-path cover or can be replaced by a spanning three-path cover with lexicographically larger `lambda`. Such an improvement would contradict the chosen maximality.

`GN3/MIGRATION/EVIDENCE/AUGMENTATION_FRONTIER.md` records research context and why the existing local facts do not yet supply that spanning replacement.

## Status convention

- **Audited** attaches to the exact statement/proof text that was checked.
- **Open** means not proved in canonical GN3 mathematics.
- GitHub placement alone never changes status.
- Research may use unaudited ideas optimistically, but only exact audited mathematics is described here as audited canon.
