# Any four-side beside a path of order at least seven descends or reaches the fixed-endpoint matching frontier

## Statement

Let H be a minimum counterexample and let X|P|Q be any spanning three-cover, where X is a Hamiltonian four-vertex path and P=(p_1,...,p_m) has m>=7. Then at least one of the following holds: (1) one legal pairwise repartition of X|P strictly decreases quadratic potential; (2) with U=V(X) union {p_1,p_m}, the graph defined by Hamiltonian two-vertex deletions on the four X-label deletions has two adjacent edges, yielding two Hamiltonian four-sets containing {p_1,p_m} and overlapping in three vertices, hence the overlap amplification package; (3) V(X)=A disjoint-union B with |A|=|B|=2 and both A union {p_1,p_m} and B union {p_1,p_m} are Hamiltonian four-sets with non-Hamiltonian path-cover-two complements. Thus the only no-descent residue not already overlap-amplified is the perfect matching on the four labels with both exterior endpoints fixed. No deletion-state origin or ambient order threshold is required.

## Body

If X union {p_1} or X union {p_m} is Hamiltonian, transfer that endpoint from P into X. The pair sizes change from (4,m) to (5,m-1), with Delta Phi=10-2m<0 since m>=7. This gives (1).

Assume both endpoint five-sets are non-Hamiltonian and put U=V(X) union {p_1,p_m}. By two_bad_five_extensions_all_opposite01, U-{x} is Hamiltonian for every x in V(X). If U is Hamiltonian, repartition X|P as U | (p_2,...,p_{m-1}). The pair sizes change from (4,m) to (6,m-2), with Delta Phi=24-4m<0 for m>=7, again giving (1).

Hence in the no-descent branch U is non-Hamiltonian, U-p_1 and U-p_m are non-Hamiltonian, and all four X-label deletions are Hamiltonian. Apply four_side_endpoint_matching_bridge01. If its graph defined by Hamiltonian two-vertex deletions has adjacent edges, we obtain exactly (2), including its overlap amplification and pc2-complement conclusions. Otherwise the graph is a perfect matching on V(X), giving a partition V(X)=A disjoint-union B into two pairs and the two fixed-endpoint Hamiltonian four-sets of (3), again with non-Hamiltonian path-cover-two complements. No step uses a deletion-state origin or a lower bound on |H| beyond the displayed m>=7 hypothesis.