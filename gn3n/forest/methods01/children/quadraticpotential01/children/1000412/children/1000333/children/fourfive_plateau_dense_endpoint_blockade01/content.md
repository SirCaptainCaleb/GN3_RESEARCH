# A trapped four-five plateau forces at least five Hamiltonian endpoint-pair four-sets

## Statement

Let X|Y|P be componentwise Phi-minimal in a trapped pairwise-repartition component, with |X|=4, |Y|=5 and |P|=m>=7. Put W=V(X) union V(Y), and let p_-,p_+ be the displayed endpoints of P. Then W has at least 36 Hamiltonian 4|5 partitions A|B in the same component, and for every such four-side A both A union {p_-} and A union {p_+} are non-Hamiltonian. Consequently the graph J on W, with uv an edge exactly when {p_-,p_+,u,v} is Hamiltonian, has at least five edges. Moreover every one of the at least 36 four-sides A contains two adjacent edges uv,vw of J.

## Body

The trapped-plateau theorem 1000333 says every two-cover of W has profile 4|5. The order-nine multiplicity theorem supplies at least 36 such partitions, each reachable by one neutral repartition of X|Y. If A plus either endpoint of P were Hamiltonian, the endpoint transfer (4,m)->(5,m-1) would change Phi by 10-2m<0, contradicting componentwise minimality. Thus both endpoint extensions of every four-side A are bad. Apply two_bad_five_extensions_adjacent_four01 to each A and the two endpoints. If J is the graph on W with uv in E(J) exactly when {p_-,p_+,u,v} is Hamiltonian, then every one of the at least 36 four-sides A contains a length-two path of J.

It remains to count globally. Suppose e(J)<=4. For a vertex v of degree d, the number of four-subsets A containing v together with at least two J-neighbors of v is f(d)=C(d,2)(8-d)+C(d,3). Every four-side A above is counted for at least one such center v. If the maximum degree is at most two, sum_v f(d_v)<=4*f(2)=24. If the maximum degree is four, four edges force J to be a four-edge star (plus isolated vertices), giving sum_v f(d_v)=f(4)=28. If the maximum degree is three, an elementary degree-sum check for a graph with at most four edges shows the largest possible contribution is the degree sequence (3,2,2,1), giving f(3)+2f(2)=16+12=28. Thus in all cases at most 28 four-subsets can contain a length-two path, contradicting the at least 36 distinct four-sides. Therefore e(J)>=5.
