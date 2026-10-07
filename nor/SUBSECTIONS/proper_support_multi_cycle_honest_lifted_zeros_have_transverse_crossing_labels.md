# Proper-support multi-cycle honest lifted zeros have transverse crossing labels

## Metadata

- ID: proper_support_multi_cycle_honest_lifted_zeros_have_transverse_crossing_labels
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 195
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Work in the pure alternating ternary sector with the honest switch-prism labels
(rho,s) in W direct-sum R.
Let a support-minimal positive lifted zero be genuinely multi-cycle, and let U be the set of physical coordinates incident with its support graph.

By the physical-cycle-rank theorem, every support edge lies on a directed cycle. Since every root carried by a refinement of one ordered-partition face is weakly forward in the face-block order, the endpoints of every directed cycle lie in one tied face block. Connectivity then puts every vertex of each connected support component in one tied block.

Because the zero is genuinely multi-cycle, its support contains directed cycles with nonzero side imbalance of both signs. For any such cycle C,
sum_{e in C}(rho_e,s_e)=(0,S(C)),
with S(C) nonzero.
Hence the linear span H of the lifted support contains the pure side direction (0,1).

Its physical projection is the incidence span of the support graph:
- W_U if the support graph is connected;
- the direct sum of the component type-A spaces if it is disconnected.
Therefore any honest lifted label whose physical root crosses from U to V minus U is transverse to H, independently of its side sign.

Assume U is a proper subset of V. We construct such a genuine violating-window label inside the same permutahedral carrier face.

Choose a support block B containing one support component and choose a coordinate w outside U. If w lies in B, place two distinct support coordinates u_1,u_2 consecutively followed by w inside a chamber refinement of B. If w lies outside B, use a coordinate in an adjacent nonempty face block outside U and place u_1,u_2 at the appropriate end of B so that
(u_1,u_2,w)
or its reversed-side analogue is one consecutive ternary window. In either case the first and last coordinates of the window lie on opposite sides of the physical support cut U | (V minus U).

Fix any admissible cut-state level of the same product carrier cell for which this window lies on one threshold side. The two chamber refinements obtained by swapping u_1,u_2 are both legal refinements of the same face and keep the window on the same threshold side. Alternation flips its color. Hence exactly one of the two orientations makes this window violate the fixed threshold target.

Use that violating state as an auxiliary subdivision vertex. Its honest lifted label has physical root either
e_{u_1}-e_w
or
e_{u_2}-e_w
(up to the mirrored orientation), and therefore its physical projection is not in the physical span of the original support. Thus the lifted label is transverse to H.

Cone the boundary of the support-minimal zero simplex to this genuine transverse state label. Projection modulo H excludes zero from every new cone simplex; old proper faces are zero-free by support minimality.

Therefore every genuinely multi-cycle support-minimal honest lifted zero with proper physical vertex support U is locally removable.

Consequently any nonremovable multi-cycle honest lifted circuit must use EVERY physical coordinate.

Combined with the physical cycle-rank theorem, the remaining full-support shapes are:
1. two disconnected simple cycles partitioning V (codimension one in the lifted target, already removable by the nearest-violation theorem);
2. a connected bridgeless bicyclic support spanning V, whose core is either a figure-eight or a theta graph.

Thus the only dimension-saturated honest-lifted obstructions are full-support connected bicyclic circuits.

## Frontier

- Development version when composed: None
- Development version now: 1
