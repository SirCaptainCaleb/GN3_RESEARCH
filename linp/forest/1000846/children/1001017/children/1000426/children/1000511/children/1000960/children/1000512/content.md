# Nonspecial edges are unique longest-path entrance vertices

## Statement

Let G be a linear 3-graph, F=L(G), and e∈E(G). For each longest induced path in F ending at the vertex e and having penultimate vertex f, call the unique vertex of f∩e its entrance label. If phi(e)=1 then e is special. If phi(e)≥2, then e is nonspecial exactly when all longest induced paths ending at e have the same entrance label. Equivalently, e is special exactly when at least two entrance labels occur.

## Body

By Pathmaker, a longest induced path f_1...f_{t-1}e in F is the edge sequence of a longest linear hypergraph path ending in e. Let w=f_{t-1}∩e. The final edge e contributes the two new vertices e\{w}; their order is arbitrary, so both are possible last vertices of a longest hypergraph path. Therefore this induced path certifies both snake incidences (e,v) for v∈e\{w}. A vertex u∈e fails to be a snake terminal exactly when every longest induced path into e enters through u: if some longest induced path enters through w≠u then u is one of its two new vertices and can be last; conversely a path entering through u cannot end at u. Since every edge already has at least two snake incidences, for phi(e)≥2 the edge is nonspecial exactly when there is one omitted vertex u, i.e. exactly when every longest induced path has entrance label u. For phi(e)=1 the vertices of the sole edge can be ordered arbitrarily, so all three terminal incidences occur.
