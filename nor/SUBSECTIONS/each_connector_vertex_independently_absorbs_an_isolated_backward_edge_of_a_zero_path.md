# Each connector vertex independently absorbs an isolated backward edge of a zero path

## Metadata

- ID: each_connector_vertex_independently_absorbs_an_isolated_backward_edge_of_a_zero_path
- Parent Section: monochromatic_connector_blocks
- Position: 20
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Either special vertex inserts into a zero shore path on a 101 tournament-edge packet, resolving an isolated backward edge. Forward endpoint pairs also allow source/sink endpoint insertion. These are local port-resolution tools for independent special-vertex motion.

## Development

Let P=(a_1,...,a_m) be a monochromatic-zero shore order in the fixed switching-normalized tournament, and write t_i=1 when a_i->a_{i+1}. Insert y in {x,z} between a_i and a_{i+1}. Because x is a sink and z is a source relative to A, both special vertices have the same three local zero conditions: alpha(a_{i-1},a_i,y)=0 iff t_{i-1}=1; alpha(a_i,y,a_{i+1})=0 iff t_i=0; and alpha(y,a_{i+1},a_{i+2})=0 iff t_{i+1}=1. Therefore either x or z may be inserted at an interior gap exactly when the shore edge-direction pattern there is 101. Thus each special vertex independently absorbs an isolated backward edge of a zero path. At the ends, z may be prepended compatibly whenever the first shore edge is forward, and x may be appended compatibly whenever the final shore edge is forward. This gives a concrete adjacency-free repair mechanism for gluing the canonical zero-path cover.
