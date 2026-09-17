# A persistent far wall reaching a source gate is a P4 or a source-dimer collision

**Workspace:** D17
**State:** established
**Key:** `g36-source-oriented-persistent-wall-collapse`

**Summary:** In the tau-three G35 hard cell, choose a canonical low-transition boundary whose old F transition is source-bearing, as guaranteed by SV112110/SV114206. Orient defect transport from that boundary so the source spoke t itself is the moving unmatched copy: use the OUT-prefix orientation when the old gate is t->h and the exact IN-suffix dual when it is h->t. Neutral normalization and SV115057 show that any obstruction persisting through successful pivots is a fixed far-end reverse star. At the source position, in the OUT case this gives a tight turn (d,b,t) while the historical source turn (A,t,C) remains tight. Test (b,t,A). If tight, (d,b,t,A) is a literal P4. If bad, R3 gives (A,t,b) tight, so (A,t,b) and (A,t,C) are a same-oriented two-tail R523 collision on the source dimer (A,t), with witnesses b,C. The IN-dual case gives either the P4 (C,t,b,d) or a same-oriented two-head collision on (t,C), with witnesses A,b. Thus persistent far-boundary debt cannot cross a source gate as an anonymous seam: it becomes P4 geometry or one exact source-dimer collision carrying an anchor witness. No R24, R5, payment, replay, or seam taxonomy is used.


### 1. Source-bearing hard-cell boundary
Retain the tau-three G35 hard cell. By SV112110 and the sharper block normal form SV114206, one canonical low-transition corridor boundary is an actual old source gate. Write its source spoke as t and its spectator neighbor as h. The historical source packet retains

  (A,t,C) tight.                                           (SW.1)

The boundary matching has the three-cover cardinality and transition count at most two.

### 2. Orient transport so the source spoke is the moving defect
If the old selected gate is

  t -> h,                                                   (SW.2)

use the OUT-defect prefix orientation of the unique augmenter. Immediately before installing (SW.2), the free moving OUT copy is t_out. If instead the old gate is

  h -> t,                                                   (SW.3)

use the exact reversal-dual IN-defect suffix orientation from the opposite end. Immediately before installing (SW.3), the moving free IN copy is t_in.

Thus in either physical orientation the source-bearing boundary can be read with t itself as the moving defect endpoint. This is only a choice of which end of the same alternating path is used as the transport origin; no edge orientation is changed.

Normalize every neutral component to F as in SV112526. Along any run of successful physical pivots, SV115057 says that near-seam debt dies when the defect advances and cycle debt dies after one successful pivot. Hence the only obstruction that can genuinely persist to the source position is one fixed far-boundary reverse star.

### 3. OUT case: the persistent wall becomes P4 or a source-dimer collision
In the OUT orientation, write the fixed far selected boundary dimer as

  b -> d.                                                   (SW.4)

If the far shortcut seam is bad when the moving endpoint is t, R3 gives the persistent reverse-star turn

  (d,b,t) tight.                                           (SW.5)

Test the ordered triple

  (b,t,A).                                                  (SW.6)

If (SW.6) is tight, then (SW.5) and (SW.6) concatenate to the literal vertex-simple P4

  (d,b,t,A).                                                (SW.7)

If (SW.6) is bad, R3 gives

  (A,t,b) tight.                                           (SW.8)

Together with the historical source turn (SW.1), the fixed tested oriented dimer

  D=(A,t)                                                   (SW.9)

has two distinct tail witnesses b and C:

  (A,t,b),  (A,t,C) tight.                                 (SW.10)

This is exactly the TT same-oriented R523 collision packet on the source dimer (A,t). The witness C is the other source anchor; the second witness b is the fixed far-boundary vertex from the persistent wall.

### 4. IN case is the exact ordered dual
In the IN-defect orientation the persistent wall is the complete reversal-dual tight turn

  (t,b,d).                                                  (SW.11)

Test

  (C,t,b).                                                  (SW.12)

If it is tight, (SW.12) and (SW.11) give the literal P4

  (C,t,b,d).                                                (SW.13)

If it is bad, R3 gives

  (b,t,C) tight.                                           (SW.14)

Now (SW.1) and (SW.14) are two distinct head witnesses A,b on the tested source dimer

  D'=(t,C):
  (A,t,C), (b,t,C) tight.                                  (SW.15)

Thus the dual residue is the HH R523 collision on (t,C), again with one witness equal to the opposite source anchor.

### 5. Consequence
A far-end reverse star may persist through same-side transport intervals, but once defect transport is oriented from a source-bearing gate and reaches that gate, persistence has only two exact outputs:

1. a literal P4 containing the source spoke and one source anchor; or
2. one same-oriented R523 collision on a source dimer, with the other source anchor as one of its witnesses.

Therefore the persistent wall is not a new obstruction family beyond the source event. The remaining non-P4 object is one source-dimer collision with unusually strong ancestry, not an arbitrary R523 packet.

This section does not claim that the P4 or source-dimer collision already closes H. It is the parent compression to which the next consumer should be applied. R24, R5, payment, replay, and generic seam classification are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
