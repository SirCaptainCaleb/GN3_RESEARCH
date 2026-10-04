# Antipodal reachability and the topological frontier

**Summary:** The conjecture becomes an antipodal self-intersection problem for a red reachability region; a counterexample would create an antipodally symmetric separating corridor.

## Statement

In the directed-by-rank single-copy geodesic graph for the auxiliary-vertex extension, let R be the vertices reachable from the source by red edges only. Then A(R) is exactly the set of vertices from which the target is reachable by blue edges only, and a one-change geodesic exists exactly when R intersects A(R). Failure forces a nonempty antipodally invariant corridor separating the two reachable regions.

## Body

## The antipodal self-intersection criterion

Work in the \(\sigma=1\) copy of the memory-lift graph for the auxiliary-vertex extension, and orient every graph edge from lower rank to higher rank. Let \(R\) be the set of states reachable from \(s\) by an increasing path using only red edges.

Because the antipodal involution reverses rank and complements color, \(A(R)\) is exactly the set of states \(x\) from which there is an increasing blue path from \(x\) to \(t\). Indeed, a red increasing path from \(s\) to \(y\) maps under \(A\) to a blue decreasing path from \(t\) to \(A(y)\); reversing it gives a blue increasing path from \(A(y)\) to \(t\), and conversely.

Therefore
\[
\boxed{\text{a red-then-blue pole geodesic exists}
\iff R\cap A(R)\ne\varnothing.}
\]
If \(x\in R\cap A(R)\), concatenate a red increasing path from \(s\) to \(x\) with a blue increasing path from \(x\) to \(t\). Rank increases at every step, so the resulting path has length equal to the pole distance and is automatically geodesic. The converse is immediate from the switch state of any such geodesic.

By the auxiliary-vertex exactification, the grand two-cover conjecture is equivalent to this antipodal self-intersection statement.

## The neutral corridor forced by a counterexample

Assume for contradiction that \(R\cap A(R)=\varnothing\). Put
\[
N=V(\Gamma)\setminus(R\cup A(R)).
\]
Then \(A(N)=N\), so \(N\) is antipodally invariant.

Moreover there is no edge, in increasing-rank direction, directly from \(R\) to \(A(R)\). Such an edge cannot be red, because its upper endpoint would then lie in \(R\); and it cannot be blue, because its lower endpoint would then have a blue increasing route through the upper endpoint to \(t\), placing it in \(A(R)\). Since the underlying ranked graph connects the poles, every pole-to-pole path must therefore pass through \(N\). In particular \(N\ne\varnothing\).

The colors on the two interfaces are forced. Any increasing edge from \(R\) to \(N\) is blue, while any increasing edge from \(N\) to \(A(R)\) is red. The antipode exchanges these two frontiers. Thus a counterexample produces an antipodally symmetric separating corridor with opposite prescribed colors on its lower and upper boundary.

This is substantially more rigid than the bare failure of one chosen geodesic. It turns the conjecture into a separation problem in a fixed antipodal ranked complex.

## What a topological proof must actually show

The current topology program is therefore not “find any antipodal path.” It is to rule out the antipodally invariant corridor \(N\) in the ranked memory lift arising from a boundary tournament extension.

Three constraints must be preserved simultaneously:

1. **Distinguished poles.** The output must connect the prescribed source and target, not an arbitrary antipodal pair.
2. **Geodesicity.** Rank must increase at every step, equivalently every original coordinate/vertex is used exactly once.
3. **Memory compatibility.** Edge color in the lift represents a triple of successive cube directions, so a theorem on ordinary cube-edge colorings cannot be applied without carrying the two-step state.

The staircase link supplies an antipodal \((n-2)\)-sphere of permutations, while the reachability criterion supplies an antipodal separation \(R\mid N\mid A(R)\). A plausible closure route is to convert this separation into an antipodal labeling or continuous odd map on the link and then show that Tucker/Borsuk-Ulam/Sperner-type parity forces a forbidden self-intersection or a simplex encoding a red-blue geodesic switch.

What remains unproved is precisely that last implication. The corridor formulation is intended to make the needed topological statement sharp enough to attack directly.

## Relation to the Norine geodesic analogy

The conceptual analogy with antipodal cube-coloring problems remains useful but should be stated at the right level. In both settings, the desired object is an antipodal geodesic constrained to use each coordinate exactly once, and the staircase triangulation turns the family of such geodesics into a simplicial decomposition indexed by permutations.

The strengthened Norine-style intuition—seek an antipodal path whose coordinate directions are all used exactly once—matches exactly the role of geodesicity here. What is special in the present problem is that the coloring is induced by consecutive triples of directions and therefore naturally lives on the memory lift rather than on the bare cube.

The strongest transferable idea is thus not a literal theorem statement but the topological architecture: antipodal symmetry, a sphere of geodesic order types, and a parity/fixed-point mechanism that should prevent an antipodal separation compatible with all local labels. The reachability corridor identifies the concrete separation that such a mechanism would need to forbid.

## Metadata

- ID: antipodal_reachability_and_topological_frontier
- Kind: section
- Version: 12
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 4: The antipodal self-intersection criterion
- Subsection 2 — crystallized, version 4: The neutral corridor forced by a counterexample
- Subsection 3 — crystallized, version 4: What a topological proof must actually show
- Subsection 4 — HOT, version 3: Relation to the Norine geodesic analogy
