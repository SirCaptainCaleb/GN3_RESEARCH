# Eight-label exclusion forces permanently internal vertices on both Hamiltonian four-sides

## Statement

In the eight-label residue, with P={u,a,b,c} and Q={v,d,e,f} as in astra003mixedgrid where u,v are excluded singleton labels, neither u nor v is an endpoint of any Hamilton tight path on its four-set. Equivalently, every Hamilton order of P has endpoints in {a,b,c}, and every Hamilton order of Q has endpoints in {d,e,f}.

## Body

Work in the eight-label residue and notation of astra003mixedgrid.

First consider Q. Let

Q=(q0,q1,q2,q3)

be an arbitrary Hamilton tight path on the four-set Q. The mixed-grid lemma applies to this arbitrary Hamilton order. For any r in {a,b,c}, it produces a reachable mixed 5|3|3 state in which the union of the two three-sides is

R_i(r)={u,r,q_i,t,s,w}

for each endpoint index i in {0,3}, and the exact bad deletion set of R_i(r) is {t,u}.

Since q_i is not one of the two bad labels, deleting q_i from R_i(r) leaves a Hamiltonian five-set. Repartitioning the two three-sides by this Hamiltonian five-set and the singleton {q_i} is therefore a legal Astra move. The untouched mixed five-side remains Hamiltonian, so the resulting state is a reachable 5|5|1 state with singleton q_i.

Thus every endpoint q0,q3 of every Hamilton order of Q belongs to the reachable singleton-label set S.

But v is one of the excluded labels, so v is not in S. Therefore v cannot be an endpoint of any Hamilton tight path on Q.

The construction is symmetric under interchanging P and Q. Applying the symmetric mixed-grid argument to an arbitrary Hamilton order of P shows that every Hamilton-path endpoint of P lies in S. Since u is excluded, u is never such an endpoint.

Hence u and v are permanently internal on their respective Hamiltonian four-sets.
