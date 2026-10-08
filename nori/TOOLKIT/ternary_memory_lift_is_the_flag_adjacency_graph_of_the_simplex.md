# The ternary memory lift is the flag-adjacency graph of the simplex triangulation

**Summary:** The memory-lift graph is already inside the simplex: its vertices are oriented 2-faces (three consecutive prefix sets), and its edges connect overlapping 2-faces inside a 3-face. So Connector/Sperner topology can be applied to the actual memory states.

## Statement

Ignoring the copy bit and poles, a ternary memory-lift state (S,u,v) is the oriented rank-two flag S < S+u < S+{u,v} in the barycentric simplex. An internal transition appending w moves to the overlapping flag S+u < S+{u,v} < S+{u,v,w}; the two state flags share an edge inside a rank-three flag. Hence the memory-lift graph has a canonical geometric realization in the second barycentric subdivision of the completed simplex.

## Body


## State flags inside the barycentric simplex

Work on the barycentric macroface B_0=sd(Delta^{n-1}) of the completed Freudenthal cube.

A ternary memory state without its copy bit is a triple (S,u,v), where u,v are distinct and not in S. Associate to it the chain

F(S,u,v):
S subset S union {u} subset S union {u,v}.

When S is empty, omit the empty-set vertex from B_0 and regard the state as attached to the lower boundary cap; equivalently work in the full completed simplex where the distinguished e_0 supplies the missing initial vertex.

For non-boundary ranks, F(S,u,v) is a 2-simplex of the barycentric subdivision.

### Transitions are overlapping flags

The memory-lift transition

(S,u,v) -> (S union {u},v,w)

corresponds to the pair of chains

S < S+u < S+u+v

and

S+u < S+u+v < S+u+v+w.

They share the edge

S+u < S+u+v

and together lie in the rank-three flag

S < S+u < S+u+v < S+u+v+w,

which is a 3-simplex of the barycentric triangulation.

Therefore, if every state is represented by the barycenter of its flag triangle and every transition by the segment joining the two state barycenters through the barycenter of their common 3-simplex, the internal memory-lift graph embeds canonically in sd(B_0), equivalently in a further barycentric subdivision of the completed simplex.

### Colors

The transition above is colored by h(u,v,w). Thus its color is determined exactly by the three successive coordinate increments of the ambient rank-three flag.

Reversal/complementation sends

F(S,u,v)

to the oppositely ranked flag representing the state with reversed memory (v,u), and sends the transition label h(u,v,w) to h(w,v,u)=1-h(u,v,w). Hence the geometric realization respects the antipodal memory-lift involution.

### Pole geodesics

A permutation pi determines a maximal chain of subset vertices. The successive rank-two flags along that chain are exactly the memory states visited by the pole geodesic for pi. Consequently the pole geodesic is the canonical gallery path through the sequence of overlapping 2-faces inside one maximal permutation chamber.

### Topological consequence

The reachability sets R, A(R), and the neutral corridor N from the memory-lift formulation can now be viewed as subsets of an actual simplicial refinement of the completed simplex, not merely as abstract graph states.

This is the appropriate place to apply a Connector/Sperner/Hex principle: any topological statement should act on the memory-state carriers themselves, where geodesicity and two-step memory are retained automatically.


## Metadata

- ID: ternary_memory_lift_is_the_flag_adjacency_graph_of_the_simplex
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
