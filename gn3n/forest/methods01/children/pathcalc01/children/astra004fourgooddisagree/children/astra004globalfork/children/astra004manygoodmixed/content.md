# Many Hamiltonian complement deletions force a direct mixed longest-path crossing or order disagreement

## Statement

Let H be a minimum counterexample, A=(a_0,...,a_{lambda-1}) a globally longest tight path, U=V(H)-V(A), and D={u in U:H[U-u] is Hamiltonian}. If |D|>=4, choose arbitrary exact two-covers G_0 of H-a_0 and G_1 of H-a_{lambda-1}. Then there exists t in D such that, for at least one endpoint y in {a_0,a_{lambda-1}}, either G_y contains an ordinary path edge directly joining U-{t} to A-{y}, or the two endpoint probes expose explicit relative-order disagreement, hence a reversed common ordered edge, a reversing tight triple, or a vertex-simple tight cycle.

## Body

# Proof

Choose any three distinct labels D_0 subset D. For each t in D_0, the fixed-A deletion state
F_t=(U-{t})|A
is an exact two-cover of H-t: U-t is Hamiltonian by definition of D, A is Hamiltonian, and H-t cannot itself be Hamiltonian in a minimum counterexample.

The family {F_t:t in D_0} is pairwise support-compatible: after deleting two labels s,t in D_0, both induced covers have the same support partition (U-{s,t})|A. Also U is non-Hamiltonian, since otherwise U together with A would two-cover H. Thus the support-compatible deletion-family theorem e92b0f47c1a6 applies with X=U and Q=A.

Choose the endpoint covers G_0,G_1. Since |D_0|=3, e92b0f47c1a6 gives a single t in D_0 such that F_t is support-incompatible with both endpoint covers. The strengthening 5e8a13d9c742 then says that synchronized endpoint incompatibility has only two genuine outcomes: either one endpoint cover contains a direct ordinary edge between X-{t}=U-{t} and Q-{y}=A-{y}, or the endpoint probes produce explicit relative-order disagreement. In the latter case pathcalc01 yields the reversed-edge / reversing-triple / tight-cycle alternatives. ∎
