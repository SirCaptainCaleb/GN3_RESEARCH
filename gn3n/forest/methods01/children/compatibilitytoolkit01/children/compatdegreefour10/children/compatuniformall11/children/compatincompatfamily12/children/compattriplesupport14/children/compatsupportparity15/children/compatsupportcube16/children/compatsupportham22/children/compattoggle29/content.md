# The one-split parity branch forces a symmetric extender-blocker toggle

## Statement

Assume the exactly-one-split branch of compatsupportham22, normalized so that R, S, R union {a}, S union {b}, R union {b,c}, and S union {a,c} are Hamiltonian. Then H being a counterexample forces each of S union {a}, R union {b}, R union {a,c}, and S union {b,c} to be non-Hamiltonian. Thus a individually Hamiltonizes R but not S, b individually Hamiltonizes S but not R, while adjoining c reverses the successful two-label side: {b,c} Hamiltonizes R but {a,c} does not, and {a,c} Hamiltonizes S but {b,c} does not.

## Body

# Proof

The Hamiltonian sets supplied by compatsupportham22 are

R,
S,
R union {a},
S union {b},
R union {b,c},
S union {a,c}.

We derive the four failures by complementary two-cover exclusion.

If S union {a} were Hamiltonian, then it would be disjoint from the already Hamiltonian set R union {b,c}, and the two sets partition V(H). They would therefore give a spanning two-cover of H, contradiction. Hence S union {a} is non-Hamiltonian.

If R union {b} were Hamiltonian, then together with the already Hamiltonian complementary set S union {a,c} it would two-cover H. Hence R union {b} is non-Hamiltonian.

If R union {a,c} were Hamiltonian, its complement S union {b} is already Hamiltonian, again giving a spanning two-cover. Hence R union {a,c} is non-Hamiltonian.

If S union {b,c} were Hamiltonian, its complement R union {a} is already Hamiltonian, again impossible. Hence S union {b,c} is non-Hamiltonian.

Collecting the positive and negative statements gives the toggle pattern:

on R:
R+a Hamiltonian,
R+b non-Hamiltonian,
R+bc Hamiltonian,
R+ac non-Hamiltonian;

on S:
S+b Hamiltonian,
S+a non-Hamiltonian,
S+ac Hamiltonian,
S+bc non-Hamiltonian.

Thus c reverses which of the two distinguished labels participates in the successful two-label enlargement on the two cores.