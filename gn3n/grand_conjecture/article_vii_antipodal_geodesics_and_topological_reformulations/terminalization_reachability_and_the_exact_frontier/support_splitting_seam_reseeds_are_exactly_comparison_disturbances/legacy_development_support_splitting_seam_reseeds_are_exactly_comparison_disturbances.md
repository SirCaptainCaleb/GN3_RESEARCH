# Support-splitting seam reseeds are exactly comparison disturbances — preserved pre-item development

## Development

## Support-splitting seam reseeds cannot remain quiet

Let (H) be a no-two-cover boundary tournament. Let
[
Smid P'mid Q'
]
be a displayed spanning three-cover, with all three supports nonempty, and let
[
K
]
be a disjoint Hamiltonian support such that
[
H-K=Amid B
]
is a two-cover.

Assume (Amid B) splits the displayed support (S), in the sense of
[[seam_reseeding_either_preserves_or_splits_the_maximal_support]].

Compare the two displayed paths (A,B) with the three support classes
[
S,qquad P',qquad Q'.
]

Cut every ordinary edge of (A) or (B) whose endpoints lie in different displayed classes. Let (t) be the number of such interclass comparison edges.

Because (Amid B) has two components and the displayed cover has three nonempty classes,
[
tge1.
]

### Case 1: (tge2)

Cutting the (t) interclass edges produces
[
2+tge4
]
nonempty monochromatic comparison blocks distributed among only three displayed classes.

Hence some displayed class occurs in at least two comparison blocks.

If those two blocks lie in different comparison paths, then along the inherited displayed Hamilton order of that class there is an ordinary displayed edge whose endpoints lie in different paths of (Amid B).

If they lie in the same comparison path, that path leaves the displayed class through a nonempty exterior segment and later returns.

Thus (tge2) gives exactly a split-edge or leave-and-return path disturbance.

### Case 2: (t=1)

Cutting the unique interclass edge produces exactly three monochromatic blocks. Since all three displayed classes are nonempty, each occurs in exactly one block.

If the relative order inside any block disagrees with the inherited Hamilton order on its displayed class, there is a Hamilton-order disagreement.

Assume therefore that all three blocks preserve their inherited relative orders.

One comparison path consists of one whole displayed class; the other comparison path concatenates the other two whole displayed classes across the unique interclass edge.

If the isolated class is (S), then
[
H-K=Smid R
]
for a Hamiltonian path (R) on (P'cup Q'). This is exactly the support-preserving reseed branch of
[[support_preserving_seam_reseeds_immediately_create_a_short_rail_state]].

If the isolated class is (P') or (Q'), then the unique interclass comparison edge directly joins (S) to the other complementary rail. This is the direct mixed-edge comparison disturbance.

Therefore:

> **Reseed-disturbance theorem.** Every support-splitting seam reseed yields at least one of:
> 1. an inherited displayed edge split between the two comparison paths;
> 2. a leave-and-return comparison path through a nonempty exterior segment;
> 3. Hamilton-order disagreement on a displayed support;
> 4. a direct comparison edge joining the old support (S) to one complementary rail;
> 5. the support-preserving reseed (H-K=Smid R).

In the globally maximal seam setting, outcome 5 is already reduced to an order-four complementary rail by
[[support_preserving_seam_reseeds_immediately_create_a_short_rail_state]].

Hence seam reseeding introduces no independent recurrence phenomenon: outside the short-rail branch, it is exactly a comparison-disturbance interface.

The proof is purely a component/block count. It uses no minimum-counterexample hypothesis, cyclic rotation, path reversal, or finite computation.
