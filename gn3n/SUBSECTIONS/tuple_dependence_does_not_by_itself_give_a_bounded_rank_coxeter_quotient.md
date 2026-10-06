# Tuple dependence does not by itself give a bounded rank Coxeter quotient

## Metadata

- ID: tuple_dependence_does_not_by_itself_give_a_bounded_rank_coxeter_quotient
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 83
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Audit of the inference from tuple dependence to rank

This addendum concerns [[boundary_block_tuple_localization_bounds_active_rank]]. Its local observation about the number of potentially label-changing *positions* does not establish its conclusion that all other generators can be collapsed to obtain bounded Coxeter coherence.

Let a block have N positions, and suppose its label factors through the ordered tuple in its final k positions. Put H=<s_1,...,s_{N-k-1}>. Orders with the same tuple are exactly the H-orbits for swaps of positions. Thus the tuple space is a coset space, of cardinality N!/(N-k)!, rather than a Coxeter group of rank k. This conclusion holds even when tuple dependence is granted in full.

Here is the explicit obstruction to a group-quotient interpretation. Assume N>=k+2. The neutral generator a=s_{N-k-1} and the tuple-crossing generator b=s_{N-k} satisfy aba=bab. In any group quotient killing a, this becomes b=b^2, so b is also killed. Propagating the same argument along the connected type-A diagram kills every generator. Hence no nontrivial Coxeter group quotient can simultaneously collapse all neutral generators and retain a potentially sign-changing crossing generator.

Nor does restriction to the last k generators solve this problem. Their parabolic subgroup only permutes the final k+1 positions. It fixes every label initially in positions 1,...,N-k-1, so it cannot reach a terminal tuple containing one of those labels. In the full block, such a label can be moved to position N-k by neutral swaps and then enter the tuple through b. Consequently the bounded list of active swap positions does not bound the number of participating vertex labels or supply a single bounded parabolic target.

The correct geometric description is a family of tuple fibers. Each fiber is the permutahedral face freely ordering the first N-k positions while freezing the final tuple. Collapsing these contractible fibers, if used, requires its own construction over the coset space, including compatibility at the crossing generator and its braid with the last neutral generator. The group argument above does not rule out a different topological quotient or carrier construction; it shows that such a construction cannot be inferred just by deleting neutral Coxeter generators.

The inherited-mask result in [[frozen_window_carriers_and_separator_relabeling_require_precise_invariants]] retains whole ambient Coxeter components disjoint from a fixed repaired window. It does not automatically justify discarding the neutral prefix of a connected boundary block while transporting its crossing generator. Applying it here would require additional tuple-level repair and gluing data.

Corrected conclusion: under the stated tuple-factorization hypotheses, at most k generator positions in one boundary block can change the label in one swap. Bounded-rank coherence, and compatibility between tuple fibers, remain proof obligations. No bound on boundary-block order, and no completed protected genus iteration, follows from this observation alone.

## Frontier

- Development version when composed: None
- Development version now: 1
