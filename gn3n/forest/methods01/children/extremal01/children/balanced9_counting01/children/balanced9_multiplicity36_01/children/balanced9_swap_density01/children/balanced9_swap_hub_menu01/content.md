# A nine-vertex balanced cover has two independent swaps or a four-fold common-core swap star

## Statement

Every nine-vertex boundary tournament has a Hamiltonian 4|5 cover A|B for which the reciprocal-swap graph J subseteq A x B has at least four edges, where ab is an edge exactly when (A-{a}) union {b} and (B-{b}) union {a} are both Hamiltonian. Consequently at least one of the following holds: (1) J contains two vertex-disjoint edges, giving two independent reciprocal one-for-one balanced swaps; (2) some a in A is adjacent to at least four distinct vertices b in B, so the fixed three-core C=A-{a} has at least four Hamiltonian four-extensions C+b and the reciprocal five-sets (B-{b})+a are Hamiltonian; (3) some b in B is adjacent to all four vertices a in A, so the fixed four-core D=B-{b} has all four Hamiltonian five-extensions D+a and every reciprocal four-set (A-{a})+b is Hamiltonian.

## Body

By balanced9_swap_density01, some balanced cover A|B has at least four Johnson-neighbors among balanced covers. Every such neighbor replaces exactly one a in A by one b in B on the four-side; because the complementary five-side simultaneously replaces b by a, it is exactly an edge ab of the reciprocal-swap graph J subseteq A x B. Thus e(J)>=4.

If J has matching number at least two, outcome (1) holds. Otherwise its matching number is one. Any bipartite graph with matching number one has all edges incident with a common vertex. If the common vertex lies in A, it is some a adjacent to at least four distinct b in B because J has at least four edges, giving outcome (2). If the common vertex lies in B, it is some b adjacent to at least four distinct a in A; since |A|=4, it is adjacent to every a, giving outcome (3). The Hamiltonicity assertions are exactly the definition of reciprocal-swap adjacency.
