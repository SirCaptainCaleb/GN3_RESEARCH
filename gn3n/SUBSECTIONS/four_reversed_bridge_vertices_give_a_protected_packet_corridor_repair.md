# Four reversed bridge vertices give a protected packet-corridor repair

## Metadata

- ID: four_reversed_bridge_vertices_give_a_protected_packet_corridor_repair
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 55
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Lemma. Let A be a four-vertex set, let y be another vertex, and let Z=(z_1,...,z_d), d>=2, be disjoint from A union {y}. Suppose Q_0=(z_d,...,z_1) is a tight path and h(u,z_1,z_2)=0 for every u in A. Then H[A union V(Z) union {y}] has a two-path cover with component orders 4,d+1. One component contains y and three vertices of A; the other is Q_0 followed by the remaining vertex of A.

Proof. There is a Hamiltonian four-set K contained in A union {y} and containing y. For an explicit citation, choose a tight order on any three vertices of A (boundary antisymmetry always supplies such an order), and use the prescribed-exterior-endpoint lemma in [[localextend01]] with the fourth vertex of A and the prescribed vertex y. It produces a Hamiltonian support of order four or five with y as an endpoint. In the five-vertex case delete the endpoint opposite y to obtain K of order four. This argument never reverses a tight path and does not require a prescribed terminal orientation.

Write A union {y}-K={r}, so r is in A. The bridge hypothesis and boundary antisymmetry give h(z_2,z_1,r)=1. Consequently Q=(z_d,...,z_1,r) is tight, while any Hamilton order on K is tight. These two paths partition the specified vertex set. QED.

Protected surgery consequence. Suppose J=[a,b+4] is the full determining span of a selected positive span-two double in a protected chamber, and its vertices admit such a packet/corridor decomposition A,Z,y. Replace its order by (K,Q^{rev}). Its internal status word avoids 001,011,0101 because it is a two-cover order. All positive determining windows at depth at most the selected edge lie inside J. Therefore the new chamber lies at strictly greater witness depth; crossing-boundary windows are farther outward.

Application to [[arbitrarily_large_boundary_blocks_can_change_the_selected_positive_witness_sign]]. Let A be the four block vertices occupying positions a,...,N, let Z=(z_1,...,z_d), and let y=z_{d+1}=v_{b+4}. All internal statuses of Z are zero, so Q_0=Z^{rev} is tight. The construction supplies h(u,z_1,z_2)=0 for every u in A. The lemma therefore gives an explicit 4|(d+1) two-cover of J, for every chamber in that family. The first component absorbs the far right endpoint; the remaining block vertex moves to the terminal end of the reversed singleton corridor.

On a fixed ambient source face, select one reference chamber and one such repair, freeze the whole repaired interval J, and use inherited masks of exterior components disjoint from J as in [[frozen_window_carriers_and_separator_relabeling_require_precise_invariants]]. The resulting carrier is protected and contractible. In this family the entire large boundary block meets J, so its generators are collapsed. Its unbounded source rank is not itself an obstruction to a protected local carrier.

The bridge lemma is sufficient, not universal. It needs all four reverse bridges to the terminal pair of Q_0, and applies to a long corridor only when that reversed corridor is actually tight. A general mixed double can have two substantial corridor paths and need not satisfy either condition. Global compatibility of chosen packet decompositions and normalized carriers across ambient source faces also remains unproved.
