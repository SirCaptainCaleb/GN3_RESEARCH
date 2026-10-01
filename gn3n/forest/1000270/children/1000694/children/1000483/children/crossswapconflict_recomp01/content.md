# Cross-swap clause conflicts occur only along central anti-diagonals

## Statement

Fix displayed paths A=(u_0,...,u_m), B=(v_0,...,v_s) and omitted label c. Across all interior pivot cells, the six alternatives in the two pivot-pivot cross-swap clauses are locally jointly consistent except for one family of reversal conflicts: the central c-containing literal of C1(i,j) reverses the central literal of C2(i-1,j+1), and symmetrically the central literal of C2(i,j) reverses that of C1(i+1,j-1). No side literal reverses any clause literal or inherited path triple. Hence every diagonal central conflict forces at least one c-free side alternative from the two overlapping clauses, and the induced cell-conflict graph is a union of anti-diagonal paths.

## Body

Within one pivot cell, all six clause alternatives may be tight simultaneously because no pair are reversals and none reverses an inherited path triple. Across cells, reversal preserves the middle vertex. Thus only central literals can conflict with central literals: solving rev(v_{j+1},c,u_i)=(u_i,c,v_{j+1}) identifies C2(i-1,j+1), and the symmetric equation identifies C1(i+1,j-1). Side literals have middle in A or B and incompatible endpoint-class/index patterns under reversal, so no side-side or central-side collision occurs. Therefore the only conflict graph edges join diagonally adjacent cells. At such an edge the two central alternatives cannot both be tight; whichever central alternative fails forces one of the two c-free side alternatives in its clause, giving the asserted side bridge.
