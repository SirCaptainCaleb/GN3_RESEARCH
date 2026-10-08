# Radon zeros of protected descent roots are physical coordinate cycles — preserved pre-item development

## Composition

(none yet)

## Development

## Radon zeros of protected descent roots are physical coordinate cycles

Work with the protected bridge setup in a minimum coordinate counterexample. For every noninert protected replacement bridge
[
B=b_1cdots b_r
]
and every adjacent descent (b_i b_{i+1}=10), subsection 197 associates the physical root
[
ho=e_{a_i}-e_{c_i}in W_V,
]
where (a_i) is the coordinate dropped when the bridge window slides from (i) to (i+1), and (c_i) is the coordinate entering.

Consider any finite collection of such descent roots
[
ho_j=e_{a_j}-e_{c_j}
]
coming from protected bridge states, and suppose
[
sum_j lambda_j ho_j=0
qquad
(lambda_j>0).
	ag{1}
]

### Theorem: positive Radon cancellation is a circulation

Equation (1) is exactly the flow-conservation equation for the directed weighted multigraph on physical coordinates having an edge
[
c_jlongrightarrow a_j
]
of weight (lambda_j).

Indeed the coefficient of (e_v) in (1) is
[
sum_{j:a_j=v}lambda_j-sum_{j:c_j=v}lambda_j,
]
so (1) says weighted inflow equals weighted outflow at every coordinate.

Consequently the support of the Radon relation decomposes into directed cycles of physical coordinates. After clearing denominators when the (lambda_j) are rational, this is the usual cycle decomposition of an integral circulation; the general real-weight case follows by the same greedy subtraction of the minimum weight on a directed cycle.

### Fixed-fiber consequence

Inside one fixed protected deletion fiber, the deleted order of all other coordinates and the protected gap are fixed. Every descent root has its positive endpoint among the (r-1) coordinates immediately to the left of the gap and its negative endpoint among the (r-1) coordinates immediately to the right. These two endpoint sets are disjoint.

Therefore all roots in one fixed fiber lie in the strict cone
[
operatorname{cone}{e_a-e_c:ain L, cin R}.
]
Pairing with the cut functional that is (+1) on (L), (-1) on (R), and (0) elsewhere is strictly positive on every nonzero root. Hence no positive Radon relation can be supported entirely in one fixed fiber.

Thus any Radon zero assembled from protected descent roots necessarily uses several deletion fibers, and its directed cycle decomposition necessarily records physical coordinates crossing protected cuts in both directions across those fibers.

### Extraction target

This converts the strategist's missing "compatible spanning path from the topological carrier" into a concrete finite problem:

> Given a directed coordinate cycle
> [
> x_1	o x_2	ocdots	o x_k	o x_1
> ]
> whose edges are certified by protected (10)-descents in successive deletion fibers, splice the corresponding protected exchanges into either
> 1. a threshold-compatible replacement bridge, or
> 2. a strictly shorter root cycle.

The base case is a two-cycle, i.e. two opposite roots
[
e_a-e_c,qquad e_c-e_a.
]
A two-cycle is the exact protected-root analogue of a complementary signed-middle pair. Proving a boundary-preserving surgery for this base case would supply the first genuine path-extraction lemma for the Radon program.

This theorem is algebraic only; it does not yet prove that an arbitrary topological carrier yields a Radon zero, nor that every root cycle is surgically realizable. Its value is that any such zero already contains a physical compatibility cycle rather than an abstract convex dependence.
