# The universal hard-reversal cross family is a complete endpoint pair grid with ubiquitous local order disagreement

## Statement

Let H be a minimum counterexample and let P=(p_0,...,p_m), m>=2, be a proper tight path. Put K=V(H)-V(P) and G=H-{p_0,p_m}. Assume the universal hard-reversal cross condition that (p_m,y,p_0) is tight for every y in K. Then every pair of distinct y,z in K makes {p_0,p_m,y,z} Hamiltonian. Moreover G, every G-y, and every G-{y,z} are non-Hamiltonian with path-cover number two. Finally, every three distinct vertices y,z,w in K contain two of the corresponding Hamiltonian four-paths that have order disagreement on the common pair involving p_m; hence the disagreement is supported on at most five vertices.

## Body

Let y,z be distinct vertices of K. By hypothesis, (p_m,y,p_0) and (p_m,z,p_0) are tight. Boundary antisymmetry on {y,p_m,z} gives exactly one of (y,p_m,z) and (z,p_m,y). In the first case (y,p_m,z,p_0) is a tight Hamilton path; in the second case (z,p_m,y,p_0) is. Thus every {p_0,p_m,y,z} is Hamiltonian.

Minimum-counterexample calculus gives |K|>=4. Each displayed four-set is therefore proper, and its complement G-{y,z} is non-Hamiltonian with path-cover number two. Also G=H-{p_0,p_m} has path-cover number two by the two-vertex deletion part of minimum-counterexample calculus and is non-Hamiltonian. For y in K, the three-set {p_0,p_m,y} is Hamiltonian (every boundary tournament on three vertices is Hamiltonian). If G-y were Hamiltonian, its Hamilton path together with one on {p_0,p_m,y} would two-cover H, impossible; since G-y is proper, minimum-counterexample calculus gives path-cover number two.

Now fix distinct y,z,w in K and orient the ordinary complete graph on them by a->b iff (a,p_m,b) is tight. Boundary antisymmetry makes this a tournament. Every three-vertex tournament has a vertex z with an incoming neighbor y and an outgoing neighbor w. Hence (y,p_m,z) and (z,p_m,w) are tight. Together with (p_m,z,p_0) and (p_m,w,p_0), the grid supplies the Hamilton paths R=(y,p_m,z,p_0) and S=(z,p_m,w,p_0). On their common pair {p_m,z}, R orders p_m before z whereas S orders z before p_m. Thus they have order disagreement, supported on {p_0,p_m,y,z,w}.