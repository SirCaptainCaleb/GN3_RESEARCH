# Repeated-intersection collisions contain a linear-size matching of source-path pairs

## Statement

Let M be a family of interior color-terminal collisions x_i=v_j on one rainbow terminal-pair path. Assume that every collision in M has the repeated-intersection outcome
  |V(R_i) intersect V(R_j)|>=2
and
  |V(R_i) intersect V(R_{j+1})|>=2,
where R_s is the chosen maximum path with last vertex x_s.

Form a simple graph Q on the parent-edge indices by adding, for every collision x_i=v_j in M, the two edges
  {i,j}, {i,j+1}.

Then Q has exactly 2|M| edges and maximum degree at most four. Consequently Q contains a matching of size at least
  ceil(2|M|/7).

Hence M forces at least ceil(2|M|/7) index-disjoint pairs of chosen maximum source paths, each pair having at least two common vertices.

## Body

First, the two graph edges contributed by one collision are distinct because j and j+1 are distinct.

No graph edge can be contributed by two different collisions. Indeed, suppose {a,b} with a>b is contributed. Since every color-terminal collision points backward, the larger index a must be the collision owner. The edge {a,b} can arise only if x_a=v_b or x_a=v_{b-1}. These two alternatives are mutually exclusive because v_b and v_{b-1} are distinct vertices of the simple terminal-pair path. Thus each unordered pair is contributed at most once, and |E(Q)|=2|M|.

Fix an index t. It can be the owner of at most one collision, because the unique entrance x_t is one fixed vertex; if it is an owner, that collision contributes exactly two Q-edges incident with t.

As a nonowner endpoint, t can occur only from a collision hitting v_t, which contributes {i,t}, or from a collision hitting v_{t-1}, which contributes {i,t}. Because the terminal-pair path is rainbow, at most one entrance label equals v_t and at most one entrance label equals v_{t-1}. Hence at most two further Q-edges are incident with t. Therefore
  Delta(Q)<=4.

Take a maximal matching N in Q. Every graph edge is incident with at least one endpoint of an edge of N. For a matched edge ab, at most
  deg_Q(a)+deg_Q(b)-1 <= 7
graph edges are incident with a or b. Therefore
  |E(Q)| <= 7|N|,
so
  |N| >= ceil(2|M|/7).

By construction, every edge of N is one of the repeated-intersection pairs supplied by its collision. Since N is a matching, these pairs use pairwise distinct parent-edge indices.