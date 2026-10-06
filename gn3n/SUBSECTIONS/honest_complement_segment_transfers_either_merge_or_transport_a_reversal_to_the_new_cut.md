# Honest complement segment transfers either merge or transport a reversal to the new cut

## Metadata

- ID: honest_complement_segment_transfers_either_merge_or_transport_a_reversal_to_the_new_cut
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 202
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let H be a minimum counterexample. Let A=(a_1,...,a_r) be a globally longest Hamiltonian path. Then every z outside A is noninsertable at both ends of A, so
h(a_2,a_1,z)=1 and h(z,a_r,a_{r-1})=1.

Let H-A=P|Q with displayed Hamilton orders, and suppose another two-cover of H-A is an honest one-crossing segment transfer with no order disagreement. Up to exchanging ends and P,Q, write
P=(p_1,...,p_m), 1<=l<m,
T=(q_1,...,q_t,p_1,...,p_l),
R=(p_{l+1},...,p_m),
where T|R is a two-cover of H-A and t>=2.

At the exposed Q-end of T, h(a_2,a_1,q_1)=1. Test h(a_1,q_1,q_2). If it fails, boundary antisymmetry gives
h(q_2,q_1,a_1)=1,
so a_1 externally reverses the initial edge of the comparison path T.

At the other end of T, put z=p_l and let u be its predecessor in T (u=p_{l-1} when l>=2 and u=q_t when l=1). We have h(z,a_r,a_{r-1})=1. Test h(u,z,a_r). If it fails, boundary antisymmetry gives
h(a_r,z,u)=1,
so a_r externally reverses the terminal edge uz of T. For l>=2 this is the inherited internal cut edge p_{l-1}p_l of P.

If neither attachment fails, then
(a_2,a_1,T,a_r,a_{r-1})
is a tight path. Its complement is the union of the two inherited tight intervals
A^o=(a_3,...,a_{r-2})
and R.
If either concatenation A^o R or R A^o is tight, these two paths merge and H has a spanning two-cover. If neither concatenation is tight, the failed-concatenation lemma gives an external reversal at one of the two new residual seams (with the obvious singleton endpoint simplifications).

Thus an honest segment-transfer comparison cannot be a featureless alternative two-cover: either it yields a two-cover of H, or it transports an explicit external reversal to the comparison-path boundary, to the inherited cut edge of P, or to the new residual seam after wrapping T by the two end-edges of A.

The four symmetric segment-transfer orientations satisfy the same conclusion. No small-order bound, cyclic rotation, path reversal, or computation is used.
