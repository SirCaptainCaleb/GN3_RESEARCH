# Leaf endpoint comparison forces direct mixing or splits the old support

**Summary:** A leaf endpoint comparison either mixes the two old supports directly or splits a displayed edge of the leaf support between the two comparison paths.

## Statement

At a leaf selected support P in a support forest, comparing the deletion cover at either endpoint of the other support Q either produces a direct edge between surviving vertices of P and Q, or splits some displayed edge of P between the two paths of the comparison cover. In the split case (Q-y) union {x} is Hamiltonian; inherited-order preservation further yields a positioned reversal or the equal-potential singleton triangle.

## Body

# Leaf endpoint comparison forces direct mixing or splits the old support

Let H be a minimum counterexample to pc(H) <= 2. Choose one deletion cover F_v for every v in V(H), and let J be the selected support graph. Suppose J is a forest and e_x=PQ is a leaf edge, with P the leaf support. Let y be an endpoint of a displayed Hamilton order on Q, and put B=Q-{y}.

Then at least one of the following holds.

1. The selected deletion cover F_y contains a path edge joining a surviving vertex of P to a surviving vertex of Q.
2. Some displayed edge of P has its endpoints in different paths of F_y.

In alternative 2, F_y has exactly two path edges joining distinct classes of P | B | {x}; both are incident with x. The path containing x consists of x, all of B, and one nonempty part of P, while the other path contains the remaining nonempty part of P. In particular B union {x} is Hamiltonian.

If this Hamilton path preserves the inherited order of B, then x lies in one of the first two insertion positions when y is the initial endpoint of Q, and in one of the last two insertion positions when y is the terminal endpoint. The non-extreme insertion forces a tight triple reversing a displayed end edge. If both endpoint comparisons use the extreme insertion, the three deletion covers at x and at the two endpoints of Q have a common fixed support P; their singleton lifts form an equal-quadratic-potential triangle, and the two endpoint-replacement orders disagree on their common non-P support.

## Proof

Because P is a leaf support of J, the selected cover F_y shares neither P nor Q with F_x: it cannot share Q because every support of F_y omits y, and it cannot share P because P is incident only with e_x. Hence F_y is support-incompatible with F_x on H-{x,y}.

Consider the three classes P, B, {x}. The cover F_y has at least two path edges joining distinct classes. If it had at most one, deleting that edge from its two paths would leave at most three path blocks. The resulting support partition would be one of (P union B)|{x}, (P union {x})|B, or P|(B union {x}). The first gives a two-cover of H after adjoining the two-vertex path (x,y); the second makes P union {x} Hamiltonian and gives a two-cover with Q; the third is support-compatible with F_x. All are impossible.

Assume alternative 1 fails. Then every interclass edge is incident with x. Since x lies on one path of F_y, at most two path edges are incident with x. Therefore there are exactly two interclass edges, both incident with x.

Cut these two edges. Besides the singleton block {x}, there are three maximal blocks contained in P or B, so exactly one of P,B is split into two blocks. If B were split, the two interclass edges would join x to the two B-blocks: joining x to the unique P-block would make P union {x} Hamiltonian. Thus one path of F_y would have support B union {x}, and the other path would have support exactly P. This would make P a support of F_y, contradicting that P is the leaf support incident only with e_x.

Hence P is split. The same contracted two-path argument shows that x joins the unique B-block to one P-block, while the other P-block is the second path. Thus the vertices of P lie in both paths of F_y. Since the displayed order on P is a path, some consecutive displayed pair has its endpoints in different paths of F_y. This proves alternative 2. The path segment B together with x is Hamiltonian, giving the additional assertion.

For the insertion refinement, write Q=(q_0,...,q_m). Suppose first y=q_0 and a Hamilton order on B union {x} preserves the order q_1,...,q_m. Since Q union {x} is non-Hamiltonian, x can occur only before q_1 or between q_1 and q_2; any later insertion permits q_0 to be prepended. In the second case, (q_0,q_1,x) must be non-tight, so (x,q_1,q_0) is tight and reverses the displayed initial edge of Q. The terminal-end statement is symmetric: a non-extreme insertion gives (q_m,q_{m-1},x) tight.

If both endpoint replacements use the extreme positions, their orders are

(x,q_1,...,q_m),
(q_0,...,q_{m-1},x).

Together with Q they give deletion covers at q_0, q_m, and x sharing P. Let X=Q union {x}. Their singleton lifts are P|(X-{d})|{d} for d in {x,q_0,q_m}; any two differ by repartitioning X and leaving P fixed. Hence they form a triangle in the pairwise-repartition graph and have equal quadratic potential. After deleting q_0 and q_m, the two endpoint-replacement paths induce opposite positions of x on the common support {x,q_1,...,q_{m-1}}, so they have an order disagreement.

## Metadata

- ID: leaf_endpoint_singleton_triangle01
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
