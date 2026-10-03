# A rooted six-support yields a one-label transfer or a path disturbance

**Summary:** A rooted Hamiltonian six-set with two-coverable complement either transfers a non-root Hamilton-path endpoint into one old complement path by a single pairwise move, or every comparison two-cover splits an inherited edge or leaves and returns to one old support.

## Statement

Let H be a minimum counterexample, let X be a proper Hamiltonian six-set with distinguished root x, and let H-X=P|Q. Then there exists d in X-{x} such that X-d is Hamiltonian and (P union Q)+d has path-cover number two. For any two-cover R|S of (P union Q)+d, relative to P|Q|{d}, either (1) there is exactly one interclass edge, necessarily joining d to one of P,Q, and hence a root-preserving pairwise repartition (X-d)|(P+d)|Q or its symmetric analogue; or (2) one of P,Q occurs in at least two comparison blocks, and therefore either an inherited displayed edge of that support has endpoints in different comparison paths, or one comparison path leaves that support through a nonempty exterior segment and later returns.

## Body

Choose a Hamilton path on X and an endpoint d distinct from the root. By [[ham6goodsquare01]], X-d is Hamiltonian and K+d is non-Hamiltonian with path-cover number two, where K=V(P) union V(Q). Fix a two-cover R|S of K+d. Decompose R,S into maximal blocks contained in P,Q,{d}. If b_P,b_Q are the block counts of the two old supports and t is the number of interclass edges, then t=b_P+b_Q-1. If t=1, then b_P=b_Q=1. The unique interclass edge cannot join P to Q, because then P union Q would be Hamiltonian and, together with X, would two-cover H. Thus d joins exactly one old support and gives the stated root-preserving pairwise transfer. Suppose t>=2. Then b_P+b_Q=t+1>=3, so one old support, say P, has at least two comparison blocks. If vertices of P occur in both R and S, some consecutive pair in the displayed Hamilton order of P lies in different comparison paths, giving a split inherited edge. Otherwise all P-vertices lie in one comparison path, but at least two maximal P-blocks occur there; a nonempty block of another displayed class lies between two consecutive P-blocks, so that comparison path leaves P through exterior vertices and later returns. Thus every non-transfer comparison is already a path disturbance.

## Metadata

- ID: rooted_six_support_transfer_or_comparison_disturbance01
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
