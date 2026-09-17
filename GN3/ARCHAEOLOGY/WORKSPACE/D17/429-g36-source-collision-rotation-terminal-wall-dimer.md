# A source-gate collision rotates to the selected far dimer; without a P4 that far rail is exactly a dimer

**Workspace:** D17
**State:** established
**Key:** `g36-source-collision-rotation-terminal-wall-dimer`

**Summary:** Retain the G36 source-gate wall packet after SV115482 lands in its source-dimer collision branch. In the OUT orientation, with historical (A,t,C), source collision (A,t,b), wall turn (d,b,t), and selected far boundary b->d, one extra test of (b,t,C) either gives the literal P4 (d,b,t,C) or forces (C,t,b). If the four-set {A,t,b,C} has no P4, R516 is then forced into its exact 11 signature. Two tests against the selected far edge show that either a labelled P4 occurs or both (A,b,d) and (C,b,d) are tight, so the two anchor vertices become head witnesses on the actual selected far dimer (b,d). If that far rail continued beyond d, its next selected turn would concatenate with either anchor witness to a P4; hence in the no-P4 residue the far rail is exactly the dimer (b,d). The IN-dual gives a terminal selected dimer (d,b) carrying A,C as tail witnesses. Thus the non-P4 wall residue is a highly special anchor-saturated R542 geometry: the selected far dimer is a reverse terminal dimer of the wall trimer and its two witnesses are exactly the deleted source anchors, with complementary carrier singleton t. No payment is invoked.

### 1. Input: the G36 collision branch
Retain the source-gate wall packet of SV115482 and suppose its first R3 test lands in the source-dimer COLLISION branch rather than the displayed P4 branch. We show that this collision cannot remain on the source dimer unless a P4 already exists: it rotates onto the literal selected far-boundary dimer.

Treat the OUT orientation first. Thus the fixed far selected boundary is

  b -> d,                                                   (CR.1)

with b the fixed free-IN far endpoint, so b is the source of its current rail, and the persistent bad closing seam gives

  (d,b,t) tight.                                           (CR.2)

The historical source trimer is

  (A,t,C) tight,                                           (CR.3)

and the collision branch of SV115482 gives

  (A,t,b) tight.                                           (CR.4)

All five displayed vertices are physical vertices with the distinctness already required by the G36 packet.

### 2. One anchor test forces the exact R516 11-cell or a P4
Test

  (b,t,C).                                                 (CR.5)

If (CR.5) is tight, then (CR.2) and (CR.5) concatenate to the literal P4

  (d,b,t,C).                                               (CR.6)

Assume therefore that (CR.5) is bad. Boundary antisymmetry R3 gives

  (C,t,b) tight.                                           (CR.7)

Now inspect the four-set {A,t,b,C} using the tight trimer

  K=(A,t,b).                                               (CR.8)

On its left terminal dimer {A,t}, the fourth vertex C has the same tail polarity as the natural K-sign because (A,t,C) is tight. On its right terminal dimer {t,b}, C has the same head polarity as the natural K-sign because (C,t,b) is tight. Thus, if this four-set has any tight Hamilton P4, we are already in the desired P4 output. Otherwise R516 applies with

  a=A,  b_R=t,  c=b,  y=C,

and both alignment bits are 1. Hence the no-P4 cell is uniquely the exact R516 signature 11. In particular it contains the two tight turns

  (b,A,C),   (b,C,A).                                     (CR.9)

No other R516 row is compatible with the retained source turns.

### 3. The source collision rotates onto the actual selected far dimer
Test the two anchor turns against the far selected boundary:

  (d,b,A),   (d,b,C).                                     (CR.10)

If (d,b,A) is tight, then (CR.9) gives the P4

  (d,b,A,C).                                               (CR.11)

If (d,b,C) is tight, then (CR.9) gives the P4

  (d,b,C,A).                                               (CR.12)

Therefore, in the branch with no labelled P4, both turns in (CR.10) are bad. R3 gives their exact reversals

  (A,b,d),   (C,b,d) tight.                               (CR.13)

Thus the actual selected far dimer

  D_far=(b,d)                                              (CR.14)

now carries the two deleted source anchors A,C as distinct HEAD witnesses on one tested orientation. The collision has been transported from the source dimer to the selected wall dimer without anonymizing its ancestry.

### 4. No-P4 forces the far rail to be exactly the dimer
Because b is the free-IN far endpoint, it is the source of its current rail. Suppose the rail continued beyond d, with next selected edge

  d -> e.                                                   (CR.15)

Then tightness of the current rail gives

  (b,d,e) tight.                                           (CR.16)

Together with either anchor witness in (CR.13), for example (A,b,d), this gives the literal P4

  (A,b,d,e).                                               (CR.17)

Hence in the no-P4 branch d has no selected successor. The far component is literally the two-vertex rail

  (b,d).                                                    (CR.18)

This uses the actual current selected edge, not merely the physical support {b,d}.

### 5. Exact IN-dual
In the IN orientation of SV115482, the fixed far selected boundary is the reversal-dual d->b, with b the free-OUT terminal, and the retained packet is

  (A,t,C),  (b,t,C),  (t,b,d) tight.                      (CR.19)

Test (A,t,b). If it is tight, (A,t,b,d) is a literal P4. If it is bad, R3 gives (b,t,A). On the tight trimer (b,t,C) with fourth vertex A, the two retained source turns force the exact R516 signature 11 whenever no P4 exists. In that row the turns

  (C,A,b),   (A,C,b)                                      (CR.20)

are tight. Testing (A,b,d) and (C,b,d), any tight test concatenates with (CR.20) to a labelled P4; if both are bad, R3 gives

  (d,b,A),   (d,b,C) tight.                               (CR.21)

Thus D_far=(d,b) carries A,C as two TAIL witnesses. If the far rail had a predecessor e->d, then (e,d,b) together with either turn in (CR.21) would give a P4. Hence the no-P4 far rail is exactly the dimer (d,b).

### 6. The surviving packet is an anchor-saturated wall dimer
The residue after excluding labelled P4 outputs is therefore extremely rigid.

OUT: the wall trimer is (d,b,t), the current far component is exactly D_far=(b,d), and D_far has head witnesses A,C. Since (b,d) is the reverse initial terminal dimer (b,a) of the carrier (a,b,c)=(d,b,t), this is precisely the short-carrier geometry underlying R542, but with the two witnesses fixed to the deleted source anchors and with complementary carrier singleton t.

IN: the wall trimer is (t,b,d), the current far component is exactly D_far=(d,b), and D_far has tail witnesses A,C. Here (d,b) is the reverse final terminal dimer (c,b) of the same wall carrier, again with complementary singleton t and the witnesses exactly A,C.

This section does NOT invoke R542 payment/capture and does not claim closure. Its gain is packet-specific: a persistent source wall has only a P4 output or one terminal selected wall dimer saturated by both source anchors. The old gate orientation, source anchor identities, fixed-wall provenance, and current selected far-dimer orientation are all retained. R24, R5, payment, replay, and generic collision compilation are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R516"
    }
]
```
