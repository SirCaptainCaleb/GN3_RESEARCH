# A reversal-linked three-label cube has endpoint, support, order, or double-internal top-cover structure

## Statement

Let H be a minimum counterexample. Then there exist distinct vertices u,v,a,x,y,z such that a tight triple containing (v,u) consecutively reverses an ordered edge (u,v) of a tight path, one of (y,u,x,v,z) and (y,v,x,u,z) is a tight Hamiltonian five-path, and with G=H-{u,v} and T={x,y,z}, every state G-S for S subseteq T is non-Hamiltonian with path-cover number two. For this same choice, at least one of the following holds for two-covers of G: (1) some two-cover has two distinct labels of T simultaneously as displayed endpoints; (2) two two-covers of G have different unordered support partitions; (3) two Hamilton paths on one common component support of two covers of G exhibit relative-order disagreement; (4) at least two labels of T are internal in every two-cover of G.

## Body

Choose u,v,a,x,y,z from reversal_stable_shell01. That theorem gives the reversing triple and alternating Hamiltonian five-path. Put G=H-{u,v} and T={x,y,z}. Its stable-family conclusion says G, every G-t, and every G-{s,t} for distinct s,t in T are non-Hamiltonian with path-cover number two. The complement of the displayed Hamiltonian five-set {u,v,x,y,z} is G-T and is also non-Hamiltonian with path-cover number two. Hence all eight states G-S, S subseteq T, are path-cover-two.

Apply pc2_square_topcover_normal01 to the common top state G for each of the three unordered pairs {x,y},{x,z},{y,z}. If any application gives its endpoint outcome, then some two-cover of G has that pair simultaneously as displayed endpoints, giving (1). If any gives support-partition disagreement or relative-order disagreement, we obtain (2) or (3).

Suppose none of (1)-(3) occurs. Then for each pair among x,y,z, pc2_square_topcover_normal01 must give its permanently-internal outcome: at least one endpoint of that pair is internal in every two-cover of G. Let I be the set of labels in T that are internal in every two-cover of G. Every edge of the triangle on T has an endpoint in I, so I is a vertex cover of K_3. Therefore |I|>=2, giving (4).
