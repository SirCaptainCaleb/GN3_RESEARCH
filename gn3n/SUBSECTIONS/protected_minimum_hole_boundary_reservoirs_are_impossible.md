# Protected fixed-boundary reservoirs are disjoint from minimum holes

## Metadata

- ID: protected_minimum_hole_boundary_reservoirs_are_impossible
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 148
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Strengthening: a protected fixed-boundary reservoir cannot contain even one minimum-hole label

Let (X) be a minimum two-cover deletion set and let
[
H-X=Pmid Q,qquad P=(z,z_1,z_2,z_3,ldots)
]
be a displayed complementary two-cover.

Let (F) be a protected face with a nonempty free block (B) whose last two positions form the first two positions of the selected left span-two window, followed by the fixed inherited labels
[
z,z_1,z_2,z_3.
]

The protection argument from [[protection_forces_a_minimum_hole_boundary_reservoir_to_be_uniformly_blocked]] forces, for **every** (vin B),
[
h(v,z,z_1)=1.
]
This part of that proof uses only protection together with
[
h(z,z_1,z_2)=h(z_1,z_2,z_3)=1;
]
it does not use (Bsubseteq X).

Now suppose merely that
[
vin Bcap X.
]
Then
[
(v,z,z_1,z_2,z_3,ldots)
]
is a tight path on (V(P)cup{v}). Together with the untouched path (Q), it gives a two-cover of
[
H-(X-{v}),
]
using only (|X|-1) deleted vertices. This contradicts minimality of (X).

Hence
[
oxed{Bcap X=arnothing.}
]

> **Protected boundary-reservoir exclusion.** In the fixed-boundary geometry above, a protected free block immediately facing an inherited tight component is completely disjoint from every minimum two-cover deletion set that produces that component.

This strictly strengthens development version 1, which assumed (Bsubseteq X). No such global inclusion is needed.

### Article VII consequence

Any protected terminal-pair loop whose free reservoir block contains one or more labels of the active minimum hole cannot occur against a fixed inherited tight boundary segment.

In particular, when a genuine two-deletion normalization has a central movable block containing the two minimum-hole labels, that block cannot simultaneously serve as the protected boundary reservoir in this fixed-boundary model. A surviving carrier loop must therefore change roles: its reservoir labels must avoid the minimum pair, or its neighboring boundary must cease to be the fixed inherited path segment, or the carrier must use a different positional enlargement.

This removes a much larger overlap between the genuine two-deletion core and the terminal-pair loop than previously recorded.

## Frontier

- Development version when composed: None
- Development version now: 2
