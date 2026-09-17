# Portal-free support-changing one-edge transport has trivial edge-token monodromy

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-one-edge-token-monodromy-extinction`

**Summary:** Label the selected directed edges of a literal maximum three-forest by ancestry tokens and transport the token on the deleted edge to the added edge across every one-edge transfer. For a closed walk of reversible support-changing one-edge transfers, any nontrivial token permutation can be reduced by commuting the first exchange through later independent exchanges using the verified-square branch of SV38940. A non-square comparison already yields augmentation, a current trimer, or a shared current cycle. After commutation, the first exchange a->b meets the first later transition that either deletes b or re-adds a. If b is deleted, the two successive transfers compose to the literal one-edge transfer a->c; if that direct move changes support the marked loop shortens, while if it preserves support it is exactly same-rail cycle-rebreak geometry. If a is re-added first, the endpoint state would give a second one-edge transfer into the same added edge b from the pre-exchange state; the fixed-added-edge uniqueness mechanism inside SV38940 rules this out whenever a->b is support-changing, except the literal inverse which cancels. Hence a shortest nontrivial token-holonomy loop cannot exist without encountering augmentation or a trimer/cycle portal. The square-only support-changing one-edge sector is therefore history-flat for canonical edge ancestry.

### 1. Canonical edge-token ancestry
Let `F` be a literal maximum spanning three-forest and let `M(F)` be its directed selected-edge matching. Give every edge of `M(F)` a distinct ancestry token.

For a literal one-edge transfer

  tau : M -> M-a+b,

define the canonical token transport by moving the token carried by `a` to `b` and leaving every other token fixed. This is genuine history-bearing data: after a closed walk returning to the same selected matching, the tokens may a priori return permuted even though the literal forest has returned.

Call such a closed walk TOKEN-NONTRIVIAL when the induced permutation of the initial edge tokens is nonidentity.

We prove that a token-nontrivial closed walk made from reversible SUPPORT-CHANGING one-edge transfers cannot survive without entering one of the portal/exit branches already isolated by SV38940.

### 2. Verified squares are token-flat
Suppose

  M --(a->b)--> M_1 --(d->c)--> M_2

and, from `M_1`, the inverse transfer `b->a` and the next transfer `d->c` fall in the SQUARE branch of SV38940. The fourth forest has matching

  N = M-d+c,

and the opposite side of the square is

  M --(d->c)--> N --(a->b)--> M_2.

Because the two deleted edges and two added edges are literally the same on both routes, the token on `a` ends at `b`, the token on `d` ends at `c`, and every other token is fixed on both routes. Thus every verified one-edge square is exactly token-coherent. No extra ancestry hypothesis is needed.

Consequently a transfer `a->b` may be commuted across any following support-changing transfer which neither deletes `b` nor adds `a`, unless the SV38940 comparison exits through AUGMENTATION, CURRENT TRIMER, or SHARED CURRENT CYCLE.

### 3. Bubble the first transfer to its first genuine interaction
Assume there is a token-nontrivial closed walk with no augmentation/trimer/cycle output during the square comparisons needed below, and choose one with the fewest representative transitions. Let its first transfer be

  tau : a -> b.

Because the walk returns to its initial matching, the newly selected edge `b` must eventually be deleted and the deleted edge `a` must eventually be re-added.

Take the first later transition which either deletes `b` or adds `a`. Every earlier transition does neither. Starting immediately after `tau`, compare the inverse `b->a` with the next transition. In the portal-free branch SV38940 supplies a verified square, and Section 2 commutes `tau` one step to the right without changing the transported token assignment. Iterate. We may therefore assume that `tau` is immediately followed by the first transition touching `{a,b}` in the only possible ways.

### 4. If the new edge is deleted, two transfers compress to one
Suppose the first interaction is

  a -> b,
  b -> c.

The endpoint matching is simply

  M-a+c.

Hence the endpoint forest itself is a literal one-edge transfer `a->c` from the pre-`tau` forest. The canonical token transport on this direct transfer sends exactly the same token from `a` to `c` as the two-step route, with all other tokens unchanged.

If the direct transfer changes the support partition, replacing the two-step segment by this one edge strictly shortens the token-nontrivial closed walk, contradicting minimality.

If the direct transfer preserves the support partition, then one directed edge was added between the terminal and source of the same old rail and one rim edge was deleted to rebreak the resulting directed cycle. This is exactly the same-support CYCLE-ROTATE/rebreak portal isolated in the proof of SV38940. Thus the only nonshortening outcome is already a current cycle portal, not a new one-edge ancestry obstruction.

The special case `c=a` is the literal inverse of `tau` and cancels outright.

### 5. If the deleted edge is re-added first, fixed-added-edge uniqueness forbids the interaction
Suppose instead the first interaction is

  a -> b,
  d -> a.

If `d=b`, the second transfer is the inverse of `tau` and the pair cancels. Assume `d!=b`.

The two-step endpoint matching is

  M-d+b.

Therefore the endpoint forest certifies a second literal one-edge transfer `d->b` from the pre-`tau` forest, using the SAME added edge `b` but a different deletion `d`.

Now use the proof mechanism of SV38940 Section 2, not merely its headline. A support-changing transfer with added edge `b=u->v` has a unique deletion. If an endpoint copy of `b` is already occupied, matching compatibility forces that occupied edge to be the deletion. If both endpoint copies are free, then `b` joins a terminal to a source. When they lie on distinct rails, the root-gate analysis gives either immediate two-cover, no one-edge transfer, or exactly one valid boundary deletion. The only circumstance in which one added edge admits several deletions is when its endpoints lie on the same rail, and then every such move is same-support cycle-rebreak geometry.

Since `a->b` is support-changing, the second transfer `d->b` with `d!=a` cannot exist. Contradiction.

Therefore the first genuine interaction with `tau` cannot be a re-addition of `a` before `b` is deleted, except for immediate inverse cancellation.

### 6. Global extinction of one-edge ancestry holonomy
Sections 2-5 give a reduction algorithm for any closed support-changing one-edge walk with canonical edge-token ancestry.

Commute the first transfer through all independent later transfers. Any failed commutation gives one of the parent exits of SV38940:

  TWO-COVER AUGMENTATION,
  CURRENT TRIMER PORTAL,
  SHARED CURRENT CYCLE PORTAL.

Otherwise the first transfer reaches its first genuine interaction. Re-adding its deleted edge first is impossible except for inverse cancellation. Deleting its newly added edge first either cancels/compresses the walk strictly or enters same-support cycle-rebreak geometry.

Iterating strictly reduces the walk until no transition remains. Hence:

  PORTAL-FREE SUPPORT-CHANGING ONE-EDGE TOKEN MONODROMY IS TRIVIAL.   (TM.1)

Equivalently, any nontrivial permutation of physical selected-edge ancestry around a closed one-edge transport loop forces, somewhere in the reduction, a spanning two-cover, a current tight trimer, or a current proper cycle.

### 7. Consequence for G15 universal discrepancy absorption
This is a global relation, not another local diamond classification. SV38940 already ended the pairwise base geometry; (TM.1) shows that its square branch also carries no hidden edge-ancestry monodromy after arbitrarily many support-changing exchanges.

Thus the most natural history-sensitive mark on the one-edge sector, ancestry of the selected physical edges themselves, is globally flat. Any surviving G15 marked holonomy must use at least one genuinely non-one-edge portal, or must transport ancestry through the trimer/cycle portal mechanisms rather than through the square-only support-changing exchange graph.

This materially narrows the universal-discrepancy target: the one-edge sector is no longer a possible source of nontrivial ancestry by itself.
