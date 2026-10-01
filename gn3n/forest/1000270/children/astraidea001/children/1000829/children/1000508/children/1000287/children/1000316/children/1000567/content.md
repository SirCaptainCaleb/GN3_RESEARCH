# Lexicographically maximal forest transversals constrain singleton-transfer label edges

## Statement

Let H be in the sharp half-order shell. Among all deletion-cover transversals whose selected support graph is a forest, choose J so that the decreasing sequence of connected-component edge counts is lexicographically maximal. Let C,D be any two distinct components of J with alpha=|E(C)|>=beta=|E(D)|. Choose selected deletion covers F_a,F_b corresponding to edges in C,D. Suppose their common-double-deletion support comparison takes the singleton-transfer branch of 68deffb43319, producing an alternative deletion edge f_x labelled x whose endpoints lie in C and D. Then the selected edge e_x of J lies in C. If removing e_x splits C and the endpoint of f_x lying in C belongs to a piece with r edges, then r<=alpha-beta-1. Consequently, if alpha=beta, the singleton-transfer branch is impossible for every pair of selected covers drawn from C and D; every such pair has the fully crossed four-cell support pattern.

## Body

Let s(J) be the decreasing list of component edge counts of J. Replace the selected edge e_x by the alternative edge f_x supplied by 68deffb43319. Since f_x joins a support vertex of C to one of D, which are distinct components of J, the replacement graph J' is again a forest deletion-cover transversal.

If e_x lies in a third component E different from C,D, deleting e_x splits E while leaving C,D intact, and adding f_x merges C and D into one component of alpha+beta+1 edges. Relative to s(J), all entries larger than alpha are unchanged, while at the first position where a component of order at most alpha appears, J' has a component of order alpha+beta+1>alpha. Thus s(J') is lexicographically larger, contradiction.

If e_x lies in D, deleting it splits D. Let the endpoint of f_x in D lie in a resulting piece with r>=0 edges. Adding f_x joins that piece to all of C, creating a component of alpha+r+1>alpha edges. Again all components originally larger than alpha are unchanged, so the sorted component-size vector strictly improves, contradiction.

Therefore e_x lies in C. Delete it and let C_1 be the piece containing the endpoint of f_x in C, with r edges. Adding f_x joins C_1 to D, creating a component with beta+r+1 edges; the other piece of C has alpha-r-1 edges. If beta+r+1>alpha, the same lexicographic comparison gives a strict improvement, impossible. Hence beta+r+1<=alpha, i.e. r<=alpha-beta-1.

If alpha=beta, the right side is -1, impossible because r>=0. Thus no singleton-transfer comparison can occur between selected covers from equal-sized components. By 68deffb43319, their common-double-deletion support partitions must instead have all four intersections nonempty. ∎
