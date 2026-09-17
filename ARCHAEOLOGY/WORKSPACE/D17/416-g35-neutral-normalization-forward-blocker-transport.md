# Neutral normalization makes every prefix blocker point strictly forward on the unique augmenter

**Workspace:** D17
**State:** established
**Key:** `g35-neutral-normalization-forward-blocker-transport`

**Summary:** In the tau-one dual-rigid G35 packet, fix any proper prefix of the unique augmenter C*. Flip every delta-zero symmetric-difference component completely to its F-state while keeping the prefix of C* in F-state and its remaining suffix in J-state. Because every neutral component has delta=0 and nonpositive transition weight, this preserves matching cardinality and cannot increase tau. Outside the still-unflipped suffix of C*, both physical matching copies at every vertex now agree exactly with F; therefore no bad turn or backtrack can occur there. Likewise any directed cycle avoiding the suffix would be a directed cycle of F, impossible. Hence every physical blocker necessarily contains a selected J-edge from a strictly later suffix position. Advancing the prefix beyond all suffix edges in a given blocker destroys that exact blocker, and every new blocker again touches a strictly later suffix. The process is well-founded and ends at the literal forest F-e_m. In particular, through the first-positive index r, either one obtains a physical normalized prefix of transition count at most two or all failures transport the obstruction strictly forward across the corridor. Neutral components therefore cannot trap the defect or create backward obstruction debt.

### 1. Prefixes with every neutral component normalized to F
Retain the tau-one dual-rigid G35 packet. Thus the symmetric difference M_F triangle M_J has one F-heavy alternating path

  C_* = e_1,f_1,e_2,f_2,...,f_{m-1},e_m,

and every other connected component D has delta(D)=0 and w(D)<=0. For 0<=q<m let M_q be the usual prefix defect matching of SV109629.

Define the F-NORMALIZED PREFIX \hat M_q as follows: on C_* use the F-edges e_1,...,e_q on the prefix and the J-edges f_{q+1},...,f_{m-1} on the still-unflipped suffix; on every delta-zero symmetric-difference component use its F-state; retain every common edge. Equivalently, start from M_q and flip every neutral component completely from J to F.

Because every neutral component has delta zero,

  |\hat M_q|=|M_q|=|M_J|.                                  (NN.1)

Let W_0=sum_D w(D), summed over all neutral components. Dual rigidity gives W_0<=0, so

  tau(\hat M_q)=tau(M_q)+W_0 <= tau(M_q).                   (NN.2)

Thus neutral normalization costs no matching gain and never worsens the transition ledger.

### 2. Behind the frontier the selected state is literally F
Fix a physical vertex z. Suppose neither matching copy z_in nor z_out belongs to the still-unflipped suffix of C_*. Then every changed copy at z is either on the flipped prefix of C_* or on a neutral component, and in both cases \hat M_q chooses the F-state. Every unchanged copy is common to F and J. Hence the selected incoming and outgoing incidences of \hat M_q at z, including possible absence of one incidence, are exactly the selected incidences of F at z.

Consequently a selected two-edge backtrack cannot occur at such z, because F is a path forest. If both incidences are present, their ordered turn is literally the corresponding F-turn and is tight. Therefore:

  every bad selected turn or backtrack of \hat M_q touches
  a matching copy lying on the unflipped suffix of C_*.          (NN.3)

This is stronger than a generic collision-preorder statement: after neutral normalization there is no physical turn debt supported wholly behind the moving defect.

### 3. Every directed cycle also touches the future suffix
Suppose \hat M_q contains a directed physical cycle Z. If Z used no selected edge from the unflipped suffix of C_*, then every selected edge of Z would be an F-edge: off that suffix the normalized matching agrees edge-for-edge with F. The same directed cycle Z would therefore occur in F, impossible because F is an exact two-path forest. Hence

  every directed cycle of \hat M_q contains at least one
  selected suffix edge f_i with i>q.                            (NN.4)

Thus cycle debt is forward debt as well.

### 4. A blocker can only be transported forward
Take any concrete bad turn, backtrack, or directed cycle B in \hat M_q. By (NN.3)-(NN.4), B contains at least one currently selected suffix edge f_i with i>q. Advance the prefix beyond every suffix edge of C_* used by this exact blocker, obtaining some q'>q. In \hat M_{q'}, each of those former suffix copies has been changed to its F-state. Therefore the exact selected configuration B no longer occurs.

Any new blocker in \hat M_{q'} again contains an unflipped suffix edge f_j with j>q'. In particular no blocker supported entirely at indices <=q' can be born. Repeating this operation strictly increases the prefix index, so it is well-founded. At q=m-1 there is no selected J-edge left on C_*; the normalized matching is exactly

  \hat M_{m-1}=M_F-{e_m},                              (NN.5)

which is a literal tight spanning three-path forest.

Hence neutral components can never trap the defect in a closed local obstruction. Every physical failure either disappears after neutral normalization or certifies strict forward contact with the remaining C_* suffix.

### 5. Low-transition consequence through the first positive pivot
Let r be the first positive index of SV110451. For q<r, SV111694 gives tau(M_q)<=1, while tau(M_r)=2. Combining with (NN.2),

  tau(\hat M_q)<=1  for q<r,
  tau(\hat M_r)<=2.                                      (NN.6)

Therefore either some normalized prefix at or before r is already a literal tight three-forest with transition count at most two, or every attempted realization up to that point carries an explicit blocker whose support reaches strictly farther along C_*. In the latter case the obstruction has literally transported across the first-positive pivot; it has not remained attached to a neutral component or moved backward.

Whenever a normalized pre-pivot prefix is a forest, the strict-descent closing fan of SV111694 applies with an equal-or-better transition ledger. A failed closing edge may still leave a local reverse-seam or same-rail cycle witness, but the underlying prefix itself has no hidden neutral-component collision debt.

### 6. Scope
This is a blocker-transport theorem, not final extinction. It does not assert that a strict-descent shortcut succeeds once the normalized prefix is physical, and it does not consume a shortcut reverse seam or same-rail cycle. Its role is to remove every delta-zero component from the obstruction mechanism: all surviving prefix blockers are forced onto the one ordered future suffix of C_*. No R24, R5, payment, replay, SAT, MILP, or blocker taxonomy is used.
