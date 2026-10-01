# One-defect states are deletion covers with the omitted vertex restored

## Statement

In a minimum counterexample, a bipartition has total longest-path deficit D=1 exactly when it is obtained from an exact one-vertex deletion two-cover by restoring the omitted vertex to one marked component. Thus the one-defect reconfiguration state space is precisely deletion-cover dynamics with a marked side. In particular the minimum deficient-support size delta equals mu+1, where mu is the globally minimum smaller side of a deletion two-cover.

## Body

# One-defect states are deletion covers with the omitted vertex restored

Let H be a minimum counterexample. For every nonempty vertex set T, let L(T) be the maximum order of a tight path in H[T], and put d(T)=|T|-L(T). For a bipartition V(H)=R disjoint-union S, put D(R,S)=d(R)+d(S).

Then every state with D(R,S)=1 is exactly a one-vertex deletion two-cover with the omitted vertex restored to one of its two components, and conversely every exact one-vertex deletion two-cover gives two such D=1 states.

Suppose d(R)=1 and d(S)=0. Choose a longest tight path on R. It has order |R|-1, so there is a unique vertex x in R outside its support. Then R-{x} and S are both Hamiltonian, hence H-x=(R-{x})|S is an exact two-path cover.

Conversely, suppose H-x=P|Q is an exact two-path cover. Then (P union {x})|Q and P|(Q union {x}) both have total deficit exactly one. Indeed P union {x} contains the Hamilton path P, so its deficit is at most one. It cannot be Hamiltonian, because a Hamilton path on P union {x} together with Q would two-cover H. Thus d(P union {x})=1 while d(Q)=0. The other state is symmetric.

Therefore the D=1 state space is exactly the state space of exact deletion two-covers together with a choice of which component receives the omitted vertex.

As an extremal corollary, let mu be the minimum smaller-component order over all exact two-path covers of all one-vertex deletions, and let delta be the minimum size of a deficient support among all D=1 states. Then delta=mu+1.

For the upper bound, choose H-x=P|Q with |P|=mu<=|Q|. The state (P union {x})|Q has D=1 and deficient support size mu+1, so delta<=mu+1.

For the lower bound, let R|S be a D=1 state with |R|=delta and d(R)=1. By the first part there is x in R such that H-x=(R-{x})|S is an exact two-cover. Hence mu<=|R|-1=delta-1, so delta>=mu+1.

Thus minimum deficient-support states are precisely globally minimum-side deletion covers with their omitted vertex restored to the minimum side.

Consequently, any proof that stays inside D<=1 can be reformulated entirely in deletion-cover dynamics. A monotone attempt to shrink the deficient support reaches exactly the globally minimum-side states already controlled by the minimum-side transfer and endpoint-barrier machinery. Any genuinely new reconfiguration mechanism must therefore either move among deletion covers while keeping the deficient-support size fixed, or make a non-monotone move before a later decrease.