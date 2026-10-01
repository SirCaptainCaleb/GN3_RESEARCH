# The all-equal support triangle yields endpoint insertion, order disagreement, or synchronized endpoint barriers

## Statement

In the all-equal support-triangle setting, let P_i=(t_i,M_i,t_{i+1}) be the displayed Hamilton path on S_i and let E_i be the displayed endpoint set of the complementary paths M_{i+1}|A_{i+2}. Then at least one of the following holds: (1) some x in E_i is insertable into the displayed order P_i; (2) some x in E_i is noninsertable into P_i while H[S_i union {x}] is Hamiltonian, in which case every Hamilton path on that enlarged support has order disagreement with P_i on old vertices; or (3) H[S_i union {x}] is non-Hamiltonian for every i and x in E_i. In case (3), writing M_i=(b_i,...,a_i), every d in E_i satisfies the endpoint barriers (b_i,t_i,d) and (d,t_{i+1},a_i) tight. Thus the all-equal residue either exposes an endpoint insertion, exposes standard order disagreement, or carries synchronized reverse endpoint barriers against every displayed endpoint of both complementary paths at all three supports.

## Body

Consider all pairs (i,x) with x in E_i. If some x inserts into the displayed order P_i, case (1) holds. Assume henceforth that no such insertion exists. If some enlarged support H[S_i union {x}] is Hamiltonian, then x is noninsertable by assumption and noninsertableorderdisagree01 gives order disagreement between P_i and every Hamilton order of that enlarged support, proving case (2).

The only remaining possibility is that H[S_i union {x}] is non-Hamiltonian for every i and every x in E_i. Apply Proposition 1.1 of coversurg01 to the Hamiltonian support S_i, its displayed Hamilton path P_i, and D=E_i. The initial ordered pair of P_i is (t_i,b_i), so (b_i,t_i,d) is tight for every d in E_i. Its terminal ordered pair is (a_i,t_{i+1}), so (d,t_{i+1},a_i) is tight for every d in E_i. Apply cyclically. The certified reverse join (b_i,t_i,a_{i-1}) from aff724a01002 is one member of the first barrier family because a_{i-1}=a_{i+2} is an endpoint of A_{i+2}.
