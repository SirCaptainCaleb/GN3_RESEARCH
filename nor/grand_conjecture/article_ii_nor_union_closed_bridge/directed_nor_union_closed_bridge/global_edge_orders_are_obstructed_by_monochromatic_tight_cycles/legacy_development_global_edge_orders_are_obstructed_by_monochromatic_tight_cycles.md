# Global edge orders are obstructed by monochromatic tight cycles — preserved pre-item development

## Global edge-order representation and monochromatic tight cycles

Let h be a reversal-antisymmetric ternary coordinate coloring on V, and suppose each center tournament T_b is transitive. Equivalently, each center b supplies a strict total order on the unordered edges incident with b.

Form the directed comparison graph D whose vertices are unordered pairs from V. Two distinct pair vertices sharing b are adjacent, oriented {a,b}->{b,c} precisely when h(a,b,c)=0. Its underlying graph is the line graph of the complete graph on V.

### Theorem
The following are equivalent:
1. There is an injective scalar edge weight lambda with h(a,b,c)=0 iff lambda(ab)<lambda(bc).
2. D is acyclic.
3. There is no cyclic ordering (x_0,...,x_{m-1}) of distinct coordinates, m>=3, for which h(x_{i-1},x_i,x_{i+1})=0 at every index modulo m.

Whenever D is cyclic, a shortest directed cycle in D yields such a monochromatic tight cyclic order. The local transitivity hypothesis is essential to the extraction from a comparison cycle.

### Proof
The equivalence of 1 and 2 is the elementary topological-order characterization of a finite acyclic directed graph. A cyclic coordinate order as in 3 gives a directed cycle through the distinct edge vertices {x_{i-1},x_i}, so 2 implies 3.

Conversely, suppose D is cyclic and choose a shortest directed cycle of length m. An oriented chord would give a shorter directed cycle: either orientation of the chord closes one of the two directed subpaths. Hence the chosen cycle is chordless in the underlying line graph.

If m=3, its three underlying edges are pairwise incident. Three distinct pairwise incident edges in a simple graph either have a common endpoint or form a triangle. The common-endpoint case is excluded because the comparison orientation at that endpoint is transitive. Thus they form a triangle, and their cyclic comparison orientations give the required three-coordinate cyclic order.

If m>=4, let e_0,...,e_{m-1} be the underlying edge vertices in directed cyclic order, and let x_i be the common endpoint of e_i and e_{i+1}. Nonconsecutive edges in this sequence are disjoint by chordlessness. In particular x_{i-1} differs from x_i, since otherwise e_{i-1} and e_{i+1} would meet. Hence e_i={x_{i-1},x_i}. The x_i are pairwise distinct: a repeated shared endpoint would make two nonconsecutive edges meet (or would make three consecutive edges meet, again furnishing a chord). Therefore the edges constitute a simple cycle in the original graph.

The arc e_i->e_{i+1} now reads h(x_{i-1},x_i,x_{i+1})=0. This produces the required monochromatic tight cyclic coordinate order and proves 3 implies 2.

### NOR significance
The locally transitive class has a precise obstruction to global scalar representation: monochromatic tight cycles on distinct coordinates. Reversal converts the color-0 cyclic order into a color-1 cyclic order.

If the extracted cycle spans V, cutting it at any edge gives a monochromatic spanning tight order and closes directed N_4. If it does not span V, no extension theorem is established here. The missing step is to absorb exterior coordinates into a spanning one-change order, or to use the acyclic case by another method.

Thus the distinction between global edge ordering and independent local orders is not merely inconsistent numerical preferences. Its primitive inconsistency already contains a NOR-compatible monochromatic cycle. Any cycle-extension approach must retain all exterior coordinates; the existence of a proper cycle alone is not closure.
