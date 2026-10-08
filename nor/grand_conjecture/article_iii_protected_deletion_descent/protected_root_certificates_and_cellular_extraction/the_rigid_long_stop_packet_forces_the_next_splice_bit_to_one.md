# The rigid long-stop packet forces the next splice bit to one

## Composition

(none yet)

## Development

## The rigid long-stop packet forces the next splice bit to one

Continue from Subsection 145. Thus
O_x=(a,b,c,d,e,f,...)
is a good deletion witness omitting x with word 0^p1^q, p>=4, and the first two splice bits satisfy
alpha(a,c,d)=alpha(a,d,e)=1.

Assume all witness-preserving same-profile surgeries of §145 have failed. Then the unique residual bit pattern is
alpha(x,c,d)=1,
alpha(x,a,e)=0,
alpha(a,b,e)=1.

The derived identities include
alpha(x,b,d)=0,
alpha(x,a,d)=0,
alpha(a,b,d)=1,
alpha(b,d,e)=1.

Let
nu=alpha(a,e,f),
where the old zero phase gives alpha(d,e,f)=0.

### Rank-3 barrier

The one-defect deletion state from §128 is
O_c=(x,b,a,d,e,f,...)
with exact prefix
0,0,1,0,...
against the target 0^p1^q.

Its rank-3 transition is the ordered tetrahedron
Q_3=(a,d,e,f)
with statuses
alpha(a,d,e)=1,
alpha(d,e,f)=0.

Coboundary flatness on {a,d,e,f} gives
alpha(a,d,f)=1 xor nu.

For a 10 transition, flatness is equivalent to the two repair faces having the target values
alpha(a,d,f)=1,
alpha(a,e,f)=0.
Hence:

- nu=0 iff Q_3 is flat;
- nu=1 iff Q_3 is fully curved.

We show the flat case closes completely.

### If nu=0, the second barrier is forced flat

Perform the inward first-pair repair of Q_3, swapping a,d:
(x,b,a,d,e,f,...)
 ->
(x,b,d,a,e,f,...).

Using the residual identities, the first four statuses are
alpha(x,b,d)=0,
alpha(b,d,a)=alpha(a,b,d)=1,
alpha(d,a,e)=0,
alpha(a,e,f)=0.

Thus the prefix is
0,1,0,0,...

The next 10 barrier is
Q_2=(b,d,a,e).

Its two repair faces are
alpha(b,d,e)=1,
alpha(b,a,e)=1-alpha(a,b,e)=0.

These are exactly the flat 10 values. Therefore Q_2 is forced flat.

Swap b,d:
(x,b,d,a,e,f,...)
 ->
(x,d,b,a,e,f,...).

The prefix becomes
1,0,0,0,...
because
alpha(x,d,b)=1-alpha(x,b,d)=1.

### The endpoint barrier is also forced flat

The remaining 10 endpoint barrier is
Q_1=(x,d,b,a).

Its two repair faces are
alpha(x,d,a)=1-alpha(x,a,d)=1,
alpha(x,b,a)=1-alpha(x,a,b)=0.

Again these are exactly the flat 10 values.

Swap x,d. There is no earlier window, and every later target status was already zero through the old first phase. Hence the resulting deletion order, still omitting c, has exact word
0^p1^q.

Thus nu=0 gives a genuine witness-preserving return to the good-deletion class after exactly three flat repairs.

### Consequence

In the unique rigid residual of §145, a minimum counterexample must satisfy
alpha(a,e,f)=1.

Therefore the long stopped endpoint obstruction has now forced THREE consecutive splice bits:
alpha(a,c,d)=1,
alpha(a,d,e)=1,
alpha(a,e,f)=1.

Equivalently, among the three possible barriers in the exact prefix extraction of §135, the second and third can never be terminal in the rigid residual; if the first one is flat, the rest of the repair sequence is deterministically flat and returns to a good deletion witness.

The only surviving local outcome is the fully-curved rank-3 barrier
(a,d,e,f),
and its full curvature is exactly the next splice-bit condition nu=1.

This suggests an inductive splice propagation along the old zero phase: each failed witness-preserving repair may force the next chord alpha(a,v_j,v_{j+1}) to equal one. The next task is to formulate and prove that propagation without assuming a special blocker scan.
