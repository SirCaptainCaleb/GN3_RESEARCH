# Above order fourteen every anchored four-window descends, disagrees, or migrates by at most two labels

## Statement

Let H be a minimum counterexample of order n>=15. Let W be any Hamiltonian four-vertex support and let H-W=P|Q be a two-cover. Then at least one of the following occurs:

(1) strict descent: W|P|Q admits a spanning three-cover with strictly smaller quadratic potential Phi;

(2) order disturbance: the local exchange data expose explicit order disagreement;

(3) bounded migration: there is another Hamiltonian four-set W'!=W such that H-W' is non-Hamiltonian of path-cover number two and |W cap W'| is 2 or 3.

Thus the family of Hamiltonian four-windows with two-cover complements is, above order fourteen, a finite migration system in which every state either escapes by Phi descent/order disagreement or moves to a Johnson-distance-one-or-two state.

## Body

Apply 27a05b61e8c3.

In the checkerboard branch, n>=15 implies one complementary path has order at least six, so 92c86d754e08 gives strict Phi descent, outcome (1).

In the shared-endpoint branch, apply 064902822993. If its six-set is non-Hamiltonian, the four-good-deletions theorem yields order disagreement, outcome (2). If its six-set is Hamiltonian, apply 476ed5aaa6ed to obtain another Hamiltonian four-set W' with path-cover-two complement and |W cap W'| in {2,3}, outcome (3).

These cases exhaust the cross-endpoint exchange dichotomy.