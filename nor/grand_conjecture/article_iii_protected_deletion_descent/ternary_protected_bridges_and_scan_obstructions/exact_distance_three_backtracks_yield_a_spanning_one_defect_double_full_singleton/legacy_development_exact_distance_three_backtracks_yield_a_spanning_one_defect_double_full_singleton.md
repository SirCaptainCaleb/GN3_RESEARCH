# Exact distance-three backtracks yield a spanning one-defect double-full singleton — preserved pre-item development

## Composition

(none yet)

## Development


Work in the coboundary-flat ternary sector and assume the exact d=e=3 backtrack of the corrected arbitrary-scan replacement dynamics.

Use the audited notation

a=v_{p+1}, z=v_{p+2}, y=v_{p+3}, b=v_{p+4}, c=v_{p+5},

with omitted coordinate x.

The original deletion carrier has

alpha(a,z,y)=1,
alpha(z,y,b)=1,
alpha(y,b,c)=1,

while the distance-three replacement data give

alpha(a,z,x)=0,
alpha(x,z,y)=0,
alpha(x,y,b)=0,
alpha(x,b,c)=0.

By alternation,

alpha(z,x,y)=1.

Now insert both exchanged coordinates consecutively in the full-support order

...,a,z,x,y,b,c,...

while leaving every outside coordinate in its old relative position.

The four displayed consecutive ternary statuses are

alpha(a,z,x)=0,
alpha(z,x,y)=1,
alpha(x,y,b)=0,
alpha(y,b,c)=1.

The old prefix immediately before this packet is still in color 0 and the old suffix immediately after it is still in color 1.

Therefore the full spanning word has exactly one threshold defect relative to the natural 0-to-1 cut:

0...0, 1, 0, 1...1,

where the middle displayed 0 is the unique wrong-color window in the 1-phase.

Equivalently, the cyclic variation is four and one of its runs has length one.

### The singleton is bounded by two fully-curved tetrahedra

The singleton wrong window is alpha(x,y,b)=0. Its neighboring statuses are

alpha(z,x,y)=1,
alpha(y,b,c)=1.

The left transition tetrahedron is

Q_L={z,x,y,b}.

Its consecutive statuses are 1,0, and the opposite face satisfies

alpha(z,y,b)=1.

By the flat/full transition classification, Q_L is fully curved.

The right transition tetrahedron is

Q_R={x,y,b,c}.

Its consecutive statuses are 0,1, and the opposite face satisfies

alpha(x,b,c)=0.

Again the flat/full transition classification gives that Q_R is fully curved.

Hence every exact d=e=3 backtrack canonically produces a full-support singleton threshold defect trapped between two adjacent fully-curved switch gadgets.

### Residual five-set geometry

On the five-set {z,x,y,b,c}, coboundary flatness leaves exactly one residual holonomy bit, as in the double-full singleton classification. The internal five-set is therefore completely understood up to that one bit; the only unresolved issue is reconnection to the opposite-color 0-prefix on the left and 1-suffix on the right.

### Flat-sector frontier

After the audited arbitrary-scan reductions:

- short p=2 or q=2 phases enter the same dynamics;
- residual drift terminates by reversal minimality;
- the d=e=2 A2 recurrence is killed by the boundary-compatible five-set weave;
- the only remaining recurrent branch d=e=3 is equivalent to the one-defect double-full singleton described above.

Thus unconditional closure of the coboundary-flat ternary sector is reduced to one boundary-surgery lemma:

> A spanning ternary order whose threshold word has exactly one wrong-color window and whose two bounding transition tetrahedra are fully curved can be transformed into a spanning one-change order.

The five-set itself is locally cancellable; only the protected reconnection to the two opposite-color exterior phases remains open.
