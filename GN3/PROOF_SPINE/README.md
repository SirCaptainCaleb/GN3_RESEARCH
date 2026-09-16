# GN3 proof spine

**Status: supervised migration reconstruction; not yet GN3-certified.**

This directory contains the blank-page reconstruction of the active proof of the two-path-cover theorem. It is intentionally organized as readable mathematics rather than as a translation of the legacy Engine graph.

At the present frontier there are two live branches. Neither is known to subsume the other, and neither has been discarded.

1. [`FIXED_PAIR_RETURN.md`](FIXED_PAIR_RETURN.md) — fix a physical pair, repeatedly return to the same literal singleton floor, spend the source-boundary histories around almost every exterior vertex, and force any later opposite-sign dimer birth to collide with spent history. The unresolved step is the extinction of exact replay at that collision.
2. [`FIRST_SOURCE_DESCENT.md`](FIRST_SOURCE_DESCENT.md) — classify a three-spoke Boolean cube of exact two-covers, turn every classification leaf into a source-visible proper path or cycle, and use marked-rail growth to obtain a strict phased-rank descent. The unresolved step is to make that strict first-source descent recursively effective after the phase-zero entrance.

Both branches begin with the same certified small-order consequence: a hypothetical smallest counterexample `H` has `|H|>10`.

The documents are mathematical reconstructions, not certifications. Legacy A7C3 PASS status is recorded only as provenance for the exact ingredients reused. Under `GN3/ARCHITECTURE.md`, these rewrites require independent GN3 audit before they can themselves be regarded as certified text.

Vocabulary normalization has deliberately **not** been performed here; that remains the next user-supervised migration gate.
