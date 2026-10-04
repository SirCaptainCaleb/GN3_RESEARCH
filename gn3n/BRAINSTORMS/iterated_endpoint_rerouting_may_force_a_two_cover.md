# Iterated endpoint rerouting may force a two-cover

Starting from a two-path cover of H-x in a boundary tournament with pc(H)>2, the omitted vertex forces a local endpoint-rerouting move across the two exposed ends. Conjecture that iterating the forced rerouting possibilities cannot remain locally trapped: the closure of these moves eventually yields a spanning two-path cover.

# Conjecture: endpoint-rerouting closure forces a global extension

Let `H` be a boundary tournament, let `x` be a vertex, and suppose `H-x` has a two-path cover `P|Q`. Whenever the current displayed ends of two tight path pieces cannot absorb `x` directly, [[omitted_vertex_endpoint_rerouting]] gives a forced local alternative: `x` crosses the two exposed endpoints and incorporates the terminal edge of one side into a new tight four-vertex path.

**Conjectural direction.** There is a natural finite state graph of path decompositions obtained by repeatedly applying these endpoint-rerouting moves, together with the obvious path restrictions and reversals. From every initial deletion two-cover `P|Q`, the reachable state space contains a configuration that splices to a spanning two-path cover of `H`.

Equivalently, a hypothetical counterexample should not admit a closed family of deletion-cover states stable under all forced endpoint reroutings.

The intended mechanism is an alternating sequence in which successive failures expose earlier vertices of one or the other path. Such a sequence may behave like an alternating walk through the two paths. The useful theorem would not be the single four-vertex move, which is elementary, but an iteration theorem showing that repeated moves must terminate in a splice or that any recurrence itself yields a splice.

**First tasks.** Define the rerouting state so that one move has an exact invariant description; determine what monotone quantity, if any, measures how far the exposed ends have moved into `P` and `Q`; and analyze the first possible repeated state. A productive target is to prove that a minimal closed orbit of reroutings can be converted into two disjoint tight paths covering all vertices.
