# A direct source-wall P4 is Hamiltonian on five vertices unless both anchors share the wall

**Workspace:** D17
**State:** established
**Key:** `g36-direct-wall-p4-star-cycle-or-twin-anchor-wall`

**Summary:** In the DIRECT P4 arm of SV115482, one additional test against the other source anchor eliminates an arbitrary source-wall P4. OUT: retain (d,b,t), (b,t,A), and the historical source turn (A,t,C). Test (b,t,C). If it is tight, the common wall prefix gives both P4s (d,b,t,A) and (d,b,t,C). If it is bad, R3 gives (C,t,b), so the ordinary comparison edges tb,tA,tC form the directed star triangle tb->tA->tC->tb. By R887 the induced five-set {A,C,t,b,d} is nonintegrable, while accepted R902 says every non-Hamiltonian five-vertex boundary tournament is edge-orderable; hence this five-set has a Hamilton P5. The IN-dual is identical: either both (C,t,b,d) and (A,t,b,d) are tight, or the anchor test creates the star triangle tA->tC->tb->tA and the same five-set is Hamiltonian. Thus the only P5-free DIRECT wall-P4 residue is a twin-anchor wall, not an arbitrary P4. This is a local contraction, not yet a full-H splice or transition descent.

### 1. OUT direct-wall input
Retain the OUT orientation of the source-gate wall packet in SV115482 and suppose its first source test lands in the DIRECT P4 branch. Thus the graph-intrinsic turns

  (d,b,t),   (b,t,A),   (A,t,C)                           (TW.1)

are tight. The first two concatenate to the literal P4

  K_A=(d,b,t,A).                                          (TW.2)

Here t is the physical source spoke, A,C are the retained source anchors, and b->d is the fixed far selected boundary from the persistent wall.

### 2. Test the other source anchor
Test

  (b,t,C).                                                 (TW.3)

If (TW.3) is tight, then the same wall turn (d,b,t) gives a second literal P4

  K_C=(d,b,t,C).                                          (TW.4)

Thus both anchors share one physical wall prefix (d,b,t).

Suppose instead that (TW.3) is bad. Boundary antisymmetry R3 gives

  (C,t,b) tight.                                          (TW.5)

Pass to the comparison orientation of R887 on the ordinary edges incident with t. The three certified turns in (TW.1),(TW.5) say exactly

  tb -> tA,   tA -> tC,   tC -> tb.                       (TW.6)

Hence the induced five-set

  Z={A,C,t,b,d}                                            (TW.7)

has a directed star triangle in its comparison orientation and is therefore nonintegrable. If Z had no tight Hamilton P5, accepted R902 would make every non-Hamiltonian five-vertex boundary tournament edge-orderable, equivalently integrable, contradiction. Therefore Z contains a tight Hamilton P5.

Consequently the OUT direct branch has the exact alternative:

  HAMILTON-5 on {A,C,t,b,d},
  or the twin-anchor wall K_A=(d,b,t,A), K_C=(d,b,t,C).    (TW.8)

### 3. IN direct-wall dual
Retain the IN orientation of SV115482 in its DIRECT P4 branch. Then

  (A,t,C),   (C,t,b),   (t,b,d)                           (TW.9)

are tight, giving K_C=(C,t,b,d). Test (A,t,b).

If (A,t,b) is tight, then

  K_A=(A,t,b,d)                                           (TW.10)

is a second literal P4 sharing the wall suffix (t,b,d).

If (A,t,b) is bad, R3 gives (b,t,A). The three turns

  (A,t,C),   (C,t,b),   (b,t,A)                           (TW.11)

produce the directed star triangle

  tA -> tC -> tb -> tA.                                   (TW.12)

Again R887 and R902 imply that the exact five-set {A,C,t,b,d} has a Hamilton P5.

### 4. Consequence and scope
A DIRECT source-wall P4 cannot remain an untyped one-anchor path. Either the exact five-vertex support consisting of both source anchors, the source spoke, and the two wall vertices is Hamiltonian, or both anchors participate in the same wall geometry: in OUT they give two P4s with common prefix (d,b,t), and in IN they give two P4s with common suffix (t,b,d).

This does not assert that the Hamilton P5 or twin-anchor wall already two-covers H, and it does not claim a strict transition descent. It is a local parent contraction for the G36 absorber. The collision arm is handled separately by SV117188. No payment, replay, R24, or R5 is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
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
