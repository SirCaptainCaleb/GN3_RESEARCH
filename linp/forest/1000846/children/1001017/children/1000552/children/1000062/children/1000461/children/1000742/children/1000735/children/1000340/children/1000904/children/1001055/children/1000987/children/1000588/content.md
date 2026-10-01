# Global r-uniform bound from ascending incidence and fixed-entrance transfer

## Statement

For every finite linear r-uniform hypergraph, r>=3, let S=sum_v phi(v), let n_+ count nonisolated vertices, let A count nonspecial ascending edges, and let m be the number of edges. Then
r m-A <= (r-1)S-(r-2)n_+.
The fixed-entrance transfer also gives
A <= ((6r-7)S-(6r-13)n_+)/(8(r-1)).
Hence
m <= ((8r^2-10r+1)S-(8r^2-18r+3)n_+)/(8r(r-1)).
Therefore every P_ell^(r)-free linear r-graph satisfies
m <= (((8r^2-10r+1)ell-(16r^2-28r+4))/(8r(r-1))) n.
At r=3 this is m<=((43ell-64)/48)n.

## Body

Fix v and q<=phi(v). A q-edge endpoint path has (r-1)(q-1) vertices outside its last edge. Every other incident edge of rank at most q must meet those vertices, else it appends to the path; by linearity different incident edges use different witnesses. Thus at most (r-1)q-(r-2) incident edges have rank at most q.

For a rank-t edge with at least two possible entrances, all r vertices have endpoint potential at least t. For an edge with unique entrance x, its r-1 terminals have potential at least t and phi(x)>=t-1. Thus exactly one incidence is lost from the preceding local count precisely for an ascending edge. Summation gives
r m-A <= (r-1)S-(r-2)n_+.

For q>=4, dcf886f98a51 gives
|J_q(v)|<=1+floor(((r-1)(q-1)+alpha_r(q-3))/2).
With a=r-2, its exact residue formula satisfies
alpha_r(L)<=((2r-3)/4)L+a.
Therefore
|J_q(v)|<=((6r-7)q+13-6r)/8.
For q=1 there is no ascending edge. For q=2 the fixed-entrance argument gives |J_2(v)|=1. For q=3, all singleton contacts on g_1 are forbidden; at most r-2 singleton contacts remain among 2(r-1) contact vertices, so |J_3(v)|<=1+floor((3r-4)/2), which is at most the same displayed real bound.

Let t(v) count ascending edges terminal at v and choose one of maximum rank q. Then q<=phi(v), so
t(v)<=((6r-7)phi(v)+13-6r)/8.
Each ascending edge has r-1 terminals, hence
(r-1)A=sum_v t(v)<=((6r-7)S-(6r-13)n_+)/8.
Combining with the first inequality yields the stated global bound after simplification. For P_ell^(r)-free H, S<=(ell-1)n_+, giving the final formula.
