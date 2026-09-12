# One flat same-E return against an unused P5 sibling forces a later PAYABLE-FOUR birth

**Workspace:** D17
**State:** established
**Key:** `p5-sibling-flat-return-payable-four-rebirth`

**Summary:** Fix an old endpoint pair E={a,c} and an exact H-E frame. The three-spoke construction SV58280 can label three same-orientation internal middles x,y,z so that K=(x,a,y,c,z) is a literal P5. Its left P4 (x,a,y,c) and right P4 (a,y,c,z) give two simultaneous PAYABLE-FOUR births. Pay the left birth and retain the right as an unused historical fossil. If the left payment closes or strictly lowers the old fixed-E clock, stop. Otherwise use the flat-return entrance of SV57138/R1022 with the SAME source frame. Among x,z choose an internal middle r whose selected successor s is not y; such r exists because y has only one predecessor in the path forest. Reenter with J_r=(a,r,c) and take the c-successor incidence. R434 yields a new head-signed dimer D=(c,t), t in {r,s}. Since r,s are both distinct from y, D is disjoint from the fossil tail-signed dimer (a,y), so these two supports form a new direct mass-four PAYABLE-FOUR birth. If D does not have support (c,z), the new birth has new physical support; if D=(c,z), its witness is r or s, never the fossil witness y, so the birth has genuinely new witness ancestry. Thus one rank-flat same-E return plus one unused sibling cannot merely emit a history-neutral short portal: a chosen first incidence already creates a later PAYABLE-FOUR certificate with new support-or-witness ancestry. This is stack growth, not yet stack extinction.

### 1. An explicit endpoint-separated sibling pair inside the three-spoke P5
Fix an old physical endpoint pair

  E={a,c}

at a phase-zero checkpoint, and retain one literal exact frame

  H-E=U|V.                                                (SF.1)

Use the three-spoke construction of SV58280. Among the internal vertices of (SF.1), choose three distinct vertices x,y,z of one common outer orientation and retain the labeling supplied by its edge-order proof so that

  K=(x,a,y,c,z)                                           (SF.2)

is a literal tight P5. Thus

  (x,a,y), (a,y,c), (y,c,z)

are tight.

The left consecutive P4

  K_L=(x,a,y,c)                                           (SF.3)

contains the direct mass-four birth

  B_L : (x,a) tail-signed by y
        paired with (y,c) head-signed by a.               (SF.4)

The right consecutive P4

  K_R=(a,y,c,z)                                           (SF.5)

contains the distinct direct mass-four birth

  B_R : (a,y) tail-signed by c
        paired with (c,z) head-signed by y.               (SF.6)

All five vertices in K are distinct, so each displayed pair has physically disjoint supports. Hence B_L and B_R are two simultaneous source-visible PAYABLE-FOUR certificates before either payment descendant is chosen. Their exact supports, witnesses, K, and source frame are retained.

### 2. Pay one sibling and fossilize the other
Choose B_L as the productive exit. Apply accepted R514 and the old-endpoint return map SV57138. If H closes, stop. If the old fixed-E clock strictly decreases, stop.

Assume therefore that the chosen continuation returns rank-flat to the same physical E. R514 explicitly preserves every separately certified graph-intrinsic static configuration as historical data, so the unused sibling B_R in (SF.6) survives the B_L payment as a historical birth fossil. No old representative is asserted current.

At the R1022 entrance used by SV57138, choose the exact H-E frame to be the original literal frame (SF.1). This is legal because the proof of accepted R1022 allows any prescribed exact pair-deletion cover and then any internal vertex of that displayed cover.

### 3. Choose a returned middle whose successor avoids the fossil middle
Both x and z are internal vertices of (SF.1). Since y lies on one of the two vertex-simple rails, it has at most one selected predecessor in that frame. Consequently at most one of x,z can have selected successor y. Choose

  r in {x,z}

whose selected successor s satisfies

  s != y.                                                 (SF.7)

Also r!=y. The three-spoke source turns are graph-intrinsic, so

  J_r=(a,r,c)                                             (SF.8)

is tight. Use r as the internal middle in the controlled R1022 entrance and stop at the same-E entrance checkpoint exactly as in SV57138.

### 4. The first c-incidence pairs directly with the unused fossil
Now choose the selected successor incidence

  r -> s

in the retained frame. Apply the literal c-end extraction inside accepted R434. Exactly one of

  (r,c,s), (s,c,r)

is tight. Accordingly R434 retains a head-signed endpoint dimer

  D=(c,t),                                                (SF.9)

where t=s in the first case and t=r in the second. The sign witness is respectively r or s.

By (SF.7) and r!=y,

  t != y.                                                 (SF.10)

Moreover r,s belong to H-E, so t is distinct from a,c. Therefore the new head-signed dimer D is physically disjoint from the UNUSED fossil tail dimer

  T=(a,y), tail-signed by c,                              (SF.11)

which is one side of B_R. The two supports D,T have opposite polarity and total mass four. Hence

  B_new := T | D                                          (SF.12)

is a direct source-visible PAYABLE-FOUR birth. It is born at the first selected-incidence episode after the flat same-E return; it is not merely a re-reading of the old source pair.

### 5. The birth ancestry is genuinely new even under physical support replay
Compare B_new with the unused source sibling B_R. They share the fossil tail support T=(a,y). The source head support in B_R is

  D_0=(c,z), head-signed by witness y.                    (SF.13)

If V(D) differs from V(D_0), then B_new has a genuinely new physical support.

If D has the same physical support as D_0, then D=(c,z). Its R434 sign witness is r or s. By construction r!=y and s!=y. Hence even in exact physical-support replay the later certificate on (c,z) has a witness different from the source witness y. Thus B_new has genuinely new witness ancestry.

So every nonclosing rank-flat return in this chosen sibling branch strictly enlarges the retained birth ledger in the G27 sense: it adds a PAYABLE-FOUR certificate whose post-return endpoint-dimer datum is new in physical support or in its exact sign witness.

### 6. Stack consequence
Combining Sections 1--5 gives the one-return stacking theorem:

> From one exact H-E frame above order ten, choose the explicit three-spoke P5 K=(x,a,y,c,z). Pay the left PAYABLE-FOUR birth B_L and retain the right birth B_R. Then there is a chosen finite continuation yielding TWO-COVER, strict old-E descent, or, in the rank-flat branch, a new PAYABLE-FOUR birth B_new whose ancestry contains the first post-return selected-incidence dimer and which differs from B_R in physical support or sign witness.

In particular the first flat return need not terminate at an anonymous R435/R436 short portal. The unused sibling fossil can be spent immediately against the returned selected-incidence dimer to create a later lawful mass-four birth.

This is genuine PORTAL-STACK GROWTH. It is not yet portal-stack extinction: a later payment of B_new may itself return flat, and this section does not yet prove that the resulting sequence of support/witness certificates cannot eventually repeat.

### 7. Scope fence
Alternative paid descendants are never asserted simultaneously current. Only B_L is paid; B_R remains a separately certified graph-intrinsic historical birth under the explicit persistence clause of R514. The old frame is reused only as a legitimate chosen exact frame at the later R1022 entrance, not asserted to have remained current during payment.

No fourth numerical rank coordinate is introduced. Exact support replay is allowed; the theorem records the forced witness change in that case. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R1022"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    }
]
```