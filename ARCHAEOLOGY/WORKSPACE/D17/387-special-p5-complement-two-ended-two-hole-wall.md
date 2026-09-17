# A special three-spoke P5 forces a two-ended two-hole wall on every two-path complement

**Workspace:** D17
**State:** established
**Key:** `special-p5-complement-two-ended-two-hole-wall`

**Summary:** Let K=(x,a,y,c,z) be a tight P5 and retain the two extra source-spoke turns (a,x,c),(a,z,c). If its complement W is covered by two nonempty tight paths B|C, then for each complement rail R=(r0,...,rt), attempting the two full splices K followed by R and R followed by K gives complete two-turn windows. A bad near turn yields an R523 collision on the source tested dimer (z,c) or (a,x). Therefore, outside those source collisions, R is nontrivial and necessarily satisfies (c,z,r0),(r1,r0,z),(r_t,x,a),(x,r_t,r_{t-1}) tight: K extends by one endpoint at either end, while the second seam is reversed. Hence both complement rails simultaneously carry a z-tail reverse shield at their initial dimers and an x-head reverse shield at their terminal dimers. For endpoints on opposite complement rails, the seven-vertex word terminal-K-source is Hamiltonian, and R933 identifies the two reversed outer seams as the exact simultaneous two-hole obstruction. In particular, any x/z pair-residue representative with exactly two W-blocks falls into this wall or an immediate source-dimer R523 collision, so the invalid one-seam tau=1/tau=2 insertions can be bypassed without claiming extinction.

### 1. Setup
Let H be a finite Strong Level-(1) boundary tournament with pc(H)>2. Retain five distinct vertices with the literal tight P5

  K=(x,a,y,c,z)

and also the two source-spoke turns

  (a,x,c),   (a,z,c)

tight. Put W=V(H)-V(K), and suppose W has a literal two-path cover

  B | C.

No relation between this complement cover and a later pair-deletion representative is assumed. The theorem below is purely static.

### 2. One complement rail: right splice
Fix one nonempty complement rail

  R=(r_0,...,r_t).

First try to concatenate K followed by R, leaving the other W-rail untouched. If t=0, the only new turn is

  alpha=(c,z,r_0).

If alpha were tight, K followed by r_0 together with the untouched W-rail would be a spanning two-cover of H. Hence alpha is bad, so R3 gives

  (r_0,z,c) tight.

Together with source (a,z,c), these are two head certificates on the SAME tested oriented dimer (z,c), with distinct witnesses r_0,a. Thus R523 gives the source-dimer HH collision.

Now assume t>=1. The complete new-turn window of K followed by R is exactly

  alpha=(c,z,r_0),
  beta =(z,r_0,r_1).

If both were tight, K R together with the untouched W-rail would two-cover H. Therefore at least one is bad. If alpha is bad, the preceding R3/R523 argument again gives the HH collision on tested dimer (z,c). Consequently, outside that collision alpha is tight and beta must be bad. Exact reversal gives

  (r_1,r_0,z) tight.                                    (TW.1)

Thus outside the source collision, K extends one vertex into R through (c,z,r_0), but the farther seam is forced into the reverse initial turn (TW.1).

### 3. One complement rail: left splice
Try the opposite concatenation R followed by K. If t=0, the only new turn is

  delta=(r_0,x,a).

It must be bad, or R K plus the untouched W-rail would two-cover H. Hence

  (a,x,r_0) tight.

Together with source (a,x,c), these are two tail certificates on the SAME tested oriented dimer (a,x), with distinct witnesses r_0,c. R523 gives the source-dimer TT collision.

Assume t>=1. The complete new-turn window is

  gamma=(r_{t-1},r_t,x),
  delta=(r_t,x,a).

At least one is bad. If delta is bad, its reversal (a,x,r_t) and source (a,x,c) give the TT collision on tested dimer (a,x). Therefore, outside that collision delta is tight and gamma must be bad, so

  (x,r_t,r_{t-1}) tight.                                (TW.2)

Thus outside the source collision, R also extends one vertex into K through (r_t,x,a), while its farther terminal seam is reversed.

### 4. Simultaneous two-ended wall on both complement rails
Apply Sections 2-3 separately to B and C. Outside an R523 collision on one of the two source tested dimers (z,c) or (a,x), neither complement rail can be a singleton. Writing

  B=(b_0,...,b_r),   C=(c_0,...,c_s),   r,s>=1,

the following eight turns coexist graph-intrinsically:

  (c,z,b_0),      (b_1,b_0,z),
  (b_r,x,a),      (x,b_r,b_{r-1}),
  (c,z,c_0),      (c_1,c_0,z),
  (c_s,x,a),      (x,c_s,c_{s-1}).                     (TW.3)

Equivalently, z tail-witnesses the reverse initial dimers (b_1,b_0),(c_1,c_0), while x head-witnesses the reverse terminal dimers (b_r,b_{r-1}),(c_s,c_{s-1}). At the same time every rail source appends after K by one vertex and every rail terminal prepends before K by one vertex.

In particular the two cross-rail seven-vertex words

  (b_r,x,a,y,c,z,c_0),
  (c_s,x,a,y,c,z,b_0)                                  (TW.4)

are literal tight paths. Apply R933 with X=V(K), Y=W, using respectively the opposite-rail endpoint pairs (b_r,c_0) and (c_s,b_0). Its strong pc(H)>2 clause says both residual attachment holes exist and are bad. Those four bad holes are exactly

  (b_{r-1},b_r,x), (z,c_0,c_1),
  (c_{s-1},c_s,x), (z,b_0,b_1),

whose reversals are precisely the four reverse shields in (TW.3). Thus the collision-free residue is not an omitted-seam ambiguity: it is an exact simultaneous R933 two-hole wall in both cross-rail directions.

A small additional consequence follows directly from R3. At the two rail sources, either (b_0,z,c_0) or (c_0,z,b_0) is tight. Combining with the corresponding reverse-initial shield gives one of the literal P4s

  (b_1,b_0,z,c_0),  (c_1,c_0,z,b_0).

Dually the two terminal shields force a cross-rail P4 through x. These P4s are constructive certificates, not contradictions.

### 5. Repair of the audited pair-residue insertion gap
Return to the conditional special-order pair residue with D={x,z}, S={a,y,c}, W=H-K. Suppose an exact cover F of H-D has exactly two maximal W-blocks. Those two blocks are vertex-disjoint tight paths covering all of W, regardless of how S is interleaved in F. Call them B,C. Sections 1-4 therefore apply immediately.

Hence the full two-W-block residue, including the audited tau=1 and tau=2 cells, has the lawful alternative:

1. an R523 same-tested-orientation collision on source dimer (z,c) or (a,x); or
2. both W-blocks are nontrivial and carry the simultaneous two-ended wall (TW.3), equivalently the two cross-rail R933 two-hole packets (TW.4).

This bypasses the invalid assertions in SV94553/SV94554 that checking only one insertion seam creates an exact singleton-deletion row. The omitted W-side turns are retained explicitly and become the reverse shields when bad. No singleton-row currentization is needed.

### 6. Scope
This is a repair/reduction, not frame absorption. R523 collisions and the simultaneous two-ended wall still require a static consumer. In particular the theorem does not revive SV94555's extinction claim. Its gain is that the audit failures no longer leave an untyped seam: the complete windows collapse to one source collision or one rigid common-parent two-ended wall, with both complement rails and both P5 ends retained physically. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R933"
    }
]
```
