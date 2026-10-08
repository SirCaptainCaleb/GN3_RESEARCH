# Distance-three flat repair overlaps are square-or-root — preserved pre-item development

## Distance-three flat repair overlaps are square-or-root

Work in the coboundary-flat alternating ternary sector on five consecutive coordinates

(a,b,c,d,e).

Suppose the local status word is an isolated singleton

u,v,u,

with v=1-u,

and suppose BOTH bounding transitions are flat:

(a,b,c,d) supports the left transition u->v and admits the first-pair repair a<->b;

(b,c,d,e) supports the right transition v->u and admits the last-pair repair d<->e.

Flatness gives

alpha(a,c,d)=v,
alpha(b,c,e)=v.

Let

r=alpha(a,c,e).

### The two individual repairs

Swap a,b. The local word becomes

v,v,u.

Swap d,e. The local word becomes

u,v,v.

The swaps are disjoint as permutations and therefore commute.

### The opposite corner

After both swaps the local order is

(b,a,c,e,d).

Its three consecutive statuses are

v, r, v.

Thus only the single five-set chord bit r decides whether the two repairs truly fill a legal square.

### Case 1: r=v

The opposite-corner word is

v,v,v.

Moreover, after performing the left repair, the remaining right transition v->u lies on the tetrahedron (a,c,d,e). Its last-pair repair criterion is precisely

alpha(a,c,e)=v,

which holds. Coboundary flatness then supplies the complementary criterion automatically.

Hence the right repair remains legal after the left repair. Symmetrically the left repair remains legal after the right repair.

So the commuting square is fully realized and the isolated singleton is annihilated at the opposite corner.

### Case 2: r=u

Now the opposite-corner word is

v,u,v.

After the left repair, the surviving right transition v->u is supported on (a,c,d,e). Its two off-faces are

alpha(a,c,e)=u,
alpha(a,d,e)=v.

The second identity follows from coboundary flatness on {a,c,d,e}:

alpha(a,c,d) xor alpha(a,c,e) xor alpha(a,d,e) xor alpha(c,d,e)=0,

i.e.

v xor u xor alpha(a,d,e) xor u=0,

so alpha(a,d,e)=v.

For a flat v->u transition the off-faces would have to be v,u. Instead they are u,v. Therefore the surviving boundary is fully curved.

Thus after performing either one of the two original repairs, the other side becomes a fully-curved terminal barrier and emits its protected physical slide root.

The argument is symmetric if the right repair is performed first.

### Theorem

Two legal flat endpoint repairs at bonds separated by three positions have exactly two outcomes:

1. **commuting-square branch:** the second repair remains flat and the double repair annihilates the isolated singleton;
2. **root branch:** the second repair becomes fully curved immediately.

There is no third behavior and no recurrent distance-three overlap.

### Topological consequence

Together with separated commuting squares for bond distance at least four, every unresolved interaction of two flat ternary repair moves is now confined to bond distances one or two.

The distance-three overlap is already a complete realized 2-cell or an immediate protected-root exit.

This further localizes any Sperner/Tucker/fixed-point obstruction in the compatible repair complex to the genuinely overlapping A2/braid-scale packets.
