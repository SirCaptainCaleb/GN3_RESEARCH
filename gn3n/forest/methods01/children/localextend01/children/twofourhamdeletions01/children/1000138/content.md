# Any two disjoint four-sets force a dense mixed three-label path-cover-two family in a minimum counterexample

## Statement

Let H be a minimum counterexample, let A and B be any disjoint four-vertex sets, and put R=V(H)-(A union B). For every two-set T subset A there are at least two vertices b in B such that H[R union T union {b}] is non-Hamiltonian with path-cover number two. Symmetrically, for every two-set U subset B there are at least two vertices a in A such that H[R union U union {a}] is non-Hamiltonian with path-cover number two. Consequently there are at least twelve such extensions of type 2A+1B and at least twelve of type 1A+2B; some fixed b in B occurs with at least three of the six pairs T, and symmetrically some fixed a in A occurs with at least three pairs U.

## Body

Fix a two-set T subset A and put S=A-T, so |S|=2. Apply twofourhamdeletions01 to the disjoint sets S and B. For at least two b in B, the five-set W=S union (B-{b}) is Hamiltonian. Since a minimum counterexample has order greater than ten, W is proper. Its complement is exactly R union T union {b}; minimum-counterexample calculus therefore makes that complement non-Hamiltonian with path-cover number two. Interchanging A and B gives the symmetric assertion.

There are six two-sets T in A and at least two successful labels b for each, giving at least twelve distinct incidences of type 2A+1B. The symmetric count gives at least twelve incidences of type 1A+2B. Averaging the first twelve incidences over the four labels of B gives one b incident with at least three A-pairs; the other statement is symmetric. No Hamiltonicity assumption on A or B is used.
