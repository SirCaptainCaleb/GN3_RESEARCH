# Support-incompatibility graph is Hamilton-connected in every minimum counterexample branch without order disagreement

## Statement

Let H be a minimum counterexample of order n>10. Choose one deletion two-cover F_x of H-x for each x in V(H), and assume no pair of chosen covers is support-compatible but order-incompatible. Form the graph J on V(H) by joining x,y when F_x and F_y are support-incompatible on their common vertex set. Then every vertex of J has degree at least n-5. Consequently J is Hamilton-connected: for any distinct prescribed labels a,b there is an ordering a=x_1,x_2,...,x_n=b of all deletion labels such that each consecutive pair F_{x_i},F_{x_{i+1}} is support-incompatible. In particular J is connected, Hamiltonian, and every prescribed pair of labels lies at the ends of a spanning support-incompatibility chain.

## Body

Under the standing hypothesis, the full-compatibility graph C on the deletion labels has maximum degree at most four by compatibility_degree4_prescribed_fan01. Since every pair of chosen covers is either fully compatible, support-compatible but order-incompatible, or support-incompatible, and the middle alternative is excluded, the support-incompatibility graph J is exactly the complement of C. Hence for every label x,
d_J(x)=(n-1)-d_C(x)>=n-5.

Because H is a minimum counterexample, mincex01 gives n>10. Therefore
n-5 >= (n+1)/2.
The standard Hamilton-connected degree criterion now applies: every simple graph on n vertices with minimum degree at least (n+1)/2 is Hamilton-connected. Thus for any distinct prescribed labels a,b, J has a Hamilton path from a to b.

Equivalently, one may order all deletion labels
a=x_1,x_2,...,x_n=b
so that each consecutive pair F_{x_i},F_{x_{i+1}} is support-incompatible on V(H)-{x_i,x_{i+1}}. This packages the m-5 crossing conclusion globally: instead of merely giving many unrelated support-incompatible partners for each anchor, it provides a spanning transport chain through the whole deletion family, with arbitrary prescribed endpoints.

This does not by itself close the grand theorem; the next consumer must exploit successive cut changes along such a chain, for example by tracking how support classes transform from one deletion state to the next and forcing endpoint reuse, a parity obstruction, or defect compression.