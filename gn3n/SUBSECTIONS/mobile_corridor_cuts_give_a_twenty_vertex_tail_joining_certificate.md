# Mobile corridor cuts give a twenty-vertex tail-joining certificate

## Metadata

- ID: mobile_corridor_cuts_give_a_twenty_vertex_tail_joining_certificate
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 69
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Let a monotone positive double corridor C=(c_1,...,c_N) have status word 1^u0^v, with u,v>=4 and N=u+v+2. Let x,y be its two exterior vertices. The three legal cuts j=u,u+1,u+2 give tight paths P_j=(c_1,...,c_j) and Q_j=(c_N,...,c_{j+1}), both of order at least four.

For any of these covers independently remove either its initial two or its terminal two vertices from P_j, and do the same for Q_j. This gives four choices of a packet
S={x,y} union the two removed vertices from each path,
of order six. The remaining contiguous sequences T,U are tight paths of order at least two.

Apply [[three_bridge_candidates_join_two_tails_and_absorb_a_six_vertex_packet]]. If any v_0 in S both has S-v_0 Hamiltonian and bridges (T,v_0,U) or (U,v_0,T), the full determining span has a two-cover. At least three bridge candidates for any packet suffice automatically by four-of-six. The normalized two-cover gives an outward positive-witness repair.

All twelve packet tests can be determined from the induced tournament on at most twenty vertices:
{x,y},
{c_1,c_2,c_3,c_4},
{c_{N-3},c_{N-2},c_{N-1},c_N},
and {c_{u-3},c_{u-2},...,c_{u+6}}.
Indeed the packets use only original path endpoint pairs. The bridge tests additionally need the initial and terminal pairs after deleting two endpoint vertices. Initial pairs at the far ends use the first or last four corridor vertices; all pairs near the mobile cut have indices from u-3 to u+6. Hamiltonian deletion tests involve only five packet vertices. Overlap among these listed sets can reduce the actual count.

This gives a bounded sufficient certificate with arbitrarily long tails attached. It is not an exhaustive finite reduction and does not assert that some test must succeed.

If the full span has no two-cover, every bridge candidate in each of the twelve tests is necessarily a non-Hamiltonian deletion label of its six-packet. Four-of-six permits at most two such labels. Thus each packet has at most two bridge candidates, and all of them have bad deletions. This implication holds whenever the span has no two-cover, whether its deletion distance is one or two.

In the genuine deletion-distance-two case, there are further simplifications. For the packet consisting of the initial pairs of both paths, neither x nor y can bridge the remaining tails, because their terminal pairs are the original terminal pairs and neither exterior vertex can append to either path. For the packet consisting of both terminal pairs, neither exterior vertex can bridge, because the remaining tails have the original initial pairs and neither exterior vertex can prepend to either path. Hence in each of these two packet types at most two of the four corridor packet vertices are bridge candidates, all with non-Hamiltonian deletions.

The exceptional 010-island corridor has only its unique cut, so it supplies four analogous fourteen-vertex tests, without the three-cut amplification. No direct computation is required by this certificate, and the simultaneous failure conditions are retained as a structural problem. Global compatibility of outward repairs remains separate.
