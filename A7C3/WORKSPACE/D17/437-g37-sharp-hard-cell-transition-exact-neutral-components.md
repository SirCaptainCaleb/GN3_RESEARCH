# D17.437 — Sharp hard-cell transition ledger: exact neutral weights with a common-edge branch

**Workspace:** D17  
**State:** provisional workspace mathematics; this qualification is not an audit verdict  
**Key:** `g37-sharp-hard-cell-transition-exact-neutral-components`

**Summary.** In the sharp hard cell `tau(F)=3`, `tau(J)=1`, `w(C_*)=2`, every neutral symmetric-difference component has transition weight exactly zero. That componentwise identity survives unchanged. The stronger previous placement statement in the `2F/0J` v-rooted residue needs an extra branch: the unique F-transition off `C_*` and the unique J-transition off `C_*` may be the same COMMON selected edge in `F intersect J`, which lies outside the symmetric difference. Only when the remaining F-transition is noncommon is it forced onto a neutral component together with the unique J-transition. The sharp counts alone therefore do not exclude the COMMON branch.

This file records the qualification exposed during source-complement integration. The originating Slack finding was not being given an audit verdict by this edit. See the canonical provisional development [`../source-complement-zipper.md`](../source-complement-zipper.md), especially its section on common selected transitions, for the explicit matching-level fixture and current downstream scope.

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

Here `w(D)` is the F-crossing count minus the J-crossing count contributed by the selected edges actually lying on the symmetric-difference component `D`. A selected edge common to `F` and `J` is not a component edge of `F triangle J` and must be tracked separately when locating individual transitions.

## 2. Every neutral component has weight zero

By (NE.1), every summand in `W_0` is nonpositive. By (NE.2), their sum is zero. Therefore

`w(D)=0` for every delta-zero component D.                 (NE.3)

So in the sharp cell neutral normalization preserves the transition ledger component by component. There is no hidden negatively weighted neutral component compensated elsewhere.

This strengthens the generic inequality from D17.416 only in the sharp numerical cell. It does **not** by itself say where a transition carried by a common selected edge lies, because such an edge is outside the symmetric-difference components.

## 3. The v-rooted 2F/0J branch

Assume the v-rooted residual geometry of D17.435 and the first transition-placement case of D17.436:

`C_*` contains exactly `2` F-transitions and `0` J-transitions. (NE.4)

Globally F has exactly three transitions and J exactly one. Hence outside `C_*` there remain exactly

- one F-transition;
- one J-transition.                                       (NE.5)

By D17.435 the three F-transitions are the unique v-B transition and the two X-mated source gates of the three-spoke block. D17.436 places the v-transition plus one forward X-mated source gate on `C_*`. Hence the unique remaining F-transition is the other X-mated source gate.

At this point there are two logically distinct possibilities.

### 3a. COMMON GATE

The remaining F-transition and the unique J-transition may be the **same selected edge**, lying in `F intersect J`. Such an edge is outside `F triangle J`, so there is no neutral symmetric-difference component containing it. In this branch every neutral component is transition-free even though one F-transition and one J-transition remain outside `C_*` globally.

### 3b. NEUTRAL GATE

If the remaining F-transition is **not** common, then it lies on a neutral symmetric-difference component; call it `D_s`. Its F-crossing contribution is `+1`. By (NE.3), `w(D_s)=0`, so `D_s` must also carry a J-transition. The unique global J-transition is off `C_*` by (NE.4), hence it is that J-transition. There are no further transition incidences outside `C_*`, so the ledger of `D_s` is exactly

`1 F-transition - 1 J-transition = 0`.                    (NE.6)

Every other neutral component is transition-free.

Therefore the safe `2F/0J` conclusion is a dichotomy, not compulsory neutral placement:

- **COMMON GATE:** the remaining source gate and unique J-transition are the same common selected edge; all neutral components are transition-free.
- **NEUTRAL GATE:** the remaining source gate and unique J-transition lie together on one zero-weight neutral component; every other neutral component is transition-free.

Excluding the COMMON GATE branch requires an additional argument from the actual canonical word or another hypothesis. It is not a consequence of the sharp transition counts alone.

## 4. The v-rooted 3F/1J branch

Assume instead the second D17.436 case:

`C_*` contains exactly `3` F-transitions and `1` J-transition. (NE.7)

These exhaust the global transition incidences. Hence every selected F-edge and J-edge on every neutral component is same-side with respect to `X|B`, and every neutral component is literally transition-free:

`#F-cross(D)=#J-cross(D)=0`.                               (NE.8)

This part of the previous placement statement needs no common-edge correction.

## 5. Exact residual ledger

The v-rooted hard cell therefore has three transition-placement patterns once common selected edges are kept visible:

1. **AUGMENTER + COMMON SOURCE GATE:** `C_*` contains the v-transition and one forward X-mated source gate, with no J-transition; the opposite X-mated source gate is also the sole J-transition as one common selected edge outside the symmetric difference; every neutral component is transition-free.
2. **AUGMENTER + NEUTRAL SOURCE GATE:** `C_*` contains the v-transition and one forward X-mated source gate, with no J-transition; the opposite X-mated source gate and the unique J-transition lie together on one zero-weight neutral component; every other neutral component is transition-free.
3. **ALL TRANSITIONS ON AUGMENTER:** `C_*` contains v, both X-mated source gates, and the unique J-transition; every neutral component is transition-free.

Thus the componentwise zero-weight conclusion is exact, but a common selected edge is a third ledger location that must not be erased by symmetric-difference bookkeeping.

## 6. Scope and downstream use

D17.416 may normalize neutral components to F without increasing transition count. Equation (NE.3) shows that such normalization changes no transition weight on any neutral component in the sharp cell. In the NEUTRAL GATE branch it installs the omitted X-mated source gate on the transition-bearing neutral component while preserving one-for-one crossing count. In the COMMON GATE branch there is no transition-bearing neutral component to normalize: the omitted gate is already common.

D17.436's forward source-gate conclusion is based on the augmenter counts and is not invalidated merely by this common-edge possibility. What fails without an additional argument is the stronger inference that the other source gate must live on a unique transition-bearing neutral component.

The explicit matching-level fixture in [`../source-complement-zipper.md`](../source-complement-zipper.md) shows that the sharp counts and source-block data alone permit the COMMON GATE pattern. That fixture is **not** asserted to realize every canonical endpoint-cut/gate hypothesis, a smallest counterexample, or a global counterexample. If the full canonical construction excludes the common case, that exclusion still needs to be proved from the actual word.

This section does not prove a zipper absorber, a physical splice, Hamiltonicity of a source complement, or a valid global descent. It preserves the exact numerical ledger while fencing the unresolved physical and canonical-word requirements.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
