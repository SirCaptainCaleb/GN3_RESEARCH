# The v-rooted first-loss cell has a two-ended X-mated three-spoke source block

**Workspace:** D17
**State:** provisional; audit reopened for repair-first reconstruction
**Key:** `g37-v-rooted-cell-two-ended-x-mated-source-block`

## Repair status

The original audit attempt found a real provenance gap: the displayed proof invokes a D17.418 tau-three block normal form, including

`b_X=2`, `b_B=3`, `d_F(v)=1`, `e_XX=2`,

together with the decomposition into one endpoint X-block containing `v` and one internal source-only X-block. No `418-*` durable D17 source is presently available, and nearby D17.419 imports older labels `SV101138` and `SV109219` whose proofs are likewise not reconstructibly present.

That absence is proof debt, not a mathematical counterexample. The earlier `[FAIL]` verdict was therefore reopened. The current audit task is to reconstruct the needed block normal form directly from the stated sharp-cell hypotheses and surviving nearby machinery, or else derive the strongest exact adjusted theorem that does not require the missing historical source. Until that repair is completed, every conclusion below remains provisional.

## Historical claim

**Summary:** In the sole potentially source-anonymous first-loss cell isolated by D17.434, the installed frontier transition is incident with the unique non-spoke `v`. The tau-three block normal form D17.418 then sharpens drastically. Since `v` is the physical outer endpoint of the endpoint X-block `E_X` and has selected degree one, a transition incident with `v` forces `E_X={v}`. Hence the other X-block `I_X` contains all three source spokes and no other vertices. It is a literal directed tight three-spoke path bracketed by B on both sides. Its two boundary transitions are distinct source gates of opposite path polarity, and each endpoint source spoke has exactly one same-side `X-X` mate inside `I_X`. Thus the residual X-MATED ancestry is not a single arbitrary source gate: it is a two-ended, ordered, opposite-polarity pair of X-mated source gates carrying the complete old source-spoke order. The only possible v-rooted first-loss packet therefore retains substantially more orientation data than an anonymous K2,2 plus one mate.

## 1. Input

Assume the V-ROOTED FIRST LOSS branch of D17.434. Thus the sharp hard cell has

`tau(F)=3`, `tau(J)=1`, `w(C_*)=2`,

and the installed transition at the first numerical loss is an old F edge incident with the unique non-spoke vertex `v` of

`X={v,p,q,r}`.

By the sharp source degree law retained in D17.418,

`b_X=2`, `b_B=3`, `d_F(v)=1`, `e_XX=2`.

D17.418 decomposes the old X-support into exactly two maximal X-blocks:

- one endpoint block `E_X` containing `v` as its physical outer rail endpoint;
- one internal block `I_X`, bracketed by B-blocks and containing only source spokes.

## 2. A v-transition forces the endpoint X-block to be the singleton v

In the present branch the first-loss installed old F edge is incident with `v` and crosses `X|B`. Since `d_F(v)=1`, this crossing edge is the only selected F edge incident with `v`.

But `v` is the physical outer endpoint of the tight X-subpath `E_X`. If `E_X` contained any second X-vertex, the first selected edge from `v` along that X-subpath would be an `X-X` edge, contradicting the fact that the unique selected edge at `v` is the displayed X|B transition.

Therefore

`E_X={v}`.                                                 (VB.1)

The two maximal X-blocks partition all four vertices of X. Hence

`I_X={p,q,r}`.                                             (VB.2)

So the internal X-block is not merely source-only: it contains every source spoke.

## 3. The internal source block is one directed tight three-spoke path

D17.418 shows that `I_X` is a literal tight path inside an old F rail and is bracketed by B-blocks. By (VB.2), after naming the source spokes in their literal old F order as

`s_1,s_2,s_3`,

the local selected old F segment has one of the two reversal-dual orientations

`B_L -> s_1 -> s_2 -> s_3 -> B_R`,                        (VB.3)

or its complete reversal.

Fix (VB.3) for notation. The two old source gates are then

`B_L -> s_1`,                                              (VB.4)
` s_3 -> B_R`.                                             (VB.5)

They have opposite path polarity: the left gate enters the source block, while the right gate exits it.

The two selected same-side incidences inside the block are exactly

`s_1 -> s_2`, `s_2 -> s_3`.                               (VB.6)

Thus the endpoint spokes `s_1,s_3` are distinct B-active source spokes, each with exactly one B-transition and one old `X-X` mate. In the terminology of D17.419, **both** boundary source gates are X-mated:

- `B_L -> s_1` is mated to `s_1 -> s_2`;
- `s_3 -> B_R` is mated to `s_2 -> s_3`.

The middle spoke `s_2` has both selected incidences inside X and no B-transition.

## 4. The residual ancestry packet is two-ended, not one-ended

D17.419 was stated as an alternative guaranteeing some X-mated source transition on `C_*` unless the singleton-spoke two-switch atom occurs. After D17.434 has isolated the only potentially source-anonymous first-loss cell, Section 3 upgrades that information:

- the old source support has a canonical three-spoke order `s_1,s_2,s_3`;
- there are exactly two source-block gates, at the two endpoints of that order;
- the gates have opposite directed polarity;
- both are X-mated by the two consecutive old `X-X` edges of the source block;
- the third old F transition is the unique `v`-B edge at the singleton block `{v}`.

Thus every old F transition in the v-rooted cell is now typed:

1. one unique non-source transition at `v`;
2. one IN-oriented X-mated source gate at one end of `I_X`;
3. one OUT-oriented X-mated source gate at the other end.

No fourth old transition exists.

## 5. Specialized contracted block shapes

The two generic contracted block shapes of D17.418 specialize, under `E_X={v}`, to exactly:

1. **same-rail shape:** one rail contains `B-I_X-B-{v}` up to complete reversal, and the other rail is an isolated B-block;
2. **split-rail shape:** one rail is `B-I_X-B`, while the other is `B-{v}` up to reversal.

In either shape the source-only block itself retains the same ordered two-gate geometry (VB.3)-(VB.6). The distinction records only whether the singleton v-block lies on the same old F rail as the source block or on the other rail.

## 6. Consequence for the reflected zipper problem

The sole v-rooted X-MATED cell from D17.434 cannot be modeled faithfully by attaching one unlabeled source mate to an otherwise anonymous first-loss rectangle. Its retained ancestry contains an ordered pair of source gates with opposite polarity and a two-edge source-only path joining their source endpoints.

Any proposed reflected first-loss realization must therefore preserve simultaneously:

- the physical singleton `v` carrying the numerical-cliff transition;
- the literal old source order `s_1,s_2,s_3`;
- the IN/OUT polarity distinction between the two source gates;
- both same-side mates `s_1s_2` and `s_2s_3`;
- the historical source trimers `(A,s_i,C)` retained for the source spokes; and
- whether the old contracted support is same-rail or split-rail.

This does not yet prove that the two-ended source packet fixes the seam-safe pairing at the K2,2 frontier. It does show that the remaining orientation question is strictly narrower than the one-source-mate formulation suggested by D17.419 alone: a reflection must respect a complete ordered three-spoke source block with opposite-polarity gates.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
