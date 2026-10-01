# Positive potential-gap terminal graphs are rainbow-path-free and have logarithmic reciprocal mass

## Statement

For t>=1, form the terminal-pair graph R_t^+ from nonspecial edges whose entrance x has phi(x)<t while both terminal potentials are at least t, coloring each terminal pair by x. The coloring is proper and R_t^+ has no rainbow t-edge path. Hence in any P_ell-free linear 3-graph,
  sum_e (1/a(e)-1/p(e)) = O(n log ell)
over all nonspecial edges with entrance potential a(e)<p(e), with the certified bound (9/7)n(1+log(ell-1))+O(n).

## Body

Properness follows from linearity: two terminal-pair edges incident at the same terminal cannot share an entrance color, or the corresponding hyperedges would share two vertices. If v_0...v_t were a rainbow t-edge path in R_t^+, lift its edges to hyperedges e_i={v_{i-1},v_i,x_i}. The terminal vertices all have potential at least t, the distinct entrance colors all have potential below t, and no entrance color equals a terminal vertex. Consecutive lifted edges meet only at the intended terminal and nonconsecutive edges are disjoint. Thus e_1,...,e_t is a linear t-edge hypergraph path whose final entrance color x_t can be chosen as a last vertex, forcing phi(x_t)>=t, contradiction.

For a nonspecial edge with entrance potential a and minimum terminal potential p>a, the edge appears in R_t^+ exactly for integers a<t<=p. Therefore
  1/a-1/p = sum_{t=a+1}^p 1/[t(t-1)],
and summing over edges gives
  sum_e(1/a(e)-1/p(e))
    = sum_{t>=2}|E(R_t^+)|/[t(t-1)].
For t=2, R_2^+ is a matching, so it has at most n/2 edges. For t>=3, the certified rainbow-path extremal bound gives |E(R_t^+)|<((9t+5)/7)n. P_ell-freeness gives t<=ell-1. Summing the resulting harmonic series yields the displayed (9/7)n(1+log(ell-1))+O(n) bound. The threshold method therefore controls all positive entrance-to-terminal potential gaps, though only logarithmically without an additional band relation.
