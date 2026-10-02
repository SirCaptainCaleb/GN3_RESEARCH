# Quadratic minimality reduces Astra trapping to pairwise balance extremality

## Statement

Let C=P_1|P_2|P_3 be a three-component cover in a connected component of the Astra-003 pairwise-repartition graph that contains no cover with at most two components, and suppose C minimizes Phi(C)=sum_i |P_i|^2 in that component. Then for every pair i<j, every exact two-path cover A|B of the induced tournament on V(P_i) union V(P_j) satisfies ||A|-|B|| >= ||P_i|-|P_j||. In particular each displayed pair is a minimum-imbalance exact two-cover of its union. Moreover, in the reciprocal singleton-transfer first form of astra003plateauescape, the certified escape strictly decreases Phi in every branch, so no state on that equality plateau is Phi-minimal.

## Body


# Quadratic potential for the Astra pairwise-repartition graph

For a spanning cover C=P_1|P_2|P_3 with three nonempty tight paths, define
[
Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2.
]

Assume a connected component of the Astra-003 move graph contains no cover with at most two components, and choose a three-component cover
[
C=P_1|P_2|P_3
]
minimizing (Phi) inside that connected component.

Fix (i<j), put (a=|P_i|), (b=|P_j|), and let (A|B) be any exact two-path cover of the induced tournament on (V(P_i)cup V(P_j)), with (c=|A|), (d=|B|). Replacing (P_i|P_j) by (A|B) is a legal Astra move, while the third component is unchanged. Since (a+b=c+d=:s), minimality of (Phi) gives
[
c^2+d^2ge a^2+b^2.
]
But
[
u^2+v^2=rac{(u+v)^2+(u-v)^2}{2},
]
so, because the sums are equal,
[
|c-d|ge |a-b|.
]
Thus the displayed split (P_i|P_j) has minimum possible size imbalance among all exact two-path covers of its union. If that union were Hamiltonian, the legal replacement by one path would already produce a spanning cover with at most two components, contrary to the assumed trapped component. Hence every pair-union is non-Hamiltonian as well.

This gives a useful normal form for a hypothetical trapped Astra component: at a quadratic-potential minimum, all three pairwise induced subtournaments simultaneously carry extremal two-covers, each as balanced as any exact two-cover of that pair-union can be.

Now apply this to the reciprocal singleton-transfer equality plateau certified in astra003plateauescape. The plateau state has component orders
[
(lambda,lambda,1),
]
so
[
Phi_0=2lambda^2+1.
]
The three certified escape branches have orders respectively
[
(lambda-1,lambda-2,4),qquad
(lambda,lambda-3,4),qquad
(lambda-2,lambda-2,5).
]
Their quadratic potentials are
[
2lambda^2-6lambda+21,qquad
2lambda^2-6lambda+25,qquad
2lambda^2-8lambda+33.
]
Therefore the decreases from (Phi_0) are
[
6lambda-20,qquad 6lambda-24,qquad 8lambda-32.
]
Since the reciprocal-one-crossing shell has (lambdage5), all three quantities are positive. Thus every branch of the certified plateau escape is not merely a change of component-size multiset: it is a strict descent of (Phi).

Consequently no reciprocal singleton-transfer equality state can be a quadratic-potential minimum of a trapped Astra-003 move component. Any genuine trapped component must contain a three-cover for which all three pairwise splits are already minimum-imbalance exact two-covers of their pair-unions. This is the next structural target: combine the simultaneous three-pair balance extremality with boundary-tournament crossing/order constraints to force a merge.
