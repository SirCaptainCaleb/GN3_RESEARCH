# Every exact q2 complement representative enters one universal paired gate

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-universal-q2-gate`

**Summary:** The q2 paired insertion depends only on the actual predecessor of q2, not on whether that predecessor lies in S or C. Source q2 first rotates to a predecessor state or produces a P4. With arbitrary predecessor h, failed rho is P4-valued using R700 plus the actual T turn (h,q2,z). The two spanning insertion words have the same complete alpha/beta/rho windows as before; alpha failure and double-gamma failure are P4-valued by R700/R523, while the P4-free four-cell forces lower H-t lifts. Hence every exact complement representative yields a labelled P4, an exact H-t row containing one orientation of {d,y}, or closure. The single-row source transport then reduces every H-t row to closure or a named wrap shield. The earlier S-predecessor/R435 and MULTI-CROSS splits are therefore not independent terminal species.


Retain the verified second-block q2 front and the source-q2 wrap consumer. The key point of this section is that the local paired insertion never needed the predecessor of q_2 to lie in C. Any actual predecessor works.

After the two eta tests, eta_y=(y,q_1,q_2) and eta_d=(d,q_1,q_2), if either eta fails then `singleton-deep-ancestral-reversal-amplification` already gives a labelled P4. Assume both eta tests pass, so

  B_d=(t,d,y,q_1,q_2),
  B_y=(t,y,d,q_1,q_2)                                    (UG.1)

are tight opposite-{d,y} insertion blocks. Fix ANY exact complement two-cover T of H-{t,d,y,q_1}.

### 1. Source q2 is already reduced to a predecessor state or P4
If q_2 is the source of its T rail, `singleton-deep-source-q2-wrap-consumer` applies. A dimer reverses freely; a successful R579 wrap moves q_2 off the source; double-wrap failure is P4-valued, including the trimer exception. Therefore the source case yields a labelled P4 or an exact representative in which q_2 has an actual predecessor. It is enough to treat that predecessor state below.

### 2. The predecessor macro class is irrelevant
Let the actual T rail containing q_2 have local order

  ... h_0,h,q_2,z ...                                     (UG.2)

with h_0 omitted when h is the rail source and z omitted when q_2 is terminal. Here h is ANY vertex of the complement residue; it may lie in ancestral S or in C=P union {q_0}. Every such vertex is distinct from t,d,y,q_1.

If z exists, test the common right seam

  rho=(q_1,q_2,z).                                        (UG.3)

If rho is bad, R3 gives K=(z,q_2,q_1). Apply accepted R700 to K with probes d,y. If R700 gives P4, retain it. Otherwise its DUAL-CP branch tail-signs the tested dimer (q_2,z) by d and y. But the actual T turn

  (h,q_2,z) tight                                         (UG.4)

is a head certificate on the SAME tested dimer, with witness h distinct from d,y. Accepted R523 therefore gives a literal P4, for example

  (h,q_2,z,d).                                             (UG.5)

Hence outside labelled P4 geometry rho is absent or tight.

### 3. Universal paired insertion
Insert the two blocks (UG.1) immediately before the existing q_2 position:

  F_d=(...,h,t,d,y,q_1,q_2,z,...),
  F_y=(...,h,t,y,d,q_1,q_2,z,...).                        (UG.6)

The other T rail remains LITERALLY unchanged. Their COMPLETE new-turn windows are exactly

  alpha=(h_0,h,t)             when h_0 exists,
  beta_d=(h,t,d),   beta_y=(h,t,y),
  rho=(q_1,q_2,z)             when z exists.              (UG.7)

There is no macro-class hypothesis in this seam ledger. Every middle turn lies in B_d/B_y and all turns outside the displayed window are inherited from T.

If either complete window passes, the corresponding active rail plus the untouched other T rail is a spanning two-cover of H. Thus in a counterexample both windows are blocked.

If alpha exists and is bad, R3 gives K_alpha=(t,h,h_0). Accepted R700 with probes d,y either emits a P4 directly or forces (h,t,d); together with retained (t,d,y), this gives the literal P4

  (h,t,d,y).                                                (UG.8)

Therefore outside P4 geometry alpha is absent or tight. Since rho is also absent or tight, both individual beta seams must be bad:

  (d,t,h), (y,t,h) tight.                                 (UG.9)

### 4. P4-free four-cell currentizes to H-t for every predecessor h
Put X={t,d,y,h}. If X has a Hamilton P4, retain it. Assume X is P4-free.

If (h,d,y) were bad, R3 would give (y,d,h), and retained (t,y,d) would produce the forbidden P4 (t,y,d,h). Hence (h,d,y) is tight. Dually, if (h,y,d) were bad, R3 gives (d,y,h), and retained (t,d,y) gives forbidden (t,d,y,h). Thus

  (h,d,y), (h,y,d) tight.                                 (UG.10)

Delete t from the two spanning proposals:

  G_d=(...,h,d,y,q_1,q_2,z,...),
  G_y=(...,h,y,d,q_1,q_2,z,...).                          (UG.11)

The common right seam rho has already passed or is absent. If h is the source, there is no remaining left seam, so BOTH are exact H-t covers with identical active support and the identical untouched complement.

If h_0 exists, their only remaining turns are

  gamma_d=(h_0,h,d),   gamma_y=(h_0,h,y).                (UG.12)

If both are tight, (UG.11) are exact common-complement H-t representatives selecting {d,y} oppositely. If exactly one is tight, it is an actual exact H-t representative. If both are bad, R3 gives

  (d,h,h_0), (y,h,h_0) tight.                             (UG.13)

Because alpha=(h_0,h,t) is tight in this branch, accepted R700 on the tight trimer (h_0,h,t) with probes d,y either gives P4 directly or tail-signs the same tested reverse initial dimer (h,h_0) by d,y. The turns (UG.13) head-sign that tested dimer. Accepted R523 then gives a literal P4, e.g.

  (d,h,h_0,y).                                             (UG.14)

Thus every non-P4 predecessor state produces at least one exact H-t row containing one orientation of {d,y}.

### 5. Universal q2 conclusion
Combining Sections 1-4, the macro split S-predecessor versus C-predecessor is unnecessary. For EVERY exact complement representative T, after the eta tests the q2 geometry yields

  labelled Hamilton P4,
  OR an actual exact H-t representative containing d->y or y->d,
  OR immediate spanning closure.                          (UG.15)

By `singleton-deep-single-row-source-transport`, every H-t row in (UG.15) then has strict selected-dimer source-distance transport to spanning closure or a named R548 wrap shield.

Consequently R435 geometry and MULTI-CROSS are not independent q2 terminal species: even when q_2 is entered from an ancestral S vertex, the same seam-complete paired insertion applies. The current hard R2 outputs are therefore only labelled P4 geometry or a current H-t wrap-shield terminal after a genuine well-founded source-distance transport. This is established working exposition, not a certified exact unit.


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
        "revision_id": "R579"
    },
    {
        "relation": "dependency",
        "revision_id": "R700"
    }
]
```
