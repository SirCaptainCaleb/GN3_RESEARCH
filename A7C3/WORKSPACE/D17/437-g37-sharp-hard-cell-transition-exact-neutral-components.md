# Every neutral component in the sharp hard cell has zero transition weight

**Workspace:** D17
**State:** established
**Key:** `g37-sharp-hard-cell-transition-exact-neutral-components`

**Summary:** In the sharp hard cell `tau(F)=3`, `tau(J)=1`, `w(C_*)=2`, every delta-zero symmetric-difference component has transition weight exactly zero. D17.416 gives `w(D)<=0` for each neutral component, while D17.434 gives total neutral weight `W_0=0`; therefore no neutral component can be transition-negative. In the v-rooted cell of D17.435-D17.436 this yields an exact placement dichotomy. If `C_*` carries `2F/0J` crossing incidences, then the unique old F transition off `C_*` is the other X-mated source gate and the unique J transition is also off `C_*`; they must lie on the same neutral component, whose transition ledger is exactly `1F/1J`, and every other neutral component is transition-free. If `C_*` carries `3F/1J`, then all transition incidences already lie on `C_*` and every neutral component is transition-free. Thus neutral normalization is not merely non-increasing in the sharp cell: it is transition-exact component by component, and in the `2F/0J` v-rooted residue the missing source gate is tied to one unique transition-bearing neutral component rather than disappearing into anonymous off-corridor ancestry.

## 1. Sharp hard-cell input

Retain the sharp cell

`tau(F)=3`, `tau(J)=1`, `w(C_*)=2`,

with `C_*` the unique F-heavy alternating component of the symmetric difference between the selected matchings of `F` and `J`.

Let the remaining connected symmetric-difference components be `D`. By the dual-rigid normalization used in D17.416, each such component has

`delta(D)=0`, `w(D)<=0`.                                  (NE.1)

Write

`W_0=sum_D w(D)`.

D17.434 computes from the global transition gap that

`W_0=tau(F)-tau(J)-w(C_*)=2-2=0`.                         (NE.2)

## 2. Every neutral component has weight zero

By (NE.1), every summand in `W_0` is nonpositive. By (NE.2), their sum is zero. Therefore

`w(D)=0` for every delta-zero component D.                 (NE.3)

So in the sharp cell neutral normalization preserves the transition ledger component by component. There is no hidden negatively weighted neutral component compensated elsewhere.

This strengthens the generic inequality from D17.416 only in the sharp numerical cell.

## 3. Consequence in the v-rooted 2F/0J branch

Now assume the v-rooted residual geometry of D17.435 and the first transition-placement case of D17.436:

`C_*` contains exactly `2` F-transitions and `0` J-transitions. (NE.4)

Globally F has exactly three transitions and J exactly one. Hence outside `C_*` there remain exactly

- one F-transition;
- one J-transition.                                       (NE.5)

By D17.435 the three F-transitions are precisely

1. the unique v-B transition;
2. the left X-mated source gate of the three-spoke block;
3. the right X-mated source gate of the three-spoke block.

D17.436 shows that on `C_*` one has the v-transition plus one forward X-mated source gate. Therefore the unique off-augmenter F-transition in (NE.5) is the **other X-mated source gate**.

Let `D_s` be the neutral symmetric-difference component containing that off-augmenter source gate. Since this F-edge crosses `X|B`, its contribution to `w(D_s)` is `+1`. By (NE.3), `w(D_s)=0`, so `D_s` must contain at least one J-transition.

But there is only one J-transition globally, and none lies on `C_*` by (NE.4). Therefore that unique J-transition lies on `D_s`.

Since there are no other transition incidences available outside `C_*`, the transition ledger of `D_s` is exactly

`1 F-transition - 1 J-transition = 0`.                    (NE.6)

Every other neutral component contains no transition at all.

Thus in the `2F/0J` v-rooted cell, the source gate omitted from the augmenter is not free-floating ancestry. It belongs to one unique transition-bearing zero-weight neutral component together with the unique J-transition.

## 4. Consequence in the v-rooted 3F/1J branch

Assume instead the second D17.436 case:

`C_*` contains exactly `3` F-transitions and `1` J-transition. (NE.7)

These are all transition incidences present globally. Hence every selected F-edge and J-edge on every neutral component is same-side with respect to `X|B`.

Therefore every neutral component is literally transition-free:

`#F-cross(D)=#J-cross(D)=0`.                               (NE.8)

This is stronger than merely knowing `w(D)=0`.

## 5. Exact residual ledger

The v-rooted hard cell therefore has only two transition-placement patterns:

1. **AUGMENTER-PLUS-NEUTRAL SOURCE PAIR:** `C_*` contains the v-transition and one forward X-mated source gate, with no J-transition. The opposite X-mated source gate and the unique J-transition lie together on one zero-weight neutral component; every other neutral component is transition-free.
2. **ALL-TRANSITIONS-ON-AUGMENTER:** `C_*` contains v, both X-mated source gates, and the unique J-transition. Every neutral component is transition-free.

In either case, every transition-bearing object is now explicitly located. There is no residual transition weight hidden in an unnamed neutral component.

## 6. Consequence for ancestry transport

D17.416 may normalize neutral components to F without increasing transition count. In the sharp hard cell, (NE.3) shows this normalization changes **no** transition count on any component. In the `2F/0J` residue, doing so flips the unique transition-bearing neutral component from its J-state to its F-state while preserving one-for-one crossing count and installing the omitted X-mated source gate as its F crossing.

Therefore any attempt to reflect the first-loss zipper while preserving the sharp-cell ancestry must account for both X-mated source gates:

- one occurs forward on `C_*` by D17.436;
- the other either also lies on `C_*`, or lies on the unique zero-weight transition-bearing neutral component paired with the unique J crossing.

This section does not yet prove a zipper absorber or a physical splice. It removes transition ambiguity from the neutral components and makes the second source gate durable ledger data rather than ambient provenance.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
