# Four source rails force two units of distinguished overlap

## Statement

In a four-edge source-clean 0-1-1 block, let Q_1,...,Q_4 be the four maximum source rails and let a_ij be the number of distinguished source-or-opposite-terminal vertices shared by Q_i and Q_j. Then either two distinct rail pairs satisfy a_ij>=2, or one rail pair satisfies a_ij>=3. Equivalently, the four-rail obstruction contains at least two units of overlap beyond a single two-vertex theta witness.

## Body

Each rail contains four distinguished vertices: its own source and one vertex from each of the other three source-terminal pairs. Thus the four distinguished-vertex sets are four 4-subsets of the eight distinguished vertices, with exactly one choice from each of four disjoint pairs. For any fixed source-terminal pair, if r of the four rails choose one member and 4-r choose the other, its contribution to the sum over rail pairs of distinguished intersections is C(r,2)+C(4-r,2), whose minimum is 2. Summing over the four source-terminal pairs gives sum_{i<j} a_ij>=8. If at most one rail pair had overlap at least two and that overlap were exactly two, then the six pair overlaps would sum to at most 2+5=7. Hence either a second pair has overlap at least two, or the unique exceptional pair has overlap at least three. Since any two common vertices of two linear paths determine a lens after passing to consecutive common vertices, the first outcome supplies two distinct double-overlap pairs while the second supplies at least two elementary lenses on one rail pair.
