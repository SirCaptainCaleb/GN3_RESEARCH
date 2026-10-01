# Potential-threshold terminal graphs are rainbow-path-free

## Statement

Let H be a finite linear 3-graph with endpoint potential phi. For an integer t>=1, form a graph R_t on the vertices v with phi(v)>=t by adding, for each ascending nonspecial hyperedge e={x,u,v} whose unique entrance is x and satisfies phi(x)<t<=min{phi(u),phi(v)}, the terminal-pair edge uv colored by x. Then this coloring is proper and R_t contains no rainbow path of t edges.

## Body

Properness follows from linearity: two distinct terminal-pair edges incident with the same terminal u cannot have the same entrance color x, since the corresponding hyperedges would share both u and x. Now suppose v_0...v_t were a rainbow t-edge path in R_t. Write e_i={v_{i-1},v_i,x_i}, where x_i is the entrance color of v_{i-1}v_i. The path vertices v_j are distinct and all have phi(v_j)>=t; the colors x_i are distinct and all have phi(x_i)<t. Hence no x_i is any v_j. Therefore e_1,...,e_t are a linear 3-uniform path: consecutive edges meet exactly in v_i and nonconsecutive edges are disjoint. Moreover x_t is a private vertex of the last hyperedge e_t, so this path ends at x_t. Thus phi(x_t)>=t, contradicting phi(x_t)<t. Hence R_t has no rainbow P_t.
