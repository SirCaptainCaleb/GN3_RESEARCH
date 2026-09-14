# Every v-rooted first-loss frontier has a forward X-mated source gate on the same augmenter

**Workspace:** D17
**State:** provisional; audit reopened for repair-first reconstruction
**Key:** `g37-v-rooted-frontier-forward-x-mated-source-gate`

## Repair status

The numerical counting inside this argument is valid under the displayed sharp-cell totals: if `w(C_*)=2`, `tau(F)=3`, and `tau(J)=1`, then the transition-bearing incidences on `C_*` can only satisfy

`(n_F,n_J)=(2,0)` or `(3,1)`.

The unresolved point is the source interpretation of the non-v F-transitions. The original proof inherits from D17.435 that the three old F transitions are exactly the unique `v-B` transition plus the two endpoint X-mated source gates of an ordered three-spoke block. Since D17.435 has been reopened for repair, D17.436 is likewise reopened rather than failed.

The repair target is to derive the source-bearing and X-mated conclusion directly from the sharp-cell / first-positive-prefix hypotheses, or to combine a repaired D17.435 normal form with the valid counting below. Until then the source-gate conclusion remains provisional while the `(2F,0J)/(3F,1J)` arithmetic is retained as established local bookkeeping.

## Historical claim

**Summary:** In the v-rooted residual cell of D17.434-D17.435, the unique augmenter `C_*` necessarily contains a source transition strictly after the first-loss v-transition. Indeed `w(C_*)=2`, while globally F has three transition edges and J has one, so the transition-bearing incidences on `C_*` are either `2F/0J` or `3F/1J`. In the first case the v-transition must be the first F-transition, so the other F-transition on `C_*` is a later source gate. In the second case both source gates and the unique J-transition lie on `C_*`; both source gates cannot precede the first-positive v-pivot because their two `+1` contributions can be offset by at most one J `-1`, which would force a positive prefix before v. Hence at least one source gate lies strictly after v. D17.435 shows both source gates are X-mated endpoints of the ordered three-spoke source block. Therefore the sole v-rooted first-loss cell always has a **forward X-mated source gate on the same alternating component**. If one source gate does occur before v in the `3F/1J` case, the unique J-transition must neutralize it before the v-pivot; this is the only possible pre-v source history.

## 1. Input

Assume the V-ROOTED FIRST LOSS branch of D17.434 and the sharpened source-block normal form of D17.435. Thus:

- `tau(F)=3`, `tau(J)=1`, `w(C_*)=2`;
- the first positive prefix index `r` is the first numerical loss;
- the installed F-transition `e_r` is the unique old transition incident with `v`;
- the other two old F transitions are the two opposite-polarity X-mated source gates at the ends of the three-spoke block `I_X`.

Let

`n_F = number of F-selected X|B edges on C_*`,
`n_J = number of J-selected X|B edges on C_*`.

Then

`n_F-n_J=w(C_*)=2`.                                       (FG.1)

Globally F has exactly three transitions and J exactly one, so

`0<=n_F<=3`, `0<=n_J<=1`.                                 (FG.2)

Combining (FG.1)-(FG.2) leaves only

`(n_F,n_J)=(2,0)` or `(3,1)`.                              (FG.3)

## 2. The 2F/0J case has one source gate strictly after v

Assume `(n_F,n_J)=(2,0)`. One of the two F-transitions on `C_*` is the v-transition `e_r`. The other is therefore one of the two source gates from D17.435.

Because there is no J-transition on `C_*`, the prefix sum `S_q` is monotone nondecreasing and increases by one at each transition-bearing F-edge. Since `r` is the first positive prefix, no F-transition can occur before `e_r`. Hence `e_r` is the first transition-bearing F-edge on `C_*`.

Therefore the second F-transition, necessarily a source gate, occurs strictly after `r`. The other source gate is the unique old F transition outside `C_*`.

So in the 2F/0J case:

`v-transition < forward source gate` along the zipper order.  (FG.4)

By D17.435 that forward source gate is X-mated.

## 3. The 3F/1J case also has a source gate strictly after v

Assume `(n_F,n_J)=(3,1)`. Then all three old F transitions lie on `C_*`: the v-transition and both source gates. The unique J-transition also lies on `C_*`.

Suppose for contradiction that both source-gate F-transitions occur before the v-transition `e_r`. By definition of `r`, every proper prefix before `r` has

`S_q<=0`.                                                  (FG.5)

But the two source F-transitions contribute total `+2` to `S`, while the entire augmenter contains only one J-transition, contributing at most `-1`. After both source transitions have appeared and before `r`, the cumulative contribution is therefore at least

`2-1=1`,                                                   (FG.6)

contradicting (FG.5).

Hence at least one of the two source gates occurs strictly after `r`. Again D17.435 makes it X-mated.

Thus in the 3F/1J case as well, `C_*` contains a forward X-mated source gate after the v-rooted numerical cliff.

## 4. Exact form of any source history before v

The same counting gives a useful refinement. At most one source F-transition can occur before `r`, since two would contradict (FG.5). If one does occur before `r`, then the unique J-transition must also occur no later than the moment that source `+1` would make the prefix positive.

Equivalently, the only possible pre-v source history in the 3F/1J case is a numerically neutralized one:

- either the J-transition occurs first, taking `S` from `0` to `-1`, and the source F-transition later returns it to `0`; or
- the source F-transition and J-transition occur at the same zipper index, contributing net zero there.

A source F-transition cannot occur first by itself, because that would make `S=1` before `r` and contradict first-positive minimality.

After such a neutralized prelude, the v-transition at `r` gives the first positive value `S_r=1`. The other source gate still lies strictly forward of `r`.

## 5. Consequence for forward blocker transport

D17.416 normalizes delta-zero components to F and shows that any surviving physical blocker at a prefix must reach strictly into the still-unflipped suffix of `C_*`. D17.424 further shows that along successful pivots only the fixed far-boundary reverse star can persist.

The present theorem identifies a mandatory source target in that suffix: in the sole v-rooted ancestry cell, there is always an X-mated source gate strictly after the first-loss pivot on the same alternating component.

Thus source ancestry is not merely known to exist somewhere in the old cover. Relative to the canonical first-loss orientation it has a forward representative on the very suffix to which persistent blockers are forced to point. Any attempted reflected zipper model must preserve this forward source gate together with its same-side mate and the complete two-ended source-block order of D17.435.

This does not yet prove that transport to the forward gate is physically successful or that its wall/P4 packet absorbs the zipper. It removes the possibility that the v-rooted numerical cliff is followed only by source-free zipper data.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
