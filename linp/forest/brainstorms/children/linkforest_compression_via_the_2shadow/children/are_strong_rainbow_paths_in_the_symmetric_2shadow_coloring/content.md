# Linear paths are strong rainbow paths in the symmetric 2-shadow coloring

## Statement

Let H be a finite linear 3-uniform hypergraph. Form its 2-shadow G on V(H), and for every shadow edge xy color xy by the third vertex z of the unique hyperedge {x,y,z}. Then this edge-coloring is proper and satisfies the symmetric triangle rule c(xy)=z iff {x,y,z} is a hyperedge, equivalently the triangle xyz has colors z,y,x on xy,xz,yz. A graph path x_0x_1...x_k in G corresponds to a k-edge linear hypergraph path in H if and only if the 2k+1 vertices x_0,...,x_k,c(x_0x_1),...,c(x_{k-1}x_k) are all distinct. Moreover e(G)=3|E(H)|. Consequently H is P_ell-free exactly when this symmetric triangle-colored shadow contains no length-ell path whose path vertices and edge-colors are mutually distinct, and the target |E(H)|<=n ell/3 is equivalent to e(G)<=n ell for this special colored-graph class.

## Body

Well-definedness follows from linearity: a pair xy lies in at most one hyperedge. Properness also follows from linearity. If two distinct shadow edges xy and xw incident with x had the same color z, then the corresponding hyperedges {x,y,z} and {x,w,z} would share both x and z, impossible. If c(xy)=z, then {x,y,z} is a hyperedge, so xz and yz are shadow edges with colors y and x respectively; the converse is the same statement.

Now let x_0x_1...x_k be a graph path and put c_i=c(x_{i-1}x_i). The associated hyperedges are e_i={x_{i-1},x_i,c_i}. If all x_0,...,x_k,c_1,...,c_k are distinct, consecutive e_i,e_{i+1} meet exactly in x_i and nonconsecutive e_i,e_j are disjoint, hence (e_1,...,e_k) is a linear hypergraph path. Conversely, if these e_i form a linear hypergraph path, its k edges contain exactly 2k+1 vertices: the k+1 chain vertices x_0,...,x_k and the k private third vertices c_1,...,c_k. Hence those 2k+1 listed vertices are all distinct.

Finally every hyperedge contributes exactly its three pairs to the shadow, and linearity prevents pair overlap between hyperedges, so e(G)=3|E(H)|.