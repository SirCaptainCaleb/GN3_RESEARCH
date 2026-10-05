# Saturated natural carriers force their outward loci to be contractible

## Metadata

- ID: saturated_natural_carriers_force_their_outward_loci_to_be_contractible
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 120
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

### Saturated carriers impose a real acyclicity requirement

If a carrier contains every outward subface of a face \(F\), then any same-face natural carried extension over \(F\) forces the outward locus \(F\cap X_{r+1}\) to be nonempty and contractible. Since protected zero faces can have disconnected or circular outward loci, a universal same-face natural-carrier theorem is false. The remaining construction must either enlarge the target carrier, remove the obstructing cycle while preserving the index, or use additional boundary-tournament structure.

## Development

## Saturated natural carriers force contractibility

Fix a protected witness depth and put D(F)=F intersect X_{r+1}. Let Q be a poset of proper protected faces. Suppose F belongs to Q and every outward face G subset F also belongs to Q. Here “outward face” means G subset X_{r+1}, so D(G)=G.

**Theorem.** If a continuous map
\[
f:\Delta Q\longrightarrow X_{r+1}
\]
is carried by the natural loci D, meaning that a chain with largest face H maps into D(H), then D(F) is nonempty and contractible.

**Proof.** Nonemptiness follows by evaluating f at the vertex corresponding to F. The face poset of D(F) is a subposet of Q. Its order complex is the barycentric subdivision of D(F); denote the canonical homeomorphism to D(F) by j.

The restricted map f_0 on this order complex is homotopic to j as a map into D(F). Indeed, on a simplex with largest outward face G, both f_0 and j take values in G because D(G)=G. In the usual geometric realization of the permutahedron, the straight-line homotopy between them stays inside the convex face G. These homotopies agree across simplex boundaries and hence define a global homotopy in D(F).

Adjoining F to each outward face chain forms a cone over the entire barycentric subdivision of D(F), unless F itself is outward. In the outward case D(F)=F is already convex and contractible. Otherwise this cone is a subcomplex of Delta Q, and its image under f lies in D(F), since every cone simplex has largest face F. Thus f_0 is null-homotopic in D(F). Since f_0 is homotopic to j, the identity of D(F) is null-homotopic. A nonempty space with null-homotopic identity is contractible. ∎

**Corollary (exact criterion for a saturated natural-carrier construction).** Suppose Q is invariant under reversal and contains every outward subface of each of its faces. An equivariant D-carried map exists if and only if each D(F), F in Q, is nonempty and contractible.

Necessity is the theorem. Sufficiency is the standard inductive contractible-carrier construction: nestedness D(G) subset D(F) carries the boundary of each chain simplex into D(F), which is contractible; extend on antipodal pairs of proper face chains.

## Application to the persistent-label separator

Every outward face has both persistence indicators zero. Thus the full zero-face poset of [[persistent_face_labels_isolate_the_double_persistent_zero_root_locus]] automatically contains all outward subfaces of each zero face. The criterion therefore applies to the full persistent-label zero separator.

In [[arbitrary_terminal_pair_relations_occur_on_protected_zero_faces]], a zero face has D(F) homotopy equivalent to a circle. The theorem shows that no natural D-carried map exists on the full zero-face poset in that local example. The missing loop filling is forced, not merely an unfortunate choice of paths. The barycentric circle inside D(F) is coned off by the zero-face vertex F, so its image would have to bound inside D(F).

Likewise a disconnected D(F) already obstructs the one-skeleton: outward chamber vertices in distinct components are forced to map to themselves, yet their edges to the F vertex would have to lie in one component.

This does not contradict [[bounded_pair_reservoirs_reduce_natural_carrier_extension_to_the_two_skeleton]]. That theorem says higher extensions are automatic *after* a carried two-skeleton map exists. In a saturated sector the point and loop obligations can themselves force contractibility of all natural carriers.

## Strategic consequence

For the full Article VII separator, natural loci alone cannot be the universal target under only boundary antisymmetry and local protectedness. The remaining successful routes must either:
- enlarge target carriers beyond the source face, with proved protection and nesting;
- remove problematic zero-face cones while preserving the required equivariant index; or
- use an additional global hypothesis to rule out the obstructing local configurations.

A same-face outward chamber is not sufficient. This is a local obstruction to the proposed carrier construction, not a counterexample to the grand two-cover theorem.
