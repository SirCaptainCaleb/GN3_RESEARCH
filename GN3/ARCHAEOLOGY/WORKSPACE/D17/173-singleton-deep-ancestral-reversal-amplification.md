# All q1q2 reversals except the source-q2 right shield amplify to labelled P4s

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-ancestral-reversal-amplification`

**Summary:** Both ancestral q1q2 eta failures amplify to labelled P4s: R700 on the reverse trimer with probes q0 and the opposite d/y label either gives P4 directly or tail-signs tested (q1,q2), which together with inherited head witness q0 gives a P4 by R523. Likewise, if the common right seam rho=(q1,q2,z) fails while q2 has an actual T-predecessor c, R700 on (z,q2,q1) with probes d,y either gives P4 or tail-signs the actual selected dimer (q2,z); the T-turn (c,q2,z) is the opposite head certificate, so R523 gives P4. The sole bare ancestral-reversal residue is therefore the source-q2 failed-rho cell, where no predecessor c exists.


Retain the second-block q2 insertion setup and accepted R700/P777, R523/P538. This section consumes the ancestral-reversal exits before generic payment.

### 1. Either eta failure is P4-valued
The ancestral source order contains

  (q_0,q_1,q_2) tight.                                    (AR.1)

Suppose eta_y=(y,q_1,q_2) is bad. R3 gives the tight trimer

  K_y=(q_2,q_1,y).                                        (AR.2)

Probe K_y by the two distinct outside vertices q_0 and d using accepted R700. If R700 takes its P4 branch, retain that labelled P4. Otherwise DUAL-CP tail-signs the reverse initial dimer (q_1,q_2) by both probes; in particular

  (q_1,q_2,d) tight.                                      (AR.3)

But (AR.1) is a head certificate on the SAME tested dimer (q_1,q_2), with distinct witness q_0. Accepted R523 therefore gives the literal P4

  (q_0,q_1,q_2,d).                                        (AR.4)

Thus eta_y failure is always P4-valued.

Dually, if eta_d=(d,q_1,q_2) is bad, the tight trimer K_d=(q_2,q_1,d) probed by q_0,y either gives an R700 P4 directly or forces

  (q_1,q_2,y) tight,

which together with (AR.1) gives the literal P4

  (q_0,q_1,q_2,y).                                        (AR.5)

Hence no eta-failure branch remains as a bare ancestral reverse turn.

### 2. A failed rho with an actual predecessor is P4-valued
Now assume both eta tests passed and work in a chosen exact complement cover T. Suppose q_2 has actual predecessor c in C and actual successor z, so the selected T turn

  (c,q_2,z) tight                                          (AR.6)

is present. If the common q2 insertion seam

  rho=(q_1,q_2,z)                                         (AR.7)

is bad, R3 gives the tight trimer

  K=(z,q_2,q_1).                                          (AR.8)

Probe K with d,y through accepted R700. If a P4 occurs, retain it. Otherwise DUAL-CP tail-signs the reverse initial dimer (q_2,z) by both probes:

  (q_2,z,d), (q_2,z,y) tight.                              (AR.9)

The actual T turn (AR.6) is a head certificate on the SAME tested dimer (q_2,z), and c is distinct from d,y because c lies in the complement residue. Accepted R523 therefore yields, for example,

  (c,q_2,z,d)                                              (AR.10)

as a literal tight Hamilton P4. Thus a failed rho in the C-predecessor branch is not a terminal ancestral shield.

### 3. Exact residual
After this amplification, the q2 insertion ancestry can produce a bare q1q2 reverse trimer only in the SOURCE-q2 case: q_2 is the source of its actual T rail, has successor z, rho=(q_1,q_2,z) fails, and K=(z,q_2,q_1) is retained. There is then no current predecessor c supplying the opposite-polarity certificate used in Section 2.

Accordingly, outside labelled P4 geometry, the only still-unconsumed ancestral-reversal cell from the q2 insertion front is this source-q2 failed-rho state. No claim is made here that it closes or descends. This is established working exposition, not a certified exact unit.


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
        "revision_id": "R700"
    }
]
```
