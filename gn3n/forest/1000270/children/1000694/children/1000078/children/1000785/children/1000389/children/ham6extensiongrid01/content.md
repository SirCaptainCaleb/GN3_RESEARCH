# Hamiltonian six-sets force a dense family of one- and two-label path-cover-two extensions

## Statement

Let H be a minimum counterexample, let U be a proper Hamiltonian six-vertex set, and put K=H-U. Assume H[K] is non-Hamiltonian, hence has path-cover number two. Let D={d in U : H[U-d] is Hamiltonian}, and let J be the graph on U in which de is an edge exactly when H[U-{d,e}] is Hamiltonian. Then |D|>=4; H[K+d] is non-Hamiltonian with path-cover number two for every d in D; J has at least six edges; H[K+d+e] is non-Hamiltonian with path-cover number two for every edge de of J; and every d in D has degree at least two in J. Consequently, if |D|>=5 then J[D] has minimum degree at least one. If |D|=4 and J[D] has no edge, writing B=U-D, every D-B pair is an edge of J; thus J contains the complete bipartite graph K_{4,2} with bipartition D|B, has no edge inside D, and only the edge inside B remains undetermined.

## Body

# Proof

By the four-of-six theorem, at least four one-vertex deletions of U are Hamiltonian, so |D|>=4. Fix d in D. If K+d were Hamiltonian, a Hamilton path on K+d together with a Hamilton path on U-d would form a spanning two-cover of H. Hence K+d is non-Hamiltonian. Since it is a proper induced subtournament of the minimum counterexample, its path-cover number is two.

Now define J on U by de in E(J) exactly when U-{d,e} is Hamiltonian. Every five-subset S of U contains at least two Hamiltonian four-subsets: if S is Hamiltonian, the five-set four-subset bound in smallset01 leaves at most three non-Hamiltonian four-subsets, while if S is non-Hamiltonian, at most one of its four-subsets is non-Hamiltonian. Summing over the six five-subsets of U gives at least twelve incidences (S,W) with W a Hamiltonian four-subset of S. Each four-subset W of U lies in exactly two five-subsets, so U has at least six Hamiltonian four-subsets. Therefore |E(J)|>=6.

For any edge de of J, if K+d+e were Hamiltonian, its Hamilton path together with a Hamilton path on U-{d,e} would two-cover H. Thus K+d+e is non-Hamiltonian and, by minimality, has path-cover number two.

Fix d in D. The five-set U-d is Hamiltonian. By the five-set four-subset bound, at least two of its five four-subsets are Hamiltonian. Equivalently, there are at least two vertices e in U-{d} for which U-{d,e} is Hamiltonian. Therefore deg_J(d)>=2.

If |D|>=5, at most one vertex of U lies outside D, so every d in D has at least one neighbor in D. Hence delta(J[D])>=1.

Finally suppose |D|=4 and J[D] has no edge. Put B=U-D, so |B|=2. Since every d in D has degree at least two and has no neighbor in D, both vertices of B are adjacent in J to every d in D. Thus all eight D-B edges belong to J. The only edge whose status is not determined by these conclusions is the edge joining the two vertices of B. Equivalently, J contains K_{4,2} with bipartition D|B and has no edge inside D. ∎
