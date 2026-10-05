# Ten-position normalization of terminal surgery

## Metadata

- ID: ten_position_normalization_of_terminal_surgery
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 12
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Normalizing terminal surgery to a ten-position window

The terminal repair need not use the minimal determining support.

Let (I) be the contiguous positional span of a centered or overlapping terminal configuration. The finite classification gives (|I|le 10). If (nle 10), the whole boundary tournament already has a spanning two-cover, so assume (nge11).

Choose a contiguous ten-position interval (Jsupseteq I). By the ten-vertex theorem, the induced boundary tournament on the ten vertices occupying (J) has a complementary Hamiltonian (5|5) cover. Replace the order on (J) by the two Hamiltonian path orders, with the second reversed in the usual status-word convention.

Every status triple wholly inside (J) is then a status triple of a genuine two-cover ordering of (H[J]), hence contains no forbidden witness (001,011,0101) (and, after the dual-polarity normalization, no selected witness at a depth (le r)). Any status coordinate changed across an endpoint of (J) lies farther from the center than the original terminal determining interval (I). Thus every newly created selected witness is strictly farther outward.

Therefore every terminal surgery may be normalized to a **ten-position surgery**. This has two advantages.

1. The local finite input is always the same theorem: every ten-vertex boundary tournament admits a Hamiltonian (5|5) partition.
2. When an adjacent Coxeter generator crosses one endpoint of (J), the ten-vertex support changes by exactly one vertex:
   [
   S=Tcup{x}longleftrightarrow S'=Tcup{y},
   qquad |T|=9.
   ]
   Hence [[compatible_two_covers_under_a_one_vertex_terminal_support_exchange]] applies uniformly; no separate (6,7,8,9,10)-vertex compatibility analysis is needed.

For generators entirely inside (J), the vertex set of the repair support does not change. For generators entirely outside (J), surgery commutes with the generator. Thus the only support-changing local transition is precisely the one-vertex exchange handled by the compatible (5|5) lemma.
