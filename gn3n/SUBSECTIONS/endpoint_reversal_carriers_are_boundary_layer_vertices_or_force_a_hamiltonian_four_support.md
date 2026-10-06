# Endpoint-reversal carriers are boundary-layer vertices or force a Hamiltonian four-support

## Metadata

- ID: endpoint_reversal_carriers_are_boundary_layer_vertices_or_force_a_hamiltonian_four_support
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 205
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let A and M be vertex-disjoint tight paths. Write A=(a_0,a_1,...,a_r) and M=(m_0,...,m_t). First suppose w=m_j reverses the displayed initial edge a_0a_1 of A, so h(a_1,a_0,w)=1. If j>=2, then M supplies h(m_{j-2},m_{j-1},w)=1. Boundary antisymmetry at middle vertex w gives exactly one of h(a_0,w,m_{j-1}) and h(m_{j-1},w,a_0). In the first case (a_1,a_0,w,m_{j-1}) is a tight Hamiltonian four-path. In the second case (m_{j-2},m_{j-1},w,a_0) is a tight Hamiltonian four-path. Hence, unless a Hamiltonian four-support already exists, every vertex of M reversing the initial edge of A lies among m_0,m_1. Symmetrically, suppose w=m_j reverses the displayed terminal edge a_{r-1}a_r of A, so h(w,a_r,a_{r-1})=1. If j<=t-2, then M supplies h(w,m_{j+1},m_{j+2})=1. Exactly one of h(m_{j+1},w,a_r) and h(a_r,w,m_{j+1}) is tight. The first gives the Hamiltonian four-path (m_{j+1},w,a_r,a_{r-1}); the second gives (a_r,w,m_{j+1},m_{j+2}). Therefore, outside the Hamiltonian-four-support branch, every carrier on M reversing the terminal edge of A lies among m_{t-1},m_t. This is a positional compression of the external-reversal interface: initial-edge reversers occur only in the first two vertices of the carrier path, and terminal-edge reversers only in its last two.

## Frontier

- Development version when composed: None
- Development version now: 1
