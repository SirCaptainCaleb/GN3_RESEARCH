# A rotation-blocked special vertex has two one-sided expulsion orders — preserved pre-item development

Work in the zero-polarity case of the blocked special cell from §21:
(p,a,x,b,c),
with both A2 rotations blocked. Then the barrier bits are zero, and the shore relations imply that
(p,a,b,c)
is itself a monochromatic-zero four-coordinate path. Its first shore edge p->a and last shore edge b->c are forward.

Since x is the sink-side special vertex relative to the shore, prepending x to this four-path gives
(x,p,a,b,c)
with word 000:
alpha(x,p,a)=0 because p->a and both shore vertices dominate x, while the remaining two windows are those of the zero four-path.

Likewise appending x gives
(p,a,b,c,x)
with word 000 because the final shore edge b->c is forward.

Thus a rotation-blocked x has two exact one-sided expulsion orders:
- x,p,a,b,c preserves the right ordered collar (b,c) and exports reconnection only to the left;
- p,a,b,c,x preserves the left ordered collar (p,a) and exports reconnection only to the right.

The reversed monochromatic polarity gives the symmetric statement, and the same argument applies to z.

This strengthens collar-removability. A blocked special is not merely deletable: once one exterior side is clipped or otherwise released, it can be moved across the whole four-shore barrier in one step while the opposite exterior side remains frozen. Therefore special-vertex barriers support a strict outward-distance strategy when endpoint compatibility is treated as a target rather than an invariant.
