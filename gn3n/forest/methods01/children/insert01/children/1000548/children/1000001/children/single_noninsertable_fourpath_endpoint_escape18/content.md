# Above order seventeen one noninsertable four-path endpoint already reaches disagreement or descent

## Statement

Let H be a minimum counterexample of order at least eighteen. Let S=(u,s_1,s_2,v) be a tight four-path such that H-S is non-Hamiltonian with path-cover number two, and let R=(r_0,...,r_m) be one path of a displayed two-cover of H-S with order at least six. Put M=(r_1,...,r_{m-1}). If u is noninsertable into M, then H contains explicit order disagreement or there is a proper Hamiltonian support of order four or five whose complementary two-cover state admits strict quadratic-potential descent in its pairwise-repartition component.

## Body

Apply insert01 to u on M. In alternative 1, 0425e03e2aa3 gives a Hamiltonian four-set or the exceptional cyclic non-Hamiltonian four-set. The Hamiltonian case is consumed by 7bab8dd31d87 and ham6_large_escape01; in the cyclic case smallset01 Hamiltonizes a five-set after adding an exterior vertex, then ham5_large_escape01 applies. In alternative 2, the reverse-through-gap triple T=(r_{i+1},u,r_i) is tight. Choose distinct a,b in S-{u} and put X=V(T) union {a}. If X is Hamiltonian, consume it with 7bab8dd31d87 and ham6_large_escape01. If X is non-Hamiltonian, db835c34cc40 applied to T inside X and exterior vertex b gives either the Hamiltonian four-set V(T) union {b} or the Hamiltonian five-set X union {b}; consume these by the same four-side machinery or by ham5_large_escape01. Minimum-counterexample calculus supplies the required non-Hamiltonian path-cover-two complements throughout. Hence one noninsertable endpoint already yields order disagreement or strict generated-state descent above order seventeen.
