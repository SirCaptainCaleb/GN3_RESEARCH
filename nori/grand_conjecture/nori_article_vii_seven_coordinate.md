# Article VII — Seven-coordinate structural and tournament methods

# Seven-direction endpoint factorization

Let c color physical ordered three-faces of Q_n. For a direction-distinct path (p_1,...,p_k) rooted at x, let w_j be the color of the actual ordered three-face traversed by (p_j,p_(j+1),p_(j+2)). Exterior-coordinate bits determine the root dependence of these colors.

## Shared-pivot formula

For seven distinct directions (a,b,c,d,e,f,g), fix the initial root bits other than x_d=t. The five window colors have the form

(A(t),M_1,M_2,M_3,E(t)).

Indeed the three interior free triples (b,c,d),(c,d,e),(d,e,f) contain d, so their physical faces and colors do not depend on t. The first triple (a,b,c) and last triple (e,f,g) omit d and may depend on t. Thus a single pivot controls the two endpoint windows while the interior color word remains fixed.

For six moves (a,b,c,d,e,f), choosing the two middle root bits x_d and x_c gives the independent endpoint formula (A(u),B,C,D(v)). Both central windows contain c and d as free directions, hence B,C are fixed. If B≠C and both endpoint maps are nonconstant, select A=B and D=C, obtaining one change. If B=C then matching either endpoint to that common middle color also suffices.

## A seven-direction conditional criterion

Let the three fixed middle bits be (M_1,M_2,M_3), and let A,E be the endpoint maps. Every possible resulting word is (A(t),M_1,M_2,M_3,E(t)). If the middle triple has two changes, both endpoint choices leave at least two changes. If the middle triple has exactly one change, a good word occurs precisely when the chosen first endpoint equals M_1 and the chosen last endpoint equals M_3, because any extra change would raise the total to two. If the middle triple is constant q, a good word occurs precisely when at least one of the two endpoint values is q. These alternatives follow by directly counting the four boundaries between consecutive colors. They give an exact one-bit rooted solvability test in any ambient dimension, provided the other exterior bits are held fixed.

## Wing factorization and closure classes

The endpoint maps are functions of the same pivot, so their attainable value pairs are correlated. The seven-coordinate wing-factorization results exploit this correlation together with changes of direction order, complemented faces and alternative pivots. Under the established crossed-sensitivity and flat-bridge hypotheses, a good antipodal seven-geodesic is forced. These structural criteria expose what a general proof would need: a coordinated pivot change or interchangeable wing that removes an endpoint obstruction while preserving the genuine middle ordered-face colors.

This article gives exact endpoint-root formulas and provable closure tests, with seven-coordinate special families providing further forced configurations. The general-dimension conjecture remains a separate global compatibility question.
