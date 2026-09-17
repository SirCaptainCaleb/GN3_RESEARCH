# The endpoint-spoke pair residue has no quiet state

**Workspace:** D17
**State:** established
**Key:** `three-spoke-xz-pair-residue-static-extinction`

**Summary:** Retain the three-spoke P5 K=(x,a,y,c,z), W=H-K, and any exact two-cover F of H-{x,z}. R560 forces at least two maximal W-blocks. If there are at least three, R159 fires against an at-most-two cover of W. Otherwise there are exactly two W-blocks and the exact conservation p+tau=3 leaves only tau=1,2,3. The tau=3 cell is consumed by restoring x at the exposed a-endpoint and z at the exposed c-endpoint: failed seams give source-pinned P4/R523 packets, while two successful restorations give H-z and H-x rows with identical trim F and the corrected common-residue endpoint-attachment theorem gives TWO-COVER because the successful endpoint attachments occur at distinct physical endpoints a,c. Tau=2 is consumed similarly according to its unique selected S-S state; the skip a-c is replaced by a-x-c and a-z-c, while source-edge cells use one automatic insertion and one W-boundary seam test. Tau=1 has the contiguous source trimer (a,y,c); x or z restores automatically on one end and the other requires one boundary seam, whose failure is R523. Thus every exact H-{x,z} cover yields TWO-COVER, R159 geometry, R435 geometry, a literal source-pinned P4, or an R523 same-dimer collision. There is no quiet x/z pair-residue state.

### 1. Source packet and endpoint-spoke pair residue
Retain the G30 three-spoke source packet

  K=(x,a,y,c,z),
  W=V(H)-V(K),

including the source turns (a,x,c),(a,y,c),(a,z,c). Let

  F

be an arbitrary exact two-cover of H-{x,z}. Put S={a,y,c}.

### 2. Block reduction
The source P5 K is a one-path absorber on {x,z} union S. By the exact reduction SV91906, R560 forces at least two maximal W-blocks in F. If there are at least three, those W-blocks give a literal at-least-three-path cover of H[W], while smallest-counterexample minimality gives an at-most-two cover; R159 produces a graph-intrinsic balanced opposite-sign pair.

Hence outside R159 geometry F has exactly two maximal W-blocks. If p is the number of selected S-S states and tau the number of selected S-W transitions, the exact two-path conservation identity is

  p+tau=3.

Since R508 gives tau>=1, only tau=1,2,3 remain.

### 3. The three finite cells
The tau=3 cell is consumed by SV92282. R429 forces the contracted support shape S_i-W_1-S_j | S_k-W_2, so the physical outer source vertices a,c are endpoints. Attempt to restore x at a and z at c. Every failed local seam reverses by R3 into either a literal P4 or an R523 collision against a retained source turn. If both restorations succeed, they give exact H-z and H-x rows whose exchanged-root trims are literally the same F; SV93413 gives TWO-COVER; its R407 same-end branch is impossible because the successful root attachments occur at distinct physical base endpoints a and c.

The tau=2 cell is consumed by SV92659. There is exactly one selected S-S state. Reverse source order is already R435 geometry. A selected skip a->c is replaced directly by a->x->c and a->z->c. A selected source edge a->y or y->c makes one root insertion source-certified; the other root needs only its W-side seam tests, and every failed test reverses into source-pinned P4/R523 geometry. Successful restorations give R159 whenever an inserted root is internal; if both are endpoints they attach at distinct a,c and commute to TWO-COVER.

The tau=1 cell is consumed by SV92660. R560 makes S one contiguous Hamilton trimer block; outside R435 it is literally (a,y,c). In either orientation relative to the unique W-block, one endpoint root restores automatically through the source P5 seam (x,a,y) or (y,c,z). The other root requires one W-boundary seam. Failure gives an R523 collision on the corresponding source boundary dimer; success gives the second singleton row, and the root inserted between the source trimer and the nonempty W-block is internal, so SV93413 gives R159.

### 4. Static extinction theorem
Therefore every exact two-cover F of H-{x,z} has at least one of the following source-visible outcomes:

1. TWO-COVER of H;
2. an R159 balanced opposite-sign pair from W-block component drop;
3. R435 adjacent-reversal/reverse-trimer/proper-cycle geometry;
4. a literal proper P4 pinned to one of the source endpoint spokes x or z;
5. an R523 same-oriented collision pinned to a source endpoint-spoke boundary dimer.

In particular there is no quiet combinatorial state of the endpoint-spoke pair residue. The theorem is static: it uses one common source K, one actual pair-deletion representative F, and direct root restoration. No R514/R428 payment, R1022 return, generation ledger, or anti-replay potential is used.

### 5. Scope
The output alphabet is not yet reduced to TWO-COVER. R159/R435/P4/R523 remain physical source-pinned outputs to be consumed by the middle-spoke y and the rest of the common-parent packet. The theorem is asymmetric in x,z versus y because its insertion proof uses the actual source P5 seams (x,a,y) and (y,c,z); no automatic relabelling to arbitrary spoke pairs is claimed. R24 and R5 are unused.

## References

```json
[
]
```
