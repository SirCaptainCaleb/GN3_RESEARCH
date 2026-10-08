# Blocked cycle absorption forces disjoint nonempty ascent sets — preserved pre-item development

## Development

## Disjoint ascent sets in the uniform obstruction to cycle absorption

Work in a locally transitive ternary coloring. Let C be a color-0 tight cycle, E a disjoint exterior set with |E|>=3, and suppose no color-0 path spans C union {x,y} for any distinct x,y in E. Write p(c),s(c) for the neighbors of c on C.

The uniform-comparison theorem gives one of two cases:
(I) every exterior vertex is before both cycle neighbors at each c, and every cycle vertex is before every other exterior vertex at each exterior center;
(II) all those comparisons are reversed.

### Theorem
In case (I), put A_x={c in C:h(c,x,s(c))=0} for x in E.
Each A_x is nonempty, the sets A_x are pairwise disjoint, and at every c in A_x, x is the least vertex of E in the center order at c.

In case (II), put B_x={c in C:h(p(c),x,c)=0}.
Each B_x is nonempty, the sets B_x are pairwise disjoint, and at every c in B_x, x is the greatest vertex of E in the center order at c.

In particular |E|<=|C|. This is a necessary condition for the absence of two-vertex monochromatic absorption; the converse is not asserted.

### Proof in case (I)
Fix x in E and c in A_x. For any y in E distinct from x, consider
(y,c,x,s(c),s^2(c),...,p(c)).
This is a permutation of C union {x,y}. Its second status is h(c,x,s(c))=0. Its third status is h(x,s(c),s^2(c))=0 by the uniform before condition at s(c), and all remaining statuses are old cycle statuses, hence 0. For a triangle C the third status still exists and this same description applies.

Therefore if h(y,c,x)=0, the entire order would be color-0 tight, contrary to hypothesis. It follows that h(y,c,x)=1 for every y!=x in E, so h(x,c,y)=0. Thus x is least in the center order restricted to E at c.

Two different exterior vertices cannot both be least at the same center, so their A sets are disjoint. Each A_x is nonempty: otherwise the strict order at x would satisfy s(c)<c for every c around C, an impossible cyclic chain of strict inequalities.

### Proof in case (II)
Fix x in E and c in B_x. For any y!=x in E, use
(s(c),s^2(c),...,p(c),x,c,y).
The old initial cycle windows have color 0. The window entering x is color 0 because x follows both cycle neighbors at center p(c); the next is h(p(c),x,c)=0 by c in B_x. Only the final window h(x,c,y) is not already fixed to 0.

The absence of a monochromatic spanning order on this support therefore forces h(x,c,y)=1 for all y!=x. Hence x is greatest in E at center c. Disjointness follows, and nonemptiness again follows because a strict total order cannot descend along every edge of a cycle.

Selecting one distinct representative from each nonempty disjoint ascent set proves |E|<=|C|.

### Equality structure
If |E|=|C|, each ascent set is a singleton and these singletons partition C. In case (I), if A_x={c}, the order at center x restricted to C is forced to be
c < p(c) < p^2(c) < ... < s(c).
Indeed every cycle edge other than c->s(c) is a descent at x, giving the entire displayed chain. The root c also makes x the unique least exterior vertex at center c.

In case (II), if B_x={c}, the unique ascent is p(c)->c, and the order at x on C is
p(c) < p^2(c) < ... < c.
The corresponding exterior vertex is greatest at cycle center c.

### Use and limits
The uniform obstruction retains a family of disjoint nonempty ascent sets; it is substantially more constrained than an arbitrary collection of local comparisons. If |E|>|C|, the proof forces an actual monochromatic path on C plus two exterior vertices.

This does not complete the conjecture: the path produced need not span the remaining exterior vertices, and the equality structure does not force a monochromatic spanning path inside E. No frequency conclusion from Frankl's conjecture is used.
