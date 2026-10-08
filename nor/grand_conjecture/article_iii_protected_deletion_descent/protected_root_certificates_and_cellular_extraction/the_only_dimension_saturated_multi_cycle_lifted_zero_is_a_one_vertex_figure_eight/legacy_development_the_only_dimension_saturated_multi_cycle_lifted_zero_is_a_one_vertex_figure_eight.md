# The only dimension-saturated multi-cycle lifted zero is a one-vertex figure eight — preserved pre-item development

## Development

## The only dimension-saturated multi-cycle lifted zero is a one-vertex figure eight

Continue from root §188. A support-minimal honest lifted zero is either one physical simple cycle or the union of exactly two physical simple cycles with opposite nonzero side imbalances.

Assume the two-cycle union covers all n physical coordinates. Let their vertex sets be A and B.

### Disjoint case

If A cap B is empty, then

|A|+|B|=n.

The lifted zero therefore has n label vertices in the n-dimensional target W direct-sum R. Its support simplex has dimension at most n-1.

More concretely, because each individual cycle has nonzero side sum, its lifted edge vectors span its physical cycle space together with the vertical direction. The combined two-cycle span has dimension n-1: the physical projection is W_A direct-sum W_B of dimension n-2, and the common vertical direction adds one.

Thus the disjoint two-cycle zero lies in a codimension-one lifted subspace. It is in principle removable by one honest state label transverse to that subspace, exactly as in the Hamiltonian single-cycle theorem §187.

### One-shared-vertex case

If A cap B={x}, then

|A|+|B|=n+1.

The support-minimal lifted dependence has n+1 label vertices, the maximum possible size of a vector circuit in the n-dimensional target.

The physical cycle spaces W_A and W_B together span all W because A union B=V and the two coordinate sets meet. Their dimensions add to

(|A|-1)+(|B|-1)=n-1=dim W.

Each individual lifted cycle has nonzero side imbalance, so its physical cycle relation is broken in W direct-sum R. Together the two lifted cycle families span all n target dimensions; the unique positive relation is the rescaled cancellation between their opposite side imbalances.

Therefore their n+1 lifted label points form an n-dimensional simplex containing 0 in its relative interior. Its boundary has nonzero local degree around 0.

### Consequence

Among support-minimal honest lifted zeroes, the ONLY multi-cycle configuration that is dimension-saturated and cannot be removed merely by finding a transverse label is:

two directed simple physical cycles of opposite nonzero side imbalance, covering all coordinates and sharing exactly one physical vertex.

This is a directed figure-eight support.

All other single/two-cycle shapes are codimension at least one in the honest lifted target and should be attacked by transverse actual-state labels.

Thus the final lifted-topology frontier is no longer an arbitrary side-balanced circulation. It is the full-dimensional one-vertex figure-eight circuit, together with the carrier-realization issue for transverse labels in lower-dimensional cases.
