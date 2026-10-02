# Second-layer synchronization fails only in a degree-four shell with a 2K2, P4, or claw core graph

## Statement

In a three-side fixed-defect shell W of threeside01, fix a persistent defect z and let d=deg_Omega(z)>=4. Let N=N_Omega(z), and define Delta_z on N by cc' in E(Delta_z) iff W-{z,c,c'} is Hamiltonian. Then delta(Delta_z)>=d-3. If the inherited long tail T has order at least six and Delta_z has at least four edges, there exist two distinct lower 4|3 corridor states associated with edges of Delta_z whose one-step threesidedescent6 moves can be chosen to land in the same lower potential layer and differ by one legal pairwise repartition. Consequently, failure of such a synchronized second-layer descent in this shell forces d=4 and Delta_z to be exactly one of 2K2, P4, or K1,3.

## Body

Let W be one rooted seven-vertex shell from threeside01, let Omega be its shell graph, fix a persistent defect z, and put N=N_Omega(z), d=|N|=deg_Omega(z). Thus d is one of 4,5,6. Let S=W-{z}, so |S|=6.

Define a graph Delta_z on N by cc' in E(Delta_z) iff W-{z,c,c'}=S-{c,c'} is Hamiltonian.

Fix c in N. Since c is a neighbor of z in Omega, S-{c}=W-{z,c} is Hamiltonian. By 1000924, every Hamiltonian five-set has at least three Hamiltonian four-vertex deletions. Among the five possible deleted labels of S-{c}, at most |S-N|=6-d lie outside N. Hence at least 3-(6-d)=d-3 good deletions are labels c' in N-{c}. For every such c', S-{c,c'} is Hamiltonian, so cc' is an edge of Delta_z. Therefore delta(Delta_z)>=d-3. Hence |E(Delta_z)|>=d(d-3)/2. In particular d=5 gives at least five edges and d=6 gives at least nine; only d=4 can have fewer than four edges.

Let T=(t_1,...,t_M) be the inherited long tail, M>=6. Every edge e=cc' of Delta_z gives a lower corridor cover D_e=K_e|T|R_e, where K_e=W-{z,c,c'} is a Hamiltonian four-set and R_e={z,c,c'} is a Hamiltonian three-set.

Define the endpoint-extension signature sigma(e) subseteq {L,R} by L in sigma(e) iff R_e union {t_1} is Hamiltonian, and R in sigma(e) iff R_e union {t_M} is Hamiltonian.

If sigma(e) and sigma(f) have a common endpoint t, apply the good-endpoint branch of threesidedescent6 to both D_e and D_f using t. Their descendants share T-{t}; their other two components are two Hamiltonian 4|4 partitions of the same eight-set W union {t}. Hence the descendants differ by one legal pairwise repartition, and both descents have the same strict Phi drop 2M-8.

If sigma(e)=sigma(f)=emptyset, apply the bad-bad branch of threesidedescent6 to both states. Their descendants share the inherited interior path (t_2,...,t_{M-1}); their other two components are two Hamiltonian 4|5 partitions of the same nine-set W union {t_1,t_M}. Again the descendants differ by one legal pairwise repartition, and both descents have the same strict Phi drop 4M-20.

Thus synchronization holds whenever signatures intersect or both are empty.

A family of subsets of {L,R} with no such pair has size at most three: there is at most one empty set, and the nonempty sets must be pairwise disjoint, so at most two of them occur. Therefore if Delta_z has at least four edges, two edges synchronize.

If synchronization fails, |E(Delta_z)|<=3. The degree bound rules out d>=5, so d=4. Since delta(Delta_z)>=1, Delta_z is a graph on four vertices with no isolated vertices and two or three edges. With two edges it is 2K2. With three edges it is either P4 or K1,3. These are the only residues.