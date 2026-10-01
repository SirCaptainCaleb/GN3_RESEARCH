# Alternative route: one-defect support reconfiguration

## Statement

A direct induction would follow from a no-trapping theorem for near-spanning two-path states: starting from an equitable deletion two-cover plus the omitted vertex, allow coupled repartition/reordering while keeping total longest-path deficit at most one, and prove that the reachable component contains a deficit-zero two-cover.

## Body

# One-defect support reconfiguration

This is an independent full-theorem route.

For a nonempty vertex set T, let L(T) be the maximum order of a tight path in H[T] and put d(T)=|T|-L(T). For a bipartition R|S, define D(R,S)=d(R)+d(S).

Then D=0 means both supports are Hamiltonian and give a spanning two-cover. A state with D<=1 is one path short of a spanning two-cover in the obvious sense.

A direct induction could proceed as follows. Delete a vertex x and take an equitable two-cover of H-x. Assign x to the side required by the next equitable size pattern; this gives a starting support partition with D<=1. Allow support swaps/transfers and arbitrary reordering inside each support, but keep only states with D<=1.

**Proposed closure theorem.** Every connected component of this reconfiguration graph that contains such an addition-start state also contains a state with D=0.

That theorem would imply the grand conjecture by induction. It is unproved. A finite state graph is not enough: one must prove the absence of a trapped D=1 component or exhibit a well-founded descent.

The radius-two exchange obstruction shows why the route must allow a sequence of support changes rather than a universal one-shot local exchange: distance two already fails in an edge-orderable example, while that example can escape through successive swaps.

The route is intentionally independent of the current defect-compression composition, though both ultimately ask for a no-trapping mechanism for local obstruction data.
