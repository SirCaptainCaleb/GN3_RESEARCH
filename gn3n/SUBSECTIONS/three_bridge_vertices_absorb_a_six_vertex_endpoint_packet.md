# Three bridge vertices absorb a six-vertex endpoint packet

## Metadata

- ID: three_bridge_vertices_absorb_a_six_vertex_endpoint_packet
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 48
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["reflected_double_carriers_reduce_to_two_bounded_rooted_endpoint_interfaces", "correction_seven_set_endpoint_absorption_needs_oriented_endpoints", "smallset01"]

## Cold composition

(none yet)

## Development

Let T=(x,y,z,...) be a tight corridor path and let A be six vertices disjoint from T. If at least three vertices t in A satisfy (t,x,y) tight, then A union V(T) has a two-cover. Indeed, by the audited four-of-six theorem at least four vertices t in A have A-t Hamiltonian. The bridge-good set has size at least three, so it intersects the good-deletion set. Choose t in the intersection. Then (t,x,y,z,...) is tight and A-t is Hamiltonian, giving the required two-path cover. Thus the reflected-double endpoint problem does not require an oriented prescribed-endpoint theorem: it suffices to prove three bridge-good packet vertices. Failure has the sharply opposite form that at least four packet vertices satisfy (t,x,y) non-tight, equivalently (y,x,t) tight by boundary antisymmetry.
