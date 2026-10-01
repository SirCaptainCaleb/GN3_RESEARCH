# Any four-side beside a path of order at least six descends, migrates neutrally, or reaches the matching frontier

## Statement

Let H be a minimum counterexample and let X|P|Q be any spanning three-cover, where X is a Hamiltonian four-path and P=(p_1,...,p_m) has m>=6. Put U=V(X) union {p_1,p_m}. Then at least one of the following holds: (1) one legal repartition of X|P strictly decreases quadratic potential; (2) m=6, U is Hamiltonian, and U|(p_2,...,p_{m-1}) is the unique size-profile neutral migration (4,6)->(6,4); (3) U is non-Hamiltonian and its good-pair graph on X has adjacent edges, giving the positioned overlap-amplification package; (4) U is non-Hamiltonian and that graph is a perfect matching, yielding the fixed-endpoint matching frontier.

## Body

If X+p_1 or X+p_m is Hamiltonian, endpoint transfer changes (4,m) to (5,m-1) with Delta Phi=10-2m<0 for every m>=6, giving (1). Assume both are non-Hamiltonian. Then two_bad_five_extensions_all_opposite01 gives U-x Hamiltonian for all x in X. If U is Hamiltonian, repartition as U|(p_2,...,p_{m-1}); the potential change is 24-4m, strictly negative for m>=7 and zero exactly at m=6. Thus this gives (1) for m>=7 and (2) for m=6. If U is non-Hamiltonian, apply the good-pair graph argument of four_side_endpoint_matching_bridge01: adjacent edges give overlap amplification, while absence of adjacent edges together with minimum degree one forces a perfect matching. That proof uses only the six-set hypotheses, so it applies equally at m=6.