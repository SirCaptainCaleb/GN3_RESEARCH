# The unique augmenter has a two-ended low-transition defect corridor containing source ancestry

**Workspace:** D17
**State:** established
**Key:** `g34-two-ended-low-transition-defect-corridor`

**Summary:** Let C*=e1,f1,...,f_{m-1},e_m be the unique F-heavy augmenting path of SV109629, with ai=chi(ei), bi=chi(fi). Since C* carries at least two old F transitions, let j be the first index with aj=1 and k the last. The left prefix defect state that replaces f1,...,fj by e1,...,ej has the same matching size as J and transition count tau(J)+1-sum_{i<=j}bi<=2. Dually, reading C* from the other endpoint, the right defect state that replaces f_{k-1},...,f_{m-1} by e_k,...,e_m also has size |M_J| and transition count at most 2. Thus C* has canonical low-transition defect positions at both ends of its F-transition support. If either boundary F-transition is incident with a source spoke, that boundary state is already source-bearing. If neither is source-bearing, both transitions must be incident with the only non-spoke vertex v of X; being distinct selected F-edges, they exhaust v selected transition degree, so every further F-transition strictly between them is source-spoke-bearing. Since SV109219 guarantees C* contains a source-spoke transition, the corridor between the two low-transition boundary positions contains source ancestry. Physical tightness/cycle realization of the two defect states remains the next issue.


### 1. Input and notation
Retain the one-dimensional G34 normal form SV109629. Thus the unique F-heavy alternating component is

  C_* = e_1,f_1,e_2,f_2,...,f_{m-1},e_m,                 (DC.1)

with e_i in M_F-M_J and f_i in M_J-M_F, while

  tau(J)=1.

Write

  a_i=chi(e_i),  b_i=chi(f_i),                            (DC.2)

where chi is the indicator of crossing the fixed physical partition X|B. By SV109219, C_* contains at least two old F transitions, so at least two a_i equal one.

### 2. The left boundary of the F-transition support is low-transition
Let

  j=min{i : a_i=1}.                                       (DC.3)

Use the left prefix defect state from SV109629:

  L := M_J - {f_1,...,f_j} + {e_1,...,e_j}.              (DC.4)

This is a bipartite matching with exactly |M_J| selected edges. Its transition count is

  tau(L)=tau(J)+sum_{i=1}^j(a_i-b_i).

By minimality of j, a_i=0 for i<j and a_j=1. Therefore

  tau(L)=1+1-sum_{i=1}^j b_i <=2.                         (DC.5)

Thus the first old F transition encountered from the left admits a matching-level defect position with at most two X|B transitions.

### 3. The right boundary is equally low-transition
Let

  k=max{i : a_i=1}.                                       (DC.6)

Read the same alternating path from its other endpoint. The reversed alternating sequence begins with e_m and has the same prefix-defect construction. Translating that construction back to the indexing (DC.1) gives

  R := M_J - {f_{k-1},f_k,...,f_{m-1}}
             + {e_k,e_{k+1},...,e_m}.                    (DC.7)

The two sets in (DC.7) have the same cardinality m-k+1, so |R|=|M_J|. Its transition count is

  tau(R)=tau(J)
         + sum_{i=k}^m a_i
         - sum_{i=k-1}^{m-1} b_i.

By maximality of k, the first sum equals a_k=1. Hence

  tau(R)=1+1-sum_{i=k-1}^{m-1}b_i <=2.                   (DC.8)

So the last old F transition encountered from the right also admits a matching-level defect position with at most two transitions.

### 4. The two low-transition boundaries bracket source ancestry
Call e_j and e_k the left and right boundary F-transitions of C_*. By SV109219 at least one old source-spoke-to-B transition belongs to C_*.

If e_j or e_k is incident with a source spoke in {p,q,r}, then the corresponding low-transition defect state L or R is already anchored at a source-bearing F-transition and retains the historical source trimer (A,t,C) for that spoke t.

Assume neither boundary transition is source-bearing. Every X|B transition has its X endpoint in

  X={v,p,q,r}.

Therefore both e_j and e_k are incident with v. They are distinct because C_* contains at least two F transitions. Since F is a path forest, v has selected degree at most two, so these two selected transition edges exhaust every possible F-transition incident with v. Consequently every additional F-transition e_i with

  j<i<k                                                   (DC.9)

is incident with one of the source spokes p,q,r. Since C_* is source-bearing by SV109219, at least one such interior source transition exists.

Hence the F-transition support of C_* has the following exact normal form: two canonical defect positions of transition count at most two occur at its two boundaries, and either one boundary is already source-bearing or the interval between them contains a source-bearing F-transition and no further v-transition.

### 5. Physical meaning
The states L and R are guaranteed bipartite matchings of the same cardinality as J. They are not asserted automatically to be physical tight three-forests. As in SV109629, the only possible physical failures are backtracks, bad mixed turns, or directed cycles. A bad mixed turn carries its exact R3 reversal support, with no assumption that an old F-edge orientation survives in the tight reverse.

The point of the two-ended construction is strategic: the source-bearing part of the unique augmenter is trapped inside a corridor whose two boundary defect positions are already below the old transition floor tau(F)>=3. One no longer needs to search the full alternating path for a favorable transition placement.

### 6. Scope
This is a matching-level localization theorem. It does not yet prove that L or R is physically realizable, does not close a blocker trimer, and does not assert that the source-bearing transition itself lies at an endpoint of C_*. It reduces the remaining G34 task to consuming one source-bearing low-transition defect corridor on one alternating path.

R24, R5, payment, replay, whole-component collision classification, and seam taxonomy are unused.

