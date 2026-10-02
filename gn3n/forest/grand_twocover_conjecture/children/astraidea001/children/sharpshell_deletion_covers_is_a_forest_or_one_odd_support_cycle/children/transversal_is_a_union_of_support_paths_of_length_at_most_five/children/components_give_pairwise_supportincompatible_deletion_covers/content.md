# Different sharp-shell transversal components give pairwise support-incompatible deletion covers

## Statement

Let H be a minimum counterexample in the sharp half-order shell n=2lambda+1, and choose one lambda|lambda deletion cover F_v=A_v|B_v of H-v for every vertex v, with selected support graph J. If selected edges e_x and e_y lie in different connected components of J, then F_x and F_y are support-incompatible on H-{x,y}. Consequently, choosing one deletion label from each connected component of J gives a pairwise support-incompatible family. In the disturbance-free forest normal form of 9d79ac6c14d5, such a family has size at least ceil(n/5).

## Body

Suppose instead that F_x and F_y are support-compatible on the common domain W=V(H)-{x,y}. Because both covers have component orders lambda,lambda before the second deletion, restricting either cover to W produces support-class sizes lambda and lambda-1: the label deleted second lies in exactly one of the two lambda-supports.

Support compatibility says the two unordered support partitions of W coincide. In particular their unique class of order lambda is the same set S.

For F_x, that order-lambda class is one of A_x,B_x; for F_y it is one of A_y,B_y. Hence the selected odd-graph edges e_x=A_xB_x and e_y=A_yB_y share the support vertex S. Therefore e_x and e_y lie in the same connected component of J, contrary to hypothesis.

Thus different connected components yield support-incompatible selected deletion covers. Selecting one edge label from each component gives a pairwise support-incompatible family. Under 9d79ac6c14d5 there are at least ceil(n/5) components, proving the quantitative conclusion. ∎