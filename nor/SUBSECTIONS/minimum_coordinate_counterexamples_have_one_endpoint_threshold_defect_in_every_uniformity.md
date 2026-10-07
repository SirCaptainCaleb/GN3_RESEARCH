# Minimum coordinate counterexamples have one endpoint threshold defect in every uniformity

## Metadata

- ID: minimum_coordinate_counterexamples_have_one_endpoint_threshold_defect_in_every_uniformity
- Parent Section: directed_nor_union_closed_bridge
- Position: 173
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Let h color ordered r-tuples of distinct coordinates and be odd under reversal. In a minimum coordinate counterexample, the minimum number of disagreements with a one-change threshold target is one, and an endpoint-defect witness exists: a good single-coordinate deletion order retains all its windows when the omitted coordinate is appended. A monochromatic deletion order would immediately extend to a good full order, so every good deletion witness is bichromatic. This holds in every translation-invariant coordinate arity r>=2, but does not automatically extend to basepoint-dependent cube colorings. In the alternating ternary sector a same-side violation-to-satisfaction bubble starts with two central defects, so no such edge leaves an E=1 state.

## Development

Let h be a binary coloring of ordered r-tuples of distinct coordinates, r>=2, odd under reversal. A good full order is one whose consecutive r-tuple word changes at most once. Assume a counterexample on V of minimum cardinality in this class, and put M=|V|-r+1.

Theorem. The minimum number E of disagreements with a one-change threshold target, minimized over full orders, cut positions, and polarities, is one. There is an E=1 witness with the defect at an endpoint window. Every good order of every single-coordinate deletion is genuinely bichromatic.

Proof. Delete any x. Minimality gives a good order O of V minus {x}. Appending x adds precisely one new r-window and preserves the other M-1 windows. Extend a threshold target for O over the new endpoint. Thus E<=1. E=0 would solve the full instance, hence E=1. The preserved M-1 windows form a contiguous matched band, so the maximal possible contiguous matched-band length is M-1; a matched band of this length leaves an endpoint window outside it. Prepending x gives the analogous statement at the other endpoint.

If a deletion order had constant word, appending x would leave a constant prefix followed by one arbitrary bit, hence at most one change. Therefore no deletion good order is monochromatic. In particular M>=3. For a bichromatic deletion word eta^p (1-eta)^q, failure of prepending forces the new first window to have color 1-eta; failure of appending forces the new last window to have color eta. This is an endpoint-singleton two-change normal form. No tetrahedral flatness is needed.

This theorem concerns translation-invariant coordinate labels, not unrestricted basepoint-dependent N_k. Deleting a coordinate in that latter model does not automatically preserve the required antipodal rule on a fixed slice.

Additional ternary observation. In the alternating sector, a same-side violation-to-satisfaction bubble edge of §§143-144 has TWO old central violations: alpha(a,b,c)=alpha(b,c,d)=1-eta. Consequently such an edge cannot start at an E=1 state. The energy/moment argument of §156 remains valid for its stated edge type, but that edge type is unavailable at a globally minimum-energy counterexample state. A carrier argument must therefore explain how it reaches or stays within the E=1 locus; acyclicity elsewhere alone does not finish extraction.

Strategic use: concentrate on the one endpoint defect and the two changed boundary packets. An unrestricted multi-barrier normal form is unnecessary for a minimum coordinate counterexample.
