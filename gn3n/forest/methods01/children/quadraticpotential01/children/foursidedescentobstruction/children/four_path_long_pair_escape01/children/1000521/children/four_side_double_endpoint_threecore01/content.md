# The hard four-side six-set has two common three-cores extended by both long endpoints

## Statement

Let H be a boundary tournament, let X be a Hamiltonian four-set, and let a,b be distinct vertices outside X. Suppose X union {a} and X union {b} are non-Hamiltonian. Then there exist at least two distinct vertices x in X such that both (X-{x}) union {a} and (X-{x}) union {b} are Hamiltonian. In particular, in the non-Hamiltonian hard branch of a25b748fb338 with a=p_1 and b=p_m, at least two distinct three-vertex cores of X extend Hamiltonianly with either endpoint of the long path.

## Body

Apply the certified five-vertex small-set theorem smallset01 to X union {a}. Since this five-set is non-Hamiltonian, at most one of its five four-subsets is non-Hamiltonian. One four-subset is X itself, which is Hamiltonian. Hence among the four subsets (X-{x}) union {a}, x in X, at least three are Hamiltonian. Let I_a be the corresponding set of omitted labels, so |I_a|>=3. Likewise |I_b|>=3 for X union {b}. Since |X|=4, |I_a intersect I_b|>=2. Every x in the intersection gives both endpoint extensions.
