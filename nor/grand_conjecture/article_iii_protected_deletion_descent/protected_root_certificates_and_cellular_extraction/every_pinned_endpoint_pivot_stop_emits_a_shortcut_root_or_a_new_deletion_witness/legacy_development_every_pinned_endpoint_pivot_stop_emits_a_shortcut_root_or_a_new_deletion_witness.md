# Every pinned endpoint pivot stop emits a shortcut root or a new deletion witness — preserved pre-item development

## Development

At a pinned boundary of a minimum-length endpoint-root cycle, use the endpoint witness
O_x=(a,b,c,d,e,...)
omitting x, with one-change word beginning in at least three zero windows. Prepending x gives the fully-curved endpoint barrier, so
alpha(x,a,c)=0.
Put
lambda_0=alpha(a,c,d),
lambda_1=alpha(x,c,d).

The double-zero case lambda_0=lambda_1=0 is already excluded by the endpoint-pivot shortcut theorem, since it realizes a shorter endpoint-root cycle.

The three surviving stop types are not terminal.

1. First-stop type lambda_0=1, lambda_1=0.
Deleting b from the prepended endpoint state gives
O_b=(x,a,c,d,e,...)
with local statuses 0,1,0,...
on xac, acd, cde.
On Q={x,a,c,d}, coboundary flatness gives
alpha(x,a,d)=lambda_0 xor lambda_1=1.
Thus for the 0->1 transition both endpoint repairs fail:
the last-pair repair would require alpha(x,a,d)=0,
while the first-pair repair would require alpha(x,c,d)=1.
Hence Q is fully curved and emits the protected shortcut root
e_x-e_d.

2. Second-stop type lambda_0=0, lambda_1=1.
The first pivot is legal, so O_b=(x,a,c,d,...) is a genuine one-change deletion witness omitting b. Its endpoint tetrahedron (b,x,a,c) is fully curved, giving
alpha(b,x,c)=0.
Deleting a produces the local singleton
(b,x,c,d,e,...)
with statuses 0,1,0,...
because alpha(x,c,d)=1 and the untouched old window alpha(c,d,e)=0.
On {b,x,c,d}, the first-pair repair would require alpha(b,c,d)=1, but alpha(b,c,d)=0 is the second old zero-phase window. Coboundary flatness then forces the other endpoint repair to fail as well. Thus this tetrahedron is fully curved and emits the shortcut root
e_b-e_d.

3. Flat first-stop type lambda_0=lambda_1=1.
For Q={x,a,c,d}, coboundary flatness gives alpha(x,a,d)=0. Hence the 0->1 transition is flat and admits both endpoint repairs. Choose the last-pair repair c<->d, preserving the ordered left boundary (x,a). The first two new statuses are 0,0, while
alpha(d,c,e)=1-alpha(c,d,e)=1.
Thus the repair creates a contiguous 1-band inside the old zero phase with a clean zero prefix. Apply threshold-band combing to the right boundary of this inserted 1-band. Every flat boundary repair strictly moves its right endpoint toward the original one phase; the finite process either merges with that phase, yielding a genuine one-change deletion witness, or stops at a fully-curved protected-root barrier.

Therefore every pinned endpoint pivot stop has a certified progress outcome:
- immediate protected shortcut root; or
- a new one-change deletion witness; or
- a fully-curved protected root after finite one-sided combing.

The local one-bit stop is not an endpoint obstruction. After the pivot-shortening reduction, the surviving endpoint frontier is global exploitation of these emitted roots/witnesses, especially when all emitted roots remain on the same side of the threshold.
