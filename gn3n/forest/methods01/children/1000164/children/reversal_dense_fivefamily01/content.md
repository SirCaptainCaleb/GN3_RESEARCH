# Every genuine reversal lies in a dense family of Hamiltonian five-supports

## Statement

Let H be a minimum counterexample of order n. Then there is a genuine reversing tight triple T on three vertices. Put X=V(H)-V(T), m=n-3, and let J_T be the graph on X in which distinct y,z are adjacent exactly when H[V(T) union {y,z}] is Hamiltonian. Then alpha(J_T)<=2 and
|E(J_T)| >= binom(m,2)-floor(m^2/4).
For every edge yz of J_T, W=V(T) union {y,z} is a proper Hamiltonian five-vertex support containing the same genuine reversal, and H-W is non-Hamiltonian with path-cover number two.

## Body

By 34583959c437, H contains a genuine reversing tight triple T. Let X=V(H)-V(T) and m=|X|=n-3.

Apply the certified bad-extension theorem in localextend01 to the tight three-vertex path T and the exterior set X. Let B be the graph on X in which yz is an edge exactly when H[V(T) union {y,z}] is non-Hamiltonian. That theorem says B is triangle-free. Hence, by Mantel's theorem,
|E(B)| <= floor(m^2/4).
The graph J_T in the statement is the complement of B on X, so
|E(J_T)| = binom(m,2)-|E(B)| >= binom(m,2)-floor(m^2/4).
Since B is triangle-free, no three vertices of X are pairwise nonadjacent in J_T, and therefore alpha(J_T)<=2.

Now fix yz in E(J_T) and put W=V(T) union {y,z}. By definition H[W] is Hamiltonian. Minimum-counterexample calculus gives n>10, so W is proper. If H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H, impossible. Thus H-W is non-Hamiltonian. Since it is a proper induced subtournament of a minimum counterexample, its path-cover number is at most two; non-Hamiltonicity makes that number exactly two.

Every such W contains the original reversing tight triple T, so the same genuine reversal is carried by every member of this dense family. ∎
