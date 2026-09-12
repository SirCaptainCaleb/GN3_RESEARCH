# Every Arm-U P4/P5 endpoint repair reenters the phased Morse system strictly below its source checkpoint

**Workspace:** D17
**State:** established
**Key:** `universal-source-p4p5-source-relative-morse-reentry`

**Summary:** Retain the Arm-U source forest F_src=P_q|B|{q} and put M=max(|P_q|,|B|). In the bad-endpoint/bad-middle-test branch of SV51542, the order-free five-cell compiler produces a literal repaired maximum forest F_rep with rail profile {4,a-2,b-1} or {5,a-2,b-2}. Let L be its largest rail order. If L>M, then its forest-phase rank (1,n-L) is already strictly below the source checkpoint (1,n-M); this can occur only in the small source range M<=4 and is immediate progress. Otherwise L<=M. Mark any largest rail A of F_rep and run the chosen greedy A-growth continuation of SV40879. Every slide raises |A| by one. If a two-cover occurs, close. If |A| ever reaches M+1, the current forest-phase rank is (1,n-|A|)<(1,n-M). If instead A-growth terminates while |A|<=M, SV40879 gives its certified terminal balanced-pair birth and SV41376 enters phase 0, whose rank is automatically below the phase-1 source checkpoint regardless of the payment coordinates. Thus every P4/P5 endpoint repair has a finite certificate-retaining continuation to TWO-COVER or genuine phased-Morse reentry below the original Arm-U source forest. No M>=6 assumption is needed. Consequently the entire good-bad Arm-U endpoint branch reduces at all orders to a universal one-extension four-core or strict source-relative Morse progress; together with the good-good endpoint router, Arm U reduces to fixed-complement R435 curvature, universal four-core, or genuine Morse descent. This does not transfer to Arm-M completed-anchor curvature, whose pre-curvature checkpoint may already lie in phase 0.

### 1. Source checkpoint
Retain the Arm-U setup and notation of SV51542. Thus

  V(H)=Omega disjoint_union V(B),
  P_q a Hamilton puncture path on Omega-q,
  a=|P_q|,
  b=|B|,
  M=max(a,b).                                             (MR.1)

Restore the good source label q as a singleton. The literal source state is

  F_src=P_q | B | {q}.                                    (MR.2)

Choose one of P_q,B of order M as the marked largest rail. In the forest phase of the phased potential SV41376 its checkpoint rank is

  Phi_src=(1,d_src)=(1,|V(H)|-M).                         (MR.3)

This is the relevant pre-curvature checkpoint for the present Arm-U argument. The source-local endpoint test and the P4/P5 repair of SV51542 occur BEFORE any signed-pair payment phase is entered.

### 2. Exact repaired-forest profiles
Suppose the good-bad endpoint branch of SV51542 avoids its universal four-core output. Then the bad middle-p test gives a bridge trimer, and SV49328 with the two physical endpoints of B yields one of two literal spanning three-forests.

The P4 branch has rail orders

  {4,a-2,b-1}.                                            (MR.4)

The P5 branch has rail orders

  {5,a-2,b-2}.                                            (MR.5)

Write F_rep for the resulting literal maximum three-forest and

  L=max rail order of F_rep.                              (MR.6)

Because a,b>=3, all complementary rails displayed in SV51542 are nonempty tight paths. Hence F_rep is a genuine current maximum-three-forest state, not merely a support partition.

No lower bound such as M>=6 is needed from this point onward.

### 3. If the repair already exceeds the old source maximum, reentry is immediate
If

  L>M,                                                    (MR.7)

mark a largest rail A of F_rep. Its forest-phase rank is

  Phi_rep=(1,|V(H)|-L).                                   (MR.8)

Since L>M,

  Phi_rep < Phi_src                                       (MR.9)

in the lexicographic order of SV41376. Thus the repaired forest itself is already a strict phased-Morse reentry below the source checkpoint.

The displayed profiles show that this exceptional numerical direction can occur only in the small source range M<=4. Whenever it occurs, the repaired forest is already below the source checkpoint, so it is progress rather than a defect.

Hence assume from now on

  L<=M.                                                   (MR.10)

### 4. Normalize the repaired forest only until it beats the old checkpoint
Mark any largest rail A of F_rep, so |A|=L, and run the chosen greedy inward-endpoint A-growth continuation of SV40879. Every successful A-growth move is a literal one-edge SLIDE and satisfies

  |A| -> |A|+1,                                           (MR.11)

while preserving the physical descendant of the marked rail.

We stop this continuation at the FIRST occurrence of one of the following events.

**CLOSE.** A move merges away a component and H has a spanning two-cover.

**OVERSHOOT.** The marked rail reaches order M+1.

