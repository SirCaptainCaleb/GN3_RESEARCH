# Two shared-endpoint Hamiltonian five-sets force a distance-one window or a forked opposite-end four-window pair

## Statement

Let D be a three-vertex set and let e,f,g be distinct vertices outside D. Suppose D union {e,f} and D union {e,g} are Hamiltonian five-sets. Then either at least one of D union {e}, D union {f}, D union {g} is Hamiltonian, or there exists d in D such that both (D-{d}) union {e,f} and (D-{d}) union {e,g} are Hamiltonian four-sets.

## Body

Apply sharedendpointmigration_recomp01 to F_f=D union {e,f}. If D union {e} or D union {f} is Hamiltonian, the first alternative holds. Otherwise at least two labels d in D make (D-{d}) union {e,f} Hamiltonian. Apply the same argument to F_g=D union {e,g}. Unless D union {e} or D union {g} is Hamiltonian, at least two labels d in D make (D-{d}) union {e,g} Hamiltonian. Two subsets of a three-set of size at least two intersect, so some d works for both.