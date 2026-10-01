# Persistent-defect shell escape has an exact degree-sensitive multiplicity bound

## Statement

Let H be a minimum counterexample of order n>=18 in the three-side fixed-defect transport setup. Fix distinct persistent defects z,z' and one rooted seven-set shell W_j with shell graph Omega_j. Let epsilon=1 if zz' is an edge of Omega_j and epsilon=0 otherwise. Then at least
deg_{Omega_j}(z)+deg_{Omega_j}(z')-2 epsilon-5
distinct vertices c in W_j-{z,z'} have the property that U_c=W_j-{c} forces either explicit order disagreement on Hamilton paths in U_c or a spanning three-cover in a pairwise-repartition component with strictly smaller quadratic potential. In particular, since delta(Omega_j)>=4, there is always at least one such witness, and there are at least three when z,z' are nonadjacent.

## Body

Let S=V(Omega_j)-{z,z'}, so |S|=5. Write
A=N_{Omega_j}(z) intersect S,
B=N_{Omega_j}(z') intersect S.
If epsilon records whether zz' is an edge, then
|A|=deg(z)-epsilon
and
|B|=deg(z')-epsilon.
Therefore
|A intersect B| >= |A|+|B|-|S|
=deg(z)+deg(z')-2epsilon-5.

Fix c in A intersect B. Since c is adjacent in the shell graph to both persistent defects, the five-sets W_j-{z,c} and W_j-{z',c} are Hamiltonian and share the four-core W_j-{z,z',c}. Hence the six-set U_c=W_j-{c} satisfies the common-four-core six-set transport dichotomy.

If U_c is non-Hamiltonian, its Hamiltonian-deletion set has size at least four, so the certified four-good-six interface yields order disagreement between Hamilton paths on distinct Hamiltonian five-deletions of U_c.

If U_c is Hamiltonian, its complement in H is non-Hamiltonian with path-cover number two. Since n>=18, the certified Hamiltonian-six large-escape theorem yields either order disagreement or a spanning three-cover in a pairwise-repartition component with strictly smaller quadratic potential.

Thus every c in A intersect B gives an independent shell escape witness, and distinct c give distinct six-sets U_c. The displayed degree bound follows. Since delta(Omega_j)>=4, when z,z' are adjacent the bound is at least 4+4-2-5=1, and when they are nonadjacent it is at least 4+4-5=3.
