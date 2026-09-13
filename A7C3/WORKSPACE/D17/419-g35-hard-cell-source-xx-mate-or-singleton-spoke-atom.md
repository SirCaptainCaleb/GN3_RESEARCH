# The tau-three hard cell has an X-mated source gate or one singleton-spoke two-transition atom

**Workspace:** D17
**State:** established
**Key:** `g35-hard-cell-source-xx-mate-or-singleton-spoke-atom`

**Summary:** In the sharp G35 hard cell tau(F)=3,tau(J)=1,w(C*)=2, the source degree law gives b_X=2 and at least two distinct B-active source spokes. At most one source spoke can have both old F incidences crossing X|B, because such a spoke is a singleton maximal X-block and two such spokes would consume both X-blocks while leaving the other two X vertices uncovered. Hence some B-active source spoke has exactly one B-transition and one selected X-X incidence. Either the B-transition of such a spoke lies on the unique augmenter C*, giving a source-bearing transition with an old same-side X-X mate, or no such transition lies on C*. In the latter case the unique F-transition outside C* is precisely the non-double source transition; the unique source-bearing transition species on C* comes from the sole double-B source spoke t, both transition edges at t must lie on C*, and because w(C*)=2 the augmenter contains exactly those two F transitions and no J-transition. Thus the exceptional hard corridor is a single-source two-switch atom: all f_i on C* are same-side and the prefix transition sum is 0 before the first t-transition, 1 between the two t-transitions, and 2 after the second.

### 1. Hard-cell input
Retain the sharp G35 zipper cell

  tau(F)=3,   tau(J)=1,   w(C_*)=2,

with C_* the unique F-heavy alternating component of SV109219. By the old source degree law SV101138, the old exact source cover F has

  b_X(F)=2,   d_F(v)=1,

and at least two distinct source spokes among p,q,r are incident with selected F transitions into B.

Call a source spoke t DOUBLE-B if both of its selected old F incidences cross X|B. Because every source spoke is internal in F, a DOUBLE-B spoke has B-neighbors on both sides and is therefore a singleton maximal X-block of F.

### 2. At most one source spoke is DOUBLE-B
There are exactly b_X(F)=2 maximal X-blocks containing all four vertices of

  X={v,p,q,r}.

If two distinct source spokes were DOUBLE-B, each would by itself be a singleton maximal X-block. Those two singleton blocks would already exhaust the two available X-blocks, while the remaining two vertices of X would still have to lie in some maximal X-block, contradiction. Hence

  at most one source spoke is DOUBLE-B.                    (HX.1)

Since at least two distinct source spokes are B-active, there exists a B-active source spoke u which is not DOUBLE-B. As u is internal of selected degree two, it has exactly one old B-transition u-h and its other selected F-incidence u-x is an X-X edge. Retain both physical incidences and their literal old F order.

### 3. If an X-mated source transition lies on C_*, retain it
If the transition u-h of some non-DOUBLE-B source spoke u lies on C_*, we are in the X-MATED SOURCE GATE alternative. Thus C_* contains an actual old source-spoke-to-B transition whose other old F-incidence is same-side inside X. The historical source trimer

  (A,u,C)

is retained simultaneously.

No assertion is made here about the relative zipper positions of u-h and u-x. Under the F-normalized prefixes of SV112526, if the u-x copy is already behind the frontier, common, or carried by a normalized neutral component, the local turn at u is literally its old F turn and is automatically tight. If u-x is still on the future C_* suffix, any source-local blocker necessarily reaches forward to that same-side incidence.

### 4. Otherwise C_* is exactly one singleton-spoke two-transition atom
Assume no B-transition of any non-DOUBLE-B source spoke lies on C_*. The transition u-h from Section 2 therefore lies outside C_*. By SV109219 at most one old F transition lies outside C_*. Consequently u-h is the unique such transition.

The augmenter C_* is nevertheless source-bearing by SV109219. Therefore it contains a transition at a source spoke t. By the assumption of this section, t must be DOUBLE-B. By (HX.1) it is the unique DOUBLE-B source spoke. Since u-h is already the unique F-transition outside C_*, both B-transition incidences of t must lie on C_*. The three old F transitions are now exhausted:

  two transitions at t lie on C_*,
  the single transition u-h lies outside C_*.             (HX.2)

Hence C_* contains exactly two F-selected X|B edges. Since its transition weight is w(C_*)=2, it contains no J-selected X|B edge at all. In zipper notation

  C_*=e_1,f_1,...,f_{m-1},e_m,

we therefore have

  sum_i chi(e_i)=2,   chi(f_i)=0 for every i<m.           (HX.3)

Both transition e-edges in (HX.3) are precisely the two old F incidences of the same source spoke t. Thus the prefix transition sum S_q is monotone and has the exact three-level form

  S_q=0 before the first t-transition,
  S_q=1 between the two t-transitions,
  S_q=2 after the second t-transition.                    (HX.4)

In particular the first-positive pivot of SV110451 is exactly the first of the two old B-incidences at t. The hard corridor has no transition-bearing J edge and no second source species on C_*: it is one physical source vertex whose two matching copies switch at two positions of the unique augmenter.

### 5. Consequence and scope
The sharp tau-three hard cell therefore has exactly two source-geometric alternatives:

1. X-MATED SOURCE GATE: C_* contains a source B-transition t-h and the other selected old F-incidence at t is an X-X edge; or
2. SINGLETON-SPOKE TWO-SWITCH ATOM: C_* contains exactly the two B-transitions incident with one DOUBLE-B source spoke t, contains no J-transition, and the unique remaining old F transition is the B-transition of a different non-DOUBLE-B source spoke outside C_*.

This is a structural contraction, not physical closure. In alternative 1 the same-side old mate is the natural forward endpoint of any source-local blocker after neutral normalization. Alternative 2 isolates the genuinely exceptional object to one source vertex and two switch positions. No R24, R5, payment, replay, SAT, MILP, or blocker taxonomy is used.
