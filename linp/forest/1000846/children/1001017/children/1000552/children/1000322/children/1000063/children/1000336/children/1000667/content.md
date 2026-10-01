# Open-chain defects and their ordered locations in saturated boundary fans

## Statement


In the saturated boundary-fan index graph J, the deficit 2-d_J(i) of a cell A_i is exactly the number of its vertices not used by double blockers. Hence open path-component endpoints are precisely the singleton-blocker defects together with the unique uncovered blocker when present. Moreover an X-type singleton defect lies in the final cell A_{q-1}, whereas Y- and Z-type singleton defects lie strictly earlier.


## Body


Each cell A_i has two vertices. A double blocker through the fan center can use at most one vertex from A_i, by linearity with the path edge containing A_i. Thus d_J(i) is exactly the number of A_i-vertices used by double blockers, and 2-d_J(i) counts the unused-by-double-blocker vertices. Exact saturation says these are precisely the singleton-blocker vertices, plus the unique uncovered blocker in the S=3 case. Since J has maximum degree two, its path-component endpoint incidences are exactly those defects. For S=2 the unique open path joins the two exceptional singleton defects; for S=3 the two open paths have endpoints X,Y,Z and the uncovered defect.

The defect labels also have ordered geometry. Because x is the last vertex of Q, it lies in A_{q-1}; hence an X-type singleton blocker is located in the final cell. If a Y-type singleton blocker had its unique blocker w in A_{q-1}, then reversing the prefix through g_{q-2}, appending that singleton edge, and then e would produce a q-edge path ending in e through y, contradicting the unique entrance of nonspecial e. Therefore every Y-defect lies in A_i with i<=q-2, and the same argument applies to Z. Thus X, when present, is pinned at the final index while Y and Z occur strictly earlier.
