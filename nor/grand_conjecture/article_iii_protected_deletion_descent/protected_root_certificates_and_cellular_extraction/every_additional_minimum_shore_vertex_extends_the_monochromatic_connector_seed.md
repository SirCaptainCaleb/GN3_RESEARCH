# Every additional minimum-shore vertex extends the monochromatic connector seed

## Composition

(none yet)

## Development

Continue from §344. Let
C=(u,x,z,v,w)
be the monochromatic five-coordinate connector seed with word 000, where u,v,w lie in the minimum signature shore A and form a directed triangle in the switching-normalized shore tournament
B -> z -> A -> x.

Fix any additional
a in A minus {u,v,w}.

If a -> u in the shore tournament, then
(a,u,x,z,v,w)
has word 0000. The only new initial window is alpha(a,u,x)=0 because a,u,x form a transitive tournament triple, and the remaining windows are those of the old 000 seed.

If u -> a, then
(u,a,x,z,v,w)
also has word 0000. Here alpha(u,a,x)=0 because u,a,x are transitive, and alpha(a,x,z)=alpha(x,z,a)=0 because a belongs to A. The remaining windows are unchanged from the seed.

Therefore every individual additional vertex of A can be placed next to the anchor u on the appropriate side while preserving monochromaticity.

The unresolved issue is collective compatibility among several added shore vertices, rather than one-vertex compatibility.

This supplies the boundary-reachability input suggested by the Hartman analogy: every single shore target is individually reachable from the monochromatic connector state by an explicit legal extension. Any least-unreachable argument should therefore detect the first collective obstruction for a set of shore vertices.
