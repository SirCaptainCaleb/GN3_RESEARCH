# Bounded pair reservoirs reduce natural carrier extension to the two-skeleton — preserved pre-item development

## Composition

(none yet)

## Development

## Bounded ordered-pair factors remove all extension obstructions above dimension two

Let Q be an antipodally invariant subposet of proper protected faces at one witness depth. For each F in Q let
\[
D(F)=F\cap X_{r+1}.
\]
Assume D(F) is nonempty and factors as a product of neutral permutahedra, one-variable endpoint-subset loci, and terminal/initial ordered-pair loci C_E whose reservoirs have order at most four. Different nonconstant determining tests must use independent factors; merely having small footprints does not imply this product hypothesis.

**Lemma.** Every connected component of D(F) has the homotopy type of a torus (including a point), and in particular has vanishing homotopy groups in every degree >=2.

**Proof.** The neutral factors and nonempty one-variable loci are contractible. By [[terminal_ordered_pair_loci_have_the_homotopy_type_of_mutual_pair_clique_complexes]], each pair factor has the homotopy type of a clique complex on at most four vertices.

For completeness, every connected component of a clique complex on at most four vertices is contractible or homotopy equivalent to a circle. If its graph is triangle-free, a connected component is a tree or the chordless four-cycle: on four vertices any additional edge in a four-cycle creates a triangle. Trees are contractible and the four-cycle is a circle. If the graph has a triangle, consider the possible fourth vertex. With zero neighbors in the triangle it is a separate point; with one neighbor it attaches an edge to the filled triangle; with two neighbors it attaches another filled triangle along an edge; with three neighbors the clique complex is a tetrahedron. Each connected component in these cases is contractible. This also includes components with fewer than four vertices.

A product component is therefore homotopy equivalent to a product of circles and contractible spaces. Tori have contractible universal covers and hence no homotopy groups above degree one. ∎

**Extension theorem.** Suppose an equivariant continuous map on the two-skeleton of Delta Q has already been constructed, carried by D in the following precise sense: a simplex F_0<...<F_j, j<=2, maps into D(F_j). Then this map extends equivariantly to all of Delta Q with the same carrier property.

**Proof.** The carriers are nested because G subset F implies D(G) subset D(F). Induct on simplex dimension j>=3. The boundary of a simplex with largest face F maps into D(F), since each boundary simplex has a largest face contained in F. Its boundary is a connected sphere S^{j-1}, so its image lies in one connected component of D(F). The lemma gives pi_{j-1}=0; consequently the boundary map extends over the simplex into that component. Perform extensions on antipodal simplex pairs and define the partner extension by reversal. Proper ordered-partition face chains have free reversal action, so there is no fixed simplex requiring an additional equivariant filling. The finite cellular induction completes the proof. ∎

This statement makes explicit when rank-two coherence suffices for higher extension. It is not the invalid claim that arbitrary rank-two repairs automatically yield a contractible higher carrier. Here the carriers are specified, natural, nested, and independently proved to have vanishing higher homotopy.

## Exact remaining obligations in this sector

1. Choose images of face vertices in D(F).
2. Join the images of comparable vertices inside the appropriate D(F); this requires compatible connected-component choices.
3. Fill each triangular chain loop inside D(F); when a pair factor contributes a circle, a loop with nonzero winding is a real obstruction and cannot be discarded.
4. Once these obligations are proved, every dimension >=3 is automatic by the extension theorem.

If Q is the complete persistent-label zero separator, the existing separator genus bound and this extension give the desired one-step protected genus inequality. If Q is only a sector, the conclusion is only an equivariant map Delta Q to X_{r+1} and the corresponding index bound for that sector. No full-separator coverage is asserted.

## Relation to the newest bounded-block and rooted-reservoir results

[[no_farther_witness_bounds_relevant_face_blocks_by_four]] bounds relevant source factors in a particular double-persistent, no-farther-witness setting. It does not by itself supply outward chambers or the product hypotheses above. A double-persistent face has empty same-face outward locus; it first needs an actual outward replacement. The rooted packet result [[two_slot_persistent_boundary_reservoirs_are_uniformly_blocked_and_rooted]] supplies endpoint-controlled packets but still needs the stated corridor handoff.

The current elevation therefore separates two genuine tasks: produce outward replacements on the double-persistent branch, and establish component/loop compatibility on the branch with outward choices. Whenever the latter branch has the bounded pair-factor structure above, no separate higher-dimensional coherence theorem remains.
