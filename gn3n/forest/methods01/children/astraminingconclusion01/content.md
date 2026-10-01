# Astra result-mining specialist conclusion

## Statement

Astra mining extracted reusable local-extension, insertion, compatibility, edge-order, cover-surgery, fractional-cover, and sharpness-fence mathematics; several additional Astra clusters remain promising for later abstraction.

## Body

## Durable extractions

New generalized results:
- fractionaldeletionfamilyavg01: deletion-family averaging for fractional path covers, removing minimum-counterexample assumptions from the Astra-001 averaging arguments.
- twocoverinseparability01: the general equivalence-class structure of pairs lying together in every two-cover.
- fivebadextensioncore01: for a Hamiltonian five-set X and t exterior labels whose six-set extensions are non-Hamiltonian, one deletion of X works Hamiltonianly with at least ceil(3t/5) exterior labels. This subsumes astra003fivecommoncore and astra003fivethreeendpoints.
- targetsizeinsertion01: absence of a target component-size profile forces noninsertability into any deletion-cover component whose one-vertex enlargement would realize that profile. This strips minimality from astra002paritybarrier01.
- balancedcompatglue01: pairwise compatible balanced deletion covers have a parity-determined global two-cover size profile, stripping the counterexample hypothesis from astra002compatparity02.
- noninsertableorderdisagree01: if x is noninsertable into a displayed path P but P+x is Hamiltonian, every Hamilton order of the enlargement has order disagreement with P.
- twofourhamdeletions01: for a disjoint two-set S and Hamiltonian four-set P, at least two p in P make S union (P-p) Hamiltonian.

Already-general certified results rehomed into toolkits:
- ca8dc4ee0bde: defect-line/contiguous-path-number formula -> pathcalc01.
- astra004fourgooddisagree: four Hamiltonian deletions force order disagreement -> pathcalc01.
- 81882d24a52f: minimum-imbalance exchange barrier -> coversurg01.
- astra003internalrank: permanently-internal edge-ordered K4 rank classification -> edgeorder01.
- 17e36057be4b: mandatory-triple Hamilton-order rigidity -> coversurg01.
- 5c95da081ff4: synchronized cyclic support exchange or full-path noninsertability -> coversurg01.

A useful general result c82e8c6d3016 (three bad extensions of a Hamiltonian four-set force six mixed 5|3 repartitions) was deliberately not moved because it owns a line-specific descendant subtree. It is instead surfaced explicitly in the Atlas.

## Consolidation and discoverability

The Atlas now has focused entries for:
- fractional path-cover and LP tools;
- Astra-mined local utility lemmas;
- balanced-cover size and compatibility tools;
- mandatory-triple cover calculus;
- reusable negative/sharpness fences.

The support-only balanced-tree construction 9a0c84b2dcbe was moved to counterfence01. It shows that support incidence alone realizes essentially every balanced tree transversal, so support-only counting cannot eliminate the forest branch.

## Generality that stops

Several inspected statements remain genuinely line-specific because the needed local hypotheses are produced only by the route:
- astra003sixcorepair depends on the specialized six-core structure theorem, not merely on having several Hamiltonian deletions.
- the remainder of astra003fiveonepath beyond the extracted noninsertability/order-disagreement core still needs the five-side quadratic-minimum exchange setup.
- most order-eleven/order-thirteen omission-surface results use fixed-size reachability and should not be promoted as general tools.
- sharp-half-order support-graph conclusions that use minimum-counterexample deletion availability remain shell-specific, although their pure support-incidence sharpness constructions are useful fences.

## Promising unmined areas

A later specialist should inspect:
1. Astra-003 canonical five-bridge / synchronized six-set work for local statements that survive after deleting the fixed-order shell assumptions.
2. Astra-004 sharp-shell support-walk lemmas for abstract labeled-support graph statements separable from minimum-counterexample hypotheses.
3. Astra-010 comparison-flip criticality for general perturbation/critical-arc lemmas about orientations of comparison digraphs.
4. The mandatory-triple cluster beyond the already surfaced Atlas package; several statements are general but still live in the originating route to preserve its reasoning tree.
5. Compatibility-neighborhood and support-switch lemmas for hypotheses pc(H)>2 that may actually require only failure of one specified gluing/separation outcome.
