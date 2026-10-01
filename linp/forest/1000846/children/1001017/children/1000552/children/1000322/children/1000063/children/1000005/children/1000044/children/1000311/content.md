# Every P4-free linear triple system of minimum degree three is all-special

## Statement

If H is a linear 3-uniform hypergraph with no P_4^(3) and minimum degree at least 3, then every edge of H is special in the snake digraph.

## Body

Let H be a linear 3-uniform hypergraph with minimum degree at least three and no P_4. We prove that every edge is special.

Work in one connected component of the intersection graph F=L(H). By the pathmaker lemma, F has no induced P_4, so F is a connected cograph.

Fix an edge e={x,y,z} of H. Suppose for contradiction that e is nonspecial.

If the vertex e is universal in F, then no induced three-vertex path can end at e, so phi(e)=2 (the component is nontrivial because every point of e has degree at least three). For any desired last vertex, say z, choose x in e\{z} and another hyperedge f!=e through x. Then f,e is a two-edge linear path ending in e with last vertex z. Doing this for each z in e shows e is special, contradiction.

Hence e is not universal in F. Since F is a connected cograph, any two nonadjacent vertices have distance two; choose a hyperedge g disjoint from e and a hyperedge f adjacent to both g and e. Then g,f,e is an induced three-vertex path, so phi(e)=3.

Because e is nonspecial of rank three, all longest paths ending at e have one common entrance label. Rename the vertices so this unique entrance is x; y and z are the two terminal labels.

Let C_y be the set of hyperedges h!=e containing y. Since delta(H)>=3, |C_y|>=2.

First note that no hyperedge disjoint from e can meet a member of C_y. Indeed, if g' is disjoint from e and meets h in C_y, then g',h,e is an induced three-edge-sequence path ending at e through entrance y. Its length is phi(e)=3, contradicting that x is the unique longest-path entrance.

In particular the chosen g is disjoint from every h in C_y.

Also f must meet e at x: if f met e at y or z, then g,f,e itself would be a rank-three path entering e through a terminal label, again contradicting uniqueness.

Write f={x,p,q}. We claim that f meets every h in C_y. Otherwise choose h in C_y disjoint from f. Then
  g - f - e - h
is an induced P_4 in F: the consecutive adjacencies hold; g is disjoint from e and from h; and f is disjoint from h by assumption. This contradicts P_4-freeness.

Thus every h in C_y intersects f. Such an intersection cannot be x, because h and e already meet at y and linearity forbids h from sharing a second point x with e. Hence every h in C_y contains p or q.

Distinct members of C_y cannot both contain p, since they already both contain y; similarly at most one contains q. Therefore |C_y|<=2. Together with |C_y|>=2, there are exactly two such edges, one containing p and one containing q.

Finally g meets f but is disjoint from e, so g∩f is p or q. Suppose g contains p. Let h_p be the unique member of C_y containing p. Then g meets h_p at p, contradicting the earlier fact that no edge disjoint from e can meet a member of C_y. The case g∩f={q} is identical.

This contradiction proves that e is special. Since e was arbitrary, every edge of H is special.
