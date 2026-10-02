# Quadratic potential at a terminal pairwise-repartition state

## Statement

Let C=P_1|P_2|P_3 be a spanning three-path cover in a connected component of the Astra-003 pairwise-repartition graph that contains no two-cover. Define Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2, and choose C with minimum Phi in its connected component. Then for every pair P_i,P_j and every exact two-path cover R|S of H[V(P_i) union V(P_j)], one has |R|^2+|S|^2 >= |P_i|^2+|P_j|^2. Equivalently, ||R|-|S|| >= ||P_i|-|P_j||. Thus each pair of components of a Phi-minimal trapped three-cover is already a minimum-imbalance exact two-cover of its own union.

## Body

# Quadratic potential reduction

For a spanning three-path cover C=P_1|P_2|P_3 define

Phi(C)=|P_1|^2+|P_2|^2+|P_3|^2.

Assume the connected component of C in the pairwise-repartition graph contains no two-cover, and choose C to minimize Phi in that component.

Fix i<j and let R|S be any exact two-path cover of V(P_i) union V(P_j). Replacing P_i|P_j by R|S is one legal Astra-003 move. Because the connected component contains no two-cover, this replacement remains a three-cover, and by minimality of C,

|R|^2+|S|^2+|P_k|^2 >= |P_i|^2+|P_j|^2+|P_k|^2,

where {i,j,k}={1,2,3}. Cancelling the unchanged term gives

|R|^2+|S|^2 >= |P_i|^2+|P_j|^2.

Both pairs have the same total order N=|P_i|+|P_j|=|R|+|S|. For numbers u+v=N,

u^2+v^2=(N^2+(u-v)^2)/2.

Hence the preceding inequality is equivalent to

||R|-|S|| >= ||P_i|-|P_j||.

So at a Phi-minimal trapped state, every current pair realizes minimum possible size imbalance among all exact two-path covers of its union. This converts Astra idea 003 into a terminal-state problem: it is enough to exclude three-covers satisfying these three simultaneous pairwise imbalance-minimality conditions.