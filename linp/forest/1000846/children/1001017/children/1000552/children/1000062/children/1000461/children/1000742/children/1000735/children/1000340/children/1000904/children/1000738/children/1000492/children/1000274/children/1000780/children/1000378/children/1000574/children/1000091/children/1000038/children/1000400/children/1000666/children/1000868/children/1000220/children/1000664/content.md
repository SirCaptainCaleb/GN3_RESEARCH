# Lens-free flat cycles induce a cycle of unique aligned entrance-rail joints

## Statement

In the setting of 315871ed0c8b, assume the flat terminal cycle is entrance-rail lens-free. Then for every i the adjacent canonical entrance rails R_i and R_{i+1} have exactly one common vertex y_i.

Moreover y_i is an internal joint of both rails at the same index: there is a unique integer
  k_i in {1,...,p-3}
such that
  y_i=r^{(i)}_{k_i} intersect r^{(i)}_{k_i+1}
     =r^{(i+1)}_{k_i} intersect r^{(i+1)}_{k_i+1}.

The joint y_i is not any of
  x_i,x_{i+1},t_i,t_{i+1},t_{i+2}.
Thus the lens-free flat cycle carries a second cyclic datum
  (R_0 --y_0-- R_1 --y_1-- ... -- R_{c-1} --y_{c-1}-- R_0)
whose adjacent intersections are anonymous aligned internal joints with well-defined levels k_i.

## Body

The edges e_i and e_{i+1} are ascending nonspecial edges sharing the terminal t_{i+1}. Their canonical source rails R_i,R_{i+1} therefore intersect by the universal pairwise-intersection theorem for common-terminal source rails (0c885137ea8c).

If R_i and R_{i+1} shared at least two vertices, two consecutive common vertices would bound an elementary lens. Both rails are maximum endpoint paths of the same length p-2, so the lens would be balanced by the standard maximum-rail replacement argument, contradicting the lens-free hypothesis. Hence they have exactly one common vertex y_i.

By 5854d853a44b, a unique intersection of two maximum endpoint paths is an internal joint at the same index on both paths. This gives k_i with 1<=k_i<=p-3.

It remains to exclude the displayed labeled vertices. Each R_i avoids the terminals t_i,t_{i+1} of its own edge, while R_{i+1} avoids t_{i+1},t_{i+2}; hence y_i is none of t_i,t_{i+1},t_{i+2}. The endpoint x_i cannot lie on R_{i+1}, and x_{i+1} cannot lie on R_i, because either entrance-label contact would create a balanced rail-rail lens by c2d109a240a9. Thus y_i is neither entrance endpoint. The cyclic description is now immediate.
