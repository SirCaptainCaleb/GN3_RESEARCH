# A bilateral R542 node currentizes across its two boundary deletions before either payment is chosen

**Workspace:** D17
**State:** established
**Key:** `bilateral-r542-prepayment-common-residue-currentization`

**Summary:** Retain one bilaterally saturated hard-run node from SV73346: J=(c,d,a), with reverse boundary dimer (d,c) tail-signed and (a,d) head-signed by the same two rail-neighbor witnesses b,e. Choose arbitrary exact covers of H-{d,c} and H-{a,d}. R542 forces each to select a carrier-singleton/exterior crossing, hence a is incident to a selected crossing in the first and c in the second. Puncture a and c to the common residue W=H-{a,c,d}. If either carrier singleton is internal, R159 gives an immediate source-visible component drop. Otherwise both are endpoints and the punctures are exact two-covers of W. R471 says any support/order disagreement already yields pair/R435 geometry; outside it the punctures are one common exact base cover T, and the two source covers are endpoint attachments of a and c to T. If a is a source attachment, testing the seam from d through a into the base rail either gives a spanning two-cover of H or a new head witness on (a,d); if that witness is distinct from b,e, the three-witness common-parent compiler SV44176/SV44695 fires before payment. Dually, if c is a terminal attachment, one gets closure or a third tail witness on (d,c). Hence outside common-parent three-witness geometry and witness replay, the only role-unconstrained synchronized residue has a terminal and c source (the orientation opposite to the carrier splice), with the remaining non-anti-aligned cases forced to attach directly at one of the two old witnesses b,e. This converts bilateral R542 recycling into a finite prepayment endpoint-role/concentration cell.

### 1. Bilaterally saturated central carrier
Retain one interior node of the alternating hard-run theorem SV73346. Normalize

  J=(c,d,a)                                                (BC.1)

as the central tight trimer. Let b,e be its two neighboring vertices on the one literal source rail. SV73346 gives the simultaneous graph-intrinsic certificates

  (d,c,b), (d,c,e) tight,                                 (BC.2)
  (b,a,d), (e,a,d) tight.                                 (BC.3)

Thus

  S_L=(d,c) is tail-signed by b,e,
  S_R=(a,d) is head-signed by b,e.                        (BC.4)

These two R542-ready packets coexist in the parent before either R542 continuation is chosen.

### 2. Choose both boundary-deletion frames before payment
Accepted R429 supplies arbitrary exact two-covers

  T_L of H-{d,c},
  T_R of H-{a,d}.                                         (BC.5)

Apply accepted R542 only for its SAME-FRAME crossing conclusion, not its paid descendant.

For S_L=(d,c), the complementary carrier vertex in J is a. Every exact T_L therefore selects a carrier/exterior state

  {a,y_L}.                                                 (BC.6)

For S_R=(a,d), the complementary carrier vertex is c. Every exact T_R selects

  {c,y_R}.                                                 (BC.7)

The selected directions are retained but are not needed below.

### 3. Puncture to one common triple deletion
Put

  W=H-{a,c,d}.                                             (BC.8)

If a is internal on its T_L rail, deleting a splits that rail into two nonempty pieces and leaves the other nontrivial rail, giving a literal three-cover of W. Minimality supplies an at-most-two cover of W and accepted R159/R176 gives source-visible component-drop geometry.

The same conclusion holds if c is internal in T_R.

Hence the only branch not already in current component-drop currency has

  a an endpoint in T_L,
  c an endpoint in T_R.                                   (BC.9)

Pair-deletion rigidity makes the source rails nontrivial, so endpoint trimming leaves two nonempty rails:

  F_L=T_L-a,
  F_R=T_R-c.                                               (BC.10)

If W were Hamiltonian, its Hamilton path together with J would two-cover H. Therefore W is non-Hamiltonian, and F_L,F_R are literal exact two-covers of the same W.

