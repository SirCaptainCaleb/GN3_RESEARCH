# Arbitrary terminal pair relations occur on protected zero faces — preserved pre-item development

## Every terminal ordered-pair relation occurs in a protected determining-window sector

Let B be any finite set of order k>=2 and let E be any loopless directed relation on B. Take n>=2k+9 vertices. Let F have B as its first ordered-partition block, occupying positions 1,...,k, and let every other block be a singleton. Write the next three fixed labels as z,z_1,z_2. Set a=k-1 and b=n-3-a; then b-a>=8.

Prescribe
\[
h(u,v,z)=\mathbf1_E(u,v)\quad(u,v\in B,\ u\ne v),
\]
and prescribe h(v,z,z_1)=1 for all v in B, h(z,z_1,z_2)=1. Prescribe every consecutive status starting at k+2 or later to be 0, uniformly over chambers of F. Internal triples of B are arbitrary.

These prescriptions are compatible with boundary antisymmetry. Reversing (u,v,z) produces (z,v,u), which is not another prescribed terminal-pair triple. The triples (u,v,z) and (v,u,z) have different middle labels and are therefore independently assignable. The other prescriptions use distinct boundary-reversal orbits. Assign the opposite values to reversed triples and fill the remaining orbits arbitrarily.

The left determining word at start a is
\[
\mathbf1_E(u,v),1,1,
\]
where (u,v) is the terminal pair of the B order. Thus the positive occurrence is absent exactly when (u,v) belongs to E. The right reflected window at b has word 000 and is always absent.

All statuses starting strictly inward of a have the form
\[
1,1,0,0,\ldots,0.
\]
Consequently neither 001 nor 011 nor 0101 occurs at an inward start. The face is protected at this reflected span-two depth. Possible witnesses entirely farther outward in B are unrestricted and do not affect this statement.

It follows that the same-face protected outward locus D(F)=F intersect X_{r+1} is exactly the terminal ordered-pair locus C_E. By [[terminal_ordered_pair_loci_have_the_homotopy_type_of_mutual_pair_clique_complexes]], its homotopy type is the clique complex of the mutual-pair graph.

In particular, choose k=4 and let E consist of both orientations of the four edges of a chordless four-cycle. Then D(F) is nonempty and connected, but
\[
D(F)\simeq S^1.
\]
Neither determining occurrence persists: the right one never occurs, and the left one occurs on nonedges but is absent on edges. Therefore F is a zero face of the persistent-label separator of [[persistent_face_labels_isolate_the_double_persistent_zero_root_locus]], in its neither-persistent branch.

This shows that replacing arbitrary tie labels by persistent face labels does not make the neither-persistent branch locally acyclic. Product splicing supplies an outward chamber; it does not supply a contractible carrier. The obstruction already occurs with a two-slot endpoint footprint, not only with a central three-block.

The construction is a local protected-face example. It is not asserted to be a counterexample to the grand two-cover theorem, nor to satisfy a hypothetical global positive deletion distance. A grand-closure argument may use such global assumptions to obtain larger target carriers or additional forcing. It must state and prove that additional step.
