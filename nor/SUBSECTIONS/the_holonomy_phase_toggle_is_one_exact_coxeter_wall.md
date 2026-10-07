# The holonomy phase toggle is one exact Coxeter wall

## Metadata

- ID: the_holonomy_phase_toggle_is_one_exact_coxeter_wall
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 51
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

At the special perfect-blocker holonomy-flip interface, the two full-support orders
Pi_1=(x,a,b,d,c,e) and Pi_0=(x,a,d,b,c,e) differ by the single adjacent transposition of b and d. Their internal ternary words are respectively 1111 and 0000, while their ordered exterior attachment pairs are identical: (x,a) on the left and (c,e) on the right. Thus this Coxeter wall complements all four internal statuses and changes no exterior-crossing window.

For any one-change target whose cut lies outside the four internal ranks, exactly one side of this wall matches the constant target color throughout the packet. Therefore a maximal threshold-compatible band cannot terminate strictly inside this packet: the matching chamber weakly dominates the other and strictly enlarges compatibility once the band reaches the packet.

Scope: this is the special perfect-blocker branch only. The common attachment pairs (x,a),(c,e) are new pairs, not the original carrier pairs (a,b),(d,e); the theorem does not by itself give an old-boundary-preserving surgery. Its value is that the holonomy-flip interior is reduced to one exact phase-toggle wall and all remaining obstruction is pushed to its fixed reconnection packets.

## Development

## The holonomy phase toggle is one exact Coxeter wall

At the special perfect-blocker holonomy-flip interface, consider the two full-support orders

Pi_1=(x,a,b,d,c,e),
Pi_0=(x,a,d,b,c,e).

The first has internal ternary word 1111 and the second has internal word 0000. They have the same ordered first pair (x,a) and the same ordered last pair (c,e).

Moreover Pi_0 is obtained from Pi_1 by the single adjacent transposition of b and d, which occupy positions 3 and 4 in Pi_1.

Therefore this one Coxeter chamber wall has an exact effect:

- every ternary window meeting the exterior is unchanged;
- the four internal windows are all complemented simultaneously;
- no other status changes.

So the holonomy flip contains a codimension-one phase-toggle wall whose two sides realize the two constant words 1111 and 0000 with identical exterior reconnection data.

### Threshold-band consequence

Fix any one-change target whose cut lies outside these four internal ranks, so the target color is constant across the whole toggle packet. Exactly one of Pi_0,Pi_1 matches all four internal target statuses, while both have identical exterior statuses.

Hence, among the two adjacent chambers, the matching side weakly dominates the other for threshold-band length and strictly dominates it whenever the compatible band reaches any internal toggle rank.

Consequently a globally maximal threshold-band obstruction cannot stop strictly inside this four-window packet on a constant-color side. It must either

1. be blocked at one of the two fixed exterior reconnection packets before entering the toggle;
2. have the proposed threshold cut pass through the toggle packet itself; or
3. already use the matching phase.

In the special perfect-blocker construction the holonomy interface lies in the old zero phase, so for the inherited deletion threshold the relevant obstruction is pushed entirely to the fixed boundary reconnections.

This converts the six-set from a vague local weave into an exact one-wall phase switch compatible with the global threshold-band potential.
