# Polar seam turns and facet feedback necessity

- Stable ID: note_nori_xvii_polar_seam_positive_turn_feedback_r12094_2
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, polar-bypass, sensitivity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12094_2
- Updated session: session_nori_r12094_2
- Disposition: none
- Successor: none

## Related references

- subsection:directed_influence_components_and_monotone_seam_lifting

## Research note

For c antipodally odd, let W be a shortest red antipodal walk, length L=n+2k. For i<j put t=j-i. Any walk Q from u_i to bar(u_j) with t+length(Q)<L must have at least one blue-to-red adjacent turn. Indeed the antipodal walk formed by reversing the red W segment from u_j to u_i and appending Q has twisted defect D=1+2*number_of_blue_to_red_turns(Q). Defect one root-slides to a shorter monochromatic antipodal walk, contradiction. For a Hamming complementary geodesic Q, the length condition is equivalent to the chosen W interval having Hamming excess less than k. For a rank-two complementary face, both spanning two-edge paths must be blue then red, forcing both directional sensitivities to be one and square curvature zero. For a general cubical face F, absence of a red-then-blue spanning path at one root forces a directed cycle in the face sensitivity graph: if the graph were acyclic, take a direction with constant edge color; traverse it first if red, last if blue, and recurse. Thus all shorter polar bypass faces have directed feedback. As a full-class consequence, if the global sensitivity digraph becomes acyclic after deleting one direction i, then NORI1 holds: choose a red i-edge, find a red-then-blue spanning geodesic in its incident complementary facet by acyclic insertion, prepend the red bridge, and rotate the root to obtain a monochromatic full geodesic. Any hypothetical counterexample therefore has a directed sensitivity cycle in every facet and remains cyclic after deletion of every one direction. This is a necessary condition, not a proof, and the next forcing task is a projective compatible assembly of blue-to-red turn witnesses on all those faces.
