# A good-bad Arm-U endpoint is a one-edge transfer/cycle portal or the same bidirectional two-probe wall as Arm M

**Workspace:** D17
**State:** established
**Key:** `universal-source-goodbad-transfer-or-two-probe-wall`

**Summary:** Continue the good-bad endpoint branch of SV48242. Let q be good, let r be a bad endpoint of an actual puncture word P_q, put K=P_q-r, and retain the exact pair-deletion row H-{q,r}=K|B. The good label q already tail-signs the reverse initial dimer of B and head-signs its reverse terminal dimer. Test whether the bad endpoint r can be transferred from P_q to either end of B in the exact H-q fiber. If r prepends to B or appends to B, trimming r from P_q and attaching it to B gives an actual exact H-q cover; after adjoining singleton q this is a literal one-edge support-changing maximum-three-forest move from P_q|B|{q}. If both end attachments succeed, B+r is a proper tight cycle and its cyclic breaks give a current movable-break family with K and singleton q fixed. If an attachment fails, R3 makes r witness the corresponding reverse B-boundary dimer, alongside q. Therefore if BOTH attachments fail, the deleted pair {q,r} tail-signs the reverse initial dimer and head-signs the reverse terminal dimer of B: an exact bidirectional two-probe wall on the pair-deletion frame K|B. Thus outside an immediate support-changing/cycle portal, the mixed Arm-U good-bad cell has exactly the same two-deleted-probe wall skeleton that Arm M carries on every pair-deletion frame, although Arm M has additional third witnesses/uniformity. This identifies a genuine cross-arm G18 parent certificate. Working/unreviewed exposition only.


### 1. Input from the Arm-U endpoint router
Retain the GOOD-BAD branch of SV51259. Thus

  V(H)=Omega disjoint_union V(B),
  B=(b_0,b_1,...,b_t),

q is a GOOD deletion label, P_q is an actual Hamilton puncture path on Omega-q, and r is a BAD endpoint of P_q. Write, after duality if necessary,

  P_q=(r,p_1,p_2,...,p_m),
  K=(p_1,p_2,...,p_m).                                   (TW.1)

Then

  H-q       : P_q | B                                    (TW.2)

is an exact singleton-deletion source and

  H-{q,r}   : K | B                                      (TW.3)

is an exact pair-deletion cover.

From the good-source wall calculation of SV51259,

  (b_1,b_0,q) tight,
  (q,b_t,b_{t-1}) tight.                                 (TW.4)

Thus q tail-signs the reverse initial B-dimer and head-signs the reverse terminal B-dimer.

The badness of r additionally gives the inward K-boundary curvature

  (p_2,p_1,q) tight,                                     (TW.5)

but the present theorem will not need to spend it until after the B-boundary test.

### 2. Test transfer of the bad endpoint to the source end of B
Test the turn

  (r,b_0,b_1).                                           (TW.6)

If it is tight, then

  (r,B) | K                                               (TW.7)

is a literal two-cover of H-q. It is exact because H-q cannot be Hamiltonian in a smallest counterexample. Adjoining the omitted singleton q gives

  F_L=(r,B) | K | {q}.                                   (TW.8)

Compare this with the source maximum forest

  F_0=P_q | B | {q}.                                     (TW.9)

Since r is the first vertex of P_q, F_L is obtained from F_0 by deleting the one selected source edge r-p_1 and adding the one selected edge r-b_0. All other selected states are unchanged. Hence source-end transfer is a literal SUPPORT-CHANGING ONE-EDGE GENERATOR with the same physical singleton q fixed.

If (TW.6) is bad, R3 gives

  (b_1,b_0,r) tight.                                     (TW.10)

Together with (TW.4), the tested reverse initial dimer (b_1,b_0) then carries two distinct TAIL witnesses q and r. Accepted R523 identifies the exact same-oriented two-tail collision packet there.

### 3. Test transfer of the bad endpoint to the terminal end of B
Dually test

  (b_{t-1},b_t,r).                                       (TW.11)

If it is tight, then

  B-r := (B,r)

is a tight path on B+r and

  F_R=K | (B,r) | {q}                                    (TW.12)

is another literal maximum forest. Relative to F_0 it deletes the same old source edge r-p_1 and adds the one selected edge b_t-r. Thus it is again a support-changing one-edge generator preserving singleton q.

