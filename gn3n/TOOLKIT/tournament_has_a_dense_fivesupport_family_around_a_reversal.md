# Every large boundary tournament has a dense five-support family around a reversal

**Summary:** Every large boundary tournament has a dense five-support family around a reversal

## Statement

Let H be a boundary tournament of order n>=7. Then H has a genuine reversing tight triple T such that, writing X=V(H)-V(T), m=n-3, and joining distinct y,z in X when H[V(T) union {y,z}] is Hamiltonian, the resulting graph J_T satisfies alpha(J_T)<=2 and |E(J_T)|>=binom(m,2)-floor(m^2/4). Moreover some y in X has degree at least floor((m-1)/2)=floor((n-4)/2), so that many Hamiltonian five-sets share the four-set V(T) union {y}. If H is a minimum counterexample, every edge yz of J_T gives a proper Hamiltonian five-set whose complement is non-Hamiltonian with path-cover number two.

## Body

By 1d746da79d34 choose a genuine reversing tight triple T; in particular T itself is a tight three-vertex path. Put X=V(H)-V(T), m=|X|. Let B be the graph on X in which yz is an edge exactly when H[V(T) union {y,z}] is non-Hamiltonian. The bad-extension theorem in localextend01, applied to the tight three-path T, says that B is triangle-free. Hence Mantel's theorem gives |E(B)|<=floor(m^2/4). Its complement J_T therefore satisfies |E(J_T)|>=binom(m,2)-floor(m^2/4), and triangle-freeness of B is exactly alpha(J_T)<=2. For the degree bound, if m=2k then the displayed edge lower bound is k(k-1), so the average degree is at least k-1=floor((m-1)/2). If m=2k+1 the bound is k^2, so the average degree is 2k^2/(2k+1)>k-1; integrality gives a vertex of degree at least k=floor((m-1)/2). Each neighbor z of such a vertex y makes V(T) union {y,z} Hamiltonian by definition. Finally suppose H is a minimum counterexample. Then n>10, so every such five-set W is proper. If H-W were Hamiltonian, a Hamilton path on W together with one on H-W would form a spanning two-cover, impossible. Minimum-counterexample calculus therefore gives path-cover number two for H-W.

## Metadata

- ID: tournament_has_a_dense_fivesupport_family_around_a_reversal
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
