# The hard fixed-endpoint branch cannot have a perfect-matching extension graph

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with X a Hamiltonian four-set and P=(p_1,...,p_m). Put U=X union {p_1,p_m}. Assume U is non-Hamiltonian, X union {p_1} and X union {p_m} are non-Hamiltonian, U-x is Hamiltonian for every x in X, and define J on X by xy in E(J) iff U-{x,y} is Hamiltonian. Then J contains two adjacent edges. In particular J cannot be a perfect matching. Consequently the perfect-matching alternative in four_side_endpoint_matching_bridge01 and four_side_m6_matching_frontier01 is impossible whenever their hard six-set hypotheses arise from a Hamiltonian four-side X with both one-endpoint extensions non-Hamiltonian.

## Body

Apply two_bad_five_extensions_adjacent_four01 to the Hamiltonian four-set X and the exterior vertices a=p_1, b=p_m. Its hypotheses are exactly that X+a and X+b are non-Hamiltonian. The graph K in that theorem joins xy precisely when {a,b,x,y}=U-{X-{x,y}} is Hamiltonian, which is exactly the graph J used in four_side_endpoint_matching_bridge01. Therefore J has two adjacent edges. A perfect matching has no adjacent edges, so the fixed-endpoint perfect-matching alternative is excluded. No minimum-counterexample property beyond the ambient hypotheses is needed for this local implication; the minimum-counterexample assumption is retained only because this theorem is aimed at the theorem-facing four-side route.