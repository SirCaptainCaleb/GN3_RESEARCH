# One path complement bounds sharpen the genuine double corridor profiles — preserved pre-item development

## Every corridor component has at least five vertices

Suppose kappa_2(H[J])=2 and deleting x,y leaves a two-cover P|Q of the corridor C. If |P|<=4, the set V(P) union {x,y} has order at most six. By [[genuine_two_deletion_obstructions_have_no_small_packet_tail_connectors]], some deletion of at most one vertex makes that set Hamiltonian. Its Hamilton path together with Q two-covers J after at most one deletion, contradicting kappa_2=2. Thus |P|>=5, and symmetrically |Q|>=5.

This applies to every two-cover of C, not merely its displayed two-cover. More generally, if P|Q covers H-X with |X|=kappa_2(H)>=2 and one enlarged side V(P) union X has a Hamiltonian support leaving fewer than kappa_2(H) vertices uncovered, that support together with Q contradicts the specified deletion distance. The order-five bound here uses |X|=2 and the universal six-set theorem.

## The monotone corridor

For status word 1^u0^v, C has N=u+v+2 vertices and its three legal displayed cuts are j=u,u+1,u+2. Their path-order pairs are
\[
(u,v+2),\qquad (u+1,v+1),\qquad (u+2,v).
\]
Each component of each cover must have order at least five. Consequently
\[
u\ge5,\qquad v\ge5,\qquad |J|=u+v+4\ge14.
\]
At the first possible monotone order fourteen, the sole exponent pair is u=v=5, with profiles 5|7, 6|6, and 7|5. The earlier lower bound u,v>=4 in [[genuine_two_deletion_corridors_start_at_order_twelve]] is valid but not sharp. In particular the monotone u=v=4 case mentioned in [[mixed_endpoint_packets_exclude_neighboring_shared_bridges]] cannot be a genuine two-deletion instance.

## The single-island corridor

For status word 1^u010^v, C has N=u+v+4 vertices and its unique legal displayed cut is j=u+2. The two path orders are u+2 and v+2. Hence
\[
u\ge3,\qquad v\ge3,\qquad |J|=u+v+6\ge12.
\]
At order twelve only u=v=3 remains, with corridor profile 5|5. The previously allowed pairs (2,4) and (4,2) are excluded by the one-path complement bound.

For that order-twelve residue every six-subset of J must be non-Hamiltonian: a Hamiltonian six-subset would leave a six-vertex complement, which becomes Hamiltonian after one deletion and gives kappa_2<=1. More generally every tight path in an order-n genuine two-deletion instance has order at most n-7.

These are necessary conditions on a fixed instance. They neither impose an upper bound on |J| nor eliminate the remaining island 5|5 residue. The kappa_2=1 repair and the protected carrier-gluing theorem remain open.
