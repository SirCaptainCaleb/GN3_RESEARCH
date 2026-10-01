# The hard four-side endpoint graph can never be a perfect matching

## Statement

In the setup of four_side_endpoint_matching_bridge01, let E={p_1,p_m} and let J be the graph on the Hamiltonian four-side X in which xy is an edge exactly when E union (X-{x,y}) is Hamiltonian. Then J contains two adjacent edges. Consequently the perfect-matching alternative of four_side_endpoint_matching_bridge01 is impossible: the hard endpoint six-shell always enters its adjacent-edge overlap-amplification branch.

## Body

Let K be the graph on X defined by yz in E(K) exactly when E union {y,z} is Hamiltonian.

The hypotheses of four_side_endpoint_matching_bridge01 include that X is Hamiltonian while X union {p_1} and X union {p_m} are both non-Hamiltonian. Therefore the certified theorem two_bad_five_extensions_adjacent_four01 applies with exterior vertices p_1,p_m and shows that K contains two adjacent edges, say e and f.

For a two-subset A of the four-set X, write tau(A)=X-A for its opposite edge in K_4. By the definition of J,
xy in E(J)
if and only if
E union (X-{x,y}) is Hamiltonian
if and only if
tau({x,y}) is in E(K).
Thus E(J)=tau(E(K)).

The opposite-edge involution tau preserves adjacency of edges of K_4: if two two-subsets of X share one vertex, their complements also share one vertex. Hence the adjacent edges e,f of K map to adjacent edges tau(e),tau(f) of J.

Therefore J necessarily has adjacent edges. In particular J cannot be a perfect matching. The dichotomy in four_side_endpoint_matching_bridge01 consequently always takes its adjacent-edge branch, where the two corresponding Hamiltonian four-windows overlap in three vertices and the certified overlap-amplification theorem 1000715 applies. The fixed-endpoint perfect-matching shell is not a genuine residual configuration.
