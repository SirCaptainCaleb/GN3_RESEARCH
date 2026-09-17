# Every forest-phase proper-path portal reenters below its birth checkpoint; Arm U curvature is source-relative cancellable

**Workspace:** D17
**State:** established
**Key:** `forest-phase-path-portal-threshold-reentry`

**Summary:** Let F0 be any marked maximum three-forest checkpoint in phase 1, with largest marked rail order M and phased rank Phi0=(1,n-M). Suppose a portal born at this checkpoint supplies any graph-intrinsic proper tight path K; a proper tight cycle counts after choosing any cyclic break. Accepted R4 currentizes K as a literal rail of some maximum forest G=K|U|V. Mark a largest rail of G, of order L. If L>M, G already has phase-1 rank below Phi0. If L<=M, run the chosen largest-rail A-growth of SV40879. If it closes H, stop. If the marked rail reaches M+1, its phase-1 rank is below Phi0. If A-growth terminates before that, SV40879 births a certified balanced pair and SV41376 enters phase 0, automatically below the phase-1 birth checkpoint regardless of payment coordinates. Thus every proper-path portal born in forest phase has a finite ancestry-retaining route to closure or strict phased-rank reentry below its birth checkpoint. Apply this to Arm U: every R435 output is a proper dimer, reverse trimer, or proper cycle break; every universal one-extension four-core contains a proper Hamilton P5 after adjoining any exterior vertex; and the P4/P5 endpoint-repair branch is already a literal maximum forest covered by SV52659. Therefore every Arm-U source-curvature output is source-relative rank-cancellable. The residual hard G18 problem is specifically curvature born at a phase-0 completed-anchor checkpoint, as in Arm M; there phase-1 currentization is not automatically below the birth rank.

### 1. A phase-1 birth checkpoint
Let H be a hypothetical smallest counterexample and let

  F_0=A|B|C                                                (FP.1)

be a literal maximum spanning three-forest. Mark A of maximum order and put

  M=|A|,
  Phi_0=(1,n-M),  n=|V(H)|.                               (FP.2)

This is a phase-1 checkpoint in the hybrid rank of SV41376.

Suppose some geometric portal born from the retained checkpoint data supplies a graph-intrinsic PROPER tight path K. The birth may be historical rather than simultaneously current; retain the exact portal ancestry together with K.

If the portal supplies a vertex-simple proper tight cycle instead, choose and retain any cyclic break. The resulting Hamilton path on the same proper support is a graph-intrinsic proper tight path, so it is included in the present setup.

### 2. Currentize the portal path
Accepted R4 applies to K. Its complement H-V(K) has exact path-cover number two, so choose one literal exact cover

  H-V(K)=U|V.                                              (FP.3)

Then

  G=K|U|V                                                  (FP.4)

is a literal current maximum spanning three-forest containing the portal path K as one physical rail.

Choose a largest rail D of G and write

  L=|D|.                                                   (FP.5)

No relation between the support of D and the old marked support A is assumed.

### 3. If currentization overshoots the birth height, reentry is immediate
If

  L>M,                                                     (FP.6)

then the forest-phase rank of the currentized state, marked on D, is

  Phi_G=(1,n-L)< (1,n-M)=Phi_0.                            (FP.7)

Thus the portal has already reentered below its birth checkpoint. Stop.

Hence assume L<=M.

### 4. Threshold-normalize the currentized forest
Starting from G, run the chosen greedy largest-rail A-growth continuation of SV40879 with D as the marked rail. Every successful inward endpoint SLIDE increases the marked physical descendant by exactly one vertex.

Stop at the first of three events.

**TWO-COVER.** A move closes H.

**THRESHOLD OVERSHOOT.** The marked rail first reaches order M+1.

**TERMINAL.** No marked-rail A-growth move remains while the marked rail has order at most M.

The process is finite because the marked rail order strictly increases at every nonclosing forest move.

In the THRESHOLD OVERSHOOT event the current rank is

  (1,n-(M+1)) < Phi_0.                                    (FP.8)

In the TERMINAL event, SV40879 supplies its genuine certificate-bearing balanced-pair birth. Choose the fixed turn required by SV41376 and enter the payment lineage. The phase coordinate drops

  1 -> 0.                                                 (FP.9)

Therefore the first phase-0 state satisfies

  (0,epsilon_J,M_pair-2,delta_J) < Phi_0                  (FP.10)

regardless of all trailing coordinates.

We have proved:

> FOREST-PHASE PATH-PORTAL ABSORPTION. Any proper graph-intrinsic tight path born as a portal from a retained phase-1 maximum-forest checkpoint has a finite certificate-retaining continuation to TWO-COVER or to a forest/pair state of phased rank strictly below that birth checkpoint. A proper tight cycle has the same conclusion after any cyclic break.

