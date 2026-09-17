# A transported P4 has at most two distinct P5-free matching reentry middles

**Workspace:** D17
**State:** established
**Key:** `p4-middle-pair-mixed-reentry-capacity-two`

**Summary:** Retain a tight P4 K=(x,p,q,y) and later matching-orientation turns (p,b,q). SV74696 says any P5-free reentry must be MIXED in the two old boundary seam tests alpha_b=(x,p,b), beta_b=(b,q,y). Two distinct LEFT-PASS mixed middles b,d force the four turns (x,p,b),(p,b,q),(x,p,d),(p,d,q). If their five-set were nonHamilton, R902 supplies an edge order with xp<pb<bq and xp<pd<dq. Comparing bq and dq immediately gives the increasing Hamilton path (x,p,b,q,d) or (x,p,d,q,b). The RIGHT-PASS case is dual: pb<bq<qy and pd<dq<qy, and comparing pb,pd gives (b,p,d,q,y) or (d,p,b,q,y). Hence two distinct mixed reentries of the same type force a literal P5. Therefore a P5-free matching-orientation replay family on one physical P4 middle pair has at most two distinct middles, and if two occur they have opposite mixed seam types. This replaces the earlier finite linear-extension check by a one-comparison human proof.

### 1. Fixed transported P4 and its only P5-free local cells
Retain a vertex-simple tight P4

  K=(x,p,q,y).                                             (MC.1)

For a later distinct middle b outside V(K), suppose the matching outer orientation

  J_b=(p,b,q)                                              (MC.2)

is tight. Define the two old boundary seam tests

  alpha_b=(x,p,b),
  beta_b =(b,q,y).                                         (MC.3)

The exact equal-seam theorem SV74696 shows:

- PASS/PASS gives the literal P5 (x,p,b,q,y);
- BAD/BAD also forces a Hamilton P5 on {x,p,q,y,b} by accepted R902;
- therefore every P5-free matching-orientation reentry is MIXED.

Call the two mixed types

  L_b: alpha_b tight and beta_b bad,
  R_b: alpha_b bad and beta_b tight.                       (MC.4)

We now show that neither mixed type can occur at two distinct middles while remaining P5-free.

### 2. Two left-pass mixed middles force a P5
Let b,d be distinct vertices outside {x,p,q,y} such that J_b,J_d are tight and both have type L. Then the following four ordered turns are tight:

  (x,p,b), (p,b,q),
  (x,p,d), (p,d,q).                                       (MC.5)

Consider the five-set

  X_L={x,p,b,d,q}.                                         (MC.6)

Suppose X_L has no Hamilton tight P5. Accepted R902 makes its line-graph comparison orientation acyclic, so by the R887 mechanism there is a strict total order < on the ordinary edges of K_5 realizing every tight turn as an increasing consecutive-edge comparison. From (MC.5),

  xp < pb < bq,
  xp < pd < dq.                                            (MC.7)

Only one comparison remains.

If bq<dq, then

  xp < pb < bq < qd,                                      (MC.8)

so R887 makes

  (x,p,b,q,d)                                              (MC.9)

a tight Hamilton P5 on X_L.

If dq<bq, then

  xp < pd < dq < qb,                                      (MC.10)

so

  (x,p,d,q,b)                                              (MC.11)

is a tight Hamilton P5.

Both alternatives contradict the assumption on X_L. Hence two distinct L-type middles force a literal P5.

### 3. Two right-pass mixed middles force a P5
Now suppose b,d are distinct and both have type R. The tight turns are

  (p,b,q), (b,q,y),
  (p,d,q), (d,q,y).                                       (MC.12)

If the five-set

  X_R={p,b,d,q,y}                                          (MC.13)

were nonHamilton, R902/R887 would give a strict edge order satisfying

  pb < bq < qy,
  pd < dq < qy.                                            (MC.14)

Compare pb and pd. If pb<pd, then

  bp < pd < dq < qy,                                      (MC.15)

so (b,p,d,q,y) is a tight Hamilton P5. If pd<pb, then

  dp < pb < bq < qy,                                      (MC.16)

so (d,p,b,q,y) is a tight Hamilton P5. Contradiction.

Thus two distinct R-type middles also force a literal P5.

### 4. Capacity-two consequence
Combining Sections 1-3:

> For one physical transported P4 K=(x,p,q,y), a P5-free family of distinct matching-orientation reentry middles b with tight (p,b,q) contains at most two vertices. If two occur, one is L-type and the other R-type.

Equivalently, repeated use of one mixed seam polarity has capacity one before P5 amplification. The only possible two-middle P5-free matching packet is the crossed pair

  one LEFT-PASS / RIGHT-BAD middle,
  one LEFT-BAD / RIGHT-PASS middle.                        (MC.17)

This is a physical finite-capacity statement: the middles b,d are named graph vertices and the seam turns are graph-intrinsic. It does not identify alternative exact covers or assert simultaneous current descendants.

### 5. Scope and relation to the earlier finite check
The argument uses only the accepted five-vertex integrability theorem R902 through its R887 edge-order mechanism and the exact equal-seam reduction SV74696. In particular the earlier finite enumeration of compatible edge orders is unnecessary: each same-side pair collapses after one comparison of two ordinary edges.

A P5 is explicit geometry, not numerical phase-zero descent. The crossed two-middle residue (MC.17), and exact replay of one already-used physical middle, may still require a family-level consumer. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```