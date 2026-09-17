# The deleted pair propagates along every cap rail: adjacent quiet cells force R435 and otherwise P4 portals have linear density

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-pair-deletion-railwide-two-probe-propagation`

**Summary:** Continue the Arm-M pair-deletion bidirectional wall SV42382. Let A=(a0,...,a_{k-1}) be the k-rail of an arbitrary exact H-{x,y} cover. For every consecutive trimer K_i=(a_i,a_{i+1},a_{i+2}), apply accepted R700 with the SAME probes x,y. Each cell either has a Hamilton probe-P4 on K_i+x or K_i+y, or is DUAL, meaning x,y both tail-sign the reverse initial dimer and both head-sign the reverse terminal dimer. Two adjacent DUAL cells share the tested reverse dimer E_i=(a_{i+1},a_i); the left cell head-signs E_i by x,y and the right tail-signs E_i by x,y. R523 gives both tight P4s (x,a_{i+1},a_i,y) and (y,a_{i+1},a_i,x). Comparing these actual same-support P4 orders by R435 necessarily emits a reverse trimer or proper tight cycle, since the first step y->a_{i+1} of the second word jumps backward from index 3 to index 1 of the first and is not an adjacent-state reversal. Therefore outside explicit current R435 geometry, DUAL cells are an independent set in the path of k-2 consecutive trimers. At least floor((k-2)/2) cells are probe-P4 active. In the surviving k>=8 range there are at least three such cells, and one fixed deleted probe participates in at least two after choosing one P4 probe per active cell. Every such proper P4 currentizes by R4 to an actual maximum three-forest. Thus the universal pair-deletion wall cannot stay localized at the cap endpoints: it either emits R435 curvature between adjacent cells or forces a linearly dense family of current probe-P4 portals along the entire k-rail.

### 1. One fixed deleted pair probes every consecutive cap trimer
Retain the arbitrary Arm-M pair-deletion frame of SV42382:

  H-{x,y}=A|B,
  A=(a_0,a_1,...,a_{k-1}),
  |A|=k, |B|=k-1.                                        (RP.1)

The physical deleted labels x,y are disjoint from A. For each

  i=0,1,...,k-3

put

  K_i=(a_i,a_{i+1},a_{i+2}),                             (RP.2)

a literal consecutive tight trimer of A.

Apply accepted two-probe amplification R700 to K_i with the SAME two probes x,y. Exactly one parent alternative is retained for each i:

  ACTIVE_i: for some z in {x,y}, K_i+z supports a Hamilton tight P4;

or

  DUAL_i: x and y both tail-sign the reverse initial dimer
          (a_{i+1},a_i),
          and x and y both head-sign the reverse terminal dimer
          (a_{i+2},a_{i+1}).                             (RP.3)

No representative synchronization between different i is used. These are graph-intrinsic consequences of the same physical A,x,y.

### 2. Two adjacent DUAL cells make one reverse rail edge bidirectional
Assume DUAL_{i-1} and DUAL_i for some 1<=i<=k-3. Their shared tested reverse rail dimer is

  E_i=(a_{i+1},a_i).                                     (RP.4)

From DUAL_{i-1}, E_i is the reverse terminal dimer of K_{i-1}, so

  (x,a_{i+1},a_i),
  (y,a_{i+1},a_i)                                        (RP.5)

are tight.

From DUAL_i, E_i is the reverse initial dimer of K_i, so

  (a_{i+1},a_i,x),
  (a_{i+1},a_i,y)                                        (RP.6)

are tight.

Thus the same tested oriented dimer E_i has both polarities with both physical witnesses. Accepted same-support interaction R523 gives in particular the two literal tight P4s

  P_xy=(x,a_{i+1},a_i,y),
  P_yx=(y,a_{i+1},a_i,x).                                (RP.7)

### 3. The two cross-P4 orders force explicit R435 geometry
Compare P_xy and P_yx by accepted Reverse Ear R435, taking P_xy as the reference order. Its vertex indices are

  x:0, a_{i+1}:1, a_i:2, y:3.

The first state of P_yx is

  y -> a_{i+1},                                          (RP.8)

so two consecutive P_yx contacts occur in decreasing P_xy order 3 -> 1. This is not the exceptional adjacent-state reversal case i=j+1 of R435. Therefore R435 emits an explicit

  reverse tight trimer,
  OR a vertex-simple proper tight cycle.                 (RP.9)

Hence two adjacent DUAL cells are never a quiet propagation pattern: they are already an R435 portal with all four physical labels x,y,a_i,a_{i+1} retained.

### 4. Linear density of probe-P4 portals outside R435
Suppose no output (RP.9) occurs anywhere along A. Then no two DUAL cells are adjacent.

There are exactly k-2 consecutive trimers K_0,...,K_{k-3}. The DUAL indices form an independent set in this path, so at most

  ceil((k-2)/2)                                          (RP.10)

of them are DUAL. Consequently at least

  floor((k-2)/2)                                         (RP.11)

indices are ACTIVE.

At every ACTIVE index retain one physical probe z_i in {x,y} and one actual Hamilton P4 on K_i+z_i. By pigeonhole, one of the two deleted probes occurs on at least

  ceil( floor((k-2)/2) / 2 )                             (RP.12)

of these retained active cells.

In particular, in the surviving large-order uniform range k>=8 there are at least three ACTIVE trimer cells, and one fixed deleted probe participates in at least two of them.

### 5. Every active cell is already current maximum-forest geometry
Each ACTIVE Hamilton P4 is a proper graph-intrinsic tight path in the live Arm-M range. Accepted R4 supplies an exact two-cover of its complement, so restoring the P4 gives an actual maximum spanning three-forest containing that physical probe-P4 literally.

Thus the two-ended wall of SV42382 propagates through the whole k-rail in the following theorem-scale dichotomy:

  explicit R435 reverse-trimer/proper-cycle curvature,

  OR a linearly dense family of actual probe-P4 maximum-forest portals along A.   (RP.13)

This is not yet Arm-M closure. The remaining strong route is to consume the repeated probe-P4 family globally: compare the at-least-two cells carrying one common deleted probe, exploit their ordered positions on the same ancestral cap rail, and force either an order-(k+1) splice, a strict cap-support transition, or one of the bounded recompletion nuclei. The point is that the universal pair-deletion wall is no longer an endpoint-only packet; outside R435 curvature it creates positive-density current geometry across the rail.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R700"
    }
]
```