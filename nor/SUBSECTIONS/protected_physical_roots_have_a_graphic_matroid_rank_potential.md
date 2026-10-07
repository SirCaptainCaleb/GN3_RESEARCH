# Protected physical roots have a graphic matroid rank potential

## Metadata

- ID: protected_physical_roots_have_a_graphic_matroid_rank_potential
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 11
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Protected physical roots e_u-e_v carry a graphic-matroid rank potential. Identify each root with the undirected coordinate edge {u,v}. For any retained edge set E, the root-span dimension is |V(E)|-c(E); equivalently the roots are independent exactly when the coordinate edges form a forest.

Thus adjoining a new protected root has a dichotomy: if its endpoints lie in different coordinate components, root-span rank increases by one; if they already lie in one component, the new edge closes a unique graphic circuit relative to a spanning forest. Since rank is at most n-1, repeated protected-root exits cannot produce indefinitely many independent directions.

For a residual antipodal cage, seed the retained set with the inert exchange root e_x-e_y. Each genuine exit root is transverse to this line, so the first exit increases rank. Subsequent exits either continue rank growth or force a signed type-A coordinate circuit.

The sign caveat is essential: a graphic circuit is only a linear signed dependence, not automatically a positive Radon dependence in the orientations supplied by the carrier. Closure therefore reduces to extracting a sign-compatible protected circuit and converting it to a monotone bridge. The first nontrivial case after the antipodal two-cycle is an A2 triangle.

## Development

## Protected physical roots have a graphic-matroid rank potential

Every protected descent certificate has type-A form
[
ho=e_u-e_v.
]
Associate to it the undirected physical-coordinate edge ({u,v}).

### Linear algebra

For any collection E of such roots, the dimension of their span is
[
|V(E)|-c(E),
]
where (c(E)) is the number of connected components of the coordinate graph on the vertices incident with E. Equivalently, a set of protected roots is linearly independent exactly when its underlying coordinate edges form a forest.

Hence, starting from any collection of previously retained protected roots, a new root (e_u-e_v) has exactly two possibilities:

1. (u,v) lie in different coordinate components. Then adjoining the root strictly increases the root-span rank by one.
2. (u,v) lie in the same coordinate component. Then the new edge closes a unique graphic cycle relative to a chosen spanning forest, and the corresponding roots support a type-A signed circuit.

This gives a finite bookkeeping potential for repeated protected-root exits: root-span rank can increase at most (n-1) times before a signed coordinate circuit is forced.

### Relation to antipodal cages

In the residual exact-backtrack cage, the inert exchange root is
[
n=e_x-e_y.
]
Each genuine protected exit supplies a transverse root whose class is nonzero modulo (langle nangle). Thus, if one starts the bookkeeping set with (n), either such an exit increases the accumulated root rank, or it closes a signed coordinate circuit with earlier protected roots.

The local quotient theorem proves the first step is genuinely transverse to the inert line; this lemma records how to continue the bookkeeping globally without pretending that successive quotient codimensions are automatically nested.

### Sign caveat

A graphic cycle yields a signed linear dependence, not automatically a positive Radon dependence in the orientations carried by the encountered states. To obtain an affine/topological zero one still needs sign compatibility. Antipodality supplies the opposite root at the antipodal state, so the signed circuit is the natural oriented-matroid object for the global carrier, but one must not identify an arbitrary graphic cycle with a positive Radon zero without proving that compatibility.

### Closure target

A global protected-root carrier proof may therefore use the lexicographic alternative:
- increase accumulated graphic-root rank; or
- extract a compatible signed circuit inside one Coxeter block.

Since rank is bounded, the unresolved part is reduced to a circuit-extraction theorem. The shortest circuit is the two-root antipodal pair already resolved locally by the caged-braid quotient fill; the next case is an A2 triangle.
