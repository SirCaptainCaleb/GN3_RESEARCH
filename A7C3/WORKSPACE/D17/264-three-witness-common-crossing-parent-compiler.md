# Three same-polarity witnesses force a same-parent interaction on one physical deletion crossing

**Workspace:** D17
**State:** established
**Key:** `three-witness-common-crossing-parent-compiler`

**Summary:** Let K be a tight carrier containing an oriented signed dimer S=(a,b), and suppose three distinct same-polarity witnesses w1,w2,w3 all lie outside K. In any exact two-cover T of H-S, R508 forces a selected crossing between C=V(K)-V(S) and E=V(H)-V(K). Such a crossing has only one exterior endpoint, so it avoids at least two witnesses. Instead of running R527 into alternative descendants, inspect the underlying R526 actualization tests in the common parent frame. If the crossing avoids all three witnesses, three binary tests pigeonhole two witnesses into the same outcome, giving an immediate R523 same-oriented-dimer two-head or two-tail collision. If the crossing uses one witness w3, test the other two after orienting the marker through w3. Equal outcomes again give an R523 collision. In the only mixed outcome, the original sign certificate of w3 resolves the split: one additional seam test gives either a literal tight P4 or a literal tight P5, with all physical labels retained. The tail-signed case has an explicit dual calculation. Therefore three witnesses are exactly enough to remove the alternative-descendant loophole: one common selected crossing already carries graph-intrinsic collision/P4/P5 geometry before any payment lineage begins. Applied to either boundary dimer of the Arm-M cap frame SV42382, every exact deletion cover has such a same-parent interaction.


### 1. Setup: keep all three witnesses in the common parent
Let H be a finite Strong Level-(1) boundary tournament with pc(H)>2. Let

  K

be a vertex-simple tight carrier path, let

  S=(a,b)                                                   (TW.1)

be one tested oriented dimer contained in K, and put

  C=V(K)-V(S),
  E=V(H)-V(K).                                              (TW.2)

Assume C and E are nonempty. Suppose S has THREE distinct same-polarity witnesses

  W={w_1,w_2,w_3} subset E.                                (TW.3)

Thus all three witnesses are physically exterior to the whole carrier, not merely exterior to S.

Let

  T=T_1|T_2                                                (TW.4)

be any exact two-cover of H-V(S). Apply accepted R508 with deletion block D=V(S), remainder block C, and absorbable path Q=K. Since K spans exactly D union C, T selects a physical adjacent state with one endpoint in C and the other in E. Write its unordered physical endpoints as

  {c,e},   c in C, e in E.                                 (TW.5)

Its selected direction in T is retained as part of the T-frame, but below we use {c,e} only as a two-vertex marker. R526/R527 explicitly allow choosing the marker orientation for actualization; this does NOT assert that the chosen orientation was selected in T.

Because c lies in C while every w_i lies in E, the marker can meet W only at e. Therefore it avoids at least two of the three witnesses.

The point is to stop BEFORE R527 creates alternative descendants and inspect the graph-intrinsic R526 terminal tests themselves.

### 2. Crossing avoids all three witnesses: binary pigeonhole gives immediate collision
Assume first

  e notin W.                                                (TW.6)

Suppose S is head-signed by all three witnesses, so

  (w_i,a,b) is tight,  i=1,2,3.                            (TW.7)

Choose the marker orientation

  M=(c,e).                                                  (TW.8)

For witness w_i the head-signed actualization proof R526 tests exactly

  t_i=(c,e,w_i).                                            (TW.9)

There are only two possible outcomes.

- If t_i is tight, then the tested oriented marker dimer (c,e) is tail-signed by w_i.
- If t_i is bad, R3 gives its complete reversal

    (w_i,e,c) tight,                                       (TW.10)

  so the reverse tested marker dimer (e,c) is head-signed by w_i.

Three witnesses occupy two outcome classes. Hence two distinct witnesses, say w_i,w_j, lie in the same class. In the first class R523 sees two tail certificates on the SAME tested orientation (c,e). In the second class R523 sees two head certificates on the SAME tested orientation (e,c). Thus the common parent already contains an explicit same-support two-extension collision packet.

For a tail-signed S the calculation is equally literal. R526 tests

  (w_i,c,e).                                               (TW.11)

A tight test head-signs (c,e) by w_i; a bad test reverses by R3 to

  (e,c,w_i) tight,                                        (TW.12)

which tail-signs the reverse marker (e,c) by w_i. Again three binary outcomes force an R523 same-oriented-dimer collision.

No actualized support has been spent and no two witness descendants have been asserted to coexist.

### 3. Crossing uses the third witness: equal outcomes still collide
Now assume the exterior crossing endpoint is itself one witness. Relabel so

  e=w_3.                                                    (TW.13)

The physical crossing {c,w_3} avoids w_1,w_2, so both corresponding R526 tests are legal in the SAME T-frame.

First suppose S is head-signed. Choose marker orientation

  M=(w_3,c).                                                (TW.14)

For i=1,2 the R526 tests are

  t_i=(w_3,c,w_i).                                         (TW.15)

If both are tight, (w_3,c) is tail-signed by both w_1,w_2, an R523 TT collision. If both are bad, R3 gives

  (w_1,c,w_3), (w_2,c,w_3) tight,                          (TW.16)

so the reverse tested dimer (c,w_3) is head-signed by both w_1,w_2, an R523 HH collision.

