# HHH quiet packet plus fixed complement has one-turn complementary-role splices

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-r961-hhh-role-splice`

**Summary:** In the fixed-complement HHH packet, three puncture paths share the same literal complement Q. Testing one boundary turn from each of the three anchor labels into the source end of Q gives either a spanning two-cover or a full three-witness reverse-boundary fan on Q. Dually testing terminal attachments gives the opposite fan. Hence failure of all six role-correct one-turn splices produces two-ended three-witness shields on the fixed complement, with no support transport or R435 payment.

### Setup
Retain the fixed-complement critical-block HHH packet from `fixed-complement-critical-block-common-parent`. Thus Omega=Y union M with anchor triangle labels Y={y_0,y_1,y_2}, literal common complement

  Q=(q_0,q_1,...,q_t),

and three actual singleton-deletion covers whose active rails are

  P_i=(y_{i+1},y_{i+2},M)

cyclically, each paired with the SAME literal Q. The exact indexing is immaterial; what matters is that deleting y_i leaves the other two Y labels followed by the common remainder M.

### Source-end complementary splices
Fix i. Consider attaching the omitted label y_i to the source of Q, producing candidate rail

  (y_i,q_0,q_1,...,q_t).

Its only new turn is

  s_i=(y_i,q_0,q_1).

If s_i is tight, pair this rail with the active puncture path P_i on Omega-y_i. Their supports are disjoint and partition H, giving a spanning two-cover. Therefore in a counterexample every s_i is bad. Boundary antisymmetry gives

  (q_1,q_0,y_i) tight

for all three i.

Thus the reverse source boundary dimer (q_1,q_0) of Q has all three anchor labels as tail witnesses.

### Terminal-end complementary splices
Dually test

  t_i=(q_{t-1},q_t,y_i).

If t_i is tight, Q-y_i terminal extension paired with P_i closes H. Hence all t_i are bad and R3 gives

  (y_i,q_t,q_{t-1}) tight

for all i.

So the reverse terminal boundary dimer (q_t,q_{t-1}) has all three anchor labels as head witnesses.

### Output
The HHH fixed-complement packet therefore carries a TWO-ENDED THREE-WITNESS WALL on Q:

  (q_1,q_0,y_i) tight,
  (y_i,q_t,q_{t-1}) tight

for every y_i in Y.

This is derived directly from one-turn spanning-cover tests; no R542/R523 payment or endpoint-accessibility theorem is needed. The TTT packet has the same conclusion because the puncture supports are identical; only their internal active orders differ.

### Scope
The two-ended wall alone does not close H and does not imply R561 on Q. It should be combined with active-side transfer geometry or a second Q representative before being spent as generic collision currency. The three witness identities and the literal Q order are the retained interface.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
