# Terminal-cycle rank controls nonspecial incidence nullity up to entrance rank

## Statement

Let H be a finite linear 3-graph, let E_ns be its nonspecial edges, and let T be the terminal-pair graph of E_ns. Let N_ns be the vertex-edge incidence matrix restricted to E_ns, and let h be the number of distinct entrance vertices among E_ns. Then nullity_R(N_ns)<=β(T)+h. Consequently, if H has s special edges and full incidence matrix N, then nullity_R(N)<=β(T)+h+s<=β(T)+n+s.

## Body

For each nonspecial edge e with unique entrance u(e) and terminal pair {y_e,z_e}, write its incidence column as 1_{y_e}+1_{z_e}+1_{u(e)}. Let B be the ordinary 0/1 vertex-edge incidence matrix of the terminal-pair graph T (with zero rows added for vertices outside V(T)), and let R be the matrix whose e-column is the unit vector 1_{u(e)}. Then N_ns=B+R.

By the rank inequality rank(A+B)>=rank(A)-rank(B), rank(N_ns)>=rank(B)-rank(R). Since all columns of R are standard basis vectors supported on the h distinct entrance vertices, rank(R)<=h. Hence nullity(N_ns)=|E_ns|-rank(N_ns)<=|E_ns|-rank(B)+h.

For a finite graph T with v vertices, b edges, c components and c_bip bipartite components, the real 0/1 incidence matrix has rank v-c_bip. Therefore b-rank(B)=b-v+c_bip=β(T)-c+c_bip<=β(T). Thus nullity(N_ns)<=β(T)+h.

Finally, adjoining the s special-edge columns to N_ns can increase nullity by at most s: if A has b columns and C has s columns, nullity([A C])=(b+s)-rank([A C])<=b+s-rank(A)=nullity(A)+s. Therefore nullity(N)<=β(T)+h+s<=β(T)+n+s.
