# Every good-bad current-star spoke is source-relative phase-rank cancellable

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-bad-singleton-current-star-phase-cancellation`

**Summary:** Compose SV65183 with the source-labelled pair-portal phase lift SV68431. For every good d and bad y in a fixed-complement shell, the current geometry on H-{y,d} has a literal phase-1 parent before payment. If y is internal in P_d, the component-drop portal comes from deleting y and singleton d from the good source forest {d}|P_d|Q. If d is internal in the bad row C_y, it comes from deleting d and singleton y from the bad source forest {y}|C_y. If both are endpoints, the two exact pair rows F_d=C_d-y and G_d=C_y-d have different support partitions; the R410 selected crossing belongs to one of those exact rows and is rooted in the corresponding restored singleton source forest. Applying SV68431 to the designated current state gives TWO-COVER or phased rank strictly below that actual source checkpoint. Hence no SV65183 current-star spoke is rank-flat at its source; the common-center payment star SV66139 is unnecessary for consuming the ordinary fixed-complement current kernel. This does not solve portals whose only parent is already phase 0.

### 1. Input: the fixed-complement current star
Retain SV65183 in a hypothetical smallest counterexample:

  V(H)=Omega disjoint_union V(Q),

Q is a literal Hamilton path, d is GOOD with an actual Hamilton puncture path P_d on Omega-d, and y is BAD. Write

  C_d=P_d|Q  on H-d,
  C_y=A_y|B_y on H-y.                                     (SC.1)

Restoring the deleted singleton labels gives literal maximum three-forests

  S_d={d}|P_d|Q,
  S_y={y}|A_y|B_y.                                        (SC.2)

Both are phase-1 checkpoints. SV65183 proves that for every good d the common pair deletion H-{y,d} carries a CURRENT crossing/component-drop portal. We verify that in every branch this current state is source-labelled by one of the literal phase-1 forests in (SC.2), before any R176/R428 payment.

### 2. Good-row fragmentation: parent is S_d
Suppose y is internal on P_d. Deleting y from P_d splits that rail into two nonempty intervals while Q survives, so deleting {y,d} from the literal source forest S_d gives the three-cover

  R_d=(P_d-y)|Q                                           (SC.3)

of H-{y,d}, with three nonempty components. Accepted R429 supplies an exact two-cover

  T_d=U_d|V_d                                              (SC.4)

of the same residue. Component counting forces T_d to select a state crossing two components of R_d; retain one such directed selected state x_d->z_d as the current portal state.

All data in (SC.3)-(SC.4) were obtained by literal deletion/recompletion from the phase-1 source S_d. No pair payment or phase-0 checkpoint has occurred. Apply SV68431 with parent F_0=S_d, deleted pair {y,d}, exact cover T_d, and designated state x_d->z_d. It gives

  TWO-COVER,
  or phased rank strictly below rank(S_d).                 (SC.5)

Thus every INTERNAL-good-row spoke is source-relative cancellable.

### 3. Bad-row fragmentation: parent is S_y
Now suppose y is an endpoint of P_d but d is internal on its C_y rail. Deleting d from C_y splits that rail, and deleting the restored singleton y from S_y gives a literal three-cover

  R'_d=C_y-d                                               (SC.6)

of H-{y,d}. Let T'_d be any exact two-cover supplied by R429 and retain a selected T'_d-state crossing two components of R'_d.

This current component-drop portal is rooted in the literal phase-1 source S_y. Apply SV68431 with parent F_0=S_y. Again one obtains

  TWO-COVER,
  or phased rank strictly below rank(S_y).                 (SC.7)

Thus every INTERNAL-bad-row spoke is source-relative cancellable.

### 4. Endpoint-endpoint support disagreement: use whichever exact row selects the R410 crossing
It remains to assume y is an endpoint of P_d and d is an endpoint of its C_y rail. SV65183 then gives two literal exact two-covers of the common pair deletion:

  F_d=C_d-y=(P_d-y)|Q,
  G_d=C_y-d,                                               (SC.8)

with different unordered support partitions. Accepted R410 supplies a selected CURRENT crossing between these two actual common-residue covers. Retain the exact orientation and record which row selects it.

If the selected crossing belongs to F_d, its source ancestry is the good phase-1 forest S_d: F_d is obtained by deleting the endpoint y and singleton d. Apply SV68431 with F_0=S_d.

If the selected crossing belongs to G_d, its source ancestry is the bad phase-1 forest S_y: G_d is obtained by deleting endpoint d and singleton y. Apply SV68431 with F_0=S_y.

Therefore the endpoint-endpoint spoke also gives

  TWO-COVER,
  or phased rank strictly below the ACTUAL phase-1 source forest whose pair row selects the R410 crossing.    (SC.9)

No representative switch is hidden here: the source forest is chosen only after the physical selected crossing and its current row are known.

### 5. Fixed-complement current-star cancellation
Sections 2-4 exhaust the SV65183 star construction. Hence:

> FIXED-COMPLEMENT CURRENT-STAR PHASE CANCELLATION. Every good-bad spoke {y,d} of the SV65183 current star has a designated current pair-deletion state and a literal restored singleton source forest S in phase one such that the spoke has a finite certificate-retaining continuation to TWO-COVER or to a checkpoint of SV41376 phased rank strictly below S.

The complete source labels are retained: d,y, the relevant actual singleton row, the literal pair deletion, the fragmented or exact comparison row, the designated selected current state, and the SV68431 dimer/trimer lift.

Thus the G24 current star is not a rank-flat terminal kernel. Its currentness is spendable into the global phased rank root by root. In particular the common-center paid-star theorem SV66139 is no longer required to consume this ORDINARY fixed-complement current kernel; it remains useful only when one intentionally follows payment ancestry for epsilon_* or completed-anchor analysis.

### 6. Family-level consequence and fence
In any reconstruction-closed nonclosing family that contains the literal source representatives of a fixed-complement bad-singleton shell and is minimized by the legitimate SV41376 phased rank, no SV65183 spoke can survive as a rank-flat recurrence at its source: the corresponding SV68431 continuation leaves the source stratum strictly downward.

This statement is source-relative. It does not claim that a portal whose only retained parent checkpoint already has phase coordinate 0 is consumed by returning to a dimer forest. Such completed-anchor/payment-phase curvature remains outside the theorem.

R24 and R5 are not used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```