**TERMINAL.** No inward endpoint A-growth move remains while |A|<=M.

Because |A| strictly increases at every slide, this chosen continuation is finite until one of these events occurs.

### 5. Overshoot is strict forest-phase reentry
In the OVERSHOOT event, at the first state with |A|=M+1 we have

  Phi=(1,|V(H)|-(M+1)).                                   (MR.12)

Therefore

  Phi < (1,|V(H)|-M)=Phi_src.                             (MR.13)

We may stop immediately. No assertion about subsequent A-growth or confluence is needed.

Notice the direction: the repaired P4/P5 forest may initially have a SMALLER largest rail than the source forest, which by itself is not Morse progress. The chosen A-growth simply uses that forest as a valley. Once the marked rail grows past the old source maximum, the ordinary forest coordinate has genuinely passed below the old checkpoint.

### 6. Terminal before overshoot drops the phase coordinate
Suppose instead the A-growth continuation reaches a nonclosing terminal forest F* with

  |A*|<=M.                                                (MR.14)

SV40879 applies exactly at this terminal state. It proves |A*|>=3 and produces a genuine certificate-bearing balanced-pair birth:

- for |A*|=3, the rooted component-drop construction gives a singleton+dimer pair;
- for |A*|>=4, the two reverse boundary dimers of A* give the mass-four opposite-sign pair.

Choose the proper turn J required by SV41376 and enter the fixed-J payment lineage. The phased rank changes from forest phase 1 to payment phase 0:

  (1, |V(H)|-|A*|)
      ->
  (0, epsilon_J, M_pair-2, delta_J).                      (MR.15)

The first coordinate alone gives

  (0, epsilon_J, M_pair-2, delta_J)
    < Phi_src=(1,|V(H)|-M),                               (MR.16)

regardless of the numerical payment coordinates and regardless of whether |A*| is smaller than, equal to, or larger than the original source rail before terminality.

Thus terminalization of the repaired forest is also genuine reentry below the source checkpoint.

### 7. All-order source-relative reentry theorem
Combining Sections 3-6 gives:

> ARM-U ENDPOINT-REPAIR REENTRY. Let F_src=P_q|B|{q} be any Arm-U source forest and let M=max(|P_q|,|B|). If the good-bad endpoint/bad-middle branch of SV51542 emits its P4 or P5 repaired maximum forest, then there is a finite chosen certificate-retaining continuation yielding either
>
> 1. a spanning two-cover of H, or
> 2. a marked forest/pair state whose SV41376 phased rank is strictly below the source checkpoint Phi_src=(1,n-M).
>
> No hypothesis M>=6 is needed.

The continuation is explicit: if the repaired largest rail already exceeds M, stop; otherwise greedily A-grow one marked largest rail until it either exceeds M or reaches its certified terminal pair birth.

### 8. Consequence for the full Arm-U endpoint router
Return to an arbitrary good source label q and actual puncture path P_q.

- If both puncture endpoints are good, SV48242 gives fixed-complement R435 geometry by accepted R966.
- If some endpoint is bad and the middle-p test of SV51542 is tight, there is a universally one-vertex Hamilton-extendable four-core.
- If some endpoint is bad and that test is bad, Sections 1-7 consume the P4/P5 repair into TWO-COVER or genuine source-relative phased-Morse reentry.

Therefore Arm U has the all-order parent compression

  FIXED-COMPLEMENT R435 CURVATURE,
  OR UNIVERSAL FOUR-CORE,
  OR TWO-COVER / STRICT PHASED-MORSE REENTRY.              (MR.17)

In particular the two-probe wall, parity-leakage matching, and bounded double-defect nucleus are not terminal parent obstructions. They remain valid structural certificates but are bypassed by the stronger endpoint middle-p test plus five-cell repair.

### 9. Why this does not settle the Arm-M G18 checkpoint
The proof is deliberately SOURCE-RELATIVE. Its pre-curvature checkpoint (MR.3) lies in forest phase 1 because the Arm-U curvature is extracted directly from the literal source forest before payment.

The completed-anchor Arm-M curvature targeted by G18 can be born downstream of a phase-0 payment checkpoint. Returning from such a curvature cell to any ordinary forest state has phase coordinate 1 and is therefore NOT automatically below its pre-curvature phase-0 checkpoint. This is exactly why SV49597's one-step transverse cap return still needs a downstream checkpoint comparison.

Thus the present theorem genuinely closes the regrowth objection on the Arm-U stress test without smuggling the same argument into Arm M where its phase ordering is wrong.

Status: complete internal working mathematics, unreviewed exposition. The only unresolved Arm-U parent outputs are now fixed-complement R435 curvature and the universal one-extension four-core; the P4/P5 local-dip branch has genuine source-relative Morse cancellation.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```