# Two monochromatic tight cycles join unless both junctions contain directed triangles — preserved pre-item development

## Development

## Two monochromatic cycles can be joined unless both junctions contain directed triangles

Work with a reversal-antisymmetric ternary coordinate label h on V, so h(z,y,x)=1-h(x,y,z). Let C and D be vertex-disjoint monochromatic tight cyclic orders, each containing at least three vertices. Reverse either cycle if necessary so that both have color 0.

Fix any c in C and d in D. Write p,c,s for the predecessor, vertex, successor at c in C, and q,d,t for the corresponding triple in D. Thus
h(p,c,s)=h(q,d,t)=0.
Let C_c^+ be the color-0 linear order obtained by cutting C just after c, so it ends (...,p,c). Let C_c^- be the reversed cyclic direction, also cut to end at c, so it ends (...,s,c) and has color 1. Let D_d^+ start (d,t,...) in the original direction and D_d^- start (d,q,...) in the reversed direction.

### Theorem: two joins or two local directed triangles
Consider the full-support linear orders on C union D
W_01=C_c^+ followed by D_d^-,
W_10=C_c^- followed by D_d^+.
If neither order has at most one color change, then the center tournament T_c contains
p -> s -> d -> p,
and the center tournament T_d contains
c -> q -> t -> c.
Conversely those two directed triangles cause both displayed joins to have three changes.

### Proof
The word of W_01 is a nonempty block of 0s, then two crossing colors
alpha=h(p,c,d), beta=h(c,d,q),
then a nonempty block of 1s. It has at most one change unless (alpha,beta)=(1,0). The blocks are nonempty because the two cycles have at least three vertices.

Similarly W_10 has a nonempty block of 1s, crossing colors
alpha'=h(s,c,d), beta'=h(c,d,t),
and a nonempty block of 0s. It has at most one change unless (alpha',beta')=(0,1).

Thus failure of both candidates is precisely
h(p,c,d)=1, h(c,d,q)=0,
h(s,c,d)=0, h(c,d,t)=1.
Together with the two original cyclic statuses, the first and third equations give p->s->d->p at center c, while the second and fourth give c->q->t->c at center d. Conversely these triangle orientations give the stated four crossing colors, and each join then has three changes.

### Corollary: local transitivity joins two cycles
If either T_c restricted to {p,s,d} or T_d restricted to {c,q,t} is transitive, at least one of W_01,W_10 has at most one change. In particular, if all center tournaments are transitive, any prescribed junction vertices c,d permit a one-change order on the union.

One can see the successful orientation directly: if W_01 fails, then d->p and p->s in T_c, and c->q and q->t in T_d. Transitivity forces d->s and c->t. Therefore W_10 has crossing colors (1,0), exactly aligned with its two constant blocks.

### Spanning consequence
For a locally transitive ternary coloring whose ground set is partitioned into one or two monochromatic tight cycles, directed N_4 holds. One cycle is cut to a monochromatic spanning path; two cycles are joined by the corollary.

For arbitrary reversal-antisymmetric h, a counterexample having such a two-cycle partition must exhibit both centered directed triangles for every pair c in C,d in D. This forces all four crossing statuses above at every junction pair. It is a necessary condition for that partition to fail, not a refutation of the grand conjecture.

### Scope and next obligation
The join preserves every vertex of both cycles and introduces only the two displayed crossing windows. It does not assume support union closure or a lift of antimatroid basic words. If C union D is a proper subset of V, the result remains a construction on that subset; exterior vertices still need to be incorporated.

Nor does the theorem justify repeated merging of three or more cycles: the merged object is a one-change path, not a monochromatic cycle. A cycle-cover reduction must therefore control its number of components or prove a further extension theorem.
