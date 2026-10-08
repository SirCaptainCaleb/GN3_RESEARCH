# Canonical proper-face outermost roots form a strongly connected physical digraph

## Metadata

- ID: canonical_proper_face_outermost_roots_form_a_strongly_connected_physical_digraph
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 281
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Canonical proper-face outermost roots form a strongly connected physical digraph

Let \(H\) be the directed graph on the physical coordinate set \(V\) defined as follows.

Put a directed edge
\[
x\to y
\]
in \(H\) whenever some canonical proper-face witness \(\pi_F\) used by the root-valued boundary carrier has outermost root
\[
D(\pi_F)=e_x-e_y.
\]

Then \(H\) is strongly connected.

### Proof

Fix arbitrary distinct coordinates \(u,v\in V\).

Apply §278 with the arbitrary apex root
\[
\rho=e_v-e_u,
\]
viewed as the directed edge
\[
v\to u.
\]

The conical degree argument gives a support-minimal positive dependence containing \(\rho\). Removing the apex edge leaves a directed return path
\[
u=x_0\to x_1\to\cdots\to x_m=v
\]
whose every edge is the outermost root of a canonical proper-face witness from one nested flag.

Hence \(H\) contains a directed path from \(u\) to \(v\).

Since \(u,v\) were arbitrary, \(H\) is strongly connected.

### Strengthened path form

The same proof gives more than strong connectivity. For every ordered pair \(u,v\), there exists a chamber order \(\tau\) such that the chosen path
\[
u=x_0\to x_1\to\cdots\to x_m=v
\]
is strictly increasing in \(\tau\):
\[
x_0<_\tau x_1<_\tau\cdots<_\tau x_m.
\]

Thus every ordered pair has a simple flag-compatible monotone path through canonical proper-subinstance witnesses.

### Consequence

The proper-face carrier does not merely force an isolated root circulation. Its canonical witnessed-root digraph already spans all physical coordinates in both directed senses.

Any remaining realization theorem may therefore choose physical endpoints freely and request a canonical monotone witness path between them. In particular, the endpoints of any protected fully-curved barrier can be connected back through canonical proper-face witnesses without rebuilding the degree argument.

## Frontier

- Development version when composed: None
- Development version now: 1
