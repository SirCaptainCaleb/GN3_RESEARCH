# Interior U_11 color-terminal collisions force a linear-size matching of repeated endpoint-path intersections

## Statement

Let v_0v_1...v_k be a simple rainbow terminal-pair path whose parent hyperedges E_s={x_s,v_{s-1},v_s} belong to U_11. Let P_w denote the globally chosen maximum endpoint path with last vertex w, and write R_i=P_{x_i}.

Let M be any family of interior color-terminal collisions x_i=v_j. For each collision, choose one adjacent parent edge F_i in {E_j,E_{j+1}} that is not the last edge of R_i; such a choice always exists. Let c_i be its unique off-x_i contact with R_i. Then
  F_i intersect V(R_i)={x_i,c_i},
and
  |V(P_{x_i}) intersect V(P_{c_i})|>=2.

The M pairs {x_i,c_i} form a loopless multigraph of maximum degree at most seven. Consequently there is a subfamily of at least
  ceil(M/13)
collisions for which the endpoint pairs {x_i,c_i} are pairwise disjoint.

Hence M interior U_11 color-terminal collisions force at least ceil(M/13) endpoint-disjoint pairs of chosen maximum endpoint paths, each pair having at least two common vertices. No edge-rank monotonicity is required.

## Body

Fix a collision x_i=v_j. The two adjacent parent edges E_j and E_{j+1} are distinct, whereas R_i has only one last edge h_i. Choose F_i in {E_j,E_{j+1}} with F_i!=h_i.

Because F_i belongs to U_11 and x_i is a terminal of F_i, its terminal contact multiplicity on R_i is one. Since F_i is not the last edge, this is the actual cardinality
  |(F_i minus {x_i}) intersect (V(R_i) minus h_i)|=1.
Let c_i be the unique vertex in this intersection. Since F_i and h_i both contain x_i, linearity forbids another vertex of F_i from lying in h_i. Hence
  F_i intersect V(R_i)={x_i,c_i},
so c_i!=x_i.

Apply the certified endpoint-overlap lemma bd1e5cb6641b to Q=R_i=P_{x_i} and y=c_i. It gives
  |V(P_{x_i}) intersect V(P_{c_i})|>=2.

Form the loopless multigraph G with one edge {x_i,c_i} for each collision. A fixed vertex w occurs as an owner endpoint x_i for at most one collision because the entrance labels x_i are pairwise distinct.

For contact occurrences, c_i lies in the selected parent edge F_i. A fixed parent edge E_t can be selected only for a collision hitting v_{t-1} or v_t, and each terminal-path vertex is hit by at most one entrance label; hence E_t is selected for at most two collisions. A fixed hypergraph vertex w belongs to at most three parent edges of the simple rainbow terminal-pair path: at most two as a terminal-path vertex and at most one as an entrance label. Therefore w can occur as c_i for at most six collisions. Thus Delta(G)<=1+6=7.

Let N be a maximal matching in G. Every multigraph edge is incident with an endpoint of some edge of N. For a matched edge ab, the union of the incident edge multisets at a and b has size at most
  deg(a)+deg(b)-1<=13.
Therefore
  M=|E(G)|<=13|N|,
so
  |N|>=ceil(M/13).
The collisions represented by N have pairwise disjoint endpoint pairs, and each corresponding endpoint-path pair has at least two common vertices.
