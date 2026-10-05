# Elevation: bounded-window witness filtrations have L+2-local commuting failures

## Metadata

- ID: elevation_bounded_window_witness_filtrations_have_l2_local_commuting_failures
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 132
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

## General locality principle for protected commuting cubes

Let a local witness filtration on spanning orders be defined by a family (mathcal W) of forbidden configurations such that every witness is determined by an interval of at most (L) consecutive vertex positions.

Fix a witness depth (r). Let (S) be a set of pairwise commuting adjacent Coxeter generators, so their two-position supports are pairwise disjoint. From one chamber (pi), write
[
pi_T=piprod_{sin T}s
qquad(Tsubseteq S).
]

Assume (T
earnothing), (pi_T) is not protected at depth (r), and every immediate predecessor
[
pi_{T-{s}}
qquad(sin T)
]
is protected. Let (W) be an inward witness in (pi_T), determined by a consecutive interval (I) with
[
|I|le L.
]

**Locality theorem.** Every generator in (T) has support meeting (I). Consequently every active adjacent-swap support lies in the one-position enlargement of (I), so the entire minimal protection failure is supported on at most
[
oxed{L+2}
]
consecutive vertex positions.

**Proof.** If some (sin T) had support disjoint from (I), undoing (s) would leave every ordered datum determining (W) unchanged. The same inward witness would therefore occur in the immediate predecessor (pi_{T-{s}}), contradicting its protection. Hence every support meets (I). If (I=[a,b]), any adjacent-swap support ({i,i+1}) meeting (I) lies in ([a-1,b+1]), which has at most (L+2) positions. (square)

For the positive Article VII language
[
mathcal W_+={001,011,0101},
]
one has (L=6). Thus every minimal commuting-cube protection failure is eight-position local, recovering [[protected_commuting_square_failures_are_eight_position_local]] and [[minimal_commuting_cube_protection_failures_are_eight_position_local]] at once.

### Elevation consequence

This theorem belongs conceptually at the first introduction of a bounded-window witness filtration, before any terminal classification. It says that **higher-dimensional commuting source freedom can never create a genuinely long-range new protectedness obstruction**. Long-range difficulty can only enter through the existence/choice of the repair itself or through noncommuting local braid structure; simultaneous commuting interactions are uniformly local from the outset.

For Article VII this strengthens the natural-carrier two-skeleton program: not only are higher-dimensional commuting cubes unnecessary as separate topological obstructions, but every minimal failure that must be checked on their boundary is already contained in an eight-position band.

## Development

## General locality principle for protected commuting cubes

Let a local witness filtration on spanning orders be defined by a family (mathcal W) of forbidden configurations such that every witness is determined by an interval of at most (L) consecutive vertex positions.

Fix a witness depth (r). Let (S) be a set of pairwise commuting adjacent Coxeter generators, so their two-position supports are pairwise disjoint. From one chamber (pi), write
[
pi_T=piprod_{sin T}s
qquad(Tsubseteq S).
]

Assume (T
earnothing), (pi_T) is not protected at depth (r), and every immediate predecessor
[
pi_{T-{s}}
qquad(sin T)
]
is protected. Let (W) be an inward witness in (pi_T), determined by a consecutive interval (I) with
[
|I|le L.
]

**Locality theorem.** Every generator in (T) has support meeting (I). Consequently every active adjacent-swap support lies in the one-position enlargement of (I), so the entire minimal protection failure is supported on at most
[
oxed{L+2}
]
consecutive vertex positions.

**Proof.** If some (sin T) had support disjoint from (I), undoing (s) would leave every ordered datum determining (W) unchanged. The same inward witness would therefore occur in the immediate predecessor (pi_{T-{s}}), contradicting its protection. Hence every support meets (I). If (I=[a,b]), any adjacent-swap support ({i,i+1}) meeting (I) lies in ([a-1,b+1]), which has at most (L+2) positions. (square)

For the positive Article VII language
[
mathcal W_+={001,011,0101},
]
one has (L=6). Thus every minimal commuting-cube protection failure is eight-position local, recovering [[protected_commuting_square_failures_are_eight_position_local]] and [[minimal_commuting_cube_protection_failures_are_eight_position_local]] at once.

### Elevation consequence

This theorem belongs conceptually at the first introduction of a bounded-window witness filtration, before any terminal classification. It says that **higher-dimensional commuting source freedom can never create a genuinely long-range new protectedness obstruction**. Long-range difficulty can only enter through the existence/choice of the repair itself or through noncommuting local braid structure; simultaneous commuting interactions are uniformly local from the outset.

For Article VII this strengthens the natural-carrier two-skeleton program: not only are higher-dimensional commuting cubes unnecessary as separate topological obstructions, but every minimal failure that must be checked on their boundary is already contained in an eight-position band.
