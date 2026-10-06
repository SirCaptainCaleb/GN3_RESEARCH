# Two aligned ordered edge cuts splice arbitrarily dissimilar deletion covers

## Metadata

- ID: two_aligned_ordered_edge_cuts_splice_arbitrarily_dissimilar_deletion_covers
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 220
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Two aligned ordered-edge cuts splice arbitrarily dissimilar deletion covers

Let F_a=P_1|P_2 be a tight two-cover of H-a and F_b=R_1|R_2 one of H-b, with a!=b. Pair the paths in either order.

Choose cuts
P_i=L_i T_i, R_i=M_i N_i (i=1,2)
such that L_i and M_i both end in the same ordered pair (u_i,v_i). Thus those prefixes have at least two vertices. Empty tails are allowed.

Suppose their prefix supports satisfy the single set identity
V(L_1) union V(L_2) = (V(M_1) union V(M_2)) union {b}.
Then
(L_1,N_1) | (L_2,N_2)
is a spanning two-cover of H.

Proof. The prefix identity implies a is not in either M_i: the left side belongs to H-a. It also implies b belongs to one L_i. Write B=V(M_1) union V(M_2). The chosen left prefixes partition B union {b}; the chosen right tails, taken from the cover of H-b, partition V(H)-(B union {b}). Hence the new paths are vertex-disjoint and span H.

Each new path is tight. Its prefix is tight because it is inherited from P_i; its suffix is inherited from R_i. At their junction, the final ordered pair of L_i equals that of M_i, so every new triple crossing the cut is already a consecutive triple of R_i. In particular (u_i,v_i,first N_i), and when defined (v_i,first N_i,second N_i), are inherited. This proves the claim.

Equivalently, after removing the differing hole labels, the two covers need only admit cuts with the same prefix vertex set and the same two ordered boundary edges. No agreement of entire path supports, common relative orders away from the boundary, or contiguity of any support intersection is required. The number and sizes of crossing intersection blocks can be arbitrary.

Thus in a no-two-cover state, for every pair of deletion covers and every pairing of their paths, no such cut can separate the two holes while matching the prefix set and the ordered boundary pairs.

This is a direct conversion criterion for dissimilar covers, not a claim that an aligned cut always exists. It separates the actual remaining obligation from generic disagreement certificates: one must force this simultaneous set-and-edge alignment, or exploit the obstruction to it. The boundary interface uses only two ordered pairs, while the prefix-set condition retains the global incidence information that local triple tests cannot replace.

This generalizes [[crossing_deletion_covers_close_by_ordered_overlap_and_a_contiguous_complementary_intersection]] in a different direction: fragmentation is allowed everywhere, provided the paired cuts satisfy the stated global prefix identity.
