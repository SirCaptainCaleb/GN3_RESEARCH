# Two-skeleton loop obstructions reduce to one four-label cycle

## Metadata

- ID: two_skeleton_loop_obstructions_reduce_to_one_four_label_cycle
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 133
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

### The remaining loop type

Under the bounded one-variable/pair-factor decomposition, any non-null loop in a carrier component projects nontrivially to one pair factor. On at most four labels the only connected noncontractible clique complex is a chordless four-cycle. Therefore every \(\pi_1\)-obstruction to the natural carrier extension reduces to one four-label cycle. Combined with the six-label disk lemma, the unresolved topological task is to force zero winding or to produce one or two protected exterior labels satisfying the finite disk tests.

## Development

## Every loop obstruction is detected by one four-label pair factor

Assume the hypotheses of [[bounded_pair_reservoirs_reduce_natural_carrier_extension_to_the_two_skeleton]]. Thus for a protected face F, each connected component of
D(F)=F cap X_{r+1}
is homotopy equivalent to a product of circles, where each circle comes from an ordered-pair factor C_E on a reservoir of order at most four whose mutual-pair graph is a chordless four-cycle.

Let gamma:S^1 -> D(F) be a loop arising as the boundary of a triangular two-skeleton extension problem.

**Lemma.** If gamma is not null-homotopic in D(F), then there is one ordered-pair factor on at most four reservoir labels such that the projection of gamma to that factor is not null-homotopic. That factor has mutual-pair graph exactly a chordless C4.

**Proof.**
Choose the connected component C of D(F) containing gamma. By the factor theorem,
C is homotopy equivalent to T^k times a contractible space
for some k>=0, with each S^1 coordinate supplied by one pair factor whose clique complex is a chordless four-cycle. Therefore
pi_1(C) is isomorphic to Z^k,
and the class of gamma is the tuple of its coordinate winding classes. If gamma is nonzero, at least one coordinate is nonzero. The corresponding pair factor is noncontractible; on at most four vertices the classification in [[bounded_pair_reservoirs_reduce_natural_carrier_extension_to_the_two_skeleton]] shows that the only connected noncontractible clique complex is the chordless four-cycle. square

Likewise, a path-component obstruction for an edge of the two-skeleton is detected by one disconnected pair factor or one disconnected one-variable factor. Thus both pi_0 and pi_1 failures are coordinatewise finite.

### Six-label reduction of the loop-filling problem

For the only genuine loop obstruction, name the four reservoir labels a,b,c,d around the mutual C4. By [[two_exterior_labels_fill_the_terminal_four_cycle_by_a_six_triangle_disk]], two additional labels g,h satisfying the explicit mutual-adjacency and protection tests enlarge this factor to a contractible six-label carrier and fill the entire cycle.

Hence the load-bearing topological theorem can be stated in bounded form:

> For every protected four-label terminal-pair C4 arising in an outward-choice zero face, either choose the two-skeleton paths with zero winding in that factor, or find at most two protected exterior labels satisfying the six-label disk tests.

No higher-dimensional topology remains, and no unbounded reservoir topology remains. Failure of the protected one-step carrier map on the outward-choice branch is witnessed either by a disconnected bounded pair factor or by one four-label C4 for which the explicit at-most-six-label filling mechanism cannot be supplied.

This is independent of the separate eighteen-position dependency halo: the halo localizes where protection can change, while this lemma localizes the homotopy obstruction itself to one pair coordinate.
