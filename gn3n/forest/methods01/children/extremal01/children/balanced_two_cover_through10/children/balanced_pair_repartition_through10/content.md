# Every component pair of total order at most ten can be optimally balanced in one move

## Statement

Let H be a boundary tournament and let A|B|C be any spanning three-cover. If s=|A|+|B| satisfies 2<=s<=10, then one legal pairwise repartition of A|B replaces their union by two Hamiltonian paths of orders floor(s/2) and ceil(s/2), leaving C unchanged. Consequently the quadratic contribution of the pair strictly decreases exactly when ||A|-|B||>=2; if the displayed orders already differ by at most one, the balanced repartition has the same minimum possible quadratic contribution.

## Body

Apply the certified theorem balanced_two_cover_through10 to the induced boundary tournament on V(A) union V(B), whose order is s<=10. It supplies a spanning two-path cover R|S of this pair union with orders floor(s/2),ceil(s/2). Replacing A|B by R|S and leaving C unchanged is one legal pairwise repartition.

For fixed sum s, quadraticpotential01 gives a^2+(s-a)^2=(s^2+(2a-s)^2)/2, so the sum of squares is minimized exactly by the integer-balanced split floor(s/2),ceil(s/2). Therefore the move strictly decreases Phi precisely when the original pair-order difference is at least two, and otherwise preserves the already minimal pair contribution. In particular the earlier 3|5 to4|4 and 4|6 to5|5 strict descents are special cases.
