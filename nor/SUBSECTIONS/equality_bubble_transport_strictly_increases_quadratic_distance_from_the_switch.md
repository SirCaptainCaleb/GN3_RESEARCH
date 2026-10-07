# Equality bubble transport strictly increases quadratic distance from the switch

## Metadata

- ID: equality_bubble_transport_strictly_increases_quadratic_distance_from_the_switch
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 86
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For a fixed switch cut define Q as the sum of squared distances of all threshold defects from the cut. In an equality same-side bubble, two consecutive defects move to the two outer ranks. Q increases by 4 if all remain on one side and by 3 in the boundary-adjacent case. Therefore (E,-Q) strictly decreases throughout the pure same-side bubble dynamics. This does not by itself globalize cellular Tucker because arbitrary complementary-cell paths include other transport classes and Tucker does not force an E-minimal cell.

## Development

Fix a ternary switch state with cut between window ranks k and k+1. For a defect at rank r define its nonnegative distance from the switch by
d_k(r)=k-r for r<=k,
and
d_k(r)=r-(k+1) for r>=k+1.
Let
Q_k=sum_{r defective} d_k(r)^2.

Consider the same-side violation-to-satisfaction bubble of the threshold-energy theorem. Its two central defects at consecutive ranks i,i+1 disappear. In the equality case exactly two outer defects are created at ranks i-1 and i+2.

If all four ranks lie on the same side of the cut, write d=d_k(i) on the left side. Then the old distances are d,d-1 and the new distances are d+1,d-2. Hence
[(d+1)^2+(d-2)^2]-[d^2+(d-1)^2]=4.
The right-side calculation is identical after reflection.

If the new outer rank crosses the cut, the central pair is adjacent to the switch. Up to reflection the old ranks are k-1,k, with squared distances 1,0, while the new outer ranks k-2,k+1 have squared distances 4,0. Thus Q_k increases by 3.

Therefore every equality same-side bubble strictly increases Q_k, by 4 away from the switch and by 3 in the boundary-adjacent case. A strict threshold-energy improvement lowers E; an equality bubble preserves E and strictly raises Q_k.

Since Q_k is bounded on a finite order, repeated equality bubbles with one fixed cut cannot cycle. In particular, inside any dynamics where every non-strict step is genuinely of the same-side bubble class and the cut is fixed, the lexicographic potential
(E,-Q_k)
strictly decreases.

Scope. This does not yet globalize the cellular Tucker theorem. An arbitrary complementary-cell path also permits neighbor-replacement transports, endpoint transports, vertical cut moves, and switch-crossing moves that may change k. Nor does Tucker force its complementary cell to lie in an E-minimal sublevel. Thus Q_k closes the old same-side equality-cycle gap only for that repair class; a global topological descent requires either compatible potentials for the other classes or a filtered/equivariant argument that forces Tucker inside an extremal subcomplex.
