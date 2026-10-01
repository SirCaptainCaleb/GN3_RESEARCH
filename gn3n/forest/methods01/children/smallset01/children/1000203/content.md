# Two bad extensions of a Hamiltonian five-set force two-for-two Hamiltonian replacements

## Statement

Let H be a boundary tournament, let X be a Hamiltonian five-vertex set, and let e,f be distinct vertices outside X. Suppose X union {e} and X union {f} are both non-Hamiltonian. Then there exists x in X such that both (X-{x}) union {e} and (X-{x}) union {f} are Hamiltonian, and for at least two distinct vertices z in X-{x}, the five-set (X-{x,z}) union {e,f} is Hamiltonian.

## Body

Apply the four-of-six theorem from smallset01 to the six-set X union {e}. At least four of its six vertex deletions are Hamiltonian. Deleting e leaves X, which is Hamiltonian, so at least three vertices x in X satisfy
(X-{x}) union {e}
Hamiltonian.

Let I_e be the set of such vertices. Thus |I_e|>=3. Define I_f analogously from the non-Hamiltonian six-set X union {f}; again |I_f|>=3.

Since X has five vertices,
|I_e intersect I_f| >= |I_e|+|I_f|-|X| >= 1.
Choose x in I_e intersect I_f. Then both
(X-{x}) union {e}
and
(X-{x}) union {f}
are Hamiltonian.

Now put
S=(X-{x}) union {e,f}.
This is a six-set. Deleting f leaves (X-{x}) union {e}, and deleting e leaves (X-{x}) union {f}; hence e and f are already two Hamiltonian deletion labels of S.

Apply four-of-six once more to S. At least four of its six vertex deletions are Hamiltonian. Since e and f account for at most two of them, at least two distinct vertices
z in X-{x}
also satisfy
S-{z}=(X-{x,z}) union {e,f}
Hamiltonian.

Thus one common first deletion x works for both bad one-vertex extensions, and at least two choices of a second deletion z permit simultaneous replacement of x,z by e,f while preserving Hamiltonicity on five vertices. ∎
