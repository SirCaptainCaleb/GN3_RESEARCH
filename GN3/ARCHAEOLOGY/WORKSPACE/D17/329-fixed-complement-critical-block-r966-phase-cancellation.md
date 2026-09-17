# Every fixed-complement critical block is source-packet phase-cancellable by one R966 triple

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-critical-block-r966-phase-cancellation`

**Summary:** Let V(H)=Omega disjoint Q be a fixed-complement critical block: Q is a literal Hamilton path, Omega is non-Hamiltonian and deletion-Hamiltonian. Fix any a in Omega and an actual Hamilton puncture path P_a on Omega-a with endpoints h,t. Since Omega-h and Omega-t are Hamiltonian, choose actual replacement paths L_h and R_t. Accepted R966 applies to base P_a, exterior a, and the two endpoint replacements. Its Hamilton-extension outcome would Hamiltonize Omega and is impossible, so one of the comparisons (P_a,L_h),(P_a,R_t),(L_h,R_t) emits explicit R435 geometry: a named selected-state reversal, reverse trimer, or proper tight cycle. Each of P_a,L_h,R_t pairs with the same literal Q in an exact singleton-deletion row, and restoring a,h,t gives three phase-1 maximum forests with identical rail-size profile and common largest-rail height M=max(|Omega|-1,|Q|). The R435 output is a genuine source-packet proper-path/cycle birth before payment: the selected reversal contributes its named reversed dimer, the reverse trimer itself is proper, and a proper cycle contributes a certified cyclic break. SV70046 therefore gives TWO-COVER or phased rank strictly below all three source forests. Hence a fixed-complement critical block cannot be a rank-flat ordinary phase-1 kernel; no R961 case split, CBCA local router, or payment is required. Combined with SV68111/SV69397, the entire portal-wheel branch is phase-cancellable into a strictly lower checkpoint. The remaining obstruction is genuinely phase-0 completed-anchor curvature, not wheel or critical-block currentness.


### 1. Fixed-complement critical block and three actual puncture rows
Let H be a hypothetical smallest Strong Level-(1) counterexample and suppose

  V(H)=Omega disjoint_union V(Q),                          (RC.1)

where Q is a literal Hamilton tight path and Omega is non-Hamiltonian but deletion-Hamiltonian.

Every three-vertex boundary tournament is Hamiltonian by R3, so Omega non-Hamiltonian implies |Omega|>=4. Fix any

  a in Omega                                               (RC.2)

and choose an ACTUAL Hamilton path

  P_a=(p_0,p_1,...,p_r)                                   (RC.3)

on Omega-a. Put

  h=p_0,   t=p_r.                                          (RC.4)

Because Omega is deletion-Hamiltonian, both Omega-h and Omega-t are Hamiltonian. Choose arbitrary actual Hamilton paths

  L_h on Omega-h,
  R_t on Omega-t.                                          (RC.5)

The fixed complement Q makes all three paths literal exact singleton-deletion rows:

  C_a=P_a|Q   on H-a,
  C_h=L_h|Q   on H-h,
  C_t=R_t|Q   on H-t.                                     (RC.6)

Restoring the omitted singleton labels gives three literal maximum spanning three-forests

  F_a={a}|P_a|Q,
  F_h={h}|L_h|Q,
  F_t={t}|R_t|Q.                                          (RC.7)

All three have the identical rail-size multiset

  {1, |Omega|-1, |Q|}.                                    (RC.8)

Hence their common largest-rail height is

  M=max{|Omega|-1,|Q|}.                                   (RC.9)

They form one finite equal-rank phase-1 source packet.

### 2. Accepted R966 forces explicit Reverse-Ear geometry
Apply accepted R966 to

  X=Omega-a,
  base Hamilton path P_a,
  exterior vertex a,
  left endpoint replacement L_h,
  right endpoint replacement R_t.                         (RC.10)

The full extension support is

  X union {a}=Omega,                                      (RC.11)

which is non-Hamiltonian. Therefore the Hamilton-extension alternative of R966 is impossible. At least one of the three path comparisons

  (P_a,L_h),   (P_a,R_t),   (L_h,R_t)                     (RC.12)

has an explicit accepted R435 output:

1. a named reversed old selected state;
2. a tight reverse trimer at one ear seam;
3. a vertex-simple proper tight cycle.                    (RC.13)

No R961 matching, endpoint-role cycle, transfer compiler, payment, or fixed-turn recurrence is needed to force this output.

### 3. Every R435 output is a genuine proper-path birth from the source packet
The output in (RC.13) is source-visible relative to the actual packet (RC.7).

- In the selected-state reversal branch, retain the named reversed physical dimer supplied by R435. A dimer is vacuously a tight path, but here it is NOT an arbitrary dimer: its opposite orientation is the explicit R435 event comparing two actual packet rows.
- In the reverse-trimer branch, retain the emitted tight trimer itself.
- In the proper-cycle branch, retain the physical cycle and choose one certified cyclic break as a proper tight path.

Call the resulting proper tight path K. Since Q is nonempty and disjoint from Omega, every such K is proper in H. The complete birth certificate retains the relevant pair of source rows from (RC.6), the two displayed Hamilton puncture orders, and the exact R435 reversal/seam/cycle output. Thus K is a legal prepayment output of the finite phase-1 source packet (RC.7), not a graph-intrinsic path chosen independently of that packet.

### 4. Packet old-threshold descent
Apply `forest-phase-source-packet-proper-path-old-threshold` SV70046 to the source packet (RC.7) and the born path K.

Because all three packet sources have common height M, SV70046 gives a finite certificate-retaining continuation to either

  TWO-COVER,                                               (RC.14)

or a legitimate SV41376 checkpoint whose phased rank is strictly below

  (1,|V(H)|-M),                                           (RC.15)

hence strictly below every source forest in (RC.7).

The conclusion is independent of the size or rank of any intermediate representative used to currentize K. The comparison is made against the OLD common source height M.

### 5. Fixed-complement phase cancellation theorem
Therefore:

> Every fixed-complement deletion-Hamiltonian critical block carries, from any chosen puncture path, a three-row common-complement R966 packet whose explicit R435 output is prepayment phase-cancellable. The block cannot be a rank-flat ordinary phase-1 recurrence kernel: from its actual singleton source packet there is always a finite route to TWO-COVER or strict phased-rank descent.

This subsumes the need for the older local CBCA routing theorem SV30477 when the strategic objective is G25 phase progress rather than classification. In particular one need not separate quiet R961 triangles, blocker/transfer cases, endpoint-endpoint reversal cycles, or maximum-forest holonomy species merely to prove source-relative descent.

### 6. Portal-wheel consequence
SV68111 removes every CURRENT-INCOHERENT wheel by source-visible phase lifting. SV68752 and SV69397 force every remaining SUPPORT-COHERENT wheel into a full fixed-complement critical block. Sections 1-5 now phase-cancel that block as well.

Hence the full portal-wheel architecture has no rank-flat ordinary phase-1 terminal species. Every wheel lineage has a finite certificate-retaining route to

  TWO-COVER,
  or a checkpoint of strictly smaller SV41376 phased rank. (RC.16)

The strategic obstruction exposed by G25 is therefore pushed entirely below forest phase: genuinely phase-0 completed-anchor curvature remains outside this theorem.

### 7. Scope fence
This is a phased-rank progress theorem, not an absolute standalone proof that H does not exist. It proves strict descent relative to the actual phase-1 singleton source packet. If a later lineage has already entered phase 0, returning from completed-anchor curvature to an R966 forest packet does not automatically lie below that phase-0 parent.

The selected-reversal dimer in Section 3 is legitimate only because it is the named R435 output of the retained source comparison. No arbitrary dimer is counted as a portal. R24 and R5 are unused.


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
        "revision_id": "R966"
    }
]
```