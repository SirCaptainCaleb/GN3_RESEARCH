# Strict-rise plus equal-level control suffices for the 2/3 leading coefficient

## Statement

Let H be a finite linear 3-graph and T_up its simple terminal-pair graph on the ascending nonspecial edges. Partition E(T_up)=E_< disjoint-union E_= according as the endpoint potentials φ(.) are unequal or equal, and orient each edge of E_< from its lower-potential endpoint to its higher-potential endpoint. Suppose every vertex has strict-rise outdegree at most C and the equal-potential graph T_= has maximum average degree at most D. Then the number A of ascending edges satisfies A<=(C+D/2)|V(H)|. Consequently every n-vertex P_ell^(3)-free linear 3-graph satisfying these two bounds obeys |E(H)|<=((2ell-3+C+D/2)/3)n. In particular any absolute constants C,D give the leading coefficient 2/3; the targets C=2,D=3 give |E(H)|<=(2ell/3+1/6)n.

## Body

Every ascending hyperedge contributes one terminal-pair edge to T_up. For unequal terminal potentials, orientation from the lower to the higher endpoint assigns each edge of E_< to exactly one tail, so |E_<|=sum_v d_strict^+(v)<=Cn. For equal potentials, mad(T_=)<=D in particular gives average degree at most D on T_= itself, hence |E_=|<=Dn/2. Therefore A=|E_<|+|E_=|<=(C+D/2)n. Apply the ascending-edge accounting inequality 419519f0efa5: 3m-A<=(2ell-3)n. Substitution yields 3m<=(2ell-3+C+D/2)n. For C=2,D=3 this is 3m<=(2ell+1/2)n, i.e. m<=(2ell/3+1/6)n.
