# The tau-one G34 defect has one source-bearing augmenter and at most one neutral transition component

**Workspace:** D17
**State:** established
**Key:** `g34-tau-one-unique-source-bearing-augmenter`

**Summary:** For the canonical G34 cut of SV108809, tau(J)=1 while tau(F)>=3. In the SV103932 dual-rigid branch the SV105548 count bound gives (P-1)d<=tau(J)=1 with d=tau(F)-tau(J)>=2, hence there is exactly one delta=+1 symmetric-difference component C* and no delta=-1 component. Every delta-zero component not containing the unique J transition has no X|B transition from either forest; the possible exceptional zero component contains the unique J transition and at most one F transition. Consequently C* contains at least tau(F)-1>=2 old F transitions. Since SV101138 gives old X|B transitions incident with at least two distinct source spokes, C* contains an actual old source-spoke-to-B incidence. For the retained omitted-spoke incidence e_s=s-h, which cannot be common because the canonical J-component of s is a singleton or X-dimer, either e_s lies on C*, or it lies on the unique exceptional zero component C0. In the latter case C0 contains exactly one F transition e_s and exactly the sole J transition, so w(C0)=0; C* then carries every other F transition and no J transition. C0 is rooted at a free matching copy of s only when e_s itself uses such a copy; in the reverse-X-dimer subcase of the rooted repair the active edge can use the J-occupied copy, so no endpoint-at-s claim is made there.


### 1. Canonical tau-one input
Retain the direct G34 packet through SV108809. Thus on the fixed top fiber

  G=H-{A,C}=X union V(B),

F is the actual old exact source two-cover, while J is the canonical literal spanning tight three-forest obtained from the bad one-hole proposal. The exact transition counts satisfy

  tau(J)=1,
  tau(F)>=3.

Put

  d=tau(F)-tau(J)>=2.                                      (UA.1)

Encode F,J by their directed bipartite matchings and let the connected components of M_F triangle M_J carry the SV103932 weights

  delta(C)=|F cap C|-|J cap C| in {-1,0,1},
  w(C)=tau(F cap C)-tau(J cap C).

Assume the DUAL RIGIDITY branch of SV103932, since the other branch already contains a matching-level strict transition descent candidate.

### 2. There is exactly one augmenting component and no losing component
Let P and N denote the numbers of components with delta=+1 and delta=-1. The refined counting theorem SV105548 gives

  (P-1)d <= tau(J).                                        (UA.2)

Using (UA.1) and tau(J)=1,

  2(P-1)<=1,

so

  P=1.                                                     (UA.3)

Since the total matching excess is

  sum_C delta(C)=1,

we also have P-N=1, hence

  N=0.                                                     (UA.4)

Write C_* for the unique delta=+1 component. It is an honest F-heavy alternating augmenting path for J. Every other symmetric-difference component has delta=0.

### 3. Only one neutral component can carry any transition data
Dual rigidity says every delta-zero component C has w(C)<=0. Let j_C and f_C be its numbers of J- and F-selected X|B edges. If C does not contain the unique J transition, then j_C=0 and

  w(C)=f_C>=0.

Therefore w(C)=0 and f_C=0. Thus every delta-zero component except possibly the one containing the unique J transition is completely transition-free.

If a delta-zero component C_0 does contain the unique J transition, then j_{C_0}=1 and w(C_0)<=0 gives

  f_{C_0}<=1.                                              (UA.5)

There is at most one such C_0.

A transition common to F and J lies outside the symmetric difference. Since J has only one transition in total, the alternatives are therefore exhaustive: the unique J transition is common, lies on C_*, or lies on one delta-zero component C_0. In every case at most one F-transition lies outside C_*.

Consequently

  f_{C_*} >= tau(F)-1 >=2.                                 (UA.6)

So the unique augmenting path itself carries at least two actual old X|B source-cover incidences.

### 4. The unique augmenter is source-bearing
The old source-cover degree law SV101138 proves that at least two distinct source spokes among p,q,r are incident with selected old F transitions into B. Since by (UA.6) at most one old transition lies outside C_*, at least one of those source-spoke transitions lies on C_*.

Hence there exist

  t in {p,q,r},  h in V(B)

such that the actual old selected edge t-h belongs to C_*. The historical source trimer

  (A,t,C)

is retained simultaneously. Thus the G34 augmenting path is not an anonymous matching object: it necessarily carries a literal old source-spoke-to-spectator incidence.

### 5. Exact dichotomy for the omitted active spoke
Let e_s=s-h_s be the retained old B-active incidence of the omitted spoke s. In the canonical J of SV108809, the J-component containing s is either the singleton (s) or an X-dimer. Therefore no selected s-B edge belongs to J, so e_s is not common to F and J.

If e_s belongs to C_*, the unique augmenting path is directly incident with the retained omitted-spoke source transition.

Assume instead that e_s does not belong to C_*. Then it lies on a delta-zero component C_0. Because e_s itself contributes one F-transition, f_{C_0}>=1. By Section 3 this forces C_0 to contain the unique J transition, and (UA.5) sharpens to

  f_{C_0}=j_{C_0}=1,
  w(C_0)=0.                                                (UA.7)

Every other old F-transition belongs to C_*, and C_* contains no J-transition.

No endpoint-at-s assertion is automatic for C_0. If the matching copy of s used by e_s is unmatched in J, then C_0 is indeed an alternating path with that s-copy as an endpoint. But the rooted repair has an exceptional X-dimer subcase: the F-edge at the free copy of s can be the exact reverse of the J dimer, while the retained s-B edge uses the other, J-occupied copy. In that subcase C_0 need not have an endpoint at s. The valid invariant is the exact one-for-one transition balance (UA.7), not rootedness of C_0.

Thus the exact alternative is:

1. OMITTED-SPOKE AUGMENTER: e_s lies on the unique F-heavy augmenting path C_*; or
2. UNIQUE NEUTRAL CANCELLATION: e_s lies on the sole possible delta-zero transition component C_0, which carries precisely e_s as its only F-transition and precisely the unique J-transition.

### 6. Scope
This is a structural contraction of the G34 blocked-augmenting-path parent, not yet its extinction. It does not claim that flipping C_* is physically tight or acyclic, and it does not count the neutral component as progress. Its use is to force the unique augmenting path to carry actual source ancestry and to show that the omitted-spoke source edge can avoid that path only through one completely pinned one-for-one transition component. No R24, R5, payment, replay, finite search, MILP, or SAT is used.

