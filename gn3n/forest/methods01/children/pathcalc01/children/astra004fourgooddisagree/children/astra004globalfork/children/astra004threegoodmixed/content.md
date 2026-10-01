# Three Hamiltonian complement deletions already force direct mixed crossing or order disagreement

## Statement

Let H be a minimum counterexample, let A=(a_0,...,a_{lambda-1}) be a globally longest tight path, put U=V(H)-V(A), and D={u in U:H[U-u] is Hamiltonian}. If |D|>=3, choose arbitrary exact two-covers G_0 of H-a_0 and G_1 of H-a_{lambda-1}. Then there exists t in D such that, for at least one endpoint y in {a_0,a_{lambda-1}}, either G_y contains an ordinary path edge directly joining U-{t} to A-{y}, or the two endpoint probes expose explicit relative-order disagreement, hence a reversed common edge, reversing tight triple, or vertex-simple tight cycle. Consequently the Astra-004 global fork sharpens to: either |D|<=2 and every u in U-D forces mixed deletion covers across A|(U-u), or |D|>=3 and the fixed-A family already yields direct mixed support/order disturbance.

## Body

# Proof

For each t in D choose a Hamilton path on U-{t}; together with A this gives the exact canonical deletion cover F_t=(U-{t})|A of H-t. These covers are pairwise support-compatible: after deleting two labels t,t prime their common support classes are U-{t,t prime} and A.

Choose any three distinct labels D_0 subseteq D. Apply the certified support-compatible deletion-family theorem e92b0f47c1a6 with X=U, Q=A, and family {F_t:t in D_0}. Since |D_0|=3, among the three labels there is a single t for which F_t is support-incompatible with both chosen endpoint covers G_0,G_1.

Now apply 5e8a13d9c742 to this synchronized endpoint-incompatible state. Its only genuine outcomes are: a direct ordinary edge in one endpoint cover joining X-{t}=U-{t} to Q-{y}=A-{y}, or explicit relative-order disagreement. Pathcalc01 converts the latter to the standard reversed-edge / reversing-triple / tight-cycle witness.

For the final fork, if |D|<=2 then 6c4d3f1a8e27 already proves that every u in U-D has every exact cover of H-u mixing the cut A|(U-u). If |D|>=3 the first paragraph applies. ∎