Apply accepted R471. Different support partitions give the R410/R176 pair output; equal supports with different Hamilton orders give explicit R435 reversal/reverse-trimer/proper-cycle geometry. Outside those outputs,

  F_L=F_R=:T                                               (BC.11)

literally up to exchange of the two rail names.

Thus T_L and T_R are obtained from one common exact base cover T of W by endpoint-attaching a and c respectively.

### 4. Any source attachment of a is closure or a third head witness
Suppose a is the SOURCE attachment in T_L. Write the corresponding base rail of T as

  P=(y,p_1,...),                                           (BC.12)

allowing P=(y) when the trimmed rail is singleton. T_L contains

  (a,y,p_1,...)                                            (BC.13)

when p_1 exists.

Test the one carrier splice seam

  sigma_R=(d,a,y).                                        (BC.14)

If sigma_R is tight, then J=(c,d,a) followed by the base rail P is one tight path

  (c,d,a,y,p_1,...).                                      (BC.15)

Together with the untouched other T-rail it spans H, contradicting pc(H)=3.

Therefore sigma_R is bad. R3 gives

  (y,a,d) tight,                                          (BC.16)

so y is a head witness on the SAME tested R542 boundary dimer S_R=(a,d).

If y is distinct from both old witnesses b,e, then S_R has THREE distinct same-polarity witnesses b,e,y, all exterior to the carrier J. The same-parent three-witness compiler SV44176 and its refinement SV44695 apply before any payment and yield

  literal P4/P5,
  direct mass-four pair,
  or R407 bidirectional interaction.                       (BC.17)

Consequently, outside (BC.17), every synchronized SOURCE attachment of a is forced to land at one of the two old rail-neighbor witnesses:

  y in {b,e}.                                              (BC.18)

### 5. Terminal attachment of c is the exact dual
Suppose c is the TERMINAL attachment in T_R. Write its base rail as

  P=(...,p_{r-1},x),                                      (BC.19)

again allowing P=(x). Test

  sigma_L=(x,c,d).                                        (BC.20)

If tight, the base rail through x concatenates with c,d,a and, together with the other T-rail, gives a spanning two-cover of H. Hence sigma_L is bad and R3 gives

  (d,c,x) tight.                                          (BC.21)

Thus x is a third tail witness on S_L=(d,c). If x is distinct from b,e, SV44176/SV44695 gives the same parent-scale output alphabet (BC.17). Outside it,

  x in {b,e}.                                              (BC.22)

### 6. The surviving prepayment cell
Therefore, after synchronizing the two R542 deletion frames, any branch avoiding

- spanning two-cover,
- R159/R176 component drop,
- R410/R435 same-residue disagreement,
- three-witness P4/P5/direct-pair/R407 geometry,

has the following sharply finite form.

Either

  a is TERMINAL and c is SOURCE on their common base attachments,          (BC.23)

which is the endpoint-role orientation opposite to the carrier splice c->d->a; or every non-anti-aligned favorable attachment is pinned directly to one of the two original witnesses b,e as in (BC.18),(BC.22).

Call this the BILATERAL R542 ENDPOINT-CONCENTRATION CELL.

No paid R542 descendant has been used to obtain it. The source trimer J, both two-witness dimers, both boundary-deletion covers, the common triple-deletion base T, endpoint roles, and any witness-pinned attachment are retained simultaneously as graph-intrinsic/source-frame ancestry.

### 7. G26 meaning
SV73346 reduced growth-free hard recurrence to an alternating bilateral R542 chain. The present theorem removes arbitrary payment history from one chain node: before either R542 packet is spent, its two deletion frames already synchronize or emit named current geometry. A completely flat survivor must therefore repeat one finite endpoint-role/concentration pattern at every interior chain node.

This is structural compression, not bottom-family extinction. In particular the anti-aligned cell (BC.23) and the old-witness attachment cases may still exist, and mass-four/R407 outputs are not called phase-zero descent. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    }
]
```