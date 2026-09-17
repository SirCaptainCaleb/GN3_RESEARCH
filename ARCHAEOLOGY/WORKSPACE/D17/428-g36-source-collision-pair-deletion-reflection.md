# Fence: source-dimer pair-deletion reflection needs a second insertion seam

**Workspace:** D17
**State:** limitation
**Key:** `g36-source-collision-pair-deletion-reflection`

**Summary:** RETRACTION/FENCE of the previous reflection claim. In an exact two-cover of H-{A,t}, replacing a selected edge p->w by p->A->t->w has two new boundary obligations, not one: besides (p,A,t), the changed predecessor at w creates (t,w,q) when w has successor q. Likewise a source occurrence still leaves the outgoing seam at w. Therefore the previous argument cannot force a reverse-orientation source-dimer collision. The exact usable residue is a two-seam insertion window for each source-dimer witness. SV115482 and SV115908 are unaffected.

### RETRACTION / FENCE
The previous version of this section claimed that the source-dimer collision of SV115482 reflects to a same-polarity collision on the reverse tested source dimer in every exact pair-deletion cover. That claim is invalid.

### 1. The omitted successor-side seam
Retain the OUT source-dimer collision

  (A,t,w) tight                                             (FPR.1)

for one witness w, and let T be an exact two-cover of H-{A,t}. Suppose T selects

  p -> w -> q                                               (FPR.2)

with both predecessor and successor present. Replacing p->w by

  p -> A -> t -> w                                         (FPR.3)

does restore the two deleted vertices at the correct matching cardinality, but its complete new-turn ledger is

  (p,A,t),   (A,t,w),   (t,w,q).                           (FPR.4)

Only the middle turn in (FPR.4) is certified by (FPR.1). The earlier version checked (p,A,t) and incorrectly treated every remaining turn as inherited. The turn at w has changed predecessor from p to t, so (t,w,q) is a genuinely new seam.

If w is a rail source, prepending A->t gives the word

  A -> t -> w -> q -> ...                                  (FPR.5)

and still requires the new turn (t,w,q). Thus source position does not by itself close H. Dually, if w is terminal only the predecessor-side seam remains, but that is a special endpoint case rather than a universal reflection theorem.

### 2. Invalid conclusions withdrawn
Consequently the previous assertions that C and b cannot be rail sources in every H-{A,t} cover, that their predecessors necessarily give turns (t,A,p_C),(t,A,p_b), and that a two-tail collision on (A,t) automatically reflects to a two-tail collision on (t,A), are withdrawn. The IN-dual successor argument has the identical omitted opposite-side seam and is withdrawn as well.

### 3. Correct residual interface
What remains valid is only the exact TWO-SEAM INSERTION WINDOW. For an OUT tail witness w of (A,t), an interior occurrence p->w->q in an exact H-{A,t} cover gives a spanning two-path proposal after insertion of A,t whose uncertified turns are precisely

  alpha_w=(p,A,t),
  beta_w=(t,w,q).                                          (FPR.6)

At a source occurrence only beta_w exists; at a terminal occurrence only alpha_w exists. Since H has no two-cover, at least one existing seam in (FPR.6) is bad, and R3 certifies its exact reverse.

For the IN/head dual on deleted pair {t,C}, the analogous complete insertion window has the two endpoint-dual seams.

This two-hole window may still be useful because the source-dimer collision supplies two witnesses w=C,b in one parent packet, but no reverse-dimer collision follows without additional interaction between their insertion windows.

### 4. Status
This section is a limitation/fence. It preserves the exact bug and the corrected two-seam obligation so the invalid one-seam reinsertion is not reused downstream. SV115482 and SV115908 are unaffected. No theorem-level progress is claimed here.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```
