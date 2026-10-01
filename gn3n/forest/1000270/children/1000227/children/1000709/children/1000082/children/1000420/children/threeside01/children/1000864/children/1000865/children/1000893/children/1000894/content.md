# Persistent-defect shells carry degree-counted common-core transport packages at every order

## Statement

In a rooted seven-vertex shell W with shell graph Omega from the three-side fixed-defect setup, fix distinct persistent defects z,z'. Let epsilon=1 when zz' is an edge of Omega and epsilon=0 otherwise, and let q be the number of vertices of W-{z,z'} adjacent to neither z nor z'. Then the number of common neighbors c outside {z,z'} is exactly deg_Omega(z)+deg_Omega(z')-2epsilon-5+q, and hence at least deg_Omega(z)+deg_Omega(z')-2epsilon-5. Equality in the degree lower bound holds exactly when every other shell vertex is adjacent to at least one of z,z'. For every common neighbor c, both five-sets W-{z,c} and W-{z',c} are Hamiltonian with common four-core W-{z,z',c}; hence U_c=W-{c} carries the full common-four-core transport dichotomy of 1000476. In particular delta(Omega)>=4 gives at least one transport package when z,z' are adjacent and at least three when they are nonadjacent. If the ambient minimum counterexample has order at least eighteen, every package additionally yields order disagreement or strict quadratic descent.

## Body

Let S=V(Omega)-{z,z'}, so |S|=5, and put A=N(z)∩S and B=N(z')∩S. Let q=|S-(A∪B)|, the number of vertices in S adjacent to neither z nor z'. Then |A|=deg(z)-epsilon and |B|=deg(z')-epsilon, while inclusion-exclusion gives
|A∩B|=|A|+|B|-|A∪B|
=deg(z)+deg(z')-2epsilon-(5-q)
=deg(z)+deg(z')-2epsilon-5+q.
Thus the previous degree bound is the q>=0 corollary, and equality holds exactly when q=0, i.e. every vertex of S is adjacent to at least one of z,z'.

For c in A∩B, the definition of the shell graph gives Hamiltonicity of W-{z,c} and W-{z',c}. These two five-sets share the four-core W-{z,z',c}, so 1000476 applies directly to U_c=W-{c}. This conclusion uses no ambient-order threshold.

The minimum-degree corollaries follow by substituting delta(Omega)>=4. Finally, in ambient order n>=18, if U_c is non-Hamiltonian then its four-Hamiltonian-deletion branch yields order disagreement, while if U_c is Hamiltonian then its complement is non-Hamiltonian with path-cover number two and ham6_large_escape01 yields order disagreement or strict quadratic descent.
