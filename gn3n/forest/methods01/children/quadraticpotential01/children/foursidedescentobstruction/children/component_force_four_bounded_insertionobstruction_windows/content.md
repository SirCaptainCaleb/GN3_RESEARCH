# Local quadratic minima with a four-vertex component force four bounded insertion-obstruction windows

## Statement

Let C=X|P|Q be a spanning three-cover in a connected component of the pairwise-repartition graph, with X=(x_0,x_1,x_2,x_3), |X|=4, and |P|,|Q|>=6. If C minimizes Phi=sum_i |C_i|^2 inside that connected component, then for each R in {P,Q}, writing R=(r_1,...,r_t) and M_R=(r_2,...,r_{t-1}), the induced subtournament H[V(M_R) union {x_j}] is non-Hamiltonian for each j in {0,3}. Hence x_0 and x_3 are each noninsertable into the displayed order of each middle path M_P,M_Q, and insert01 supplies four bounded insertion-obstruction windows, one for each pair (x_j,M_R), j in {0,3}, R in {P,Q}.

## Body

Apply foursidedescentobstruction first to X|P. Its first alternative is a legal pairwise repartition inside the same connected component with strictly smaller Phi. This is impossible because C is Phi-minimal in that component. Therefore its second alternative holds: if P=(p_1,...,p_m) and M_P=(p_2,...,p_{m-1}), then both H[V(M_P) union {x_0}] and H[V(M_P) union {x_3}] are non-Hamiltonian. Since M_P is the displayed tight path, neither x_0 nor x_3 can be inserted into its displayed order.

Apply the same theorem independently to X|Q. Again the strict-descent alternative is impossible for the same local-minimality reason, so with Q=(q_1,...,q_r) and M_Q=(q_2,...,q_{r-1}), both H[V(M_Q) union {x_0}] and H[V(M_Q) union {x_3}] are non-Hamiltonian and x_0,x_3 are noninsertable into the displayed order of M_Q.

The failed-insertion normal form in insert01 now applies to each of the four vertex-path pairs
(x_0,M_P), (x_3,M_P), (x_0,M_Q), (x_3,M_Q).
Each produces a bounded obstruction window supported on the failed vertex and at most four consecutive vertices of the relevant middle path.

No global Phi-minimality and no minimum-counterexample hypothesis is used. Thus these four bounded windows are available at any local quadratic minimum in the pairwise-repartition component. ∎