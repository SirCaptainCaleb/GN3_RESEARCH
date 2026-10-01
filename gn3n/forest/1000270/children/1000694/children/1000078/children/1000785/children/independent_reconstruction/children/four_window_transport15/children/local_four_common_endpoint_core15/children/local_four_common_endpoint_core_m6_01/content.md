# A locally minimal four-side with a complementary path of order at least six has a common endpoint-pair three-core

## Statement

Let H be a minimum counterexample and let W|P|Q be a spanning three-cover with |W|=4 that minimizes quadratic potential within its connected pairwise-repartition component. Suppose max{|P|,|Q|}>=6. Let E_P,E_Q be the displayed endpoint pairs. Then some w in W has the property that, with D=W-{w}, both D union E_P and D union E_Q are Hamiltonian. Moreover, either D union {e} is Hamiltonian for some displayed endpoint e, or D union {x,y} is Hamiltonian for every two distinct displayed endpoints x,y; in the latter case every such proper five-set has non-Hamiltonian path-cover-two complement.

## Body

Define A_R={w in W:(W-{w}) union E_R is Hamiltonian} for R=P,Q. By twofourhamdeletions01, both A_P and A_Q have order at least two. If they were disjoint, they would be complementary two-subsets of W. Then c0ec8ff0e968 gives W union {e} Hamiltonian for every displayed endpoint e. Choose a component R of order m>=6 and one displayed endpoint e of R. Replacing W|R by a Hamilton path on W+e and the inherited path R-e is a legal pairwise repartition with size change (4,m)->(5,m-1) and Phi change 10-2m<0, contradicting local Phi-minimality. Hence A_P and A_Q intersect. Choose w in the intersection and set D=W-{w}. The remaining refinement is exactly the same as in local_four_common_endpoint_core15: if no D+e is Hamiltonian, apply three_bad_four_extensions_fiveshell01 to D and triples of displayed endpoints to obtain every pair extension, and use minimum-counterexample calculus for their complements. The total-order hypothesis n>=15 is unnecessary once one long component of order at least six is given.
