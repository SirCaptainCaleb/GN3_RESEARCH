# The singleton-spoke hard cell roots the first-loss zipper at its source

**Workspace:** D17
**State:** established
**Key:** `g37-singleton-spoke-source-rooted-first-loss-zipper`

**Summary:** In the SINGLETON-SPOKE TWO-SWITCH alternative of D17.419, the normalized neutral transition contribution of D17.421 is forced to vanish. Consequently the normalized closure staircase is exact: it has transition count 1 before the first old B-incidence of the unique DOUBLE-B source spoke `t`, jumps to 3 at that first incidence, and stays at 3 thereafter. Thus, unless the unique singleton-defect loop occurs exactly there, the first numerical loss rectangle of D17.421 is precisely the first `t`-transition. Moreover its old same-side pairing consists of one `X-X` edge incident with `t` and one `B-B` edge, while its new pairing consists of the two cross edges. The first-loss `K_{2,2}` is therefore not source-anonymous: it carries a canonical physical source-rooted same-side diagonal. The remaining G37 reflection problem must preserve this marked corner; a reflection that exchanges the two old same-side edges while fixing the source and the physical `X|B` partition is not an admissible symmetry of this branch.

## 1. Input

Assume the sharp G35 hard cell

`tau(F)=3`, `tau(J)=1`, `w(C_*)=2`

and the SINGLETON-SPOKE TWO-SWITCH alternative of D17.419. Thus one DOUBLE-B source spoke `t` has both old F transition incidences on the unique augmenter

`C_* = e_1,f_1,...,f_{m-1},e_m`,

there is no J-transition on `C_*`, and these are the only two F-transitions on `C_*`. In particular, for the prefix sum

`S_q = sum_{i<=q}(chi(e_i)-chi(f_i))`,

D17.419 gives the exact three-level form

- `S_q=0` before the first `t`-transition;
- `S_q=1` between the two `t`-transitions;
- `S_q=2` after the second.

Retain the F-normalized closures of D17.421:

`hat N_q = hat M_q + g_q`,  `g_q=a_q->b_m`,

whenever `a_q != b_m`. Write

`W_0 = sum_D w(D)`

for the total transition weight of the delta-zero symmetric-difference components. D17.421 gives

`T_q := tau(hat N_q)=1+S_q+W_0+gamma_q`,

where `gamma_q=chi(g_q)` and

`gamma_q = (S_q mod 2) xor (w(C_*) mod 2)`.

## 2. Neutral normalization has zero transition weight

The transition-count difference between the old exact source cover and J is

`tau(F)-tau(J)=3-1=2`.

The symmetric difference consists of the unique F-heavy augmenter `C_*` together with the delta-zero components. Transition differences add over these components, so

`tau(F)-tau(J)=w(C_*)+W_0`.

Since `w(C_*)=2`, necessarily

`W_0=0`.                                                   (SR.1)

Thus in this branch the neutral normalization of D17.421 loses no transition information at all.

## 3. The closure staircase is exact

Because `w(C_*)=2` is even, D17.421's parity identity reduces to

`gamma_q = S_q mod 2`.                                    (SR.2)

Combining (SR.1), (SR.2), and the three-level form of `S_q` gives, at every defined normalized closure,

- before the first `t`-transition: `S_q=0`, `gamma_q=0`, hence `T_q=1`;
- between the two `t`-transitions: `S_q=1`, `gamma_q=1`, hence `T_q=3`;
- after the second `t`-transition: `S_q=2`, `gamma_q=0`, hence `T_q=3`.

Therefore the transition floor `tau(F)=3` is reached for the first time exactly when the first old B-incidence of `t` is installed.

Let `r` be the index of that first `t`-transition. If `g_r` is defined, then the canonical first-loss index `q^dagger` of D17.421 is

`q^dagger=r`,                                             (SR.3)

and

`T_{r-1}=1`, `T_r=3`.                                    (SR.4)

If `g_r` is not defined, then `a_r=b_m`, and this is precisely the unique singleton-defect loop interruption already fenced in D17.421. No second exceptional case is introduced here.

## 4. The first-loss rectangle has a source-rooted same-side diagonal

Assume the non-loop case. D17.421 identifies the upward step at `r` as the literal matching switch

`{f_r, g_{r-1}}  <->  {e_r, g_r}`,

with

`chi(f_r)=chi(g_{r-1})=0`,
`chi(e_r)=chi(g_r)=1`.                                    (SR.5)

The installed old F-edge `e_r=a_{r-1}->b_r` is, by (SR.3), the first transition incidence of the physical source spoke `t`. Hence `t` is one endpoint of `e_r` and lies in `X`.

There are two copy-side possibilities.

### OUT copy of t

If `a_{r-1}=t`, then `b_r` lies in `B` because `e_r` crosses. Since `f_r=a_r->b_r` is same-side, `a_r` also lies in `B`. Since `g_{r-1}=t->b_m` is same-side, `b_m` lies in `X`. Therefore

- `g_{r-1}` is the `X-X` old edge and is incident with `t`;
- `f_r` is the `B-B` old edge;
- `e_r` and `g_r` are the two cross edges.

### IN copy of t

If `b_r=t`, then `a_{r-1}` lies in `B`. Since `f_r=a_r->t` is same-side, `a_r` lies in `X`. Since `g_{r-1}=a_{r-1}->b_m` is same-side, `b_m` lies in `B`. Therefore

- `f_r` is the `X-X` old edge and is incident with `t`;
- `g_{r-1}` is the `B-B` old edge;
- `e_r` and `g_r` are again the two cross edges.

Thus in either orientation the old same-side diagonal of the first-loss `K_{2,2}` has a unique `X-X` member, and that member contains the physical source spoke `t`. Equivalently, the first-loss rectangle carries a canonical marked source corner before any turn-level absorber is applied.

## 5. Consequence for the G37 reflection test

The SINGLETON-SPOKE branch cannot support a reflection that treats the two old same-side edges of the first-loss rectangle as interchangeable while preserving the exported physical source and the fixed `X|B` partition. Exactly one of those edges is `X-X`, and it is exactly the one incident with `t`; the other is `B-B`.

This does **not** yet prove source-gate zipper absorption. A turn-level reflection could still preserve the marked source corner while changing the relative pairing of the source anchors `A,C` against the two cross edges, and seam legality remains a separate physical obligation. What has been removed is the coarser `S_2` ambiguity of an anonymous exact `K_{2,2}` in the singleton-spoke ancestry class.

Therefore the ancestry split of D17.419 has real discriminating content at the exact first-loss zipper:

- the SINGLETON-SPOKE class is canonically source-rooted at its first numerical loss;
- any remaining reflected-pairing obstruction in this class must respect that root;
- the X-MATED SOURCE GATE class remains the natural place to test whether the same-side old mate supplies an analogous root or whether one genuine orientation bit survives.

No R24, R5, payment, replay, pair-deletion reflection, SAT, or MILP is used.
