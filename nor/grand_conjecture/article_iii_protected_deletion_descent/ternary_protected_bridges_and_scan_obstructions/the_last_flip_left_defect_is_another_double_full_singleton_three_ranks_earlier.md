# The last-flip left defect is another double-full singleton three ranks earlier

## Composition

Assume the last special-scan holonomy flip occurs at j>=4. After choosing its clean-right color-0 toggle state, the sole left defect is the five-coordinate packet
(r,t,u,x,a)=(v_{j-3},v_{j-2},v_{j-1},x,v_j)
with word 010.

The right transition tetrahedron {t,u,x,a} is fully curved by the forced-left-barrier theorem. The left transition tetrahedron {r,t,u,x} is also fully curved: the blocker scan rules out one endpoint repair, and flat four-face parity forces the opposite repair value to fail. Hence the residual defect is another double-full singleton.

Its residual holonomy is exactly H=alpha(r,t,a)=h_{j-3}. Thus the special branch is closed under the same local double-full geometry while the packet location moves three old ranks left at the level of normal forms.

This is not yet a terminating transport theorem. One still has to show that a standard resolution of this earlier packet preserves the already-clean right suffix and either eliminates the defect or produces the same state at a strictly earlier position. The cases j<4 are clipped endpoint cases and are outside this recursive statement.

## Development

## The last-flip left defect is another double-full singleton three ranks earlier

Continue from subsection 54. The canonical last-holonomy-flip state has otherwise threshold-compatible word, with one isolated left defect

0,1,0

on consecutive ternary windows.

Write the five involved coordinates as

(r,t,u,x,a)
=
(v_{j-3},v_{j-2},v_{j-1},x,v_j).

The three displayed statuses are

alpha(r,t,u)=0
from the old zero phase,

alpha(t,u,x)=alpha(x,t,u)=1
from the special blocker scan and cyclic invariance,

alpha(u,x,a)=1-alpha(x,u,a)=0
from the special blocker scan and alternation.

Thus (r,t,u,x,a) is a singleton 010 packet.

### The right transition is fully curved

Subsection 53 already proves that the tetrahedron
{t,u,x,a}
supporting 1->0 is fully curved.

### The left transition is also fully curved

Consider the tetrahedron
{r,t,u,x}
with ordered consecutive statuses 0,1.

The last-pair endpoint repair would require

alpha(r,t,x)=alpha(r,t,u)=0.

But the blocker scan gives alpha(x,r,t)=1, and cyclic invariance gives

alpha(r,t,x)=1.

So the last-pair repair fails.

Coboundary flatness on {x,r,t,u} gives

alpha(x,r,t)+alpha(x,r,u)+alpha(x,t,u)+alpha(r,t,u)=0.

Substituting
alpha(x,r,t)=1,
alpha(x,t,u)=1,
alpha(r,t,u)=0

forces
alpha(x,r,u)=0.

Cyclic invariance gives
alpha(r,u,x)=0.

For a 0->1 transition the first-pair repair would require alpha(r,u,x)=1, so it also fails.

Hence {r,t,u,x} is fully curved.

Therefore the isolated left defect is itself a double-full singleton packet.

### Its residual holonomy is an earlier tube bit

For the normalized double-full packet (r,t,u,x,a), the residual holonomy may be taken as

H=alpha(r,t,a).

But by the perfect-blocker holonomy definition,

h_{j-3}
=
alpha(v_{j-3},v_{j-2},v_j)
=
alpha(r,t,a).

Thus

H=h_{j-3}

whenever j>=4.

So after the last holonomy flip has cleaned the entire right side, the remaining obstruction recursively reappears as the same double-full singleton geometry three old positions to the left, with residual holonomy read directly from the earlier tube sequence.

This is a concrete candidate for a well-founded leftward transport: the obstruction state is closed under the same local geometry while its physical position decreases by three. The next task is to verify, holonomy branch by holonomy branch, that one of the standard five-set resolutions preserves the already-clean right suffix while moving or eliminating this packet.
