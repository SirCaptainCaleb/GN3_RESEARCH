# Neutral support copies into one singleton fiber have a strict hub-distance descent

**Workspace:** D17
**State:** established
**Key:** `singleton-neutral-hub-distance`

**Summary:** Fix a deletion fiber b and sum the support-partition Hamming disagreements of every other row with b. A seam-free R511 support copy a<-b sets the a,b overlap disagreement to zero and changes no other term in this hub potential, so every K-neutral copy into b strictly decreases a finite secondary coordinate. Thus in a K-minimal family chosen to minimize D_b, every R511 bridge into b must have strictly positive K cost or be replaced by a different defect species.

### Hub Hamming potential
Retain a family of singleton-deletion support partitions sigma_x. Fix one deletion label b. For every a!=b define

  d_b(a)=|{ unordered {u,v} subset V(H)-{a,b} :
             sigma_a and sigma_b give different same-block status to {u,v} }|.

Let

  D_b(F)=sum_{a!=b} d_b(a).

This is a finite support-level potential measuring how far the family is from the single hub row b. It ignores path orders.

### A seam-free R511 copy strictly lowers D_b
Suppose an ordered defect a<-b is in the seam-free R511 bridge form of `singleton-multirow-energy-ledger`. Its actual support-changing repair replaces sigma_a by

  sigma'_a = tau_{a<-b},

the deleted-label transport of sigma_b. By construction sigma'_a and sigma_b have identical restrictions to the common residue H-{a,b}. Hence

  d'_b(a)=0.

For every c outside {a,b}, neither sigma_c nor sigma_b changes, so

  d'_b(c)=d_b(c).

Therefore

  D_b(F') = D_b(F)-d_b(a).

Because a<-b is a genuine overlap disagreement, d_b(a)>=1. Thus every seam-free support copy into the fixed hub b strictly decreases D_b. No new support disagreement elsewhere can affect this particular potential.

### Consequence for neutral K moves
If the support copy is K-neutral, then F' is again globally K-minimal whenever F was. The strict D_b decrease gives an exact terminating secondary coordinate: a sequence of K-neutral seam-free R511 copies all directed into the same hub b can occur only finitely many times, at most D_b(F) times.

Equivalently, for any fixed b one may choose, among globally K-minimal cover families, a family minimizing D_b. In such a choice every genuine seam-free R511 bridge a<-b is forced to have strictly positive K-cost: it cannot lower K by minimality, and it cannot be neutral because neutrality would lower D_b.

This gives a useful fixed-hub normal form for the defect fan. Once b is chosen, every cross-fiber defect directed into b is either a direct selected source-rail crossing, a non-R511 residue, or an R511 bridge whose fully costed support copy strictly increases K and therefore exports more collateral than its repaired pair saving.

### Scope
D_b is a secondary potential only for copies directed into one fixed hub b. It does not compare moves with different hubs and does not prove that a fixed witness fan contains enough R511 copies into one hub. It is nevertheless a genuine terminating coordinate for neutral moves, as required by the coordinated K program.
