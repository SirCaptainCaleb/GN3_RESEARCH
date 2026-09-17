# The sole parity-hard shortcut cell has a source-bearing low-transition boundary

**Workspace:** D17
**State:** established
**Key:** `g35-hard-cell-source-boundary`

**Summary:** Assume the unique G35 augmenter lies in the sole numerical non-descent cell of SV111278: tau(F)=3, d=tau(F)-tau(J)=2, and w(C*)=2. The exact old-source degree law SV101138 then forces b_X(F)=2 and d_F(v)=1. Let e_j,e_k be the first and last old F transitions on C* as in SV110040. That theorem shows that if neither boundary transition is source-bearing, both must be incident with the unique non-spoke vertex v. Since e_j and e_k are distinct selected F transitions, this would give d_F(v)>=2, contradiction. Hence at least one boundary F transition is an actual source-spoke-to-B incidence. The corresponding left or right defect matching of SV110040 has transition count at most two and retains the historical source trimer (A,t,C). Thus even the sole parity-hard matching cell cannot hide all source ancestry in the corridor interior; one canonical low-transition boundary is source-anchored. The remaining obligation is physical realization/consumption of that boundary state.


### 1. The sole numerical shortcut exception
Retain the G35 dual-rigid packet and suppose the internal shortcut theorem SV111278 lands in its unique numerical non-descent cell

  tau(F)=3,
  tau(J)=1,
  d:=tau(F)-tau(J)=2,
  w(C_*)=2.                                                (HB.1)

Here C_* is the unique F-heavy alternating component from SV109219.

### 2. The old source degree law becomes sharp
Apply the exact source-crossing degree law SV101138 to the old exact source cover F. With b_X the number of maximal X-blocks and d_F(v) the selected degree of the unique non-spoke vertex v in X={v,p,q,r},

  tau(F)=2 b_X + d_F(v)-2,
  b_X>=2,
  d_F(v) in {1,2}.                                        (HB.2)

Substituting tau(F)=3 gives the unique solution

  b_X=2,
  d_F(v)=1,
  b_B=3.                                                   (HB.3)

Thus v is an endpoint of its old F-rail and is incident with only one selected F-edge in total.

### 3. One corridor boundary must be source-bearing
Let

  j=min{i: chi(e_i)=1},
  k=max{i: chi(e_i)=1}

be the first and last old F transitions on C_* as in SV110040. They are distinct because C_* carries at least two F transitions.

SV110040 gives the exact alternative: if either e_j or e_k is incident with a source spoke in {p,q,r}, the corresponding low-transition boundary defect state is already source-bearing; otherwise both e_j and e_k must be incident with v, the only non-source vertex of X.

Assume for contradiction that neither boundary transition is source-bearing. Then e_j and e_k are two distinct selected F-edges incident with v. Hence

  d_F(v)>=2,                                               (HB.4)

contradicting (HB.3).

Therefore

  at least one of e_j,e_k is a source-spoke-to-B edge.     (HB.5)

Write that edge as t-h with t in {p,q,r} and h in B. The graph-intrinsic historical source trimer

  (A,t,C)

is retained simultaneously.

### 4. The hard cell has a source-anchored low-transition boundary
For e_j, SV110040 supplies the left boundary defect matching L; for e_k it supplies the right boundary defect matching R. Each has the same matching cardinality as J and transition count at most two. By (HB.5), at least one of these two canonical boundary states is attached to an actual old source transition t-h.

Hence the sole numerical cell in which the SV111278 first-positive internal shortcut can have transition count equal to tau(F) still has a canonical source-bearing defect position with

  tau<=2<tau(F)=3.                                         (HB.6)

The source ancestry cannot be hidden strictly inside the corridor in this hard case.

### 5. Scope
This is a localization theorem, not physical closure. The source-bearing boundary matching need not yet be a literal tight acyclic three-forest, and this section does not consume its bad mixed turn, backtrack, directed cycle, or shortcut seam. Its role is to eliminate the only numerical excuse for treating the parity-hard cell as source-anonymous: one low-transition boundary is necessarily anchored at a physical source-spoke transition and its source trimer.

No R24, R5, payment, replay, MILP, SAT, or seam taxonomy is used.

