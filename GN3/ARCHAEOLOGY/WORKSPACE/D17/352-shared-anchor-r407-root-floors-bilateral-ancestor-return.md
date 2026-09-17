# The repeated-certificate R407 root fork returns both root floors with literal bilateral ancestors

**Workspace:** D17
**State:** established
**Key:** `shared-anchor-r407-root-floors-bilateral-ancestor-return`

**Summary:** Refine the R407 branch of SV74357 using the shared xi-birth trimer itself. In the HEAD case the common certificate is (xi,u) head-signed by w, so T=(w,xi,u) is tight and its initial dimer M=(w,xi) is tail-signed by u with anchor xi. The same-end attachment failure gives both root-dimer orientations (d,e),(e,d) head-signed by the common boundary witness p0. Since d,e are disjoint from {w,xi,u}, M pairs directly with each root orientation as a disjoint opposite-polarity mass-four pair. R514 pays each alternative birth and R432 steers its floor to {xi,d} or {xi,e}. The graph-intrinsic dimers persist, so the {xi,d} floor carries M=(w,xi) tail and (d,e) head, while {xi,e} carries M=(w,xi) tail and (e,d) head. These are exactly bilateral ancestor packets for SV57993. The TAIL case is dual. Thus the R407 residue does not remain an opaque fixed-trimer interaction: each alternative root branch returns to its original pair with nontrivial literal endpoint ancestors, after which every later same-orientation turn is P4/reverse-trimer/adjacent-reversal constrained. No bottom-family extinction or rank decrease is claimed.

### 1. Input: the R407 branch of the repeated-certificate diamond
Retain the ROOT-DIMER INTERACTION branch of `virtual-shared-anchor-two-root-common-residue-diamond` SV74357. Thus d,e are two distinct roots of the retained five-root packet, xi is the common center, and the two root source frames share one identical xi-anchored R434 certificate.

Treat the HEAD case first. Write the common certificate as

  D=(xi,u) head-signed by w,
  so T=(w,xi,u) is tight.                                 (RB.1)

The same-end endpoint-attachment obstruction in SV74357 supplies one common base-rail boundary witness p_0 and

  (p_0,d,e) tight,
  (p_0,e,d) tight.                                       (RB.2)

Hence both tested orientations of the physical root dimer are head-signed by p_0. The exact root and certificate construction gives

  {d,e} disjoint from {w,xi,u}.                           (RB.3)

### 2. Use the opposite terminal dimer of the shared xi-trimer
The tight trimer T=(w,xi,u) has initial dimer

  M=(w,xi),                                               (RB.4)

and (w,xi,u) says precisely that M is tail-signed by witness u, with signed tail anchor xi.

Now read the two root orientations separately:

  R_d=(d,e) head-signed by p_0, anchor d;
  R_e=(e,d) head-signed by p_0, anchor e.                 (RB.5)

By (RB.3), M is physically disjoint from each R_d,R_e. Therefore

  M | R_d,
  M | R_e                                                 (RB.6)

are two graph-intrinsic direct opposite-sign balanced pairs of total support mass four. They are alternative pair births from one shared parent packet; no simultaneous active descendants are asserted.

### 3. Return the first pair to the original root floor {xi,d}
Apply accepted R514 to M|R_d. It yields TWO-COVER or an ancestry-bearing mass-two floor while retaining T,M,R_d and their exact witness data as graph-intrinsic historical facts. In the nonclosing branch apply accepted R432 with prescribed target pair

  E_d={xi,d}.                                             (RB.7)

At the returned E_d-floor, retain

  L_d=M=(w,xi) tail-signed by u,
  R_d=(d,e) head-signed by p_0.                           (RB.8)

Thus the two signed anchors are exactly xi and d, the coordinates of the returned floor. This is a literal bilateral ancestor packet of the same form used by SV57993.

### 4. The reverse root orientation returns the other original floor
Apply the same construction alternatively to M|R_e. Outside TWO-COVER, R514 followed by R432 with target

  E_e={xi,e}                                             (RB.9)

returns an ancestry-bearing floor carrying

  L_e=M=(w,xi) tail-signed by u,
  R_e=(e,d) head-signed by p_0.                          (RB.10)

Again the anchors are exactly the floor coordinates xi,e.

The two returned floors are alternative descendants of the common R407 parent; the durable simultaneous data are the shared trimer T, its dimer M, both root-dimer orientations and their witnesses.

### 5. Immediate replay-breaker consequence
At the E_d-floor, any later proper turn with the matching outer orientation

  J'=(xi,b,d)                                            (RB.11)

meets the exact local hypotheses of `fully-anchored-pre-singleton-replay-breaker` SV57993 with ancestors (RB.8). Therefore independently at both endpoints the turn produces a literal P4, a labelled reverse trimer, or an adjacent reversal; when the two extension seams pass with distinct secondary vertices they concatenate to a P5.

The same statement holds at E_e with packet (RB.10). No claim is made for the complete-reversal outer orientation, which must be analyzed separately.

Thus the R407 branch of SV74357 is not an opaque fixed-trimer interaction state. It reconstructs both original root pairs with concrete nontrivial endpoint ancestors attached.

### 6. TAIL dual
If the common repeated certificate is TAIL, write it as

  D=(u,xi) tail-signed by w,
  so (u,xi,w) is tight.                                  (RB.12)

Use the terminal dimer

  M=(xi,w),                                               (RB.13)

which is head-signed by u with signed head anchor xi. The terminal same-end root fork in SV74357 makes both root-dimer orientations tail-signed by one common boundary witness. Pair M with each root orientation. The polarity and endpoint order are the exact dual of Sections 2--5, yielding floors {d,xi},{e,xi} with the corresponding bilateral ancestor packets.

### 7. Scope fence
This theorem does not count either R514 payment as a decrease at the exhausted phase-zero clock, does not assert the two paid descendants coexist, and does not by itself consume the P4/reverse/reversal packet after return. Its role is a family-interface refinement: the only nonmerging root-dimer branch of SV74357 is forced back into the same literal bilateral-ancestor language used elsewhere in the current G27 development.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R432"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    }
]
```