The proof is rank-aware but species-free: once a proper path is exposed, no additional local curvature taxonomy is needed.

### 5. Every R435 species is a proper-path portal
Accepted Reverse Ear R435 has exactly three nonquiet output types:

1. a reversed old adjacent state;
2. a tight reverse trimer;
3. a vertex-simple proper tight cycle.

The reversed state is a two-vertex tight path, the reverse trimer is a proper tight path, and the proper cycle yields a proper tight path after a cyclic break. Therefore every R435 output born in forest phase is absorbed by Sections 1-4.

This observation is stronger than merely saying R435 currentizes to maximum-forest dynamics: it compares the reentered state to the actual phase-1 checkpoint which emitted the curvature.

### 6. A universal one-extension four-core is also a proper-path portal
Suppose a forest-phase portal produces a four-set S such that

  S+y is Hamiltonian for every y outside S.                (FP.11)

In the applications below H has more than five vertices, so choose any y outside S for which S+y is proper in H. Retain one literal Hamilton P5 K_y on S+y.

Then K_y is a graph-intrinsic proper tight path. Sections 1-4 currentize it and force TWO-COVER or strict reentry below the same phase-1 birth checkpoint.

Thus, for rank cancellation of a forest-phase portal, a universal four-core does not need its full pair-core C3/C4 machinery. One Hamilton five-extension is enough.

### 7. Arm-U endpoint curvature is entirely forest-phase born
Return to the Arm-U fixed-universe/source setup. For a good source label q, the literal restored source forest is

  F_src=P_q|B|{q}.                                        (FP.12)

Choose a largest source rail of order

  M=max(|P_q|,|B|).                                       (FP.13)

The endpoint router and its refinements occur directly from this literal source representative, before any signed-pair payment. Hence their relevant birth checkpoint is the phase-1 state

  Phi_src=(1,n-M).                                        (FP.14)

There are now only the following cases.

**GOOD-GOOD ENDPOINT.** SV51259 uses accepted R966 and emits explicit fixed-complement R435 geometry among actual puncture paths. By Section 5, whichever R435 species fires is a proper-path portal, hence reenters strictly below Phi_src or closes H.

**GOOD-BAD, TIGHT MIDDLE TEST.** SV51542 produces a universally one-vertex Hamilton-extendable four-core. By Section 6, choose one exterior Hamilton P5 and absorb it below Phi_src.

**GOOD-BAD, BAD MIDDLE TEST.** SV51542/SV49328 produces a literal P4/P5 repaired maximum forest. SV52659 already proves directly that this branch reaches TWO-COVER or strict phased-Morse reentry below Phi_src at every order.

Therefore every endpoint-curvature branch of Arm U is source-relative cancellable.

### 8. All-order Arm-U source-curvature cancellation
We obtain the parent statement

> ARM-U SOURCE-CURVATURE CANCELLATION. Fix any Arm-U universally crossed source and any retained good puncture source forest F_src. The complete endpoint router has a finite certificate-retaining continuation to either
>
> 1. a spanning two-cover of H, or
> 2. a marked forest/pair state whose SV41376 phased rank is strictly below the source checkpoint Phi_src.
>
> In particular fixed-complement R435 curvature, universal four-core curvature, two-probe walls, parity leakage, and P4/P5 endpoint repairs are not independent terminal Arm-U obstructions.

The endpoint geometry is still useful because it tells us how curvature is physically born and preserves source ancestry. But once the birth checkpoint is known to lie in phase 1, any proper-path output is enough for strict rank-aware cancellation.

### 9. The G18 load-bearing hypothesis is phase of birth
The same argument must NOT be applied blindly to completed-anchor Arm-M curvature.

A completed-anchor R434/R436 exit can be born after the largest-rail forest has already terminated and the fixed-turn payment lineage has entered phase 0. Its pre-curvature checkpoint therefore has rank

  (0,epsilon_J,M_pair-2,delta_J).                          (FP.15)

Currentizing a trimer, cycle, dimer, P4, or P5 by R4 returns to forest phase 1. Since 1>0 in the hybrid order, no amount of merely observing that currentization exists proves reentry below (FP.15). One must compare the returned terminal/payment coordinates to the OLD phase-0 checkpoint, or find a direct phase-0 monotone.

This is precisely the distinction exposed by the Arm-U stress test:

  FOREST-PHASE CURVATURE: proper-path currentization is automatically cancellable;
  PAYMENT-PHASE CURVATURE: currentization alone is not rank progress.   (FP.16)

Hence the genuine G18 parent theorem should target PHASE-0 CURVATURE CANCELLATION, not curvature in the abstract.

Status: complete internal working mathematics, unreviewed exposition. No claim is made that the remaining Arm-M phase-0 cancellation is solved.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```