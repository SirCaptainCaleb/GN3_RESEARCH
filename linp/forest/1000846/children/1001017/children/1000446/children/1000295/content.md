# Full shadow doubles hypergraph degree

## Statement

Let H be a linear 3-uniform hypergraph and S its 2-shadow, with each shadow edge yz colored by the unique third vertex x such that xyz is in E(H). Then S is properly edge-colored and d_S(v)=2d_H(v) for every vertex v. Hence delta(S)=2delta(H). A minimum-degree theorem for properly edge-colored graphs applied to the full shadow must use delta(S), not delta(H).

## Body

Proof. Every hyperedge e={v,x,y} through v contributes the two shadow edges vx and vy incident with v. Different hyperedges through v cannot reuse either shadow neighbor, because two hyperedges containing v and the same second vertex would intersect in two vertices, contradicting linearity. Thus the 2d_H(v) incident pairs are all distinct and d_S(v)=2d_H(v). Properness of the third-vertex coloring is the same linearity argument: two shadow edges incident with v cannot have the same third-vertex color x, since their corresponding triples would both contain v and x. WARNING ON LIFTING: an ordinary rainbow path in the full shadow need not be a linear hypergraph path because a color may equal a nonincident path vertex. Either require a strong rainbow path whose colors avoid all path vertices, or pass to the A/B retained shadow where path vertices and colors lie in disjoint classes.