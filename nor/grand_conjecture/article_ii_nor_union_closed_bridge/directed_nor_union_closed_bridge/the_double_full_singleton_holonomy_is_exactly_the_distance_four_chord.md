# The double-full singleton holonomy is exactly the distance-four chord

## Composition

(none yet)

## Development


Work in the coboundary-flat ternary sector and normalize a coordinate order so every adjacent tournament edge points forward. Then consecutive ternary statuses are the distance-two chord bits.

Take five consecutive vertices 0,1,2,3,4 with singleton pattern

alpha(0,1,2)=0,
alpha(1,2,3)=1,
alpha(2,3,4)=0,

and assume both transition tetrahedra {0,1,2,3} and {1,2,3,4} are fully curved.

In Hamilton-normalized chord coordinates, full curvature at a transition is equivalent to the corresponding distance-three chord being zero. Hence

t(0,3)=0,
t(1,4)=0.

Let h be the residual five-set holonomy bit from the double-full analysis:

h=alpha(0,1,4).

Using the tournament formula

alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a)

and the normalized adjacent edge t(0,1)=1, together with t(1,4)=0 and t(4,0)=1 xor t(0,4), one obtains

h
=1 xor 1 xor 0 xor (1 xor t(0,4))
=1 xor t(0,4).

Therefore

h=1  iff  t(0,4)=0,
h=0  iff  t(0,4)=1.

So the residual double-full holonomy is exactly the complemented distance-four chord across the five-coordinate packet.

By the previously proved boundary-holonomy theorem:
- a backward distance-four chord t(0,4)=0 is precisely the branch admitting the coherent two-sided monochromatic resolution;
- a forward distance-four chord t(0,4)=1 is precisely the branch in which every monochromatic cancellation must export a one-sided boundary mismatch.

This identifies two previously separate pieces of the flat-sector analysis. The extra distance-four memory required by three-step switch transport and the residual five-set holonomy of double-full barrier cancellation are the same type of tournament datum.
