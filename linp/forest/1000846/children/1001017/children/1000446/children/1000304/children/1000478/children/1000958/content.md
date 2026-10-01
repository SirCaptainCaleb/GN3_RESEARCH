# Unbounded common-last-vertex degree for ascending edges

## Statement

For every r>=1 there is a finite linear 3-graph containing r+1 ascending edges with a common last vertex. Consequently no absolute bound of the form a(v)<=C+h(v) can hold pointwise, even with h(v)=0.

## Body

Construction. Let L=6*2^(r-1). Take a 3-uniform linear path Q=(E_1,...,E_L), with E_i={a_{i-1},b_i,a_i} and all displayed vertices otherwise distinct. Put v=b_L. For 1<=s<=r define D_s=3(2^(r-s)-1) and j_s=L-1-D_s, and add F_s={b_{j_s},v,c_s}, where the c_s are new. The hypergraph is linear. Its intersection graph consists of the induced path E_1...E_L, the clique on {E_L,F_1,...,F_r}, and the additional edge E_{j_s}F_s for each s. Note that j_1=L/2+2, j_r=L-1, j_r-j_{r-1}=3, and D_{s-1}=2D_s+3.

We claim that E_L,F_1,...,F_r are all ascending and have common last vertex v. For F_s, the path E_1,...,E_{j_s},F_s has length j_s+1 and enters F_s through b_{j_s}. Any induced path ending with F_s contains at most one other clique vertex, necessarily immediately before F_s. If that vertex is F_t with t<s, the path has length at most j_t+2<j_s+1; if t>s, its base-path part lies in the component of (E_1,...,E_{L-1})-E_{j_s} containing E_{j_t}, and the total length is at most L-j_s+1<j_s+1; the case of E_L is bounded by the same quantity. Hence φ(F_s)=j_s+1 and b_{j_s} is its unique entrance.

It remains to compute φ(b_{j_s}). A path ending at b_{j_s} has last edge E_{j_s} or F_s. If the last edge is F_s and the path enters through v, the preceding paragraph bounds its length by j_s. If the last edge is E_{j_s}, an induced path in the intersection graph can use at most two clique vertices, consecutively. Paths using no clique jump have length at most j_s because j_s>L/2. The only potentially longer form uses a prefix ending at E_{j_t} with t<s, then F_t,F_u with u>s, then a base segment from E_{j_u} back to E_{j_s}; its length is j_t+j_u-j_s+3. This is maximized by t=s-1 and u=r, and the recurrence D_{s-1}=2D_s+3 gives j_{s-1}+j_r-j_s+3=j_s. The endpoint cases s=1 and s=r are shorter or equal, with j_r-j_{r-1}=3. Thus φ(b_{j_s})=j_s, so each F_s is ascending.

For E_L, the base path E_1,...,E_L gives φ(E_L)=L with unique entrance a_{L-1}; any route entering E_L through the clique is shorter because the nearest earlier attachment is at j_{r-1}=L-4. The same two-clique calculation gives φ(a_{L-1})=L-1. Hence E_L is also ascending. All r+1 edges have v as one of their two last vertices. These are the only edges incident with v, and all are ascending, so h(v)=0 while a(v)=r+1.
