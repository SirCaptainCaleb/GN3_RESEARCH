# Failure of both oriented three-block shortcuts forces a crossed two-coordinate blocker pattern

## Metadata

- ID: failure_of_both_oriented_three_block_shortcuts_forces_a_crossed_two_coordinate_blocker_pattern
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 304
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For distinct x,z and a good order O of V\{x,z}, if neither oriented three-block witness xOz nor zOx closes NOR or realizes a direct x-z outermost root, all endpoint and pair bits are forced into one of two complementary crossed blocker patterns. One exterior coordinate blocks exactly where the other is compatible, and the roles reverse at the opposite endpoint.

## Development

## Failure of both oriented three-block shortcuts forces a crossed two-coordinate blocker pattern

Assume a minimum counterexample. Fix distinct coordinates \(x,z\), and let
\[
O=(w_1,\ldots,w_m)
\]
be a NOR-good order of
\[
V\setminus\{x,z\}.
\]

Normalize
\[
w(O)=0^p1^q,\qquad p,q\ge1.
\]

Define the endpoint insertion bits
\[
A=\alpha(x,w_1,w_2),\qquad
B=\alpha(z,w_1,w_2),
\]
\[
C=\alpha(w_{m-1},w_m,x),\qquad
D=\alpha(w_{m-1},w_m,z).
\]

Also define the pair bits
\[
E=\alpha(x,z,w_1),\qquad
F=\alpha(w_m,x,z).
\]

### Adjacent singleton blocks constrain the left endpoint

The order
\[
x,z,O
\]
has status word
\[
E,\ B,\ 0^p1^q.
\]
If \(E=B=0\), this word has at most one change, impossible. Hence
\[
(E,B)\ne(0,0).
\]

Similarly
\[
z,x,O
\]
has word
\[
1-E,\ A,\ 0^p1^q,
\]
because swapping \(x,z\) complements the first ternary window. Therefore
\[
(1-E,A)\ne(0,0).
\]

Consequently
\[
A=0\Longrightarrow E=0\Longrightarrow B=1,
\]
and
\[
B=0\Longrightarrow E=1\Longrightarrow A=1.
\]

In particular \(A,B\) cannot both be \(0\).

### The right endpoint is dual

The order
\[
O,x,z
\]
has word
\[
0^p1^q,\ C,\ F.
\]
If \(C=F=1\), it is NOR-good. Hence
\[
(C,F)\ne(1,1).
\]

The order
\[
O,z,x
\]
has word
\[
0^p1^q,\ D,\ 1-F.
\]
Thus
\[
(D,1-F)\ne(1,1).
\]

Consequently
\[
C=1\Longrightarrow F=0\Longrightarrow D=0,
\]
and
\[
D=1\Longrightarrow F=1\Longrightarrow C=0.
\]

So \(C,D\) cannot both be \(1\).

### Assume both oriented three-block witnesses fail directly

By §295, the order \(xOz\) gives:

- closure if \((A,D)=(0,1)\);
- direct root \(x\to z\) if \((A,D)=(1,0)\);
- a one-sided root only when \(A=D\).

Likewise \(zOx\) gives closure or the direct root \(z\to x\) unless
\[
B=C.
\]

Suppose neither orientation gives closure nor a direct \(x\)-\(z\) root. Then
\[
A=D,\qquad B=C.
\]

There are only two possibilities.

#### Type I
If
\[
A=D=1,
\]
then \(D=1\) forces \(C=0\), hence \(B=0\). Then \(B=0\) forces \(E=1\), and \(D=1\) forces \(F=1\). Thus
\[
\boxed{(A,B,C,D;E,F)=(1,0,0,1;1,1).}
\]

#### Type II
If
\[
A=D=0,
\]
then \(A=0\) forces \(B=1\), hence \(C=1\). Then \(A=0\) forces \(E=0\), and \(C=1\) forces \(F=0\). Thus
\[
\boxed{(A,B,C,D;E,F)=(0,1,1,0;0,0).}
\]

These types are exchanged by swapping \(x,z\) together with reversal/color normalization.

### Interpretation

In Type I:
\[
xOz:\quad 1,0^p1^q,1,
\]
while
\[
zOx:\quad 0,0^p1^q,0.
\]
The coordinate \(x\) is the left blocker and \(z\) is the right blocker.

In Type II the roles are reversed.

Thus failure of the certified shortcut \(x\leftrightarrow z\) in both orientations is no longer an arbitrary one-sided recursion. It forces a rigid **crossed blocker pair**: one coordinate blocks the left endpoint exactly where the other is compatible, and their roles reverse at the right endpoint. The pair windows \(E,F\) are forced to the same blocker color.

This is the remaining two-coordinate local object for shortcut realization.
