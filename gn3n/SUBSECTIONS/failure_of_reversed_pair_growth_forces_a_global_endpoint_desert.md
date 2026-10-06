# Failure of reversed-pair growth forces a global endpoint desert

## Metadata

- ID: failure_of_reversed_pair_growth_forces_a_global_endpoint_desert
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 298
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## One-step failure forces a global rooted endpoint desert

Assume the odd uniform residue on n=2r+1 vertices:
every r-set is Hamiltonian and every (r+1)-set is non-Hamiltonian.
Hence the global maximum tight-path order is r.

Suppose an actual maximum path begins
P=(a,b,p_3,...,p_r)
and there is a vertex u distinct from a,b such that
(u,b,a)
is tight. Such an anchored reversed prefix is supplied by
[[a_majority_coloring_closes_universal_endpoint_pair_rigidity_and_yields_an_anchored_three_vertex_prefix]]
unless that theorem has already produced a spanning two-cover.

Assume there is no tight four-path ending with the same ordered pair (b,a).
In particular no vertex z outside {u,b,a} satisfies
(z,u,b)
tight, because then
(z,u,b,a)
would be such a four-path.

Boundary antisymmetry therefore gives, for every
z outside {u,b,a},
(b,u,z)
tight.

This has the following maximum-support consequence.

### Endpoint-desert theorem

Let S be any r-set containing u but not b, and let
R=(u,z,s_3,...,s_r)
be any Hamilton order of H[S] having u as its initial endpoint.

If z is not a, then z is outside {u,b,a}, so (b,u,z) is tight.
Because b is not in S, the word
(b,u,z,s_3,...,s_r)
is vertex-simple and tight of order r+1, contradiction.

Therefore every maximum Hamilton order on an r-support containing u but not b which starts at u must start with the unique vertex a. In particular:

1. If S contains u but neither a nor b, then u is internal in every Hamilton order of H[S].
2. If S contains u and a but not b, then any Hamilton order with u initial has forced initial pair (u,a).

Thus failure to grow the anchored reversed pair from order three to order four is not local. It creates a rooted endpoint desert on every r-support through u avoiding the two blockers a,b.

The terminal analogue is symmetric: failure to extend a three-path with fixed initial pair by one vertex forces the opposite endpoint to be internal on every maximum support avoiding the corresponding two blockers.

## Relation to the rooted-support graph

For the root u, maximum supports on which u is an attainable endpoint form the rooted endpoint family studied in
[[odd_cycles_of_actual_endpoint_paths_force_a_longer_path_without_compatible_insertion_orders]].
The theorem above says that, in the no-growth branch, every such support avoiding b must contain a, and if u is initial then a is forced to be its neighbor.

Equivalently, among r-supports containing u and avoiding {a,b}, the rooted endpoint family is empty. This is substantially stronger than the previously proved bipartiteness of the rooted disjointness graph.

The remaining closure target is now precise: show that the odd-uniform hypothesis forces u to be an endpoint of some Hamiltonian r-support avoiding {a,b}. That single endpoint realization grows the reversed pair to order four or directly produces an (r+1)-path. No bounded-order cutoff is involved.
