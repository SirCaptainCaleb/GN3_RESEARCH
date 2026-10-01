# Source/non-source decomposition couples a forced digraph to a proper colored graph

## Statement

Let V be a finite set and let F be a linear family of triples. In every T∈F choose a source σ(T)∈T. Form a digraph D by replacing T={u,v,w} with source u by the arcs u→v,u→w, and form a graph H by adding the edge vw colored u. For x∈V let s(x) be the number of triples sourced at x and h(x)=d_H(x). Then H is simple and properly edge-colored, and
s(x)+h(x)=d_F(x),
d_D^+(x)=2s(x),
d_D^-(x)=h(x).
Hence
(1/2)d_D^+(x)+d_D^-(x)=d_F(x)
for every x.

## Body

Simplicity of H follows because two distinct triples producing the same graph edge vw would share v and w, contradicting linearity. Properness follows similarly: two adjacent graph edges vx and vy with the same color u would arise from triples {u,v,x} and {u,v,y}, sharing u and v.

Every triple containing x places x in exactly one of two roles. If x is the chosen source, it contributes one to s(x). Otherwise x is one of the two non-source vertices and the triple contributes exactly one H-edge incident with x. Hence
s(x)+h(x)=d_F(x).

Each source triple at x contributes two distinct out-neighbors in D; distinct source triples at x cannot share a non-source vertex by linearity. Thus d_D^+(x)=2s(x).

Finally, incoming arcs u→x in D are in bijection with H-edges incident with x: the triple {u,x,y} sourced at u creates both the arc u→x and the H-edge xy colored u. Hence d_D^-(x)=h(x).

Combining the identities gives
(1/2)d_D^+(x)+d_D^-(x)=d_F(x).