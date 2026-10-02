# Directed graph of ascending edges and a level-cut inequality

## Statement

For each ascending edge e={x,y,z} with unique entrance x, orient two arcs x→y and x→z on V(H). Then φ strictly increases along every arc. If c(v) is the number of ascending edges with entrance v, then d^+(v)=2c(v), d^-(v)<=2φ(v)-1, and d_H(v)-c(v)<=2φ(v)-1. Consequently, for S={v:φ(v)<K}, 2Σ_{v∈S}d_H(v)-3Σ_{v∈S}(2φ(v)-1) <= Σ_{v∉S}(2φ(v)-1).

## Body

If e={x,y,z} is ascending, then φ(x)=φ(e)-1, while y and z are last vertices of longest paths ending with e, so φ(y),φ(z)>=φ(e)=φ(x)+1. Hence the orientation is acyclic. Linearity forbids parallel arcs in the same direction and opposite arcs are impossible because φ increases. Each ascending edge with entrance x contributes two outgoing arcs, giving d^+(x)=2c(x). Every incoming arc at v comes from an edge for which v is a snake vertex, so d^-(v)<=2φ(v)-1. Every incident edge at v not counted by c(v) has φ(e)<=φ(v), hence there are at most 2φ(v)-1 of them. Therefore d_H(v)-c(v)<=2φ(v)-1. For S={φ<K}, the number of arcs from S to its complement is at least 2Σ_S c(v)-Σ_S d^-(v), and at most Σ_{V\S}d^-(v). Substituting the preceding bounds yields the displayed cut inequality.