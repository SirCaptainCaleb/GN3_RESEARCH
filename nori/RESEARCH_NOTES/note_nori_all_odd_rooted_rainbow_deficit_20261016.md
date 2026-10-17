# All-dimensional rooted rainbow two-direction obstruction

- Stable ID: note_nori_all_odd_rooted_rainbow_deficit_20261016
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, folded-cube, rainbow, rooted, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_folded_cube_transit_conservation_20261016_r10917

## Research note

THEOREM. For every odd d>=7, the folded d-cube G_d admits a near-balanced orientation and a distinguished root zero whose longest directed path using each generator at most once has length d-2. The bound is attained.

SEVEN-DIMENSION SEED. Use generators (1,2,4,8,16,32,63) on F2^6 and enumerate the 224 undirected edges (u,v), u<v, by increasing u and displayed generator order. The 224-bit orientation mask in big-endian binary is hexadecimal
17a68ed2cb88d34e89e3e0f557b4052ef6ac549e5bec07235767a99a.
A one-bit directs u->v; a zero-bit directs v->u. Complete verification shows 32 vertices of outdegree 3 and 32 of outdegree 4. The number of reachable direction subsets from root zero by rank is (1,3,6,11,11,8,0,0). There is a five-step path with order (5,1,4,0,2) but no six-step path. The corresponding legal antipodally odd ordinary Q7 coloring has a red full geodesic from the same root with direction order (3,1,4,5,6,0,2); the orientation is therefore not a NORI1 counterexample.

UNIFORM PROOF. Write d=7+2k. Represent folded G_d on V=F2^(d-1) with generators h_i=e_i for i<d-1 and h_(d-1)=sum_(i<d-1)e_i. Let g_i=(1,2,4,8,16,32,63) for i=0,...,6. Define a surjective linear map Phi:V->F2^6 by Phi(e_i)=g_i for i<7 and Phi(e_i)=0 for i>=7. The final generator also maps to zero because sum_(i<7)g_i=0. Orient the first seven generators by pulling back the seven-dimensional seed orientation along Phi.

Pair the remaining 2k labels as (7,8),(9,10),...,(d-2,d-1). For each pair (j,j+1) with j+1<d-1 put L_j(x)=x_j+x_(j+1) modulo two; for the final pair put L_(d-2)(x)=x_(d-2). Orient the j-edge outward at x when L_j(x)=0, and the j+1 edge outward when L_j(x)=1. Both generators toggle L_j, so this is a valid oriented four-cycle in each pair, with one outgoing direction per pair at every vertex. The old seven directions contribute three or four outgoing edges and new pairs contribute k, so the full outdegree is 3+k or 4+k, the two permitted values for near balance.

Every directed generator-distinct path from zero projects, after deleting the new pair directions, to a directed generator-distinct path from zero in the seed. At most five old labels and 2k new labels can occur, giving length <=5+2k=d-2. Conversely, take the seed directed five-step path followed by each new pair's two edges consecutively. Each oriented pair can be traversed in two forward steps from every vertex, so this attains d-2.

GENERAL LOWER BOUND. Every near-balanced folded G_(2m+1) admits a directed generator-distinct path of at least m+1 steps from each root. At the endpoint of a maximal path of length r<=m, the last used generator must point inward. At most r-1 of the used generators can point outward, fewer than the minimum outgoing degree m. Some unused generator therefore points outward and extends the path, contradiction.

The construction rules out a proposed rooted path through all but one generator in all odd dimensions >=7. It does not disprove NORI1, because the directed rainbow condition corresponds to an alternating-color geodesic rather than the monochromatic target.

INDEPENDENT AUDIT. Reproducible Python file nori_rooted_rainbow_deficit_family.py checks the seed mask, near balance, direction consistency and rooted maximum lengths 5,7,9,11 for d=7,9,11,13, respectively.
