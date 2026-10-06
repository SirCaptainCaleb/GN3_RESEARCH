# Cellular odd maps from reversal-odd chamber labels

## Metadata

- ID: cellular_odd_maps_from_reversal_odd_chamber_labels
- Parent Section: port_permutahedral_antipodal_topology
- Position: 1
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition


A reversal-odd vector label on permutation chambers extends canonically to a continuous odd map on the barycentric subdivision by averaging chamber labels on each face barycenter and extending affinely along face chains. A zero on a minimal carrier face yields a positive convex dependence among that face's chamber labels. This is the portable cellular mechanism behind the Article VII topology.


## Development


The permutations of \(V\) are the chambers of the type-\(A\) Coxeter complex, equivalently the chamber set associated with the permutahedron. Reversal of a permutation defines the antipodal chamber involution.

Suppose a vector label
\[
L(\pi)\in W
\]
is assigned to every chamber and satisfies
\[
L(\pi^{\mathrm{rev}})=-L(\pi).
\]
On the barycentric subdivision, assign to the barycenter of each face \(F\) the average of \(L\) over the chambers containing \(F\), and extend affinely along nested face chains. Because reversal preserves face incidence and negates every chamber label, this produces a continuous odd map.

If a zero lies in a face, then \(0\) lies in the convex hull of the labels of its chambers. Choosing a minimal carrier face gives a positive convex dependence on its participating chamber labels.

This is the transferable topological mechanism from Article VII: a reversal-odd combinatorial statistic on coordinate orders can be promoted canonically from chamber data to an odd cellular map, and a topological zero becomes a positive balanced relation inside one permutahedral face.
