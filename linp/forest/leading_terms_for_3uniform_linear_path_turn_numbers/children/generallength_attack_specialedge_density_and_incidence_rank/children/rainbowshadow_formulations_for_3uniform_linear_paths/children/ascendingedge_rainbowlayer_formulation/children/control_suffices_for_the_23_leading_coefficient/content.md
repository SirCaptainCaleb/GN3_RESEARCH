# Sublinear common-last-vertex control suffices for the 2/3 leading coefficient

## Statement

Let H be an n-vertex P_ell^(3)-free linear 3-graph, let A be the number of ascending edges, and for each vertex v let c(v) be the number of ascending edges for which v is a last vertex. Suppose g is nondecreasing and c(v)<=g(φ(v)) for every v. Then A<=n g(ell-1)/2 and |E(H)|<=((2ell-3)/3+g(ell-1)/6)n. In particular, any uniform bound c(v)=O(φ(v)^alpha) with fixed alpha<1 implies ex_L(n,P_ell^(3))<=(2ell/3+O(ell^alpha))n, and any c(v)=o(φ(v)) gives leading coefficient 2/3.

## Body

Every ascending edge has exactly two last vertices, so 2A=sum_v c(v). Since H is P_ell^(3)-free, φ(v)<=ell-1 for all v; monotonicity of g gives 2A<=n g(ell-1). The ascending-edge accounting inequality gives 3m-A<=sum_v(2φ(v)-1)<=(2ell-3)n. Hence 3m<=(2ell-3)n+A<=((2ell-3)+g(ell-1)/2)n, which is the claimed bound. The power-law and little-o consequences are immediate.