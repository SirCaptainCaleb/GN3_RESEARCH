# The exceptional P4 pattern is a two-switch support corridor

## Statement

Let F_1,F_2,F_3,F_4 be pairwise incompatible deletion covers for distinct labels a_1,a_2,a_3,a_4, with nonempty common core W, and suppose their support-compatibility graph is the path 1-2-3-4. Then all four covers induce one common support partition R|S on W. Moreover a_1 has one fixed core class in every cover that contains it, and a_4 likewise has one fixed core class in every cover that contains it. The internal labels a_2,a_3 each switch core class exactly once across the blue path: a_2 has one class in F_1 and the opposite class in F_3,F_4, while a_3 has one class in F_1,F_2 and the opposite class in F_4. Thus the three red support-incompatibilities 13,14,24 are carried by a_2, by both a_2 and a_3, and by a_3 respectively.

## Body

# Proof

The support-compatible pairs are exactly 12,23,34.

Restrict all four covers to the common core

W=V(H)-{a_1,a_2,a_3,a_4}.

Support compatibility of F_1,F_2 gives the same partition on W. Support compatibility of F_2,F_3 gives the same partition on W, and support compatibility of F_3,F_4 does likewise. By transitivity all four covers induce one common two-class partition R|S on W.

Fix the labels of R,S once and for all by anchoring one core vertex.

For i != j, let x_{ij} be the class bit of a_j in F_i.

The blue edge 12 gives

x_{13}=x_{23},
x_{14}=x_{24}.

The blue edge 23 gives

x_{21}=x_{31},
x_{24}=x_{34}.

The blue edge 34 gives

x_{31}=x_{41},
x_{32}=x_{42}.

Therefore a_1 has one common class in F_2,F_3,F_4, and a_4 has one common class in F_1,F_2,F_3.

Now use the red edge 13. The common surviving special labels are a_2,a_4. The label a_4 has the same class in F_1 and F_3 by the equalities above. Since F_1,F_3 are support-incompatible while their core partition agrees, the disagreement must be carried by a_2. Hence

x_{12} != x_{32}.

Because x_{32}=x_{42}, the label a_2 has one class in F_1 and the opposite class in F_3,F_4.

Similarly use the red edge 24. Its common special labels are a_1,a_3. The label a_1 has the same class in F_2 and F_4. Therefore support incompatibility forces

x_{23} != x_{43}.

Because x_{13}=x_{23}, the label a_3 has one class in F_1,F_2 and the opposite class in F_4.

Finally the red edge 14 is then automatic: on the common domain of F_1,F_4 both surviving internal labels a_2,a_3 have switched class, so the two support partitions differ.

Thus the P4 pattern is completely localized: the endpoint labels a_1,a_4 are support-stable, while a_2 and a_3 perform one class switch each at opposite ends of the blue path.