# A product bound excludes short sides from every two-cover of a pair-union

## Statement

Let F=A|B|P minimize Phi in a connected component of the pairwise-repartition graph containing no cover with at most two paths. Put a=|A|>=3, b=|B|>=3, and c=|P|>=6. If c>(a-3)(b-3)+4, then every two-cover of H[V(A) union V(B)] has both path orders at least four. In particular that union has no Hamiltonian support of order at least a+b-3.

## Body

Write s=a+b and W=V(A) union V(B). Trappedness excludes a Hamilton path on W, since it could replace A|B and give a spanning two-cover together with P.

Suppose W has a two-cover U|V with |U|<=3. If |U|=3 it already has orders 3,s-3. If |U|=2, move one endpoint of V into U: every three-vertex boundary tournament has a Hamilton path, and the remainder of V is contiguous. If |U|=1, take the first two vertices of V together with U as a three-set and retain the suffix of V. Thus W has a two-cover T|R of orders 3,s-3 in all cases. Both orders are positive since s>=6. Replacing A|B directly by T|R is one legal pairwise repartition, irrespective of how the cover T|R was found.

The potential increase in this move is 9+(a+b-3)^2-a^2-b^2=2(a-3)(b-3). Apply threesidedescent6 to T|P, keeping R fixed. Since c>=6, that move decreases Phi by at least 2c-8: its two possible drops are 2c-8 and 4c-20, and the latter is at least the former. Hence the final potential lies below the original by at least 2[c-4-(a-3)(b-3)]>0, contradicting minimality throughout the connected component.

Finally, if W has a Hamiltonian support S of order at least s-3, then its complement has at most three vertices. If the complement is empty W is Hamiltonian, already excluded. Otherwise the complement has a Hamilton path, giving a two-cover with a side of order at most three, also excluded. This proves the last assertion.

The argument is uniform in a,b,c. The cases |U|=1,2,3 are a fixed bounded set of possibilities, not an order-by-order analysis.
