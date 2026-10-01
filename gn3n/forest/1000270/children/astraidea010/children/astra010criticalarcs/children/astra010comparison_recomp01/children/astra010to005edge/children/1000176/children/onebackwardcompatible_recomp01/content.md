# Compatible one-backward deletion states either glue after the flip or force a reverse-cross triple

## Statement

In the minimum-order one-backward comparison setup with flipped triple (a,b,c), suppose the three deletion covers F_a,F_b,F_c are pairwise compatible. Let their common insertion gap split a common path as P=L,R, with the other path Q fixed, and let D be the precedence tournament on {a,b,c}. Then the corrected edge-orderable tournament G has the canonical spanning two-cover (L,a,b,c,R)|Q unless D is one of the two transitive orders b->c->a or c->a->b. The common gap is two-deep in either surviving case. If D is b->c->a, then either the canonical cover exists or (b,ell,a) is tight, where ell is the last vertex of L. If D is c->a->b, then either the canonical cover exists or (c,r,b) is tight, where r is the first vertex of R. Thus every genuinely nonglued pairwise-compatible residue exposes an explicit reverse-cross triple at a neighbor of the common gap.

## Body

Compatibility gives the common-gap model and makes every directed Hamilton order of D a non-tight label triple in H. The comparison flip changes only the reversal pair (a,b,c)/(c,b,a). If a->b->c, the newly tight triple closes the common-gap path in G. If this chain is absent, comparison with the tight reverse (c,b,a) forces b to be a source or sink, so D is transitive and the gap is two-deep.

There are four transitive orders not already covered by a->b->c and not forbidden by c->b->a. For b->a->c and a->c->b, the global edge order and the inherited local comparisons on the two sides of the gap place ell,a,b,c,r in increasing order, so the canonical path again glues. Hence only b->c->a and c->a->b remain.

For b->c->a, inherited comparisons give ell b<ab and bc<cr, while the flip and reversed precedence triple give ab<bc and ac<bc. The only missing comparison for the canonical path is ell a<ab. If it fails, ab<ell a, so ell b<ab<ell a and (b,ell,a) is tight. The c->a->b case is symmetric: failure of the final comparison gives cr<bc<br, hence (c,r,b) is tight. This proves the stated dichotomy directly.
