# Two-terminal rank ascent from a low-rank nonspecial edge

## Statement

Let e be a nonspecial edge of rank t in a linear 3-uniform hypergraph, with terminal vertices y,z. If d(y)>2t-1, then some edge f_y containing y has phi(f_y)>t; likewise for z. Hence if the minimum degree is delta and t<(delta+1)/2, then e has two distinct higher-rank neighbors, one through each terminal.

## Body

Because y is a terminal vertex of the nonspecial edge e, phi(e,y)=phi(e)=t. If every other edge f containing y satisfied phi(f)<=t, then the second assertion of the snake maximum-degree lemma, applied to e at y, would give d(y)<=2(t-1)+1=2t-1. Therefore d(y)>2t-1 forces an incident edge f_y with phi(f_y)>t. The same argument applies at z. The two higher-rank edges f_y and f_z are distinct: if one edge contained both y and z, it would intersect e in two vertices, contradicting linearity. Thus in a minimum-degree-delta hypergraph, every nonspecial edge of rank t<(delta+1)/2 branches to two distinct strictly higher-rank neighbors through its two terminal vertices.
