# Low-dimensional cube forcing before the general Norine proof

## Statement

Before the 2026 general proof, simple square constraints and explicit Q_4--Q_6 analyses already forced monochromatic antipodal paths. These local cube mechanisms are retained because they are more likely than the final chain construction to port directly to finite LINP state spaces.

## Body


Feder--Subi 2013: https://doi.org/10.1016/j.dam.2012.12.025
They call a two-edge-coloring of Q_n simple when no square has one pair of opposite edges in one color and the other opposite pair in the other color (equivalently, no alternating square in the relevant sense). Their theorem shows that every simple coloring has a monochromatic path between antipodal vertices, even without assuming antipodality. They also proposed the stronger 1-switch conjecture and proved it for n<=5. The reusable lesson is that a purely 2-dimensional local prohibition on squares can force a global antipodal connection.

West--Wise 2019: https://dwest.web.illinois.edu/pubs/antip.pdf
They prove that for 2<=k<=6 every antipodal edge-coloring of Q_k has a monochromatic antipodal geodesic. Their smaller-cube arguments repeatedly expose forced colors around an alternating 4-cycle and then propagate those constraints through the remaining coordinate directions. For Q_4, an alternating square and its antipodal mate are joined across the remaining two directions; if the connecting 2-path is monochromatic it immediately completes an antipodal geodesic, and if it is not, antipodality plus the square pattern forces neighboring edges until a monochromatic antipodal geodesic appears. The Q_5,Q_6 arguments elaborate this same local-forcing philosophy.

Džavoronok 2026 provides a cleaner topological bridge: https://arxiv.org/abs/2606.04181. A centrally symmetric simply connected simplicial complex with an antipodal two-edge-coloring always contains a monochromatic antipodal path. The proof assumes no such path, labels red/blue components, and constructs an equivariant map to S^1, contradicting the absence of an equivariant map from a simply connected centrally symmetric complex to the antipodal circle. In the cube, square faces supply the 2-cells; classes with enough resolvable squares therefore fall to this criterion.

LINP relevance. Three escalating templates are available:
(1) square test: characterize forbidden 4-state transition patterns;
(2) finite cube forcing: prove a bounded-dimensional local configuration already forces the desired splice/path;
(3) 2-complex test: fill local commutation squares and prove the resulting state complex simply connected, then use an antipodal component obstruction.
These are potentially useful for product constructions, binary-coordinate blow-ups, or path-state graphs where changing two independent local choices gives a square.
 