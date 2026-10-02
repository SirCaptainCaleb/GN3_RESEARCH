# Two-sided extension of an inherited interval gives a merge or strict quadratic descent

## Statement

Let P=(p_0,...,p_{N-1}) be a path in a boundary tournament and let d lie outside P. Suppose 0<=j<i<=N-1 and both (d,p_j,...,p_i) and (p_j,...,p_i,d) are paths. Then V(P) union {d} is Hamiltonian or it has a two-cover with both path orders at least two. In the latter case replacing P|{d} by this cover strictly decreases the quadratic potential, with all other paths unchanged.

## Body

Put K=V(P) union {d}. If j=0, the order (d,p_0,...,p_{N-1}) is a path: its first triple is supplied by the left extension, and all later triples are inherited from P. If i=N-1, the corresponding right extension gives (p_0,...,p_{N-1},d). Thus assume 1<=j<i<=N-2.

If j>=2, use the two paths (p_0,...,p_{j-1}) and (d,p_j,...,p_{N-1}). The second is tight because its first triple is supplied by the left extension and every later triple is inherited from P. Their orders are j and N+1-j, both at least two.

If i<=N-3, use (p_0,...,p_i,d) and (p_{i+1},...,p_{N-1}). The first is tight because its last triple is supplied by the right extension and all earlier triples are inherited from P. Their orders are i+2 and N-i-1, both at least two.

The only remaining possibility is j=1 and i=N-2. Here N>=4. Use (d,p_1,...,p_{N-2}) and (p_0,p_{N-1}). The former is a path by hypothesis, and the latter is a path because every two-vertex order is a path. Their orders are N-1 and 2.

Every displayed pair is disjoint and covers K. For any resulting orders t and N+1-t with 2<=t<=N-1, the decrease from the original orders N,1 is N^2+1-t^2-(N+1-t)^2=2(t-1)(N-t)>0. No concatenation of two same-end extenders is used.