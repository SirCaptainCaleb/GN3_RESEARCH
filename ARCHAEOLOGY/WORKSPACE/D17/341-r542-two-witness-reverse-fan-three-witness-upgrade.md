# Every short-carrier two-witness packet upgrades to a three-witness common-parent interaction before payment

**Workspace:** D17
**State:** established
**Key:** `r542-two-witness-reverse-fan-three-witness-upgrade`

**Summary:** Let K be a tight trimer in a hypothetical smallest counterexample and let one tested oriented boundary dimer S=(u,v) of K carry two distinct same-polarity witnesses outside K, as in an R542-ready packet. Since |H|>10, after removing K and the two witnesses at least six vertices remain. In the head-signed case, test (z,u,v) on those vertices. If any test is tight, S immediately has a third exterior head witness. If every test is bad, R3 makes (v,u,z) tight for all six, so the reverse tested dimer (v,u) is tail-signed by a large witness fan. Choose one fan vertex z0 to form the tight reverse carrier (v,u,z0) and three further fan vertices as exterior witnesses. The tail-signed case is the exact ordered dual: either S gets a third tail witness or the reverse tested dimer becomes head-signed by the remaining vertices and is placed in carrier (z0,v,u). R429 supplies the exact deletion cover in either orientation, so SV44176 and SV44695 apply in the common parent before any R542 payment. Therefore every R542-ready short-carrier packet already yields a literal P4/P5, a direct mass-four balanced pair, or an R407 bidirectional interaction. R542 payment recycling is not an independent phase-zero family species.

### 1. Input: one literal two-witness short-carrier packet
Let H be a hypothetical smallest Strong Level-(1) counterexample. Accepted R533 gives

  n=|V(H)|>10.                                             (RF.1)

Retain a vertex-simple tight trimer K and one tested oriented boundary dimer

  S=(u,v)                                                  (RF.2)

of K. Suppose two distinct vertices w_1,w_2 outside K give S the same polarity. This is exactly the local signed datum of an R542-ready short-carrier packet. No R542 continuation is chosen.

Because K has three vertices and w_1,w_2 lie outside K, the reservoir

  X=V(H)\(V(K) union {w_1,w_2})                           (RF.3)

has

  |X|=n-5>=6.                                              (RF.4)

We show that the parent packet already contains a three-witness carrier packet, possibly on the reverse tested orientation of the same physical dimer.

### 2. Head-signed case
Assume S=(u,v) is head-signed by w_1,w_2, so

  (w_1,u,v), (w_2,u,v) are tight.                          (RF.5)

For each z in X inspect the exact ordered turn

  (z,u,v).                                                 (RF.6)

If (RF.6) is tight for some z, then w_1,w_2,z are three distinct head witnesses on the SAME tested orientation S=(u,v), and all three are exterior to the original carrier K. Accepted pair-deletion rigidity R429 supplies an exact two-cover of H-{u,v}. Therefore the three-witness same-parent compiler SV44176 and its refinement SV44695 apply immediately.

Suppose instead every turn (z,u,v), z in X, is bad. Boundary antisymmetry R3 gives the complete reversals

  (v,u,z) tight for every z in X.                          (RF.7)

Thus the reverse tested dimer

  S^op=(v,u)                                               (RF.8)

is TAIL-signed by every vertex of X. Choose four distinct vertices

  z_0,z_1,z_2,z_3 in X.                                   (RF.9)

The turn (v,u,z_0) from (RF.7) makes

  K'=(v,u,z_0)                                             (RF.10)

a literal tight trimer containing S^op as its initial dimer. The three vertices z_1,z_2,z_3 are distinct tail witnesses on S^op and lie outside K'. Again R429 supplies an exact two-cover of H-{u,v}=H-V(S^op), so SV44176/SV44695 apply to the literal reverse-orientation carrier K'.

No cyclic rereading has occurred: (RF.7) is the exact complete reversal of the failed test (RF.6), and K' is displayed in the order certified by (RF.7).

### 3. Tail-signed case
Assume instead S=(u,v) is tail-signed by w_1,w_2, so

  (u,v,w_1), (u,v,w_2) are tight.                          (RF.11)

For each z in X inspect

  (u,v,z).                                                 (RF.12)

If some (RF.12) is tight, then S has three distinct exterior tail witnesses and SV44176/SV44695 apply in the original carrier K.

If every (RF.12) is bad, R3 gives

  (z,v,u) tight for every z in X.                          (RF.13)

Hence S^op=(v,u) is HEAD-signed by every z in X. Choose four distinct z_0,z_1,z_2,z_3 in X. The certified turn

  K'=(z_0,v,u)                                             (RF.14)

is a literal tight trimer containing S^op as its terminal dimer, while z_1,z_2,z_3 are three exterior head witnesses. R429 plus SV44176/SV44695 again give the same common-parent output alphabet.

This is the exact ordered dual of Section 2; no informal reversal of a tight turn is used.

### 4. Prepayment output theorem
Combining the two polarity cases with the refined three-witness compiler, every packet satisfying Section 1 yields, before any R542 payment descendant is chosen, at least one of

  literal tight P4,
  literal tight P5,
  direct graph-intrinsic opposite-sign mass-four pair,
  R407 bidirectional same-witness dimer interaction.       (RF.15)

The output may arise on S in the original carrier K or on the reverse tested orientation S^op in the explicitly constructed reverse carrier K'. In both branches the physical dimer support {u,v} is unchanged, every witness is named, and the exact carrier order is retained.

### 5. G26 consequence: R542 payment recycling is not a bottom-family species
In particular, every R542-ready two-witness packet occurring in the hard-run chain SV73346 is already consumed at parent scale by (RF.15). The later R542 capture/payment continuation remains valid and may still be useful for ancestry, but it is no longer needed merely to escape the two-witness packet. Therefore a reconstruction-closed phase-zero bottom family cannot use repeated R542 payment/return as an independent terminal symbol: before that choice it must already contain one of the four physical outputs in (RF.15).

This strictly sharpens the geometric P4 extraction of SV73681 and the prepayment synchronization analysis SV75037 at the level of the family alphabet. It does NOT claim that P4/P5 geometry, a direct mass-four pair, or R407 is numerical phase-zero descent; those are the remaining physical species to consume. No paid descendants are asserted simultaneously current. R24 and R5 are unused.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R533"
    }
]
```