Thus only the split outcome needs work.

### 4. The mixed split is resolved by the witness consumed by the crossing
Assume after swapping w_1,w_2 if necessary that

  (w_3,c,w_1) is tight,                                    (TW.17)

while t_2 is bad. R3 then gives

  (w_2,c,w_3) is tight.                                    (TW.18)

Because w_3 is the third original head witness of S,

  (w_3,a,b) is tight.                                      (TW.19)

Test the single parent-frame seam

  sigma=(c,w_3,a).                                         (TW.20)

If sigma is tight, the three consecutive turns (TW.18), (TW.20), (TW.19) concatenate to the literal vertex-simple tight P5

  (w_2,c,w_3,a,b).                                         (TW.21)

If sigma is bad, R3 gives

  (a,w_3,c) tight.                                         (TW.22)

Together with (TW.17) this gives the literal tight P4

  (a,w_3,c,w_1).                                           (TW.23)

All five/four vertices are distinct: a,b lie in S; c lies in C; and w_1,w_2,w_3 lie in E and are pairwise distinct.

Hence even the unique binary split that defeats a two-witness pigeonhole is not an alternative-descendant escape. The witness used by the selected crossing closes the split inside the original parent frame.

### 5. Explicit tail-signed calculation
Suppose instead S is tail-signed by all three witnesses:

  (a,b,w_i) tight,  i=1,2,3.                               (TW.24)

When e=w_3 choose

  M=(c,w_3).                                                (TW.25)

The tail-signed R526 test for witness w_i is

  t_i=(w_i,c,w_3),  i=1,2.                                 (TW.26)

Equal outcomes give the same immediate R523 collision: two tight tests head-sign (c,w_3) by w_1,w_2; two bad tests reverse to

  (w_3,c,w_1), (w_3,c,w_2) tight,                          (TW.27)

so (w_3,c) is tail-signed by both.

In the mixed case, after swapping w_1,w_2 if necessary, retain

  (w_1,c,w_3) tight,                                       (TW.28)

and from a bad t_2 obtain

  (w_3,c,w_2) tight.                                       (TW.29)

The third original sign certificate is

  (a,b,w_3) tight.                                         (TW.30)

Test

  sigma'=(b,w_3,c).                                        (TW.31)

If sigma' is tight, (TW.30),(TW.31),(TW.29) concatenate to the literal tight P5

  (a,b,w_3,c,w_2).                                         (TW.32)

If sigma' is bad, R3 gives

  (c,w_3,b) tight.                                         (TW.33)

Together with (TW.28) this gives the literal tight P4

  (w_1,c,w_3,b).                                           (TW.34)

Thus the head and tail cases are both proved by displayed ordered turns; no informal reversal symmetry is being used.

### 6. Three-witness same-parent interaction theorem
Combining Sections 2-5 gives the order-free compiler:

> Let one tested oriented signed dimer S lie in a tight carrier K and have at least three distinct same-polarity witnesses outside K. For any exact two-cover of H-S, choose any R508 carrier/exterior selected crossing. Then, in the common parent frame and before any R527/R526 payment descendant is chosen, one obtains either
>
> - an R523 same-oriented-dimer two-head/two-tail collision packet on the physical crossing marker or its reverse, or
> - a literal graph-intrinsic tight P4, or
> - a literal graph-intrinsic tight P5.

The theorem is genuinely a SAME-PARENT statement. The two witness-indexed R527 actualizations need never be declared simultaneous. Their terminal tests are simultaneous graph facts in the original frame, and the third witness is exactly what resolves the only split pattern.

The number three is structurally sharp for this proof mechanism. With only two witnesses avoiding the marker, the two binary actualization tests may split and there is no third witness forced onto the crossing to provide the splice turn (TW.19) or (TW.30).

### 7. Arm-M consequence: every boundary-wall deletion frame is already interactive
Now apply the theorem to the universal Arm-M cap wall SV42382. In an arbitrary pair-deletion frame

  H-{x,y}=A|B,
  A=(a_0,...,a_{k-1}),
  B=(b_0,...,b_{k-2}),                                    (TW.35)

its reverse terminal boundary dimer

  D_R=(a_{k-1},a_{k-2})                                   (TW.36)

is head-signed by the three distinct exterior witnesses

  {x,y,b_0},                                               (TW.37)

while its reverse initial boundary dimer

  D_L=(a_1,a_0)                                            (TW.38)

is tail-signed by

  {x,y,b_{k-2}}.                                           (TW.39)

Take K=A. For either S=D_R or S=D_L, accepted smallest-counterexample deletion gives an exact two-cover of H-S, and R508 forces a selected crossing between A-S and V(H)-A. All three witnesses in (TW.37) or (TW.39) lie outside A. Hence the common-parent compiler applies on BOTH ends of every cap rail.

Therefore every Arm-M pair-deletion cap frame carries, at each reverse boundary dimer, an immediate graph-intrinsic output

  R523 COLLISION  or  literal P4  or  literal P5,          (TW.40)

before any aligned refund/payment lineage begins.

In the live large-k range these P4/P5 paths are proper and may be currentized by accepted R4 if a literal maximum-forest representative is desired, but currentization is not needed for the same-parent conclusion.

This removes the exact loophole highlighted in G16: the three witness captures do not need to coexist as alternative descendants. Their common R526 test geometry has already interacted upstream.


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
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R526"
    }
]
```