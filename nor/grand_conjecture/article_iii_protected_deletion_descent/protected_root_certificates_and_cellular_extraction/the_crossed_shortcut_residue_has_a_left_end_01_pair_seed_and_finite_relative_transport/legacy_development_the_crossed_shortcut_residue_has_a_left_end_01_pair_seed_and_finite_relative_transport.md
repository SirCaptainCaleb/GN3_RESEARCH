# The crossed shortcut residue has a left-end 01 pair seed and finite relative transport — preserved pre-item development

## Composition

(none yet)

## Development

## The crossed two-exterior shortcut residue has a left-end 01 pair seed and finite relative transport

Work in the sole crossed shortcut residue of §§301,304–305. Let
\[
O=(w_1,\ldots,w_m)
\]
be a NOR-good order of \(V\setminus\{x,z\}\), and write the two exterior scans
\[
X_i=\alpha(x,w_i,w_{i+1}),\qquad
Z_i=\alpha(z,w_i,w_{i+1}).
\]
Normalize the crossed endpoint data as
\[
X_1=0,\qquad Z_1=1.
\]

Define the pair-potential bits
\[
R_i=\alpha(x,z,w_i).
\]
By the pair-end calculation in §305,
\[
R_1=0.
\]
By tetrahedral parity on \(\{x,z,w_1,w_2\}\),
\[
R_2\oplus R_1=X_1\oplus Z_1=1,
\]
hence
\[
\boxed{R_2=1.}
\]

### A full-order 01 seed

Insert the ordered pair \(x,z\) between \(w_1\) and \(w_2\):
\[
\Pi=(w_1,x,z,w_2,w_3,\ldots,w_m).
\]

Its first two ternary windows are
\[
\alpha(w_1,x,z)=\alpha(x,z,w_1)=R_1=0
\]
by cyclic invariance, and
\[
\alpha(x,z,w_2)=R_2=1.
\]

Therefore
\[
\boxed{\Pi\text{ begins with the exact threshold seed }01.}
\]

No information about the later rail patterns is required.

### One-sided threshold transport

Fix the one-change target whose switch lies between these first two window ranks:
\[
0\,|\,1.
\]
Let \(I\) be the maximal target-compatible interval containing the initial \(01\) seed.

The left endpoint of \(I\) is already the global first window. Hence only the right endpoint can be unresolved.

If the nearest right mismatch is supported by a flat transition tetrahedron, apply the audited outward endpoint repair. By the threshold-band potential theorem, every previously matched window is preserved and \(I\) strictly enlarges to the right.

Crucially, every repair occurs at or beyond the current right boundary of \(I\). Thus the initial coordinate prefix
\[
\boxed{(w_1,x,z)}
\]
is never changed.

Since the full order has finitely many windows, the process terminates.

Its only outcomes are:

1. \(I\) reaches the global right endpoint, yielding a spanning one-change NOR order; or
2. the right boundary becomes fully curved, yielding an actual protected physical root while the prefix \((w_1,x,z)\) remains literally fixed.

### Theorem

Every crossed two-exterior shortcut residue satisfies the finite relative dichotomy
\[
\boxed{
\text{spanning NOR}
\quad\text{or}\quad
\text{protected full barrier with }(w_1,x,z)\text{ frozen}.
}
\]

By reversal, the same residue also gives a right-end transport with the corresponding terminal prefix/suffix data frozen.

### Consequence for the shortcut program

The opposite-scan binary ladder is not an independent recurrent obstruction. Its crossed boundary condition already contains a canonical pair-insertion threshold seed at an endpoint.

Thus the three-block shortcut analysis is now completely routed:

- unequal endpoint bits realize the direct shortcut or NOR;
- equal-ended residue closes by pair insertion (§301);
- crossed residue produces the endpoint \(01\) seed above and terminates in NOR or a relative protected-root exit.

The remaining Article III obligation is therefore a relative extraction theorem for protected barriers with the desired shortcut pair retained in frozen boundary provenance, rather than any further scan-ladder classification.
