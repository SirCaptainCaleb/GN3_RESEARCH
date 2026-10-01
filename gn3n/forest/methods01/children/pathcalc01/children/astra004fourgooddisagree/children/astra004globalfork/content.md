# A longest-path complement is either deletion-sparse or intrinsically order-disturbed

## Statement

Let H be a minimum counterexample, let A be a globally longest tight path, and put U=V(H)-V(A). Define D={u in U:H[U-u] is Hamiltonian}. Then exactly one of the following two regimes holds. (I) |D|<=3; for every u in U-D, every exact two-cover of H-u has at least two ordinary path edges crossing the cut A|(U-u). (II) |D|>=4; for arbitrary Hamilton tight paths P_u on U-u, u in D, some pair P_u,P_v has relative-order disagreement, hence yields a reversed common ordered edge, a reversing tight triple, or a vertex-simple tight cycle inside U. Moreover, in regime (II), choosing exact covers at the two endpoints of A, one can choose u in D whose fixed-A deletion state A|(U-u) is support-incompatible with both endpoint covers whenever |D|>=3.

## Body

# Proof

By the longest-path complement theorem 6c4d3f1a8e27, U is non-Hamiltonian and has path-cover number two. If |D|<=3, then for every u in U-D the set U-u is non-Hamiltonian, and the same theorem proves that every exact two-cover of H-u has at least two ordinary crossings across A|(U-u). This is regime (I).

Assume instead |D|>=4. Apply astra004fourgooddisagree to the non-Hamiltonian tournament H[U] and the good deletion set D. For arbitrary Hamilton paths P_u on U-u, some two chosen deletion paths disagree in relative order, and pathcalc01 gives the reversed-edge / reversing-triple / tight-cycle alternatives. This is regime (II).

Finally 6c4d3f1a8e27 shows that each exact cover of an endpoint deletion H-a is support-compatible with at most one fixed-A state A|(U-u). Since |D|>=3 in regime (II), the two endpoint covers exclude at most two good labels in total, so some u in D is support-incompatible with both. ∎