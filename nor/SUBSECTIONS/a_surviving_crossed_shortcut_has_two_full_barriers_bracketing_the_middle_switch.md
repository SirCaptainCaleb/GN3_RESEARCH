# Corrected: the crossed shortcut has two endpoint-pinned threshold transports

## Metadata

- ID: a_surviving_crossed_shortcut_has_two_full_barriers_bracketing_the_middle_switch
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 316
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Corrected: the crossed shortcut has two endpoint-pinned threshold transports

Continue from §314. Let
\[
O=(w_1,\ldots,w_m)
\]
have word
\[
0^p1^q
\]
in the crossed shortcut residue.

Because both
\[
xO,\qquad Ox
\]
are good deletion witnesses omitting \(z\), §287 implies
\[
p,q\ge3.
\]

### Left endpoint seed

Section §314 inserts \(x,z\) after \(w_1\):
\[
\Pi_L=(w_1,x,z,w_2,\ldots,w_m),
\]
whose first two windows are exactly
\[
0,1.
\]

Fix the one-change threshold target with its switch between these first two window ranks. The maximal matched interval already reaches the global left endpoint.

Outward flat repair therefore proceeds only to the right. Every repair preserves the whole previously matched interval, so in particular the coordinate prefix
\[
(w_1,x,z)
\]
is retained throughout the transport.

Finite termination gives:
1. a spanning NOR-good order; or
2. a fully-curved right boundary carrying an actual protected root, with \((w_1,x,z)\) still frozen.

### Right endpoint seed

The crossed endpoint data also give
\[
R_{m-1}=1,\qquad R_m=0.
\]
Insert the reversed pair \(z,x\) between \(w_{m-1}\) and \(w_m\):
\[
\Pi_R=(w_1,\ldots,w_{m-1},z,x,w_m).
\]
Its final two windows are
\[
0,1.
\]

Use the one-change threshold target whose switch lies between those final two ranks. The matched interval already reaches the global right endpoint, so outward flat repair proceeds only to the left and preserves the terminal triple
\[
(z,x,w_m).
\]

Again the outcome is:
1. a spanning NOR-good order; or
2. a fully-curved left boundary carrying an actual protected root, with \((z,x,w_m)\) frozen.

### What is and is not localized

The two endpoint-pinned transports are rigorous. They preserve the distinguished pair \(\{x,z\}\) in opposite boundary orientations and produce either closure or relative protected-root exits.

One must NOT infer that the terminal barriers lie on prescribed sides of the original switch of \(O\). An outward flat repair changes windows farther outward from the current matched interval; before the front reaches the old switch it may already have altered windows beyond that front, including windows near or beyond the original switch. Hence the original phase decomposition of \(O\) is not a fixed background during transport.

### Correct conclusion

Every surviving crossed shortcut residue supplies two relative protected-root exits:
\[
\boxed{
(w_1,x,z)\ \text{frozen at the left}
\qquad\text{and}\qquad
(z,x,w_m)\ \text{frozen at the right}.
}
\]

The next valid closure target is to compare or glue these two endpoint-relative exits through their retained \(\{x,z\}\) provenance.

## Frontier

- Development version when composed: None
- Development version now: 2
