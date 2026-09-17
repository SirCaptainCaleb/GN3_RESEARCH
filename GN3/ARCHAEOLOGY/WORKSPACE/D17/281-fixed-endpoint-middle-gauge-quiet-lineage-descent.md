# Completed endpoint capture is middle-invariant, so the quiet R172 clock descends on a fixed endpoint pair

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-middle-gauge-quiet-lineage-descent`

**Summary:** Fix an unordered endpoint pair E={a,c}. Define A_E to consist of physical endpoints e in E for which some earlier selected-incidence episode, at any admissible middle, completed the R434 protected return to an E-aligned both-singleton floor with e retained as its signed singleton coordinate. This ledger is independent of the middle: if e is already in A_E and a later admissible middle b' is used, the new R434 predecessor/successor channel anchored at e creates a nontrivial signed dimer containing the same historical singleton anchor e; R436 therefore gives an at-anchor nonquiet output, regardless of which middle created the old completion. If e is fresh, the ordinary R434 protected continuation either exits nonquietly or returns and adds e to A_E. Thus switching between admissible middles at an aligned E-floor costs no endpoint budget and cannot reset a completed endpoint. Consequently the R172 quiet-lineage proof generalizes verbatim to the fixed endpoint pair: with Psi_E=(2-|A_E|,M-2,delta_E), R415 strictly lowers mass above the floor, R432 strictly lowers target distance at a misaligned mass-two floor, and every quiet aligned episode at any chosen admissible middle strictly enlarges A_E. Hence every quiet, nonclosing, nonexit macro preserving E strictly lowers Psi_E even when the middle changes arbitrarily between aligned checkpoints. In particular, when A_E=E no admissible middle can support another quiet selected-incidence episode. This is a middle-rebasing/fully-anchored no-quiet theorem, not yet a consumer of the explicit R436 geometry.


### 1. Endpoint completion is physical, not middle-labelled

Fix an unordered physical endpoint pair

  E={a,c}.

A completed selected-incidence episode at endpoint e in E means the exact R434 event, but we now forget the middle that produced it: some proper tight turn J_b with outer pair E was used at an E-aligned both-singleton floor; its selected-incidence channel produced an e-anchored signed dimer; that birth was immediately designated R42-protected; and the quiet branch of the R427/R428/R433 return reached another E-aligned both-singleton floor with e itself retained as the signed singleton coordinate. Retain the complete historical certificate stack.

Define A_E subseteq E to be the set of endpoints admitting such a completed certificate, regardless of the middle b at which the episode occurred.

This is more than a change of notation. We prove that the completed certificate can be spent against every later admissible middle on the same endpoint pair.

### 2. Middle-independent replay obstruction

Suppose e belongs to A_E. At a later E-aligned floor choose any exact pair-deletion frame

  H-E = U | V

and any proper tight turn J_{b'} whose outer pair is E and whose middle b' is internal in that frame. Orient the two outer labels so that J_{b'}=(a',b',c') is tight, with {a',c'}=E.

Use either selected-incidence channel at b' which is anchored at the physical endpoint e. The proof mechanism of accepted R434 is local to the current frame: a selected predecessor of b' yields an endpoint-anchored signed dimer at the left outer endpoint, and a selected successor yields the dual dimer at the right outer endpoint. Hence the chosen e-channel produces, unless H has already closed during actualization, a nontrivial graph-intrinsic signed dimer

  D_e

whose signed anchor is the physical vertex e.

The old completed A_E certificate retained a historical signed singleton support (e). The new path D_e contains that same signed anchor e and has order two. Apply accepted R436 with the old signed singleton as the historical support and D_e as the later proper path. The away-anchor branch is impossible because D_e contains e, and the exact-singleton stationary-replay exception is irrelevant because the later object is the new nontrivial dimer. Thus R436 gives an explicit at-anchor output: path growth, later-path growth, a proper cycle, or reverse-contact/reversal geometry.

Crucially, this argument never uses the old middle b. It uses only:
- the physical endpoint e;
- its completed protected signed-singleton certificate;
- the new e-anchored dimer from the current middle b'.

Therefore

  COMPLETED ENDPOINT e IS SPENT AGAINST EVERY FUTURE ADMISSIBLE MIDDLE ON E.   (ME.1)

A middle change cannot make a completed endpoint quiet again.

### 3. Fresh endpoints complete exactly as in R434

If the current e-channel has e not in A_E, run the ordinary R434 protected-return protocol. The proof is unchanged by our endpoint-pair bookkeeping. Immediately protect e by R42, run R427, use R428 if the opposite support reaches singleton width first, and in the quiet arm obtain the singleton (e). Then R433 restores the other member of E while preserving (e).

Hence every quiet completed episode at any admissible middle returns to an E-aligned floor and strictly enlarges A_E by e. Any failure of that protected return is an explicit nonquiet first-contact/output.

Thus the two-element budget is global over the family of admissible middles:

  each quiet aligned episode spends one fresh physical endpoint of E,
  and a spent endpoint stays spent under every middle switch.                (ME.2)

### 4. Middle rebasing at an aligned checkpoint is rank-neutral

At an E-aligned both-singleton floor the active pair has mass M=2 and singleton set S=E. Replacing the proof coordinate J_b by another admissible J_{b'} does not modify the active pair, its ancestry, the exact target endpoint pair, or any completed endpoint certificate. Therefore

  A_E, M, S, and delta_E

are literally unchanged by the rebase. No representative surgery is being asserted: the turns are graph-intrinsic certificates available over the same aligned pair-deletion data, and the lineage simply chooses which admissible selected-incidence frame to inspect next.

So the middle is a gauge coordinate at aligned macro boundaries.

### 5. An admissible middle is always available in the live counterexample range

At any E-aligned floor, accepted R429 supplies an exact cover H-E=U|V with both rails nontrivial. Accepted R533 gives n>10. If |U|=r and |V|=s, then r+s=n-2 and the number of rail-internal vertices is

  (r-2)+(s-2)=n-6>0.

Choose any internal vertex b. By R3 exactly one orientation of the outer pair gives a tight turn on {a,b,c}; hence after possibly swapping the order of the two outer labels there is a proper tight turn J_b with outer set E and internal middle b. Thus the fixed-endpoint continuation never runs out of an admissible middle merely because the previous one was abandoned.

### 6. Fixed-endpoint quiet-lineage lex descent

Define

  epsilon_E = 2-|A_E|.

Let M be the active ancestry-bearing balanced-pair mass. For M>2 set delta_E=0. For M=2 with singleton floor S set

  delta_E = 2-|S intersect E|.

Set

  Psi_E = (epsilon_E, M-2, delta_E)

in ordinary lexicographic order.

Now repeat the proof mechanism of accepted R172, but allow the middle to change between aligned checkpoints.

**Above floor, M>2.** Use accepted R415. Every quiet nonclosing macro ending at the first strict mass decrease preserves the retained ancestry, hence cannot delete a completed A_E certificate. Therefore epsilon_E does not increase, while M strictly decreases unless epsilon_E has already fallen first. So Psi_E strictly decreases.

**Misaligned floor, M=2 and S != E.** Use accepted R432 with fixed target E. Every nonclosing replacement macro preserves the ancestry ledger and increases |S intersect E| by one. Hence epsilon_E does not increase and delta_E strictly decreases. So Psi_E strictly decreases.

**Aligned floor, M=2 and S=E.** Choose any admissible middle. By Sections 2-3, a quiet episode must use an endpoint e not yet in A_E, and a completed quiet return adds e to A_E. Thus epsilon_E strictly decreases. If e was already completed, the episode is nonquiet by (ME.1), independent of which middle produced the old certificate.

These regimes exhaust the same macro boundaries as R172. Consequently

  EVERY QUIET NONCLOSING NONEXIT FIXED-E CONTINUATION,
  EVEN WITH ARBITRARY MIDDLE CHANGES AT ALIGNED CHECKPOINTS,
  STRICTLY DECREASES Psi_E.                               (ME.3)

Ordinary lexicographic order on N^3 is well founded. Therefore no infinite quiet recurrence is possible while the physical endpoint pair E is retained, even if the middle vertex is repeatedly rebased.

### 7. Fully anchored consequence and exact remaining obstruction

If A_E=E, then epsilon_E=0 and every endpoint is already spent. At any E-aligned checkpoint, every admissible middle has a predecessor and successor channel, and whichever endpoint channel is tested is already completed. By (ME.1) it is immediately nonquiet. Hence

  FULLY ANCHORED E => NO QUIET SELECTED-INCIDENCE EPISODE AT ANY MIDDLE.       (ME.4)

This is the local fully-anchored collapse of quiet recurrence.

The theorem does **not** consume the resulting R436 growth/cycle/reversal geometry and therefore does not yet prove that every explicit phase-0 curvature excursion returns to a smaller Psi_E. That is now the exact residual G21 problem. What has been removed is the middle-reset obstruction itself: a curvature return through R1022 may choose a new middle on the old endpoint pair without resetting A_E or the numerical clock.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R415"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R432"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R436"
    },
    {
        "relation": "dependency",
        "revision_id": "R533"
    }
]
```