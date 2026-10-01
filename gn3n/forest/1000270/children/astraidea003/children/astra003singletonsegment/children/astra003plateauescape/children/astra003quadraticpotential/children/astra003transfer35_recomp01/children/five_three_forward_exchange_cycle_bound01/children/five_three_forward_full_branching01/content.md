# Every forward three-five exchange edge is fully branching and lies on a six-cycle

## Statement

Let W be an eight-vertex boundary tournament with no Hamiltonian 4|4 partition, and use the forward exchange graph of five_three_forward_exchange_cycle_bound01. For every directed edge X->Y, if Z=W-(X union Y), then the Hamiltonian five-side W-Y=X union Z has Hamiltonian-deletion set exactly X. Consequently Y has all three possible forward successors obtained by deleting an arbitrary two-subset of X from X union Z. In particular every directed edge of the exchange graph lies on an explicit directed six-cycle.

## Body

Let X->Y be a forward exchange and put Z=W-(X union Y)={e,f}. The proof of five_three_forward_exchange_cycle_bound01 shows that the new five-side F=W-Y=X union Z is Hamiltonian and that F-e=X union {f} and F-f=X union {e} are both non-Hamiltonian. It also proves D(F) subseteq X.

Apply two_bad_threecore_opposite_pair_shell01 to the three-set X and exterior labels e,f. For every two-subset P of X, P union {e,f} is Hamiltonian. Equivalently, for every x in X the four-set F-x=(X-{x}) union Z is Hamiltonian. Hence X subseteq D(F). Together with the previous inclusion, D(F)=X. Therefore every two-subset of X is an allowed transfer pair for the next forward exchange from Y.

For the explicit cycle, write X={a} disjoint-union A, Y={d} disjoint-union B, where A,B are two-sets, and retain the leftover pair Z. Starting from X->Y, use full branching successively to choose transfer pairs A, then B, then Z, then A, then B. This gives
X={a} union A -> Y={d} union B -> {a} union Z -> {d} union A -> {a} union B -> {d} union Z -> {a} union A=X.
At each step the chosen transfer pair is a two-subset of the preceding triple guaranteed by the full-branching conclusion just proved. Thus this is a directed six-cycle containing the original edge.
