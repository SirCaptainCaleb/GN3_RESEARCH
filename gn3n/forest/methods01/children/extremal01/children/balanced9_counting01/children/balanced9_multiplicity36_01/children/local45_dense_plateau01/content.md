# Every trapped local four-five plateau contains thirty-six states with synchronized long-endpoint replacements

## Statement

Let H be a boundary tournament and let X|Y|P be a spanning three-cover minimizing quadratic potential within a trapped connected component of the pairwise-repartition graph, with |X|=4, |Y|=5, and P=(p_1,...,p_a) of order a>=7. Put W=X union Y. Then the same trapped component contains at least thirty-six distinct three-covers A|B|P with A union B=W and {|A|,|B|}={4,5}, all having the same minimum Phi. Among these states there are at least sixty one-move reciprocal-swap adjacencies. Moreover, for every such state with |A|=4, at least two distinct x in A satisfy simultaneously that (A-{x}) union {p_1} and (A-{x}) union {p_a} are Hamiltonian, B union {x} is non-Hamiltonian, and at least three y in B make (B-{y}) union {x} Hamiltonian.

## Body

By balanced9_multiplicity36_01, the induced nine-vertex tournament H[W] has at least thirty-six Hamiltonian 4|5 partitions A|B. Replacing X|Y by any such A|B while leaving P fixed is one legal pairwise repartition, so every state A|B|P lies in the same connected component as X|Y|P. Since each has component-order multiset {4,5,a}, all have the same Phi as the original state and therefore are themselves Phi-minimal in that component. Trappedness is inherited because it is a property of the connected component.

By balanced9_swap_density01, among these balanced partitions there are at least sixty Johnson-adjacent pairs; each adjacency is exactly one legal reciprocal one-for-one 4|5 repartition on W with P fixed. Hence these give at least sixty equal-Phi one-move adjacencies among the corresponding three-covers.

Now fix any one state A|B|P with |A|=4 and |B|=5. It satisfies precisely the hypotheses of the certified theorem 8e138afbc628: it is Phi-minimal in the same component and the long path P has order at least seven. Therefore at least two x in A simultaneously satisfy the two long-endpoint replacement conditions, non-Hamiltonicity of B union {x}, and at least three Hamiltonian deletions (B-{y}) union {x}. Since the state was arbitrary, this positioned endpoint package holds at every one of the at least thirty-six equal-Phi states.
