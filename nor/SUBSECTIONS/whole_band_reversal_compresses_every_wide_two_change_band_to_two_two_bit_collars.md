# Whole-band reversal compresses every wide two-change band to two two-bit collars

## Metadata

- ID: whole_band_reversal_compresses_every_wide_two_change_band_to_two_two_bit_collars
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 275
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Whole-band reversal compresses an arbitrary two-change band to two two-bit boundary defects

Let
pi=(v_1,...,v_n)
have ternary word
0^A 1^B 0^C
with A,B,C>=1.

The middle 1-run occupies window ranks A+1,...,A+B. Its exact supporting coordinate interval is
Z=(v_{A+1},...,v_{A+B+2}).
Reverse Z and leave every coordinate outside Z fixed.

Every ternary window wholly inside Z is the reversal of an old 1-window, so by reversal oddness it now has color 0. Every window wholly outside Z is unchanged and already has color 0.

Only windows crossing the two ends of Z can change. When the relevant exterior coordinates exist, these are exactly two on each side:
L_0=alpha(v_{A-1},v_A,v_{A+B+2}),
L_1=alpha(v_A,v_{A+B+2},v_{A+B+1}),
R_0=alpha(v_{A+2},v_{A+1},v_{A+B+3}),
R_1=alpha(v_{A+1},v_{A+B+3},v_{A+B+4}).

Hence the reversed full word is
0^(A-2), L_0,L_1, 0^B, R_0,R_1, 0^(C-2),
with the obvious endpoint clipping when A<2 or C<2.

Therefore an arbitrarily wide isolated band is converted, in one explicit full-support move, into two defect clusters of width at most two separated by a monochromatic zero bridge of length B.

Consequences:
1. If either boundary cluster is 00 and the other is nonzero, the resulting full order has exactly one isolated 1-band of width at most two.
2. If both clusters are 00, the resulting order is monochromatic and NOR closes.
3. If both clusters are nonzero, all remaining variation is confined to two bounded collars; the entire length-B middle interval is solved and frozen.
4. The construction uses only reversal oddness and applies before any flat/full curvature analysis.

For the coboundary-flat Article III route, singleton and width-two local packets are already reduced to NOR or a protected-root handoff. Thus every wide two-change band admits a direct reduction to two bounded collar defects connected by a solved monochromatic bridge. The remaining theorem is a two-collar gluing/extraction statement, rather than any further wide-band classification.

## Frontier

- Development version when composed: None
- Development version now: 1
