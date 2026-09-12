# The three-port spindle thickens to a two-square maximum-forest exchange disk

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-three-port-spindle-two-square-exchange-disk`

**Summary:** Continue the exact three-port spindle currentization SV37257. For the two R579 DOUBLE-FAIL ports p,q, common core K=(r0,...,rm), and frozen third-label Hamilton rail Q_t, the retained turns (p,r0,q), (r0,q,r_m), and (q,r_m,r_{m-1}) generate not just the previously displayed three-transfer path F0->F1->F2->F3 but six literal maximum-three-forest representatives A_xy arranged as a 2-by-3 grid. Horizontal edges all exchange r0-r1 for r0-q; first vertical edges exchange r_{m-1}-r_m for q-r_m; second vertical edges exchange r_{m-2}-r_{m-1} for r_m-r_{m-1}. Every one of the seven grid edges is a reversible one-edge support transfer and Q_t is literally fixed. The outer six-cycle is the boundary of two explicit exchange squares sharing their middle horizontal edge, so it contracts by two square substitutions and immediate backtracking. Equivalently, among the eight formal subsets of the three edge exchanges, exactly the six path-forest states occur; the two omitted subsets apply the final tail reversal before removing r_{m-1}->r_m and therefore carry the physical 2-cycle r_{m-1}<->r_m. Thus the spindle supplies a concrete local model in which support-changing recurrence is square-contractible and the only missing cube states are visible cycle debt. No global marked-holonomy extinction or O4 closure is claimed.

### 1. Input from the exact spindle currentization
Retain the Arm-M three-port spindle packet of SV37257. Thus k>=5,

  K=(r_0,r_1,...,r_m),   m=k-2>=3,

is a retained Hamilton order on the (k-1)-core R, p,q are two physical completion labels in the R579 DOUBLE-FAIL branch, t is the third retained completion label, and Q_t is one fixed actual Hamilton path on the complementary k-set W+t.

The exact physical turn certificates retained by SV37257 are

  (p,r_0,q) tight,
  (r_0,q,r_m) tight,
  (q,r_m,r_{m-1}) tight.                           (XD.1)

Every inherited consecutive turn of K is tight. The previously currentized spindle forest is

  (p,r_0,q,r_m,r_{m-1}) | (r_1,...,r_{m-2}) | Q_t. (XD.2)

All labels, the literal K order, the DOUBLE-FAIL ancestry, and the literal Q_t word remain fixed below.

### 2. Six literal maximum-three-forest representatives
Define the following six spanning three-path forests, indexed as a 2-by-3 grid:

  A_00=(p,r_0,r_1,...,r_{m-1},r_m) | {q} | Q_t,

  A_10=(p,r_0,q) | (r_1,...,r_{m-1},r_m) | Q_t,

  A_01=(p,r_0,r_1,...,r_{m-1}) | (q,r_m) | Q_t,

  A_11=(p,r_0,q,r_m) | (r_1,...,r_{m-1}) | Q_t,

  A_02=(p,r_0,r_1,...,r_{m-2}) | (q,r_m,r_{m-1}) | Q_t,

  A_12=(p,r_0,q,r_m,r_{m-1}) | (r_1,...,r_{m-2}) | Q_t. (XD.3)

Each displayed component is a literal tight path. A_00 is the canonical singleton lift from SV37257. A_10 uses only the first turn in (XD.1). A_01 uses only the automatic tight dimer (q,r_m). A_11 uses the first two turns in (XD.1). A_02 uses the third turn in (XD.1). A_12 uses all three turns and is exactly the spindle forest (XD.2).

Because m>=3, every displayed residual K-subpath is nonempty. Thus every A_xy is a literal spanning three-cover. Since H is a hypothetical counterexample with no spanning two-cover, every A_xy is a maximum spanning three-forest.

### 3. Seven reversible one-edge exchanges
There are three horizontal exchange edges

  A_0j <-> A_1j,   j=0,1,2,

all obtained by deleting the selected physical edge r_0 r_1 and adding r_0 q. For j=0 the new component is (p,r_0,q). For j=1 it joins (p,r_0) to (q,r_m), and tightness of (r_0,q,r_m) certifies the junction. For j=2 it joins (p,r_0) to (q,r_m,r_{m-1}); the same junction turn certifies the move. The inherited turn (p,r_0,q) certifies the left end in every case.

There are two first vertical exchange edges

  A_i0 <-> A_i1,   i=0,1,

obtained by deleting r_{m-1} r_m and adding q r_m. For i=0 the new rail (q,r_m) is a dimer. For i=1 it appends r_m to (p,r_0,q), and (r_0,q,r_m) certifies the new turn.

There are two second vertical exchange edges

  A_i1 <-> A_i2,   i=0,1,

obtained by deleting r_{m-2} r_{m-1} and adding r_m r_{m-1}. For i=0 this extends (q,r_m) using (q,r_m,r_{m-1}); for i=1 it extends (p,r_0,q,r_m) by the same certified turn.

Thus every one of the seven grid edges is an exact reversible one-edge support transfer between literal maximum-three-forest representatives. The rail Q_t is IDENTICAL at all six vertices.

### 4. The spindle has two distinct three-step realizations
The path recorded in SV37257 is the upper/right route

  A_00 -> A_10 -> A_11 -> A_12.                    (XD.4)

There is an equally literal lower/left route

  A_00 -> A_01 -> A_02 -> A_12.                    (XD.5)

The grid also contains the middle rung A_01 <-> A_11. Hence the outer closed representative walk

  A_00,A_10,A_11,A_12,A_02,A_01,A_00              (XD.6)

is the boundary of the two explicit exchange squares

  A_00-A_10-A_11-A_01-A_00,
  A_01-A_11-A_12-A_02-A_01.                        (XD.7)

This gives a completely literal square-contraction certificate: replace the two-edge side A_00-A_10-A_11 by A_00-A_01-A_11, and replace A_11-A_12-A_02 by A_11-A_01-A_02. The resulting closed walk cancels by immediate backtracking. No ambient topological definition is required; the contraction is the finite sequence of displayed representative substitutions.

Accordingly the spindle's natural support-changing recurrence is SQUARE-CONTRACTIBLE at the level of actual maximum forests, while preserving p,q,t, the entire K ancestry, and Q_t. In any exchange 2-complex whose elementary 2-cells are precisely such verified one-edge exchange squares, (XD.6) is null-homotopic.

### 5. Collision/cycle-debt reading
Relative to A_00 and A_12, the three edge replacements are

  X: r_0 r_1       -> r_0 q,
  Y: r_{m-1} r_m   -> q r_m,
  Z: r_{m-2}r_{m-1}-> r_m r_{m-1}.                 (XD.8)

Formally there are eight subsets of {X,Y,Z}. The six subsets

  empty, X, Y, XY, YZ, XYZ

are exactly the six path-forest representatives in (XD.3). The two omitted subsets Z and XZ try to apply the final tail reversal Z while the old selected state r_{m-1}->r_m is still present. They therefore contain the literal directed two-cycle

  r_{m-1} -> r_m -> r_{m-1},                       (XD.9)

and are not path forests.

Thus the entire local obstruction to filling the three-exchange cube is visible cycle debt on one physical dimer. After Y removes the old orientation, Z becomes legal. This is an exact miniature of the global maximum-forest gain/cycle-debt program: the spindle itself contributes no mysterious residual transport beyond a two-square disk plus one explicitly identified cyclic incompatibility.

### 6. Scope
This section does NOT assert that every support-changing representative loop in H contracts, that every history-bearing mark is preserved under arbitrary exchange-square substitution, or that O4 is closed. It proves only the exact local statement above: the canonical three-port spindle packet carries a six-state, seven-edge maximum-forest grid whose outer recurrence has an explicit two-square contraction and whose two missing formal cube states are precisely the named physical two-cycle debt. This strengthens the spindle-to-forest handoff from mere currentization to a concrete contractible local exchange cell.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R579"
    }
]
```