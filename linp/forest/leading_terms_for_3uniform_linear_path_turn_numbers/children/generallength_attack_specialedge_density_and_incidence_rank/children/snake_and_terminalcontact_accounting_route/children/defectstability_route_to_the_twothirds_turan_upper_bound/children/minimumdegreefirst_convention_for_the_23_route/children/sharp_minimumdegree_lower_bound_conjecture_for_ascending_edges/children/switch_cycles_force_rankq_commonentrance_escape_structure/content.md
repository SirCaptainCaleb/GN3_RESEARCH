# Switch cycles force rank-q common-entrance escape structure

## Statement


In the boundary fixed-target entrance rotation graph, a terminal-label switch occurs exactly when the rotating edge blocks at the opposite terminal sigma(P). Such a switch closes the current entrance path into a linear q-cycle C=(g_1,...,g_{q-2},f,h) in which the fixed target edge f={x,y,z} has cycle joints y,z and private entrance x.

For any edge a!=f through x with at most one additional vertex on C, if a is cycle-clean or its unique extra contact is the private vertex of either cycle neighbor of f, then phi(a)>=q. Since phi(x)=q-1 forces every edge through x to have rank at most q, every such favorable ear has rank exactly q and is either special or ascending nonspecial with unique entrance x.

Moreover, among edges through x other than f, if C_0,S,D count those with respectively 0,1,2 non-x contacts on the q-1 edge path C-h, then 2C_0+S>=2. Hence every switch cycle exposes either a clean favorable rank-q ear or at least two distinct one-contact ears; neighboring-private one-contact ears are favorable in the same sense.


## Body


A single-blocker rotation changes the terminal label precisely when its unique blocker is the terminal sigma(P) opposite the predecessor joint tau(P). In that case the rotating edge h meets the old path only in the opposite endpoint a on g_1 and sigma(P) on f, so adjoining h closes the path into a q-edge linear cycle. The two cycle neighbors of f meet f at y and z, leaving x private.

Now let a be another edge through x. If a is clean on the cycle, delete h; the remaining q-1 cycle edges form a path ending in f, and appending a through x gives a q-edge path ending in a. The same argument works when the unique extra contact of a is private on h, since deleting h removes it. If the extra contact is private on g_{q-2}, delete g_{q-2} instead and traverse the complementary q-1 cycle path before appending a through x. Thus phi(a)>=q in all favorable cases.

Because phi(x)=q-1, the certified rank-layer bound gives phi(a)<=q for every a through x. Therefore favorable ears have rank exactly q. If such an edge is nonspecial, the exhibited q-edge witness enters through x, so uniqueness of entrance makes x its entrance; hence it is ascending.

Finally classify the d_H(x)-1 edges a!=f by their number of non-x contacts with P=C-h. Linearity makes their non-x pairs disjoint. Minimum degree gives C_0+S+D>=q-1, while P-f has 2q-4 vertices available for blocker contacts, so S+2D<=2q-4. Subtracting yields 2C_0+S>=2. Thus either a clean ear already exists or at least two one-contact ears do. Combining this count with the favorable-ear criterion isolates the remaining obstruction to one-contact ears whose contacts avoid the private vertices of both cycle neighbors.
