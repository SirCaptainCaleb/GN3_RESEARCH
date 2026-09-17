# Dual rigidity forces all useful motion inside the unique augmenting path

**Workspace:** D17
**State:** established
**Key:** `g34-unique-augmenter-prefix-defect-transport`

**Summary:** In the tau-one G34 dual-rigid packet, SV109219 gives exactly one F-heavy symmetric-difference component C* and every other component has delta=0. Therefore every union U of whole symmetric-difference components with matching gain delta(U)=1 must contain C*. By the defining dual-rigidity conclusion of SV103932, every such U has transition weight w(U)>=d=tau(F)-tau(J), so no whole-component recombination of size |M_F| can have transition count below tau(F). The strict-descent mechanism must therefore act inside C*, not merely choose a better family of whole alternating components. Writing C*=e1,f1,e2,...,f_{m-1},e_m in F/J alternating order, there is a canonical prefix ladder M_r obtained by replacing f_i with e_i for i<=r. For r<m this is a size-|M_J| matching carrying one transported unmatched-copy defect; the full r=m state has size |M_J|+1. The transition count of each prefix is exactly tau(J)+sum_{i<=r}(chi(e_i)-chi(f_i)), with the final e_m added at r=m. Thus the surviving G34 obstruction is a one-dimensional defect-transport problem along one source-bearing augmenting path. Any useful strict descent must exploit a proper prefix together with retained source geometry, or otherwise break the path internally. Bad mixed turns, backtracks and directed cycles are physical blockers of prefix realization, not new obstruction families.


### 1. Input: the tau-one dual-rigid packet
Retain SV109219. Thus on the fixed top fiber G the old source representative F is an exact two-cover, J is a literal tight spanning three-forest, and

  tau(J)=1,
  d:=tau(F)-tau(J)>=2.

In the DUAL RIGIDITY branch of SV103932 the bipartite matching symmetric difference

  M_F triangle M_J

has exactly one component C_* with

  delta(C_*)=+1,

no component with delta=-1, and every other component has delta=0.

### 2. Whole-component recombination cannot produce transition descent
Let U be any union of complete connected components of M_F triangle M_J. If the componentwise recombination has the same matching size as F, then

  delta(U)=1.

Because C_* is the unique positive-delta component and every other component has delta zero, this is equivalent to

  C_* in U.                                                (PD.1)

But DUAL RIGIDITY in SV103932 says exactly that every component subfamily of total delta one has transition weight at least the full gap d. Therefore

  w(U)>=d.                                                 (PD.2)

The recombined matching has transition count

  tau(J)+w(U) >= tau(J)+d = tau(F).                        (PD.3)

Hence no recombination obtained by flipping only WHOLE symmetric-difference components can be the desired strict old-source transition descent. This remains true even if a collision-preorder closure forces extra delta-zero components to accompany C_*: such closure may repair physical turn compatibility, but it cannot lower the transition count below tau(F) in the dual-rigid branch.

Thus the remaining obstruction is not a choice among alternating components. Useful motion must cut inside the unique augmenting component C_* or use additional retained source geometry before C_* is flipped in full.

### 3. Canonical prefix defect transport on C_*
Orient the alternating path C_* from one endpoint copy unmatched by M_J to the other. Since C_* is F-heavy, its copy-edge sequence is

  e_1, f_1, e_2, f_2, ..., f_{m-1}, e_m,                  (PD.4)

where every e_i belongs to M_F-M_J and every f_i belongs to M_J-M_F.

For 0<=r<m define

  M_r := M_J - {f_1,...,f_r} + {e_1,...,e_r}.             (PD.5)

Set M_0=M_J. Because e_1 begins at an M_J-unmatched copy and each consecutive pair e_i,f_i shares the next occupied copy of the alternating path, (PD.5) is a bipartite matching of the SAME cardinality as M_J. Equivalently, each prefix replacement moves one unmatched matching copy one step forward along C_* without changing the number of selected adjacencies.

The full augmentation is

  M_m := M_J - {f_1,...,f_{m-1}} + {e_1,...,e_m},          (PD.6)

and has

  |M_m|=|M_J|+1=|M_F|.                                    (PD.7)

Thus C_* carries a canonical one-dimensional ladder of defect positions. The strict matching gain appears only at the final endpoint; every proper prefix is a size-|M_J| defect-transport state.

### 4. Exact transition ledger along the prefix ladder
For a selected directed adjacency e write chi(e)=1 if e crosses the fixed partition X|B and chi(e)=0 otherwise. Since every edge outside C_* remains exactly as in J, for r<m,

  tau(M_r)=tau(J)
           + sum_{i=1}^r (chi(e_i)-chi(f_i)).              (PD.8)

For the full augmentation,

  tau(M_m)=tau(J)
           + sum_{i=1}^{m-1}(chi(e_i)-chi(f_i))
           + chi(e_m).                                    (PD.9)

If the other delta-zero components remain in their J state, (PD.9) is the transition count of flipping C_* alone. More generally Section 2 shows that after ANY whole-component closure completing the matching gain, the transition count is still at least tau(F).

Therefore a strict transition descent, if obtained from this packet, must use a proper defect position M_r together with some extra physical/source operation, or must replace part of C_* by structure not equal to a union of its original whole symmetric-difference components. The old source trimers and source-spoke incidences are precisely the retained data capable of such an internal intervention.

### 5. Physical realization and the meaning of a blocker
Each M_r is automatically a bipartite matching, but it need not yet be a tight path forest. Its only possible physical defects are the familiar ones: a selected two-edge backtrack, a bad mixed predecessor-successor turn, or a directed cycle. A bad mixed turn is reversed by R3 on the same three-vertex support; the resulting tight orientation need not preserve the direction of the old F-edge that participated in the failed pivot.

This is the correct role of the source-rooted trimer in SV108809: it is a local witness that the first attempted defect position is not directly realizable, not a new global obstruction family. The natural continuation is to understand whether the defect can be transported farther along C_* or consumed by retained source geometry.

### 6. Consequence for G34
The G34 parent object has therefore contracted again. It is not an arbitrary weighted defect-one exchange and not a family of seam or trimer species. It is one source-bearing F-heavy alternating path C_* equipped with

- its ordered F/J edge sequence;
- one moving unmatched-copy defect along the prefix ladder;
- the exact prefix transition ledger;
- at least one actual old source-spoke-to-B incidence carried by C_* from SV109219;
- the corresponding historical source trimer (A,t,C);
- and, only when a prefix is physically blocked, the exact local R3 reversal support witnessing that block.

The next theorem should consume this path as a path. Whole-component collision closure is now fenced as too coarse for strict transition descent.

R24, R5, payment, replay, and generic seam taxonomy are unused.

