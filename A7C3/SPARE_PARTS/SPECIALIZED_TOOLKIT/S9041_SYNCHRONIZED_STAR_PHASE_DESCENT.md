# S9041 — Synchronized-Star Direct Phase-Descent Package

## Setup

Let `H` be a smallest Strong Level-(1) boundary-tournament counterexample in the order range `|H|>10`. Assume the synchronized singleton-star output of the three-spoke Boolean-cube classifier. Thus there are anchors `A,C`, sources

`P={p,q,r}`,

an auxiliary vertex `v`, a tight spectator path `B`, and

`X={v,p,q,r}`,

such that:

- `(A,s,C)` is tight for each `s in P`;
- the top residue `G=H-{A,C}` has a retained exact two-cover `F` in which `p,q,r` are all internal;
- the common core cover is `(v)|B`;
- for each pair `{t,u} subset P`, there is a literal exact two-cover `J_{tu}|B` of `H-{A,C,s}`, where `s=P-{t,u}` and `J_{tu}` is a physical tight trimer on `{t,v,u}`;
- `X` has no Hamilton tight path of order four; and
- all these objects belong to the same retained phase-one prepayment packet.

The conclusions below are alternative direct consumers of this synchronized packet. They do not use the synchronized mass-four balanced pair as a phase-zero trigger.

## Theorem A — Internal-puncture entrance

For every source `s in P`, puncturing `s` from the retained top cover `F` and comparing with the complementary rank-two row `J_{tu}|B`, where `{t,u}=P-{s}`, produces the internal-puncture three-to-two entrance of the first-source phase-descent engine. Consequently that engine returns either a spanning two-cover or a checkpoint of phased rank strictly below the participating phase-one source packet.

### Proof

Fix `s` and write `{t,u}=P-{s}`. Since `s` is internal on one rail of `F`, deleting `s` splits that rail into two nonempty inherited tight paths while the other rail survives. Hence `F-s` is a literal spanning three-path cover of

`W_s=H-{A,C,s}`.

The synchronized rank-two row

`T=J_{tu}|B`

is an exact two-cover of precisely the same residue `W_s`.

Some selected edge of `T` crosses two components of `F-s`: otherwise each connected rail of `T` would lie inside one inherited component, and two rails could not cover all three components. If one crossed component is nontrivial, combine the crossing edge with its inherited `F`-neighbor. If the resulting seam is tight, it is already a proper tight trimer; if it is bad, boundary antisymmetry gives the complete reverse trimer. If both crossed components are singletons, they are the two pieces of the punctured source rail, so that rail had order three; combining the crossing edge with either inherited source edge gives the same proper-trimer conclusion by boundary antisymmetry.

Thus the comparison emits a literal source-labelled proper tight path while retaining its phase-one birth ancestry. This is exactly the internal-puncture entrance of the first-source phase-descent theorem. ∎

## Theorem B — Direct full-H anchor lift and cap surgery

For every `s in P`, with `{t,u}=P-{s}`, the three paths

`N_s=(A,s,C) | J_{tu} | B`

form a literal spanning three-forest of `H`. Both nonanchor rails are edge-bearing. For either nonanchor rail

`R=(u_0,...,u_k)`, `k>=1`,

with the other nonanchor rail denoted `Q`, counterexample status forces at least one of the following:

1. `(s,C,u_0)` is bad;
2. `(u_k,A,s)` is bad;
3. `k>=2` and both `(C,u_0,u_1)` and `(u_{k-1},u_k,A)` are bad.

Thus the later one-cut/two-join cap trichotomy is already present directly in the synchronized star.

### Proof

The paths `(A,s,C)`, `J_{tu}`, and `B` are tight, pairwise vertex-disjoint, and together cover `V(H)`. Hence `N_s` is a literal spanning three-forest. The trimer `J_{tu}` has an edge, while

`|B|=|H|-6>=5`,

so `B` is edge-bearing as well.

Fix an edge-bearing nonanchor rail `R=(u_0,...,u_k)`. Cut an edge `u_i u_{i+1}` and add the two joins

`u_k -> A`, `C -> u_0`.

If every new seam is tight, the non-`Q` vertices form the literal path

`u_{i+1},...,u_k,A,s,C,u_0,...,u_i`,

