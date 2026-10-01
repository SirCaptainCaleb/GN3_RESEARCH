# Synchronized five-side replacements give equal-size swaps or bounded insertion obstructions

## Statement

In the setting of astra003fivecommoncore, choose x in X so that D=V(X)-{x} extends Hamiltonianly with both endpoints of P. For each endpoint e of P, either X|P has an exact repartition of the same component sizes obtained by replacing x with e on the five-side and e with x on the P-side, or x has a bounded failed-insertion obstruction on the inherited path P-e. Hence either an equal-quadratic-potential support exchange exists at one end, or the same displaced vertex x yields bounded insertion obstructions on both endpoint truncations of P. If both other paths have order at least seven, x can be chosen so that this alternative holds simultaneously for at least three of their four endpoints.

## Body


Let X|P|Q be a quadratic-potential-minimal three-cover in a connected component of the pairwise-repartition graph containing no two-cover, with |X|=5.

First suppose P=(p_1,...,p_m), m>=7. By astra003fivecommoncore, choose x in V(X) such that, with D=V(X)-{x}, both
D union {p_1} and D union {p_m}
are Hamiltonian.

Fix e in {p_1,p_m}, and let P-e denote the inherited endpoint truncation of P. The path P-e is tight and has order m-1.

If H[V(P-e) union {x}] is Hamiltonian, choose a Hamilton path L_e on D union {e} and a Hamilton path R_e on V(P-e) union {x}. These two paths are disjoint and partition V(X) union V(P). Thus
L_e | R_e
is an exact two-path cover of that pair union. Its component orders are 5 and m, exactly the displayed orders of X|P, so replacing X|P by L_e|R_e is a legal repartition preserving the quadratic potential. It exchanges the support labels x and e between the two sides.

Suppose instead that H[V(P-e) union {x}] is non-Hamiltonian. Then x cannot be inserted at any position into the displayed inherited tight-path order of P-e, since any successful insertion would itself be a Hamilton tight path on that support. The failed-insertion theorem therefore supplies a bounded local obstruction involving x and at most four consecutive vertices of P-e.

Applying this dichotomy to both e=p_1 and e=p_m proves: either there is an equal-potential support exchange at one of the two ends, or the same displaced vertex x has bounded failed-insertion obstructions on both endpoint truncations P-p_1 and P-p_m.

If also Q has order at least seven, use astra003fivethreeendpoints to choose x so that D union {e} is Hamiltonian for at least three of the four endpoints of P and Q. Applying the same argument separately to those endpoints gives the strengthened conclusion: either one of at least three equal-potential support exchanges exists, or the same vertex x produces bounded failed-insertion obstructions on at least three corresponding endpoint-truncated paths, while all exchanges use the same four-vertex support D.
