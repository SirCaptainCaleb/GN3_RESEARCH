# Two bad endpoint extensions of a four-side give a repartition or an interior lock

## Statement

Let H be a boundary tournament and let W|P|Q be a spanning three-cover with |W|=4. Write W=D union {w}, |D|=3, and let Q=(f,q_1,...,q_{q-2},g) have order q>=3. Suppose D union {f} and D union {g} are non-Hamiltonian. Put M=(q_1,...,q_{q-2}). Then F=D union {f,g} is Hamiltonian. Moreover either H[V(M) union {w}] is Hamiltonian, in which case W|Q has the legal pairwise repartition F | (M union {w}) and the change in quadratic potential on this pair is 10-2q, or H[V(M) union {w}] is non-Hamiltonian, in which case w is noninsertable into every position of the inherited path M.

## Body

Equip D with any tight Hamilton order. Since D union {f} and D union {g} are both non-Hamiltonian, the certified two-bad-four-extensions lemma in localextend01 gives a Hamilton path on F=D union {f,g}, with both endpoints in D. The supports F and V(M) union {w} are disjoint and partition V(W) union V(Q). If the second support is Hamiltonian, replacing W|Q by these two Hamilton paths is a legal pairwise repartition. Its component orders change from (4,q) to (5,q-1), so new Phi minus old Phi equals 25+(q-1)^2-16-q^2=10-2q. If V(M) union {w} is non-Hamiltonian, any insertion of w into the inherited tight path M would itself Hamiltonize that support, contradiction. Hence w is noninsertable in M. No extremality or minimum-counterexample hypothesis is used.