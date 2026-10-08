# Idea: use a polytopal Tucker carrier on the original switch-prism cells

## Composition

(none yet)

## Development

To avoid artificial complementary diagonals from triangulation, keep the original centrally symmetric cell structure of the switch prism. Label bad vertices by signed physical middles. If every original cell avoids containing both +b and -b for every b, then each cell label set lies in a face of the crosspolytope avoiding the origin; using an equivariant barycentric subdivision and normalized face averages gives a continuous extension from the whole switch ball to the crosspolytope sphere. Its boundary restriction is antipodal, impossible by mod-2 degree. Therefore some genuine original switch-prism cell contains a complementary pair. A minimal complementary one-cell is automatically a legal adjacent-swap repair, since vertical complementary edges are impossible. The first unresolved carriers are genuine two-cells: edge-times-cut rectangles, commuting squares, and A2 braid hexagons. Thus the extraction problem can be attacked on actual Coxeter/product residues without ever introducing a fake diagonal edge.
