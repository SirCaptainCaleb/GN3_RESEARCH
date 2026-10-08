# Universal connector bases require no minimum-shore or triangle hypothesis

## Composition

General compatible connector bases are (z,x) on empty shore support, (z,a,x) on one vertex, (a,x,z,b) on two, and (u,x,z,a,b) on three with a->b. All ports are forward. These remove triangle/minimality assumptions from seed existence and supply the empty-complement barycentric base.

## Development

## Universal connector bases require no minimum-shore or triangle hypothesis

In the fixed switching split B -> z -> A -> x, compatible zero connectors exist on every shore support of size zero, one, two, or three.

For the empty support use (z,x). Its endpoint pair is forward, and its internal word is empty. This is a valid size-two connector for the elevated homogeneous-cut insertion theorem.

For support {a}, use (z,a,x). The tournament is transitive in that order, so its one ternary label is zero and both endpoint pairs are forward.

For support {a,b}, use (a,x,z,b). Its two labels alpha(a,x,z) and alpha(x,z,b) are zero by the pair-signature identity; its endpoint pairs a->x and z->b are forward. This uses no relation between a and b.

For any support {u,a,b}, orient a,b so a->b and use (u,x,z,a,b). The first two labels are zero by the pair signature and the last label alpha(z,a,b) is zero because z dominates a,b. Its exposed pairs are forward.

Every additional individual vertex can be absorbed into a suitable extension of the two-shore seed (u,x,z,v): if v->a use (u,x,z,v,a); if a->v use (u,x,z,a,v). This states individual seed extension, with no assertion of collective absorption from arbitrary larger states.

Consequently a minimal obstruction to general compatible connector construction has shore support of size at least four. Its proper-support barycentric boundary data include the empty complement: the corresponding connector is (z,x). The full repair state space must allow the special vertices to change their order and positions.

Directed triangles and protected almost-cliques retain their root-theoretic uses, but seed existence does not depend on those hypotheses. This elevates the original five-coordinate triangle seed to a general switching-split base construction.
