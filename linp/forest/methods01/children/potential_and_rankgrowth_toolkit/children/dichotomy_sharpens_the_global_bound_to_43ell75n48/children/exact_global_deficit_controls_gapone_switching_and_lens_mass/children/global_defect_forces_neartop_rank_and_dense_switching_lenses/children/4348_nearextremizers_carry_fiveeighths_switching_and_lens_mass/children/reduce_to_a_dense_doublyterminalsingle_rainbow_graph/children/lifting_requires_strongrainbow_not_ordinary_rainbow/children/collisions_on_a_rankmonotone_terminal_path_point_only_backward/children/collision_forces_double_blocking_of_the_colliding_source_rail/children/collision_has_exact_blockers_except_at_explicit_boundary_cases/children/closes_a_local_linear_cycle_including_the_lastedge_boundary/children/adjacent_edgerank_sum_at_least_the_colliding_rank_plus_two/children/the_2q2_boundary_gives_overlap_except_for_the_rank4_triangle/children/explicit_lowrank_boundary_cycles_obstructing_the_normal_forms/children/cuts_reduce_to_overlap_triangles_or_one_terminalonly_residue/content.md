# Near-factor-two collision cuts reduce to overlap, triangles, or one terminal-only residue

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path whose parent hyperedges lie in U_11 and have nondecreasing ranks, with chosen maximum source paths R_i.

At a cut r_t=q, r_{t+1}=2q-3:
1. In the separated plus-three case r_i=2q-3 and r_j=r_{j+1}=q, the later exact contact on R_i is the unique entrance x_s of one adjacent parent edge E_s, and |V(R_i)∩V(R_s)|>=2.
2. Consequently, if M interior color-terminal collisions cross the cut, then either there are at least ceil(M/6) pairwise index-disjoint source-path pairs with at least two common vertices, or at least ceil(M/64) pairwise edge-disjoint linear 3-cycles.

At the next cut r_t=q, r_{t+1}=2q-4, every interior collision again yields adjacent source-path multiple overlap or a local linear 3-cycle, except possibly the single residual rank pattern
r_i=2q-4, r_j=r_{j+1}=q,
where both exact contacts are opposite terminals with disjoint intervals. In that residue the earlier contact lies in {g_{q-4}∩g_{q-3}, private(g_{q-3})} and the later contact lies in {private(g_{q-2}), g_{q-2}∩g_{q-1}} on R_i=(g_1,...,g_{2q-5}).

## Body

For the 2q-3 cut, the separated plus-three contact bounds force the later contact to occur at its maximal singleton position. The stronger opposite-terminal bound is then violated unless this later contact is the unique entrance x_s of its parent edge. Since x_s lies on R_i and R_s ends at x_s, unique-intersection rigidity forbids x_s from being their only common vertex, giving a second intersection.

Classifying all crossing collisions at the 2q-3 cut therefore leaves only overlap certificates and local 3-cycles. Choosing overlap certificates with their adjacent target index gives a graph of bounded degree on path indices, so a constant-fraction matching exists; the triangle branch has the certified constant-factor edge-disjoint packing. This gives the stated M/6 versus M/64 alternative.

For the 2q-4 cut, the universal collision rank floor restricts r_i to 2q-4,2q-3,2q-2. The higher two owner ranks reduce to the already certified tight or plus-three cases. When r_i=2q-4, the adjacent ranks lie in {q-1,q}; the (q-1,q-1) and mixed (q-1,q) cases again reduce to overlap or triangle. Thus only (q,q) remains. If either exact contact is a unique entrance, unique-intersection rigidity again gives multiple source-path overlap. Hence a genuine new residue has both contacts opposite-terminal. The terminal-only singleton window on the host of length 2q-5 leaves exactly five possible central contact intervals; disjoint ordered pairs must take the earlier interval from the first two and the later interval from the last two, yielding precisely the four stated terminal-only patterns.