# A non-Hamiltonian six-set yields one- and two-label path-cover-two extensions

## Statement

Let H be a minimum counterexample and let K be a non-Hamiltonian six-vertex induced subtournament. Put D={d in V(K): H[K-d] is Hamiltonian} and L=H-K. Then |D|>=4. For every d in D, H[L union {d}] is non-Hamiltonian with path-cover number two. Define a graph J on D by de in E(J) exactly when H[K-{d,e}] is Hamiltonian. Then delta(J)>=1, and for every edge de of J the induced subtournament H[L union {d,e}] is non-Hamiltonian with path-cover number two. Consequently, if H[L] is non-Hamiltonian, then every edge de of J yields four induced subtournaments L, L+d, L+e, L+d+e in which all four induced subtournaments are non-Hamiltonian with path-cover number two.

## Body

By the four-of-six theorem, the Hamiltonian-deletion set D has order at least four. Fix d in D. Since K-d is Hamiltonian, if L+d were Hamiltonian then a Hamilton path on K-d together with a Hamilton path on L+d would form a spanning two-cover of H, contradicting that H is a counterexample. Thus L+d is non-Hamiltonian. It is a proper induced subtournament of the minimum counterexample H, so minimum-counterexample calculus gives path-cover number at most two; non-Hamiltonicity forces path-cover number two. This holds for every d in D.

Now fix d in D. The prescribed-Hamiltonian-K4-overlap theorem in extremal01, applied to the non-Hamiltonian six-set K and the prescribed Hamiltonian deletion d, gives some e in D-{d} for which K-{d,e} is Hamiltonian. Hence every vertex d of J has a neighbor, so delta(J)>=1. For any edge de of J, K-{d,e} is Hamiltonian. If L+d+e were Hamiltonian, its Hamilton path together with a Hamilton path on K-{d,e} would two-cover H. Therefore L+d+e is non-Hamiltonian, and minimum-counterexample calculus again gives path-cover number two.

Finally suppose L itself is non-Hamiltonian. Since L is a proper induced subtournament of H, it too has path-cover number two. Thus for every edge de of J the four induced subtournaments on supports L, L+d, L+e, and L+d+e are all non-Hamiltonian with path-cover number two, so all four induced subtournaments have path-cover number two and are non-Hamiltonian. No choice of Hamilton orders is involved.