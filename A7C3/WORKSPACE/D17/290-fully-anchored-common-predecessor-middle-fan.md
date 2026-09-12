# A common completed predecessor forces a one-sided middle fan or immediate PAYABLE-FOUR curvature

**Workspace:** D17
**State:** established
**Key:** `fully-anchored-common-predecessor-middle-fan`

**Summary:** Continue the fully anchored predecessor-equality atom of SV78911. Fix E={a,c} and the common old secondary vertex x, so every rank-flat same-E reentry middle b in the no-P4 branch satisfies (b,a,x), (x,c,b), and (a,b,c) tight. Take two distinct admissible middles b,d. If (b,a,d) is tight, then (b,a,d,c) is a literal P4 using J_d; if it is bad, R3 gives (d,a,b), which together with J_b gives the literal P4 (d,a,b,c). Therefore any TWO distinct equality-atom middles immediately produce a proper P4, hence PAYABLE-FOUR cancellation. Consequently a rank-flat fully anchored lineage can realize the predecessor-equality atom at at most one middle. After one such occurrence, any later R1022 reentry at the same endpoint pair must either reproduce the same physical middle or expose PAYABLE-FOUR / explicit nonquiet geometry. This reduces the equality atom to a one-middle stationary replay problem rather than an arbitrary middle-fan recurrence.

### 1. Equality atom
Retain the fully anchored bottom checkpoint and the predecessor-equality atom from SV78911:

  E={a,c},
  x outside E,
  J_b=(a,b,c) tight,
  (b,a,x) tight,
  (x,c,b) tight.                                         (MF.1)

Assume b is an admissible internal middle in some exact H-E reentry frame. The packet lies on four vertices {a,b,c,x}.

### 2. Compare two distinct middles
Suppose a second later reentry uses a different admissible middle d, d!=b, and also lands in the same rank-flat predecessor-equality form:

  J_d=(a,d,c) tight,
  (d,a,x) tight,
  (x,c,d) tight.                                         (MF.2)

Test the single turn

  (b,a,d).                                               (MF.3)

If it is tight, concatenate with J_d=(a,d,c) to get the literal tight P4

  (b,a,d,c).                                             (MF.4)

If (MF.3) is bad, R3 gives

  (d,a,b) tight.                                         (MF.5)

Together with J_b=(a,b,c), this gives the literal tight P4

  (d,a,b,c).                                             (MF.6)

The four vertices are distinct because b,d are distinct internal middles outside E.

Thus any two distinct equality-atom middles force a proper P4 in the common historical parent data.

### 3. PAYABLE-FOUR cancellation
By SV78086, every proper P4 is PAYABLE-FOUR. Hence at fixed-E phase zero, the P4 from Section 2 yields

  TWO-COVER,
  STRICT old-E Psi_E descent,
  or EXPLICIT NONQUIET PORTAL.                            (MF.7)

At the fully anchored bottom tuple there is no silent strict numerical descent available; therefore two distinct equality middles cannot participate in a portal-free rank-flat recurrence.

### 4. One-middle stationary residue
Consequently the predecessor-equality atom can occur rank-flatly at at most ONE physical middle b. Any later same-E R1022 return which chooses a different middle d immediately exits through (MF.7).

The only residual possibility is exact physical replay of the SAME middle b together with the same endpoint pair E and same common predecessor x. This is a finite stationary atom, not an unbounded middle-rebasing family.

Consuming that same-middle replay may require spending the original R434 birth witnesses or the exact current pair-deletion frame; no claim is made here that repetition of the same graph-intrinsic four-vertex atom alone is progress.

### 5. Scope
This theorem does not consume explicit nonquiet geometry after the P4 payment return. It does not claim different reentry frames with the same physical middle are identical current representatives. It proves only the middle-fan collapse: rank-flat predecessor-equality cannot move among two distinct middles.

R24 and R5 are unused.