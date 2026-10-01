# The hard endpoint-pair grid forces order disagreement on five vertices

## Statement

Continue the setting of a71e5571d6a2. Let y,z,w be any three distinct vertices outside P. For each unordered pair {a,b} among {y,z,w}, exactly one of (a,p_m,b) and (b,p_m,a) is tight, and a71e5571d6a2 supplies the corresponding Hamilton path (a,p_m,b,p_0) or (b,p_m,a,p_0). Then two of these three Hamilton four-paths have order disagreement on their common vertices. Consequently the unresolved endpoint-reversal residue always contains two Hamiltonian four-paths supported on at most five vertices that order a common pair oppositely.

## Body

Orient the ordinary complete graph on {y,z,w} by a->b exactly when (a,p_m,b) is tight. Boundary antisymmetry makes this a tournament: for every pair {a,b}, exactly one of (a,p_m,b) and (b,p_m,a) is tight. Every tournament on three vertices has a vertex z with one incoming and one outgoing incident arc; after relabeling, y->z and z->w. By a71e5571d6a2 the corresponding Hamilton paths are R=(y,p_m,z,p_0) and S=(z,p_m,w,p_0). Their common vertices include z,p_m,p_0. In R, p_m precedes z, whereas in S, z precedes p_m. Thus R and S have order disagreement on the common pair {z,p_m}. Their union is contained in {p_0,p_m,y,z,w}, so the disagreement is supported on at most five vertices. No path reversal or cyclic permutation is used.