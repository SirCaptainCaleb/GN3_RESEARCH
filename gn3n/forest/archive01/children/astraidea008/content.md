# Positive correlation of complementary Hamiltonian supports

## Statement

Let H have n vertices, k=floor(n/2), and let S be a uniformly random k-subset. Then Pr(H[S] and H[V(H)-S] are both Hamiltonian) >= Pr(H[S] is Hamiltonian) Pr(H[V(H)-S] is Hamiltonian).

## Body

Unproved, very low-confidence counting conjecture. This replaces construction of a particular two-cover by a correlation inequality between complementary supports. If both marginal probabilities are positive, the inequality forces a balanced two-cover. Positivity of the two marginals is a separate obligation and is not assumed automatic at the larger order. A possible proof would pair bad complementary choices with good choices by path-order switches, preserving multiplicities; this is a global counting task rather than local endpoint transport. Main risk: there is no obvious monotone probability space or FKG mechanism here, and complementation often creates negative correlation. A counterexample with negative covariance would kill the exact inequality but might suggest the correct weaker inequality or a different distribution on supports. No test has been made.
