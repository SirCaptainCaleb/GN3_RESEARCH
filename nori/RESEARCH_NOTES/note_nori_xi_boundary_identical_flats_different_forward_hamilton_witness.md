# Boundary colorings with identical component flats but different monochromatic Hamilton status

- Stable ID: note_nori_xi_boundary_identical_flats_different_forward_hamilton_witness
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: boundary-tournament, graphic-flat, resource-selector, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

On four original vertices 0,1,2,3, index 12 reversal-pairs of ordered triples by increasing middle vertex, then ascending outer pair a<c, with reversed triple receiving complementary color. Two masks 0x5f and 0x55 define distinct legal reversal-odd colorings. Their red ordered-pair covering graphs have the SAME two connected components: A={(0,1),(0,2),(1,2),(2,0),(2,3),(3,0)} and B={(0,3),(1,0),(1,3),(2,1),(3,1),(3,2)}. Their graphic closure flats in M(S(K4)) therefore coincide: every internal covering edge in A or B belongs to both flats. Yet the mask 0x5f has no monochromatic spanning vertex-simple tight word among the 24 orderings, whereas mask 0x55 has four monochromatic spanning words, including (0,1,2,3). The result follows by enumerating the 24 words and checking their two consecutive triple colors, and by BFS in the red covering graph for each mask. Consequence: even the full monochromatic-component partition and the antipodal graphic flat F=cl_M(B) do not determine whether a forward monochromatic spanning tight path exists. The selected red edge-orbit basis B and original-vertex resource independence contain essential extra data. This finite obstruction does not address the spanning one-turn conjecture, which is trivial on four original vertices.
