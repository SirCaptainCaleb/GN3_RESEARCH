# Audit: the external gauge does not by itself close rank-two coherence

## Metadata

- ID: audit_the_external_gauge_does_not_by_itself_close_rank_two_coherence
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 16
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["local_witness_topology_and_the_finite_terminal_theorem", "a_local_pure_carrier_shows_same_face_escape_is_false", "rank_two_coherence_closes_by_the_external_gauge", "rank_two_normalization_squares_close_and_only_the_inside_boundary_braid_remains"]

## Cold composition

(none yet)

## Development

## Audit of the proposed external-gauge closure

The proposed argument in [[rank_two_coherence_closes_by_the_external_gauge]] is not valid for the witness labeling actually used in Article VII. The fixed external antipodal gauge does **not** orient every occurrence of a fixed unsigned witness edge.

In the local-witness construction, after choosing the first path edge represented by a forbidden-pattern occurrence, the label is assigned as follows: if exactly one witness orientation of that path edge occurs, that intrinsic witness orientation is used; the external antipodal gauge is used only when both orientations occur, and on the self-reverse-complement centered alternating case. Thus in general one cannot write ell(pi)=g(pi)e_r on all chambers carrying the same unsigned edge e_r.

Consequently a terminal sign flip +e_r <-> -e_r across a Coxeter edge need not be a swap of the two fixed gauge vertices. The asserted "two gauge edges per rank-two residue" bound therefore does not follow, and the reduction of every square/hexagon to at most two surgery sites is unsupported. The six-vertex same-face counterexample is consistent with a gauge flip, but it proves only that particular local model, not the universal implication used by the closure argument.

The safe conclusions preceding that argument remain available. In particular, [[rank_two_normalization_squares_close_and_only_the_inside_boundary_braid_remains]] closes commuting squares by ten-position normalization and safe transport/collapse, and reduces braid coherence to the maximal-support boundary braid: an order-eleven configuration with an eight-vertex core T and moving vertices a,b,c, whose three ten-vertex supports are T+ab, T+ac, and T+bc.

For the side-sharing compatibility model, the residual braid has an exact common-core form. If one assigns one (5|5) cover to each of the three supports and requires adjacent supports to share an entire Hamiltonian side, then cyclic compatibility forces one Hamiltonian five-set B subset T to be common to all three covers. Writing C=T minus B, the required finite statement is therefore: B, C+ab, C+ac, and C+bc are all Hamiltonian. Pairwise one-vertex-exchange compatibility alone cannot bypass this cyclic obstruction.

Accordingly the grand-conjecture frontier remains the maximal-support A_2 braid, not the external-gauge lemma.
