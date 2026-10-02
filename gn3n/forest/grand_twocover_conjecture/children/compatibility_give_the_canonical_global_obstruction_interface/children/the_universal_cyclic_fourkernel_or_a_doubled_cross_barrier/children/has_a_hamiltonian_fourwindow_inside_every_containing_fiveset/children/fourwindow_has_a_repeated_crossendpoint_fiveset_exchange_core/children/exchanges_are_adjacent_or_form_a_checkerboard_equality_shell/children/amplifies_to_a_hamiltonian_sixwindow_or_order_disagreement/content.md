# The shared-endpoint exchange branch amplifies to a Hamiltonian six-window or order disagreement

## Statement

Assume branch (A) of 27a05b61e8c3. Thus for some w in W and, after symmetry, some endpoint e of P, both cross pairs (e,q_0) and (e,q_s) are good. Put D=W-{w} and
U=D union {e,q_0,q_s}.
Then either H[U] is Hamiltonian, in which case U is a proper Hamiltonian six-vertex support and H-U is non-Hamiltonian of path-cover number two, or H[U] is non-Hamiltonian and Hamiltonian vertex-deletion paths of U necessarily exhibit order disagreement on a common pair. Hence the shared-endpoint branch always amplifies to a bounded Hamiltonian six-window or an explicit order-disagreement witness.

## Body

The two good cross pairs mean precisely that
U-{q_s}=D union {e,q_0}
and
U-{q_0}=D union {e,q_s}
are Hamiltonian five-sets.

If U itself is Hamiltonian, minimum-counterexample complement calculus gives the first outcome.

Assume U is non-Hamiltonian. The certified four-of-six theorem in smallset01 says that every six-vertex boundary tournament has at least four vertices v for which U-{v} is Hamiltonian. Thus U has at least four Hamiltonian vertex deletions. Apply astra004fourgooddisagree to the non-Hamiltonian tournament H[U]: for arbitrary Hamilton paths chosen on those Hamiltonian deletions, some two induce different relative orders on a common vertex pair. This is the second outcome.