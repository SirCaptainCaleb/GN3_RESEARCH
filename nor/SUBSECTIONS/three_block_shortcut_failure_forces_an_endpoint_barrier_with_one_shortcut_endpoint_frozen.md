# Three-block shortcut failure forces an endpoint barrier with one shortcut endpoint frozen

## Metadata

- ID: three_block_shortcut_failure_forces_an_endpoint_barrier_with_one_shortcut_endpoint_frozen
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 298
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Failure of a three-block shortcut forces an endpoint barrier with the shortcut endpoint frozen

Continue from §295. Fix distinct coordinates \(x,z\), let
\[
W=V\setminus\{x,z\},
\]
and choose a NOR-good order
\[
O=(w_1,\ldots,w_m)
\]
of \(W\) with normalized word
\[
0^p1^q.
\]
Write
\[
L=\alpha(x,w_1,w_2),\qquad
R=\alpha(w_{m-1},w_m,z).
\]

The direct-shortcut and closure cases of §295 are \(L\ne R\). We analyze the two same-bit cases.

### Case 1: \(L=R=1\)

Then
\[
H=O,z
\]
is a NOR-good order of \(V\setminus\{x\}\), with word
\[
0^p1^{q+1}.
\]
The coordinate \(z\) is frozen as its final coordinate.

Because the ambient instance is a minimum counterexample, appending the omitted coordinate \(x\) to \(H\) must create a second change. Hence
\[
\alpha(w_m,z,x)=0.
\]

Now insert \(x\) immediately before the final coordinate \(z\). The two new terminal windows have colors
\[
\alpha(w_{m-1},w_m,x),\qquad
\alpha(w_m,x,z)=1-\alpha(w_m,z,x)=1.
\]
If
\[
\alpha(w_{m-1},w_m,x)=1,
\]
the old terminal 1-window is replaced by \(1,1\), and the full order remains one-change, contradiction.

Therefore
\[
\alpha(w_{m-1},w_m,x)=0.
\]

The full order
\[
H,x=(w_1,\ldots,w_m,z,x)
\]
has terminal transition
\[
\alpha(w_{m-1},w_m,z)=1
\longrightarrow
\alpha(w_m,z,x)=0.
\]
Its two off-faces are
\[
\alpha(w_{m-1},w_m,x)=0
\]
and, by four-face parity,
\[
\alpha(w_{m-1},z,x)=1.
\]
Thus this terminal transition is fully curved.

Consequently failure of the shortcut in the \(11\) case forces an actual endpoint barrier on
\[
(w_{m-1},w_m,z,x),
\]
with slide root
\[
\boxed{w_{m-1}\to x},
\]
while \(z\) is the penultimate endpoint coordinate of the good deletion witness.

### Case 2: \(L=R=0\)

Now
\[
H=x,O
\]
is a NOR-good order of \(V\setminus\{z\}\), with word
\[
0^{p+1}1^q,
\]
and \(x\) is frozen as its first coordinate.

By the reversed argument, prepending the omitted coordinate \(z\) must create a second change, and inserting \(z\) immediately after the first coordinate cannot preserve the one-change word. The resulting initial endpoint transition is therefore fully curved.

Equivalently, after applying full reversal to Case 1, shortcut failure in the \(00\) case produces an actual endpoint barrier whose protected root has target \(z\), with \(x\) frozen at the opposite global endpoint of the good deletion witness.

### Strengthened shortcut dichotomy

For the three-block state \(xOz\), exactly one of the following occurs:

1. \(xOz\) is spanning NOR-good;
2. \(D(xOz)=e_x-e_z\), directly realizing the shortcut;
3. \(O,z\) is a good deletion witness omitting \(x\), with \(z\) frozen at its final endpoint, and the opposite insertion of \(x\) creates a fully-curved terminal barrier;
4. \(x,O\) is a good deletion witness omitting \(z\), with \(x\) frozen at its first endpoint, and the opposite insertion of \(z\) creates a fully-curved initial barrier.

Thus failure of the certified shortcut always returns to the endpoint-barrier class with one desired shortcut endpoint retained literally at the boundary.

## Frontier

- Development version when composed: None
- Development version now: 1
