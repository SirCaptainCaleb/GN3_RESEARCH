# D17.435 — The v-rooted sharp cell has a singleton v block and a two-ended three-spoke source block

**Workspace:** D17
**State:** audited PASS
**Canonical result:** `A7C3/RESULTS/USABLE/ACTIVE/R1037.md`
**Key:** `g37-v-rooted-cell-two-ended-x-mated-source-block`

## Statement
Let `F` be the retained exact two-path source cover of `G=B disjoint-union X`, `X={v,p,q,r}`, with `p,q,r` internal and `tau(F)=3`. In the v-rooted residual cell, the selected F-edge incident with `v` is an `X|B` transition.

Then

`d_F(v)=1`, `e_XX(F)=2`, `b_X(F)=2`, `b_B(F)=3`.

The two maximal X-blocks are the singleton endpoint block `{v}` and one internal block containing all three source spokes. Up to reversal the latter is

`B_L -> s_1 -> s_2 -> s_3 -> B_R`,

with `{s_1,s_2,s_3}={p,q,r}`. Its two boundary source gates have opposite path polarity and are both X-mated. The unique `v-B` edge is the third and only non-source transition.

## Direct repair proof
Because the three source spokes are internal in F, their selected degrees contribute six incidences at X. If `d=d_F(v)` and `e_XX` is the number of selected X-X edges, then

`6+d = 2e_XX + tau(F) = 2e_XX+3`.

The v-rooted branch gives a selected edge at v, so `d in {1,2}`; parity forces `d=1`, hence `e_XX=2`.

Each maximal X-block with m vertices contributes m-1 selected X-X edges, so `e_XX=|X|-b_X=4-b_X`, giving `b_X=2`. Across two path components the total number of X/B blocks is `tau(F)+2=5`, hence `b_B=3`.

Since the unique selected edge at v is crossing, v has no selected X-neighbor and its X-block is `{v}`. The other X-block therefore contains exactly p,q,r. All three are internal in F, so the block is bracketed by B on both sides. In its literal directed order `s_1,s_2,s_3`, the endpoint spokes each have one crossing incidence and one internal X-X mate, giving the two opposite-polarity X-mated source gates. Together with the unique v-B edge these exhaust `tau(F)=3`.

This proof reconstructs the formerly missing D17.418 source-degree/block package directly; no historical SV input is needed.
