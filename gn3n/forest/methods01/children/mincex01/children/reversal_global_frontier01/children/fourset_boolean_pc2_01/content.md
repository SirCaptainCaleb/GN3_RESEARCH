# Hamiltonian complementary subsets force path-cover-two extensions

## Statement

Let H be a minimum counterexample, let X be any nonempty proper vertex set, and put K=V(H)-X. If S is a nonempty proper subset of X and H[X-S] is Hamiltonian, then H[K union S] is non-Hamiltonian with path-cover number exactly two. In particular, for every four-vertex set X, with no assumption on H[X], all fourteen states K union S indexed by nonempty proper S subset X have path-cover number exactly two.

## Body

Fix nonempty proper S subset X and assume H[X-S] is Hamiltonian. The set K union S is proper because X-S is nonempty. If H[K union S] were Hamiltonian, Hamilton paths on K union S and X-S would form a spanning two-cover of H, contradiction. Therefore H[K union S] is non-Hamiltonian. It is a proper induced subtournament of the minimum counterexample, so its path-cover number is at most two; non-Hamiltonicity makes it exactly two. If |X|=4, then X-S has order one, two, or three for every nonempty proper S, hence is automatically Hamiltonian. Thus all fourteen nontrivial proper extensions are pc2. The former non-Hamiltonian-four-set and matching-block hypotheses were unnecessary.