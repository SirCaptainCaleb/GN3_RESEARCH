# A synchronized global 4|5|a minimum gives an equal-potential exchange or three labels locked against the long path

## Statement

In the setting of 866b0442112e, choose x in X and a set J subseteq Y of at least three vertices such that both (X-{x}) union {p_1} and (X-{x}) union {p_a} are Hamiltonian and (Y-{y}) union {x} is Hamiltonian for every y in J. Then for each y in J either there is an equal-potential spanning three-cover of orders 4,5,a obtained by the cyclic support exchange x -> Y, y -> P, and one endpoint e of P -> X, or y is noninsertable into every position of the displayed path P. Consequently either at least one such equal-potential exchange exists or at least three distinct vertices of Y are globally noninsertable into P.

## Body

Fix y in J. For e in {p_1,p_a}, set A_e=(X-{x}) union {e} and B_y=(Y-{y}) union {x}. By construction both A_e and B_y are Hamiltonian.

If H[(P-{e}) union {y}] is Hamiltonian for at least one endpoint e, then choosing Hamilton paths on A_e, B_y, and (P-{e}) union {y} gives a spanning three-cover. Its component orders are 4,5,a, exactly the same as the original cover, so its quadratic potential is equal to the original Phi. Its supports realize the cyclic exchange x from X to Y, y from Y to P, and e from P to X.

Suppose instead that neither (P-{p_1}) union {y} nor (P-{p_a}) union {y} is Hamiltonian. If y could be inserted at any position of the displayed tight order P, then after deleting a suitable endpoint of that inserted order one would obtain a Hamilton tight path on one of these two endpoint truncations together with y. For an extreme insertion delete the opposite endpoint; for an internal insertion delete either endpoint while retaining the local insertion. This contradicts the assumed non-Hamiltonicity of both endpoint truncations. Hence y is noninsertable into every position of P.

Applying the dichotomy independently to every y in J proves the result. Since |J|>=3, if none of the equal-potential exchanges occurs then at least three distinct labels of Y are globally noninsertable into P. ∎