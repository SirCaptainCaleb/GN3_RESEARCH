# Quadratic descent must be measured from the same extremal cover

## Statement

Let C be a three-cover and let Phi be the sum of its squared path orders. If a sequence of pairwise repartitions takes C to D with Phi(D)=Phi(C)+Delta, and a continuation takes D to E with Phi(E)=Phi(D)-delta, then Phi(E)<Phi(C) if and only if delta>Delta. Existence of some descending three-cover in a boundary tournament is a strictly weaker conclusion: whenever H-x=P|Q and |P|=m>=3, the three-cover P|Q|{x} has an immediate decrease of 2m-4, irrespective of any additional local configuration.

## Body

The first assertion is the identity Phi(E)-Phi(C)=Delta-delta. It requires the two sequences to concern the same covers at their common endpoint D; existence of a different cover with a decrease supplies neither reachability nor the required inequality.

For the second assertion write P=(p_1,...,p_m). Replace P|{x} by (x,p_1)|(p_2,...,p_m), keeping Q fixed. The first new path has order two and is therefore valid without a triple condition. The second is a nonempty contiguous subpath. The decrease is m^2+1-[4+(m-1)^2]=2m-4>0. This is the already established singleton descent, included to make the quantifiers explicit.

For example, suppose a path U of order k loses one endpoint u to a path P of order p, and the enlarged P+u is a path. The pair of orders k,p becomes k-1,p+1, with increase Delta=(k-1)^2+(p+1)^2-k^2-p^2=2(p-k+1). For k=6 this is 2p-10. A later strict decrease measured from the resulting five-side state does not establish a decrease from the original six-side state unless it exceeds 2p-10. If a fresh two-cover of the complement is chosen instead, even reachability from the original cover needs its own proof.

Consequently a contradiction to minimality of C requires a reachable E with Phi(E)<Phi(C). A positive decrease from an unspecified or newly selected cover is insufficient. This observation does not invalidate a theorem whose literal conclusion only asserts that some descending cover exists; it limits what that theorem can prove about an extremal input.
