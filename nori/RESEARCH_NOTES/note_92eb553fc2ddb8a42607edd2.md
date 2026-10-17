# Cyclic turn traps: local minimum criterion and dimension-nine onset

- Stable ID: note_92eb553fc2ddb8a42607edd2
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, turn-energy, local-trap
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11300_1
- Updated session: session_nori_r11300_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For a coherent cube geodesic support O, let T(O) be the number of changes in its 2n-step antipodally complementary cyclic edge-color word. T is always 2 modulo 4; T=2 means O supports a monochromatic geodesic. The union of O and its n adjacent-exchange neighbors involves 3n independent antipodal edge orbits: per direction the original orbit and the two alternatives toggling a cyclic neighbor. A prescribed cyclic color word on O can be extended to a legal coloring with every neighbor having strictly more turns precisely when each monochromatic cyclic run has length at least three. Proof: exchanging adjacent directions replaces two neighboring color bits and their antipodes. The maximum increase in the local three-gap transition count is two when the original local transition count is zero or one, and zero otherwise; the new orbit choices of distinct neighbors are independent. Consequently for every odd s>=3 and n>=3s one can prescribe T(O)=2s and all neighbors T=2s+4. A second path with the same direction order rooted at e0+e2 uses no prescribed orbit in these dimensions, so set every edge of that path red, giving another support R with T(R)=2. Thus strict nonmonochromatic local minima first occur in dimension nine, with central first-half word 000111000. The all-dimensional proof and verifier are in attached files nori_strict_cyclic_turn_traps.md and nori_strict_turn_trap_verifier.py; checks passed for n=9,10,15,20,27. This precludes strict local turn descent as a universal NORI1 forcing argument.
