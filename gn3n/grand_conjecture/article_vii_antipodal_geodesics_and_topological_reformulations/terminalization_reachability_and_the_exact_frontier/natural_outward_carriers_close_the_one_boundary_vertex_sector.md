# Natural outward carriers close the one boundary vertex sector

## Composition

(none yet)

## Development

## A globally compatible extension on an explicit sector

Fix depth r in the positive witness filtration. Let Q be an invariant subposet of protected separator faces. Assume that for every F in Q:
1. the left and right determining windows are separated into independent face factors;
2. each occurrence indicator is either constant, or depends on a single vertex in a first or last position of one free face block; the remaining determining positions are fixed throughout F;
3. F contains an outward chamber.

The two variable blocks, when both indicators are nonconstant, belong to the independent left and right factors.

**Theorem.** There is an equivariant continuous map
\[
|\Delta Q|\longrightarrow X_{r+1}
\]
carried by D_r(F)=F intersection X_{r+1}. In particular the higher-dimensional extension on this sector needs no independently chosen normalization windows.

**Proof.** The product formula in [[separated_window_outward_loci_are_products_and_can_be_disconnected]] expresses D_r(F) as the product of the two single-sided absence loci and the neutral permutahedral factors. A constant occurrence indicator must be identically zero whenever an outward chamber exists; it therefore imposes no restriction. Each nonconstant single-vertex restriction is a prescribed first- or last-vertex locus C_S. Hypothesis 3 makes every required S nonempty. By [[prescribed_endpoint_subsets_of_a_permutahedron_give_contractible_outward_loci]], every factor is contractible. Hence D_r(F) is nonempty and contractible.

For G subset F,
\[
D_r(G)=G\cap X_{r+1}\subseteq F\cap X_{r+1}=D_r(F).
\]
Thus these loci are naturally nested, without any mask recomputation or comparison of independently selected repair orders. Reversal also gives D_r(tau F)=tau D_r(F).

Construct the map on the barycentric order complex inductively. Choose images of face vertices in their nonempty carriers. On a simplex corresponding to F_0 subset ... subset F_k, all its already mapped boundary simplices lie in D_r(F_k) by nesting. Contractibility supplies an extension over the simplex. Make choices on one representative of each antipodal pair and reverse them on the other. The action on proper-face chains is free, so this defines a continuous equivariant map. ∎

If Q is the entire depth-r separator poset, the separator genus bound gives
\[
\gamma(X_{r+1})\ge\gamma(X_r)-1.
\]
For a proper sector Q, the theorem gives only
\[
\gamma(X_{r+1})\ge\gamma(|\Delta Q|);
\]
the full separator's genus cannot be assigned to this sector without a separate argument.

This result handles unbounded boundary blocks with one varying determining position. It does not require a bound on their Coxeter rank. The cases with two or more variable determining positions and the cases without same-face outward chambers remain outside its hypotheses. In particular the nine-isolated-chamber example prevents extending the proof by replacing single-vertex conditions with arbitrary triple conditions.
