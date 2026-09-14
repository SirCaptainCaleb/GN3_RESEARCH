# A7C3 Current Strategy

## G41 — Vice Director: bridge provenance or bypass it by minimality

Director-function pass: 2026-09-13. This sharpens G41 without replacing its core contraction. O4 and O6 remain open.

## Assess

Four targeted audits now govern the live O4 frontier.

Audited [R1031](../RESULTS/INTERESTING/R1031.md) proves that the three retained source turns `(A,p,C),(A,q,C),(A,r,C)` force a Hamilton P5 on

    S={A,C,p,q,r}.

Therefore a hypothetical counterexample must have `H[B union {v}]` nonHamiltonian. Any Hamilton path on that support, in any order, together with the source P5 would already be a spanning two-cover of `H`.

Audited [R1033](../RESULTS/INTERESTING/R1033.md) then turns failure of every displayed-order insertion of `v` into the tight spectator path `B` into one exact local obstruction: either a comparison star-triangle or a reverse-spoke hook on `v` and at most three consecutive vertices of `B`.

Audited [R1032](../RESULTS/INTERESTING/R1032.md) shows that raw sharp source-frame data are insufficient. Audited [R1034](../RESULTS/INTERESTING/R1034.md) goes further: even the displayed static D17.391 spectator-gate conclusions, including the noncyclic R516-11 P4-free cell, both endpoint P5-free five-sets, both universal reverse endpoint stars, and physical sharp `F/J`, can coexist with the stubborn one-vertex obstruction in one globally edge-ordered realization.

Thus the missing information is not another static gate condition. Whatever closes O4 must use something R1034 deliberately does not encode: dynamic/canonical provenance, a stronger smallest-counterexample consequence, or another genuinely global invariant.

## Integrate

The strongest actual frontier is now:

1. `S={A,C,p,q,r}` has an audited Hamilton P5.
2. `B union {v}` must be nonHamiltonian.
3. The displayed spectator order on `B` therefore carries an audited R1033 star-triangle or reverse-hook obstruction for `v`.
4. Raw sharp counts do not eliminate it, by R1032.
5. The full displayed static quiet spectator-gate packet does not eliminate it, by R1034.
6. The remaining D17 information with possible force is chiefly *how* the sharp configuration was produced: unique augmenter, first positive prefix, canonical first-loss switch, source ancestry, and related provenance.

There is also a structural mismatch that should be treated explicitly rather than hand-waved away. R1033 lives in the **spectator-order coordinate system**: its `B-B` edges are consecutive edges of the Hamilton path `B`. D17.421 lives in the **old-F / augmenter coordinate system**: its `B-B` side is a selected edge of the old source cover and need not be adjacent in spectator order. Therefore “the hook overlaps the zipper” is not even a well-defined premise until a theorem bridges those coordinate systems.

The active object is accordingly not a larger local packet. It is the missing bridge between two exact representations of the same counterexample.

## Elevate

There are now two legitimate parent targets.

### A. Provenance / coordinate bridge

> In the retained smallest-counterexample source frame, the canonical generation of the unique augmenter and first-loss `K2,2` packet forces the R1033 spectator-order obstruction to constrain an old-F transition, gate, or augmenter state strongly enough to yield a physical cover or strict old-source descent.

This target must use genuinely dynamic information. Any proof whose hypotheses can be read entirely from a static D17.391 snapshot is attacking an abstraction already survived by R1034.

### B. Minimality splice

Minimality gives an exact at-most-two cover of the proper subsystem `B union {v}`. Because R1031 supplies a Hamilton source P5 on the disjoint five-set `S`, a counterexample carries a very rigid three-path decomposition

    source-P5 | U | V.

Seek a theorem that splices the source P5 into one rail of an arbitrary exact two-cover `U|V` of `B union {v}`, or otherwise transforms this three-cover into a two-cover. Such a theorem would bypass the zipper provenance entirely.

A current provisional strengthening shows that the source turns force some Hamilton source P5 with at least one source-spoke endpoint, but not with a prescribed source spoke. Treat that endpoint fact as provisional until audited if it is used.

