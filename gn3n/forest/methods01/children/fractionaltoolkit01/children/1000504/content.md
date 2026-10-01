# Sharp half-order shell optima are fractional perfect matchings on longest-path supports

## Statement

Let H be a minimum counterexample in the sharp half-order shell n=2 lambda+1. Then every optimal primal fractional path cover x has: (i) every positive-weight path support has order lambda; and (ii) every vertex has total x-coverage exactly one. Hence x is a fractional perfect matching on the lambda-uniform hypergraph of Hamiltonian lambda-subsets. Moreover, choosing one lambda|lambda deletion cover of H-v for each v and assigning weight 1/(n-1) to each component occurrence gives an optimal fractional perfect matching supported only on nonisolated vertices of the Hamiltonian-support odd graph.

## Body

In the sharp half-order shell, fractionalequalityshell01 gives tau*=2n/(n-1)=2+1/lambda and says every optimal dual weighting is uniform. The normalized value is w(v)=1/lambda for every vertex, because a longest path has lambda vertices and dual path weight at most one.

Let x be any optimal primal cover. Primal-dual equality gives
sum_P x_P >= sum_P x_P w(P)=sum_v w(v)c_x(v) >= sum_v w(v),
with equality at the endpoints. Therefore equality holds termwise in the complementary-slackness sense. If x_P>0 then w(P)=1, so |P|/lambda=1 and |P|=lambda. Since w(v)>0 for every vertex, every primal vertex constraint is tight: c_x(v)=1.

Thus every optimal primal is a fractional perfect matching on the Hamiltonian lambda-supports.

For the explicit deletion-cover optimum, choose for each vertex z one deletion cover P_z|Q_z of H-z. Sharpness gives |P_z|=|Q_z|=lambda. Give each of the 2n component occurrences weight 1/(n-1), combining equal supports by addition. Fix a vertex v. It is absent from the z=v cover, and for each of the other n-1 deletion covers it lies in exactly one of the two components. Hence its total coverage is (n-1)/(n-1)=1. The total mass is 2n/(n-1)=tau*, so the cover is optimal.

Each component support P_z is disjoint from its mate Q_z and their union is V(H)-{z}; hence they are adjacent in the Hamiltonian-support odd graph. Therefore every path support carrying positive weight in this canonical optimum is nonisolated.
