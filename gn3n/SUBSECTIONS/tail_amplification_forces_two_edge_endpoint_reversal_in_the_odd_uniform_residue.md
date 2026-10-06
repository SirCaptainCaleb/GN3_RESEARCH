# Tail amplification forces two-edge endpoint reversal in the odd uniform residue

## Metadata

- ID: tail_amplification_forces_two_edge_endpoint_reversal_in_the_odd_uniform_residue
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 292
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Tail amplification across disjoint maximum paths

Assume the odd uniform middle-layer state on
n=2r+1 with r>=3, so every r-set is Hamiltonian and every (r+1)-set is non-Hamiltonian. Let
A=(a_1,...,a_r), B=(b_1,...,b_r)
be vertex-disjoint Hamiltonian r-paths. These are maximum paths.

The universal endpoint-reversal theorem already gives
(b_2,b_1,a_1), (a_2,a_1,b_1), (a_r,b_r,b_{r-1}), (b_r,a_r,a_{r-1})
tight.

In fact reversal propagates one edge farther inward:
(b_3,b_2,a_1), (a_3,a_2,b_1), (a_r,b_{r-1},b_{r-2}), (b_r,a_{r-1},a_{r-2})
are tight.

For the first identity, since b_2 is exterior to A, universal endpoint reversal on A gives (a_2,a_1,b_2) tight. If (a_1,b_2,b_3) were tight, then
(a_2,a_1,b_2,b_3,...,b_r)
would be a vertex-simple tight path of order r+1: the first two triples are the two seams and every later triple is inherited from B. This contradicts maximality. Hence (a_1,b_2,b_3) is non-tight, so boundary antisymmetry gives (b_3,b_2,a_1) tight. Exchanging A,B gives the second identity.

For the terminal identity, universal endpoint reversal gives (b_{r-1},a_r,a_{r-1}) tight. If (b_{r-2},b_{r-1},a_r) were tight, then
(b_1,...,b_{r-2},b_{r-1},a_r,a_{r-1})
would be a tight (r+1)-path. Therefore its boundary reverse (a_r,b_{r-1},b_{r-2}) is tight. Exchange A,B for the fourth identity.

## General seam-tail principle

The proof uses only triple locality plus maximum path order. More generally, let B=(b_1,...,b_t) be a globally maximum tight path. Let R=(u_1,...,u_s) be a vertex-disjoint tight path, s>=2, and suppose for some i<t that (u_{s-1},u_s,b_i) is tight. If i<=s, then (u_s,b_i,b_{i+1}) must be non-tight, because otherwise
(u_1,...,u_s,b_i,b_{i+1},...,b_t)
would be a longer tight path. Hence (b_{i+1},b_i,u_s) is tight. There is a symmetric prefix version.

This is an actual unbounded-gluing mechanism of the type missing from the truncated support countermodel: one bounded seam condition controls an arbitrarily long inherited tail. It does not require compatible Hamilton orders on overlapping supports.

## Consequence for the endpoint frontier

For a fixed maximum path B, any endpoint of a disjoint maximum path carries not merely the exposed-edge reversal from the universal odd-uniform theorem but a two-edge reversal fan into B. Thus any endpoint-availability theorem in the rooted-support graph of [[odd_cycles_of_actual_endpoint_paths_force_a_longer_path_without_compatible_insertion_orders]] immediately supplies stronger positioned seam data than was previously recorded.

A natural global reformulation is to mark, on every Hamiltonian r-support, the vertices attainable as endpoints. For each root a, rooted endpoint supports form a bipartite subgraph of the disjointness graph on (r-1)-subsets of V-a, otherwise the odd-cycle theorem gives an (r+1)-path. Every support has at least two endpoint marks. Proving that these simultaneous rooted bipartiteness requirements are impossible would close the odd-uniform residue. This last marking obstruction is a target, not a proved theorem.
