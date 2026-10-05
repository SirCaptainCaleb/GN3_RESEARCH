# Coxeter-local protection has an eighteen-position dependency halo

## Metadata

- ID: coxeter_local_protection_has_an_eighteen_position_dependency_halo
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 131
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

### Dependency halo

If two spanning orders differ only inside an active interval \(B\), any positive witness whose truth value changes must have determining interval meeting \(B\). Since positive witnesses use at most six consecutive vertices, every changed witness lies in the five-position enlargement on each side of \(B\). In particular an eight-position active band has an eighteen-position dependency halo. This is a localization statement, not a repair theorem: modifying the active band may still create a new witness in the halo.

## Development

## The full protection dependency halo has order at most eighteen

Let B=[a,b] be a consecutive positional band, and compare two spanning orders which agree outside B but may reorder the labels inside B. Work with W_+={001,011,0101}.

Every positive witness is determined by a consecutive vertex interval D of order at most six.

**Lemma (dependency halo).** If the truth value of a positive witness occurrence differs between the two orders, then its determining interval D intersects B. Consequently
D subseteq [a-5,b+5].
Thus every change in the positive-witness set is determined entirely by the labels and triple orientations occurring in the halo
H(B)=[a-5,b+5].

**Proof.**
If D is disjoint from B, the two orders agree at every position of D, so every consecutive ordered triple used by the occurrence is identical in the two chambers. Its truth value is therefore unchanged. Hence D intersects B.

An interval of order at most six that intersects [a,b] can begin no earlier than a-5 and end no later than b+5. square

Combine this with [[minimal_commuting_cube_protection_failures_are_eight_position_local]]. For a minimal protection failure in a commuting cube, all essential generators lie in a band B of order at most eight. Therefore every positive witness whose status can differ anywhere in that local compatibility problem lies in a halo of order at most
8+10=18.

For an A2 braid the active positional band has order three, so the corresponding halo has order at most thirteen.

### Exact finitization of Coxeter-local protection

Every Coxeter-local obstruction to protected carrier compatibility is completely determined by a uniformly bounded positional interface:
- at most 18 consecutive positions for commuting-factor interactions;
- at most 13 consecutive positions for braid interactions.

All vertices outside the halo are invisible to the protection comparison: their relative order and all witness occurrences supported wholly outside the halo are identical throughout the local residue.

This does not assert that every order-18 interface is repairable, nor does it invoke direct enumeration. It identifies the correct finite theorem. Any failure of the one-step protected carrier map can be witnessed by a bounded local configuration of at most eighteen positions together with its face-block structure. In particular no unbounded reflected corridor or remote endpoint reservoir can enter a two-skeleton obstruction except through the bounded labels actually occupying this halo.
