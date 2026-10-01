# Incidence-rank spectral identity

## Statement

Let G be a linear 3-uniform hypergraph with m edges, incidence matrix N, and intersection graph F with adjacency matrix A. Then N^T N=3I_m+A, so rank_R N=rank_R(3I_m+A)=m-mult_F(-3). In particular rank_R(3I_m+A)≤|V(G)|.

## Body

For hyperedges e,f, the (e,f)-entry of N^T N is |e∩f|. It equals 3 when e=f, 1 when e≠f and the two hyperedges intersect, and 0 otherwise, because G is linear. Hence N^T N=3I+A. Over R, ker(N^T N)=ker(N), so the ranks are equal. Since 3I+A is symmetric, its nullity is precisely the multiplicity of adjacency eigenvalue -3, giving rank=m-mult_F(-3). Finally rank N is at most its number of rows, |V(G)|.