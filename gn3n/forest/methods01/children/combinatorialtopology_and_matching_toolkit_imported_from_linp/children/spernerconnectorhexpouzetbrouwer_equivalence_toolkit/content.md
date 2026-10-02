# Sperner--Connector--Hex--Pouzet--Brouwer equivalence toolkit

## Statement

Sperner's lemma, the Hochberg--McDiarmid--Saks Connector Theorem, multidimensional Hex, Pouzet's lattice-direction lemma, and Brouwer's fixed-point theorem form a short implication cycle. The discrete middle of the cycle is especially reusable for finite path-state spaces.

## Body


Expository source supplied by the user: https://www.cs.uaf.edu/~hartman/pouzethex.pdf

Statements.
Sperner: a proper labeling of a simplicial subdivision of a d-simplex has a completely labeled d-cell.
Connector (Hochberg--McDiarmid--Saks): every d-coloring of the vertices of a simplicial subdivision of a d-simplex has a connected monochromatic subgraph meeting every facet.
Hex: in the d-dimensional lattice-box version with each color assigned a pair of opposite faces, some color contains a path joining its assigned faces.
Pouzet: let A be a finite integer box and f:A->{+/-e_1,...,+/-e_d} satisfy x+f(x) in A for every x. Then two neighboring lattice points x,y satisfy f(x)=-f(y).
Brouwer: every continuous self-map of a closed d-box has a fixed point. Equivalently, by conjugating with a homeomorphism, the same fixed-point property holds for a closed d-simplex.

Short proof cycle.

Sperner => Connector. Suppose no monochromatic connector exists. Number the d+1 facets. For each vertex v, label v by the least facet that v cannot reach by a path in its own color. Boundary geometry makes this a proper Sperner labeling. A completely labeled d-cell has d+1 vertices but only d colors, so two adjacent vertices have the same original color. They lie in the same monochromatic component and therefore have exactly the same reachable facets, contradicting their different Sperner labels.

Connector => Hex. Given a d-coloring of a triangulated d-dimensional box, with each color/player assigned a pair of opposite faces, add one new vertex z_i of color i for each player i. Join z_i to every vertex on one of player i's assigned faces and join all the new vertices to one another. This is the standard augmentation of the box to a triangulated d-simplex. By Connector there is a connected monochromatic subgraph meeting every facet. If its color is i, then because the new vertices form one facet and z_i is the only new vertex of color i, the connector contains z_i. Every same-color edge from z_i into the original box enters through the attached face of player i, while meeting the opposite relevant facet forces the same monochromatic component to meet player i's opposite face. Deleting z_i leaves a monochromatic path in the original box joining player i's two assigned faces, so player i wins Hex.

Hex => Pouzet. Color x by the coordinate index of f(x), ignoring its sign. Hex gives a monochromatic path between the two faces perpendicular to some coordinate i. The inward-pointing condition x+f(x) in A forces f to point +e_i at one end and -e_i at the other. Along the path the sign must change; at the first change, two neighboring vertices have opposite f-values.

Pouzet => Brouwer. Suppose F:[0,1]^d->[0,1]^d is continuous and has no fixed point. Put G(x)=F(x)-x. Since G is continuous and never zero on the compact box, there is a number δ>0 such that ||G(x)||_∞>=δ for every x.

By uniform continuity of G, choose a sufficiently fine rectangular grid so that whenever x and y are neighboring grid points,
||G(x)-G(y)||_∞<2δ.

At each grid point x, choose an index i for which |G_i(x)|=||G(x)||_∞, and define h(x)=sign(G_i(x))e_i, breaking ties arbitrarily. After scaling the grid to an integer box, h has the inward-pointing property required by Pouzet: if x lies on the lower i-face then G_i(x)=F_i(x)-x_i>=0, so h(x) cannot be -e_i; if x lies on the upper i-face then G_i(x)<=0, so h(x) cannot be +e_i. Hence x+h(x) remains in the box.

Pouzet therefore gives neighboring grid points x,y with h(x)=-h(y). Say h(x)=e_i and h(y)=-e_i. Then G_i(x)>=δ and G_i(y)<=-δ, so
|G_i(x)-G_i(y)|>=2δ,
contradicting the choice of the grid. Thus F has a fixed point.

Brouwer => Sperner. Number the outer simplex vertices V_0,...,V_d cyclically. From a proper Sperner labeling with no completely labeled cell, define a piecewise-affine self-map by sending every triangulation vertex labeled i to V_{i+1 mod (d+1)}. On each small simplex one label is missing, so its image lies in a proper face; hence an interior fixed point is impossible. If x were a boundary fixed point, let J be the proper set of outer vertices spanning the minimal face whose relative interior contains x. The boundary rule implies that every label used on the minimal subdivision simplex containing x lies in J, so the image of x lies in the face spanned by the cyclic successor set sigma(J). Equality g(x)=x would force x into the intersection of the J-face and sigma(J)-face. Since x lies in the relative interior of the J-face, this forces J subset sigma(J), hence J=sigma(J); a nonempty proper subset of one cyclic orbit cannot be invariant. Thus there is no boundary fixed point either, contradicting Brouwer on the simplex.

LINP relevance. The most portable pieces are Connector and Pouzet: if a finite state box carries a local "direction of escape" and boundary states point inward, Pouzet forces adjacent states with opposite directions; if states are colored by obstruction type, Connector forces one type to persist across all boundary classes.
