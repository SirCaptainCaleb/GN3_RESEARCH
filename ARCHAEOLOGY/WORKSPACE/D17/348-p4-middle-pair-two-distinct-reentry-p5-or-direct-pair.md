# Two distinct matching reentries on one transported P4 force P5 or a direct mass-four pair

**Workspace:** D17
**State:** established
**Key:** `p4-middle-pair-two-distinct-reentry-p5-or-direct-pair`

**Summary:** Let K=(x,p,q,y) be a tight P4 and let b,d be two distinct later middles with matching outer orientation (p,b,q),(p,d,q) tight. SV74696 already kills equal seam parity at either middle by a Hamilton P5. SV77447 kills two mixed middles of the same type. In the only remaining crossed mixed cell, orient b as LEFT-PASS/RIGHT-BAD and d as LEFT-BAD/RIGHT-PASS. Then (x,p,b),(p,b,q),(y,q,b),(d,p,x),(p,d,q),(d,q,y) are tight. Test (b,q,d): if tight, (x,p,b,q,d) is P5; otherwise R3 gives (d,q,b). Test (b,p,d): if tight, (b,p,d,q,y) is P5; otherwise R3 gives (d,p,b). In the double-failure branch the disjoint dimers (d,p) and (q,b) have opposite polarity: (d,p) is tail-signed by external witness x using (d,p,x), while (q,b) is head-signed by external witness y using (y,q,b). Hence R514 gives a direct graph-intrinsic mass-four balanced pair. Therefore any two distinct matching reentry middles on one physical transported P4 force P5 or direct mass-four pair. The only matching-orientation replay that can avoid both outputs is exact reuse of a single physical middle.

### 1. Setup and prior reductions
Retain a vertex-simple tight P4

  K=(x,p,q,y).                                             (DM.1)

Let b,d be two distinct vertices outside V(K) such that the matching-orientation turns

  J_b=(p,b,q),
  J_d=(p,d,q)                                              (DM.2)

are tight. We compare their two old boundary seam tests against K:

  alpha_z=(x,p,z),
  beta_z =(z,q,y),   z in {b,d}.                           (DM.3)

Accepted working unit SV74696 says that PASS/PASS or BAD/BAD at either z already produces a Hamilton tight P5 on the corresponding five-set. Thus if no P5 has yet appeared, both b and d are MIXED.

Current unit SV77447 says that two distinct mixed middles of the SAME type also force a P5. Therefore the only still-unconsumed two-middle pattern is the crossed mixed cell. After interchanging b,d if necessary, normalize it as

  alpha_b PASS, beta_b BAD,
  alpha_d BAD,  beta_d PASS.                              (DM.4)

We now consume this cell exactly.

### 2. Literal turns in the crossed mixed cell
From (DM.1), (DM.2), and the two passing seams we retain

  (x,p,b),
  (p,b,q),
  (p,d,q),
  (d,q,y)                                                  (DM.5)

as tight turns.

The failed right seam at b is

  (b,q,y) bad.                                             (DM.6)

Boundary antisymmetry R3 gives its exact complete reversal

  (y,q,b) tight.                                           (DM.7)

The failed left seam at d is

  (x,p,d) bad,                                             (DM.8)

so R3 gives

  (d,p,x) tight.                                           (DM.9)

Every vertex and order in (DM.5)-(DM.9) is physical and graph-intrinsic; no exact cover is identified with another.

### 3. Two probes
First inspect the reversal pair at middle q on {b,q,d}.

If

  (b,q,d) tight,                                           (DM.10)

then (DM.5) gives the literal Hamilton tight P5

  (x,p,b,q,d).                                             (DM.11)

Hence in the no-P5 branch R3 forces

  (d,q,b) tight.                                           (DM.12)

Next inspect the reversal pair at middle p on {b,p,d}. If

  (b,p,d) tight,                                           (DM.13)

then together with (p,d,q) and (d,q,y) we obtain the literal Hamilton tight P5

  (b,p,d,q,y).                                             (DM.14)

Thus the only branch with neither displayed P5 has

  (d,p,b) tight.                                           (DM.15)

### 4. The double-failure branch is a direct mass-four pair
In the branch (DM.12)+(DM.15), consider the two oriented dimers

  D_T=(d,p),
  D_H=(q,b).                                               (DM.16)

They are physically disjoint because b,d are distinct reentry middles outside the four vertices x,p,q,y.

By (DM.9),

  (d,p,x) tight,                                           (DM.17)

so D_T is TAIL-signed by the external witness x. We deliberately use x, not the alternate witness b from (DM.15), so the sign witness is outside both dimer supports.

By (DM.7),

  (y,q,b) tight,                                           (DM.18)

so D_H is HEAD-signed by the external witness y. Again y is outside both dimer supports.

Therefore D_T and D_H are disjoint opposite-polarity signed dimers with literal external sign witnesses x and y. Accepted R514 applies and gives a direct graph-intrinsic mass-four balanced pair

  (d,p)  perpendicular  (q,b).                            (DM.19)

No paid-floor ancestry is inferred merely from (DM.19); R514 is exactly the lawful direct-pair entrance if one later chooses to pay it.

### 5. Two-distinct-middle theorem
Combining SV74696, SV77447, and Sections 2-4 yields:

> For one physical transported P4 K=(x,p,q,y), any two distinct matching-orientation reentry middles b,d with (p,b,q) and (p,d,q) tight force either a literal tight Hamilton P5 on five of the named vertices or a direct graph-intrinsic mass-four balanced pair on two disjoint named dimers.

Equivalently, after quotienting P5 and direct-pair exits, the matching-orientation replay relation on one P4 middle pair has capacity ONE in physical middles. The only remaining matching replay that can avoid both outputs is exact reuse of the same physical middle.

This is a local alphabet reduction, not phase-zero numerical descent. A direct R514 pair may be paid and may return rank-flat at the exhausted phase-zero clock. The gain is that a reconstruction-closed G26 family cannot support a sequence of distinct matching reentry middles without emitting one of these two explicit side exits. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    }
]
```