# Edge-codegree two forces half-density

## Statement

Let G be a finite simple graph on N vertices such that every edge uv has at most two common neighbors. Then d(u)+d(v)<=N+2 for every edge uv. Consequently, if G has at least one edge then delta(G)<=(N+2)/2 and its average degree is at most (N+2)/2, equivalently |E(G)|<=N(N+2)/4. If equality holds in the average-degree bound, then G is (N+2)/2-regular and every edge uv has exactly two common neighbors and satisfies N(u) union N(v)=V(G).

## Body

# Proof

For an edge uv,
d(u)+d(v)=|N(u) union N(v)|+|N(u) intersect N(v)|<=N+2,
because the union is contained in V(G) and an edge has at most two common neighbors. This proves the edgewise degree-sum bound.

If G has an edge and minimum degree delta, applying the bound to any edge gives 2 delta<=N+2.

Summing the edgewise bound over all uv in E(G) gives
sum_v d(v)^2 <= |E(G)|(N+2),
since each vertex v contributes d(v) once for each incident edge. By Cauchy,
sum_v d(v)^2 >= (sum_v d(v))^2/N = 4|E(G)|^2/N.
For |E(G)|>0, cancellation yields 4|E(G)|/N<=N+2, equivalently |E(G)|<=N(N+2)/4 and average degree at most (N+2)/2.

Suppose equality holds in the average-degree bound. Then equality holds in Cauchy, so all vertex degrees are equal to (N+2)/2. Equality must also hold in every summed edgewise inequality. Hence for every edge uv, |N(u) union N(v)|=N and |N(u) intersect N(v)|=2.

Applied to a deletion-cover compatibility graph once the edge-codegree-at-most-two lemma is available, any construction forcing average compatibility degree strictly above (N+2)/2 already contradicts the counterexample regime. At the exact threshold, the compatibility graph is forced into the rigid regular equality case above, giving a second concrete target for the deletion-cover incompatibility brainstorm.