# Failed one-vertex connector absorption has a two-sided blocker normal form

## Metadata

- ID: failed_one_vertex_connector_absorption_has_a_two_sided_blocker_normal_form
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 360
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Failed one-vertex absorption has the stated no-010 blocker structure. This controls monochromatic insertion, not endpoint-port compatibility: a whole connector state must retain both exposed forward pairs.

## Development

## Failure to absorb one shore vertex into a zero connector has a two-sided blocker normal form

Let
\[
Q=(q_1,\ldots,q_m)
\]
be a monochromatic zero connector:
\[
\alpha(q_i,q_{i+1},q_{i+2})=0
\qquad(1\le i\le m-2).
\]
Assume \(x,z\) occur consecutively in \(Q\), in the order \(x,z\).

Fix a new shore vertex
\[
a\in A\setminus V(Q).
\]
Define its insertion scan along \(Q\):
\[
s_i=\alpha(a,q_i,q_{i+1}),
\qquad 1\le i\le m-1.
\]

Because \(a\in A\),
\[
\alpha(x,z,a)=0.
\]
By cyclic invariance,
\[
\alpha(a,x,z)=0.
\]
Hence the scan has a forced zero at the \(xz\)-edge.

### Endpoint insertion

Prepending \(a\) produces only one new ternary window:
\[
(a,q_1,q_2).
\]
Therefore prepending preserves monochromatic zero exactly when
\[
s_1=0.
\]

Similarly, appending \(a\) preserves monochromatic zero exactly when
\[
s_{m-1}=0.
\]

### Interior insertion

Insert \(a\) between \(q_i\) and \(q_{i+1}\). The three new windows are
\[
(q_{i-1},q_i,a),\qquad
(q_i,a,q_{i+1}),\qquad
(a,q_{i+1},q_{i+2}).
\]
By cyclic invariance and alternation their colors are
\[
s_{i-1},\qquad
1-s_i,\qquad
s_{i+1}.
\]

Thus the insertion preserves monochromatic zero exactly when
\[
\boxed{(s_{i-1},s_i,s_{i+1})=(0,1,0).}
\]

### Exact obstruction normal form

Therefore \(a\) is NOT absorbable anywhere into \(Q\) iff:

1. \(s_1=1\);
2. \(s_{m-1}=1\);
3. the scan contains no occurrence of \(010\).

Since the \(xz\)-edge contributes a zero, any failed scan is nonconstant. Starting and ending at \(1\), it must contain both a \(1\to0\) transition before the zero-run containing \(xz\), and a \(0\to1\) transition after it.

Moreover the absence of \(010\) means every internal 1-run has length at least two.

Hence every failed one-vertex absorption has the canonical form
\[
1\cdots1\;0\cdots0\;1\cdots1
\]
possibly with additional zero-runs, but with no isolated internal \(1\), and with the distinguished \(xz\)-edge lying in a zero-run bracketed on both sides by blocker transitions.

### Consequence

The collective connector problem can be attacked one vertex at a time. At the first vertex whose absorption fails, the obstruction is not arbitrary: it is a two-sided insertion blocker around the protected \(xz\)-edge.

Each boundary of the distinguished zero-run is an actual four-coordinate transition involving \(a\). Flat boundaries can be pushed outward by the existing insertion/threshold repair machinery; a terminal boundary is fully curved and therefore emits a protected physical root.

Thus growth of a compatible connector reduces to resolving a pair of blocker transitions around one forced-zero edge.
