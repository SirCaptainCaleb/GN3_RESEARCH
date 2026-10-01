# Two Hamiltonian four-sets meeting in three vertices yield a Hamiltonian five-set or four Hamiltonian four-subsets

## Statement

Let H be a minimum counterexample, and let W,W' be distinct Hamiltonian four-vertex sets such that H-W and H-W' are non-Hamiltonian with path-cover number two and |W∩W'|=3. Put S=W∪W'. Then either H[S] is Hamiltonian, or at least four of the five four-subsets Z of S are Hamiltonian; for every such Hamiltonian Z, H-Z is non-Hamiltonian with path-cover number two.

## Body

The set S has order five. If H[S] is Hamiltonian there is nothing to prove. Assume H[S] is non-Hamiltonian. By the five-vertex small-set theorem, a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Hence at least four of the five sets Z⊂S of order four are Hamiltonian. Fix such a Z. Since H is a minimum counterexample and Z is a proper Hamiltonian set, H-Z cannot be Hamiltonian: otherwise a Hamilton path on Z together with a Hamilton path on H-Z would form a spanning two-path cover of H. Minimum-counterexample calculus therefore gives pc(H-Z)=2, and H-Z is non-Hamiltonian. Thus each Hamiltonian four-subset Z is a Hamiltonian four-set with non-Hamiltonian path-cover-two complement. The original W,W' are two members of this collection.