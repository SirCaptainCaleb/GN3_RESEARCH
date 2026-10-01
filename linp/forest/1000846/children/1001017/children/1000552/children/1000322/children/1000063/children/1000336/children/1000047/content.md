# Saturated boundary fans are degree-two cell graphs with rigid adjacent-cell blockers

## Statement


In a saturated boundary fan, the two-vertex cells C_i=g_i minus g_{i-1} support a degree-two multigraph: double blockers join distinct cells, singleton blockers are labeled half-edges, and in the S=3 case the unique unused blocker is an extra half-edge. Thus the fan is cycles plus one or two open paths pairing the defects. Under the no-safe-rotation hypothesis, an adjacent-cell double blocker joining C_i to C_{i+1} is impossible at the final pair, and otherwise must use the forward joint g_{i+1}∩g_{i+2} in its later cell.


## Body


For i>=2, linearity of Q makes C_i=g_i minus g_{i-1} a two-set, and the cells partition V(Q) minus g_1. A double blocker cannot use both vertices of one cell, so it determines an edge between two distinct cell indices. A singleton blocker becomes a half-edge at the cell containing its blocker. Exact saturation covers every blocker vertex when S=2 and all but one when S=3; mark the latter by an extra half-edge. Every cell then has total incidence two, so the resulting multigraph is a union of cycles and paths. With S=2 there is one open path between the two exceptional singleton labels. With S=3 the four half-edge labels X,Y,Z,U form two open paths, so some open path joins two of X,Y,Z.

Now suppose a double blocker f through the opposite endpoint uses w_i in C_i and w_{i+1} in C_{i+1}. Consider
  g_{i-1},g_{i-2},...,g_1,f,g_{i+1},...,g_{q-1}.
The only possible obstruction is an additional suffix contact of f. The earlier blocker w_i cannot lie in g_{i+1} by linearity. The later blocker w_{i+1} can lie beyond g_{i+1} only in g_{i+2}, and exactly when it is the forward joint g_{i+1}∩g_{i+2}. Hence if C_{i+1} is final, or if w_{i+1} is not that forward joint, the displayed sequence is a safe length-preserving rotation, contradiction. This gives the rigid adjacent-cell rule.
