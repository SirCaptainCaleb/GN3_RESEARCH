# A global five-side minimum containing a longest path already forces order disagreement

## Statement

Let H be a minimum counterexample and let X|P|Q be a globally Phi-minimal spanning three-cover with |X|=5 and |P|=m>=|Q|=r>=7. If P is globally longest among all tight paths of H, then the order-disagreement alternative of 73b4a2a15831 occurs for every pair of distinct displayed endpoints among P and Q. In particular, a global five-side minimum with no such order disagreement cannot contain a globally longest path as its largest component.

## Body

Fix any two distinct displayed endpoints e,f among P,Q and apply 73b4a2a15831. If its order-disagreement alternative occurs, we are done for this pair. Otherwise its Hamiltonian-six alternative gives a two-cover U|V of the complement H-S whose larger component has order p>=m+1. That component is itself a tight path of H strictly longer than P, contradicting the hypothesis that P is globally longest. Therefore the Hamiltonian-six alternative is impossible for every endpoint pair, and the order-disagreement alternative occurs for all six pairs.