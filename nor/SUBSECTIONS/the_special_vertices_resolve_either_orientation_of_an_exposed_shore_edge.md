# The special vertices resolve either orientation of an exposed shore edge

## Metadata

- ID: the_special_vertices_resolve_either_orientation_of_an_exposed_shore_edge
- Parent Section: monochromatic_connector_blocks
- Position: 24
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

A forward shore edge accepts source z before it or sink x after it; a backward edge accepts either special vertex between its ends. These exact ordered zero-triple identities are the elementary port-resolution rules used by the larger gluing constructions.

## Development

In the switching-normalized split B -> z -> A -> x, let u,v be shore vertices. If u->v, then alpha(z,u,v)=0 and alpha(u,v,x)=0. If v->u, then alpha(u,z,v)=0 and alpha(u,x,v)=0. Thus either orientation of a shore edge can be incorporated into a monochromatic-zero connector by placing one special vertex in the appropriate adjacent position. Forward edges accept z before them or x after them; backward edges accept z or x between their endpoints. This is the basic local port-resolution mechanism available when x and z are allowed to move independently.
