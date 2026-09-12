# Every same-oriented dimer collision above order ten parent-compiles to the refined three-witness alphabet

**Workspace:** D17
**State:** established
**Key:** `same-dimer-collision-reverse-fan-parent-compiler`

**Summary:** In a hypothetical smallest counterexample, let a tested oriented dimer D=(u,v) have two distinct same-polarity witnesses w1,w2, i.e. an R523 same-dimer collision packet. No pre-existing carrier is needed. For the head case classify every z outside {u,v,w1,w2} by the turn (z,u,v). If at least two such turns are tight, use one new head witness z0 to form the carrier (z0,u,v), leaving w1,w2 and a second new witness exterior to it. If at most one is tight, at least six vertices give bad tests because |H|>10; R3 reverses all of them to (v,u,z), a large tail-witness fan on the reverse tested dimer. Use one fan vertex to form carrier (v,u,z0) and three others as exterior witnesses. The tail case is the exact ordered dual. R429 then supplies the dimer deletion cover and SV44176/SV44695 yield P4/P5, a direct mass-four pair, or R407 in the common parent. Thus the raw R523 collision output of the five-root virtual compiler is not an independent G26 terminal species.

### 1. Input: a raw same-oriented collision, with no carrier assumed
Let H be a hypothetical smallest Strong Level-(1) counterexample. By accepted R533,

  n=|V(H)|>10.                                             (RC.1)

Let

  D=(u,v)                                                  (RC.2)

be one tested oriented physical dimer carrying two distinct same-polarity witnesses w_1,w_2. Thus we retain exactly an R523 HH or TT collision packet. Unlike the short-carrier theorem SV76402, no tight trimer containing D is assumed in advance.

Put

  X=V(H)\{u,v,w_1,w_2}.                                  (RC.3)

Then

  |X|=n-4>=7.                                              (RC.4)

The extra vertex count lets us manufacture a carrier while still leaving three witnesses outside it.

### 2. Head collision
Assume

  (w_1,u,v), (w_2,u,v) are tight.                          (RC.5)

Partition X according to the exact test

  (z,u,v).                                                 (RC.6)

Let A be the vertices z for which (RC.6) is tight and B=X\A.

If |A|>=2, choose distinct z_0,z_1 in A. Then

  K=(z_0,u,v)                                              (RC.7)

is a literal tight trimer containing D as its terminal dimer, while

  w_1,w_2,z_1                                              (RC.8)

are three distinct HEAD witnesses on D, all exterior to K. Pair-deletion rigidity R429 supplies an exact two-cover of H-{u,v}, so the three-witness common-parent compiler SV44176 and refinement SV44695 apply.

Suppose |A|<=1. Then |B|>=|X|-1>=6. For every z in B the turn (z,u,v) is bad, so R3 gives its exact complete reversal

  (v,u,z) tight.                                           (RC.9)

Thus the reverse tested orientation

  D^op=(v,u)                                               (RC.10)

is TAIL-signed by every vertex of B. Choose four distinct z_0,z_1,z_2,z_3 in B. The turn

  K'=(v,u,z_0)                                             (RC.11)

is a literal tight trimer with initial dimer D^op, and z_1,z_2,z_3 are three exterior tail witnesses. R429 plus SV44176/SV44695 apply to D^op in K'.

Hence every head collision produces the refined three-witness output alphabet without any paid continuation.

### 3. Tail collision
Assume instead

  (u,v,w_1), (u,v,w_2) are tight.                          (RC.12)

Partition X by whether

  (u,v,z)                                                  (RC.13)

is tight. If at least two vertices z_0,z_1 pass, use

  K=(u,v,z_0)                                              (RC.14)

as a tight carrier and retain w_1,w_2,z_1 as three exterior TAIL witnesses on D.

If at most one passes, at least six fail. For every failed z, R3 gives

  (z,v,u) tight,                                           (RC.15)

so D^op=(v,u) is HEAD-signed by at least six vertices. Choose four distinct z_0,z_1,z_2,z_3 among them;

  K'=(z_0,v,u)                                             (RC.16)

is the literal reverse-orientation carrier, with z_1,z_2,z_3 exterior head witnesses. Again R429 and SV44176/SV44695 apply.

Every ordered turn used here is displayed; no cyclic permutation or informal reversal convention is used.

### 4. Collision-elimination theorem
Therefore every R523 same-oriented-dimer collision packet in a surviving smallest counterexample yields, in a common parent before generic payment, at least one of

  literal tight P4,
  literal tight P5,
  direct graph-intrinsic opposite-sign mass-four pair,
  R407 bidirectional same-witness dimer interaction.       (RC.17)

The construction either uses the original orientation D and a newly chosen same-polarity carrier witness, or the reverse orientation D^op and a newly exposed opposite carrier fan. The physical support {u,v} is unchanged.

### 5. G26 consequence
The R523 collision output in the current five-root physical compiler SV76063 is therefore not an independent terminal symbol. Together with SV76402, the same conclusion applies in particular to every R542 two-witness collision packet before its payment branch is chosen.

This does not consume the four outputs in (RC.17). In particular, a direct balanced pair may pay and return flat at phase zero, and R407 is an interaction certificate rather than numerical descent. The gain is an alphabet reduction: raw same-oriented collision labels cannot support a closed rank-flat family by themselves. R24 and R5 are unused.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```