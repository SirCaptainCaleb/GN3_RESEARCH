# Local strict quadratic descent implies three-cover no-trapping

## Statement

Let H be an n-vertex boundary tournament. Suppose that every spanning three-path cover C of H for which no pair of components has Hamiltonian union admits a legal pairwise repartition to another spanning three-path cover C' with Phi(C')<Phi(C), where Phi is the sum of squared component orders. Then every spanning tight-path cover with at most three components reaches a cover with at most two components by Astra-003 moves. Moreover any sequence that always takes a strict Phi-descent has fewer than n^2/2 strict-descent moves before reaching a two-cover.

## Body

# Local quadratic descent is enough

Define Phi(P_1|P_2|P_3)=|P_1|^2+|P_2|^2+|P_3|^2.

Assume the following local property: whenever C is a spanning three-path cover and no union of two components is Hamiltonian, there is a legal pairwise repartition C->C' with C' again a three-cover and Phi(C')<Phi(C).

Start from any spanning cover with at most three components. If it already has at most two components there is nothing to prove. Otherwise it is a three-cover C.

If some pair of components has Hamiltonian union, replacing that pair by one Hamilton path immediately produces a two-cover. If no pair union is Hamiltonian, the assumed local property supplies a strict Phi-descent to another three-cover. Repeat.

The process cannot continue indefinitely. A legal two-path repartition preserves the total order N of the modified pair. For integers u+v=N one has u^2+v^2 congruent to N modulo 2. Hence the change in the squared-size contribution of that pair is even. Every strict decrease of Phi is therefore at least 2. Also Phi<n^2 for every genuine three-cover with three nonempty components. Thus there are fewer than n^2/2 strict-descent steps before a step with no further three-cover descent is possible. By the local property, that can happen only when some pair union is Hamiltonian, at which point one final move gives a two-cover.

Therefore Astra idea 003 reduces to a local statement: rule out a Phi-local minimum among genuine three-covers by finding either an immediate pair merge or a more balanced exact two-cover of one pair union. The reciprocal singleton-transfer descent theorem verifies this local criterion on one of the presently hardest endpoint residues.
