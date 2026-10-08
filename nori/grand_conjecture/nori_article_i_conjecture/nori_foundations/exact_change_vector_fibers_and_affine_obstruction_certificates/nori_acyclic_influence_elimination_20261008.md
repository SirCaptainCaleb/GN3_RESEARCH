# Acyclic Boolean influence elimination forces a one-change geodesic

Let p=(p_1,...,p_n) be a fixed coordinate order in Q_n, x_i its starting bit at p_i, and d_i(x)=w_i(x) XOR w_{i+1}(x) for i=1,...,s=n-3, where w_i is the ordered-three-face color of its ith three-move window.

THEOREM (acyclic Boolean influence elimination). Let J be a subset of {1,...,s} and let phi:J -> {1,...,n} be an injection. Assume (i) for every i in J and every x, toggling x_{phi(i)} complements d_i(x); (ii) the directed graph on J with arrow i -> j (i != j) whenever d_i depends nontrivially on x_{phi(j)} is acyclic. Then the restricted change map x -> (d_i(x))_{i in J} is exactly 2^{n-|J|}-to-one onto all of F_2^J. If |J| >= n-4, the given direction order admits a full antipodal geodesic with at most one change. If J contains every seam, each difference vector occurs exactly 8 times, with precisely 8 monochromatic starts and 8(n-2) one-change-or-better starts.

PROOF. Choose an arbitrary assignment to the n-|J| nonpivot variables. Prescribe arbitrary target bits t_i for i in J. In a reverse topological order where every j pointed to by i is solved before i, d_i is independent of all pivot variables still unset. The uniformly nonzero Boolean derivative in its own pivot means precisely one choice of x_{phi(i)} makes d_i=t_i. Earlier target equations remain fixed because all variables on which they depend were set before them. Thus every nonpivot assignment has a unique extension to each prescribed target. Choosing all target d_i=0 makes at most s-|J| residual color changes; if this number is at most 1 the path succeeds. The counts follow from the s+1 Hamming-weight-at-most-one words in F_2^s. QED.

FACE-LOCAL COROLLARY (triangular seam certificate). Call seam i controllable when d_i is independent of earlier starting bits x_1,...,x_{i-1}, and toggling x_i always complements d_i. Then the choice phi(i)=i on all controllable seams gives an acyclic influence graph, as every arrow points to a larger index. If a permutation has at most one uncontrollable seam, that permutation admits a good antipodal geodesic; with t uncontrollable seams it admits a geodesic with at most t changes. The pivot condition is precisely uniform sensitivity of the ordered face window i+1 to its fixed exterior coordinate p_i, since window i has that coordinate free. The prefix condition is equality of the two adjacent window-color Boolean derivatives in each earlier exterior coordinate.

NONLINEAR EXAMPLE. Suppose for a fixed p the window-color functions are
 w_i(x) = XOR_{j<i}(x_j XOR 1) XOR G_i(x_{i+3},...,x_n),
where G_i are arbitrary Boolean functions of later exterior coordinates, without affine or degree restrictions. Then d_i(x)=(x_i XOR 1) XOR G_i(...) XOR G_{i+1}(...), so each seam is controllable and the complete change map is eight-to-one. Since the ordered triples in one permutation are all different and their reversals are not among that same list, the prescribed window-face functions can be extended to antipodal-reversal-odd ordered-three-face colorings by pairing each ordered face with its antipodal reverse.

SCOPE. The certificate works even without antipodal symmetry. It establishes a sufficient condition, not global NORI closure. A hypothetical NORI counterexample must have at least two uncontrollable seams for every order and no acyclic uniform-pivot matching of size n-4 in any order.

**Statement**

For a fixed direction order, acyclic uniform pivots controlling at least n-4 of the n-3 Boolean color-change equations force a full antipodal geodesic with at most one change. The controlled change map is uniformly surjective, with exact fiber size 2^(n-|J|).

**Proof**

Fix the nonpivot bits and prescribe controlled differences. Set pivot bits in reverse topological order of their influence graph. Every current equation is independent of unset pivots and has derivative one in its pivot, giving a unique solution; induction yields exact fibers.
