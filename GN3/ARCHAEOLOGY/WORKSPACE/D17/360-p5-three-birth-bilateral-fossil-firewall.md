# A source P5 carries three PAYABLE-FOUR births; the outer birth leaves a bilateral fossil firewall

**Workspace:** D17
**State:** established
**Key:** `p5-three-birth-bilateral-fossil-firewall`

**Summary:** A literal source P5 K=(u,a,m,c,v) carries three distinct PAYABLE-FOUR births B_L=((u,a),(m,c)), B_R=((a,m),(c,v)), and B_X=((u,a),(c,v)), together with dual cross-signs (a,m) head-signed by u and (m,c) tail-signed by v. Pay B_X through SV78086 and retain B_L,B_R as historical fossils on a flat same-E return. For a returned middle in the source orientation (a,b,c), the two raw R434 endpoint channels pair against the unused fossil heads/tails. Any deviation from exact replay of (u,a) tail-by-m and (c,v) head-by-m gives either a new direct mass-four birth or an R523 collision; SV76748 plus SV78086/SV79137 converts the collision output to PAYABLE-FOUR. The opposite orientation (c,b,a) is stricter: its tail channel (t,c) pairs with the source head (a,m) unless t=m, while its head channel (a,w) pairs with source tail (m,c) unless w=m. Avoiding new ancestry forces exact replays (m,c) tail-by-v and (a,m) head-by-u. Raw R434 then forces local labels r=v,b=m,s=u in the only label-compatible case, making (c,m,a) tight, contrary by R3 to the retained tight source turn (a,m,c). Hence opposite orientation can never be history-neutral. The only history-neutral flat-return candidate is source-oriented exact outer replay, which together with (a,m,c) reconstructs the literal source P5. This compresses the G27 kernel to repeated payment with exact full-P5 replay, without claiming stack extinction.

### 1. Three births in one literal P5
Retain a literal tight P5

  K=(u,a,m,c,v),                                         (BF.1)

with five distinct physical vertices. Its three consecutive turns give four signed dimers:

  T_1=(u,a), tail-signed by m,
  T_2=(a,m), tail-signed by c,
  H_1=(m,c), head-signed by a,
  H_2=(c,v), head-signed by m.                           (BF.2)

The same P5 also retains the dual cross-signs

  H_a^+=(a,m), head-signed by u,
  T_c^-=(m,c), tail-signed by v.                         (BF.2a)

These extra signs are used only when a returned R434 middle has the opposite outer orientation.

The opposite-polarity support pairs

  B_L=(T_1,H_1),
  B_R=(T_2,H_2),
  B_X=(T_1,H_2)                                           (BF.3)

are each physically disjoint and have total mass four. Hence each is a source-visible PAYABLE-FOUR birth. Their retained birth ledgers are physically distinct: B_L and B_R are the two adjacent P4 siblings already used in the flat-return analysis, while B_X uses the two outer boundary dimers of K. All three exist graph-intrinsically before any payment descendant is selected.

### 2. Pay the outer birth and retain two bilateral fossils
Choose the outer birth B_X and run the fixed-E PAYABLE-FOUR cancellation SV78086. If it closes H or strictly lowers the old fixed-E clock, stop. Otherwise take its flat same-E return. By accepted R514 and the SV78086 persistence contract, the two unused births B_L and B_R remain separately certified graph-intrinsic historical facts.

Thus the returned state carries two unused fossils

  B_L : tail T_1=(u,a), head H_1=(m,c),
  B_R : tail T_2=(a,m), head H_2=(c,v).                 (BF.4)

They sit on opposite endpoint sides. No claim is made that either fossil is current.

### 3. Source-oriented returned middle: the a-end firewall
Take any exact returned H-E frame, E={a,c}, and an internal middle b for which (a,b,c) is tight. Run the raw bilateral R434 incidence mechanism at this displayed turn. Its a-end channel produces a nontrivial tail-signed dimer

  D_a=(t,a),                                              (BF.5)

where t is an internal frame vertex and hence t is not a or c. Compare D_a with the two unused fossil heads H_1=(m,c), H_2=(c,v). Since m and v are distinct, t cannot equal both. Therefore D_a is physically disjoint from at least one of H_1,H_2, giving a direct mass-four PAYABLE-FOUR certificate by R514.

Moreover this certificate has new birth ancestry unless D_a is literally the old oriented support T_1=(u,a). Indeed, if t=m only H_2 need be used, giving the new oriented tail (m,a); if t=v use H_1, giving the new oriented tail (v,a); and for every t distinct from u,m,v at least one available pairing uses a new physical tail support. The only way every available pairing is one of the old support-pairs B_L or B_X is t=u, i.e. D_a=T_1.

