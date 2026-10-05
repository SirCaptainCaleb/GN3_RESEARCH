# Minimal commuting-cube protection failures are eight-position local

## Metadata

- ID: minimal_commuting_cube_protection_failures_are_eight_position_local
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 130
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Minimal protection failures in commuting cubes are eight-position local

Work with the positive witness language W_+={001,011,0101}. Every positive occurrence is determined by a consecutive vertex interval I of order at most six.

Let S be a set of pairwise commuting adjacent Coxeter generators, so their two-position supports are pairwise disjoint. From one chamber pi form the commuting cube
pi_T = pi prod_{s in T} s
for T subseteq S.

Assume T is nonempty, pi_T is not protected at depth r, and every immediate predecessor pi_{T-{s}} is protected at depth r for s in T. Let W be a positive witness of depth <r in pi_T, with determining interval I.

**Lemma.** The support of every generator s in T meets I. Consequently every active swap support is contained in the one-position enlargement of I, and hence all essential generators lie in at most eight consecutive vertex positions.

**Proof.**
Fix s in T. If supp(s) were disjoint from I, undoing s would leave every ordered triple used by W unchanged. Thus the same witness W would occur in pi_{T-{s}}, contradicting its protection. Therefore supp(s) meets I for every s.

If I=[a,b], then any adjacent-swap support {i,i+1} meeting I satisfies i<=b and i+1>=a, hence is contained in [a-1,b+1]. Since |I|<=6, this enlarged interval has order at most eight. square

Because the swap supports are disjoint, at most four adjacent transpositions can participate at all, and in fact the geometry is completely determined inside this eight-position band.

### Consequence

For any carrier construction built by independently varying commuting source factors, a minimal failure of protectedness cannot involve an unbounded collection of factors. All source factors outside one eight-position band are genuinely neutral to the failure and may be collapsed or transported independently.

Thus the finite two-skeleton reduction has a stronger form: every obstruction coming from simultaneous commuting choices is already an eight-position local obstruction, even before reducing to squares. Higher-dimensional commuting cubes introduce no new unbounded protection phenomenon.

Braid interactions remain separately local because an A2 braid is supported on three adjacent positions. Therefore every Coxeter-local protection failure in the positive filtration is supported in a uniformly bounded positional neighborhood.
