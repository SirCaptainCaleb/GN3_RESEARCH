# Every eight-vertex boundary tournament has at least twenty-eight Hamiltonian four-sets and 56 adjacent pairs

## Statement

Every boundary tournament on eight vertices has at least 28 Hamiltonian four-vertex sets and at least 56 unordered pairs of distinct Hamiltonian four-sets whose intersection has order three.

## Body

Fix an unordered pair {u,v}. By 1000615, the other six vertices split into two fixed-pair orientation classes, and every two vertices from one class complete {u,v} to a Hamiltonian four-set. If the class sizes are s and 6-s, the number of same-class exterior pairs is C(s,2)+C(6-s,2)>=6. Summing over the 28 unordered pairs {u,v} gives at least 168 incidences (T,F), where T is an unordered pair contained in a Hamiltonian four-set F and the complementary pair F-T lies in one fixed-pair orientation class relative to T. Any four-set has only six unordered pairs, so it contributes to at most six such incidences. Hence there are at least 168/6=28 Hamiltonian four-sets.

For each triple T let d_T be the number of Hamiltonian four-sets containing T. Then sum_T d_T=4|H_4|>=112 over the 56 triples. Two distinct four-sets intersect in three vertices exactly when they contain the same triple, so the number of unordered adjacent pairs is sum_T C(d_T,2). Among nonnegative integers d_T with total at least 112, convexity gives the minimum when all d_T=2, yielding at least 56 adjacent pairs.