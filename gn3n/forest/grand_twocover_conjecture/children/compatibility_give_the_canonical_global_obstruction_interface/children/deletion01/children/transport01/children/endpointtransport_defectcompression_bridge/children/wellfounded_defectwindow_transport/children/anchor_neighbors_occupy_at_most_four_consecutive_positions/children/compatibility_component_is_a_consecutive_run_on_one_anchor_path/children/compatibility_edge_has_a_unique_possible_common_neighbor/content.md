# An endpoint-labeled compatibility edge has a unique possible common neighbor

## Statement

Let H be a minimum counterexample. Choose one deletion cover F_x of H-x for each deletion label under consideration, and let G be the full compatibility graph. Suppose dy is an edge of G and y is an endpoint of one displayed path of the anchor cover F_d. If z is a common neighbor of d and y in G, then z is the unique anchor vertex immediately adjacent to y on that displayed path. In particular d and y have at most one common neighbor, so every compatibility edge from an anchor label to one of its displayed endpoints has codegree at most one.

## Body

Let z be a common neighbor of d and y. Then y,z both lie in N_G(d), and yz is an edge of the induced graph G[N_G(d)]. By 689b439cc429, every such neighborhood edge joins consecutive vertices on one displayed anchor path of F_d. Since y is an endpoint of that anchor path, there is only one anchor vertex consecutive to y, namely its unique inward neighbor. Therefore z must be that vertex. Hence there is at most one possible common neighbor z, and the compatibility edge dy has codegree at most one.