# The sharp hard cell loses descent at its first positive pivot, and only X-mated v-rooting can remain source-anonymous

**Workspace:** D17
**State:** established
**Key:** `g37-hard-cell-first-loss-root-dichotomy`

**Summary:** In the entire sharp G35 hard cell `tau(F)=3`, `tau(J)=1`, `w(C_*)=2`, the total transition weight of all delta-zero symmetric-difference components is exactly zero. Hence the D17.421 normalized closure count is `T_q=1+S_q+(S_q mod 2)`. Before the first positive prefix, matching nonnegativity gives `S_q in {-1,0}`, so every defined normalized closure has exactly one transition; at the first positive pivot `r`, necessarily `S_r=1` and `T_r=3=tau(F)`. Thus the canonical first numerical loss is exactly `r` (apart from the unique loop interruption), not merely some later zipper rectangle. Its old same-side diagonal has one `X-X` member incident with the physical X-endpoint of the installed F-transition. If that X-endpoint is a source spoke, the frontier is canonically source-rooted. D17.433 shows the SINGLETON-SPOKE ancestry class always has this form. Therefore the only hard-cell ancestry regime in which the first-loss rectangle itself is not source-rooted is the X-MATED SOURCE GATE class with the installed transition incident with the unique non-spoke `v`. Since `d_F(v)=1`, every other old F transition is source-bearing. The remaining reflected-pairing problem can consequently be localized to this v-rooted X-mated cell.

## 1. Sharp hard-cell input

Retain the sharp G35 cell

`tau(F)=3`, `tau(J)=1`, `w(C_*)=2`,

with `C_*` the unique F-heavy alternating component and with the F-normalized prefix closures of D17.421. Write

`W_0=sum_D w(D)`

for the total transition weight of the delta-zero components, and

`T_q=1+S_q+W_0+gamma_q`,

where

`gamma_q=(S_q mod 2) xor (w(C_*) mod 2)`.

## 2. All neutral transition weight vanishes

Transition differences add over the symmetric-difference components. The unique F-heavy component contributes `w(C_*)=2`, while the delta-zero components contribute `W_0`. Therefore

`tau(F)-tau(J)=w(C_*)+W_0`.

The left side is `3-1=2`, so

`W_0=0`.                                                   (RD.1)

Because `w(C_*)` is even,

`gamma_q=S_q mod 2`.                                      (RD.2)

Hence every defined normalized closure satisfies

`T_q=1+S_q+(S_q mod 2)`.                                  (RD.3)

This conclusion uses only the sharp-cell numerical identities and the exact normalization formula of D17.421.

## 3. Every pre-first-positive normalized closure has exactly one transition

Let `r` be the least positive prefix index with `S_r=1`, the first-positive pivot already used in the G35 corridor analysis. For `q<r`, first-positive minimality gives `S_q<=0`.

The normalized prefix matching has transition count

`tau(hat M_q)=1+S_q+W_0=1+S_q`.

This is a nonnegative integer, so `S_q>=-1`. Thus

`S_q in {-1,0}` for every q<r.                             (RD.4)

Substituting either value into (RD.3) gives

`T_q=1` for every defined q<r.                             (RD.5)

At `r`, the one-step zipper ledger changes by at most one, so the first positive value is exactly

`S_r=1`.

Then (RD.3) gives

`T_r=3=tau(F)`.                                           (RD.6)

Consequently, if `g_r` is defined, the first numerical loss index `q^dagger` of D17.421 is exactly

`q^dagger=r`.                                             (RD.7)

If `g_r` is undefined because `a_r=b_m`, this is precisely the unique singleton-defect loop interruption already isolated in D17.421. No new exceptional branch occurs.

So the normalized closing fan has an exact numerical cliff in the sharp hard cell: every defined closure before `r` has transition count one, and the first positive pivot jumps directly to the old floor three.

## 4. The first-loss rectangle is rooted at the X-endpoint of its installed F-transition

Assume the non-loop case. By D17.421 the switch at `r` is

`{f_r,g_{r-1}} <-> {e_r,g_r}`,

with

`chi(f_r)=chi(g_{r-1})=0`,
`chi(e_r)=chi(g_r)=1`.                                    (RD.8)

Let `z` be the physical X-endpoint of the installed cross edge

`e_r=a_{r-1}->b_r`.

Exactly as in the side calculation of D17.433, the old same-side pair in (RD.8) has one `X-X` member and one `B-B` member, and the `X-X` member is incident with `z`:

- if `z=a_{r-1}`, then `g_{r-1}` is `X-X` and `f_r` is `B-B`;
- if `z=b_r`, then `f_r` is `X-X` and `g_{r-1}` is `B-B`.

Thus the first-loss rectangle always carries a canonical marked X-corner, namely the X-endpoint `z` of the old F-transition `e_r`.

## 5. Source-rooted versus v-rooted first loss

In the hard cell the X-side is

`X={v,p,q,s}`,

where `p,q,s` are the three source spokes and `v` is the unique non-spoke vertex. Therefore the marked corner `z` from Section 4 is either a source spoke or `v`.

If `z` is a source spoke, the first-loss rectangle is physically source-rooted: its unique old `X-X` diagonal member is incident with that source spoke, and the installed F-transition at the numerical cliff is itself an old source gate.

D17.433 proves that the SINGLETON-SPOKE TWO-SWITCH alternative of D17.419 always lands in this source-rooted case: `r` is exactly the first B-incidence of its unique DOUBLE-B source spoke `t`.

Hence any hard-cell first-loss rectangle that is **not** source-rooted must lie in the other D17.419 ancestry class, X-MATED SOURCE GATE, and must have

`z=v`.                                                     (RD.9)

The sharp old-source degree law gives `d_F(v)=1`. Therefore when (RD.9) holds, `e_r` is the unique selected old F edge incident with `v`; in particular every other old F transition on or off `C_*` has its X-endpoint at a source spoke.

## 6. Exact residual ancestry cell

The ancestry/reflection campaign therefore contracts to the following dichotomy at the numerical frontier:

1. **SOURCE-ROOTED FIRST LOSS.** The installed transition `e_r` is source-bearing. The first-loss `K_{2,2}` has a canonical source-marked `X-X` old diagonal member. This includes the entire SINGLETON-SPOKE ancestry class.
2. **V-ROOTED FIRST LOSS.** The installed transition `e_r` is the unique old F incidence at `v`. This can occur only in the X-MATED SOURCE GATE ancestry class. All remaining old F transitions are source-bearing, and D17.419 additionally retains on `C_*` at least one source transition whose other old F incidence is an `X-X` mate.

Thus a reflected zipper model that is meant to show the preserved ancestry fails to determine the seam-safe pairing need only be sought in case 2. Conversely, an absorber may treat case 1 as source-rooted and focus its genuinely nonlocal ancestry transport on the v-rooted X-mated cell.

This section does not yet prove that a source-rooted first-loss rectangle closes globally, nor that the X-mated mate fixes the remaining orientation in case 2. It removes the larger anonymous-hard-cell search space and identifies the sole cell where source ancestry is not already sitting on the numerical-cliff corner.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
