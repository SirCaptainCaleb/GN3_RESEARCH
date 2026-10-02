# The simple source-rail graph has at most four edges

## Statement

For a four-edge 0-1-1 consecutive-rank violation, let G_s record source-rail pairs having exactly one common vertex. Then every edge of G_s lies in at most one triangle, so |E(G_s)|<=4. Hence at least two of the six rail pairs have at least two common vertices. If equality holds, G_s is either C4 or a triangle with one pendant edge, and the nonsimple pairs have explicitly shared opposite-terminal vertices forced by the simple U-U exchanges.

## Body


Consider four source-clean 0-1-1 edges e_i={x_i,v,u_i}, i=1,2,3,4, in a consecutive-rank block, with chosen source rails Q_i. Let G_s be the graph on {1,2,3,4} in which ij is an edge exactly when
  |V(Q_i) cap V(Q_j)|=1.

By cddeebb1b0b2, every simple pair ij is reciprocal U-U:
  u_j in V(Q_i),   u_i in V(Q_j).

Suppose ij is simple and has two distinct common neighbors k,l in G_s. Then:
- because ik and jk are simple, both Q_i and Q_j contain u_k;
- because il and jl are simple, both Q_i and Q_j contain u_l.
The vertices u_k,u_l are distinct, since distinct offending hyperedges through v have disjoint non-v pairs by linearity. Hence Q_i and Q_j share at least the two distinct vertices u_k,u_l, contradicting simplicity of ij.

Therefore every simple edge of G_s has at most one common neighbor in G_s; equivalently no simple edge lies in two triangles.

On four vertices this implies |E(G_s)|<=4. Indeed any graph with five or six edges contains an edge lying in two triangles: K4 does, and K4 minus one edge still has the opposite edge in the two triangles through the missing edge's endpoints.

Hence among the six rail pairs, at least two are nonsimple:
  |V(Q_i) cap V(Q_j)|>=2.

If equality |E(G_s)|=4 holds, the simple graph is one of the two four-edge graphs with no edge in two triangles:
- a 4-cycle C4; or
- a triangle with one pendant edge.
Thus the extremal residual rail pattern is finite.

In the C4 case, if the simple cycle is 1-3-2-4-1, then the two nonsimple pairs are 1-2 and 3-4. Moreover Q_1,Q_2 both contain u_3 and u_4, while Q_3,Q_4 both contain u_1 and u_2, so each nonsimple pair has two explicitly labeled common terminal vertices.

In the triangle-plus-pendant case, say 1,2,3 form the simple triangle and 1-4 is the pendant simple edge. Then 2-4 and 3-4 are nonsimple, and both Q_2,Q_4 and Q_3,Q_4 contain u_1 as a labeled common terminal inherited from the simple edges to vertex 1.
