# A failed two-sided three-block shortcut produces a full barrier with the shortcut pair as its source shore — preserved pre-item development

## Development

## A failed two-sided three-block shortcut produces a full barrier with the shortcut pair as its source shore

Continue from §304. Fix distinct \(x,z\), and a good order
\[
O=(w_1,\ldots,w_m)
\]
of \(V\setminus\{x,z\}\), normalized by
\[
w(O)=0^p1^q.
\]

Assume neither \(xOz\) nor \(zOx\) gives NOR closure or a direct outermost root between \(x\) and \(z\).

By §304 there are exactly two crossed blocker types.

### Type I

The forced data are
\[
(A,B,C,D;E,F)=(1,0,0,1;1,1),
\]
where
\[
A=\alpha(x,w_1,w_2),\qquad
B=\alpha(z,w_1,w_2),\qquad
E=\alpha(x,z,w_1).
\]

Thus the first two windows of
\[
x,z,O
\]
are
\[
E,B=1,0.
\]

Consider the transition tetrahedron
\[
(x,z,w_1,w_2).
\]
For a \(1\to0\) transition, write the second off-face as
\[
Q=\alpha(x,w_1,w_2)=A=1.
\]

In the coboundary-flat alternating sector, a \(1\to0\) tetrahedron is flat exactly when its off-faces are
\[
(P,Q)=(1,0),
\]
and fully curved exactly when
\[
(P,Q)=(0,1).
\]
Since \(Q=1\), the transition is fully curved.

Therefore the barrier realizes the complete protected square
\[
x\to w_1,\qquad x\to w_2,\qquad
z\to w_1,\qquad z\to w_2.
\]

Its source shore is exactly
\[
\boxed{\{x,z\}}.
\]

### Type II

Now
\[
(A,B,C,D;E,F)=(0,1,1,0;0,0).
\]
Use the reversed singleton ordering
\[
z,x,O.
\]
Its first two windows are
\[
1-E,A=1,0,
\]
and the corresponding second off-face is
\[
\alpha(z,w_1,w_2)=B=1.
\]
Hence
\[
(z,x,w_1,w_2)
\]
is again fully curved.

It realizes the same source shore
\[
\{x,z\}
\]
with the two common targets \(w_1,w_2\).

### Theorem

For every pair of coordinates \(x,z\) and every good order \(O\) of the doubly-deleted subinstance, one of the following occurs:

1. a spanning NOR-good order;
2. a direct outermost root \(x\to z\) or \(z\to x\);
3. a fully-curved protected \(K_{2,2}\) barrier whose source shore is exactly \(\{x,z\}\).

Thus the failure of direct shortcut realization is itself a protected square certificate:
\[
\boxed{\text{direct shortcut or source-pair barrier}.}
\]

### Application to an endpoint-cycle junction

For consecutive protected-cycle vertices
\[
x\to y\to z,
\]
§291 certifies the physical shortcut pair \(x,z\). Apply the theorem to a good order of \(V\setminus\{x,z\}\).

If the direct shortcut \(x\to z\) is realized in the needed orientation, the cycle shortens immediately.

If direct realization fails in both orientations, then \(\{x,z\}\) is the source shore of an actual full barrier. Hence there are two distinct coordinates \(u,v\notin\{x,z\}\) with protected roots
\[
x\to u,\quad x\to v,\quad z\to u,\quad z\to v.
\]

The certified-shortcut obstruction is therefore converted into a concrete common-target square rather than another abstract one-sided recursion.
