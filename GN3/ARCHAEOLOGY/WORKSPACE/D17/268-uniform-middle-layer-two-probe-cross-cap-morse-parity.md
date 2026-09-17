# Equal cross-cap probe parity gives strict Morse descent; mixed parity is a rigid twist

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-two-probe-cross-cap-morse-parity`

**Summary:** In the Arm-M pair-deletion wall SV42382, test tau_u=(a0,u,a_{k-1}) for the two deleted probes u=x,y. If tau_x,tau_y have the same status, accepted R584 converts the two common bridges, or their R3 reversals, into a literal cross-end P5 or P4 whose complement is exactly two retained rails; for k>=6 the resulting spanning maximum three-forest has largest rail at most k-1, a strict descent from the original cap height k. If the two tests have opposite status, one gets the rigid mixed twist (a0,x,a_{k-1}) and (a_{k-1},y,a0) tight, together with the four endpoint-wall turns. Importantly, direct R435 comparison of the reverse cross-cap trimer with A is sterile: both seam tests are already bad because their R3 reverses are exactly the known boundary-wall trimers. Thus equal parity is fully consumed into strict Morse descent, while mixed parity is isolated as the sole genuine two-probe residue and cannot be relabelled as new Reverse-Ear progress.


### 1. Input: one common two-probe wall at both ends of the cap
Assume the Arm-M pair-deletion wall of SV42382. Thus

  H-{x,y}=A|B,
  A=(a_0,a_1,...,a_{k-1}),
  |A|=k, |B|=k-1,

and, for both probes u in {x,y},

  (a_1,a_0,u) tight,                                      (MP.1)
  (u,a_{k-1},a_{k-2}) tight.                              (MP.2)

Work in the live range k>=6. Put

  L=a_0,  R=a_{k-1}.

For each u in {x,y} test the single CROSS-CAP turn

  tau_u=(L,u,R).                                           (MP.3)

The two bits tau_x,tau_y give a complete parity split.

### 2. Both cross-cap tests tight: an explicit P5 with a two-rail complement
Assume

  (L,x,R) tight,
  (L,y,R) tight.                                          (MP.4)

Apply accepted R584 with A=L and C=R. It yields one of the two tight P4s

  (L,x,R,y),
  (L,y,R,x).                                              (MP.5)

Let the first case hold; the second is symmetric. By (MP.1) for x,

  (a_1,L,x)

is tight, so

  S=(a_1,L,x,R,y)                                         (MP.6)

is a literal vertex-simple tight P5.

Its complement is exactly the two literal paths

  A[2,k-2]=(a_2,a_3,...,a_{k-2}),
  B.                                                       (MP.7)

Therefore

  S | A[2,k-2] | B                                        (MP.8)

is a literal spanning three-path cover, hence a maximum three-forest by accepted R4. The rail orders are

  5, k-3, k-1.                                            (MP.9)

For k>=6 their maximum is k-1. Thus the largest-rail height strictly falls from k.

### 3. Both cross-cap tests bad: reversal plus R584 gives an even shorter descent
Assume both tau_x and tau_y are bad. Accepted R3 gives

  (R,x,L) tight,
  (R,y,L) tight.                                          (MP.10)

Apply accepted R584 with A=R and C=L. One of

  K=(R,x,L,y),
  K'=(R,y,L,x)                                            (MP.11)

is a literal tight P4.

For either choice, the complement is exactly

  A[1,k-2] | B,                                           (MP.12)

so

  K | A[1,k-2] | B                                        (MP.13)

(or the K' version) is a literal spanning maximum three-forest. Its rail orders are

  4, k-2, k-1,                                            (MP.14)

whose maximum is k-1. This is again strict largest-rail descent.

### 4. Mixed parity: the surviving two-probe twist
It remains that exactly one cross-cap test is tight. Relabel so

  (L,x,R) tight,
  (L,y,R) bad.                                            (MP.15)

R3 gives

  (R,y,L) tight.                                          (MP.16)

Thus the common two-probe wall has compressed to the literal mixed twist

  (a_1,L,x), (a_1,L,y),
  (L,x,R), (R,y,L),
  (x,R,a_{k-2}), (y,R,a_{k-2})                            (MP.17)

all tight.

There is an important NON-PROGRESS fact. Comparing the reverse cross-cap trimer

  E=(R,y,L)

with the ancestral cap path A by accepted R435 does not automatically produce new long curvature. The two seam tests in the R435 proof are

  (a_{k-2},R,y),
  (y,L,a_1).                                              (MP.18)

But their exact reverses are respectively

  (y,R,a_{k-2}),
  (a_1,L,y),                                              (MP.19)

and both are already tight by the original wall (MP.1)-(MP.2). Hence R3 makes both seam tests in (MP.18) bad. R435 therefore simply returns the already-known boundary reverse trimers; it need not create a proper cycle or any new nonlocal cell.

So the mixed branch must not be counted as fresh Reverse-Ear progress. Its actual retained datum is the six-turn twist (MP.17): one probe crosses the cap in the forward cross-cap sense, while the other crosses in the reverse sense, and both still sign the same two reverse boundary dimers.

### 5. Exact Morse consequence and remaining target
Combining Sections 2-4:

> In every Arm-M pair-deletion frame of SV42382 with k>=6, equal cross-cap parity of the two deleted probes gives an explicit strict largest-rail Morse descent from height k to height at most k-1. Therefore any frame that resists this descent must have mixed cross-cap parity.

Equivalently, the entire two-probe obstruction has been reduced to one order-sensitive mixed twist. This is a same-parent statement: no R526/R527 descendant coexistence, payment, or representative synchronization is used. The third witnesses b_0,b_{k-2} are not needed for the equal-parity descent.

The remaining problem is now precise: consume (MP.17). Generic R435 on E is sterile for the reason above, so a successful consumer must spend the simultaneous good and bad probe geometry, the third witnesses, or a genuinely global Arm-M constraint. This correction is essential; the mixed branch is not being exported as an already-new curvature portal.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R584"
    }
]
```