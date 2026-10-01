# Every endpoint compatibility triangle enters the cyclic four-kernel frontier

## Statement

Let H be a minimum counterexample with chosen deletion covers and compatibility graph G. Fix an anchor cover F_d=P|Q, let y be an endpoint of P, and suppose dy lies in a compatibility triangle with third label z. Then z is the unique vertex of P adjacent to y, the common insertion gap of the triangle F_d,F_y,F_z is the endpoint gap of their common exceptional path, and the triangle precedence is cyclic. Consequently the endpoint-triangle theorem c0118dfa86c6 applies: the three deletion labels together with the first surviving common-path vertex form either a Hamiltonian four-set with non-Hamiltonian path-cover-two complement, or the exceptional cyclic four-kernel with its universal exterior Hamiltonian-extension conclusions.

## Body

By 0f94f3d4dbbb, the common neighbor z of d and y must be the unique inward neighbor of y on the displayed anchor path P. Assume for definiteness that P=(y,z,R); the terminal-end case is symmetric. Apply the compatible-triangle common-gap theorem gapgeom01 to F_d,F_y,F_z. In F_d the two surviving triangle labels y,z occur consecutively as the first two vertices of the exceptional path. Since gapgeom01 says all three labels are inserted at one identical gap of one common path, that gap must be the left endpoint: there is no common surviving vertex before y. Thus this is an endpoint common-gap compatible triangle. The endpoint-gap clause of gapgeom01 makes its precedence tournament cyclic, and c0118dfa86c6 applies verbatim, yielding the stated four-kernel dichotomy and complement consequences.
