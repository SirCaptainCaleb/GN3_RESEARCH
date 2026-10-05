# No farther witness collapses outer boundary blocks to order two

## Metadata

- ID: no_farther_witness_bounds_relevant_face_blocks_by_four
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 110
- Row version: 3
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

### Boundary footprint bound

In the no-farther-witness branch, every interior face block meeting a determining window has bounded width, while an outer boundary block can occupy at most two positions of the persistent span-two window. Thus the relevant endpoint freedom of a double-persistent carrier is a one- or two-slot reservoir; unbounded exterior block order is irrelevant to the selected witness once the neutral portion is frozen.

## Development

In a double-persistent protected face, assume no chamber has a strictly farther positive witness on the left. Then every status start strictly left of the selected 011 is 1. If a face block straddling the outer boundary had at least three vertices, three consecutive positions of that block would begin at some outward status. Two chambers can place the same three labels there in reverse orders. The outward-ray lemma would force both ordered triples to have status 1, contradicting boundary antisymmetry. Therefore every outer-boundary block has order at most two. The right side is symmetric with forced status 0. Hence, after excluding the farther-witness outcome, a support-changing endpoint factor is exactly a two-vertex A1 swap; a two-slot determining-window block cannot also extend outward. Interior blocks remain of order at most four by the five-position obstruction. This supersedes the weaker boundary order-four estimate in the first version.
