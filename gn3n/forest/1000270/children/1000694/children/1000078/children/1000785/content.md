# Every vertex has a Hamiltonian four-window inside every containing five-set

## Statement

Let H be a minimum counterexample, let x be any vertex, and let F be any five-vertex subset of V(H) containing x. Then some four-vertex subset W of F containing x induces a Hamiltonian boundary tournament. Consequently H-W is non-Hamiltonian and has path-cover number two. In particular, for any deletion state H-x=P|Q, the Hamiltonian four-window containing x may be chosen inside any prescribed five-set containing x; no failed-insertion or deletion-state taxonomy is needed to produce it.

## Body

Let H be a minimum counterexample, let x∈V(H), and let F⊆V(H) be any five-set containing x.

Apply the certified five-set four-subset theorem in smallset01.

If H[F] is Hamiltonian, at least two of the five four-subsets of F are Hamiltonian. Exactly one four-subset omits x, so at least one Hamiltonian four-subset W contains x.

If H[F] is non-Hamiltonian, at most one of its five four-subsets is non-Hamiltonian. Hence at least four are Hamiltonian, while again only one omits x. Thus at least three Hamiltonian four-subsets contain x.

Therefore in either case there is a four-set W⊂F with x∈W and H[W] Hamiltonian.

The set W is proper. If H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H, contradicting that H is a counterexample. By the minimum-counterexample calculus, every proper induced subtournament has path-cover number at most two. Hence H-W is non-Hamiltonian and has path-cover number exactly two.

The conclusion is stronger than the previous deletion-state formulation: F is arbitrary. In particular, once a vertex x is fixed, no deletion cover, failed-insertion normal form, cyclic-kernel branch, or doubled-cross branch is needed merely to obtain a Hamiltonian four-window containing x.