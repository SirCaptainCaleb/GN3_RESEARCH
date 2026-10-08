# Protected physical roots have a graphic matroid rank potential — preserved pre-item development

## Composition

(none yet)

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
