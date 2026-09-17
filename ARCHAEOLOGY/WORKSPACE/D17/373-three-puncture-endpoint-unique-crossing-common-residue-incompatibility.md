# The two endpoint puncture rows cannot both be quiet unique-crossing rows

**Workspace:** D17
**State:** established
**Key:** `three-puncture-endpoint-unique-crossing-common-residue-incompatibility`

**Summary:** For K=(x,a,y,c,z) and W=H-K, work outside the higher-W-block R159 branch so the endpoint rows H-x,H-z each have exactly two W-blocks. If both rows had exactly one petal|W transition, R560 plus R435 forces their petal blocks to be the literal source paths P_x=(a,y,c,z), P_z=(x,a,y,c) outside explicit R435 geometry. SV90784 then removes the far-end forms P_x->W and W->P_z by R523, leaving W->P_x and P_z->W. Deleting z from the first and x from the second gives two exact covers of the common residue H-{x,z}: W_x->(a,y,c)|W_x' and (a,y,c)->W_z|W_z'. Different support partitions give R410; equal partitions force different same-support literal orders, hence R471/R435. Thus outside R159/R523/R410/R435 outputs the endpoint rows cannot both be unique-transition; at least one has at least two petal|W transitions.

### 1. Endpoint rows after the two-W-block reduction
Retain the source three-spoke Hamilton path K=(x,a,y,c,z) and put W=V(H)-V(K). Let T_x be an exact two-cover of H-x and T_z an exact two-cover of H-z. Work outside the higher-W-block component-drop output of SV90412, so both rows have exactly two maximal W-blocks. Their literal endpoint petals are P_x=(a,y,c,z) and P_z=(x,a,y,c). Suppose each row has exactly one selected transition between its petal support and W.

### 2. Unique transition makes the petal one literal block
Apply accepted R560 to T_x with D={x}, S=V(P_x), C=W. Exactly one rail is mixed and consists of one S-block and one W-block; the other rail is wholly in W. Thus the S-block is a Hamilton path on all vertices of P_x. Compare it with P_x by R435. Outside adjacent reversal, reverse trimer, or proper-cycle output, the common-support contact order is increasing, so the S-block is literally P_x. The same argument gives the literal block P_z in T_z. Therefore the only R435-quiet unique-transition forms are T_x=P_x B_x|C_x or B_x P_x|C_x, and T_z=P_z B_z|C_z or B_z P_z|C_z, with all B,C nonempty W-blocks.

### 3. Far-end collision leaves one orientation per endpoint row
SV90784 consumes T_x=P_x B_x because its unique transition leaves z toward W and yields an R523 collision on (z,c). It also consumes T_z=B_z P_z because its unique transition enters x from W and yields an R523 collision on (a,x). Hence outside R523 geometry the only pair of quiet unique-transition rows is T_x=B_x P_x|C_x and T_z=P_z B_z|C_z.

### 4. Puncture the opposite endpoints
Delete z from T_x. Since z is terminal in P_x, F_x:=B_x(a,y,c)|C_x is an exact two-cover of H-{x,z}. Delete x from T_z. Since x is initial in P_z, F_z:=(a,y,c)B_z|C_z is another exact two-cover of H-{x,z}. All four components are nonempty.

### 5. Common-residue incompatibility
Apply R410/R471 to F_x,F_z. If the unordered support partitions differ, R410 gives a graph-intrinsic balanced opposite-sign pair. If the partitions agree, the unique rails containing a,y,c correspond and have the same support. But their literal orders cannot agree: F_x has a nonempty W-prefix before the contiguous trimer (a,y,c), whereas F_z has a nonempty W-suffix after that trimer. Thus R471/R435 yields an adjacent reversal, reverse trimer, or vertex-simple tight cycle.

### 6. Two-ended transition pressure
Therefore, outside R159 higher-W-block geometry, R523 far-end collision, R410 balanced-pair geometry, and R435 reversal/reverse-trimer/cycle geometry, the endpoint puncture rows H-x and H-z cannot both have exactly one selected (K-d)|W transition. Since R508 forces at least one transition in every row, at least one endpoint row has transition count at least two; equivalently the quiet endpoint pair satisfies tau_x+tau_z>=3.

The two original rows are alternative exact representatives. They are compared only after puncturing opposite endpoints to the common residue H-{x,z}; no selected state is transported between them. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R560"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    }
]
```