# The odd closed core is exactly the middle Bier sphere

## Metadata

- ID: the_odd_closed_core_is_exactly_the_middle_bier_sphere
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 268
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Assume a nonempty closed minimum-imbalance deletion core exists in odd order n=2r+1. By [[closed_minimum_cover_cores_force_uniform_half_order_hamiltonicity_and_deletion_critical_middle_sets]], every r-set is Hamiltonian and no Hamiltonian support has order greater than r. Let K be the middle skeleton K={S subseteq V: |S|<=r}. Since n=2r+1, its Alexander dual equals itself: S belongs to K* iff V-S is not in K iff |V-S|>=r+1 iff |S|<=r. Consider the signed support-pair downward-closure complex E(H). A signed face A+ union B- belongs to E(H) iff A and B are disjoint and are contained in disjoint Hamiltonian supports. Under the residue, this is equivalent to |A|<=r and |B|<=r. The forward implication follows from the support-order cap. Conversely, disjoint A,B of these sizes can be enlarged disjointly to r-sets A',B' because |V|=2r+1; both A',B' are Hamiltonian, so they witness the face. Hence E(H)=K *_Delta K*, the deleted join defining the Bier sphere Bier(K). In particular the entire surviving order-free support topology is the canonical (n-2)-dimensional Bier sphere of the self-dual middle skeleton. Thus generic antipodal topology cannot be expected to eliminate the odd closed core: the residue already has exactly the sphere dimension needed to carry the obstruction. Closure in odd order is therefore equivalent to ruling out a boundary-tournament Hamiltonian realization of this middle Bier sphere, i.e. the rank profile 'every r-set Hamiltonian, every (r+1)-set non-Hamiltonian'. This identifies precisely where tournament structure, rather than stronger generic Borsuk-Ulam machinery, must enter.

## Development

Assume a nonempty closed minimum-imbalance deletion core exists in odd order n=2r+1. By [[closed_minimum_cover_cores_force_uniform_half_order_hamiltonicity_and_deletion_critical_middle_sets]], every r-set is Hamiltonian and no Hamiltonian support has order greater than r. Let K be the middle skeleton K={S subseteq V: |S|<=r}. Since n=2r+1, its Alexander dual equals itself: S belongs to K* iff V-S is not in K iff |V-S|>=r+1 iff |S|<=r. Consider the signed support-pair downward-closure complex E(H). A signed face A+ union B- belongs to E(H) iff A and B are disjoint and are contained in disjoint Hamiltonian supports. Under the residue, this is equivalent to |A|<=r and |B|<=r. The forward implication follows from the support-order cap. Conversely, disjoint A,B of these sizes can be enlarged disjointly to r-sets A',B' because |V|=2r+1; both A',B' are Hamiltonian, so they witness the face. Hence E(H)=K *_Delta K*, the deleted join defining the Bier sphere Bier(K). In particular the entire surviving order-free support topology is the canonical (n-2)-dimensional Bier sphere of the self-dual middle skeleton. Thus generic antipodal topology cannot be expected to eliminate the odd closed core: the residue already has exactly the sphere dimension needed to carry the obstruction. Closure in odd order is therefore equivalent to ruling out a boundary-tournament Hamiltonian realization of this middle Bier sphere, i.e. the rank profile 'every r-set Hamiltonian, every (r+1)-set non-Hamiltonian'. This identifies precisely where tournament structure, rather than stronger generic Borsuk-Ulam machinery, must enter.
