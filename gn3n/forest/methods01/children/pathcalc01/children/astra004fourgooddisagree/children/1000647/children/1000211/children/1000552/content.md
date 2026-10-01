# A minimal order-disagreement pair is local or a pure two-arc tight cycle

## Statement

Let H contain order disagreement. Choose disagreeing tight paths P,Q lexicographically minimizing first |V(P) union V(Q)| and then |V(P)|+|V(Q)|. Then at least one of the following holds: (1) P and Q contain a common ordinary edge in opposite directions; (2) there is a tight triple on V(P) union V(Q) reversing an ordered edge of P or Q at an intersection; (3) P and Q share exactly two vertices u,v, are internally vertex-disjoint, and their union is a vertex-simple tight cycle, with P running from u to v and Q from v to u.

## Body

Apply Section 4 of the certified path-intersection calculus pathcalc01. Outcomes (1) and (2) there give conclusions (1) and (2) here. It remains to analyze its cycle construction.

Read the common vertices in their order along Q and choose consecutive common vertices v_i,v_j with i>j in the P-order, exactly as in pathcalc01. Let E be the Q-subpath from v_i to v_j. Its interior contains no vertex of P. In the cycle branch, the two join triples certified in pathcalc01 make a vertex-simple tight cycle Z obtained by traversing E from v_i to v_j and then P forward from v_j through v_{i-1} and back to v_i.

Open Z at the cyclic edge between v_{i-1} and v_i. This gives a tight path
R=(v_i, E^circ, v_j,v_{j+1},...,v_{i-1}),
where E^circ denotes the internal vertices of E in their Q-order. Let
P'=(v_j,v_{j+1},...,v_i).
Then R and P' disagree on the common pair v_i,v_j: R orders v_i before v_j, while P' orders v_j before v_i. Their union is exactly V(Z), a subset of V(P) union V(Q).

By minimality of |V(P) union V(Q)|, equality must hold:
V(Z)=V(P) union V(Q).
Since the interior of E is disjoint from P, any vertex of P outside the interval P' would lie outside Z, impossible. Hence P=P'.

Now E itself and P form a disagreeing pair: E orders v_i before v_j and P orders v_j before v_i. Their union is V(Z), the same minimum union. If Q had any vertex outside E, then replacing Q by E would strictly decrease |V(P)|+|V(Q)| while preserving the minimum union and disagreement, contradicting the secondary minimality. Hence Q=E.

Therefore P and Q meet only at the two endpoints v_j,v_i, their interiors are disjoint, and their opposite traversals form the tight cycle Z. This is conclusion (3).
