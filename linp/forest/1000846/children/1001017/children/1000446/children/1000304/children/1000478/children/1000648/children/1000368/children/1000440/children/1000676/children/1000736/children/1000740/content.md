# An endpoint chord raises the next joint's vertex rank

## Statement

Let P=(g1,...,gp) be a linear path in a finite linear 3-graph, with p≥3 and last vertex v. For 1≤i≤p-2 put a=g_i∩g_{i+1} and c=g_{i+1}∩g_{i+2}. If an edge f contains a and v, then φ(c)≥min{i+2,p-i+1}.

## Body

Write f={a,v,z}. The edge f is not a path edge, since no path edge contains both a and v. It meets g_i and g_{i+1} exactly at a, and g_p exactly at v. In particular z lies in neither g_i nor g_{i+1} nor g_p, and c is not in f.

Suppose first that z is absent from g_{i+2}∪...∪g_{p-1}. Then
(g_i,f,g_p,g_{p-1},...,g_{i+2})
is a linear path of length p-i+1. Here the decreasing final segment includes just g_p if i=p-2. The only contacts of f with that segment are at v in g_p. The edge g_i is disjoint from the entire segment. All other required intersections and disjointness follow from P. Its last vertex may be c: if the last edge g_{i+2} has a path edge as predecessor, c lies outside that predecessor; if its predecessor is f, c is outside f. Hence φ(c)≥p-i+1.

Otherwise let j be the least index in {i+2,...,p-1} such that z∈g_j. Then
(g_1,...,g_i,f,g_j,g_{j-1},...,g_{i+2})
is a linear path of length j. Indeed f meets the prefix only at a in g_i: z lies in g_j with j≥i+2, while v belongs only to g_p. It meets the reversed segment only at z in its first edge, by minimality of j. The prefix and reversed segment are disjoint because their indices differ by at least two. Its last vertex may again be c, which is outside f and outside the next path edge to its right. Thus φ(c)≥j≥i+2.

The two cases prove the claimed lower bound. No maximality, edge rank, specialness, or charging assumption is used.
