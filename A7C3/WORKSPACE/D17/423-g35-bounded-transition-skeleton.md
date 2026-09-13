# The unique defect corridor has at most nine transition-bearing zipper indices

**Workspace:** D17
**State:** established
**Key:** `g35-bounded-transition-skeleton`

**Summary:** In the G35 source frame the old cover transition count is uniformly bounded: SV101138 gives tau(F)=2b_X+d_F(v)-2 with at most four nonempty X-blocks and d_F(v)<=2, hence 3<=tau(F)<=8. The canonical forest J has tau(J)=1. Along the unique augmenter C*=e1,f1,...,e_m, mark an index whenever its F-edge e_i or, for i<m, its J-edge f_i is an X|B transition. The number of marked indices is at most the number of F transitions on C* plus the number of J transitions on C*, hence at most tau(F)+tau(J)<=9. Every actual source-spoke transition carried by C* lies at a marked index. On each open run between marked indices both e_i and f_i are same-side, so the prefix transition sum S and the moving defect side are constant, and every normalized shortcut has constant transition cost. SV112526 then ensures physical blockers cannot be trapped behind the frontier inside such a zero-transition run: any exact blocker touches a later suffix edge and is destroyed by advancing past its last used suffix edge. Therefore the unbounded alternating path may be quotiented, for transition/descent purposes, to at most nine transition-bearing events plus the terminal augmentation event. This is a bounded skeleton reduction, not physical extinction.


### 1. Uniform transition bound in the old source cover
Retain the G35 packet on

  G=H-{A,C}=X union V(B),
  X={v,p,q,r},

with old exact source two-cover F and canonical tight three-forest J. The exact old-source degree law SV101138 gives

  tau(F)=2 b_X+d_F(v)-2,                                  (BS.1)

where b_X is the number of maximal nonempty X-blocks of F and d_F(v) is the selected degree of v. Since X has only four physical vertices,

  b_X<=4,                                                 (BS.2)

and since F is a path forest,

  d_F(v)<=2.                                              (BS.3)

Consequently

  tau(F)<=8.                                              (BS.4)

The source floor gives tau(F)>=3, while the canonical G35 cut has

  tau(J)=1.                                               (BS.5)

Thus the entire live source packet has a bounded transition budget independent of |B|.

### 2. Mark the transition-bearing zipper indices
Write the unique F-heavy augmenter as

  C_* = e_1,f_1,e_2,f_2,...,f_{m-1},e_m,

with e_i in F-J and f_i in J-F. Call an index i TRANSITION-BEARING when

  chi(e_i)=1,

or, for i<m,

  chi(f_i)=1.                                             (BS.6)

Let I be the set of such indices. Every transition edge of F occurring on C_* contributes to at least one element of I, and every J-transition occurring on C_* does likewise. Therefore

  |I| <= #(F transitions on C_*) + #(J transitions on C_*)
       <= tau(F)+tau(J)
       <= 9.                                              (BS.7)

If one index contains both an F transition and the sole J transition, it is counted only once, so (BS.7) may be strict.

By SV109219, C_* contains an actual old source-spoke-to-B incidence. Every such incidence is an F transition, hence occurs at one of the at most nine marked indices.

### 3. Between marked indices the transition ledger is completely flat
Consider a consecutive interval of zipper indices containing no member of I. For every index i in that interval,

  chi(e_i)=chi(f_i)=0.                                    (BS.8)

Hence

  Delta_i:=chi(e_i)-chi(f_i)=0.                           (BS.9)

The prefix transition sum S_q is constant throughout the interval. Zipper parity then also shows that the moving unmatched OUT vertex a_q remains on one fixed side of X|B throughout the interval, and the direct closing edge to the far unmatched IN endpoint has constant transition indicator. Thus every matching-level closure in one such interval has the same transition count.

These intervals are ZERO-TRANSITION TRANSPORT RUNS: they can move the physical defect, but they cannot change the numerical descent status.

### 4. Physical blockers cannot create a stationary state inside a zero-transition run
Apply the F-normalized blocker theorem SV112526. At every prefix q, any bad turn, backtrack, or directed cycle in the normalized prefix touches an unflipped suffix edge of C_* with index strictly larger than q. Advancing beyond every suffix edge used by that exact blocker destroys that exact configuration; any new blocker again reaches to a strictly later suffix position.

Inside a zero-transition run, this forward advancement changes neither S_q nor the transition cost of the associated closing shortcut by Section 3. Therefore a blocker may wander through the run, but it cannot create a new numerical state there and cannot move backward or remain supported wholly behind the frontier.

For transition/descent analysis, the entire run may consequently be regarded as one transport interval between its adjacent marked events. The physical witness must still be tracked while traversing the interval; no claim is made that all intermediate prefixes are tight forests.

### 5. Bounded transition skeleton
Contract every maximal zero-transition transport run to one interval edge while retaining each marked index of I as a vertex/event. The resulting ordered TRANSITION SKELETON has

  at most 9 marked transition events.                     (BS.10)

If the final augmenting edge e_m is same-side and hence unmarked, retain the terminal full-augmentation endpoint as one additional terminal event. Thus the entire unbounded alternating corridor is represented, for transition/descent purposes, by at most

  9 transition events + 1 terminal event.                 (BS.11)

The distinguished first-positive pivot, the two-ended low-transition boundaries, every source-bearing old transition on C_*, and every rise/fall of the normalized closing staircase all occur at marked skeleton events.

### 6. Consequence and scope
The live G35 obstruction is therefore not combinatorially unbounded in the coordinate that drives strict old-source descent. Long stretches through the spectator support B can carry physical blocker transport, but every change of X|B transition state occurs on a skeleton of uniformly bounded size at most nine, and source ancestry is present on that skeleton.

This does not by itself consume a bad shortcut seam, a loop coincidence, or a directed cycle, and it does not allow one to erase the exact physical labels traversed inside a zero-transition run when those labels are needed by a local consumer. It is a proof-architecture compression: a final defect-transport theorem need only understand bounded transition events plus monotone physical transport through the zero-cost intervals between them.

No R24, R5, payment, replay, SAT, MILP, or generic seam taxonomy is used.

