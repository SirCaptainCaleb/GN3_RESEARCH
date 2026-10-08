# Two neighboring shared failures force thirty-six mixed Hamiltonian five-sets — preserved pre-item development

Assume the monotone corridor has shared bridge labels at both neighboring cut pairs j=u and j=u+1, and that neither of the two original packet tests at either pair yields a two-cover. Let
A={x,y,c_1,c_2}, Z={c_{u+1},c_{u+2},c_{u+3},c_{u+4}}.
The four five-sets A+z, z in Z, are then all non-Hamiltonian.

Proof of this first assertion. The failure at j=u makes A+c_{u+1} and A+c_{u+3} non-Hamiltonian. The failure at j=u+1 makes A+c_{u+2} and A+c_{u+4} non-Hamiltonian. Each statement is a failed Hamiltonian deletion test for its actual shared bridge. QED.

The following structural density conclusion needs only this family of four bad five-sets, not the bridge orientations and not Hamiltonicity of A.

(1) Every five-set with three vertices from A and two vertices from Z is Hamiltonian. For a pair r,s in Z, A+r and A+s are the two bad deletions of the six-set A+r+s. Four-of-six forces all its other deletions, (A-w)+r+s with w in A, Hamiltonian. There are 4 times 6 =24 distinct such supports.

(2) At least twelve five-sets with two vertices from A and three vertices from Z are Hamiltonian. Fix a pair B in A. The six-set B+Z has at least four Hamiltonian five-deletions. Only two deletion supports have type one vertex of A plus all four Z vertices. Thus at least two of its other four five-subsets, of type B plus three vertices of Z, are Hamiltonian. Summing over the six pairs B gives at least twelve distinct supports of type 2|3.

The two classes are disjoint. Hence the eight-set A+Z contains at least thirty-six Hamiltonian mixed five-subsets, while its four subsets of type 4|1 are non-Hamiltonian. The reversed order (c_{u+4},c_{u+3},c_{u+2},c_{u+1}) is also a tight path, since the two relevant corridor statuses are zero. The density proof does not rely on this additional fact.

There is a graph description of the remaining bad supports of type 2|3. For a fixed triple D in Z, join two vertices a,b in A when {a,b}+D is non-Hamiltonian. This graph is triangle-free: on any three vertices B in A, the six-set B+D has three deletions of type 3|2 already known Hamiltonian by (1); four-of-six then forces at least one of its three deletions of type 2|3 Hamiltonian. Thus the three pairs in B cannot all be edges. Across the four triples D, each pair in A is bad for at most two D, by the count in (2).

These many Hamiltonian packets are verified alternatives available to a repair. They do not alone yield a two-cover of the full determining span: the complement of an arbitrary mixed five-set need not be one tight path, and deletion of internal path vertices cannot be treated as harmless. An attachment or compatible tail decomposition is still required. This records the extra structure forced by two simultaneous shared-cut failures without replacing the remaining rooted problem by a density claim.
