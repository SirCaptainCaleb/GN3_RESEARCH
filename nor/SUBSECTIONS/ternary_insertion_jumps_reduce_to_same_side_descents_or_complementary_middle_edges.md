# Ternary insertion jumps reduce to same-side descents or complementary middle edges

## Metadata

- ID: ternary_insertion_jumps_reduce_to_same_side_descents_or_complementary_middle_edges
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 173
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Ternary insertion-jump classification

Work in the pure alternating ternary sector; no tetrahedral flatness is assumed.

Let adjacent fixed-insertion states differ by
pi=(...,a,b,x,y,c,d,...)
and
pi'=(...,a,b,y,x,c,d,...).

Write the four affected colors before as U0,U1,U2,U3 and after as V0,V1,V2,V3, in rank order. Alternation gives
V1=1-U1 and V2=1-U2.

Assume pi has only pre-threshold defects and pi' only post-threshold defects relative to their inherited one-change targets.

If the inherited cut does not move, purity forces U1=U2=1 and V1=V2=0. Checking the cut position through the four-rank packet, one endpoint then has a monotone affected packet compatible with the unchanged outside 0-prefix and 1-suffix, hence is a spanning one-change order. Contradiction.

If the cut moves one rank to the right, the same purity constraints again force one endpoint to be globally one-change. Therefore a surviving jump moves the cut one rank to the left.

Up to reversal there are two target changes.

Case A: 0011 -> 0111.
Purity gives U2=U3=1, V0=0, and V2=0.
If U1=1, then the x-centered window (b,x,y) is a pre-switch violation and the x-centered window (y,x,c) is a post-switch violation. Thus the horizontal edge is complementary signed-middle for the same coordinate x.
If U1=0, badness forces U0=1, so U0U1=10 entirely on the old side: a same-side protected descent.

Case B: 0001 -> 0011.
Purity gives U3=1, V0=V1=0, hence U1=1.
If U2=1, the same x-centered pair gives a complementary signed-middle edge.
If U2=0, U1U2=10 is a same-side protected descent.

Therefore every adjacent pure-sign jump in a fixed insertion fiber for an alternating ternary orientation is either:
1. a protected 10 descent remaining on one threshold side; or
2. a complementary signed-middle edge for x crossing the threshold.

In the second case the existing complementary-edge theorem applies: horizontal swap followed by the one-rank cut move makes the two central windows phase-compatible; only the two outer packet windows remain uncontrolled.

Scope: this uses alternation under a single transposition and is not asserted for a general reversal-odd ternary label.

## Frontier

- Development version when composed: None
- Development version now: 1
