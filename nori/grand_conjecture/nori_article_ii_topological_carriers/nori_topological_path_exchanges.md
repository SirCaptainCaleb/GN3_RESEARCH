# Geodesic pseudomanifolds and maximal-path exchanges

# The all-root geodesic complex and its equivariant limits

Let K_n be the simplicial complex whose vertices are the vertices of Q_n and whose facets are the unordered vertex sets of all full antipodal cube geodesics. A facet contains n+1 vertices, one at every distance from either endpoint. Each such path has a unique unordered antipodal endpoint pair, because distances along a geodesic strictly increase from its starting endpoint.

## Root blocks and pseudomanifold incidence

For one antipodal pair {x,bar x}, let K_x consist of facets with these endpoints. A full rooted geodesic is specified by a permutation of the n directions. Its internal vertices are the successive nonempty proper supports of that permutation, viewed relative to x. These chains form the barycentric subdivision of the boundary of the (n−1)-simplex on the direction set. Consequently

K_x={x,bar x} * sd(boundary Delta^(n−1)),

where the two endpoint vertices span an edge and the join has dimension n. Its link at the endpoint edge is an (n−2)-sphere. The full complex has 2^(n−1) root blocks and 2^(n−1)n! facets, one for each antipodal endpoint pair and direction order.

A codimension-one face of a geodesic facet is obtained by omitting one path vertex. Omitting an interior vertex permits the two adjacent distinct steps to be transposed, supplying a second incident facet. Omitting an endpoint permits the new endpoint to be changed along the freed direction, giving the corresponding root-slide facet. Both operations keep all intermediate cube vertices physically valid. Every ridge therefore has exactly two incident facets: K_n is a closed mod-two pseudomanifold. Summing all facets modulo two yields its canonical top cycle.

## Antipodal symmetry and the coloring interface

Bitwise complementation acts freely on vertices and carries a geodesic facet to another facet. This creates an honest antipodal carrier which is absent when one cube root is fixed. Permutohedral links and root slides provide actual combinatorial cells on which a Tucker- or Borsuk–Ulam-type argument may be formulated. The topology of K_n, however, is independent of the three-face coloring. An equivariant zero or an intersecting pair of path facets gives a topological coincidence only; a one-switch witness additionally requires their full ordered window words and the colors of physical seam faces.

One may decorate facets by their first and last ordered directions and track window labels across adjacent transpositions. For a transposition at positions i,i+1, every physical three-window outside start positions i−2 through i+1 remains unchanged. The preserved exterior bits follow because the two direction orders have identical prefix vertices before the exchange and identical vertices after both directions are traversed. Thus local exchange checks require only four affected physical windows, but an improvement in switch count is an additional combinatorial statement.

## The extraction frontier

The all-root pseudomanifold supplies a global equivariant domain and genuine root-slide gluing. The remaining issue is a color-dependent carrier or obstruction class which forces a compatible one-switch facet. General index statements for the uncolored K_n do not automatically survive passage to a subcomplex cut out by color conditions. A successful topological proof must certify a high-index subcarrier of actual good-window data, or show that its obstructed boundary produces a path-exchange improvement. The root-coupled complex and its facet incidence provide the geometric stage for this stronger theorem.
