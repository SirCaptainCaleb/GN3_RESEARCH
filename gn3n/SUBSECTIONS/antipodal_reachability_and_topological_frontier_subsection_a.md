# The antipodal self-intersection criterion

## Metadata

- ID: antipodal_reachability_and_topological_frontier_subsection_a
- Parent Section: antipodal_reachability_and_topological_frontier
- Position: 1
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Composition

Work in the \(\sigma=1\) copy of the memory-lift graph for the auxiliary-vertex extension, and orient every graph edge from lower rank to higher rank. Let \(R\) be the set of states reachable from \(s\) by an increasing path using only red edges.

Because the antipodal involution reverses rank and complements color, \(A(R)\) is exactly the set of states \(x\) from which there is an increasing blue path from \(x\) to \(t\). Indeed, a red increasing path from \(s\) to \(y\) maps under \(A\) to a blue decreasing path from \(t\) to \(A(y)\); reversing it gives a blue increasing path from \(A(y)\) to \(t\), and conversely.

Therefore
\[
\boxed{\text{a red-then-blue pole geodesic exists}
\iff R\cap A(R)\ne\varnothing.}
\]
If \(x\in R\cap A(R)\), concatenate a red increasing path from \(s\) to \(x\) with a blue increasing path from \(x\) to \(t\). Rank increases at every step, so the resulting path has length equal to the pole distance and is automatically geodesic. The converse is immediate from the switch state of any such geodesic.

By the auxiliary-vertex exactification, the grand two-cover conjecture is equivalent to this antipodal self-intersection statement.

## Development

Work in the \(\sigma=1\) copy of the memory-lift graph for the auxiliary-vertex extension, and orient every graph edge from lower rank to higher rank. Let \(R\) be the set of states reachable from \(s\) by an increasing path using only red edges.

Because the antipodal involution reverses rank and complements color, \(A(R)\) is exactly the set of states \(x\) from which there is an increasing blue path from \(x\) to \(t\). Indeed, a red increasing path from \(s\) to \(y\) maps under \(A\) to a blue decreasing path from \(t\) to \(A(y)\); reversing it gives a blue increasing path from \(A(y)\) to \(t\), and conversely.

Therefore
\[
\boxed{\text{a red-then-blue pole geodesic exists}
\iff R\cap A(R)\ne\varnothing.}
\]
If \(x\in R\cap A(R)\), concatenate a red increasing path from \(s\) to \(x\) with a blue increasing path from \(x\) to \(t\). Rank increases at every step, so the resulting path has length equal to the pole distance and is automatically geodesic. The converse is immediate from the switch state of any such geodesic.

By the auxiliary-vertex exactification, the grand two-cover conjecture is equivalent to this antipodal self-intersection statement.
