# Rank the terminal pair by two-cover completion

## Statement

For an ordered terminal pair (u,v), define R(u,v) as the largest size of a vertex set S containing u,v for which H[S] has a tight path ending (u,v) and the complement V(H)-S is Hamiltonian (allow the empty complement). Orient each unordered pair toward the direction with larger R. Conjecture that for every vertex v and rank r, the number of incoming u with R(u,v)=r is O(r) with a constant small enough that summing ranks forces some R(u,v)=n-O(1); the remaining O(1) vertices could then be absorbed by small-set structure to obtain a two-cover.

## Body

Why it might matter globally:
This tries to lift the successful terminal-pair rank argument from a single long path to the actual two-cover objective. A rank bound would be global and order-independent, bypassing the current endpoint-kernel machinery rather than refining it.

Plausible first attack:
Fix v and an equal-rank in-neighborhood X. For each u in X choose an extremal path P_u ending (u,v) with Hamiltonian complement Q_u. Use boundary antisymmetry to orient X by (u,v,w). If u has many outneighbors w outside P_u, appending w shortens the Hamiltonian complement by one; test whether a one-vertex Hamiltonian-deletion lemma for Q_u forces a higher R(v,w). Quantify the obstruction when the deleted complement is not Hamiltonian.