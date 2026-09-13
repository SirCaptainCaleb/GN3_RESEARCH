# A7C3 Current Strategy

## G41 — Vice Director: synchronize the one-vertex obstruction with the canonical source packet

Director-function pass: 2026-09-13. This supersedes G40. O4 and O6 remain open.

## Assess

Three targeted audits have changed the live frontier materially.

Audited [R1031](../RESULTS/INTERESTING/R1031.md) proves that the three retained source turns `(A,p,C),(A,q,C),(A,r,C)` force a Hamilton P5 on

    S={A,C,p,q,r}.

Therefore a hypothetical counterexample must have `H[B union {v}]` nonHamiltonian. Any Hamilton path on that support, in any order, together with the source P5 would already be a spanning two-cover of `H`.

Audited [R1033](../RESULTS/INTERESTING/R1033.md) then turns failure of every displayed-order insertion of `v` into the tight spectator path `B` into one exact local obstruction: either a comparison star-triangle or a reverse-spoke hook on `v` and at most three consecutive vertices of `B`.

Audited [R1032](../RESULTS/INTERESTING/R1032.md) is the matching fence. Even in the globally edge-ordered subclass, one can simultaneously realize the source turns, source P5, tight spectator `B`, a physical old source two-cover with `tau(F)=3`, a physical three-forest with `tau(J)=1`, and nonHamiltonicity of both `B+v` and `S+v`. Therefore the remaining obstruction cannot be killed from raw sharp counts plus old-source-block geometry alone.

This removes the main reason for G40's three-complement/common-window taxonomy. The current problem is smaller and more specific.

## Integrate

The strongest actual frontier is now:

1. `S={A,C,p,q,r}` has an audited Hamilton P5.
2. `B union {v}` must be nonHamiltonian.
3. The displayed `B` order therefore carries an audited R1033 star-triangle or reverse-hook obstruction for `v`.
4. Generic sharp source-frame data do not eliminate that obstruction, by R1032.
5. The extra information not represented in R1032 is precisely where the old D17 route may still have teeth: the *canonical* first-loss rectangle, source ancestry, gate placement, and smallest-counterexample provenance.

So the active object is no longer a family of three failed complements. It is one local `v` obstruction that must be synchronized with one canonical source/zipper packet.

The old adaptive complement `B union {v,s}` remains available as a physical consumer when useful, but it should not govern the representation. Likewise the two-vertex insertion automata and common-window lemmas become secondary machinery rather than the default research surface.

## Elevate

The parent target is a **synchronization-or-cover theorem**.

> In the retained smallest-counterexample source frame, combine the canonical D17.421 first-loss/source-gate ancestry with the audited R1033 local obstruction on `v`. Prove that their coexistence forces either a Hamilton path on `B union {v}`, another explicit spanning two-cover of `H`, or a literal strict physical old-source descent with a valid global consumer.

The key word is *canonical*. R1032 already shows that an arbitrary physical `F/J` pair with the same sharp counts is not enough. A successful theorem must use information that identifies how the first-loss switch, source block, gate, or augmenter actually arises from the retained construction, or else use a genuinely global minimal-counterexample consequence that R1032 does not satisfy.

## Moonshot

Try to collapse the synchronization in one shot rather than growing a new taxonomy.

The most promising attack is the **reverse-hook branch first**. R1032 can be chosen globally edge-ordered, so cyclic comparison geometry is not the essential obstruction. A star-triangle-only argument would miss the hard case. Ask instead:

- where can the R1033 hook sit relative to the selected edges and transitions of the actual old `F`?
- can the canonical D17.421 first-loss rectangle occur strictly away from that hook without creating a successful insertion/exchange?
- if the hook overlaps the first-loss rectangle or terminal source gate, do its forced reverse comparisons supply the missing turn in a physical switch or source-pair recompletion?
- does the ordered internal source block force a hook crossing to be one of the canonical transition edges, thereby converting a generic obstruction into old-source descent?

The desired theorem should have a small explicit output, not a sprawling case ledger: synchronized overlap gives a cover/descent; disjointness gives a bypass insertion; or one exact residual gadget survives and becomes the next parent target.

A second moonshot is to derive a minimal-counterexample extension principle strong enough to rule out the R1032 model directly. If minimality forces more than “proper induced subsystem has a two-cover” in this source decomposition, that may bypass the zipper synchronization completely.

## Guide

Three shared focuses dominate.

### 1. Put R1033 onto the actual old F

The first question is not merely where the hook/star sits along `B`, but how the involved `B` edges and spokes occur relative to the selected edges of the physical source two-cover `F`. Track exact predecessor/join/successor turns. If the local certificate does not touch `F`, try to exploit that separation as a legal insertion or switch rather than classifying more patterns.

### 2. Spend canonical ancestry, not just sharp counts

R1032 already includes `tau(F)=3`, `tau(J)=1`, an internal source block, and physical `F/J`. Any argument that mentions only those facts is attacking a known-surviving abstraction. Use something R1032 deliberately lacks: the D17.421 first-loss mechanism, actual augmenter ancestry, canonical gate placement, or an exact smallest-counterexample consequence.

D17.433-D17.439 remain provisional unless separately audited. Their use must retain that trust qualification and the D17.437 COMMON-edge branch.

### 3. Keep adaptive complements as consumers

The old G39 source-pair choice is still valuable when a synchronized local configuration produces a candidate Hamilton word on `B union {v,s}` or a source P4 plus residual path. Use it to finish a concrete branch. Do not rebuild the whole proof around comparing three companions unless new mathematics requires it.

These are shared focuses, not worker assignments.

## Standing fences

- R24/R5 remain frozen and unusable.
- SV118046/D17.428's omitted predecessor-seam route remains fenced.
- R1029 forbids inferring a prescribed far-wall endpoint from D17.430 alone.
- D17.380's special-P5-order and changed-turn warnings remain in force.
- D17.437's COMMON `F intersect J` transition alternative remains live until explicitly excluded.
- R1032 forbids treating raw sharp counts, physical `F/J`, the source P5, or global edge-order integrability as sufficient closure data.
- The R1033 certificate concerns insertion into the displayed `B` order; the stronger nonHamiltonicity of `B+v` comes from R1031 plus the counterexample assumption.
- Matching cardinality is not a physical path cover, numerical improvement is not automatically global descent, and arbitrary reversal of a long path is not free.

O6 remains an independent foundational recovery front.

## What should change after the next wave

A useful next wave should do one of three things:

1. prove that the R1033 obstruction must overlap or align with a canonical first-loss/source-gate feature and physically consume that overlap;
2. prove that separation between them yields a bypass insertion, exchange, or strict old-source descent; or
3. produce an exact counterconfiguration satisfying substantially more of the canonical D17 ancestry than R1032, thereby identifying the next indispensable hypothesis.

More generic insertion classification is no longer the main question.
