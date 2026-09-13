# The v-rooted first-loss cell has a canonical terminal X-mated source boundary

**Workspace:** D17
**State:** established
**Key:** `g37-v-rooted-terminal-source-boundary`

**Summary:** In the v-rooted first-loss residue of D17.434-D17.437, the first-loss transition at `v` cannot be the last old F-transition on the unique augmenter. D17.436 forces at least one X-mated source gate strictly after it. Hence the last old F-transition `e_k` on `C_*` is necessarily a source-spoke-to-B gate. By the two-ended boundary theorem used in D17.420, the canonical right boundary defect matching at `e_k` has the same matching cardinality as `J`, transition count at most two, and retains the historical source trimer. D17.435 further shows that this terminal source gate is one endpoint gate of the ordered three-spoke source block and is X-mated to its adjacent `X-X` edge. Thus the sole v-rooted first-loss cell does not require physically transporting the v-rooted defect through every intermediate prefix in order to recover source geometry: it already carries a canonical low-transition source boundary at the opposite end of the same augmenter. The G36 source-oriented wall consumer may therefore be launched from this terminal source boundary, subject to its usual physical-realization/blocker alternatives.

## 1. Input

Assume the V-ROOTED FIRST LOSS branch of D17.434. Thus the sharp hard cell satisfies

`tau(F)=3`, `tau(J)=1`, `w(C_*)=2`,

and the canonical first numerical loss occurs at the first-positive zipper pivot `r`, whose installed F-transition is the unique old transition incident with the non-spoke vertex `v`.

D17.435 identifies the other two old F transitions as the opposite-polarity X-mated source gates at the ends of the ordered three-spoke source block

`B_L - I_X - B_R`, `I_X={s_1,s_2,s_3}`.

D17.436 proves that at least one of those source gates lies strictly after the v-transition in the zipper order on `C_*`.

## 2. The last old F-transition on the augmenter is source-bearing

Let

`k=max{i : chi(e_i)=1}`

be the index of the last old F transition on `C_*`, as in the two-ended boundary construction underlying D17.420.

The v-transition occurs at index `r`. By D17.436 there exists a source-gate F-transition at some index `s>r`. Therefore

`k>=s>r`.                                                  (TB.1)

There is only one old F transition incident with `v`, namely `e_r`, because `d_F(v)=1`. Hence `e_k` cannot be v-bearing. Every other old F transition in the v-rooted cell is one of the two source gates from D17.435. Consequently

`e_k` is a source-spoke-to-B transition.                   (TB.2)

Write its source endpoint as `t` and its B endpoint as `h`.

## 3. The right boundary defect is low-transition and source-anchored

The two-ended defect theorem used in D17.420 associates to the last F-transition `e_k` the canonical right boundary defect matching

`R := M_J - {f_{k-1},...,f_{m-1}} + {e_k,...,e_m}`

in the appropriate indexed orientation. It has the same matching cardinality as `J` and satisfies

`tau(R)<=2`.                                               (TB.3)

Because `e_k=t-h` is source-bearing, this boundary state retains the graph-intrinsic historical source trimer

`(A,t,C)` tight.                                           (TB.4)

Thus the v-rooted first-loss cell carries a canonical low-transition source boundary on the **right end of the same unique augmenter**, even though its numerical-cliff transition at `r` is not source-bearing.

## 4. The terminal source gate is X-mated

D17.435 shows that both source gates of the v-rooted cell occur at the endpoints of the three-spoke source block and each has an old same-side X-X mate.

Therefore the terminal source gate `e_k=t-h` has a selected old F mate `t-x` or `x-t` with `x` the neighboring source spoke in the literal old order of `I_X`. The two selected incidences form the corresponding old tight source-block turn.

Hence the canonical terminal boundary retains simultaneously:

- the source gate `t-h`;
- the source trimer `(A,t,C)`;
- the old adjacent X-X mate at `t`;
- the complete source-block order from D17.435; and
- the right-boundary low-transition defect ledger `tau<=2`.

## 5. Reorientation from the terminal source boundary

D17.425 is expressly formulated for a canonical low-transition boundary whose old F-transition is source-bearing. It orients defect transport from that boundary so that the source spoke itself is the moving unmatched copy:

- if the selected gate is `t->h`, use the OUT-prefix orientation based at that boundary;
- if the selected gate is `h->t`, use the exact reversal-dual IN-suffix orientation.

The present theorem supplies exactly such a boundary in the v-rooted residue, namely `e_k`.

Therefore one need **not** prove that every physical blocker beginning at the v-rooted first-loss pivot survives continuously until the forward source gate. Instead, the same unique augmenter has an independently certified terminal low-transition source boundary from which the existing G36 source-oriented transport/wall machinery can be launched.

This is an important logical distinction: D17.416 guarantees forward support contact but not a chain of physically successful prefixes. The terminal-boundary argument avoids assuming that stronger statement.

## 6. Consequence for the G37 ancestry split

The two ancestry classes now both expose source-rooted low-transition geometry at the exact hard-cell level:

1. **SINGLETON-SPOKE:** D17.433 roots the numerical first-loss rectangle itself at the DOUBLE-B source spoke.
2. **V-ROOTED X-MATED:** the first-loss rectangle is rooted at `v`, but D17.438 supplies a canonical terminal X-mated source boundary later on the same augmenter, with transition count at most two and full source ancestry.

Thus the X-mated-versus-singleton split no longer represents “source-rooted versus source-anonymous.” It represents two different placements of the source root relative to the numerical cliff: at the cliff in the singleton branch, or at a canonical terminal boundary beyond the cliff in the v-rooted branch.

This section does not claim that the terminal boundary is automatically a literal tight three-forest; its physical failures remain governed by the existing forward-blocker and persistent-wall machinery. Nor does it itself absorb the first-loss K2,2. Its gain is to reconnect the only non-source-rooted numerical frontier to an exact source-boundary launch point without an unjustified intermediate-realizability assumption.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
