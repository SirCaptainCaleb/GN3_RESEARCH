# A rooted eight-set has at least twenty-one Hamiltonian five-shells

## Statement

Let H be a boundary tournament on W=A disjoint-union {r}, where |A|=7. Let F_r be the family of triples T in binom(A,3) such that H[W-T] is Hamiltonian. Then |F_r|>=21. Equivalently, at least twenty-one of the thirty-five five-vertex subsets of W that contain r are Hamiltonian.

## Body

For each t in A, apply the rooted seven-set shell theorem 84ac56baf953 to the seven-set W-{t}=(A-{t}) union {r}, rooted at r. Its shell graph on A-{t} has at least nine edges. Thus for at least nine unordered pairs {a,b} subset A-{t}, the five-set W-{t,a,b} is Hamiltonian. Count incidences (t,T) with t in T and T in F_r. The preceding argument gives at least 7*9=63 incidences. Every good triple T is counted exactly three times, once for each t in T. Therefore 3|F_r|>=63 and |F_r|>=21.