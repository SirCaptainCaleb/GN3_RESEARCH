# Successive bad five-packets force four cross-endpoint repairs

## Metadata

- ID: successive_bad_five_packets_force_four_cross_endpoint_repairs
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 57
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Lemma. Let A be a four-vertex set and let r,s be two further vertices. If both five-sets A union {r} and A union {s} are non-Hamiltonian, then for every u in A the five-set (A-u) union {r,s} is Hamiltonian.

Proof. In the six-set A union {r,s}, the four-of-six theorem of [[smallset01]] supplies at least four Hamiltonian five-subsets. The two deletions s and r are already non-Hamiltonian, so all four remaining deletions u in A must be Hamiltonian. No assumption that A itself is Hamiltonian is needed. QED.

Tail repair consequence. Let Q=(q_1,...,q_t), t>=4, be a tight path disjoint from A. Suppose A union {q_{t-1}} and A union {q_t} are both non-Hamiltonian. Set T=(q_1,...,q_{t-2}). If any u in A satisfies either
h(q_{t-3},q_{t-2},u)=1
or
h(u,q_1,q_2)=1,
then A union V(Q) has a two-path cover: use the Hamiltonian five-set (A-u) union {q_{t-1},q_t}, and append or prepend u to the actual tight path T. The component orders are 5,t-1.

This applies to the residual same-word double in [[two_bridge_vertices_absorb_a_five_vertex_packet]], with A equal to the absorbed tight three-path together with the remaining exterior vertex. If the five-packet is non-Hamiltonian at two successive terminal positions of Q, every deletion in the four-vertex packet is now available for transfer. Thus one compatible initial or terminal bridge is enough, rather than the two bridges required by the general five-packet test.

Failure of this particular repair has the exact attachment condition, for all u in A,
h(q_{t-3},q_{t-2},u)=0 and h(u,q_1,q_2)=0.
Boundary antisymmetry equivalently supplies the wrong-way hooks
h(u,q_{t-2},q_{t-3})=1 and h(q_2,q_1,u)=1.
These are constraints at both ends of the actual tight tail. They do not permit reversing that tail, and the existence of four Hamiltonian cross-packets does not alone join them to it. This preserves the remaining attachment obligation explicitly.

Once one bridge exists, the resulting two-cover order of the full determining span gives an outward positive-word repair. Frozen-window inherited-mask carriers apply on a fixed ambient source face, as before. The lemma does not resolve the simultaneous wrong-way-hook case or global carrier compatibility.
