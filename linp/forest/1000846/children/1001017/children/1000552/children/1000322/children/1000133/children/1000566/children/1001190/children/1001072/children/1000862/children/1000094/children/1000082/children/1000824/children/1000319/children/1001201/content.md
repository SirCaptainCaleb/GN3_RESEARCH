# Rigid zero-slack half-neighborhoods expose a usable fixed-target cut

## Statement

In the zero-slack alternating witness T_1,C_1,...,C_{c-1},T_c=e={x,y,z}, suppose both alternate ports y,z fail the initial uncolored two-switch. Then they have the same complete half-neighborhood A of size c/2 among the forest triples, and no neighbors in the complementary index set B.

In this rigid branch, an alternate port such as y has an unused-color safe connector into some T_i with i in A. Moreover there exists i in A, 1<=i<=c-2, such that the contracted graph also contains an edge T_1T_{i+1}. Thus some cut simultaneously has the target adjacency y-T_i and the return adjacency T_{i+1}-T_1 needed for the fixed-target 2-opt exchange; only color compatibility and the bounded unsafe ports remain.

## Body

Failure of the first two-switch for both y and z forces their half-neighborhood sets to avoid B. Tightness gives A_y=A_z equal to the complement of B, of size c/2, and each alternate port is complete to every triple indexed by A.

Since y has degree 3c/2 in the DXX graph while the witness uses only c-1 colors, at least c/2+1 incident y-edges have unused colors. These land in c/2 target triples, so some T_i receives at least two unused-color y-connectors; at least one avoids the unique unsafe local port.

For the return side, c-1 lies in B, so A is contained in {1,...,c-2}. Minimum degree c/2 in the contracted graph gives T_1 at least c/2-1 neighbors among T_2,...,T_{c-1}. If C is the corresponding index set, then |A|=c/2, |C|>=c/2-1, and both lie in a universe of size c-2; hence A∩C is nonempty. Any i in the intersection gives both required uncolored adjacencies at one cut.