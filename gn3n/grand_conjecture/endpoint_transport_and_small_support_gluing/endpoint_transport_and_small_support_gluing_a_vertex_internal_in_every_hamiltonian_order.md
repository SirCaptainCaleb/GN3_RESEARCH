# A vertex internal in every Hamiltonian order

It remains to consider an augmented support \(K\cup\{x\}\) in which \(x\) is internal in every Hamiltonian order.

Take two such labels \(x,y\) occurring over the same four-vertex support and compare deletion covers of the one- and two-label deletions. If a comparison cover has only one edge joining the path pieces obtained by deleting \(x\) or \(y\) from a Hamilton path, the block-count identity forces that edge to join the two pieces directly; otherwise restoring the deleted label would place it at an endpoint, contrary to the assumption.

With two labels, the same count shows that either at least two such inter-piece edges occur, or the labels occupy adjacent internal positions and every lower deletion cover uses the direct join between the two outer pieces. Comparing the three lower deletion covers in the adjacent case gives either an order disagreement or the same inherited order on all common pieces. In the latter case the one- and two-label deletions form a four-state configuration in which the opposite path is unchanged and all direct joins occur in the same position.

We record this as follows.

**Lemma 7.** If two relevant labels are internal in every Hamiltonian order of their augmented supports, then either
1. a comparison deletion cover has at least two edges joining distinct inherited path pieces;
2. an order disagreement occurs among the lower deletion covers; or
3. the one- and two-label deletion covers preserve one common inherited order and one unchanged complementary path.

The proof is the preceding block count applied successively to the one- and two-label deletions.
