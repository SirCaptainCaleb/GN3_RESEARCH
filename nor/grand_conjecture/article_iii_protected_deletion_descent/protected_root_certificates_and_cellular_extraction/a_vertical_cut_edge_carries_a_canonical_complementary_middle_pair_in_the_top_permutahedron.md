# A vertical cut edge carries a canonical complementary-middle pair in the top permutahedron

## Composition

(none yet)

## Development

## Corrected local complementary-middle lemma

Work in ternary arity over the TOP permutahedron face, so every permutation of the physical coordinates is available in the same horizontal carrier face.

Fix one vertical switch-prism edge joining adjacent cut levels k and k+1. Let
W=(u,b,v)
be the ternary window whose rank is crossed by this vertical edge, and let
c=alpha(u,b,v).

At cut level k the window lies on one threshold side with target T. At cut level k+1 it lies on the opposite side with target 1-T.

There are two cases.

### Case 1: W violates at level k

Then c=1-T. The state with order containing W at level k carries the signed-middle violation b on the old side, with physical root
rho=e_u-e_v.

Reverse the local triple while keeping it at the same window rank. Because the horizontal face is the top permutahedron this chamber refinement is available in the same product cell. The reversed window
W^rev=(v,b,u)
has color 1-c=T by alternation and physical root -rho.

At cut level k+1 its target is 1-T, so W^rev violates there. Its side sign is the opposite one. Hence the same product cell contains the complementary pair
(rho,s) and (-rho,-s)
with the SAME physical middle b.

### Case 2: W is satisfied at level k

Then c=T. After crossing the vertical edge to level k+1, the unchanged window W has target 1-T and therefore violates, with label (rho,-s).

At level k, reverse the local triple. Its color is 1-T, so W^rev violates the old target T, with label (-rho,s).

Again the product cell contains exact complementary signed-middle violations with the same middle b.

### Lemma

For every vertical cut edge in the top permutahedron product cell, the ternary window whose rank is crossed by that edge canonically yields an exact complementary signed-middle pair in that SAME product cell, using the two orientations of the window at the two vertical endpoints.

This is the vertical-local version of the earlier complementary-middle idea. It does NOT require moving an arbitrary selected violation across many cut levels.

### Carrier-selection qualification

The lemma is a statement about genuine violating STATES available in the product cell. A single-valued selected-violation carrier uses it only if its selector actually chooses these boundary-window violations at the two required states.

For a set-valued/cellular Tucker carrier containing every available signed-middle violation, the pair is present automatically.

For a nearest-violation selector, the crossed window is cut-adjacent and therefore of minimum possible distance, but an explicit reversal-compatible tie rule is still needed if another equally near violation exists. Thus this lemma repairs vertical locality but does not by itself justify the selector-dependent conclusion of the current full-dimensional extraction claim.

### Consequence

The full-dimensional top-cell frontier is sharper than a long fixed-middle transport problem. The required complementary pair already exists on every vertical edge; the remaining issue is carrier inclusion/selection of that canonical pair. A closure route should therefore either:
- use the set-valued complementary-middle carrier directly on the top cell; or
- prove a nearest-violation tie rule/degree construction that retains one canonical vertical-edge pair.

Once such a pair is admitted by the carrier, the arbitrary complementary-cell extraction theorem hands it to the established Article III repair/threshold-band machinery.
