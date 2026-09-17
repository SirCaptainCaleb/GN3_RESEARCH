# S9042 — Backward E9003 Consumption Portals

## Setup

Work inside a retained phase-one prepayment packet to which the published first-source phase-descent engine applies. Let

`G=H-{A,C}`

be the relevant pair-deletion residue and let `F` be its retained physical exact two-cover. Every proper path, reversal, or cycle constructed below is required to be born inside that retained packet, before any transition to phase zero.

The point of this package is that several objects which arose historically only after long exchange arguments are already complete inputs to first-source descent.

## Theorem A — Exact-cardinality defect portal

Let `M` be a split-copy matching on `G` of exact-two-cover cardinality with

`tau(M)<tau(F)`.

Assume that if `M` is nonphysical, its construction retains an explicit certificate of one of the following kinds:

- a bad selected turn;
- a selected two-edge backtrack; or
- a directed selected cycle.

Then `M` yields an immediate first-source phase-descent entrance.

### Proof

If `M` is physical, exact-two-cover cardinality and physicality make it a literal exact two-cover of `G`. It differs from `F`, because their transition counts differ. Thus `F` and `M` are two nonidentical exact covers of the same residue. Restoring the same deleted anchor support `{A,C}` gives the common-residue exact-exact portal of the first-source phase-descent engine.

Suppose `M` is nonphysical. A bad selected turn `(x,y,z)` gives the tight reverse trimer `(z,y,x)` by boundary antisymmetry. A selected two-edge backtrack is already a packet-born reversal path. A directed selected cycle whose turns are tight is a proper tight cycle; choose any selected state as a named break. Each alternative therefore produces the required packet-born proper path or certified cycle break. ∎

## Theorem B — Singleton-loop portal

Suppose a proper-prefix split matching `N` in the retained packet has the same selected-state cardinality as a spanning three-forest and reaches a singleton-defect coincidence: both split copies of one physical vertex `x` are unmatched. Then either `N` already has a bad-turn, backtrack, or cycle birth, or it produces a packet-born proper tight trimer. Hence it is an immediate first-source phase-descent entrance.

### Proof

If a bad turn, selected backtrack, or directed selected cycle is present, Theorem A's defect argument applies.

Otherwise `N` is a physical acyclic tight path forest. Its cardinality is `|G|-3`, so it has exactly three path components. Since both split copies of `x` are free, one component is the singleton `(x)`. In the qualification regime `|H|>10`, so `|G|>=9`; the remaining two components therefore contain a selected edge `y->z` on vertices distinct from `x`.

Boundary antisymmetry makes exactly one of `(x,y,z)` and `(z,y,x)` tight. That tight trimer is proper and is produced directly from the retained loop packet. Hence it is a first-source prepayment birth. ∎

## Theorem C — Three-forest merge portal

Let `D` be a retained pair- or triple-deletion support carrying a tight Hamilton path. Put

`G=H-D`.

Let `F` be a retained exact two-cover of `G`, and let

`J=P|Q|R`

be any physical spanning three-path forest of `G` born in the same retained prepayment packet. Then a cross-component endpoint bridge either emits a packet-born proper reverse trimer or yields a physical exact two-cover of `G` different from `F`. Consequently every such `J` is already an entrance to first-source phase descent.

### Proof

Take an ordered pair of distinct rails, say

`P=(p_0,...,p_k)`, `Q=(q_0,...,q_l)`,

and propose the endpoint bridge

`e=p_k -> q_0`.

Because the rails are disjoint components, adding `e` creates neither a directed cycle nor a selected two-edge backtrack. Every inherited turn remains tight. The only new turns are

`(p_{k-1},p_k,q_0)` when `k>=1`,

and

`(p_k,q_0,q_1)` when `l>=1`.

If either existing seam is bad, boundary antisymmetry gives its complete reversal as a tight trimer on three distinct physical vertices. This is a packet-born proper path and therefore a first-source entrance.

If every existing new seam is tight, `J+e` is a physical exact two-cover `T_e` of `G`. If `T_e` differs from `F`, restore the retained Hamilton path on `D` to both covers and use the common-residue exact-exact portal.

It remains to avoid the case `T_e=F`. Every merged cover has selected-state set

`E(J) union {e}`.

Since `|F|=|J|+1`, equality `T_e=F` forces `E(J) subset E(F)` and makes `e` the unique state in `E(F)-E(J)`. Therefore at most one of the six ordered bridges between the three rails can reconstruct `F`. If one does, choose any other ordered rail pair. That bridge either has a bad seam, giving the proper trimer, or produces a nonidentical exact cover. ∎

## Theorem D — Every canonical E9005 terminal interface is cancellable before specialization

In the canonical sharp-cell exchange engine, every exported terminal interface already enters first-source descent. More precisely:

1. every lower-transition exact-cardinality output is consumed by Theorem A;
2. every singleton-defect loop is consumed by Theorem B; and
3. in the sharp staircase with `tau(F)=3`, `tau(J)=1`, and first-positive index `r`, the source-rooted and `v`-rooted first-loss branches are both consumed one step earlier, at `q=r-1`.

### Proof

The first two assertions are Theorems A and B applied to the canonical exchange packet.

For the sharp staircase, use its established prefix ledger. For every `q<r`, the prefix sum satisfies

`S_q in {-1,0}`,

and whenever the canonical closure `g_q` exists, the closed matching

`Nhat_q`

has exact-two-cover cardinality and transition count one. Take `q=r-1`.

If `g_{r-1}` does not exist, the two free split copies have the same physical label. This is precisely the singleton-defect loop, so Theorem B applies.

If `g_{r-1}` exists, `Nhat_{r-1}` has exact-two-cover cardinality and

`tau(Nhat_{r-1})=1<3=tau(F)`.

If physical, it is a nonidentical exact cover of the common residue. If nonphysical, the canonical matching construction exposes one of the standard literal defects: a bad selected turn, a selected backtrack, or a directed selected cycle. Theorem A applies in either case.

This happens before examining the first-loss rectangle at index `r`, and therefore before deciding whether its root is a retained source or `v`. The two sharp structural branches are thus first-source cancellable before their specialization. ∎

## Why this is reusable

The first-source engine consumes much weaker data than the later exchange machinery was originally designed to produce. A physical three-forest, a nonidentical exact cover, or an explicitly certified matching defect is already enough. This package is intended as a backward-applicability checklist whenever a later construction first creates one of those objects.

## Scope and nonclaims

Every theorem here depends on retained phase-one prepayment ancestry. An arbitrary proper path, cycle, matching defect, or three-forest created after entering phase zero is not licensed for replay. These statements prove first-source descent, not global extinction.

## Provenance

Durable synthesis of independently audited workspace results `R2155`, `R2157`, and `R2158`. The final theorem records their application to the published canonical sharp-cell exchange engine.