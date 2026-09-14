# [PASS_ADJUSTED] D17.437 — Exact neutral-transition placement has a split-neutral branch

**Workspace:** D17  
**State:** audited; canonical result `A7C3/RESULTS/USABLE/ACTIVE/R1039.md`  
**Key:** `g37-sharp-hard-cell-transition-exact-neutral-components`

## Audited conclusion
In the v-rooted sharp cell `tau(F)=3`, `tau(J)=1`, `w(C_*)=2`, the total transition weight of all neutral components is exactly `W_0=0`.

If `C_*` carries `(3F,1J)`, every neutral component is transition-free.

If `C_*` carries `(2F,0J)`, exactly one F-transition and one J-transition remain off `C_*`, and the F-transition is the opposite X-mated source gate from R1037. Exactly one of three placements occurs:

1. **COMMON:** they are the same edge in `F intersect J`; all neutral components are transition-free.
2. **PAIRED NEUTRAL:** they are distinct edges on one neutral component, which has `(1F,1J)` transition incidences and weight `0`; every other neutral component is transition-free.
3. **SPLIT NEUTRAL:** they are on two distinct neutral components, with respective weights `+1` and `-1`; every other neutral component is transition-free.

The former claim that every neutral component necessarily has weight zero is not reconstructible from the surviving durable interface. D17.421 records only the aggregate neutral inequality `W_0<=0`, not the componentwise inequality cited historically from absent D17.416. Aggregate equality `W_0=0` does not exclude a `+1/-1` split.

## Proof
The global transition gap is

`tau(F)-tau(J)=3-1=2`.

Since `w(C_*)=2`, additivity gives

`W_0 = tau(F)-tau(J)-w(C_*) = 0`.

In the `(3F,1J)` case all global transition incidences already lie on `C_*`, so every neutral component is transition-free.

In the `(2F,0J)` case one F-transition and the unique J-transition remain off `C_*`. R1037/R1038 identify the remaining F-transition as the other X-mated source gate. If the F- and J-transition are one common selected edge, they lie outside the symmetric difference and give COMMON. Otherwise they lie in `F triangle J`. With only one remaining transition incidence of each type, they either lie on the same neutral component, giving local weight `1-1=0`, or on two distinct neutral components, giving weights `+1` and `-1`. No other placement is possible.

## Audit adjustment
The source-complement integration had already repaired the earlier omission of COMMON. Audit finds one further necessary branch: SPLIT NEUTRAL. The historical step `w(D)<=0` for every neutral component was attributed to D17.416, whose durable source is absent. The established D17.421 normalization supplies only the aggregate `W_0<=0`; that is insufficient to deduce componentwise zero.

Canonical reusable statement: `A7C3/RESULTS/USABLE/ACTIVE/R1039.md`.
