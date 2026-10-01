# Every trapped three-five-five state contains a reachable two-by-two exchange rectangle

## Statement

Let H be a boundary tournament on thirteen vertices and let T|F|R be a spanning 3|5|5 cover in a trapped Astra-003 component consisting of 3|5|5 states. Then there exist distinct u,v in T and distinct r,s in R such that all four singleton exchanges u<->r, u<->s, v<->r, v<->s are legal neutral pairwise repartitions while F remains fixed. Equivalently, with C=R-{r,s}, each of the four five-sets C union {u,r}, C union {u,s}, C union {v,r}, C union {v,s} is Hamiltonian. Hence the same trapped component contains the four corner states (T-{x}+{y}) | F | (C union {x,y}) for x in {u,v}, y in {r,s}.

## Body

Form the bipartite swap-incidence graph G with left part T and right part R, joining x in T to y in R exactly when R-{y}+{x} is Hamiltonian. By the side-specific coordinate exchange argument in astra003mobility94_recomp01, every x in T has degree at least three, so e(G)>=9. Suppose no two left vertices have two common right neighbors. Then sum_{y in R} binom(d(y),2)<=binom(3,2)=3, because each unordered pair of left vertices is counted by at most one common neighbor. But among five integers d(y) in {0,1,2,3} with sum at least nine, the minimum possible value of sum binom(d(y),2) is attained at the most even distribution (2,2,2,2,1), where it equals four. This contradiction proves that some distinct u,v in T have two distinct common neighbors r,s in R. By definition of G, R-r+u=C+s+u, R-s+u=C+r+u, R-r+v=C+s+v, and R-s+v=C+r+v are all Hamiltonian. Each corresponding exchange only repartitions T union R, leaves F unchanged, and preserves the 3|5 component orders, so all four corner states are reachable by one legal Phi-neutral move from the original state.
