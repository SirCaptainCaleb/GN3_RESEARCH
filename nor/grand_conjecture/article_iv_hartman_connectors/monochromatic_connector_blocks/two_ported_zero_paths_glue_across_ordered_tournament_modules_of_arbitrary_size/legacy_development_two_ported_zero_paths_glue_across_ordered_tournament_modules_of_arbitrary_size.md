# Two ported zero paths glue across ordered tournament modules of arbitrary size — preserved pre-item development

## Closure under ordered joins and strong-component reduction

Fix the flat split B→z→A→x and the representing shore tournament T=t[A]. A ported zero path is an ordered shore path with color zero on each consecutive triple and forward first and last ordered pairs when defined. An empty path is permitted as a member of a two-path cover.

LEMMA (ordered-join closure). Let H,K be disjoint shore subtournaments with H→K. Suppose H admits a cover by at most two ported zero paths (P_H,Q_H) and K admits a cover by at most two (P_K,Q_K), including empty paths as necessary. Then H∪K admits the ported two-path cover
P=P_H P_K, Q=Q_H Q_K,
with empty factors omitted.

PROOF. Only joins between nonempty constituent paths need checking. If P_H=(...,a,b) has at least two vertices and P_K=(c,d,...) at least two, then a→b, c→d, and H→K yield zero for the new ternary windows (a,b,c) and (b,c,d); these are transitive forward triangles. If either path is a singleton, only the corresponding applicable crossing window exists, and it is likewise a transitive forward triangle. Internal windows retain zero. Both external endpoint pairs are forward, inherited from the first and last nonempty constituents, or supplied by the uniform forward join for singleton factors. The identical proof applies to Q. QED.

THEOREM (ordered modular closure). Suppose T admits an ordered partition
A=H_1 ⊔ ... ⊔ H_k, H_i→H_j whenever i<j,
where every H_i has a cover by at most two ported zero paths. Then A admits two ported zero paths. The previously proved gluing theorem constructs a compatible zero connector on A∪{x,z} and the homogeneous-cut insertion lemma closes the full NOR instance.

PROOF. Iterate the ordered-join lemma. If the resulting cover has two nonempty paths P,Q, use P,x,z,Q. If only P is nonempty, use z,P,x, with the singleton/empty cases handled by their same three-coordinate signatures. Then insert this spanning compatible connector into a good B-order using the homogeneous-cut theorem. QED.

COROLLARY (strong-component localization). The strongly connected components of every tournament have a unique linear dominance order, since the condensation of a tournament is a transitive tournament. If each strong component admits two ported zero paths, then the full shore closes. In particular, if every strong component has at most six vertices, the full NOR instance closes for arbitrarily large |A|: by the existing six-vertex transitive bipartition theorem (connector-block §8), each component splits into at most two transitive subtournaments, whose forward orders are ported zero paths.

Thus any remaining whole-shore connector obstruction contains a strongly connected shore component of at least seven vertices that is itself not two-path-portable, and every minimal obstruction to *ported two-path cover existence* is a strongly connected tournament of size at least seven.

Additional consequence combining the source/sink-module absorption lemma (§45): if an inclusion-minimal compatible-connector obstruction A has more than one strong component, at least two strong components must fail to possess a ported zero Hamiltonian path. Otherwise, start with a proper-support compatible connector on the sole exceptional component (or with (z,x) if none), then absorb the other components, one at a time in dominance order from the adjacent ends, using §45. Each absorbed component remains an extreme dominating or dominated block relative to the current connector shore. This is a necessary obstruction condition rather than a proof of strong connectivity of minimal connector obstructions.

The theorem is size independent and reduces ported-cover construction to strongly connected tournament blocks; it strengthens the universal |A|≤6 shore bases to an unbounded family.
