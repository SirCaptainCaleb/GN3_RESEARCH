# Reconstruction of Astra 11/12 clean-contact route

## Statement

Astra interruption reconstruction: the certified inequality 3m-A<=2 sum_v phi(v)-n would combine with a local/global clean-contact packing bound A<=3/4 sum_v phi(v) to give m<=11/12 sum_v phi(v)-n/3, hence m<=((11ell-15)/12)n in a P_ell-free system. The likely local form is t_up(v)<=3phi(v)/2, obtained by pairing linearly many nearby path-contact slots and forbidding simultaneous clean occupancy. The exact splice remains unproved; naive consecutive single-blocker pairing is known false.

## Body


Astra's interrupted Work transcript states:
(1) two clean contacts in certain nearby path positions would create a path too long for an ascending edge's entrance;
(2) there are linearly many disjoint pairs of such positions, producing a deficit linear in edge rank;
(3) the resulting count is
    A <= (3/4) sum_v phi(v),
where A is the number of ascending nonspecial edges;
(4) combined with certified accounting this gives coefficient 11/12 in place of 1.

The global algebra is exact. Put
  S=sum_v phi(v).
Certified ascending accounting 419519f0efa5 gives
  3m-A <= 2S-n.
Thus any proof of
  A <= (3/4)S                                           (A)
immediately gives
  3m <= (11/4)S-n,
hence
  m <= (11/12)S - n/3.                                (B)
For a P_ell-free system S<=(ell-1)n, so
  m <= ((11ell-15)/12)n.                              (C)
This has leading coefficient 11/12 instead of 1.

The most natural local formulation producing (A) is the following terminal-incidence packing statement. Let
  t_up(v)=#{ascending nonspecial edges e containing v as a terminal}.
Since every ascending edge has exactly two terminal incidences,
  2A=sum_v t_up(v).
Therefore the pointwise estimate
  t_up(v) <= (3/2)phi(v)                              (D)
(with floors or a nonpositive additive correction allowed)
would imply (A).

Why the coefficient 3/2 is exactly suggested by Astra's wording:
A maximum p=phi(v) endpoint path has about 2p available contact slots for terminal blockers. If one can choose about p/2 pairwise-disjoint pairs of nearby slots such that both members of a pair cannot simultaneously be occupied by the relevant clean contacts, then one loses one slot per pair:
  2p - p/2 = 3p/2.
Summing this terminal deficit yields A<=3S/4.

Existing LINP structure makes this plausible:
- 0e550ff0eadd gives the baseline terminal capacity about 2p.
- 220a14637b5f / a570b0ad0001 localize low-rank ascending terminal contacts into central/tail windows.
- Type-A records a57057ab0001, 8e108e74fa82, 4c0a0105c825 show exact near-saturation of path-contact slots, full-rank special edges, and rank jumps of at least two across Type-A ascending arcs.
- a9ce4e3cd5da and fa278a529f70 show linearly many genuine private-contact rotations in saturated Type-A states.
These are consistent with a linearly growing forbidden-pair deficit.

CRITICAL FENCE.
The naive statement "two consecutive private single blockers force an extension" is false: 47c17993cf60 is refuted by certified example 2712f65b5d5e. Hence Astra's word "clean" must be essential. A valid proof cannot simply pair consecutive single-blocker locations. It must use additional structure such as:
- both contacts being clean relative to an ascending entrance rail;
- the unique entrance label and forbidden-terminal condition;
- Type-A full-rank special incidences / rank jump;
- or a two-rail splice in which inherited path intersections are explicitly controlled.

Likely proof obligation:
Find, for each terminal vertex v and an appropriate maximum p-path P ending at v, a family of floor(p/2)-O(1) disjoint two-slot windows such that if both slots carry ascending-terminal clean contacts of the designated kind, an explicit splice creates a path of length >phi(entrance) or gives a second longest entrance to a nonspecial edge. Then charge all remaining ascending terminal incidences injectively to the unpaired slots plus at most O(1) exceptional slots.

Even a version
  t_up(v) <= (3/2)phi(v)+O(1)
would yield
  A <= (3/4)S+O(n)
and therefore the same leading coefficient 11/12 with an additive O(n) term. The screenshot's exact A<=3S/4 suggests Astra believed the endpoint corrections could be made nonpositive or exactly absorbed.