and together with `Q` this is a spanning exact two-cover of `H`, impossible.

When `k=1`, cutting the sole rail edge removes both rail-facing seams, so the only new seams are `(u_k,A,s)` and `(s,C,u_0)`; at least one is bad.

Now let `k>=2` and suppose both source-facing seams are tight. Cutting the first rail edge leaves only the additional seam `(u_{k-1},u_k,A)`, so that seam must be bad. Cutting the last rail edge leaves only `(C,u_0,u_1)`, so that seam must also be bad. This proves the trichotomy. Complete reversal converts every bad seam into its corresponding tight reverse cap. ∎

## Theorem C — Source-insertion dichotomy

Fix `s in P`, let `{t,u}=P-{s}`, and retain the displayed spectator order

`B=(b_1,...,b_m)`.

Exactly one of the following useful alternatives occurs.

1. The source `s` inserts into some literal slot of `B`. Then the resulting tight path `B_s` gives a physical exact two-cover

   `J_{tu} | B_s`

   of `G=H-{A,C}`, with transition count `1` for an endpoint insertion and `2` for an internal insertion.

2. Every insertion slot fails. Then S9031 supplies a star-triangle or reverse-spoke-hook certificate supported on `s` and at most three consecutive vertices of `B`.

### Proof

Test the `m+1` literal insertion positions of `s` in the displayed tight order of `B`. If one succeeds, `B_s` and `J_{tu}` are disjoint tight paths covering all of `G`. Since `J_{tu}` lies wholly in `X` and `B` wholly in the spectator shore, an endpoint insertion introduces exactly one selected `X|B` transition, while an internal insertion introduces exactly two. The trimer contributes none.

If every insertion fails, this is exactly the hypothesis `I_B(s)=empty` of S9031, which returns the stated bounded first-flip certificate. ∎

## Theorem D — Elementary all-branches entrance to first-source descent

Every synchronized singleton-star output above enters the first-source prepayment phase-descent engine directly.

### Proof

Fix any source `s`, with complementary sources `{t,u}`, and apply Theorem C.

If an insertion succeeds, put

`T=J_{tu}|B_s`.

Then `T` and `F` are physical exact two-covers of the same pair-deletion residue `G`. They are nonidentical: `t,u` are endpoints of the trimer rail in `T`, while every source is internal in `F`. Therefore the common-residue exact-cover comparison of the first-source phase-descent engine applies after restoring the same deleted anchor support `{A,C}`. It produces an eligible packet-born proper path or cycle.

Assume instead that every insertion fails. Write

`e_i={b_i,b_{i+1}`, `f_i={s,b_i}`

in the line-graph comparison notation of S9031. In a star-triangle

`f_t -> e_{t-1} -> e_t -> f_t`, 

the comparison arrows give literal tight source trimers, for example

`(s,b_t,b_{t-1})` and `(b_{t+1},b_t,s)`.

In a reverse-spoke hook, the relation

`f_{t+1} -> f_t`

gives the literal tight source trimer

`(b_{t+1},s,b_t)`.

The terminal hook cases retain the same source-containing relation. These trimers are proper because `|B|>=5`, and they are born directly from the retained source-labelled phase-one insertion analysis before any phase-zero transition. Hence they satisfy the generic proper-path birth interface of the first-source phase-descent theorem.

Thus either insertion branch enters first-source descent. Combined with the four nonsynchronized classifier outputs, which already carry the same licensed phase-one birth interface, every output of the three-spoke Boolean-cube classifier feeds the first-source phase-descent engine. ∎

## Why this is reusable

The synchronized singleton star does not require a transition zipper, source-gate normalization, or marked residual chase merely to obtain first-source descent. It already contains three independent direct portals: internal puncture, full-H anchor-lift surgery, and elementary source insertion. The insertion proof is the shortest complete consumer.

## Scope and nonclaims

These results prove first-source phase descent, not global extinction. In particular, they do not authorize replay from a phase-zero parent, and they do not treat the synchronized balanced pair itself as a phase-zero trigger.

## Provenance

Durable synthesis of independently audited workspace results `R2153`, `R2159`, `R2161`, and `R2162`; the failed-insertion local lemma is the already durable S9031.