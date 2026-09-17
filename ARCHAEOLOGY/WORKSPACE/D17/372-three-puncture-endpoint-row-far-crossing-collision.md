# Far-end crossings in the x/z two-block puncture rows force R523 collisions

**Workspace:** D17
**State:** established
**Key:** `three-puncture-endpoint-row-far-crossing-collision`

**Summary:** Retain K=(x,a,y,c,z), W=H-K, and the two endpoint puncture petals P_x=(a,y,c,z) in H-x and P_z=(x,a,y,c) in H-z. After the two-W-block reduction, R509 gives exact one-hole proposals at petal endpoints. In the H-z row, if a W-block enters the far endpoint x as w->x, R509 at j=0 forces the reverse turn (a,x,w); the source spoke (a,x,c) then gives a same-oriented two-tail R523 collision on (a,x). Dually, in the H-x row, if the far endpoint z exits as z->w, R509 at i=m forces (w,z,c); together with source (a,z,c) this is a two-head R523 collision on (z,c). Hence outside R523/PAYABLE-FOUR geometry those two far-end crossing directions are forbidden. This orients the surviving x/z two-block crossing system inward/rootward but does not classify all remaining cuts.

### 1. Opposite endpoint puncture rows
Retain the three-spoke source P5

  K=(x,a,y,c,z)

and put W=V(H)-V(K). Work outside the higher-block component-drop branch of the two-W-block reduction, so the chosen exact H-x and H-z rows each have exactly two maximal W-blocks.

The endpoint petals are

  P_x=(a,y,c,z)   in H-x,
  P_z=(x,a,y,c)   in H-z.

The retained source spoke turns include

  (a,x,c), (a,z,c).

### 2. A W-to-x crossing in the H-z row is not quiet
Let T_z be an exact two-cover of H-z and suppose one of its selected crossing states is

  w -> x

with w in W. Since x is the first vertex q_0 of P_z and the W-block decomposition has exactly two blocks, the endpoint case of accepted R509 applies to this C-to-S crossing into q_0. Its one-hole spanning proposal has unique uncertified turn

  (w,x,a).

Because pc(H)>2, that turn is bad, so R3 gives the exact reverse

  (a,x,w) tight.

The source spoke turn (a,x,c) is also tight. These are two TAIL certificates on the same tested oriented dimer (a,x), with distinct witnesses w and c because w lies in W. Accepted R523 therefore gives a same-oriented two-tail collision on (a,x).

Thus, outside the R523 collision branch, no exact two-W-block H-z row may realize a far-end crossing w->x.

### 3. A z-to-W crossing in the H-x row is not quiet
Dually let T_x be an exact two-cover of H-x and suppose it selects

  z -> w

with w in W. Here z is the last vertex q_m of P_x. The endpoint S-to-C case of R509 at i=m gives a one-hole spanning proposal whose unique uncertified turn is

  (c,z,w).

Hence R3 forces

  (w,z,c) tight.

The source spoke turn (a,z,c) is tight as well. These are two HEAD certificates on the same tested oriented dimer (z,c), with distinct witnesses w and a. Accepted R523 gives a same-oriented two-head collision on (z,c).

Therefore, outside R523 geometry, no exact two-W-block H-x row may realize the far-end crossing z->w.

### 4. Consequence and fence
In the quiet two-block x/z system, the crossing behavior is already oriented away from two remote directions: W cannot enter P_z through x, and P_x cannot leave through z. Remaining root-facing endpoint directions and internal petal cuts are not classified here; in particular no synchronization between T_x and T_z is asserted. The point is that two of the eight endpoint crossing orientations are consumed directly by the common source spoke packet.

R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R509"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```