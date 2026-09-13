# A terminal source gate and its X-mate reduce full-H absorption to a three-path two-seam recompletion

**Workspace:** D17
**State:** established
**Key:** `g38-terminal-source-mate-three-path-two-seam-recompletion`

**Summary:** In the v-rooted hard-cell residue, let `t` be the source spoke of the canonical terminal source boundary from D17.438 and let `x` be its adjacent old `X-X` mate in the ordered three-spoke source block of D17.435. The vertices `t,x` are consecutive internal vertices of one old F rail. Deleting them splits that rail into exactly two nonempty path intervals, while the other old F rail remains a nonempty path. Hence `F-{t,x}` is a literal three-path cover of `G-{t,x}`. Independently, the retained historical source trimers `(A,t,C)` and `(A,x,C)` force a Hamilton P4 on the four-set `{A,C,t,x}` by one R3 test. Therefore any Hamilton recompletion of the three residual F paths into one path immediately gives a spanning two-cover of H, with the source four-set as the other rail. The global G38 source-gate zipper problem is thus reduced, in the sole v-rooted ancestry cell, to joining exactly three known residual paths by exactly two legal seams. This matches the combinatorial size of the live two-crossing K2,2 zipper and gives a concrete seam target; it does not assert that the K2,2 cross edges are already the two required residual seams.

## 1. Input

Retain the v-rooted sharp hard-cell residue of D17.434-D17.438. Thus

`G=H-{A,C}`

has the old exact source two-cover `F`, with three source spokes `s_1,s_2,s_3` internal on the displayed source rails and historical tight source trimers

`(A,s_i,C)` for i=1,2,3.

D17.435 gives the literal old source block, up to complete reversal,

`B_L -> s_1 -> s_2 -> s_3 -> B_R`,

and D17.438 chooses the last old F-transition on the unique augmenter as a canonical terminal source gate. Let its source endpoint be `t`. Since the only source gates of the block are its two endpoints, `t` is one of `s_1,s_3`.

Let `x=s_2` be the unique source-spoke neighbor of `t` inside the source block. Then the selected old F edge `tx` (in its actual orientation) is the X-X mate of the terminal source gate.

## 2. t and x are consecutive internal vertices on one old F rail

Every source spoke is internal in the retained old source cover F. In particular, `t` has exactly two selected F incidences:

- the terminal source gate joining `t` to a B-vertex `h`;
- the same-side mate joining `t` to `x`.

The middle spoke `x=s_2` has the two selected same-side incidences joining it to the two endpoint source spokes of the three-spoke block. Hence `t` and `x` are consecutive vertices of one old F rail, and neither is an endpoint of that rail.

The two local old path orders are therefore, according to which endpoint gate is terminal,

`... h, t, x, y, ...`                                    (TS.1)

or its complete reversal, where `y` is the third source spoke. The vertices before `t` and after `x` in this rail are both nonempty because `t,x` are internal.

## 3. Deleting the terminal source-mate pair leaves exactly three paths

Delete the physical vertices `t,x` from F.

On the old rail containing them, the consecutive internal pair in (TS.1) is removed. A path with two consecutive internal vertices deleted splits into exactly two nonempty path intervals: the prefix ending immediately before `t`, and the suffix beginning immediately after `x`.

The other old F rail is untouched. It is nonempty because F is an exact two-cover and the retained source-frame nontriviality excludes a vanishing rail.

Consequently

`F-{t,x}` is exactly a three-path cover of `G-{t,x}`.       (TS.2)

Write these three literal residual paths as

`P_1 | P_2 | P_3`.                                        (TS.3)

No abstract component-count argument is needed: these are the actual old-order path intervals plus the untouched old rail.

## 4. The deleted pair plus A,C forms a Hamilton P4

The retained source packet contains

`(A,t,C)` tight,
`(A,x,C)` tight.                                          (TS.4)

Apply R3 to the ordered triple `(t,A,x)`.

- If `(t,A,x)` is tight, then `(t,A,x,C)` is a tight Hamilton P4 on `{A,C,t,x}` using the second turn from (TS.4).
- If `(t,A,x)` is bad, R3 gives `(x,A,t)` tight, and then `(x,A,t,C)` is a tight Hamilton P4 using the first turn from (TS.4).

Thus there exists a literal tight Hamilton path

`Q_{t,x}` on `{A,C,t,x}`.                                 (TS.5)

This is the same elementary source-four-set construction used earlier in D17.398, now applied to the terminal source gate and its actual old X-mate.

## 5. Exact full-H reduction

The supports of (TS.3) and (TS.5) are disjoint and together partition V(H):

`V(Q_{t,x})={A,C,t,x}`,
`V(P_1) union V(P_2) union V(P_3)=V(H)-{A,C,t,x}`.

Therefore, if the three residual paths `P_1,P_2,P_3` can be recompleted into one tight Hamilton path `P` on their union, then

`P | Q_{t,x}`                                             (TS.6)

is a spanning two-path cover of H, contradicting the hypothetical counterexample.

So the v-rooted G38 obstruction has been reduced to:

> **Three-path two-seam recompletion problem.** Join the three literal paths `P_1,P_2,P_3` from `F-{t,x}` into one tight path using two legal joins.

Two joins are combinatorially necessary and sufficient to connect three path components without vertex overlap.

## 6. Relation to the live two-crossing zipper

The canonical first-loss packet from D17.421/D17.434 is an exact K2,2 switch replacing one diagonal by the other, with two crossing edges on its new side. The current G38 target asks for source-gate zipper absorption while retaining the fixed far wall and ancestry.

The reduction above explains what a successful two-crossing packet must accomplish globally in the v-rooted ancestry class: after spending the terminal source pair `{t,x}` on the source Hamilton P4, its two legal seam effects must connect the three explicit residual F paths into one path.

This is a precise interface target, but not yet an identification theorem. In particular this section does **not** assert that the two crossing edges of the first-loss K2,2 have endpoints on the three residual paths in the correct `2+2` component pattern, nor that both associated turns are tight. Those are exactly the remaining synchronization/seam obligations.

## 7. Scope

The gain is structural:

- the anchors A,C are fully absorbed into a fixed four-vertex source rail;
- the terminal source gate and its old X-mate are consumed with them;
- the complement is not an arbitrary forest but exactly three known old F paths;
- full-H closure now needs exactly two seam joins, matching the size of the live two-crossing zipper.

The remaining G38 work should therefore inspect the endpoint-component incidence of the first-loss K2,2 against `P_1|P_2|P_3`, rather than search for generic Hamilton P5 extension or anonymous reflection principles.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
