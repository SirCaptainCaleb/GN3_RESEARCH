# A proper tight cycle forces a cyclic square of path-cover-two extensions of its complement

## Statement

Let H be a minimum counterexample and let C=(u_0,...,u_{r-1}) be a proper vertex-simple tight cycle, with indices modulo r. Put K=H-V(C). Then H[K] is non-Hamiltonian with path-cover number two. For every i, H[V(K) union {u_i}] is non-Hamiltonian with path-cover number two. For every cycle edge u_i u_{i+1}, H[V(K) union {u_i,u_{i+1}}] is non-Hamiltonian with path-cover number two. Consequently every cycle edge determines a full two-label path-cover-two square over the common core K: K, K+u_i, K+u_{i+1}, and K+{u_i,u_{i+1}} are all non-Hamiltonian of path-cover number two.

## Body

Opening the tight cycle C at any cyclic cut gives a Hamilton tight path on V(C). If H[K] were Hamiltonian, that path together with a Hamilton path on K would two-cover H, impossible. Since K is a proper induced subtournament, minimum-counterexample calculus gives pc(K)<=2, hence pc(K)=2. Fix i. Deleting u_i from a tight cycle leaves the inherited cyclic interval C-u_i as one tight path. If K+u_i were Hamiltonian, a Hamilton path on K+u_i together with C-u_i would two-cover H. Thus K+u_i is non-Hamiltonian; it is proper, so pc(K+u_i)=2. Now fix adjacent u_i,u_{i+1}. Deleting these two adjacent cycle vertices leaves the remaining cyclic interval as one tight path (possibly a singleton when r=3). If K+{u_i,u_{i+1}} were Hamiltonian, it together with that remaining interval would two-cover H. Hence K+{u_i,u_{i+1}} is non-Hamiltonian and, being proper, has path-cover number two. This gives the stated overlapping square for every cycle edge.
