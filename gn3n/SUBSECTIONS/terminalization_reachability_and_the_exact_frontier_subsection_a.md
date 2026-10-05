# Current closure frontier

## Metadata

- ID: terminalization_reachability_and_the_exact_frontier_subsection_a
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 1
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

The geodesic program now has a sharply separated finite and global structure.

### What is already closed

The exact status-word theory gives local forbidden witnesses. The witness-path topology gives positive balanced carrier faces. The finite classification in [[local_witness_topology_and_the_finite_terminal_theorem]] proves:
[
oxed{	ext{every terminal local-witness support is two-coverable}.}
]

Thus there is no remaining finite terminal obstruction to classify. Centered witnesses, overlapping reflected witnesses, double witnesses, and disjoint single-sided branches have all been reduced to explicit finite supports and closed.

The exact-root route independently reaches the same bounded scale: nonzero recurrent carriers have a central block of order at most four and at most ten determining vertices.

### The missing global implication

Let (C) be a positive balanced carrier for the fixed-path local-witness map, and let (e) be the innermost witness edge appearing among chamber labels. Then all chambers are protected from witness edges closer to the center, both orientations (+e) and (-e) occur, and face-product splicing may produce chambers in which (e) disappears and the selected witness moves farther outward.

The missing point is that an improved chamber is not automatically an improved **balanced carrier**. Convex cancellation may still use other chambers labeled by (e).

**Terminalization theorem.** From a positive balanced carrier with innermost witness edge (e), either obtain a spanning two-cover directly, obtain one of the already classified terminal finite supports, or construct a new positive balanced carrier whose chamber labels all lie strictly farther outward than (e).

Iteration would terminate because the witness path is finite. Together with the finite terminal theorem, this would prove the grand conjecture.

### Relative-index formulation

The natural topological model is a relative separator problem. The (+e) and (-e) chamber regions are separated by configurations in which the (e)-witness is absent. On that (e)-free locus, the remaining witness coordinates lie on the outer subpath.

The desired mechanism is a relative (mathbb Z_2)-index or Bourgin--Yang recursion:
[
	ext{balanced carrier index}
longrightarrow
	ext{index retained on the }e	ext{-free separator}
longrightarrow
	ext{zero of the outer witness map}.
]

The technical issue is that an individual carrier face need not be antipodally invariant, and a barycentric zero may cancel (+e) and (-e) contributions without containing an actual chamber where (e) is absent. The finite mixed-cell classification should be used precisely here: if cancellation across (e) occurs without a genuine separator chamber, the responsible cell should already fall into one of the closed finite support types.

This is now the principal research target.

### Relation to antipodal reachability

The earlier exact reachability formulation remains valid:
[
operatorname{pc}(H)le2
quadLongleftrightarrowquad
Rcap A(R)	ext{ is nonempty}
]
in the auxiliary memory lift. Its neutral corridor is best viewed as a global analogue of the witness-carrier separator.

The current witness topology is more economical because it compresses the obstruction before attempting reachability intersection. A successful terminalization theorem would effectively resolve the relevant neutral-corridor obstruction without proving a separate reachability theorem.

Thus antipodal reachability is no longer an independent branch that must be closed after terminalization; it is an alternate language for the same global separator phenomenon.

### Exact status of the grand conjecture

The proof architecture is
[
	ext{counterexample}
Longrightarrow
	ext{balanced local-witness carrier}
Longrightarrow
egin{cases}
	ext{terminal finite support},\
	ext{or an outward escape}.
end{cases}
]

The first branch is closed by the finite terminal theorem. The second branch is what terminalization must convert into a new balanced carrier or a direct two-cover. Accordingly
[
oxed{
	ext{terminalization}
+
	ext{the proved finite terminal theorem}
Longrightarrow
operatorname{pc}(H)le2.
}
]

No separate solution of the old omission-facet, zero-root, neutral-corridor, or disturbance branches would then be required.

### Proof-transfer program toward generalized Norine

The eventual terminalization proof should be audited for portability. The chamber topology, antipodal symmetry, witness-tree compression, and relative-index recursion appear substantially less dependent on GN3 translation invariance than the block-swap and splicing lemmas.

This motivates the independent meta-conjecture recorded in [[meta_conjecture_gn3_closure_should_seed_generalized_norine]]: a substantial core of the eventual boundary-tournament proof should seed a generalized bounded-memory Norine geodesic theorem. That program is deliberately kept separate from the proof of the present conjecture, but the distinction between portable topology and GN3-specific face combinatorics should be tracked as the terminalization argument is developed.