## Moonshot

### 1. Attack the unique-augmenter provenance, not the endpoint snapshot

Read D17.409-412 as a generated chain. Ask what invariant of that generation survives into D17.421 and is absent from R1034. In particular:

- does the first positive prefix force a relation between the old-F selected `B-B` edge and a consecutive spectator edge?
- does the unique v-transition occur at a spectator-order cut that the R1033 first-flip index must cross?
- can a spectator-order reverse hook sit entirely inside one old-F block without creating an earlier positive pivot?
- if the two coordinate systems remain independent, can that independence itself be realized by a stronger countermodel satisfying the actual canonical construction?

The desired output is a coordinate lemma, not another taxonomy of local turns.

### 2. Attack minimality as a three-cover recompletion problem

Forget the zipper temporarily and take an arbitrary exact two-cover `U|V` of `B union {v}`. Combine it with the source P5. Try to prove one of:

- one endpoint of a source Hamilton P5 can always join one endpoint of `U` or `V` with all necessary neighboring turns;
- failure of all such joins forces an endpoint comparison pattern that R3 cannot sustain across the two rail ends and three source spokes;
- a pairwise source P4 from D17.368 plus one rail gives a more flexible recompletion than the full source P5.

Do not assume the old withdrawn three-petal prism: D17.166 explicitly corrected that endpoint-perfect data only gives a matching, not the claimed prism.

### 3. Strengthen the countermodel if both targets are too weak

If neither bridge nor splice yields a theorem, push R1034 toward the actual canonical provenance. The useful negative result is not “another edge-ordered example”; it is the strongest exact subset of D17.409-421 that can still coexist with the R1033 obstruction. That identifies the next indispensable hypothesis cleanly.

## Guide

Three shared focuses dominate.

### 1. Coordinate bridge

Work with exact old-F selected edges and exact spectator-adjacent edges simultaneously. Do not identify them by notation or geometric intuition. The first valuable lemma says where one coordinate system must touch the other.

### 2. Minimality splice

Treat `source-P5 | U | V` as a concrete physical three-cover and search for a two-cover recompletion theorem. Endpoint control is valuable only when it certifies the actual neighboring turns needed by the final concatenated words.

### 3. Dynamic provenance only

R1034 exhausts the displayed static D17.391 frame. Spend D17.409-421 only where the proof uses that a state is the unique augmenter, the first positive prefix, the first numerical loss, or another generated/canonical object. Merely restating endpoint gates or sharp counts is low value.

These are shared focuses, not worker assignments.

## Standing fences

- R24/R5 remain frozen and unusable.
- SV118046/D17.428's omitted predecessor-seam route remains fenced.
- R1029 forbids inferring a prescribed far-wall endpoint from D17.430 alone.
- D17.380's special-P5-order and changed-turn warnings remain in force.
- D17.437's COMMON `F intersect J` transition alternative remains live until explicitly excluded.
- R1032 forbids treating raw sharp counts, physical `F/J`, the source P5, or global edge-order integrability as sufficient closure data.
- R1034 further forbids treating the displayed static D17.391 spectator-gate conclusions as sufficient closure data.
- The R1033 certificate concerns insertion into the displayed `B` order; the D17.421 `B-B` side is not automatically adjacent in that order.
- The provisional source-P5 endpoint strengthening does not permit prescribing which source spoke is an endpoint.
- Matching cardinality is not a physical path cover, numerical improvement is not automatically global descent, and arbitrary reversal of a long path is not free.

O6 remains an independent foundational recovery front.

## What should change after the next wave

A useful next wave should do one of four things:

1. prove the first exact coordinate bridge between R1033 and the canonical augmenter / first-loss chain;
2. close O4 through a minimality-based three-cover-to-two-cover splice;
3. identify a small exact residual obstruction to either parent theorem; or
4. extend R1034 through a substantial part of the actual D17.409-421 provenance, thereby proving that an even later canonical ingredient is indispensable.

Another static gate lemma is not progress on the current frontier.
