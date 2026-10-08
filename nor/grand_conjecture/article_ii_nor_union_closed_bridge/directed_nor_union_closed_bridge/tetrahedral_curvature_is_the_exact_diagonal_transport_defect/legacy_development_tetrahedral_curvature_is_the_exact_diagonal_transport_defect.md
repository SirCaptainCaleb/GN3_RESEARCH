# Tetrahedral curvature is the exact diagonal transport defect — preserved pre-item development

## Development


## Tetrahedral curvature is the exact diagonal transport defect

Let O=(...,a,b,c,...) be an ordered coordinate sequence and let x be an exterior vertex. Work with the alternating triangle orientation alpha, written additively in F_2.

Define the local scan signs

s_0 = alpha(x,a,b),
s_1 = alpha(x,b,c),

the old consecutive status

c_0 = alpha(a,b,c),

and the diagonal sign

t = alpha(x,a,c).

Let kappa(x,a,b,c) be the tetrahedral coboundary bit delta f on the underlying four-set, using any fixed global ordering convention. After absorbing the fixed parity convention into kappa, one has the invariant transport identity

t = s_0 xor s_1 xor c_0 xor kappa.

Equivalently,

kappa = s_0 xor s_1 xor c_0 xor t.

### Meaning

The three pieces visible to one-vertex insertion -- the two adjacent scan values and the old status -- do not determine the diagonal triangle alpha(x,a,c) unless the tetrahedral curvature bit is also known.

Thus kappa is exactly the obstruction to flat transport of the scan across the old edge pair a-b-c.

When kappa=0,

t = s_0 xor s_1 xor c_0.

When kappa=1, the transported diagonal sign is flipped.

### Audit of the naive connector crossing claim

A move of x from one insertion gap to the next only reads consecutive-window data such as s_0,s_1 and c_0. The singly-curved condition kappa=1 also depends on the diagonal face t. Therefore singly-curved support by itself does not determine whether the orientation-compatibility failure changes side when the insertion gap moves.

Any Connector/Sperner carrier based only on safe insertion gaps and the support of delta f forgets one necessary local bit.

### Corrected connector packet

The minimal local packet for transporting an insertion certificate across adjacent gaps is the tetrahedral packet

(s_0,s_1,c_0,t;kappa),

with the displayed identity making one coordinate redundant.

Geometrically, this means the connector carrier must live on the full tetrahedral 2-skeleton, not merely on the dual support of the 3-coboundary. The diagonal face alpha(x,a,c) is the transport state.

This is promising rather than merely obstructive: kappa now has an exact operational role. It is the curvature of a discrete F_2 connection transporting the diagonal sign along the insertion scan. A future connector argument can accumulate kappa along a chain, with parity conservation delta^2 f=0 controlling path independence around 4-simplex cells.
