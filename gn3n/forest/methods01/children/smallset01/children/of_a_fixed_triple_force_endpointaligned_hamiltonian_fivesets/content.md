# Bad four-extensions of a fixed triple force endpoint-aligned Hamiltonian five-sets

## Statement

Let H be a boundary tournament, let T be a three-vertex set, and let B be a set of vertices disjoint from T such that H[T union {u}] is non-Hamiltonian for every u in B. Then for every distinct u,v in B, the five-set S=T union {u,v} is Hamiltonian, and every Hamilton path of H[S] has both endpoints in T.

Consequently, if |B|=m, choose one Hamilton path on T union {u,v} for every pair {u,v} subset B and label the pair {u,v} by the unordered pair of endpoints of the chosen path. Some endpoint pair E subset T occurs for at least binom(m,2)/3 pairs, and some u in B belongs to at least ceil((m-1)/3) such pairs with the same endpoint pair E.

If H is a minimum counterexample, then every one of these Hamiltonian five-sets has non-Hamiltonian complement of path-cover number exactly two.

## Body

Fix distinct u,v in B and put S=T union {u,v}. By hypothesis, the two four-subsets S-{u}=T union {v} and S-{v}=T union {u} are both non-Hamiltonian.

The five-vertex small-set theorem in smallset01 says that a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Hence S cannot be non-Hamiltonian. Thus H[S] has a Hamilton path.

Let R be any Hamilton path of H[S]. Deleting either endpoint of R leaves a Hamilton path on the remaining four vertices. Since S-{u} and S-{v} are non-Hamiltonian, neither u nor v can be an endpoint of R. Both endpoints therefore lie in T. This proves the structural assertion, including the stronger fact that every Hamilton order of S has its two endpoints in T.

Now assume |B|=m. For each unordered pair {u,v} choose one Hamilton path of H[T union {u,v}] and label {u,v} by its unordered endpoint pair, which is one of the three two-subsets of T. One label class contains at least binom(m,2)/3 pairs. In the graph on B formed by that class, the average degree is at least
2 binom(m,2)/(3m)=(m-1)/3.
Hence some u in B has degree at least ceil((m-1)/3), giving the stated fixed-endpoint star.

Finally suppose H is a minimum counterexample. Each five-set S above is proper. Its complement has path-cover number at most two by minimum-counterexample calculus. The complement cannot be Hamiltonian, because a Hamilton path on S together with a Hamilton path on its complement would two-cover H. Therefore the complement is non-Hamiltonian with path-cover number exactly two.