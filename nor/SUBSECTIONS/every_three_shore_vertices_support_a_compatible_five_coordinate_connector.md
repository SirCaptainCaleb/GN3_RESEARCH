# Every three shore vertices support a compatible five-coordinate connector

## Metadata

- ID: every_three_shore_vertices_support_a_compatible_five_coordinate_connector
- Parent Section: monochromatic_connector_blocks
- Position: 19
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Any three shore vertices u,a,b, with a->b chosen, give the compatible seed (u,x,z,a,b). No directed-triangle or minimum-shore hypothesis is needed. The universal bases elevate seed existence further to supports of size zero, one, and two.

## Development

Use the switching-normalized split B -> z -> A -> x. Let u,a,b be any three distinct vertices of A, and orient the last two so that a -> b in the shore tournament. Then C=(u,x,z,a,b) has ternary word 000. Indeed alpha(u,x,z)=alpha(x,z,u)=0 by the shore signature, alpha(x,z,a)=0 for the same reason, and alpha(z,a,b)=0 because z dominates both a,b while a->b. The first endpoint pair u->x is forward and the last pair a->b is forward. Thus every three-element subset of A supports a compatible monochromatic connector on those three vertices together with x,z. Directed-triangle structure is not needed for seed existence; it supplies only additional A3 root information.
