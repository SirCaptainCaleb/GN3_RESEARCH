# The order-four source-wrap P4 is a locked common-complement reversal with a finite B-terminal consumer

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-source-q2-four-rail-complement-consumer`

**Summary:** In the source-q2 double-wrap-failure branch with current q2 rail of order four, the original rail R=(q2,z,r2,r3) and emitted P4 F=(z,q2,r3,r2) are exact same-support rows with the identical literal complement B_T. They select both endpoint dimers q2-z and r2-r3 oppositely. The fixed-complement selected-reversal transport is already blocked at its first required wrap by an inherited turn from the other row, so the cell is a mutually locked double current reversal rather than automatic R561. Testing the terminal b of B_T against the retained eta blocks gives a finite cover-aware alternative: a passing prepend creates the exact R933 two-hole spanning word and therefore a current reverse B-terminal shield; double prepend failure either gives a P4 whose residual forest is explicitly R|(B_T-b)|{q1}, or in the P4-free branch forces both b-d-y and b-y-d. Then a passing B attachment seam yields an exact H-t row selecting d-y or y-d and re-enters the strict source-distance transport; double attachment failure leaves d,y as two named witnesses on the actual reverse terminal dimer of B_T. No generic packet payment is taken.

Retain `singleton-deep-source-q2-wrap-consumer` in its long double-wrap-failure branch, and specialize to an actual q2-source rail of order four. Write

  R=(q2,z,r2,r3),      T=R | B                         (FC.1)

for the exact two-cover of W=H-{t,d,y,q1}, with B the literal other Hamilton rail. Both eta rows passed, so

  (t,d,y,q1,q2),   (t,y,d,q1,q2)                      (FC.2)

are tight, while rho=(q1,q2,z) is bad and hence

  (z,q2,q1) tight.                                       (FC.3)

The two R579 wrap seams are bad. Thus the emitted P4 is

  F=(z,q2,r3,r2).                                         (FC.4)

### 1. The P4 already gives an exact common-complement double reversal
Because |R|=4, F spans exactly V(R). Hence both

  R | B,        F | B                                    (FC.5)

are literal exact two-covers of the SAME residue W with the SAME support partition and the SAME literal complement B. Moreover R selects q2->z and r2->r3, whereas F selects z->q2 and r3->r2. Thus two disjoint physical dimers are selected in opposite directions across the two rows.

Apply the working fixed-complement selected-reversal normal form to q2-z. The R-row already begins q2,z. Moving the reverse state z,q2 in F toward the opposite boundary would first require the head-wrap seam

  (r2,z,q2).                                               (FC.6)

But (FC.6) is the complete reverse of the inherited tight R-turn (q2,z,r2), so R3 forces it bad. Thus that reversal is already at a named blocked normal form, with the exact shield (q2,z,r2) retained. Dually, for r2-r3 the required first tail-wrap of R is (r2,r3,q2), the complete reverse of the tight F-turn (q2,r3,r2), and is therefore bad. Hence (FC.5) is a mutually locked double selected-reversal cell. It is genuine current same-complement structure, but it does NOT by itself give R561 or restore D0.

### 2. Test the actual terminal of the untouched complement
Write B=(b0,...,bs) and put b=bs. When s>0 write b-=b_{s-1}. Test

  theta_d=(b,t,d),       theta_y=(b,t,y).                 (FC.7)

If theta_d is tight, then

  Q_d=(b,t,d,y,q1,q2)                                    (FC.8)

is Hamiltonian on {b,t,d,y,q1,q2}; theta_y gives the dual Q_y=(b,t,y,d,q1,q2). Apply accepted R933 to H with Y covered by the two current rails R and B, choosing q2 as the source endpoint of R and b as the terminal endpoint of B, and using Q_d or Q_y as the role-correct Hamilton bridge through D0 plus those endpoints. The right attachment hole is exactly rho=(q1,q2,z), already bad. Since pc(H)>2, R933's strengthened clause forces the left residual seam to exist and be bad as well. Thus if s>0,

  (b-,b,t) bad,   hence (t,b,b-) tight.                   (FC.9)

If s=0, the missing left seam would leave only one hole, impossible under pc(H)>2; therefore a passing theta already closes/contradicts the counterexample. No reversal of B is used.

### 3. If both terminal prepends fail, either a P4 is explicit or both d/y orders leave b
Assume both turns in (FC.7) are bad. R3 gives

  (d,t,b), (y,t,b) tight.                                 (FC.10)

If X_b={t,d,y,b} has a Hamilton P4, retain its ACTUAL order together with its literal residual forest

  R | (B-b) | {q1},                                       (FC.11)

where B-b is omitted if empty. This is a complement-aware P4 output, not a closure claim.

Assume X_b is P4-free. Apply accepted R518 first to the retained trimer (t,d,y) with fourth vertex b and then to (t,y,d) with fourth vertex b. In the no-P4 branch their forced reverse contacts give

  (b,y,d), (b,d,y) tight.                                 (FC.12)

### 4. The next B seam either gives an exact H-t row or a two-witness current B shield
If s=0, (FC.12) immediately gives the two exact H-t covers

  (b,d,y,q1,q2) | (z,r2,r3),
  (b,y,d,q1,q2) | (z,r2,r3).                              (FC.13)

They are exact because H-t cannot be Hamiltonian in a smallest counterexample. Each selects one orientation of {d,y}, with the matching prepend turn from (FC.2), so either row enters `singleton-deep-single-row-source-transport`.

Assume s>0 and test

  alpha_d=(b-,b,d),      alpha_y=(b-,b,y).                (FC.14)

If alpha_d is tight, then

  (b0,...,b-,b,d,y,q1,q2) | (z,r2,r3)                    (FC.15)

is an exact H-t two-cover. If alpha_y is tight, the same statement holds with y,d exchanged. Again the selected d/y orientation and the literal complementary rail (z,r2,r3) are retained, so the verified source-distance transport applies immediately.

If both turns in (FC.14) are bad, R3 gives

  (d,b,b-), (y,b,b-) tight.                               (FC.16)

Thus d and y are two named witnesses on the ACTUAL reverse terminal dimer b->b- of the untouched current complement B. This is retained as a B-boundary terminal; no generic R542/R523 payment is taken here.

### 5. Exact scope
The |R|=4 source-wrap P4 is therefore substantially more current than a bare P4: it is an exact same-residue same-complement double selected reversal. Its first fixed-complement transport attempts are blocked by the other retained Hamilton row itself. At the terminal end of B, the smallest restoration test yields only: immediate contradiction when a one-hole R933 splice would occur; a named reverse B-terminal shield (FC.9); a P4 with explicit residual forest (FC.11); an exact H-t row feeding the strict d/y source-distance transport; or the two-witness current B-boundary state (FC.16). The source end of B and the final two-witness B-boundary state are not consumed here.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R518"
    },
    {
        "relation": "dependency",
        "revision_id": "R933"
    }
]
```
