# Any two deletion covers share a singleton support-pair lower bound — preserved pre-item development

## Composition

(none yet)

## Development

## Any two normalized deletion covers of a minimum counterexample have a common singleton lower pair

Let H be a minimum-order counterexample. For each vertex x choose a two-cover H-x=A_x|B_x. Normalize it so both supports have order at least two; if one side is a singleton, move an endpoint from the other path onto that side.

Fix distinct holes x,y and work on W=V(H)-{x,y}. Put A=A_x∩W, B=B_x∩W, C=A_y∩W, D=B_y∩W. Since each original support has order at least two, deleting the one additional label leaves A,B,C,D all nonempty.

Form the 2x2 intersection matrix with cells A∩C, A∩D, B∩C, B∩D. Every row and every column has positive total size. Therefore its support bipartite graph has no isolated vertex and hence, in a 2x2 bipartite graph, has a perfect matching. After possibly swapping C,D, choose u∈A∩C and v∈B∩D.

Singletons are Hamiltonian, so ({u},{v}) is a vertex of the singleton-allowed support-pair poset below both deletion-cover states.

Thus every two normalized one-hole support-pair states of a minimum counterexample have a common lower pair of total support two, after the harmless global side swap of one cover.

Equivalently, arbitrary deletion-cover dissimilarity is never a pairwise connectivity obstruction in the singleton-allowed support-pair complex. Every two top-rank deletion-cover vertices are connected by a two-edge poset path through a singleton pair.

The remaining coherence problem begins at triples of deletion covers. In sign language, two bipartitions can always be gauge-aligned so that both sign-agreement classes are nonempty; three bipartitions may have nontrivial Z_2 monodromy. This is where the old negative support-agreement cycles and the equivariant carrier problem naturally meet.
