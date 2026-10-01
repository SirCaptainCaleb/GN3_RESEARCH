# The one-backward mandatory side forces an original-tournament tight triple or Hamiltonian four-set

## Statement

Let H be a minimum counterexample in the one-backward comparison setting, and let G be the edge-orderable tournament obtained by reversing the unique backward comparison. Let T=(a,b,c) be the newly tight mandatory triple of G. Choose a spanning two-cover A|B of G such that A contains T consecutively and |A| is minimum among such covers. Let u,v be the endpoints of A and Q=(q_0,...,q_m) the displayed path on B.

Then H contains either
(1) a tight triple (u,q_j,v) or (v,q_j,u) for some q_j in B; or
(2) a Hamiltonian four-set {u,v,q_i,q_{i+1}} for some displayed edge q_i q_{i+1} of Q.

In case (2), the complement of that four-set in H is non-Hamiltonian with path-cover number two.

## Body

Endpoint minimality and mandatoryness imply that B+u, B+v, and B+u+v are all non-Hamiltonian. The one-end assertions follow from 20939673157e, and the joint non-Hamiltonicity of B+u+v is the two-end endpoint-minimal obstruction in 35ad47cf08a5. For B+u+v, a Hamilton path Q' on that support together with A-{u,v} would either give a smaller mandatory-side two-cover, if T survives in A-{u,v}, or a two-cover in which neither component contains the mandatory triple T, if u or v meets T. Both are impossible.

Thus u and v are noninsertable into the displayed increasing order Q. Apply 51b466093d5c to the least right-feasible gaps beta(u), beta(v). If these gaps differ, 51b466093d5c yields a tight connector (u,q_j,v) or (v,q_j,u) in G.

Suppose instead beta(u)=beta(v)=i. Then
u q_{i+1}<u q_i and v q_{i+1}<v q_i
in the representing edge order. If the four-set {u,v,q_i,q_{i+1}} were non-Hamiltonian, its three perfect matchings would form strict comparison blocks. The inequality u q_{i+1}<u q_i orders the two relevant matching blocks one way, while v q_{i+1}<v q_i orders them the opposite way, a contradiction. Hence that four-set is Hamiltonian in G.

Finally transfer the output back to H. The unique changed comparison has vertex set V(T) subseteq A. A connector triple {u,q_j,v} contains a B-vertex and therefore is not V(T), so its orientation is unchanged from G to H. Likewise the four-set {u,v,q_i,q_{i+1}} contains only two vertices from A, so it cannot contain all three vertices of T; H and G induce the same boundary tournament on it. Thus the connector or Hamiltonian four-set exists already in H. In the Hamiltonian four-set branch the support is proper, and its complement cannot be Hamiltonian without two-covering H; minimum-counterexample calculus therefore gives complement path-cover number two.
