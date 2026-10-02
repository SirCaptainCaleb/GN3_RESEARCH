# An all-clean two-regular sharp-shell support component is impossible

## Statement


Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, and let
S_0S_1...S_{m-1}S_0
be a connected 2-regular component of the Hamiltonian-support odd graph. Choose one Hamilton order on each support and suppose every length-two subwalk takes the clean alternative of astra004twowalk.

Then no such component exists.

Equivalently, every 2-regular sharp-shell support component contains a length-two subwalk exposing one of the non-clean astra004twowalk outcomes: an inherited three-part crossing or relative-order disagreement.


## Body


Apply astra004shelldecagon.

First suppose some three-step label repetition occurs:
x_i=x_{i+3}.
Using indices i=0 after rotation, write the first four edge labels as
a,b,c,a.
Cleanliness gives
S_2=(S_0-{b}) union {a},
S_4=(S_2-{a}) union {c}=(S_0-{b}) union {c}.
By astra004fiveactiveshell, the even supports S_0,S_2,S_4 have one common ordered interior C of order lambda-2. The clean replacements preserve the entire order outside the replaced endpoint. Therefore there is one active label e such that the three active pairs are
{e,b}, {e,a}, {e,c},
and the three chosen Hamilton orders keep e on one fixed endpoint side while b,a,c occupy the opposite side.

This is exactly the configuration ruled out by 8867264db573: two of the three varying labels together with e Hamiltonize a path of order lambda+1. Hence the repeated-label branch is impossible.

It remains that no equality x_i=x_{i+3} occurs. Then astra004cleandecagon applies and produces a third odd neighbor of one cycle support. But the displayed cycle is a connected 2-regular component, so every one of its vertices has degree exactly two in the full odd graph. Contradiction.

Both alternatives are impossible. Therefore an all-clean 2-regular support component cannot exist.