If (TW.11) is bad, R3 gives

  (r,b_t,b_{t-1}) tight.                                 (TW.13)

Together with (TW.4), the tested reverse terminal dimer (b_t,b_{t-1}) carries two distinct HEAD witnesses q and r, hence the corresponding R523 two-head collision packet.

The right-endpoint version P_q=(...,p_{m-1},r) is exact by reversing the roles of the source and terminal edge removed from P_q; the conclusions on B are unchanged.

### 4. Two successful transfers are already a current cycle portal
If both (TW.6) and (TW.11) are tight, then every consecutive turn of the closed word

  (r,b_0,b_1,...,b_t,r)                                  (TW.14)

is tight: the internal turns are those of B and the two boundary turns are exactly (TW.6) and (TW.11). Hence B+r is a proper vertex-simple tight cycle.

Its complement is K union {q}. The literal paths K and singleton {q} cover that complement, so every cyclic break of B+r gives a literal maximum spanning three-forest with K and {q} fixed. Thus the double-transfer branch is already a CLOSED MOVABLE-BREAK CURRENT PORTAL, not a static Arm-U obstruction.

### 5. Portal-free residue is a bidirectional two-probe wall
Suppose neither endpoint transfer succeeds. Then (TW.10) and (TW.13) both hold. Combining with q's wall signs (TW.4), the exact pair-deletion frame

  H-{q,r}=K|B                                             (TW.15)

has the following symmetric deleted-probe packet:

  (b_1,b_0,q),   (b_1,b_0,r) tight,                      (TW.16)
  (q,b_t,b_{t-1}),   (r,b_t,b_{t-1}) tight.              (TW.17)

Equivalently, BOTH deleted vertices q,r tail-sign the reverse initial B-dimer and BOTH head-sign the reverse terminal B-dimer.

Call (TW.15)-(TW.17) the BIDIRECTIONAL TWO-PROBE WALL on B. It is an actual pair-deletion representative with physical probe labels and tested dimer orders retained. The bad-endpoint curvature (TW.5) remains additional ancestry on the opposite rail K.

Therefore every Arm-U good-bad endpoint cell satisfies the exact trichotomy

  ONE-EDGE SUPPORT TRANSFER,
  or CLOSED TIGHT-CYCLE PORTAL,
  or BIDIRECTIONAL TWO-PROBE WALL.                        (TW.18)

The first two branches are current representative dynamics. Only the third is portal-free.

### 6. Cross-arm G18 identification
The portal-free object (TW.15)-(TW.17) is the same wall skeleton carried by Arm M. In the accepted R927 Arm-M pair-deletion setting, the current pair-deletion wall theorem shows that both deleted vertices sign both reverse boundary dimers of the k-rail in every exact pair-deletion frame; Arm M further supplies at least a third witness at each end and the uniform k/(k-1) size profile.

Arm U therefore does NOT require a separate parent notion once one spends the bad endpoint against the fixed complement. Its GOOD-BAD branch either enters support-changing maximum-forest dynamics immediately or lands in the common object

  EXACT PAIR-DELETION ROW
  + TWO DELETED PROBES
  + BIDIRECTIONAL REVERSE BOUNDARY WALL.                  (TW.19)

This is a stronger G18 common certificate than “historical singleton + curvature path”. It is current, representative-level, and survives the Arm-U stress test without deletion-Hamiltonicity of the whole active universe.

### 7. Exact remaining distinction
The theorem does not yet prove curvature cancellation. Arm M's wall comes with extra multiplicity: its opposite rail endpoints supply third same-polarity witnesses, and uniformity forbids all inward growth of the k-rail. The bare Arm-U two-probe wall need not have either property.

Thus the next parent theorem can be asked sharply:

  TWO-PROBE WALL CANCELLATION.
  Does an exact pair-deletion row A|B whose two deleted labels both tail-sign the reverse initial B-dimer and both head-sign the reverse terminal B-dimer force a two-cover or genuine rank-aware support escape once one also retains one ancestry-bearing boundary-curvature mark on A?

If YES, G18 is genuinely arm-independent. If NO, the counterexample should expose exactly which Arm-M strengthening is load-bearing, most plausibly the third-witness pressure of SV42382/SV44176 or the uniform no-growth profile.

Status: complete internal working mathematics, unreviewed exposition. No canonical certification or cancellation theorem is claimed.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```