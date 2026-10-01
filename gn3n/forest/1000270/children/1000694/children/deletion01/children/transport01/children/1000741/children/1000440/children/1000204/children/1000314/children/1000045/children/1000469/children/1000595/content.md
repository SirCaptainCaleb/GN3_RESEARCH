# Every deletion-cover endpoint gives incompatibility, an isolated compatible edge, or the four-kernel frontier

## Statement

Let H be a minimum counterexample with one chosen deletion cover F_x for each deletion label and full compatibility graph G. Fix an anchor cover F_d=P|Q and let y be any displayed endpoint of P or Q. Then exactly one of the following structural alternatives holds: (1) F_d and F_y are incompatible; (2) dy is a compatibility edge with no common neighbor, equivalently y is isolated in G[N_G(d)]; or (3) dy lies in a compatibility triangle, in which case its unique third label is the inward anchor neighbor of y and the endpoint-triangle cyclic four-kernel frontier of 93109600e88d occurs.

## Body

If dy is not an edge of G, outcome (1) holds. Suppose dy is an edge. By 0f94f3d4dbbb, dy has at most one common neighbor, and any such common neighbor must be the unique inward anchor vertex adjacent to y. If no common neighbor exists, then y has degree zero in the induced neighborhood graph G[N_G(d)], which is outcome (2). If a common neighbor exists, dy lies in a compatibility triangle and 93109600e88d gives the endpoint common-gap cyclic geometry and four-kernel frontier, which is outcome (3). The alternatives are mutually exclusive by definition.