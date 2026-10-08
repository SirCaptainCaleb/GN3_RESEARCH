# Deleting the middle old coordinate collapses the recursive packet to one earlier holonomy bit

## Composition

Deleting the middle old coordinate from the recursive double-full singleton removes the local 010 packet while preserving the ordered right boundary pair and hence the already-clean suffix. The only new left crossing is the earlier holonomy bit h_{j-4}. If that bit is 0 the deletion carrier is globally one-change; if it is 1 the sole remaining defect lies strictly farther left. Thus the recursive obstruction admits an explicit protected deletion that strictly ejects all failure from the old packet.

## Development

## Deleting the middle old coordinate collapses the recursive packet to one earlier holonomy bit

Continue with the recursive double-full singleton from subsection 55:

(r,t,u,x,a)
=
(v_{j-3},v_{j-2},v_{j-1},x,v_j),

with local word 010 and an already threshold-compatible suffix beginning at the ordered pair (x,a).

Delete the old coordinate

t=v_{j-2}.

The remaining local order is

(r,u,x,a).

Its two ternary statuses are

alpha(r,u,x)=0

from the left-fullness computation in subsection 55, and

alpha(u,x,a)=0

from the perfect-blocker scan.

Hence deletion of t removes the entire internal 010 defect and preserves the ordered right boundary pair (x,a). The clean right suffix is therefore unchanged.

### The only new left crossing bit

Let

q=v_{j-4}.

After deleting t, the first new crossing window on the left is

alpha(q,r,u).

By the tube holonomy identity,

h_{j-4}
=
alpha(v_{j-4},v_{j-3},v_{j-1})
=
alpha(q,r,u).

All windows farther left are unchanged old zero-phase windows.

Therefore the replacement deletion state has, near the splice,

...,0, h_{j-4}, 0,0,0,...,

followed by the already-clean original 0-to-1 suffix.

### Dichotomy

If h_{j-4}=0, the replacement deletion order is globally one-change: the recursive double-full obstruction disappears completely.

If h_{j-4}=1, the only excess variation is an isolated 1 strictly farther left. In particular no defect survives at or to the right of the old packet.

Thus deleting t converts the recursive five-coordinate obstruction into a single earlier holonomy bit and strictly moves every possible failure leftward.

This is stronger than an abstract root certificate: it is an explicit protected replacement deletion. The remaining obligation is to analyze the h_{j-4}=1 branch and show that its isolated earlier defect either admits the same kind of deletion collapse or contradicts minimum-phase extremality.
