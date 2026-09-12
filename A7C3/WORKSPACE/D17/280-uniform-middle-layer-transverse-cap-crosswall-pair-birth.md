# Transverse Arm-M caps force a direct cross-wall mass-four pair

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-transverse-cap-crosswall-pair-birth`

**Summary:** If two Arm-M Hamilton k-caps C,K meet in at most one vertex, their universal reverse boundary walls force a direct mass-four balanced pair. Pair the tail-signed left wall dimer of C with the head-signed right wall dimer of K, or the head-signed right wall dimer of C with the tail-signed left wall dimer of K. When C and K are disjoint both are disjoint; when they share one vertex s, if one cross pairing meets at s then disjointness of the two boundary dimers within each cap forces the other cross pairing to avoid s. Hence one opposite-polarity cross pair is physically disjoint, and accepted R514 yields a mass-four pair. Applied to SV49597, every one-step canonical return cap from an equal-parity dip has overlap at most one with the source cap and therefore immediately yields such a cross-wall pair. This converts the cap-return branch into an explicit pair-bearing phase-0 object, but does not yet bridge the lineage-relative R172 clock.

### 1. Input
Work in accepted R927(M), k>=6. Let C and K be two literal Hamilton k-cap paths. Assume

  |V(C) intersect V(K)| <= 1.                              (TP.1)

For each cap retain its universal reverse boundary wall. Write

  L_C=(c_1,c_0),   R_C=(c_{k-1},c_{k-2}),
  L_K=(k_1,k_0),   R_K=(k_{k-1},k_{k-2}).                 (TP.2)

Every exterior label tail-signs L_C and L_K, while every exterior label head-signs R_C and R_K. Because the two caps have order k and meet in at most one vertex, both differences C-K and K-C are nonempty. Choose any y in K-C and x in C-K. Then L_C is tail-signed by y and R_C is head-signed by y, while L_K is tail-signed by x and R_K is head-signed by x.

### 2. One opposite-polarity cross pairing is disjoint
Consider the two opposite-polarity cross pairings

  L_C with R_K,
  R_C with L_K.                                            (TP.3)

If C and K are disjoint, both pairings are physically disjoint. Suppose instead C intersect K={s}. If L_C intersects R_K, their intersection can only be s. Since the two boundary dimers L_C,R_C are disjoint inside C, s is not in R_C. Since R_K,L_K are disjoint inside K, s is not in L_K. Hence R_C and L_K are physically disjoint. The dual implication is identical. Therefore at least one pairing in (TP.3) consists of two physically disjoint signed dimers of opposite polarity.

Accepted R514 then gives a graph-intrinsic balanced opposite-sign pair of total support mass four. Its continuation yields either a spanning two-cover or an ancestry-bearing both-singleton floor.

### 3. Application to the canonical parity-dip return
SV49597 proves that every portal-free canonical return from an SV46809 equal-parity cap dip is either the dip forest itself or one unique one-SLIDE terminal cap K with

  |V(K) intersect V(C)| <= 1.                              (TP.4)

In the returned-cap branch, Sections 1-2 therefore produce a direct mass-four pair using one boundary dimer of the source cap C and the opposite-polarity boundary dimer of K. Thus the transverse return is not merely another cap discrepancy or another R435 source: it is already pair-bearing before any further comparison of cap words.

### 4. Exact scope
This does not yet prove phase-0 curvature cancellation. R514 pays the new pair to a floor, but accepted R172 is lineage-relative and does not automatically compare that floor with the pre-curvature phase-0 checkpoint. The remaining task is to bridge the retained source-turn/anchor ancestry across this cross-wall pair payment and show that the re-aligned fixed-turn checkpoint strictly lowers the old R172 coordinates, or closes H.

Status: established working integration lemma, unreviewed exposition.