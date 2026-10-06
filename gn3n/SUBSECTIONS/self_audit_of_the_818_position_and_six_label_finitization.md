# Self-audit of the 8/18-position and six-label finitization

## Metadata

- ID: self_audit_of_the_818_position_and_six_label_finitization
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 134
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Self-audit of the new finitization

The recent localization results establish three different bounds which must not be conflated.

1. [[protected_commuting_square_failures_are_eight_position_local]] and [[minimal_commuting_cube_protection_failures_are_eight_position_local]] show that the **essential Coxeter generators** in a minimal commuting protection failure lie in at most eight consecutive positions.

2. [[coxeter_local_protection_has_an_eighteen_position_dependency_halo]] shows that every positive witness whose truth can differ across that local residue lies in an eighteen-position halo around the active band.

3. [[two_skeleton_loop_obstructions_reduce_to_one_four_label_cycle]] shows that, once the natural carrier factors into bounded pair loci, every nontrivial pi_1 obstruction is detected in one four-label ordered-pair factor; the only connected noncontractible case is a chordless C4. The explicit known fill uses at most two extra labels.

These are localization theorems, not automatic repair theorems.

In particular, the order-eight equitable 4|4 theorem cannot simply be applied to the active eight-position band to claim a protected repair. Reordering the band may alter positive witness windows crossing its boundary. The eighteen-position halo records exactly those possible changes, but an arbitrary reorder of the whole halo would enlarge the dependency range again. Any valid repair must therefore either:
- stay within the original active local degrees of freedom and prove the required protected path/filling there; or
- enlarge the carrier with an explicit protection proof, as in the one- and two-exterior-label pair-locus filling lemmas.

This also clarifies the role of the six-label C4 disk. It fills the topological loop only when its explicit mutual-adjacency and protection tests hold. [[arbitrary_terminal_pair_relations_occur_on_protected_zero_faces]] shows that boundary antisymmetry alone cannot force those tests.

### Correct finite frontier

The outward-choice topology branch has therefore been reduced to:

- component compatibility in bounded pair/one-variable factors;
- a four-label chordless C4 with nonzero winding;
- finding zero-winding path choices or supplying at most two protected exterior labels satisfying the explicit six-label disk tests.

The double-persistent combinatorial branch remains separate. Its unbounded corridor is already compressed to deletion-distance two and bounded endpoint transport data. The two branches should meet only after one proves additional global deletion/cover structure that forces the finite pair-locus tests; local boundary antisymmetry is insufficient.

This is the self-checked form of the finitization.

## Frontier

- Development version when composed: None
- Development version now: 1
