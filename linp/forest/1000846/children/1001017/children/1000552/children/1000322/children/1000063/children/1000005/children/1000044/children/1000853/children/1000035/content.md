# Class-III systems have no rank-four nonspecial edge

## Statement

A 12-vertex 5-regular linear triple system has no nonspecial edge of rank four.

## Body

Suppose for contradiction that e={x,y,z} is nonspecial of rank four with unique entrance x, and choose a longest path
  P=(g_1,g_2,g_3,e)
ending in e through x.

Apply the repaired terminal-star matching lemma 5cba7c87c67a. Use its notation:
  g_1={r,a,b},  g_2={r,c,d},  g_3={c,x,t},
with outside vertices u,v,w,
  A={r,a,b,c,d},
  B={x,t,u,v,w},
and two residual terminal matchings M_y,M_z on
  R={r,t,u,v,w}.

The lemma gives:
1. M_y∪M_z is an alternating five-vertex path;
2. r is internal in that path, so exactly two of its four matching edges are incident with r and exactly two are not;
3. exactly eight hyperedges remain after the path and terminal-star edges are listed;
4. every remaining hyperedge contains exactly one vertex of A and therefore exactly two vertices of B.

Each of the eight remaining hyperedges therefore determines a pair of vertices of B. By linearity these eight B-pairs are all distinct.

But B has only ten unordered pairs. At least three of them are already unavailable to the remaining edges:
- the pair {x,t} lies in g_3;
- M_y∪M_z has four edges on R, exactly two incident with r because r is internal, so its other two matching edges lie entirely in {t,u,v,w}⊂B. Those two B-pairs already occur in terminal edges.

These three forbidden B-pairs are distinct. Hence at most
  C(5,2)-3=7
pairs of B remain available.

The eight remaining hyperedges require eight distinct available B-pairs, a contradiction.

Therefore no nonspecial edge of rank four exists in a 12-vertex 5-regular linear triple system.
