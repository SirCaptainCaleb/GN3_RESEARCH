# Audit correction: separated connector vertices have an exact three-path gluing law

## Metadata

- ID: separated_connector_vertices_have_an_exact_three_path_gluing_law
- Parent Section: monochromatic_connector_blocks
- Position: 26
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

For L,x,P,z,R, the zero word and compatibility are determined by the path endpoint edges and two cross-dominance bits. A nonempty middle path has length at least two; a singleton gives alpha(x,p,z)=1. Empty middle recovers adjacent-xz gluing. All exposed ports remain explicit.

## Development

Let L,P,R be disjoint zero shore paths in the switching-normalized split z dominates A and A dominates x. For a middle block P of size at least two, the order L,x,P,z,R is zero exactly when the last edge of L is forward, the first and last edges of P are forward, the first edge of R is forward, the first vertex of P dominates the last vertex of L, and the first vertex of R dominates the last vertex of P, with outer endpoint clipping. Compatibility additionally requires the first edge of L and last edge of R to be forward when those outer blocks have size at least two. If P is empty, x,z are adjacent and the corresponding middle conditions disappear. If P has size one, the window (x,p,z) has color one, so a zero connector of this form is impossible. Thus the middle block has a genuine arity-two lower bound.
