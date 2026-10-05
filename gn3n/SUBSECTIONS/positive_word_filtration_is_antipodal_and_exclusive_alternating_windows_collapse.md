# Positive-word filtration is antipodal and exclusive alternating windows collapse

## Metadata

- ID: positive_word_filtration_is_antipodal_and_exclusive_alternating_windows_collapse
- Parent Section: local_witness_topology_and_the_finite_terminal_theorem
- Position: 10
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity", "positive_reflected_double_carriers_have_unbounded_local_spans", "audit_terminal_surgery_and_compression_use_different_witness_polarities", "spanning_orders_and_defect_helly"]

## Cold composition

(none yet)

## Development

## A consistent positive-word filtration and elimination of the twelve-position alternating residue

The polarity mismatch can be avoided without sacrificing antipodal equivariance.

Put
[
mathcal W_+={001,011,0101}.
]
For a status word (w), chamber reversal acts by reverse-complement:
[
wlongmapsto overline{w^{m rev}}.
]
Under this operation
[
001longleftrightarrow011,qquad 0101longleftrightarrow0101.
]
Hence (mathcal W_+) is invariant under the actual antipodal involution. A witness-selection/depth rule based only on positive forbidden occurrences can therefore be made antipodal. The negative words (110,100,1010) are not needed for equivariance; they were only an auxiliary compression device.

This matters because a local two-cover surgery is exactly adapted to (mathcal W_+): an order of the form (P,Q^{m rev}) avoids (mathcal W_+) internally by the exact inversion-window theorem. Thus the same predicate can be used for both protection and surgery.

The price is that the dual-polarity compression statements must be replaced by genuinely one-polarity arguments.

### Exclusive disjoint alternating windows cannot be adjacent

By [[exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity]], any genuinely exclusive disjoint terminal pair has adjacent determining windows.

For alternating witnesses each determining window has six vertex positions and four status positions. If the two six-vertex windows are adjacent, translate so that the two positive alternating occurrences start at status positions (1) and (7). The status segment has the form
[
0101,x,y,0101
]
up to reverse-complement symmetry, with (x,yin{0,1}).

There are four cases:
[
egin{array}{c|c}
(x,y)&	ext{strictly inward positive occurrence}\ hline
(0,0)&001	ext{ at start }6,\
(0,1)&0101	ext{ at start }3	ext{ (also at }5),\
(1,0)&011	ext{ at start }3,\
(1,1)&011	ext{ at start }3.
end{array}
]
Every displayed occurrence lies strictly between the two terminal starts. Therefore a protected carrier at the reflected alternating edge cannot realize adjacent disjoint exclusive alternating windows.

The same argument applies to the reverse-complement orientation, since (0101) is fixed by reverse-complement.

Consequently the order-twelve bound in [[exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity]] is never attained in the protected positive-word filtration:

**Positive exclusive-disjoint compression.**
A protected exclusive disjoint terminal carrier has only the span-two type, and its full determining support has order at most ten.

The local example [[positive_protection_allows_a_disjoint_single_sided_span_two_carrier]] shows that order ten is genuine and that this branch should be handled by finite surgery rather than declared impossible.

### What remains

This repairs the polarity consistency for the exclusive branch:
- protection uses only (mathcal W_+);
- terminal finite surgery uses only (mathcal W_+);
- antipodal reversal preserves (mathcal W_+);
- exclusive disjoint supports are bounded by ten.

It does not solve [[positive_reflected_double_carriers_have_unbounded_local_spans]]. When both reflected positive occurrences coexist in every chamber, the exclusive-indicator equation is unavailable and their determining windows may be arbitrarily far apart.

Thus the single-polarity frontier is now exactly the **reflected-double branch**, together with nested protected-carrier gluing after that branch is handled.