Even in that support-replay case, if the new a-channel witness differs from the old witness m, the same tested oriented dimer T_1 carries two distinct tail witnesses. Accepted R523 gives a raw same-oriented collision. SV76748 parent-compiles it to P4/P5, a direct mass-four pair, or R407; SV78086/SV79137 then make that output PAYABLE-FOUR with new witness ancestry. Therefore failure to create new PAYABLE-FOUR ancestry at the a-end forces exact replay of T_1 with its old witness m.

### 4. Source-oriented returned middle: the c-end firewall
Dually the c-end raw R434 channel produces a head-signed dimer

  D_c=(c,w),                                              (BF.6)

with w internal and outside E. Pair it with the two fossil tails T_1=(u,a), T_2=(a,m). Since u and m are distinct, D_c is disjoint from at least one of them, hence gives PAYABLE-FOUR. Every such pairing has new physical/oriented birth ancestry unless D_c is literally H_2=(c,v). If the support is H_2 but its new witness differs from m, R523 again gives a same-oriented two-witness collision on H_2. SV76748 parent-compiles it to P4/P5, a direct mass-four pair, or R407; SV78086/SV79137 then give new PAYABLE-FOUR ancestry.

Thus failure to create new PAYABLE-FOUR ancestry at the c-end forces exact replay of H_2 with its old witness m.

### 5. Opposite outer orientation cannot be history-neutral
Now suppose instead that the returned internal middle b has the opposite displayed orientation

  (c,b,a) tight.

Apply the same raw R434 extraction to this turn. The predecessor channel at c produces a tail-signed dimer

  D_c^-=(t,c),

and the successor channel at a produces a head-signed dimer

  D_a^+=(a,w),

with t,w outside E. Compare these with the dual source signs in (BF.2a). If t!=m, D_c^- is physically disjoint from H_a^+=(a,m), so there is a direct PAYABLE-FOUR birth. If t=m, the tested support is (m,c), the same orientation as T_c^-, which is tail-signed by v. Unless the new witness is exactly v, R523 gives a same-oriented tail collision; SV76748 followed by SV78086/SV79137 makes it PAYABLE-FOUR. Hence absence of new PAYABLE-FOUR ancestry at this channel forces exact replay of (m,c) tail-signed by v.

Dually, if w!=m then D_a^+=(a,w) is physically disjoint from T_c^-=(m,c), giving a direct PAYABLE-FOUR birth. If w=m, the tested support is (a,m), the same orientation as H_a^+, which is head-signed by u. Unless the new witness is exactly u, R523 gives a same-oriented head collision and the same parent compiler makes it PAYABLE-FOUR. Thus absence of new ancestry at this channel forces exact replay of (a,m) head-signed by u.

The two exact replays cannot occur simultaneously. Write the local returned rail segment as r->b->s. For the predecessor c-channel, replay of (m,c) with witness v requires either (r,b)=(m,v) or (r,b)=(v,m). For the successor a-channel, replay of (a,m) with witness u requires either (b,s)=(u,m) or (b,s)=(m,u). Three of the four pairings force b to equal two distinct vertices among u,m,v. The only label-compatible pairing is r=v, b=m, s=u. But then the returned turn (c,m,a) is tight, whereas the retained source turn (a,m,c) is tight; these are complete reversals, contradicting R3.

Therefore every opposite-orientation returned middle creates new PAYABLE-FOUR ancestry. A history-neutral flat replay can occur only in the source orientation treated in Sections 3--4.

### 6. Exact full-P5 replay is the only history-neutral flat return
By Section 5, any opposite-orientation returned middle already creates new PAYABLE-FOUR ancestry. Hence a history-neutral candidate must have source orientation (a,b,c), and for such a returned middle Sections 3--4 leave only two outcomes:

1. at least one endpoint produces a PAYABLE-FOUR birth whose retained support/orientation/witness ancestry is new relative to the three source births; or
2. both endpoints replay exactly

     (u,a) tail-signed by m,
     (c,v) head-signed by m.                              (BF.7)

In the second case the retained source middle turn

  (a,m,c) tight                                           (BF.8)

concatenates with the two replayed boundary turns to recover the literal source P5 K=(u,a,m,c,v) itself.

Thus a generic returned endpoint event cannot be the history-neutral G27 recurrence. The two unused sibling fossils act as a bilateral firewall: every deviation from the exact outer P5 boundary data manufactures new PAYABLE-FOUR ancestry before payment. Combined with SV83487, which contracts every explicit short portal back to PAYABLE-FOUR, the remaining flat kernel is reduced to repeated payment with exact full-P5 replay.

### 7. Scope fence
This is a stack-compression theorem, not yet stack extinction. PAYABLE-FOUR ancestry lives in a finite graph, but this section does not yet prove that exact full-P5 replay cannot recur after two distinct flat payment lineages. Nor does it identify a historical fossil with a current representative. The remaining G27 target is now the exact replay statement: two flat same-E returns with distinct paid-birth ancestry cannot both reproduce the same source P5 boundary packet without closure or strict descent.

R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```