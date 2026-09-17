# The first positive prefix has transition count two and a crossing pivot

**Workspace:** D17
**State:** established
**Key:** `g34-first-positive-prefix-low-transition-pivot`

**Summary:** In the tau-one dual-rigid G34 packet, orient the unique augmenter C*=e1,f1,...,f_{m-1},e_m and let S_r=sum_{i<=r}(chi(e_i)-chi(f_i)) for r<m. Since w(C*)>=d>=2 while chi(e_m)<=1, S_{m-1}>=1. Hence there is a first proper index r with S_r=1. By minimality and unit increments, chi(e_r)=1 and chi(f_r)=0. The proper prefix matching M_r therefore has exactly tau(M_r)=2, while every earlier prefix has transition count at most one. Thus before the final matching gain occurs, the moving defect necessarily crosses an actual old F X|B edge while deleting a same-side J edge. This gives a canonical first low-transition pivot inside the unique source-bearing augmenter; any physical blocker at that pivot is attached to a transition edge rather than an anonymous same-side move.

### 1. Setup
Retain the tau-one dual-rigid G34 packet and the prefix ladder of SV110451. Thus the unique F-heavy alternating path is

  C_* = e_1,f_1,e_2,f_2,...,f_{m-1},e_m,

with e_i in M_F-M_J and f_i in M_J-M_F. The canonical proper-prefix matching M_r, 0<=r<m, replaces f_i by e_i for i<=r and has the same matching cardinality as J. Write chi(g)=1 when the selected directed adjacency g crosses X|B and chi(g)=0 otherwise, and put

  S_r := sum_{i=1}^r (chi(e_i)-chi(f_i)),   S_0=0.          (FP.1)

By SV110451,

  tau(M_r)=tau(J)+S_r=1+S_r.                              (FP.2)

The full component transition weight is

  w(C_*)=S_{m-1}+chi(e_m).                                (FP.3)

### 2. A positive proper prefix is forced
Dual rigidity and SV109219 give

  w(C_*)>=d:=tau(F)-tau(J)>=2.                             (FP.4)

Since chi(e_m)<=1, equations (FP.3)-(FP.4) imply

  S_{m-1}>=1.                                             (FP.5)

Therefore there exists a least proper index r, 1<=r<m, with S_r>=1. Every increment

  S_i-S_{i-1}=chi(e_i)-chi(f_i)

lies in {-1,0,1}. Hence at the first positive crossing we have exactly

  S_{r-1}<=0,
  S_r=1.                                                  (FP.6)

The increment at r must be +1, so

  chi(e_r)=1,
  chi(f_r)=0.                                             (FP.7)

Thus the r-th defect-transport pivot installs an actual old F X|B transition e_r and removes a same-side J edge f_r.

### 3. Canonical tau-two checkpoint
By (FP.2) and (FP.6),

  tau(M_r)=2.                                             (FP.8)

For every q<r,

  S_q<=0,

so

  tau(M_q)<=1.                                            (FP.9)

Thus along the unique augmenter there is a canonical FIRST tau-two defect position, and it is reached precisely by crossing one old-source transition edge. This occurs strictly before the final augmenting edge e_m is installed, so the matching still has the three-forest cardinality |M_J|.

### 4. Physical interface
The prefix state M_r is automatically a bipartite matching. If it is physically realized as a tight acyclic forest, it is a spanning three-path forest with exactly two X|B transitions and one moving unmatched-copy defect. Any physical obstruction to this realization must occur at or before the r-th pivot. At the first pivot the newly installed edge e_r is a genuine old source transition, while the removed f_r is same-side. Therefore any mixed-turn or copy-competition blocker born exactly at the first positive step retains the physical support and old-source orientation of a transition edge.

This is sharper than the generic statement that the unique augmenter contains at least two source transitions: it identifies a canonical ordered transition pivot before final matching gain.

### 5. Scope
This is a transition-ledger lemma, not yet a blocker consumer. It does not assert that M_r is always a tight forest, nor that the first physical obstruction occurs exactly at step r. It supplies the canonical low-transition checkpoint and the source-crossing nature of the pivotal edge. No MILP, SAT, R24, R5, payment, replay, or seam taxonomy is used.

